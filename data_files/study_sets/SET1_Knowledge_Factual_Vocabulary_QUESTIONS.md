# DCIT418 MOCK — SET 1
## Knowledge, Factual Recall & Vocabulary
**Chapters 1–13 | Time limit: 75 minutes | Closed book**

Write your answers on paper. Do not check the answer key until you have attempted every question.

Chapters 11–13 material sits at the end of each section, clearly marked. Skip those parts until the hash, MAC and signature blocks have been taught.

---

## SECTION A — MULTIPLE CHOICE (40 marks, 1 mark each)

Circle or write the letter of the best answer.

**A1.** Which of the following is NOT one of the three pillars of the OSI Security Architecture?
a) Security Attack
b) Security Mechanism
c) Security Service
d) Security Protocol

**A2.** Traffic analysis is classified as:
a) An active attack
b) A passive attack
c) A denial of service attack
d) A masquerade attack

**A3.** The defensive emphasis for passive attacks is on:
a) Detection
b) Recovery
c) Prevention
d) Retaliation

**A4.** Which security service assures that a communicating entity is who it claims to be?
a) Access Control
b) Data Integrity
c) Authentication
d) Non-repudiation

**A5.** In the symmetric cipher model, which component is independent of both the plaintext and the algorithm?
a) The ciphertext
b) The secret key
c) The decryption algorithm
d) The encryption algorithm

**A6.** A monoalphabetic substitution cipher is primarily broken using:
a) Brute force on the key length
b) Frequency analysis
c) Differential cryptanalysis
d) The birthday attack

**A7.** The Playfair cipher operates on:
a) Single letters
b) Digraphs (letter pairs)
c) Trigraphs
d) Whole words

**A8.** Which cipher is theoretically unbreakable when used correctly?
a) Vigenère cipher
b) Playfair cipher
c) One-Time Pad (Vernam)
d) Rail Fence cipher

**A9.** The Rail Fence cipher is an example of a:
a) Substitution technique
b) Transposition technique
c) Polyalphabetic technique
d) Product cipher

**A10.** DES has a block size of:
a) 32 bits
b) 56 bits
c) 64 bits
d) 128 bits

**A11.** The effective key length of DES is:
a) 48 bits
b) 56 bits
c) 64 bits
d) 128 bits

**A12.** In a Feistel cipher, decryption is achieved by:
a) Running a completely separate decryption algorithm
b) Running the same algorithm with the subkeys in reverse order
c) Inverting each S-box
d) Reversing the initial permutation only

**A13.** How many rounds does DES have?
a) 8
b) 10
c) 16
d) 32

**A14.** The only nonlinear component of the DES round function is the:
a) Expansion permutation
b) S-box substitution
c) P-box permutation
d) Subkey XOR

**A15.** The avalanche effect refers to:
a) Key size doubling security
b) A small input change producing a large output change
c) The cascading of block cipher modes
d) Error propagation across blocks

**A16.** GF(p) is a finite field only when p is:
a) Even
b) Odd
c) Prime
d) A power of 2

**A17.** The multiplicative inverse of a mod n exists only if:
a) a < n
b) gcd(a, n) = 1
c) n is even
d) a is prime

**A18.** In a field, but NOT necessarily in a ring:
a) Addition is associative
b) Multiplication distributes over addition
c) Every nonzero element has a multiplicative inverse
d) There is an additive identity

**A19.** AES has a fixed block size of:
a) 64 bits
b) 128 bits
c) 192 bits
d) 256 bits

**A20.** AES-192 uses how many rounds?
a) 10
b) 12
c) 14
d) 16

**A21.** AES is best described as:
a) A Feistel cipher
b) A stream cipher
c) A substitution-permutation network (SPN)
d) A transposition cipher

**A22.** Which AES transformation is omitted in the final round?
a) SubBytes
b) ShiftRows
c) MixColumns
d) AddRoundKey

**A23.** Which block cipher mode should NOT be used for long messages because identical plaintext blocks produce identical ciphertext blocks?
a) CBC
b) ECB
c) CFB
d) CTR

**A24.** Which mode allows blocks to be decrypted out of order (random access)?
a) CBC
b) CFB
c) OFB
d) CTR

**A25.** In CFB and OFB modes, decryption uses:
a) The decryption function D only
b) The encryption function E
c) Both E and D
d) Neither, it uses a separate keystream cipher

**A26.** RC4 stands for:
a) Rotational Cipher 4
b) Rivest Cipher 4
c) Random Cipher 4
d) Round Cipher 4

**A27.** Euler's totient function φ(n) for n = p × q (distinct primes) equals:
a) pq
b) p + q
c) (p−1)(q−1)
d) (p+1)(q+1)

**A28.** Fermat's Little Theorem states that for prime p and a not divisible by p:
a) a^p ≡ 1 (mod p)
b) a^(p−1) ≡ 1 (mod p)
c) a^(p+1) ≡ a (mod p)
d) a^φ(p) ≡ 0 (mod p)

**A29.** The security of RSA rests on the difficulty of:
a) The discrete logarithm problem
b) Factoring large integers
c) Solving elliptic curve equations
d) Inverting hash functions

**A30.** The security of Diffie-Hellman rests on the difficulty of:
a) Factoring large integers
b) The discrete logarithm problem
c) Frequency analysis
d) The birthday problem

### Chapters 11–13

**A31.** A cryptographic hash function maps:
a) Fixed-length input to variable-length output
b) Variable-length input to fixed-length output
c) Fixed-length input to fixed-length output
d) Variable-length input to variable-length output

**A32.** Given a digest h, the infeasibility of finding any input x with H(x) = h is:
a) Collision resistance
b) Second preimage resistance
c) Preimage resistance
d) Avalanche

**A33.** Given a specific input x, the infeasibility of finding a different x′ with the same digest is:
a) Preimage resistance
b) Second preimage resistance
c) Collision resistance
d) Diffusion

**A34.** The birthday attack reduces the effective security of an n-bit digest to approximately:
a) n bits
b) n/2 bits
c) n/4 bits
d) 2n bits

**A35.** SHA-3 is built on which construction?
a) Merkle-Damgård
b) Feistel
c) Sponge
d) Substitution-permutation network

**A36.** Which attack specifically affects Merkle-Damgård hashes but not sponge constructions?
a) Birthday attack
b) Length extension attack
c) Differential cryptanalysis
d) Replay attack

**A37.** A message authentication code differs from a plain hash because it:
a) Produces a longer digest
b) Uses a secret key
c) Is reversible
d) Is faster to compute

**A38.** HMAC uses two padding constants known as:
a) salt and pepper
b) ipad and opad
c) nonce and counter
d) seed and mask

**A39.** Which service can a digital signature provide that a MAC cannot?
a) Data integrity
b) Authentication
c) Non-repudiation
d) Confidentiality

**A40.** In producing a digital signature, the message is normally hashed first because:
a) It encrypts the message
b) It fixes the input size and improves efficiency
c) It provides confidentiality
d) It is required by law

---

## SECTION B — FILL IN THE BLANKS (40 marks, 1 mark each)

**B1.** The three core objectives of computer security, known as the CIA triad, are ______________, ______________, and ______________.

**B2.** Two additional security objectives beyond the CIA triad mentioned by Stallings are ______________ and ______________.

**B3.** The four types of active attack are ______________, ______________, ______________, and ______________.

**B4.** The two types of passive attack are ______________ and ______________.

**B5.** The six X.800 security service categories are ______________, ______________, ______________, ______________, ______________, and ______________.

**B6.** The Caesar cipher encryption formula is C = ______________.

**B7.** The Vigenère cipher is classified as a ______________ substitution cipher.

**B8.** For a one-time pad to be unbreakable, the key must be ______________, ______________ as the message, and used ______________.

**B9.** The two Feistel round equations are L_i = ______________ and R_i = ______________.

**B10.** In the DES round function, the 32-bit right half is expanded to ______________ bits before being XORed with the subkey.

**B11.** DES uses ______________ S-boxes, each taking ______________ bits in and producing ______________ bits out.

**B12.** The Euclidean algorithm computes the ______________ of two integers.

**B13.** A set with one operation satisfying closure, associativity, identity, and inverse is called a ______________.

**B14.** A group that is also commutative is called an ______________ group.

**B15.** The irreducible polynomial used as the modulus in AES's GF(2^8) arithmetic is ______________.

**B16.** In GF(2^n), polynomial addition is equivalent to the bitwise ______________ operation.

**B17.** The four AES round transformations, in order, are ______________, ______________, ______________, and ______________.

**B18.** AES treats the 128-bit block as a 4×4 matrix of bytes called the ______________.

**B19.** In AES, the only transformation that uses the secret key is ______________.

**B20.** The five block cipher modes of operation covered are ______________, ______________, ______________, ______________, and ______________.

**B21.** In CBC mode, the first plaintext block is XORed with the ______________ before encryption.

**B22.** In CTR mode, the value that must never repeat with the same key is the ______________.

**B23.** The CBC encryption formula is C_i = ______________.

**B24.** The two phases of RC4 are ______________ and ______________.

**B25.** RC4's internal state array S contains ______________ bytes.

**B26.** Euler's Theorem states that if gcd(a,n) = 1, then ______________.

**B27.** The RSA public key consists of the pair ______________ and the private key consists of ______________.

**B28.** The RSA encryption formula is C = ______________ and the decryption formula is P = ______________.

**B29.** In Diffie-Hellman, the two public parameters agreed upon in advance are a large prime ______________ and a ______________ of that prime.

**B30.** The hard problem underlying elliptic curve cryptography is called the ______________.

### Chapters 11–13

**B31.** A cryptographic hash function takes ______________-length input and produces ______________-length output.

**B32.** The three required security properties of a cryptographic hash function are ______________, ______________ and ______________.

**B33.** The attack exploiting the probability of collisions rather than exhaustive search is the ______________ attack.

**B34.** For an n-bit digest, that attack reduces effective collision security to approximately ______________ bits.

**B35.** SHA-1 and SHA-2 use the ______________ construction, while SHA-3 uses the ______________ construction.

**B36.** The attack that affects the first of those constructions but not the second is the ______________ attack.

**B37.** A keyed hash used to provide message authentication is called a ______________.

**B38.** The standard nested construction for building one from a hash function is ______________, and its two padding constants are ______________ and ______________.

**B39.** A MAC provides ______________ and ______________, but cannot provide ______________.

**B40.** A digital signature is produced using the sender's ______________ key and verified using the sender's ______________ key.

---

## SECTION C — SHORT ANSWER (50 marks)

Answer in 2–4 sentences each unless stated otherwise.

**C1.** (3 marks) Distinguish between a security attack, a security mechanism, and a security service.

**C2.** (3 marks) Explain why passive attacks are defended against by prevention while active attacks are defended against by detection and recovery.

**C3.** (3 marks) Explain why the one-time pad is theoretically unbreakable, and state why it is impractical.

**C4.** (4 marks) State the two Feistel round equations and explain why the same algorithm can be used for both encryption and decryption.

**C5.** (3 marks) List five parameters that determine the security and performance of a Feistel cipher.

**C6.** (3 marks) Why is DES with a 56-bit key considered insecure today? What was the direct successor designed to address this?

**C7.** (4 marks) Define a group, a ring, and a field, stating the key structural difference between a ring and a field.

**C8.** (3 marks) Explain why GF(2^n) requires an irreducible polynomial as its modulus, drawing the parallel to GF(p).

**C9.** (4 marks) Name the four AES round transformations and give a one-line description of what each does.

**C10.** (3 marks) Explain why AES is not a Feistel cipher.

**C11.** (3 marks) Why is MixColumns omitted from the final AES round?

**C12.** (4 marks) Explain why ECB mode is insecure for long messages. Reference the mathematics, not just "patterns leak."

**C13.** (3 marks) Explain why decryption in CFB mode uses the encryption function E rather than the decryption function D.

**C14.** (3 marks) Distinguish between the role of an IV in CBC/CFB/OFB and the role of the counter in CTR mode.

**C15.** (3 marks) Distinguish between a PRNG and a CSPRNG. Why is a linear congruential generator unsuitable for cryptography?

**C16.** (3 marks) Describe the two phases of RC4 and what each accomplishes. Why has RC4 been deprecated?

**C17.** (4 marks) State Fermat's Little Theorem and Euler's Theorem, and explain the relationship between them.

**C18.** (4 marks) List the five steps of RSA key generation in order.

**C19.** (3 marks) State both conditions that relate e, d, and φ(n) in RSA, and explain why the second depends on the first.

**C20.** (3 marks) Describe the man-in-the-middle attack on plain Diffie-Hellman and explain what property of the protocol makes it possible.

**C21.** (3 marks) State the main practical advantage of elliptic curve cryptography over RSA, with an example of comparable key sizes.

### Chapters 11–13

**C22.** (4 marks) Define the three security properties required of a cryptographic hash function and give one practical application that depends on each.

**C23.** (3 marks) Explain the birthday attack and why collision resistance is the weakest of the three hash properties.

**C24.** (3 marks) List four applications of cryptographic hash functions.

**C25.** (3 marks) Distinguish between the Merkle-Damgård and sponge constructions, and name one attack the second resists.

**C26.** (4 marks) Explain why a plain hash alone cannot provide message authentication over an insecure channel, and how a MAC solves this.

**C27.** (3 marks) Describe the structure of HMAC at a high level and state why it nests the hash function rather than simply appending the key.

**C28.** (4 marks) Explain why a MAC cannot provide non-repudiation while a digital signature can, referencing the key structure of each.

---

**END OF SET 1**
