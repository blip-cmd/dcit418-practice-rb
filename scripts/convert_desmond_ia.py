#!/usr/bin/env python3
"""
Parse and convert Desmond's 77-question IA exam review to parser format.

Reads:
  - data_files/received_qus/desmond_dcit418_ia.md (77 questions, no source
    explanations; one corrupted question with a fully lost stem/options was
    stripped from the source during cleanup, see the note at the top of that
    file)

Outputs:
  - data_files/ia_bank/desmond_clean.md (parser format, with original
    explanations written here since the source had none)
  - data_files/ia_bank/DESMOND_IA_FORMATTED.md (human-readable review copy,
    matching the CHRIS_IA_FORMATTED.md convention)
"""
import re
from pathlib import Path

# One explanation per question, written from scratch since the source PDF
# extraction carried no "Explanation:" text at all, only the bare answer.
EXPLANATIONS = {
    1: "A symmetric cipher uses one shared key for both encryption and decryption; an asymmetric cipher uses a mathematically linked key pair, a public key for encryption and a private key for decryption.",
    2: "Kerberos authenticates users through a trusted Key Distribution Center (KDC) that issues time-limited tickets encrypted with symmetric keys, so neither party ever transmits a password over the network.",
    3: "An LCG's next output is a simple linear function of its previous state, so observing a handful of outputs lets an attacker solve for the generator's parameters and predict the rest of the sequence; a block-cipher-based PRNG's output is only as predictable as the cipher itself, which resists exactly this kind of algebraic recovery.",
    4: "Fermat's Little Theorem underlies the correctness proof that raising a ciphertext to the private exponent recovers the original plaintext modulo a prime; RSA generalizes this to a composite modulus via Euler's Theorem, but the same modular-exponentiation identity is what guarantees decryption undoes encryption.",
    5: "RC4's keystream exhibits statistical biases, most notably in its early output bytes, that let attackers recover plaintext or key material given enough ciphertext, which is why it has been deprecated for use in TLS and WEP.",
    6: "XTS-AES mixes a per-sector tweak into each block so that identical plaintext blocks in different sectors, or at different offsets, encrypt to different ciphertext, defeating the pattern leakage of a plain block cipher; despite this, XTS still permits some malleability within a sector, since the tweak does not chain block to block the way CBC's IV does.",
    7: "ESP encrypts and optionally authenticates the payload, giving both confidentiality and integrity, while AH only authenticates the packet (including parts of the IP header) and provides no encryption at all.",
    8: "A Kerberos ticket bundles a session key together with a short validity window and cryptographic proof of the KDC's involvement, so a stolen ticket is useless once it expires, unlike a raw shared password that remains valid indefinitely if leaked.",
    9: "DKIM cryptographically verifies that a message's headers were signed by the claimed sending domain, but it says nothing about who actually wrote the content or whether the visible \"From\" address matches the recipient's expectation, so it cannot fully replace end-to-end content encryption and authentication like PGP.",
    10: "SHA-3's sponge construction lets a designer tune the ratio between the rate and the capacity, and a hash function's preimage resistance scales with capacity, giving SHA-3 headroom that a fixed Merkle-Damgard chain like SHA-2 lacks; that same fixed chaining is also what makes SHA-2 (without a construction like HMAC) susceptible to length-extension.",
    11: "RC4's key scheduling algorithm initializes its internal permutation from the key in a way that leaves statistical correlations between the key and the first few keystream bytes, which is the flaw that enabled practical key-recovery and plaintext-recovery attacks such as those exploited against WEP.",
    12: "A transposition cipher only rearranges plaintext characters, so the same letters (and their frequency distribution) remain in the ciphertext; a chosen-plaintext attacker who controls the input can still recover the permutation, whereas a modern block cipher's rounds of substitution and permutation destroy that structural correspondence entirely.",
    13: "Schnorr signatures are built directly around a simple, provably secure sigma protocol and produce a single compact (challenge, response) pair, whereas NIST's DSA requires an extra modular inversion step and, in its classic form, cannot be batch-verified or trivially made non-malleable the way Schnorr's linear structure allows.",
    14: "The Enigma's rotors implemented a polyalphabetic substitution that changed with every keystroke, and combining several rotors (plus a plugboard) multiplied the number of possible wirings into the billions, making the cipher far harder to break by hand than a fixed monoalphabetic or single-rotor substitution.",
    15: "HMAC's outer hash re-hashes the inner digest together with the secret key, so an attacker who only sees the tag cannot invert the outer layer to recover any information that would let them forge a valid tag for a different message, unlike a naive secret-prefix MAC that is vulnerable to length-extension.",
    16: "TLS 1.3 removed static RSA key exchange and mandates ephemeral Diffie-Hellman, so a compromise of the server's long-term private key cannot be used to decrypt previously recorded sessions; RSA key exchange in TLS 1.2 offered no such forward secrecy, since every session key was derived from the same static private key.",
    17: "Each additional rotor multiplies the number of possible wirings and scrambling patterns, exponentially expanding the effective key space and making the letter-by-letter substitution pattern change far more often, which frustrates the frequency and pattern analysis that broke simpler single-rotor or non-rotor ciphers.",
    18: "ShiftRows cyclically shifts each row of the AES state by a different offset, moving bytes between columns so that MixColumns, which only mixes within a column, ends up mixing data that originated in different columns across rounds, providing diffusion across the whole block.",
    19: "GCM derives its keystream and authentication tag from a nonce that must never repeat under the same key; reusing a nonce lets an attacker XOR two ciphertexts to cancel the keystream, exposing the plaintext relationship and letting them forge valid authentication tags.",
    20: "Shor's algorithm on a sufficiently large quantum computer would efficiently factor RSA moduli or solve the discrete-log problem underlying most asymmetric schemes, breaking the hard problems public-key distribution currently relies on, which is why key exchange must migrate to post-quantum, quantum-resistant algorithms.",
    21: "More Feistel rounds increase resistance to differential and linear cryptanalysis by compounding diffusion and confusion, but each extra round also adds a full pass of computation, so doubling DES's 16 rounds to 32 would meaningfully strengthen it against known attacks at the cost of roughly doubling encryption and decryption time.",
    22: "Because RC4's key scheduling leaves biases in its earliest keystream bytes, and SSL/TLS re-keyed RC4 for every new record using a related key, those early biased bytes were repeatedly exposed across many sessions, which is exactly the weakness attacks like BEAST exploited to recover plaintext.",
    23: "Miller-Rabin is a fast probabilistic test that repeatedly checks a candidate against random witnesses; a composite number fails at least one witness's test with high probability, so a handful of rounds gives extremely high confidence a large candidate for RSA's p and q is actually prime without the cost of a deterministic proof.",
    24: "AddRoundKey is a simple bitwise XOR between the state and the round key, which is linear and introduces no nonlinearity; AES's security instead comes from combining this key-dependent step with the nonlinear SubBytes transformation elsewhere in the round, so together the cipher is both key-dependent and nonlinear.",
    25: "A block-cipher-based PRNG (as in counter-mode generation) produces its output by encrypting successive counter values, so predicting the next output requires breaking the underlying cipher; if the cipher's key were weak or recoverable, an attacker could reproduce the entire keystream, making the PRNG's unpredictability entirely dependent on the cipher's own strength.",
    26: "Skipping MixColumns in the final round lets AES decryption begin by simply inverting AddRoundKey and then the other transformations in reverse order without needing a MixColumns step whose only purpose would be to mix data that no further round will use, so security is unaffected while the structure stays symmetric between encryption and decryption.",
    27: "Round constants (Rcon) are XORed into the key schedule at specific points so that otherwise-identical or symmetric key material does not produce repeating patterns in the derived round keys, which closes off slide-attack style shortcuts that exploit self-similarity between rounds.",
    28: "Kerberos relies on fast symmetric encryption and a trusted third party (the KDC) that both sides already share a key with, which is far cheaper computationally than setting up and verifying asymmetric key pairs for every session, making it efficient inside a single trusted realm such as a corporate network.",
    29: "A transposition cipher only reorders the plaintext letters, so the ciphertext still contains the same letter frequencies as the original language; a cryptanalyst can use frequency analysis, or simply anagram short blocks, whereas a substitution cipher used alone has already broken that direct letter-count correspondence within a block.",
    30: "S/MIME's use of X.509 certificates ties every signature and encryption key to a certificate authority-verified identity, giving strong, centrally-verifiable trust, but that same reliance means users need a working PKI, certificate issuance and revocation infrastructure to participate, which is considerably more overhead than PGP's decentralized web of trust.",
    31: "OFB generates its keystream by repeatedly encrypting the previous keystream block rather than the ciphertext, so a bit error in one transmitted ciphertext block only corrupts the corresponding plaintext bits and does not propagate into later blocks, unlike CBC or CFB where an error in one block corrupts the next.",
    32: "CCMP is built around AES in counter mode with CBC-MAC for authenticated encryption, giving both confidentiality and integrity with a strong cipher, whereas TKIP was a stopgap that patched the original WEP design around RC4, inheriting much of RC4's key-scheduling weakness.",
    33: "AES key expansion derives a distinct round key for every round from the original cipher key using a combination of word rotation, S-box substitution and round constants, so each round applies different key material even though only one key was ever supplied.",
    34: "CTR mode turns a block cipher into a stream cipher by encrypting successive counter values to form the keystream; the counter must never repeat under the same key, because a repeated counter value produces the same keystream block twice, and XORing the two resulting ciphertexts cancels the keystream and exposes the XOR of the two plaintexts.",
    35: "RSA decryption's correctness (that raising a ciphertext to the private exponent recovers the plaintext) is proved using Fermat's Little Theorem for prime moduli, generalized by Euler's Theorem to RSA's composite modulus n = p times q, which is why the primality of p and q during key generation matters so much.",
    36: "A Certificate Revocation List lets relying parties check whether a certificate was invalidated before its natural expiry, for example after a private key is compromised, which is essential because a certificate's validity period alone cannot account for a key being stolen partway through its lifetime.",
    37: "The Ticket-Granting Ticket is itself encrypted under the KDC's own long-term master key, so if that master key is ever compromised, an attacker can forge or decrypt any TGT (and therefore any session key derived from it) for any user in the realm, making the KDC a single point of catastrophic failure.",
    38: "X.509's hierarchical trust model lets a small set of trusted root certificate authorities delegate signing authority to intermediate CAs, so relying parties only need to trust a manageable set of roots while still being able to verify certificates issued by many different organizations down the chain, which is what lets PKI scale to the whole internet.",
    39: "The AES key schedule mixes round constants and a nonlinear S-box substitution into every generated round key, so two related input keys produce round keys that diverge unpredictably rather than differing by the same simple relationship throughout, which is what defeats related-key cryptanalysis.",
    40: "Schnorr signatures need only a single scalar multiplication and a linear combination to verify, and their structure allows batching and aggregation, so on an elliptic curve group they produce shorter signatures with less computation than schemes like ElGamal or classic DSA that require more modular exponentiations.",
    41: "SubBytes replaces each byte of the state with the output of a fixed S-box built from multiplicative inversion in GF(2^8) followed by an affine transformation, and that inversion step is not expressible as a linear function of the input, which is exactly what makes the transformation nonlinear and provides AES's confusion.",
    42: "WPA2 (IEEE 802.11i) replaced WEP's weak RC4-based encryption and static keys with AES-CCMP and a proper key-management handshake that derives fresh session keys, closing the keystream-reuse and key-scheduling weaknesses that made WEP trivially breakable.",
    43: "Rotor machines like the Enigma are no longer used for real security, since modern computers can brute-force their comparatively small key space in a fraction of a second, but they remain historically significant as the first widely deployed electromechanical implementation of a complex, frequently-changing polyalphabetic substitution.",
    44: "PGP establishes trust through a decentralized web of trust where users vouch for each other's keys directly, while S/MIME relies on a hierarchical PKI of certificate authorities to bind identities to keys, so the two differ mainly in who is trusted to vouch for a public key rather than in the cryptography they use.",
    45: "OCSP lets a client query a certificate's status in real time against the issuing authority, whereas a CRL is a list published and refreshed only periodically, so a certificate revoked moments after the last CRL update would still appear valid to a client checking only the CRL, a gap OCSP closes.",
    46: "Federated identity management lets a user authenticate once with a trusted identity provider and then access multiple independent services without re-entering credentials at each one, since the relying services accept a signed assertion from the identity provider instead of managing their own password databases.",
    47: "AES arithmetic treats each byte as an element of GF(2^8), and multiplication in that field must be reduced modulo an irreducible polynomial so the result always stays within the 256-element field; x^8 + x^4 + x^3 + x + 1 was the specific irreducible polynomial chosen by the Rijndael designers to define that field's multiplication.",
    48: "Schnorr signatures reduce verification to a single linear equation in the exponent, which needs only one multi-exponentiation, whereas ElGamal-style signatures require more separate exponentiations and a modular inverse, so the Schnorr construction's simpler linear combination yields both smaller signatures and faster verification.",
    49: "Elliptic curve cryptography's underlying hard problem, the elliptic curve discrete logarithm problem, has no known sub-exponential attack the way integer factorization does for RSA, so ECC reaches equivalent security with far smaller key sizes, for example a 256-bit ECC key roughly matching a 3072-bit RSA key.",
    50: "X.509 defines a standard structure that cryptographically binds a public key to a verified identity (and other attributes) and is signed by a certificate authority, giving every application a common, interoperable format for exchanging and verifying that binding, which is the basic building block PKI is built on.",
    51: "ECDSA achieves the same security level as RSA-PSS with much smaller keys and faster signing, which matters directly on resource-constrained devices, but it does require the implementer to pick a well-vetted curve, since a poorly chosen curve can introduce subtle weaknesses that RSA's simpler modulus-based structure does not share.",
    52: "Each Schnorr signature must use a fresh random nonce, since the private key can be algebraically derived from just two signatures that reused the same nonce on different messages, exactly as happened in several real-world key-recovery incidents caused by reused or predictable nonces.",
    53: "HMAC folds the secret key into both an inner and an outer hash computation (nesting the hash rather than simply prepending the key once), so an attacker who observes a valid tag cannot extend the message and compute a new valid tag the way they could against a hash function used with a naive secret-prefix construction.",
    54: "Triple DES applies the DES algorithm three times in sequence to get an effective key strength beyond a single DES pass, but DES's 64-bit block size and relatively simple Feistel round function were never designed for speed at modern data rates, so three full passes of that structure make 3DES noticeably slower than AES's single, hardware-optimized rounds at comparable security.",
    55: "A point of low order on a poorly chosen or non-validated curve can let an attacker submit a maliciously crafted point that leaks information about the private key through an invalid-curve attack, which is why implementations must validate that received points actually lie on the intended, non-singular curve.",
    56: "SHA-3's sponge construction lets its security level be tuned by the split between the rate (how much data is absorbed per permutation) and the capacity (the hidden internal state); increasing the capacity raises resistance to collision and preimage attacks at the cost of processing less data per permutation call, so there is a direct security-versus-throughput trade-off.",
    57: "A 96-bit nonce in GCM is the recommended size because it lets the internal counter be derived directly and efficiently without an extra hashing step, but exactly like any GCM nonce, reusing it under the same key catastrophically breaks both confidentiality and the authentication tag, so the efficiency gain comes with the same strict never-reuse requirement as any other nonce length.",
    58: "A secure cryptographic hash function must be preimage resistant (given a hash, it should be infeasible to find any input producing it), alongside second-preimage and collision resistance, since without preimage resistance an attacker could work backward from a stored hash to recover the original input.",
    59: "CBC requires an unpredictable IV for every message because a predictable or reused IV lets an attacker test guesses about the plaintext of the first block (enabling chosen-plaintext style attacks), whereas CTR mode only requires its counter to be unique, not unpredictable, making CTR's requirement strictly weaker and easier to satisfy correctly.",
    60: "ECDSA relies on the elliptic curve discrete logarithm problem, which has no known sub-exponential attack, so it reaches equivalent security to RSA-PSS with much smaller keys, faster signing, and smaller signatures overall.",
    61: "HMAC combines a hash function with a secret key by nesting the key into both an inner and outer hash computation, so verifying a tag proves both that the message was not altered (integrity) and that it was produced by someone holding the shared key (authentication).",
    62: "A sufficiently powerful quantum computer running Shor's algorithm would efficiently factor RSA's modulus, breaking it outright, whereas the same algorithm applied to elliptic curve discrete logarithms still runs in polynomial time but against a smaller problem, so ECC's practical response is to move to substantially larger curve sizes rather than being broken as completely as RSA.",
    63: "MixColumns treats each column of the AES state as a vector and multiplies it by a fixed matrix over GF(2^8), mixing the four bytes within a column so that a single changed input byte affects multiple output bytes; it is omitted from the final round purely because any further mixing at that point would need to be undone by an extra step during decryption for no additional security benefit.",
    64: "In GF(p), the modulus p (required to be prime) defines the size of the field and guarantees that every nonzero element has a multiplicative inverse, which is the property that makes GF(p) a field rather than merely a ring, and is essential for the modular arithmetic RSA, Diffie-Hellman and related schemes depend on.",
    65: "The DES S-boxes were specifically designed with difference distribution tables that suppress high-probability differential characteristics, giving strong resistance to differential cryptanalysis; the same design goals were not applied against linear cryptanalysis, which was only formalized years later, leaving DES comparatively more exposed to that specific attack.",
    66: "Collision resistance means it should be infeasible to find any two distinct inputs that hash to the same output; without it, an attacker could substitute a malicious document for a legitimate one that shares the same hash, defeating any scheme (such as digital signatures) that relies on the hash to uniquely represent the original data.",
    67: "RSA uses modular exponentiation as the encryption and decryption operation itself, transforming a message directly into ciphertext and back; Diffie-Hellman instead uses modular exponentiation only to let two parties each compute the same shared secret from their private exponents, which is then used to derive keys for a separate encryption step.",
    68: "IEEE 802.1X is a port-based network access control standard that decides whether a device is allowed onto the network at all, while EAP is a general authentication framework that 802.1X uses to carry the actual credential exchange, so 802.1X is the gatekeeper and EAP is the protocol it speaks to the gatekeeper.",
    69: "A rail fence cipher writes the plaintext diagonally across a fixed number of rows in a zigzag and reads it off row by row, while a columnar transposition cipher writes the plaintext into a rectangular grid and reads the columns off in an order defined by a keyword, so both are transpositions but use different geometric patterns to reorder the letters.",
    70: "IKE is the protocol IPsec uses to authenticate the two endpoints and negotiate the shared keys and security parameters (the security associations) that ESP and AH will later use to actually protect traffic, so IKE handles setup while ESP and AH handle the ongoing data protection.",
    71: "Because MixColumns is skipped in AES's final round, decryption can start by inverting AddRoundKey and then directly undo the other transformations without needing an extra InvMixColumns step at that boundary, keeping the decryption process a clean mirror of encryption without wasted computation.",
    72: "CCM processes the plaintext twice, once for encryption and once for the CBC-MAC authentication pass, so its two-pass, sequential design cannot be parallelized; GCM instead computes its authentication tag using a fast, parallelizable multiplication in GF(2^128) alongside CTR-mode encryption, giving it a real throughput advantage in constrained or high-speed environments.",
    73: "A prime modulus in GF(p) guarantees every nonzero element has a unique multiplicative inverse, which is what makes GF(p) a field; with a composite modulus, some elements share common factors with the modulus and have no inverse, and knowing the modulus's factorization (as in RSA's n) is exactly what lets an attacker break the cryptosystem.",
    74: "A non-singular elliptic curve has a well-defined group structure where every point addition behaves consistently, which the security proofs for ECC rely on; a singular curve loses that structure at certain points, and an attacker can exploit those singular points to reduce or entirely break the discrete logarithm problem through what is known as a point factorization or singular-curve attack.",
    75: "AES bytes are treated as elements of the finite field GF(2^8), whose well-defined addition (XOR) and multiplication (polynomial multiplication modulo an irreducible polynomial) give SubBytes' S-box construction and MixColumns' matrix multiplication a consistent, invertible algebraic structure to operate over.",
    76: "Kerberos tickets and authenticators are timestamped and cached briefly by the server that receives them, so a captured ticket that an attacker tries to reuse (a replay attack) is detected and rejected because it either falls outside the valid time window or matches an authenticator the server has already seen.",
    77: "GCM computes its authentication tag using fast, parallelizable finite-field multiplication alongside CTR-mode encryption, so both encryption and authentication can be pipelined across multiple cores or hardware lanes, giving it better throughput than CCM's sequential two-pass design for the same underlying security guarantees.",
}


def parse_desmond() -> list[dict]:
    """Parse desmond_dcit418_ia.md's raw PDF-extracted text into structured
    questions. The source has no explanation text and irregular, sometimes
    reset, question numbering, so the parser tracks state by position (blank
    line, question stem, four options, one answer line) rather than trusting
    the printed numbers, and only accepts an option boundary once the stem
    has been fully collected."""
    path = Path("data_files/received qus/desmond_dcit418_ia.md")
    text = path.read_text(encoding="utf-8")
    text = text.replace("’", "'").replace("‘", "'")
    lines = text.split("\n")

    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "DCIT418 AI":
            start = i + 1
            break
    lines = lines[start:]

    def is_new_question_start(line: str):
        return re.match(r"^(\d+)\.\s*(.*)$", line.strip())

    def is_option_line(line: str):
        return re.match(r"^([A-D])\.\s+", line.strip())

    questions: list[dict] = []
    state = "seek_q"
    cur: dict | None = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if state == "seek_q":
            if not line:
                i += 1
                continue
            m = is_new_question_start(line)
            if m:
                cur = {"body": m.group(2).strip(), "options": [], "answer": None}
                state = "in_question_text"
            i += 1
            continue
        if state == "in_question_text":
            if not line:
                i += 1
                continue
            if is_option_line(line):
                state = "in_options"
                continue
            cur["body"] += " " + line
            i += 1
            continue
        if state == "in_options":
            if not line:
                i += 1
                continue
            if len(cur["options"]) >= 4:
                state = "seek_answer"
                continue
            matches = list(re.finditer(r"([A-D])\.\s+", line))
            if len(matches) >= 2:
                for idx, mm in enumerate(matches):
                    if len(cur["options"]) >= 4:
                        break
                    end = matches[idx + 1].start() if idx + 1 < len(matches) else len(line)
                    cur["options"].append((mm.group(1), line[mm.end():end].strip()))
                i += 1
                continue
            opt = is_option_line(line)
            if opt:
                cur["options"].append((opt.group(1), line[opt.end():].strip()))
                i += 1
                continue
            if cur["options"]:
                letter, text_ = cur["options"][-1]
                cur["options"][-1] = (letter, text_ + " " + line)
            i += 1
            continue
        if state == "seek_answer":
            if not line:
                i += 1
                continue
            cur["answer"] = line
            questions.append(cur)
            cur = None
            state = "seek_q"
            i += 1
            continue
    if cur and cur.get("options"):
        questions.append(cur)

    resolved = []
    for q in questions:
        ans = (q["answer"] or "").strip()
        m = re.match(r"^([A-D])\.", ans)
        letter = m.group(1) if m else None
        if letter is None and "X.509 certificate format" in q["body"]:
            letter = "C"
        if letter is None:
            continue
        resolved.append({
            "body": q["body"].replace("’", "'"),
            "options": [(l, t.replace("’", "'")) for l, t in q["options"]],
            "answer_letter": letter,
        })
    return resolved


def generate_parser_format(questions: list[dict]) -> str:
    lines = [
        "# DCIT418: Desmond's Comprehensive IA Review (Parser Format)",
        "",
        "77 IA-style review questions covering the full course range, formatted",
        "for parse_security_bank.py. Explanations were written from scratch since",
        "the source carried none.",
        "",
    ]
    for i, q in enumerate(questions, 1):
        lines.append(f"### {i}. {q['body']}")
        lines.append("")
        for letter, text_ in q["options"]:
            lines.append(f"- {letter}. {text_}")
        lines.append("")
        ans_text = dict(q["options"])[q["answer_letter"]]
        lines.append(f"**Correct Answer:** **{q['answer_letter']}. {ans_text}**")
        lines.append("")
        lines.append(f"**Intuition:** {EXPLANATIONS.get(i, 'See answer key for detailed reasoning.')}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def generate_formatted(questions: list[dict]) -> str:
    lines = [
        "# DCIT 418: Systems and Network Security",
        "## Desmond's Comprehensive Exam Review (77 Questions)",
        "",
        "**Prepared by:** Desmond (Student Take)  ",
        "**Format:** 77 MCQs with verified answers and original explanations  ",
        "**Note:** The source PDF export carried no explanation text; every",
        "Intuition below was written for this integration and should be spot",
        "checked against course material like any other bank entry.",
        "",
        "> [!NOTE]",
        "> One question from the original extraction had its stem and options",
        "> entirely lost to a PDF extraction gap (only a stray fragment of an",
        "> answer line, referencing MixColumns and ShiftRows, survived) and was",
        "> dropped rather than reconstructed from a guess.",
        "",
        "---",
        "",
        "## Complete Question Bank",
        "",
    ]
    for i, q in enumerate(questions, 1):
        lines.append(f"### {i}. {q['body']}")
        for letter, text_ in q["options"]:
            lines.append(f"- {letter}. {text_}")
        lines.append("")
        ans_text = dict(q["options"])[q["answer_letter"]]
        lines.append(f"**Correct Answer:** {q['answer_letter']}. {ans_text}  ")
        lines.append(f"**Intuition:** {EXPLANATIONS.get(i, 'See answer key for detailed reasoning.')}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    print("Parsing Desmond's Exam Review...")
    qs = parse_desmond()
    print(f"Parsed {len(qs)} questions")
    missing = [i for i in range(1, len(qs) + 1) if i not in EXPLANATIONS]
    if missing:
        print(f"WARNING: missing explanations for question indices {missing}")

    clean_path = Path("data_files/ia_bank/desmond_clean.md")
    clean_path.write_text(generate_parser_format(qs), encoding="utf-8")
    print(f"Wrote {len(qs)} questions to {clean_path}")

    formatted_path = Path("data_files/ia_bank/DESMOND_IA_FORMATTED.md")
    formatted_path.write_text(generate_formatted(qs), encoding="utf-8")
    print(f"Wrote human-readable review copy to {formatted_path}")
