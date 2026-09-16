# DCIT 418 — Study Blocks, Chapters 1 to 13
### Stallings, *Cryptography and Network Security*, 6th ed.
**Total: 5 hours across 13 blocks. Works as first-time learning or revision.**

---

## How to use this

Each block has four parts. **Frame** tells you what the chapter is for in one line. **Core** is the content. **Exam hooks** are the specific items most likely to be asked, based on the format and what came up in class. **Check** is a closed-book question set — do not skip it, because recognising material is not the same as producing it.

**First-time learning:** read Frame, work through Core slowly, then do Check. Use the full time.

**Revision:** read Frame, skip straight to Check. Only go back into Core for what you miss. This cuts the five hours to roughly two.

---

## Exam format and what it implies

Sixty minutes on Sakai. MCQs, fill-ins, and essay. Roughly fifty multiple choice, ten fill-ins, and two longer questions. Coverage is Chapters 1 to 13 plus the course outline. **No calculation questions.**

Four consequences worth internalising before you start:

**Breadth beats depth.** Fifty MCQs across thirteen chapters means roughly four per chapter. A chapter you know at 70 percent across the board scores better than one chapter at 100 percent and another at zero.

**Fill-ins want the exact term.** "The thing that mixes the columns" earns nothing; **MixColumns** earns the mark. Terminology is the single highest-yield thing to drill.

**Numbers get written as words.** If the answer is a number, write it out — *sixteen*, not 16. This was stated explicitly in class. It costs nothing to comply and it is an easy mark to lose.

**No calculation does not mean no numbers.** You will not be asked to compute an RSA key, but you may well be asked how many rounds DES has, what AES's block size is, or how many S-boxes the DES round function uses. Memorise the constants; skip the arithmetic.

---

# BLOCK 1 — Chapter 1: Overview
**20 minutes**

### Frame
The vocabulary chapter. Almost pure terminology, and terminology is what fill-ins test. Highest marks-per-minute in the whole book.

### Core

**The CIA triad.** *Confidentiality* keeps data from unauthorised reading, and splits into data confidentiality and privacy. *Integrity* keeps data from unauthorised alteration, and splits into data integrity (the information is unmodified) and system integrity (the system functions as intended, unimpaired). *Availability* keeps systems and data accessible to authorised users on demand.

Stallings adds two beyond the triad: *authenticity* (the entity is who it claims to be) and *non-repudiation* (neither party can later deny sending or receiving).

**The OSI Security Architecture** has three pillars: security **attack**, security **mechanism**, security **service**. Keep them straight — the *service* is what is delivered (data integrity), the *mechanism* is how (a MAC), the *attack* is what you are defending against.

**Passive attacks** observe without altering. Two kinds: *release of message contents* and *traffic analysis*. Because nothing changes, there is no trace to detect, so the defence is **prevention** — encryption.

**Active attacks** alter data or system state. Four kinds: *masquerade* (pretending to be another entity), *replay* (capturing and retransmitting), *modification of messages* (altering, delaying, reordering), *denial of service* (preventing normal use). Because the attack surface is unbounded, absolute prevention is impossible, so the defence is **detection and recovery**.

**The six X.800 security services:** Authentication, Access Control, Data Confidentiality, Data Integrity, Non-repudiation, Availability.

**Model for network security:** sender → security transformation (using a secret) → insecure channel, with an opponent present → inverse transformation → receiver. A **trusted third party** sits above, distributing secrets and arbitrating disputes.

### Exam hooks
- The full list of six services. Availability is the one students drop.
- Which attacks are passive and which are active. Traffic analysis is passive; DoS is active.
- Service versus mechanism. Encipherment is a *mechanism*; authentication is a *service*.
- The inverted defence strategies: prevent passive, detect-and-recover active.
- Traffic analysis still works against encrypted traffic — the payload is hidden but source, destination, size, timing and frequency are not.

### Check
1. List the six X.800 security services.
2. Name the four active attack types.
3. Is encipherment a service or a mechanism?
4. Why is prevention the strategy for passive attacks but not active ones?

---

# BLOCK 2 — Chapter 2: Classical Encryption
**15 minutes**

### Frame
Historical ciphers. Low weight, but the substitution-versus-transposition distinction and the one-time pad show up reliably.

### Core

**The symmetric cipher model has five components:** plaintext, encryption algorithm, secret key, ciphertext, decryption algorithm. The key is independent of both plaintext and algorithm.

**Substitution** replaces characters. **Transposition** rearranges their positions without changing them. This matters for cryptanalysis: transposition leaves letter frequencies untouched, so frequency analysis tells you nothing and you attack the permutation instead.

**Caesar** — fixed shift of three. **Monoalphabetic** — each plaintext letter maps consistently to one ciphertext letter; keyspace is 26 factorial, yet it falls instantly to frequency analysis because the mapping is consistent. This is the chapter's central lesson: a large keyspace bounds brute force only, and brute force is rarely the best attack.

**Playfair** — first practical digraph cipher, uses a five-by-five matrix with I and J sharing a cell.

**Vigenère** — polyalphabetic, repeating keyword, so one plaintext letter maps to several ciphertext letters depending on position. This flattens the frequency distribution. Broken once the key length is recovered, because the ciphertext then decomposes into several Caesar ciphers.

**One-time pad (Vernam)** — the only unconditionally secure cipher. Three conditions: the key is **truly random**, **as long as the message**, and **used only once**. Perfect secrecy means every plaintext of that length is equally likely given the ciphertext, so the ciphertext carries zero information. Impractical because distributing a key as long as the message is as hard as sending the message.

**Rail fence** — transposition, zigzag across rails then read off row by row.

**Rotor machines** — mechanical polyalphabetic substitution with a very long effective period.

**Steganography** hides the *existence* of a message; cryptography hides its *content*. They are complementary, not alternatives.

### Exam hooks
- One-time pad's three conditions, and that it is the only unconditionally secure scheme.
- Substitution versus transposition, and that transposition preserves letter frequencies.
- Vigenère is polyalphabetic; Caesar and simple substitution are monoalphabetic.
- Playfair works on digraphs, and I/J share a cell.
- Steganography conceals existence, not meaning.

### Check
1. What three conditions make the one-time pad unbreakable?
2. Which cipher type leaves letter frequencies unchanged, and why does that matter?
3. Why is a keyspace of 26 factorial not enough to make a cipher secure?

---

# BLOCK 3 — Chapter 3: Block Ciphers and DES
**30 minutes**

### Frame
One of the two most heavily tested chapters. Feistel structure, DES parameters, and Shannon's principles all appear repeatedly.

### Core

**Block versus stream.** A block cipher processes a fixed-size group of bits at once. A stream cipher processes one bit or byte at a time.

**Shannon's two principles.** **Confusion** makes the relationship between the *key* and the ciphertext as complex as possible — achieved by substitution, meaning S-boxes. **Diffusion** spreads the statistical structure of the *plaintext* across the ciphertext — achieved by permutation. Memorise which goes with which; they are a classic MCQ pair.

**Feistel structure.** The block splits into two halves. Each round:

> L(i) = R(i−1)
> R(i) = L(i−1) ⊕ F(R(i−1), K(i))

The significance: because the change is applied by XOR and only half the block moves, **decryption is the same algorithm with the subkeys in reverse order**. The round function F never needs inverting and need not even be invertible, so it can be arbitrarily complex and chosen purely for strength. One implementation serves both directions.

Design parameters: block size, key size, number of rounds, subkey generation algorithm, complexity of F.

**DES parameters.** Block size **sixty-four** bits. Stored key **sixty-four** bits, of which eight are parity, giving an effective key of **fifty-six** bits. **Sixteen** rounds.

**DES structure:** initial permutation → sixteen Feistel rounds → thirty-two-bit swap → inverse initial permutation. IP and its inverse are fixed, public, and key-independent, so they contribute **nothing cryptographically** — they exist for hardware reasons.

**The DES round function, in order:** expansion permutation takes the thirty-two-bit right half to **forty-eight** bits (to match the subkey); XOR with the forty-eight-bit subkey; **eight** S-boxes, each taking **six** bits in and producing **four** out, so forty-eight bits reduce back to thirty-two; then the P-box permutation for diffusion.

The S-boxes are the **only non-linear component**. Everything else — expansion, permutation, XOR — is linear, and a purely linear cipher collapses to a single linear transformation solvable by algebra. All of DES's security originates in the S-boxes.

**Avalanche effect:** a one-bit change in plaintext or key flips roughly half the output bits. Without it, related plaintexts give related ciphertexts, which is what differential cryptanalysis exploits.

**Why DES fell:** fifty-six bits gives about seven times ten to the sixteen keys, brute-forced by dedicated hardware from the late 1990s. The design was otherwise sound — keyspace was the binding constraint.

**The S-box controversy:** the design criteria were classified, which fuelled suspicion of a deliberate backdoor. Declassification later showed they had been hardened against differential cryptanalysis, which was not publicly known at the time.

### Exam hooks
- Both Feistel equations, with the indices right.
- Confusion versus diffusion, and which is substitution versus permutation.
- Sixteen rounds, sixty-four-bit block, fifty-six-bit effective key, eight parity bits.
- Expansion thirty-two to forty-eight; S-boxes six in, four out; eight of them.
- The S-box is the only non-linear element.
- IP contributes nothing cryptographically.
- **DES does not shift rows** — that is AES. This was flagged explicitly in class as a distractor.

### Check
1. Write both Feistel round equations.
2. Which Shannon principle is achieved by substitution?
3. How many S-boxes does DES use, and what are their input and output widths?
4. Why does the round function F not need to be invertible?

---

# BLOCK 4 — Chapter 4: Number Theory and Finite Fields
**20 minutes**

### Frame
The support chapter. No calculations on the exam, so learn the *definitions* and the *reasons*, not the arithmetic.

### Core

**Euclidean algorithm** computes the greatest common divisor by successive division. The **extended** version computes multiplicative inverses — which is how RSA's private exponent is found.

**Multiplicative inverse** of a mod n exists **only when gcd(a, n) = 1**. This single rule explains three separate things later: why GF(p) needs p prime, why the GF(2ⁿ) modulus must be irreducible, and why RSA's e must be coprime to φ(n).

**The algebraic ladder.**
- **Group**: one operation, with closure, associativity, an identity, and inverses. Add commutativity and it is **abelian**.
- **Ring**: two operations. Abelian group under addition; multiplication is associative and distributes over addition. Multiplication does **not** need inverses.
- **Field**: a ring where multiplication is also commutative, has an identity, and **every nonzero element has a multiplicative inverse** — so division works.

The ring-to-field boundary is the multiplicative inverse. That is the exam answer.

**GF(p)** is a field only when **p is prime**. Concretely: modulo six, the element two has no inverse — two times one through five never yields one — so it is not a field. Modulo seven, every nonzero element has an inverse.

**GF(2ⁿ)** represents elements as polynomials with binary coefficients, so a byte is a polynomial rather than a number. **Addition is XOR**, with no carries. **Multiplication** is polynomial multiplication reduced modulo an **irreducible** polynomial — irreducible being the polynomial analogue of prime, and required for exactly the same reason.

**AES uses GF(2⁸)** with the modulus **x⁸ + x⁴ + x³ + x + 1**. Note the terms carefully: eight, four, three, one, constant.

Why not just integers modulo 256? Because 256 is composite, so every even byte would lack an inverse and AES's transformations could not be inverted. GF(2⁸) gives byte-sized arithmetic *and* a genuine field.

### Exam hooks
- What distinguishes a field from a ring.
- GF(p) requires p prime; GF(2ⁿ) requires an irreducible modulus; same underlying reason.
- Addition in GF(2ⁿ) is XOR.
- The AES modulus polynomial, exactly.
- Abelian means commutative.

### Check
1. State the one property a field has that a ring may lack.
2. Why must the GF(2ⁿ) modulus be irreducible?
3. What bitwise operation is addition in GF(2ⁿ)?
4. Write the AES irreducible polynomial.

---

# BLOCK 5 — Chapter 5: AES
**30 minutes**

### Frame
The other heavily tested chapter. Know the four transformations cold, in order, with what each does.

### Core

**Origin:** selected by NIST through an **open public competition**, unlike DES which was developed internally. The winning algorithm was **Rijndael**, by Joan Daemen and Vincent Rijmen. Standardised as FIPS 197.

**Parameters.** Block size is always **one hundred and twenty-eight** bits, whatever the key. Key sizes **128, 192, 256**, giving **ten, twelve, fourteen** rounds respectively.

**Structure: AES is NOT a Feistel cipher.** It is a **substitution-permutation network**. In Feistel, half the block is transformed per round; in AES the **entire block** is transformed every round. This is the single most common AES exam question.

**The State** is a four-by-four matrix of bytes, filled column by column, holding the 128-bit block.

**The four round transformations, in order:**

1. **SubBytes** — byte-by-byte substitution via a fixed S-box. The S-box is built from the **multiplicative inverse in GF(2⁸) followed by an affine transformation**. This is the **only non-linear** step, so it supplies **confusion**.
2. **ShiftRows** — each row cyclically shifted left: row zero by zero, row one by one, row two by two, row three by three. Diffusion **across** columns.
3. **MixColumns** — each column treated as a polynomial and multiplied by a fixed matrix in GF(2⁸), so every output byte depends on all four input bytes of that column. Diffusion **within** a column.
4. **AddRoundKey** — XOR the State with the round subkey. The **only** step that uses the secret key.

There is an **initial AddRoundKey** before round one, and **MixColumns is omitted from the final round**.

**Why MixColumns is dropped last:** its diffusion is only useful if further rounds follow to compound it. Including it would cost computation for no security gain and would complicate the inverse cipher.

**Why AddRoundKey alone is not enough:** the other three transformations are fixed and public, so anyone can compute or invert them — they supply mixing but no secrecy. A bare XOR with key material is trivially broken. Security comes from injecting key material between rounds of complex public mixing.

**Key expansion** stretches the cipher key into one round key per round (eleven total for AES-128: one initial plus ten). The g-function applies **RotWord** (cyclic byte shift), **SubWord** (S-box each byte), then XOR with a **round constant (Rcon)**. Distinct round constants break the symmetry between rounds, which otherwise invites slide attacks.

**AES versus DES:** SPN versus Feistel; 128-bit block versus 64; 128/192/256-bit key versus 56; 10/12/14 rounds versus 16; separate inverse cipher versus reversed subkeys.

### Exam hooks
- The four transformations, in order, correctly named. It is **ShiftRows**, never "ShiftCols".
- AES is an SPN, not Feistel, because the whole block is transformed.
- MixColumns is the omitted one in the final round.
- AddRoundKey is the only key-dependent step.
- SubBytes is the only non-linear step.
- Rijndael, Daemen and Rijmen, open NIST competition.
- Block size fixed at 128 regardless of key size.
- Key-size-to-round-count mapping.

### Check
1. Name the four transformations in order and what each provides.
2. Why is AES not a Feistel cipher?
3. Which transformation uses the secret key?
4. How many rounds for a 192-bit key?

---

# BLOCK 6 — Chapter 6: Block Cipher Operation
**30 minutes**

### Frame
Modes of operation plus Triple DES. Dense with easily-confused pairs, which makes it MCQ-rich.

### Core

**Multiple encryption.** Double DES fails to double security because of the **meet-in-the-middle attack**: encrypt the plaintext under all possible first keys and store the intermediates, decrypt the ciphertext under all possible second keys, and look for a match. This cuts the work from two-to-the-112 down to roughly two-to-the-57, so double DES is barely stronger than single DES.

**Triple DES** uses the **Encrypt-Decrypt-Encrypt** sequence. Two-key 3DES gives **one hundred and twelve** effective bits; three-key gives **one hundred and sixty-eight**. The EDE ordering exists so that setting the keys equal reproduces single DES, preserving backward compatibility. 3DES remained a stopgap because it inherits DES's **sixty-four-bit block**, which key lengthening cannot fix, and it is roughly three times slower.

**The five modes.**

**ECB** — each block encrypted independently: C(i) = E(K, P(i)). Because E under a fixed key is deterministic, **identical plaintext blocks produce identical ciphertext blocks**, so plaintext repetition structure leaks. The cipher is not broken; the mode leaks. No safe general-purpose use.

**CBC** — each plaintext block XORed with the previous ciphertext before encryption: C(i) = E(K, P(i) ⊕ C(i−1)), with an **IV** for the first block. Encryption is serial. An error in one ciphertext block corrupts that block and flips the corresponding bit in the next — **two blocks** of error propagation.

**CFB** — the keystream comes from encrypting the **previous ciphertext**: C(i) = P(i) ⊕ E(K, C(i−1)). Self-synchronising stream cipher. Errors propagate over two blocks.

**OFB** — the keystream comes from encrypting the **previous keystream block**: O(i) = E(K, O(i−1)), then C(i) = P(i) ⊕ O(i). **No error propagation**, because the keystream never touches the ciphertext. But strictly **serial**, since each keystream block depends on its predecessor.

**CTR** — the keystream comes from encrypting an incrementing **counter**: C(i) = P(i) ⊕ E(K, Counter(i)). No error propagation, **fully parallelisable**, and supports **random access** to any block.

**In CFB, OFB and CTR, decryption uses the encryption function E**, never D. The reason: E is never applied to the plaintext — it only manufactures a keystream, and XOR is self-inverse, so the same operation runs both directions.

**IV versus counter.** The CBC IV must be **unpredictable**, because it is XORed directly with plaintext and a predictable IV enables chosen-plaintext attacks. The CTR counter need only be **unique** — the (key, counter) pair must never repeat, since repetition reuses a keystream and lets an attacker recover the XOR of two plaintexts.

**XTS-AES** is the NIST mode for **block-oriented storage** — disks and SSDs. It uses a **tweak** derived from the sector address so that identical plaintext at different disk locations encrypts differently.

### Exam hooks
- Which mode leaks patterns, and that the fault is the mode's determinism.
- CTR is the parallelisable, random-access mode.
- OFB feeds back the **keystream**; CFB feeds back the **ciphertext**. This is the most-missed distinction in the chapter.
- OFB and CTR have no error propagation; CBC and CFB span two blocks.
- CFB/OFB/CTR decryption uses E.
- IV unpredictable, counter unique.
- Triple DES: EDE, 112 or 168 bits, limited by the 64-bit block.
- Meet-in-the-middle defeats double DES.
- XTS-AES is for storage, and uses a tweak.

### Check
1. Which mode allows random-access decryption, and why?
2. In OFB, what is fed back — ciphertext or keystream?
3. Why does CFB decryption use E rather than D?
4. What is the effective key length of three-key Triple DES?

---

# BLOCK 7 — Chapter 7: PRNG and Stream Ciphers
**20 minutes**

### Frame
Randomness quality and RC4. Conceptually light, terminology-heavy.

### Core

**Three generator types.** A **TRNG** draws on a non-deterministic physical process — thermal noise, clock jitter — and is unpredictable but slow. A **PRNG** is a deterministic algorithm expanding a **seed** into a long sequence; fast, reproducible, and eventually **periodic**. A **CSPRNG** is a PRNG that is additionally **computationally unpredictable**. In practice a TRNG supplies entropy to **seed** a CSPRNG, combining unpredictability with speed.

**Randomness versus unpredictability.** Statistical randomness asks "does it look random?" Cryptographic unpredictability asks "can an attacker predict the next output after seeing many past ones?" Standard test suites check only the first.

**The LCG** is defined by X(n+1) = (aX(n) + c) mod m. It passes statistical tests and is fine for simulations, but it is **cryptographically worthless**: a handful of consecutive outputs lets an attacker solve for a, c and m and reproduce the whole sequence.

**Blum Blum Shub** squares modulo n = pq and takes the least significant bit. Its security reduces to the hardness of **factoring**, the same problem underlying RSA. Provably secure but slow.

**Stream cipher structure:** a keystream generator takes the key (and often an IV) and produces a keystream; ciphertext is plaintext **XORed** with the keystream, and decryption is the identical XOR.

**Keystream reuse is fatal.** If C₁ = P₁ ⊕ K and C₂ = P₂ ⊕ K, then C₁ ⊕ C₂ = P₁ ⊕ P₂ — the keystream cancels and the attacker has the XOR of two plaintexts with no key knowledge at all.

**RC4** — **Rivest Cipher 4**, designed by Ron Rivest in 1987. Two phases:
- **KSA (Key Scheduling Algorithm)** initialises a **256-byte** state array S to the values zero through 255, then shuffles it into a key-dependent permutation.
- **PRGA (Pseudo-Random Generation Algorithm)** then swaps entries using two index pointers and emits one keystream byte per step.

**RC4's downfall came through WEP.** WEP used a **twenty-four-bit IV** concatenated with the master key. The small IV space caused rapid IV reuse, and the concatenation exposed weaknesses in RC4's key schedule — the FMS attack. The failure was in **how WEP used RC4**, compounded by statistical biases in RC4's early keystream bytes.

### Exam hooks
- TRNG versus PRNG versus CSPRNG, and that a TRNG typically seeds a PRNG.
- LCG passes statistics but is predictable; the property needed is unpredictability.
- RC4 stands for Rivest Cipher 4; state array is 256 bytes; KSA sets up, PRGA outputs.
- Keystream reuse yields the XOR of the plaintexts.
- WEP's 24-bit IV.
- Blum Blum Shub rests on factoring.

### Check
1. What are RC4's two phases and what does each do?
2. Why is an LCG unsuitable for cryptography despite passing randomness tests?
3. What does an attacker obtain if a keystream is reused?

---

# BLOCK 8 — Chapter 8: More Number Theory
**20 minutes**

### Frame
The bridge into public-key. Learn the statements, not the computations.

### Core

**Fundamental Theorem of Arithmetic:** every integer greater than one factors into primes in exactly one way.

**Fermat's Little Theorem:** for **prime** p and a not divisible by p, a^(p−1) ≡ 1 (mod p). Alternate form valid for all a: a^p ≡ a (mod p).

**Euler's totient φ(n)** counts the positive integers below n that are **coprime** to n. For prime p, φ(p) = p − 1. For n = pq with p and q distinct primes, **φ(n) = (p−1)(q−1)** — the formula RSA is built on.

**Euler's Theorem:** if gcd(a, n) = 1 then a^φ(n) ≡ 1 (mod n). This **generalises Fermat's to any modulus**, not just primes. Fermat's is the special case where n is prime.

This distinction carries a mark: **RSA's correctness depends on Euler's, not Fermat's**, because the RSA modulus n = pq is composite.

**Primality testing.** Trial division is infeasible at RSA key sizes. **Miller-Rabin** is a fast **probabilistic** test: a failed test proves compositeness definitively, while passing means "probably prime", with the error probability shrinking by at least a factor of four per additional random witness. The **AKS algorithm** (2002) was the first **deterministic** polynomial-time primality proof.

**Prime Number Theorem:** near a large integer n, primes occur roughly once every ln(n) integers — so random search for large primes is practical.

**Chinese Remainder Theorem:** given remainders with respect to **pairwise coprime** moduli, there is a unique solution modulo their product. Used to **speed up RSA decryption** roughly fourfold by working modulo p and modulo q separately, then recombining.

**Discrete logarithm problem:** given g, p and g^x mod p, recover x. Easy forward by repeated squaring, infeasible backward for large p. This is the hardness assumption behind Diffie-Hellman, ElGamal and DSA.

**Primitive root:** a base whose successive powers modulo p cycle through **every** nonzero remainder before repeating — it generates the whole multiplicative group.

### Exam hooks
- Fermat's applies to prime moduli; Euler's to any modulus. RSA needs Euler's.
- φ(pq) = (p−1)(q−1); φ(p) = p − 1.
- Miller-Rabin is probabilistic; AKS is deterministic.
- CRT speeds up RSA decryption.
- Discrete log is easy forward, hard backward.
- A primitive root generates all nonzero residues.

### Check
1. State Euler's Theorem and say how it relates to Fermat's.
2. Why does RSA's correctness argument need Euler's rather than Fermat's?
3. What is Miller-Rabin used for, and what kind of test is it?

---

# BLOCK 9 — Chapter 9: Public-Key Cryptography and RSA
**30 minutes**

### Frame
The highest-yield chapter in the second half. Know the key generation steps, the two formulas, and which modulus goes where.

### Core

**Diffie and Hellman, 1976** addressed two problems inherent in symmetric cryptography: **secure key distribution without a pre-shared secret**, and the absence of anything equivalent to a **handwritten signature**.

**A trapdoor one-way function** is easy to compute forward, infeasible to invert, and easy to invert *only* with secret extra information — the trapdoor being the private key.

**Two uses of a key pair.**
- **Confidentiality:** encrypt with the **recipient's public** key, decrypt with the recipient's private key.
- **Authentication (signature):** sign with the **sender's private** key, verify with the sender's public key.

For both together: sign first, then encrypt — Z = E(PU_b, E(PR_a, X)).

A message encrypted only with the sender's private key gives authentication but **no confidentiality**, because anyone holding the public key can read it.

**RSA** — Rivest, Shamir, Adleman, 1977. Security rests on the difficulty of **factoring** the product of two large primes.

**Key generation, five steps:**
1. Choose two large distinct primes p and q.
2. Compute n = pq.
3. Compute φ(n) = (p−1)(q−1).
4. Choose e with 1 < e < φ(n) and **gcd(e, φ(n)) = 1**.
5. Compute d as the **multiplicative inverse of e modulo φ(n)**, so e·d ≡ 1 (mod φ(n)).

**Public key is (e, n). Private key is (d, n).**

**Encryption: C = P^e mod n. Decryption: P = C^d mod n.**

**The modulus is n in both. φ(n) appears only during key generation.** Mixing these up is the most common RSA error.

**Why decryption works:** since e·d ≡ 1 (mod φ(n)), we have e·d = 1 + kφ(n), so P^(ed) = P·(P^φ(n))^k, and by **Euler's Theorem** P^φ(n) ≡ 1 (mod n), leaving P.

**Why p, q and φ(n) must stay secret:** any one of them yields d immediately. Worse, knowing n together with φ(n) recovers p and q as the roots of a quadratic. Publishing n is safe only because factoring it is infeasible.

**Attacks and countermeasures.**
- **Timing attack** (Kocher): measures how long decryption takes for different ciphertexts to infer private key bits, because square-and-multiply takes longer when exponent bits are set. Defences: constant-time implementation, or **blinding** — multiply by a random factor before exponentiating and divide it out afterwards.
- **Malleability:** plain RSA satisfies E(M₁)·E(M₂) = E(M₁·M₂), so an attacker can manipulate a ciphertext by a known factor.
- **Low exponent:** e = 3 without padding permits a cube-root attack when the same message goes to several recipients.
- **The fix for all of these is padding:** **OAEP** (Optimal Asymmetric Encryption Padding) randomises the plaintext before encryption, making the scheme probabilistic and non-malleable.

**Why public-key has not replaced symmetric:** it is orders of magnitude slower, so it is confined mainly to signatures and key management. Real systems are **hybrid** — public-key transports a session key, a symmetric cipher carries the data.

### Exam hooks
- The five key generation steps in order.
- Both formulas, with **n** as the modulus.
- Public key (e, n), private key (d, n).
- e coprime to φ(n); d is e's inverse mod φ(n) — two separate conditions.
- Security rests on **factoring**, not discrete logarithms.
- Euler's Theorem is what makes decryption work.
- OAEP randomises plaintext against chosen-ciphertext attacks.
- Timing attacks and blinding.

### Check
1. Write the RSA encryption and decryption formulas, naming the modulus.
2. State both conditions relating e, d and φ(n).
3. What hard problem underlies RSA?
4. What does OAEP do and why?

---

# BLOCK 10 — Chapter 10: Other Public-Key Cryptosystems
**25 minutes**

### Frame
Diffie-Hellman, ElGamal and ECC. ECC and IoT were both flagged in class.

### Core

**Diffie-Hellman key exchange** establishes a **shared secret** over an insecure channel — it does **not** encrypt.

Public parameters, known to everyone including attackers: a large prime **q** and a **primitive root α** of q.

Alice picks secret X_A and sends Y_A = α^(X_A) mod q. Bob picks secret X_B and sends Y_B = α^(X_B) mod q. Alice computes Y_B^(X_A) mod q; Bob computes Y_A^(X_B) mod q. Both equal **α^(X_A·X_B) mod q**, because exponentiation commutes. The shared key is never transmitted, and the private exponents never leave their owners.

Security rests on the **discrete logarithm problem**.

**The man-in-the-middle attack.** The attacker substitutes their own public value in each direction, establishing one key with Alice and a different one with Bob, then relays traffic while reading it. **No discrete logarithm is ever solved** — the protocol is bypassed, not broken, because plain Diffie-Hellman provides **no authentication**. The fix is to authenticate the exchange with **digital signatures and certificates**.

**ElGamal** uses the same discrete-log foundation but actually encrypts. The sender picks a random ephemeral **k** per message, and the ciphertext is a **pair** of values. Reusing k across two messages lets an attacker who knows one plaintext recover the other.

**Elliptic curve cryptography.** Proposed independently in 1985 by Victor Miller and Neal Koblitz.

The curve is **y² = x³ + ax + b**. For cryptography it is defined over a **finite field** — Z_p or GF(2^m) — not the real numbers, so the set of points is finite and discrete.

The points, plus a **point at infinity** serving as the identity, form an **abelian group** under the chord-and-tangent addition rule. Repeated addition is **point multiplication**: kP.

The hard problem is the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**: given P and Q = kP, recover k.

**The practical advantage:** equivalent security at far smaller key sizes — **256-bit ECC ≈ 3072-bit RSA**. The reason is that factorisation admits sub-exponential attacks (the number field sieve), forcing RSA keys to grow, while the best attacks on well-chosen curves remain fully exponential. Smaller keys mean less storage, less bandwidth and cheaper computation, which is why ECC suits **IoT sensors, mobile devices and constrained environments**.

### Exam hooks
- Diffie-Hellman does key **exchange**, not encryption.
- Its public parameters are q and a primitive root α, and both are public.
- Man-in-the-middle succeeds because there is **no authentication**, not because discrete log was solved.
- ElGamal produces a **pair** of ciphertext values and needs a fresh random k.
- ECC's curve equation, the point at infinity as identity, the abelian group.
- ECDLP by name.
- 256-bit ECC matches 3072-bit RSA; ECC suits IoT.
- Miller and Koblitz, 1985.

### Check
1. What does Diffie-Hellman actually establish, and what problem secures it?
2. Why does man-in-the-middle work without solving the discrete logarithm?
3. Name ECC's hard problem and state its main practical advantage.

---

# BLOCK 11 — Chapter 11: Cryptographic Hash Functions
**20 minutes**

### Frame
Three security properties, the birthday bound, and two constructions.

### Core

A hash function maps **variable-length** input to **fixed-length** output — the **message digest**. It is unkeyed, deterministic, and one-way.

**The three security properties.**
- **Preimage resistance**: given a digest h, infeasible to find any x with H(x) = h. The one-way property. Protects stored password hashes.
- **Second preimage resistance**: given a **specific** x, infeasible to find a different x′ with the same digest. Also called weak collision resistance. Protects a named document from substitution.
- **Collision resistance**: infeasible to find **any** colliding pair, with both inputs free. Also called strong collision resistance. Protects signatures.

**Collision resistance is the weakest** — not because the requirement is mild, but because the attacker has the most freedom. Both inputs are free, so the **birthday attack** applies: a collision is expected after about 2^(n/2) attempts rather than 2^n. An **n-bit digest therefore gives only n/2 bits of collision security**, which is why digests must be **twice** the intended security level. SHA-256 gives 128 bits against collisions.

**Applications:** message and file integrity, digital signatures, MACs, one-way password files, intrusion and virus detection, PRNG construction. Hashing does **not** provide confidentiality — it is not encryption and cannot be reversed.

**Merkle-Damgård** is the iterative construction behind MD5, SHA-1 and SHA-2: pad the message, split into blocks, and iterate a **compression function**, carrying a chaining value forward; the final chaining value is the digest. Its weakness is the **length extension attack** — because the digest *is* the final chaining state, an attacker knowing H(M) and the length of M can append data and compute a valid digest without knowing M.

**SHA-3 / Keccak** uses the **sponge construction**: an **absorbing** phase XORs message blocks into a large internal state, then a **squeezing** phase extracts output. Because the state is larger than the output, the digest does not reveal the full state, which **eliminates length extension**. SHA-3 was chosen for structural diversity rather than because SHA-2 was broken.

**Digest sizes:** SHA-1 gives **one hundred and sixty** bits and is retired after practical collisions in 2017. SHA-256 gives **two hundred and fifty-six**; SHA-512 gives **five hundred and twelve**.

### Exam hooks
- All three properties by name, and which is weakest and why.
- The birthday bound: n-bit digest, n/2 bits of collision security, digest must be double the security target.
- Merkle-Damgård versus sponge, and which resists length extension.
- SHA-1 is 160 bits; SHA-3 is Keccak.
- Hashing provides integrity, never confidentiality.

### Check
1. Name the three properties and say which the birthday attack targets.
2. Why must a digest be twice the desired security level?
3. Which construction suffers length extension, and which fixes it?

---

# BLOCK 12 — Chapter 12: Message Authentication Codes
**15 minutes**

### Frame
Short chapter. The hash-versus-MAC distinction and HMAC's structure are the whole of it.

### Core

**A MAC is a keyed checksum:** MAC = C(K, M), where K is a secret shared by sender and receiver. The receiver recomputes and compares.

**Why a plain hash is not enough.** A hash is unkeyed, so an attacker on the channel can alter the message, recompute the digest, and forward both — verification succeeds. A hash detects **accidental** corruption but not **deliberate** modification. A MAC's key means only key holders can produce a valid tag.

A MAC provides **integrity and authentication**. It gives **no confidentiality** — the message travels in the clear alongside the tag. And it **cannot provide non-repudiation**, because the key is shared: either party could have produced any tag, so a third party cannot attribute it.

**HMAC** is the standard construction, wrapping any hash function:

> HMAC(K, M) = H((K ⊕ **opad**) ‖ H((K ⊕ **ipad**) ‖ M))

The two padding constants are **ipad (0x36)** and **opad (0x5C)**. The nesting exists because the naive H(K ‖ M) falls to the **length extension attack** — an attacker could append data and forge a tag without knowing K. The outer hash hides the inner chaining state, closing that route. HMAC treats the hash as a black box, so it works with any hash function, and its security depends on the **underlying hash**.

**CMAC** is the block-cipher-based MAC, using a cipher such as AES in CBC mode with derived subkeys. Its predecessor **DAA** used DES in CBC mode with a zero IV and had a length-extension weakness that CMAC fixes.

**Authenticated encryption** provides confidentiality and authenticity in one scheme. **CCM** = Counter with CBC-MAC. **GCM** = Galois/Counter Mode, combining CTR encryption with GHASH authentication in GF(2^128); GCM is the high-throughput choice because GHASH parallelises.

### Exam hooks
- MAC is keyed; hash is not. That single fact answers several questions.
- A MAC cannot give non-repudiation, because the key is shared.
- HMAC's ipad and opad, and why it nests.
- HMAC's security rests on the underlying **hash**, not on a block cipher.
- CCM and GCM expansions, and that both are authenticated encryption.
- A replay attack on a MAC-protected message is countered by a **sequence number or timestamp**.

### Check
1. What can a MAC provide that a hash cannot, and what can it still not provide?
2. Name HMAC's two padding constants and explain why it nests.
3. What do CCM and GCM stand for?

---

# BLOCK 13 — Chapter 13: Digital Signatures
**20 minutes**

### Frame
The chapter that completes the picture: what a MAC could not do.

### Core

**A digital signature** is created with the signer's **private** key and verified with their **public** key. It provides **authentication, integrity and non-repudiation** — the last being exactly what a MAC cannot offer, because only one party holds the private key and verification is public.

**The message is hashed before signing.** Two reasons: signing operations are expensive and size-limited, so hashing reduces the work to one small fixed-size value; and the digest commits to the **entire document as a single indivisible unit**, avoiding the splicing attacks that per-block signatures would invite.

**Signature security depends on the hash's collision resistance.** Because the signature covers the digest, any two messages sharing a digest share a valid signature. An attacker who can construct a collision gets an innocuous document signed, then attaches that signature to a malicious one — without ever touching the private key. A scheme's real strength is the **minimum** of the signing algorithm's strength and the hash's collision resistance. This is why SHA-1's collision break invalidated signatures built on it.

**Forgery levels**, weakest to strongest for the attacker:
- **Existential forgery** — a valid signature on *some* message, with no control over its content.
- **Selective forgery** — a valid signature on a message the attacker chose.
- **Total break** — the attacker recovers the private key and can sign anything.

**Schemes.**
- **RSA signature:** sign with the private exponent, verify with the public one — RSA with the roles of e and d swapped.
- **RSA-PSS** — Probabilistic Signature Scheme, by Bellare and Rogaway. Textbook RSA signing is **deterministic** and vulnerable to existential forgery; PSS adds a **random salt** and structured padding, making signing probabilistic and provably secure.
- **ElGamal signature** — discrete-log based, needs a fresh random k per signature.
- **Schnorr** — discrete-log based, valued for efficiency and a simple structure.
- **DSA / DSS** — the NIST standard (FIPS 186), based on **discrete logarithms**, not factoring. Uses a per-message random **k** and outputs a pair **(r, s)**.
- **ECDSA** — DSA over elliptic curves, giving equal security with much shorter keys and signatures.

**Deterministic versus randomised signing** was flagged in class. Textbook RSA is deterministic: the same message always gives the same signature. DSA, ECDSA, ElGamal and RSA-PSS are randomised, each using a fresh per-message random value. The randomness is essential — **reusing k in DSA or ECDSA leaks the private key outright.**

**Certificates and identity.** A signature proves only that the private key holder signed. It says nothing about **who** that holder is. Binding a public key to a real identity requires a **certificate** issued by a **Certificate Authority** within a **PKI**, in the **X.509** format. Without that binding, an attacker can generate their own key pair and sign fraudulently. This is the same missing property that makes Diffie-Hellman vulnerable to man-in-the-middle, appearing in a second context.

### Exam hooks
- Sign with private, verify with public.
- Non-repudiation is the service a MAC cannot supply.
- Why hash before signing — efficiency plus whole-document commitment.
- DSA rests on **discrete logarithms**; RSA on factoring.
- The three forgery levels.
- RSA-PSS is probabilistic; textbook RSA signing is deterministic.
- Reusing the per-message k leaks the private key.
- X.509 binds a public key to an identity; the CA signs it.

### Check
1. Which key signs and which verifies?
2. Why does signature security depend on the hash's collision resistance?
3. What hard problem underlies DSA?
4. Name the three forgery levels in order of severity.

---

# FINAL SWEEP — 30 minutes

Answer these closed-book. They are the items most likely to appear and most likely to be misremembered.

1. The six X.800 security services.
2. The four active attack types.
3. Both Feistel round equations.
4. Confusion versus diffusion — which is substitution, which is permutation.
5. DES: block size, effective key size, number of rounds, number of S-boxes.
6. The one property a field has that a ring may lack.
7. The AES irreducible polynomial.
8. The four AES transformations in order, and which is dropped in the final round.
9. Why AES is not a Feistel cipher.
10. The five modes of operation.
11. OFB feeds back what? CFB feeds back what?
12. IV requirement versus counter requirement.
13. Triple DES effective key lengths, two-key and three-key.
14. RC4's two phases and its state array size.
15. Euler's Theorem, and why RSA needs it rather than Fermat's.
16. RSA encryption and decryption formulas, with the modulus named.
17. Both conditions relating e, d and φ(n).
18. What hard problem underlies RSA? Diffie-Hellman? ECC?
19. Why man-in-the-middle defeats Diffie-Hellman without solving discrete log.
20. 256-bit ECC is equivalent to how many bits of RSA?
21. The three hash security properties, and which the birthday attack targets.
22. Merkle-Damgård versus sponge — which resists length extension?
23. HMAC's two padding constants.
24. What can a MAC not provide, and why?
25. Which key signs a document, and which verifies it?

Anything you miss goes on a single sheet of paper. Read that sheet, not the book, in the hour before the exam.

---

# EXAM-DAY REMINDERS

**Write numbers as words.** Sixteen rounds, not 16. Stated explicitly in class.

**Fill-ins want the exact technical term.** ShiftRows, not "the row shifting one". MixColumns, not "column mixing".

**Do not spend essay time on preamble.** Open by answering the question. "Security is important in today's world" earns nothing.

**Watch the classic distractors.** AES is not Feistel. DES does not shift rows. The RSA modulus is n, not φ(n). Traffic analysis is passive. DSA uses discrete logs, not factoring. A MAC cannot give non-repudiation.

**If time runs short on an essay**, write the skeleton as a bullet list. A marker can award partial credit for structure and points you did not reach; they cannot award anything for a blank.
