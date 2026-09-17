# DCIT418 — SET 6
## Essay Bank with Skeletons
**Chapters 1–13 | 24 prompts | Use: drafting practice, then recall**

In a 60-minute Sakai paper shared with MCQs and fill-ins, an essay gets perhaps 8 to 12 minutes. You will not have time to compose a structure on the spot. Learn the skeletons; the prose writes itself once the shape is there.

**How to use this file (oral exam mode, for speed).** Do not read the skeletons before answering. Read only the prompt, then answer out loud from memory, as if speaking to an examiner, and record the audio. Go through all 24 prompts this way in one sitting: prompt, spoken answer, next prompt. Check yourself against the skeleton only after you have answered, not before, since seeing it first defeats the recall practice. This is faster than writing, since speaking a full answer takes 60 to 90 seconds instead of 8 to 12 minutes, so a full run of the set fits in under an hour.

**Tip: get the bot to grade your audio in one pass.** Record each spoken answer as a separate audio file named by prompt number (A1.m4a, A2.m4a, and so on), or one continuous recording with the prompt number spoken aloud at the start of each answer. Attach the audio alongside this file (SET6_Essay_Bank.md) in a single message to the bot, and ask it to transcribe each answer, match it to the corresponding prompt, and score it against that prompt's skeleton for coverage and the right verb (explain, compare, discuss, describe, justify). Doing this in one pass means the bot has both the audio and the skeletons together and does not need a second round trip to fetch the answer key.

**Universal structure for every answer:**
1. One-sentence direct answer to the question asked.
2. Definition of the key terms you are about to use.
3. The body — mechanism, comparison, or steps, depending on the verb.
4. A concrete example or consequence.
5. One-sentence close that answers the question again, now earned.

**Read the verb.** *Explain* wants mechanism. *Compare* wants a structured contrast, ideally a table. *Discuss* wants both sides and a judgement. *Describe* wants ordered steps. *Justify* wants reasons with weighting. Answering a "compare" prompt with a description loses marks even when every fact is right.

---

## GROUP A — Foundations

### A1. Discuss the CIA triad and explain why authenticity and non-repudiation are often added to it.
**Skeleton:** Define confidentiality (data confidentiality plus privacy), integrity (data and system integrity), availability. → Note each maps to a distinct class of threat: disclosure, alteration, disruption. → Argue the triad says nothing about *who* the parties are: a message can be confidential, unaltered and available yet sent by an impostor. → Authenticity fixes identity; non-repudiation fixes deniability, which matters for commerce and legal evidence. → Close: the triad protects the data, the additions protect the transaction.

### A2. Compare passive and active attacks, and explain why each demands a different defensive strategy.
**Skeleton:** Define both. → Passive: release of message contents, traffic analysis. Active: masquerade, replay, modification, DoS. → Table across four rows: alters system state, detectability, preventability, typical countermeasure. → Reasoning: passive attacks leave no trace so detection is hopeless and prevention (encryption) is the only route; active attacks are detectable but the attack surface is unbounded so prevention is hopeless and detection plus recovery is the only route. → Note traffic analysis persists even under encryption, which is why padding and traffic shaping exist. → Close on the inverted strategies.

### A3. Describe the X.800 security services and give a practical mechanism implementing each.
**Skeleton:** State all six. → For each, one line of definition plus one mechanism: Authentication → digital signature or challenge-response. Access control → ACLs, capabilities. Data confidentiality → encryption. Data integrity → hash or MAC. Non-repudiation → digital signature with a trusted third party. Availability → redundancy, rate limiting. → Note services are what is delivered, mechanisms are how, and one service usually needs several mechanisms. → Close on the service/mechanism distinction.

---

## GROUP B — Classical Cryptography

### B1. Explain why classical ciphers fail against modern cryptanalysis, using at least three examples.
**Skeleton:** Thesis: they fail because they preserve plaintext structure, and structure is what cryptanalysis attacks. → Monoalphabetic: huge keyspace (26!) yet trivially broken by frequency analysis, since the letter mapping is consistent. → Vigenère: flattens frequencies but the repeating key gives periodicity, so recovering the key length decomposes it into several Caesar ciphers. → Transposition: letter frequencies are untouched, so anagramming works. → Draw the general lesson: keyspace size bounds brute force only, and brute force is rarely the best attack. → Close: modern ciphers destroy statistical structure, which is what confusion and diffusion formalise.

### B2. Explain why the one-time pad offers perfect secrecy yet is impractical.
**Skeleton:** State the three conditions: truly random, as long as the message, never reused. → Mechanism of perfect secrecy: for any ciphertext, every plaintext of that length is equally likely, so the ciphertext is statistically independent of the plaintext and carries zero information. → Impracticality: the key is as long as the message, so distributing it securely is as hard as sending the message securely — the problem is moved, not solved. → Consequence of reuse: C₁ ⊕ C₂ = P₁ ⊕ P₂, the key cancels and both messages fall to crib dragging. → Close: it is the benchmark of security, not a usable system, and it is why key management dominates practical cryptography.

---

## GROUP C — Symmetric Ciphers

### C1. Explain the Feistel structure and why it is significant in cipher design.
**Skeleton:** Define: block split into Lᵢ₋₁ and Rᵢ₋₁; equations Lᵢ = Rᵢ₋₁ and Rᵢ = Lᵢ₋₁ ⊕ F(Rᵢ₋₁, Kᵢ). → Significance: because the alteration is via XOR and only half the block changes, the same algorithm with reversed subkeys decrypts, so F need never be inverted and need not even be invertible. → Consequence: F can be arbitrarily complex and nonlinear, chosen purely for strength, and one implementation serves both directions. → Note the design parameters: block size, key size, round count, subkey generation, complexity of F. → Close: it decoupled cryptographic strength from invertibility, which is why it dominated block cipher design for decades.

### C2. Describe the structure of DES and discuss why it is no longer considered secure.
**Skeleton:** Parameters: 64-bit block, 64-bit stored key with 8 parity bits giving 56 effective, 16 Feistel rounds, initial and final permutations with no cryptographic effect. → Round function in order with widths: expansion 32 → 48, XOR with the 48-bit subkey, eight S-boxes 6 → 4 giving 48 → 32, P-box permutation. → S-boxes are the only nonlinear stage and therefore the source of security. → Insecurity: 2⁵⁶ ≈ 7.2 × 10¹⁶ keys, brute-forced by dedicated hardware since the late 1990s; the design is otherwise sound, so keyspace is the binding constraint. → Responses: Triple DES as a stopgap, limited by the 64-bit block; AES as the replacement. → Close.

### C3. Compare DES and AES.
**Skeleton:** Table: structure (Feistel vs SPN), block size (64 vs 128), key size (56 vs 128/192/256), rounds (16 vs 10/12/14), round operations, decryption method (reversed subkeys vs separate inverse cipher), status. → Then the analysis marks: AES transforms the whole block per round so it needs fewer rounds; it pays for this by requiring every transformation to be invertible, hence a separate inverse cipher; its byte-oriented operations suit modern hardware and software. → Close: AES traded implementation convenience for speed, larger parameters and cleaner analysability.

### C4. Describe the AES round transformations and explain the role of each.
**Skeleton:** Setup: 128-bit block as a 4×4 State, initial AddRoundKey before round one. → SubBytes: byte substitution via an S-box built from GF(2⁸) inverses plus an affine map; supplies nonlinearity, hence confusion. → ShiftRows: rows cyclically shifted by 0, 1, 2, 3; diffusion across columns. → MixColumns: each column multiplied by a fixed matrix in GF(2⁸); diffusion within a column; omitted in the final round. → AddRoundKey: XOR with the round subkey; the only key-dependent step. → Synthesis: the first three are public and fixed, providing mixing but no secrecy; AddRoundKey supplies the secrecy. Neither half is secure alone. → Close on why MixColumns is dropped last: no later round to compound its diffusion.

---

## GROUP D — Mathematical Foundations

### D1. Explain the role of finite fields in modern cryptography.
**Skeleton:** Define group, ring, field as a ladder of increasing structure, with the field's distinguishing property being a multiplicative inverse for every nonzero element, hence division. → Why cryptography needs it: transformations must be invertible to decrypt, and RSA's d is defined as a multiplicative inverse. → GF(p) requires p prime; demonstrate with 2 mod 6 having no inverse versus every nonzero element mod 7 having one. → GF(2ⁿ) requires an irreducible modulus polynomial for the identical reason; irreducible is the polynomial analogue of prime. → Application: AES uses GF(2⁸) with x⁸+x⁴+x³+x+1, because integers mod 256 do not form a field. → Close.

### D2. Explain the role of number theory in public-key cryptography.
**Skeleton:** Thesis: public-key cryptography needs one-way functions, and number theory supplies them. → Fermat's Little Theorem, and its use in primality testing. → Euler's totient and Euler's Theorem, and why RSA correctness depends on the latter since n is composite. → Primality testing: Miller-Rabin, probabilistic, one-sided error, needed because trial division is infeasible at RSA sizes. → CRT for decryption speedup. → The two hard problems: factorisation for RSA, discrete logarithm for Diffie-Hellman and ElGamal, ECDLP for ECC. → Close: security rests on an asymmetry of computational difficulty, not on secrecy of method.

---

## GROUP E — Modes and Stream Ciphers

### E1. Compare the five block cipher modes of operation and their security implications.
**Skeleton:** State each with its formula. → Table: error propagation, stream-cipher behaviour, parallelisability, typical application. → ECB's failure: determinism means equal plaintext blocks give equal ciphertext blocks, leaking structure regardless of cipher strength. → CBC: chaining plus IV makes encryption probabilistic; errors span two blocks; serial encryption. → CFB and OFB: keystream generation, E used in both directions; CFB chains off ciphertext so errors propagate, OFB chains off keystream so they do not. → CTR: independent counters give parallelism and random access. → Close: the mode, not the cipher, usually decides whether a deployment is secure.

### E2. Explain why mode selection matters more in practice than key size.
**Skeleton:** Thesis and framing: attackers take the cheapest route. → AES-128 already gives a 2¹²⁸ work factor, beyond reach; AES-256 raises an already unreachable number. → Mode and parameter errors create attacks that never touch the key: ECB pattern leakage, predictable CBC IVs, repeated CTR counters, keystream reuse. → These succeed identically against AES-256. → Broaden: same lesson in Diffie-Hellman falling to man-in-the-middle with the discrete log intact. → Close: security is a property of the system, and effort spent on correct modes buys more than effort spent on larger keys.

### E3. Explain the difference between a PRNG and a CSPRNG and why the distinction matters.
**Skeleton:** Define both; note both are deterministic from a seed. → Statistical randomness versus computational unpredictability; test suites check only the former. → LCG as the worked case: Xₙ₊₁ = (aXₙ + c) mod m, a few outputs reveal a, c, m, and the whole sequence follows. → Consequence in a stream cipher: keystream recovered, therefore all plaintext recovered, since C = P ⊕ KS. → Note TRNGs draw on physical entropy and are typically used to seed a CSPRNG rather than to generate bulk output. → Close: fit for simulation is not fit for cryptography.

### E4. Describe RC4 and discuss why it has been deprecated.
**Skeleton:** Position it: a stream cipher built from scratch, not a block cipher in a streaming mode. → KSA: a 256-byte state array initialised to 0–255 then shuffled into a key-dependent permutation, the key cycled to fill 256 bytes. → PRGA: two index pointers, continuous swapping, one keystream byte per step, XORed with plaintext. → Appeal: simple, fast, tiny code, hence WEP and early SSL. → Deprecation: statistical biases in early keystream bytes let an attacker recover plaintext or key information from enough ciphertext; related-key weaknesses broke WEP outright. → Replacements: AES in CTR or GCM. → Close.

---

## GROUP F — Public-Key Cryptography

### F1. Describe the RSA algorithm and explain why decryption recovers the plaintext.
**Skeleton:** Five key generation steps: choose p, q; n = pq; φ(n) = (p−1)(q−1); choose e with gcd(e, φ(n)) = 1; compute d as e's inverse mod φ(n). Public (e, n), private (d, n). → Encryption C = P^e mod n, decryption P = C^d mod n; stress the modulus is n. → Correctness: ed ≡ 1 (mod φ(n)) so ed = 1 + kφ(n); then P^(ed) = P·(P^φ(n))^k ≡ P (mod n) by Euler's Theorem. → Why Euler rather than Fermat: n is composite. → Security: recovering d from (e, n) requires φ(n), which requires factoring n. → Close.

### F2. Discuss the security considerations of RSA.
**Skeleton:** Foundation: factoring n. → Key size must track advances in factoring algorithms (the number field sieve is sub-exponential), hence the drift to 2048 and 3072 bits. → Secrets: p, q and φ(n) are each as sensitive as d, since any one yields the private key; knowing n and φ(n) recovers p and q via a quadratic. → Raw RSA is deterministic, so it leaks like ECB and needs randomised padding (OAEP). → Small-exponent and related implementation pitfalls; timing and fault side channels, including the CRT fault leak. → Quantum: Shor's algorithm breaks it outright, motivating post-quantum work. → Close: RSA's mathematics is rarely the failure point; parameters and implementation are.

### F3. Describe Diffie-Hellman key exchange and explain its vulnerability to man-in-the-middle attack.
**Skeleton:** Public parameters q and primitive root α. → Alice: secret X_A, sends Y_A = α^(X_A) mod q. Bob likewise. → Both compute α^(X_A·X_B) mod q; show the algebra. → Note the shared key is never transmitted and the secrets never leave their owners; security rests on the discrete logarithm problem. → Attack: the adversary substitutes their own public value in each direction, running two legitimate exchanges, then relays traffic while reading it. → Key insight: no discrete log is solved; the protocol is bypassed, not broken, because nothing binds a public value to an identity. → Remedy: authenticate the exchange via signatures or certificates. → Close on primitive strength not implying protocol security.

### F4. Compare RSA and elliptic curve cryptography.
**Skeleton:** Table: hard problem (factorisation vs ECDLP), key size for comparable security (3072 vs 256), operation cost, maturity and deployment, typical use. → The reason for the size gap: factorisation has sub-exponential attacks (number field sieve) so RSA keys must grow quickly, while the best attacks on well-chosen curves are fully exponential (Pollard's rho, roughly square root of the group order). → Consequences: ECC suits constrained devices, mobile and IoT; RSA retains legacy footprint and simpler implementation. → Note both fall to Shor's algorithm, so neither is post-quantum. → Close.

### F5. Explain why practical systems use hybrid encryption rather than public-key cryptography alone.
**Skeleton:** Restate the problem each solves: symmetric ciphers are fast but need a shared key; public-key solves distribution but is slow. → Cost gap: modular exponentiation or point multiplication over huge operands versus AES's byte operations with hardware acceleration. → Additional limits: RSA can only encrypt below the modulus size, and raw RSA is deterministic so it needs padding. → Hybrid scheme: public-key transports or agrees a session key, symmetric cipher carries the data. → Example: TLS handshake then bulk record encryption. → Close: each primitive used for what it is good at.

---

## GROUP G — Hashes, MACs and Signatures

### G1. Explain the required properties of a cryptographic hash function and why each matters.
**Skeleton:** Define: variable-length input, fixed-length digest, efficient to compute. → Preimage resistance: given h, infeasible to find any x with H(x) = h; protects stored password hashes. → Second preimage resistance: given x, infeasible to find x′ ≠ x with the same digest; protects a specific document from substitution. → Collision resistance: infeasible to find any pair colliding; protects signatures, and is the weakest of the three because of the birthday bound, which gives roughly n/2 bits of security for an n-bit digest. → Note applications: integrity checks, signatures, password storage, PRNG construction. → Close on why collision resistance drove SHA-1's retirement.

### G2. Compare a hash function, a MAC and a digital signature.
**Skeleton:** Table across: key used (none, shared secret, private key), services provided (integrity; integrity plus authentication; integrity plus authentication plus non-repudiation), who can verify (anyone; holders of the shared key; anyone with the public key), relative cost. → The crucial distinction: a MAC cannot give non-repudiation because both parties hold the same key, so either could have produced the tag; a signature can, because only the signer holds the private key. → HMAC as the standard MAC construction, nesting a hash with the key and the ipad/opad constants. → Close: choose by which service you actually need, since cost rises with each.

### G3. Explain how digital signatures provide non-repudiation and what is required for this to hold in practice.
**Skeleton:** Mechanism: hash the message, then transform the digest with the signer's private key; anyone with the public key verifies. → Why non-repudiation follows: only the private key holder could have produced it, so the signer cannot credibly deny authorship. → Why hashing first: efficiency, and it fixes the input size for the signature operation. → Practical requirements: the private key must genuinely be private; the public key must be bound to a real identity, which is what certificates and a PKI provide; the hash must be collision resistant, or an attacker could sign one document and claim another. → Close: the cryptography alone is not enough — identity binding and hash strength are load-bearing.

---

## GROUP H — Synthesis

### H1. "A strong algorithm is not a secure system." Discuss.
**Skeleton:** Thesis: the algorithm is one component among several, and failures cluster elsewhere. → Four independent illustrations: mode (AES in ECB leaks structure), parameter reuse (IV, counter or keystream reuse exposes plaintext XOR), protocol (Diffie-Hellman falls to man-in-the-middle with the hard problem intact), key management (RSA collapses if p, q or φ(n) leaks). → Add the human and implementation layer: side channels, poor entropy, weak passwords. → Generalise: an attacker picks the cheapest route, which is almost never the cipher. → Close: security must be argued for the whole system, algorithm, mode, parameters, protocol, keys and implementation.

### H2. Discuss the role of XOR across the cryptographic constructions studied in this course.
**Skeleton:** List where it appears: Feistel round, one-time pad, all keystream modes (CFB, OFB, CTR), stream ciphers, AddRoundKey, HMAC padding. → Property one, self-inverse: one operation serves both directions, so a single implementation encrypts and decrypts. → Property two, balance: XOR with a uniform random bit yields a uniform output regardless of input, which is the source of the one-time pad's perfect secrecy and the reason keystream modes are sound. → Property three, cost: bitwise, no carries, one instruction. → Property four, linearity over GF(2): what makes Feistel reversible even when F is not invertible. → The flip side: linearity means reuse is catastrophic, as the key cancels. → Close: the same property that makes XOR useful makes parameter reuse fatal.

### H3. Compare symmetric and asymmetric cryptography, and explain why both are needed.
**Skeleton:** Table: key structure, speed, key distribution, typical key sizes, services offered, examples. → Symmetric: fast, compact keys, but n parties need n(n−1)/2 keys and distribution requires a secure channel. → Asymmetric: solves distribution and enables signatures and non-repudiation, but is orders of magnitude slower and size-limited. → Hybrid practice: asymmetric for key establishment and authentication, symmetric for bulk data. → Example: the TLS handshake versus the record layer. → Close: they are complementary, not competing, and every real system uses both.

---

## TIMING DISCIPLINE

Budget roughly: 1 minute planning the skeleton, 8 minutes writing, 1 minute checking. Write the skeleton as a bullet list at the top of your answer before you begin prose — if you run out of time, a marker can still see the structure and award partial credit for points you did not reach.

Do not open with throat-clearing. "Security is very important in today's world" earns nothing. Open by answering the question.
