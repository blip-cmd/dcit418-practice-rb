# DCIT418 — SET 4: MCQ Drill (Parser Format)

100 questions from the SET4 MCQ practice examination, formatted for parse_security_bank.py.

### 1. Which is NOT part of the CIA triad?

- A. Confidentiality
- B. Integrity
- C. Authentication
- D. Availability

**Correct Answer:** **C. Authentication**

**Reason:** CIA is Confidentiality, Integrity, Availability. Authentication is an additional objective, not part of the triad.

---

### 2. Assuring that a communicating entity is who it claims to be is:

- A. Integrity
- B. Authentication
- C. Access control
- D. Availability

**Correct Answer:** **B. Authentication**

**Reason:** Authentication.

---

### 3. Traffic analysis is:

- A. An active attack
- B. A passive attack
- C. A denial of service
- D. A masquerade

**Correct Answer:** **B. A passive attack**

**Reason:** Passive — observation without alteration.

---

### 4. Which attack type is hardest to prevent but easiest to detect?

- A. Passive
- B. Active
- C. Both equally
- D. Neither

**Correct Answer:** **B. Active**

**Reason:** Active attacks alter state so they are detectable, but the attack surface is too broad to prevent absolutely.

---

### 5. The three pillars of the OSI Security Architecture are attack, mechanism and:

- A. Protocol
- B. Policy
- C. Service
- D. Standard

**Correct Answer:** **C. Service**

**Reason:** Attack, mechanism, service.

---

### 6. Replay attacks fall under:

- A. Passive attacks
- B. Active attacks
- C. Traffic analysis
- D. Steganography

**Correct Answer:** **B. Active attacks**

**Reason:** Replay alters the communication, so it is active.

---

### 7. Which service prevents a sender denying having sent a message?

- A. Access control
- B. Data integrity
- C. Non-repudiation
- D. Authentication

**Correct Answer:** **C. Non-repudiation**

**Reason:** Non-repudiation.

---

### 8. System integrity refers to:

- A. Data being unmodified
- B. The system performing as intended, unimpaired
- C. Uptime percentage
- D. Access logging

**Correct Answer:** **B. The system performing as intended, unimpaired**

**Reason:** System integrity concerns the system functioning unimpaired; data integrity concerns the data.

---

### 9. The five components of the symmetric cipher model include all EXCEPT:

- A. Plaintext
- B. Secret key
- C. Public key
- D. Ciphertext

**Correct Answer:** **C. Public key**

**Reason:** The symmetric model has no public key.

---

### 10. The Caesar cipher is a:

- A. Transposition cipher
- B. Monoalphabetic substitution
- C. Polyalphabetic substitution
- D. Product cipher

**Correct Answer:** **B. Monoalphabetic substitution**

**Reason:** A fixed shift is monoalphabetic.

---

### 11. The Playfair cipher encrypts:

- A. Single letters
- B. Digraphs
- C. Trigraphs
- D. Whole words

**Correct Answer:** **B. Digraphs**

**Reason:** Digraphs via the 5×5 matrix.

---

### 12. In the Playfair 5×5 matrix, which letters are combined?

- A. U and V
- B. I and J
- C. C and K
- D. X and Y

**Correct Answer:** **B. I and J**

**Reason:** I and J share a cell.

---

### 13. The Vigenère cipher resists frequency analysis because it is:

- A. A transposition cipher
- B. Polyalphabetic
- C. Unbreakable
- D. A block cipher

**Correct Answer:** **B. Polyalphabetic**

**Reason:** Polyalphabetic — one plaintext letter maps to several ciphertext letters.

---

### 14. A cipher offering perfect secrecy is:

- A. Vigenère
- B. Playfair
- C. One-time pad
- D. Rail Fence

**Correct Answer:** **C. One-time pad**

**Reason:** One-time pad.

---

### 15. The Rail Fence cipher is an example of:

- A. Substitution
- B. Transposition
- C. Steganography
- D. A rotor machine

**Correct Answer:** **B. Transposition**

**Reason:** Reorders without substituting.

---

### 16. Steganography differs from cryptography in that it:

- A. Uses stronger keys
- B. Conceals the existence of the message
- C. Is always unbreakable
- D. Requires no key

**Correct Answer:** **B. Conceals the existence of the message**

**Reason:** Steganography hides that a message exists at all.

---

### 17. Rotor machines were significant because they:

- A. Introduced public-key cryptography
- B. Implemented complex polyalphabetic substitution mechanically
- C. Used transposition only
- D. Were unbreakable

**Correct Answer:** **B. Implemented complex polyalphabetic substitution mechanically**

**Reason:** Mechanical polyalphabetic substitution with a very long effective period.

---

### 18. A brute-force attack on a monoalphabetic cipher is impractical, yet the cipher is weak because:

- A. The key is too short
- B. Letter frequencies survive encryption
- C. It uses transposition
- D. The algorithm is secret

**Correct Answer:** **B. Letter frequencies survive encryption**

**Reason:** Frequency analysis, not brute force, is the attack.

---

### 19. DES block size is:

- A. 32 bits
- B. 56 bits
- C. 64 bits
- D. 128 bits

**Correct Answer:** **C. 64 bits**

**Reason:** 64 bits.

---

### 20. DES effective key size is:

- A. 48 bits
- B. 56 bits
- C. 64 bits
- D. 128 bits

**Correct Answer:** **B. 56 bits**

**Reason:** 56 effective; 64 stored with 8 parity bits.

---

### 21. The number of DES rounds is:

- A. 8
- B. 10
- C. 16
- D. 32

**Correct Answer:** **C. 16**

**Reason:** 16.

---

### 22. In a Feistel cipher, decryption uses:

- A. A separate inverse algorithm
- B. The same algorithm with subkeys reversed
- C. Inverted S-boxes
- D. A different key entirely

**Correct Answer:** **B. The same algorithm with subkeys reversed**

**Reason:** Same algorithm, reversed subkey order.

---

### 23. The only nonlinear element of the DES round function is:

- A. Expansion
- B. The S-boxes
- C. The P-box
- D. The subkey XOR

**Correct Answer:** **B. The S-boxes**

**Reason:** S-boxes. Everything else is linear.

---

### 24. The DES initial permutation contributes:

- A. Confusion
- B. Diffusion
- C. Nothing cryptographically
- D. Key mixing

**Correct Answer:** **C. Nothing cryptographically**

**Reason:** IP and IP⁻¹ are key-independent and public, so they add no security.

---

### 25. The avalanche effect means:

- A. Errors cascade across blocks
- B. A small input change causes a large output change
- C. Keys grow with rounds
- D. Encryption slows over time

**Correct Answer:** **B. A small input change causes a large output change**

**Reason:** Small in, large out.

---

### 26. Claude Shannon's two principles of cipher design are:

- A. Speed and simplicity
- B. Confusion and diffusion
- C. Substitution and rotation
- D. Entropy and redundancy

**Correct Answer:** **B. Confusion and diffusion**

**Reason:** Confusion and diffusion.

---

### 27. Diffusion refers to:

- A. Hiding the relationship between key and ciphertext
- B. Spreading plaintext statistics across the ciphertext
- C. Slowing encryption
- D. Expanding key length

**Correct Answer:** **B. Spreading plaintext statistics across the ciphertext**

**Reason:** Diffusion spreads plaintext statistics.

---

### 28. Confusion refers to:

- A. Obscuring the relationship between key and ciphertext
- B. Spreading plaintext statistics
- C. Random padding
- D. Key rotation

**Correct Answer:** **A. Obscuring the relationship between key and ciphertext**

**Reason:** Confusion obscures the key–ciphertext relationship.

---

### 29. In the DES round function, the right half is expanded from 32 bits to:

- A. 40
- B. 48
- C. 56
- D. 64

**Correct Answer:** **B. 48**

**Reason:** 48, to match the subkey width.

---

### 30. DES S-boxes take how many bits in and out?

- A. 4 in, 6 out
- B. 6 in, 4 out
- C. 8 in, 4 out
- D. 6 in, 6 out

**Correct Answer:** **B. 6 in, 4 out**

**Reason:** 6 in, 4 out, eight of them, 48 → 32.

---

### 31. GF(p) is a field only when p is:

- A. Even
- B. Odd
- C. Prime
- D. Composite

**Correct Answer:** **C. Prime**

**Reason:** Prime.

---

### 32. A multiplicative inverse of a mod n exists only if:

- A. a < n
- B. gcd(a, n) = 1
- C. n is even
- D. a is prime

**Correct Answer:** **B. gcd(a, n) = 1**

**Reason:** gcd = 1.

---

### 33. A set with one operation satisfying closure, associativity, identity and inverse is a:

- A. Ring
- B. Field
- C. Group
- D. Lattice

**Correct Answer:** **C. Group**

**Reason:** Group.

---

### 34. A commutative group is called:

- A. Cyclic
- B. Abelian
- C. Finite
- D. Simple

**Correct Answer:** **B. Abelian**

**Reason:** Abelian.

---

### 35. The key property a field has that a ring may lack is:

- A. Associativity
- B. Distributivity
- C. Multiplicative inverses for all nonzero elements
- D. An additive identity

**Correct Answer:** **C. Multiplicative inverses for all nonzero elements**

**Reason:** Multiplicative inverses for every nonzero element.

---

### 36. In GF(2ⁿ), polynomial addition is equivalent to:

- A. Integer addition
- B. XOR
- C. AND
- D. Rotation

**Correct Answer:** **B. XOR**

**Reason:** XOR.

---

### 37. The AES irreducible polynomial is:

- A. x⁸+x⁴+x³+x+1
- B. x⁸+x⁴+x²+1
- C. x⁴+x+1
- D. x⁸+x⁷+x+1

**Correct Answer:** **A. x⁸+x⁴+x³+x+1**

**Reason:** x⁸+x⁴+x³+x+1. Note the x⁴ term and the trailing 1.

---

### 38. An irreducible polynomial plays the role in GF(2ⁿ) that is played in GF(p) by:

- A. The identity element
- B. A prime modulus
- C. The generator
- D. The order

**Correct Answer:** **B. A prime modulus**

**Reason:** A prime modulus. Irreducible is the polynomial analogue of prime.

---

### 39. The Euclidean algorithm computes:

- A. Modular inverses directly
- B. The greatest common divisor
- C. Prime factorisations
- D. Discrete logarithms

**Correct Answer:** **B. The greatest common divisor**

**Reason:** GCD.

---

### 40. The extended Euclidean algorithm is used in cryptography chiefly to:

- A. Test primality
- B. Find multiplicative inverses
- C. Generate random numbers
- D. Compute hashes

**Correct Answer:** **B. Find multiplicative inverses**

**Reason:** Multiplicative inverses — used to compute d in RSA.

---

### 41. AES block size is always:

- A. 64 bits
- B. 128 bits
- C. 192 bits
- D. Variable

**Correct Answer:** **B. 128 bits**

**Reason:** 128 bits always, whatever the key size.

---

### 42. AES-192 uses how many rounds?

- A. 10
- B. 12
- C. 14
- D. 16

**Correct Answer:** **B. 12**

**Reason:** 12.

---

### 43. AES is structurally:

- A. A Feistel cipher
- B. A substitution-permutation network
- C. A stream cipher
- D. A transposition cipher

**Correct Answer:** **B. A substitution-permutation network**

**Reason:** SPN.

---

### 44. The AES State is arranged as:

- A. A 4×4 matrix of bytes
- B. An 8×8 matrix of bits
- C. A 16-byte vector
- D. Two 64-bit halves

**Correct Answer:** **A. A 4×4 matrix of bytes**

**Reason:** 4×4 byte matrix, filled column by column.

---

### 45. Which AES transformation provides nonlinearity?

- A. ShiftRows
- B. MixColumns
- C. SubBytes
- D. AddRoundKey

**Correct Answer:** **C. SubBytes**

**Reason:** SubBytes.

---

### 46. Which AES transformation is omitted in the final round?

- A. SubBytes
- B. ShiftRows
- C. MixColumns
- D. AddRoundKey

**Correct Answer:** **C. MixColumns**

**Reason:** MixColumns.

---

### 47. The only AES transformation using the secret key is:

- A. SubBytes
- B. ShiftRows
- C. MixColumns
- D. AddRoundKey

**Correct Answer:** **D. AddRoundKey**

**Reason:** AddRoundKey.

---

### 48. In ShiftRows, row 3 is cyclically shifted by:

- A. 0 bytes
- B. 1 byte
- C. 2 bytes
- D. 3 bytes

**Correct Answer:** **D. 3 bytes**

**Reason:** Rows shift by 0, 1, 2, 3 respectively.

---

### 49. The AES S-box is constructed using:

- A. Random selection
- B. Multiplicative inverses in GF(2⁸) plus an affine transformation
- C. A Feistel function
- D. A linear congruential generator

**Correct Answer:** **B. Multiplicative inverses in GF(2⁸) plus an affine transformation**

**Reason:** GF(2⁸) inverse plus affine transformation.

---

### 50. AES key expansion produces how many round keys for AES-128?

- A. 10
- B. 11
- C. 12
- D. 14

**Correct Answer:** **B. 11**

**Reason:** 11 — one initial AddRoundKey plus ten rounds.

---

### 51. Which mode encrypts each block independently?

- A. CBC
- B. ECB
- C. CFB
- D. CTR

**Correct Answer:** **B. ECB**

**Reason:** ECB.

---

### 52. Which mode is unsuitable for long messages due to pattern leakage?

- A. ECB
- B. CBC
- C. OFB
- D. CTR

**Correct Answer:** **A. ECB**

**Reason:** ECB.

---

### 53. In CBC, the first plaintext block is XORed with:

- A. The key
- B. The IV
- C. A counter
- D. Nothing

**Correct Answer:** **B. The IV**

**Reason:** The IV.

---

### 54. Which mode allows random-access decryption?

- A. CBC
- B. CFB
- C. OFB
- D. CTR

**Correct Answer:** **D. CTR**

**Reason:** CTR — counters are independent.

---

### 55. In OFB the keystream is produced by encrypting:

- A. The plaintext
- B. The previous ciphertext
- C. The previous keystream block
- D. A counter

**Correct Answer:** **C. The previous keystream block**

**Reason:** The previous keystream block, which is why OFB cannot parallelise.

---

### 56. In CFB the keystream is produced by encrypting:

- A. The plaintext
- B. The previous ciphertext
- C. The previous keystream
- D. A counter

**Correct Answer:** **B. The previous ciphertext**

**Reason:** The previous ciphertext block.

---

### 57. Which modes do NOT propagate errors?

- A. ECB and CBC
- B. CBC and CFB
- C. OFB and CTR
- D. CFB and OFB

**Correct Answer:** **C. OFB and CTR**

**Reason:** OFB and CTR.

---

### 58. CFB decryption uses:

- A. The decryption function D
- B. The encryption function E
- C. Both
- D. Neither

**Correct Answer:** **B. The encryption function E**

**Reason:** E — it only ever generates keystream.

---

### 59. The counter in CTR must above all be:

- A. Secret
- B. Unique with a given key
- C. Prime
- D. Even

**Correct Answer:** **B. Unique with a given key**

**Reason:** Unique with a given key. Unpredictability is the IV's requirement, not the counter's.

---

### 60. Triple DES applies DES:

- A. Twice with one key
- B. Three times
- C. Once with a tripled key
- D. In parallel

**Correct Answer:** **B. Three times**

**Reason:** Three times.

---

### 61. Triple DES remains limited because of its:

- A. Key size
- B. 64-bit block size
- C. Round count
- D. S-boxes

**Correct Answer:** **B. 64-bit block size**

**Reason:** The 64-bit block size, which key lengthening cannot fix.

---

### 62. Which mode turns a block cipher into a stream cipher?

- A. ECB
- B. CBC
- C. CFB
- D. None

**Correct Answer:** **C. CFB**

**Reason:** CFB. (OFB and CTR also do; CFB is the only one offered here.)

---

### 63. A PRNG is:

- A. Truly random
- B. Deterministic given a seed
- C. Hardware-based
- D. Always cryptographically secure

**Correct Answer:** **B. Deterministic given a seed**

**Reason:** Deterministic given a seed.

---

### 64. The key property of a CSPRNG is:

- A. Uniform distribution
- B. Unpredictability of output
- C. Speed
- D. Short period

**Correct Answer:** **B. Unpredictability of output**

**Reason:** Unpredictability, not merely good statistics.

---

### 65. A linear congruential generator is unsuitable for cryptography because:

- A. It is slow
- B. Its parameters can be deduced from output
- C. It has no seed
- D. It produces only even numbers

**Correct Answer:** **B. Its parameters can be deduced from output**

**Reason:** A few outputs reveal a, c and m.

---

### 66. A true random number generator draws on:

- A. A mathematical formula
- B. A physical source of entropy
- C. A fixed seed
- D. A hash function

**Correct Answer:** **B. A physical source of entropy**

**Reason:** Physical entropy.

---

### 67. RC4 stands for:

- A. Random Cipher 4
- B. Rivest Cipher 4
- C. Rotational Cipher 4
- D. Round Cipher 4

**Correct Answer:** **B. Rivest Cipher 4**

**Reason:** Rivest Cipher 4.

---

### 68. The RC4 state array S contains:

- A. 128 bytes
- B. 256 bytes
- C. 512 bytes
- D. 1024 bytes

**Correct Answer:** **B. 256 bytes**

**Reason:** 256 bytes.

---

### 69. The RC4 phase that produces keystream bytes is:

- A. KSA
- B. PRGA
- C. MixColumns
- D. Key expansion

**Correct Answer:** **B. PRGA**

**Reason:** PRGA. KSA does the setup.

---

### 70. RC4 is deprecated mainly because of:

- A. Slow performance
- B. Biases in its keystream
- C. Large key size
- D. Patent issues

**Correct Answer:** **B. Biases in its keystream**

**Reason:** Keystream biases.

---

### 71. In a stream cipher, plaintext is combined with the keystream using:

- A. Addition mod 26
- B. XOR
- C. Multiplication
- D. Substitution

**Correct Answer:** **B. XOR**

**Reason:** XOR.

---

### 72. Reusing a stream cipher keystream allows an attacker to obtain:

- A. The key
- B. The XOR of two plaintexts
- C. The IV
- D. Nothing useful

**Correct Answer:** **B. The XOR of two plaintexts**

**Reason:** The XOR of two plaintexts — the key cancels.

---

### 73. Fermat's Little Theorem states, for prime p and a not divisible by p:

- A. aᵖ ≡ 1 (mod p)
- B. a^(p−1) ≡ 1 (mod p)
- C. a^φ(p) ≡ 0 (mod p)
- D. a² ≡ a (mod p)

**Correct Answer:** **B. a^(p−1) ≡ 1 (mod p)**

**Reason:** a^(p−1) ≡ 1 (mod p).

---

### 74. φ(n) for n = pq with p, q distinct primes is:

- A. pq
- B. p+q
- C. (p−1)(q−1)
- D. (p+1)(q+1)

**Correct Answer:** **C. (p−1)(q−1)**

**Reason:** (p−1)(q−1).

---

### 75. φ(17) equals:

- A. 15
- B. 16
- C. 17
- D. 18

**Correct Answer:** **B. 16**

**Reason:** 16, since 17 is prime.

---

### 76. Euler's Theorem generalises Fermat's Theorem to:

- A. Prime moduli only
- B. Any modulus n with gcd(a,n)=1
- C. Even moduli
- D. Polynomial rings

**Correct Answer:** **B. Any modulus n with gcd(a,n)=1**

**Reason:** Any n with gcd(a,n) = 1.

---

### 77. Miller-Rabin is:

- A. A deterministic primality test
- B. A probabilistic primality test
- C. A factoring algorithm
- D. A hash function

**Correct Answer:** **B. A probabilistic primality test**

**Reason:** Probabilistic.

---

### 78. A Miller-Rabin result of "probably prime" means:

- A. Certainly prime
- B. Composite
- C. Prime with high probability
- D. Unknown

**Correct Answer:** **C. Prime with high probability**

**Reason:** Prime with high probability; composites are never wrongly certified after a failed test.

---

### 79. The Chinese Remainder Theorem is used in RSA to:

- A. Generate primes
- B. Speed up decryption
- C. Choose e
- D. Compute hashes

**Correct Answer:** **B. Speed up decryption**

**Reason:** Speed up decryption via mod p and mod q separately.

---

### 80. The discrete logarithm problem is:

- A. Easy in both directions
- B. Easy forward, hard backward
- C. Hard forward, easy backward
- D. Solved in polynomial time

**Correct Answer:** **B. Easy forward, hard backward**

**Reason:** Easy forward, hard backward.

---

### 81. RSA security rests on the difficulty of:

- A. Discrete logarithms
- B. Factoring large integers
- C. Inverting hashes
- D. Solving linear systems

**Correct Answer:** **B. Factoring large integers**

**Reason:** Factoring.

---

### 82. The RSA public key is:

- A. (d, n)
- B. (e, n)
- C. (p, q)
- D. (e, φ(n))

**Correct Answer:** **B. (e, n)**

**Reason:** (e, n).

---

### 83. RSA encryption is:

- A. C = P^d mod n
- B. C = P^e mod n
- C. C = P^e mod φ(n)
- D. C = P × e mod n

**Correct Answer:** **B. C = P^e mod n**

**Reason:** C = P^e mod n. The modulus is n.

---

### 84. φ(n) in RSA is used:

- A. In every encryption
- B. In every decryption
- C. Only during key generation
- D. For padding

**Correct Answer:** **C. Only during key generation**

**Reason:** Only during key generation.

---

### 85. e must satisfy:

- A. e is prime
- B. gcd(e, φ(n)) = 1
- C. e > n
- D. e divides n

**Correct Answer:** **B. gcd(e, φ(n)) = 1**

**Reason:** gcd(e, φ(n)) = 1.

---

### 86. d is defined as:

- A. The inverse of e mod n
- B. The inverse of e mod φ(n)
- C. e squared
- D. p × q

**Correct Answer:** **B. The inverse of e mod φ(n)**

**Reason:** Inverse of e mod φ(n).

---

### 87. If an attacker learns φ(n), they can:

- A. Do nothing useful
- B. Compute d and break the system
- C. Only verify signatures
- D. Only encrypt

**Correct Answer:** **B. Compute d and break the system**

**Reason:** d follows immediately from e and φ(n).

---

### 88. Diffie-Hellman provides:

- A. Encryption
- B. Key exchange
- C. Digital signatures
- D. Hashing

**Correct Answer:** **B. Key exchange**

**Reason:** Key exchange, not encryption.

---

### 89. Diffie-Hellman's main weakness is:

- A. Slow speed
- B. No authentication
- C. Small keys
- D. Weak randomness

**Correct Answer:** **B. No authentication**

**Reason:** No authentication, hence man-in-the-middle.

---

### 90. A 256-bit ECC key is roughly comparable in security to an RSA key of:

- A. 512 bits
- B. 1024 bits
- C. 2048 bits
- D. 3072 bits

**Correct Answer:** **D. 3072 bits**

**Reason:** 3072 bits.

---

### 91. The elliptic curve group identity element is:

- A. The origin
- B. The point at infinity
- C. The generator
- D. Zero

**Correct Answer:** **B. The point at infinity**

**Reason:** The point at infinity.

---

### 92. ElGamal encryption produces a ciphertext consisting of:

- A. One value
- B. Two values
- C. Three values
- D. A hash

**Correct Answer:** **B. Two values**

**Reason:** A pair (C₁, C₂), so ciphertext is twice the plaintext size.

---

### 93. A cryptographic hash function produces:

- A. Variable-length output
- B. Fixed-length output
- C. Encrypted output
- D. A keyed digest

**Correct Answer:** **B. Fixed-length output**

**Reason:** Fixed-length digest from variable-length input.

---

### 94. The property that it is infeasible to find any two inputs hashing to the same value is:

- A. Preimage resistance
- B. Second preimage resistance
- C. Collision resistance
- D. Avalanche

**Correct Answer:** **C. Collision resistance**

**Reason:** Collision resistance (strong collision resistance).

---

### 95. The birthday attack targets:

- A. Preimage resistance
- B. Collision resistance
- C. Key length
- D. Block size

**Correct Answer:** **B. Collision resistance**

**Reason:** Collision resistance — it halves the effective security in bits.

---

### 96. A hash function is sometimes called a one-way function because of:

- A. Collision resistance
- B. Preimage resistance
- C. Its fixed output
- D. Its speed

**Correct Answer:** **B. Preimage resistance**

**Reason:** Preimage resistance: hard to invert the digest.

---

### 97. SHA-3 is based on which construction?

- A. Merkle-Damgård
- B. Feistel
- C. Sponge
- D. SPN

**Correct Answer:** **C. Sponge**

**Reason:** Sponge construction (Keccak). SHA-1 and SHA-2 use Merkle-Damgård.

---

### 98. A MAC differs from a hash in that it:

- A. Produces variable output
- B. Uses a secret key
- C. Is reversible
- D. Is faster

**Correct Answer:** **B. Uses a secret key**

**Reason:** A MAC is keyed; a plain hash is not.

---

### 99. HMAC is constructed by:

- A. Encrypting a hash
- B. Nesting a hash function with a key and two padding constants
- C. XORing two hashes
- D. Using a block cipher directly

**Correct Answer:** **B. Nesting a hash function with a key and two padding constants**

**Reason:** Nested hashing with the key and the ipad/opad constants.

---

### 100. A digital signature provides authentication, integrity and:

- A. Confidentiality
- B. Availability
- C. Non-repudiation
- D. Anonymity

**Correct Answer:** **C. Non-repudiation**

**Reason:** Non-repudiation — the property a MAC cannot provide.

---
