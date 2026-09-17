# DCIT418: SET 5, Fill-in-the-Blanks (Parser Format)

100 fill-in questions from SET5, formatted for parse_security_bank.py.

### 1. The three components of the CIA triad are ______, ______ and ______.

**Correct Answer:** **Confidentiality; Integrity; Availability**

**Reason:** Confidentiality keeps information from unauthorized readers, integrity keeps it from unauthorized modification, and availability keeps it accessible to authorized users when they need it. Every other security service Stallings lists is usually explained as supporting one of these three.

---

### 2. Two security objectives beyond the CIA triad are ______ and ______.

**Correct Answer:** **Authenticity; Non-repudiation**

**Reason:** Stallings extends the classic CIA triad with authenticity (verifying that a message or party genuinely is who it claims to be) and non-repudiation (preventing either party from later denying a message was sent or received), since neither is really a special case of confidentiality, integrity or availability.

---

### 3. The three pillars of the OSI Security Architecture are security ______, security ______ and security ______.

**Correct Answer:** **attack; mechanism; service**

**Reason:** A security attack is any action that compromises security; a security mechanism is a process designed to detect, prevent or recover from an attack; a security service is what a mechanism (or combination of mechanisms) actually delivers, such as confidentiality or authentication.

---

### 4. The two categories of passive attack are ______ and ______.

**Correct Answer:** **Release of message contents; Traffic analysis**

**Reason:** Release of message contents is an eavesdropper simply reading the data; traffic analysis infers information from patterns (who's talking to whom, how often, how much) even when the content itself is encrypted and unreadable.

---

### 5. The four categories of active attack are ______, ______, ______ and ______.

**Correct Answer:** **Masquerade; Replay; Modification of messages; Denial of Service**

**Reason:** All four alter system state or data, which is what makes them "active" rather than "passive." Masquerade means pretending to be someone else, replay resends captured legitimate data, modification alters a message in transit, and denial of service degrades or blocks availability.

---

### 6. The six X.800 security services are ______, ______, ______, ______, ______ and ______.

**Correct Answer:** **Authentication; Access Control; Data Confidentiality; Data Integrity; Non-repudiation; **Availability****

**Reason:** X.800 (ITU-T's security architecture standard) defines Authentication, Access Control, Data Confidentiality, Data Integrity, Non-repudiation and Availability as the six core security services a system can provide, each addressing a distinct part of the CIA-plus-authenticity-and-non-repudiation picture.

---

### 7. In the network security model, the entity that distributes secret information or arbitrates disputes is the ______.

**Correct Answer:** **trusted third party**

**Reason:** The trusted third party sits outside the two communicating principals and is relied on for tasks neither party could safely do alone, distributing shared secret keys, or acting as a neutral arbiter if a dispute arises over what was actually sent or received.

---

### 8. Passive attacks are countered primarily by ______, while active attacks are countered by ______ and ______.

**Correct Answer:** **prevention; detection; recovery**

**Reason:** A passive attack (eavesdropping, traffic analysis) leaves no trace to detect, so the only real defense is preventing it in the first place, mainly through encryption. An active attack does alter something, so it can in principle be detected, and the practical goal shifts to detecting it and recovering from the damage, since preventing every possible active attack outright is unrealistic.

---

### 9. The five components of the symmetric cipher model are ______, ______, ______, ______ and ______.

**Correct Answer:** **Plaintext; Encryption algorithm; Secret key; Ciphertext; Decryption algorithm**

**Reason:** Plaintext is the original readable message; the encryption algorithm transforms it using a secret key into ciphertext; the decryption algorithm reverses that transformation using the same key to recover the plaintext. All five pieces, plaintext, algorithm, key, ciphertext, and the inverse algorithm, are what Stallings' basic symmetric model diagram lays out.

---

### 10. A cipher in which each plaintext letter maps consistently to one ciphertext letter is called ______.

**Correct Answer:** **monoalphabetic**

**Reason:** A monoalphabetic cipher uses a single, fixed substitution alphabet for the entire message, so the same plaintext letter always produces the same ciphertext letter, which is exactly what preserves the underlying language's letter frequencies and makes frequency analysis effective against it.

---

### 11. A cipher in which a plaintext letter may map to several different ciphertext letters is called ______.

**Correct Answer:** **polyalphabetic**

**Reason:** A monoalphabetic cipher uses one fixed substitution for the whole message, so letter frequencies survive intact. A polyalphabetic cipher (the Vigenere cipher is the classic example) cycles through multiple substitution alphabets, so the same plaintext letter can map to different ciphertext letters depending on position, which is exactly what flattens the frequency profile and resists simple frequency analysis.

---

### 12. The Playfair cipher operates on letter pairs known as ______.

**Correct Answer:** **digraphs**

**Reason:** Playfair encrypts two letters (a digraph) at a time using a 5x5 key square, rather than one letter at a time like a simple substitution cipher, which is what makes single-letter frequency analysis far less effective against it.

---

### 13. In the Playfair matrix, the letters ______ and ______ occupy the same cell.

**Correct Answer:** **I; J**

**Reason:** The Playfair square has only 25 cells for 26 letters, so I and J are conventionally merged into a single cell to make the alphabet fit a 5x5 grid.

---

### 14. The cipher offering perfect secrecy is the ______, also known as the ______ cipher.

**Correct Answer:** **one-time pad; Vernam**

**Reason:** The One-Time Pad XORs plaintext with a truly random key at least as long as the message, used only once. Because the key is uniformly random and never reused, the ciphertext gives an attacker zero statistical information about the plaintext, which is the definition of perfect (information-theoretic) secrecy. It's impractical precisely because distributing a key as long as the message is its own hard problem.

---

### 15. For that cipher to be secure the key must be ______, ______ as the message, and used ______.

**Correct Answer:** **truly random; the same length; only once**

**Reason:** This is the One-Time Pad's condition for perfect secrecy: the key must be truly random, at least as long as the message, and used only once. Violating any one of these three conditions (a short key, a predictable key, or key reuse) breaks the perfect-secrecy guarantee.

---

### 16. Rearranging letter positions without changing the letters themselves is called a ______ technique.

**Correct Answer:** **transposition**

**Reason:** A transposition technique permutes the order of the plaintext characters without substituting any of them for different characters, which is the opposite approach from a substitution cipher and is why transposition alone still leaks the original letter frequencies.

---

### 17. Concealing the very existence of a message is called ______.

**Correct Answer:** **steganography**

**Reason:** Cryptography scrambles a message so its content is unreadable but its presence is obvious; steganography hides the message inside an innocuous carrier (an image, audio file, or similar) so an observer doesn't even know communication is happening. The two are complementary, not competing, techniques.

---

### 18. The technique used to break monoalphabetic substitution ciphers is ______.

**Correct Answer:** **frequency analysis**

**Reason:** Frequency analysis compares how often each ciphertext symbol appears against known letter-frequency statistics for the language (e.g. 'E' is the most common English letter), since a monoalphabetic cipher preserves those frequencies one-to-one under a fixed substitution.

---

### 19. The two Feistel round equations are Lᵢ = ______ and Rᵢ = ______.

**Correct Answer:** **Lᵢ = Rᵢ₋₁ ; Rᵢ = Lᵢ₋₁ ⊕ F(Rᵢ₋₁, Kᵢ)**

**Reason:** Li = Ri-1 (the new left half is just the old right half), and Ri = Li-1 XOR F(Ri-1, Ki) (the new right half is the old left half XORed with the round function applied to the old right half and that round's subkey). This structure is what lets the exact same algorithm run both encryption and decryption.

---

### 20. Feistel decryption uses the same algorithm with the subkeys applied in ______ order.

**Correct Answer:** **reverse**

**Reason:** Because XOR is its own inverse, running the identical Feistel round structure but feeding the subkeys in reverse order (Kn down to K1 instead of K1 up to Kn) exactly undoes each round, so no separate decryption algorithm or circuitry is needed.

---

### 21. DES has a block size of ______ bits, a stored key of ______ bits and an effective key of ______ bits.

**Correct Answer:** **64; 64; 56**

**Reason:** DES operates on 64-bit blocks. The key is stored as 64 bits, but 8 of those bits are parity bits (one per byte) that carry no security-relevant information, leaving an effective key length of 56 bits, which is also why DES's 2^56 keyspace became brute-forceable and drove the move to Triple DES and then AES.

---

### 22. The unused key bits in DES serve as ______ bits.

**Correct Answer:** **parity**

**Reason:** DES stores a 64-bit key, but only 56 of those bits are actually used in encryption; the remaining 8 bits (one per byte) are parity bits used for basic error checking on the key, not for security.

---

### 23. DES performs ______ rounds.

**Correct Answer:** **16**

**Reason:** DES runs 16 rounds of its Feistel structure, a number chosen as a balance between enough rounds to resist known cryptanalytic attacks of the time and reasonable encryption/decryption speed.

---

### 24. The DES round function expands the right half from ______ bits to ______ bits.

**Correct Answer:** **32; 48**

**Reason:** The 32-bit right half is expanded to 48 bits by the E-table so it can be XORed with the 48-bit round subkey before being compressed back down to 32 bits by the S-boxes, that expansion is also what lets each output bit of the S-boxes depend on more than one input bit, aiding diffusion.

---

### 25. DES uses ______ S-boxes, each taking ______ bits and producing ______ bits.

**Correct Answer:** **8; 6; 4**

**Reason:** The 48-bit expanded half-block from the E-table is split into eight 6-bit chunks, one per S-box, and each S-box compresses its 6 input bits down to a 4-bit output, recombining into a 32-bit result. That 6-to-4 compression, chosen via a fixed lookup table rather than a formula, is what supplies DES's nonlinearity.

---

### 26. The only nonlinear component of the DES round function is the ______.

**Correct Answer:** **S-box (substitution)**

**Reason:** The expansion permutation, the P-box permutation, and the XOR with the round key are all linear operations, so if DES only used those, the whole cipher would collapse into a linear function solvable directly. The S-boxes are the sole non-linear step, and that nonlinearity is exactly what makes differential and linear cryptanalysis hard rather than trivial.

---

### 27. Shannon's two principles of cipher design are ______ and ______.

**Correct Answer:** **confusion; diffusion**

**Reason:** Confusion makes the relationship between the key and the ciphertext as complex as possible; diffusion spreads the statistical influence of each plaintext (and key) bit across many ciphertext bits. Together they're the foundational design goals behind both DES's Feistel structure and AES's substitution-permutation network.

---

### 28. Obscuring the relationship between the key and the ciphertext is ______; spreading plaintext statistics across the ciphertext is ______.

**Correct Answer:** **confusion; diffusion**

**Reason:** Confusion hides how the key relates to the ciphertext (achieved through substitution, like an S-box); diffusion spreads plaintext structure across many ciphertext bits (achieved through permutation and mixing), Shannon's two complementary defenses against statistical cryptanalysis.

---

### 29. The property whereby a one-bit input change flips roughly half the output bits is the ______ effect.

**Correct Answer:** **avalanche**

**Reason:** The avalanche effect means a tiny change to the plaintext or key (even a single bit) should cascade into a large, unpredictable change in the ciphertext, roughly half the output bits flipping is the benchmark a well-designed cipher is expected to hit, since anything less would leak exploitable structure.

---

### 30. The algorithm used to compute the greatest common divisor of two integers is the ______ algorithm.

**Correct Answer:** **Euclidean**

**Reason:** The Euclidean algorithm repeatedly replaces the larger of two numbers with the remainder from dividing it by the smaller, until the remainder reaches zero; the last nonzero remainder is the gcd.

---

### 31. The variant used to compute multiplicative inverses is the ______ algorithm.

**Correct Answer:** **extended Euclidean**

**Reason:** The Extended Euclidean algorithm runs the same recursion as the ordinary Euclidean algorithm but additionally tracks coefficients x and y satisfying ax + by = gcd(a,b); when gcd(a,n) = 1, that x is exactly a's multiplicative inverse mod n, which is how RSA derives d from e.

---

### 32. A multiplicative inverse of a modulo n exists only when ______ = 1.

**Correct Answer:** **gcd(a, n)**

**Reason:** gcd(a, n) = 1 is the exact condition for a to have a multiplicative inverse mod n: if a and n share any common factor greater than 1, no integer multiple of a can ever land on 1 modulo n.

---

### 33. A set with one operation satisfying closure, associativity, identity and inverse is a ______.

**Correct Answer:** **group**

**Reason:** This is the definition of a group: closure keeps results inside the set, associativity lets operations be grouped in any order, an identity element leaves other elements unchanged, and every element has an inverse that combines with it to produce the identity.

---

### 34. A group whose operation is also commutative is called an ______ group.

**Correct Answer:** **abelian**

**Reason:** An abelian group adds commutativity (a * b = b * a for every pair of elements) on top of the ordinary group axioms; addition of integers is a familiar abelian group, while general matrix multiplication is a familiar example of a non-abelian one.

---

### 35. A structure with two operations where multiplication need not have inverses is a ______.

**Correct Answer:** **ring**

**Reason:** A ring has two operations (typically called addition and multiplication), forms an abelian group under addition, and has associative, distributive multiplication, but unlike a field, multiplication in a ring is not required to have inverses for every nonzero element.

---

### 36. A structure in which every nonzero element has a multiplicative inverse is a ______.

**Correct Answer:** **field**

**Reason:** A ring only guarantees an additive group plus associative, distributive multiplication, nothing about multiplicative inverses. A field adds exactly that guarantee, every nonzero element is invertible, which is what makes division well-defined and is why GF(p) and GF(2^n) (fields, not just rings) are what cryptographic arithmetic is built on.

---

### 37. GF(p) is a field only when p is ______.

**Correct Answer:** **prime**

**Reason:** GF(p) is a field exactly when p is prime, since primality guarantees every nonzero residue is coprime to p and therefore has a multiplicative inverse; for a composite modulus, some nonzero elements share a factor with the modulus and lose their inverse, breaking the field structure.

---

### 38. In GF(2ⁿ), polynomial addition is equivalent to the bitwise ______ operation.

**Correct Answer:** **XOR**

**Reason:** Addition of polynomials with coefficients in GF(2) reduces coefficient-by-coefficient addition modulo 2, which is exactly the bitwise XOR operation, that's why AES's GF(2^8) arithmetic uses plain XOR for addition rather than any carrying arithmetic.

---

### 39. The modulus polynomial in GF(2ⁿ) must be ______.

**Correct Answer:** **irreducible**

**Reason:** An irreducible polynomial cannot be factored into lower-degree polynomials over GF(2), which is the polynomial analogue of a prime number. Just as GF(p) needs p prime for every nonzero residue to have an inverse, GF(2^n) needs the modulus polynomial irreducible, otherwise some nonzero elements would share a factor with the modulus and lose their inverse, breaking the field structure.

---

### 40. The irreducible polynomial used by AES is ______.

**Correct Answer:** **x⁸ + x⁴ + x³ + x + 1**

**Reason:** AES defines its GF(2^8) byte arithmetic modulo the irreducible polynomial x^8 + x^4 + x^3 + x + 1, chosen by the Rijndael designers so that every nonzero byte value has a well-defined multiplicative inverse in that field.

---

### 41. AES has a fixed block size of ______ bits.

**Correct Answer:** **128**

**Reason:** AES always operates on a 128-bit block regardless of which key size (128, 192 or 256 bits) is chosen; only the key length and the corresponding number of rounds change, the block size never does.

---

### 42. AES supports key sizes of ______, ______ and ______ bits.

**Correct Answer:** **128; 192; 256**

**Reason:** AES-128, AES-192 and AES-256 are the three standardized variants, differing only in key length and round count, all three still encrypt the same fixed 128-bit block.

---

### 43. The corresponding round counts are ______, ______ and ______.

**Correct Answer:** **10; 12; 14**

**Reason:** Longer AES keys get more rounds to preserve the security margin as the key space grows: 10 rounds for a 128-bit key, 12 for 192-bit, and 14 for 256-bit.

---

### 44. AES is structurally a ______ network, not a Feistel cipher.

**Correct Answer:** **substitution-permutation**

**Reason:** A Feistel cipher only transforms half the block each round while the other half passes through unchanged. AES instead transforms the entire 128-bit state every round through substitution (SubBytes) and permutation/mixing (ShiftRows, MixColumns) layers, which is the defining shape of a substitution-permutation network.

---

### 45. AES arranges the block as a 4×4 matrix of bytes called the ______.

**Correct Answer:** **State**

**Reason:** The 16 bytes of a 128-bit AES block are loaded column by column into a 4x4 byte matrix called the State, and every round transformation (SubBytes, ShiftRows, MixColumns, AddRoundKey) operates directly on that State matrix.

---

### 46. The four AES round transformations in order are ______, ______, ______ and ______.

**Correct Answer:** **SubBytes; **ShiftRows**; MixColumns; AddRoundKey**

**Reason:** SubBytes supplies nonlinear confusion via the S-box, ShiftRows shifts each row of the state to diffuse bytes across columns, MixColumns mixes the four bytes within each column via matrix multiplication in GF(2^8) for diffusion within a column, and AddRoundKey XORs in the round's key material, the only step that actually depends on the secret key.

---

### 47. The transformation omitted in the final round is ______.

**Correct Answer:** **MixColumns**

**Reason:** MixColumns is skipped in AES's last round, since its diffusion only helps if further rounds follow to compound it, and including it there would force decryption to add an extra InvMixColumns step for no additional security benefit.

---

### 48. The only transformation using the secret key is ______.

**Correct Answer:** **AddRoundKey**

**Reason:** AddRoundKey is the sole AES round step that actually incorporates the key, a straightforward XOR of the State with that round's derived round key; SubBytes, ShiftRows and MixColumns are all fixed, key-independent operations.

---

### 49. The AES S-box is built from multiplicative inverses in ______ combined with an ______ transformation.

**Correct Answer:** **GF(2⁸); affine**

**Reason:** The AES S-box takes each byte's multiplicative inverse in GF(2^8) (mapping 0 to itself as a special case) and then applies a fixed affine transformation over GF(2), that combination is what gives SubBytes both strong nonlinearity and resistance to simple algebraic attacks.

---

### 50. AES-128 requires ______ round keys in total.

**Correct Answer:** **11**

**Reason:** AES-128 runs 10 rounds, but there's also an initial AddRoundKey applied before round 1 even starts, so the key schedule must produce Nr + 1 = 11 separate 128-bit round keys (44 words of 32 bits each) to cover the initial whitening step plus all 10 rounds.

---

### 51. The five block cipher modes are ______, ______, ______, ______ and ______.

**Correct Answer:** **ECB; CBC; CFB; OFB; CTR**

**Reason:** Electronic Codebook encrypts each block independently (and leaks plaintext structure); Cipher Block Chaining XORs each plaintext block with the previous ciphertext before encrypting; Cipher Feedback and Output Feedback turn the block cipher into a self-synchronizing or synchronous stream cipher respectively; Counter mode encrypts successive counter values to form a keystream, enabling parallel encryption and decryption.

---

### 52. The mode that encrypts each block independently is ______.

**Correct Answer:** **ECB**

**Reason:** ECB (Electronic Codebook) encrypts each plaintext block separately with no dependency on any other block, an IV, or a counter, which is exactly why identical plaintext blocks always produce identical ciphertext blocks and leak structural patterns.

---

### 53. The mode in which each plaintext block is XORed with the previous ciphertext block is ______.

**Correct Answer:** **CBC**

**Reason:** CBC (Cipher Block Chaining) XORs each plaintext block with the previous block's ciphertext before encrypting, chaining every block to the one before it (with an IV standing in for block zero), which is what hides repeated plaintext patterns that ECB would expose.

---

### 54. The random value used to seed CBC, CFB and OFB is the ______.

**Correct Answer:** **Initialization Vector (IV)**

**Reason:** The Initialization Vector (IV) is XORed into (or otherwise mixed with) the very first block of these modes so that encrypting the same plaintext twice under the same key still produces different ciphertext, as long as the IV differs each time.

---

### 55. In OFB, the keystream is generated by repeatedly encrypting the previous ______.

**Correct Answer:** **keystream block**

**Reason:** OFB feeds the block cipher's own output back in as the next input, generating a keystream that is completely independent of the ciphertext or plaintext. That's what gives OFB its "no error propagation" property, and also why the keystream can be precomputed before the plaintext is even available.

---

### 56. In CFB, the keystream is generated by encrypting the previous ______.

**Correct Answer:** **ciphertext block**

**Reason:** CFB feeds the previous ciphertext block back through the block cipher to produce the next keystream segment. Because the feedback is the ciphertext rather than the raw output, CFB is self-synchronizing, an error in one ciphertext block corrupts a bounded run of subsequent plaintext but then resynchronizes, unlike OFB's fully independent keystream.

---

### 57. In CTR, the keystream is generated by encrypting an incrementing ______.

**Correct Answer:** **counter**

**Reason:** CTR mode encrypts a counter value that increments by one for each block (rather than chaining off the previous ciphertext or plaintext) to produce the keystream, which is XORed with the plaintext; that independence from prior blocks is what makes CTR fully parallelizable.

---

### 58. The two modes with no error propagation are ______ and ______.

**Correct Answer:** **OFB; CTR**

**Reason:** In both modes, the keystream is generated independently of the ciphertext (from repeated encryption in OFB, from encrypting a counter in CTR), and recovery is a simple XOR. A flipped ciphertext bit therefore flips exactly the corresponding plaintext bit and nothing else, no full-block corruption and no bleed into neighboring blocks, unlike ECB, CBC or CFB, where decryption runs the corrupted ciphertext through the block cipher itself and scrambles the whole affected block.

---

### 59. The only mode permitting parallel encryption and random-access decryption is ______.

**Correct Answer:** **CTR**

**Reason:** CTR mode is the one where every block's keystream depends only on the key and that block's own counter value, not on any neighboring block, so any block can be encrypted or decrypted independently and in any order, including in parallel across multiple cores.

---

### 60. The requirement placed on a CBC IV is that it be ______; the requirement placed on a CTR counter is that it be ______.

**Correct Answer:** **unpredictable; unique**

**Reason:** CBC's IV must be unpredictable (essentially random), since a predictable IV lets an attacker test guesses about the first plaintext block. CTR's counter only needs to be unique, never repeated with the same key, it doesn't need to be secret or random at all, which is a strictly weaker and easier requirement to satisfy correctly.

---

### 61. Applying DES three times in succession yields ______.

**Correct Answer:** **Triple DES (3DES)**

**Reason:** Triple DES (3DES) runs the DES algorithm three times in sequence (typically encrypt-decrypt-encrypt with two or three distinct keys) to extend the effective key strength well beyond single DES's brute-forceable 56 bits, without designing an entirely new cipher.

---

### 62. That construction remains limited by its ______ size.

**Correct Answer:** **block**

**Reason:** 3DES inherits DES's original 64-bit block size, and a block that small becomes vulnerable to birthday-bound collision attacks once enough data has been encrypted under one key, which is part of why AES (with its 128-bit block) eventually replaced it.

---

### 63. A generator producing random-looking output deterministically from a seed is a ______.

**Correct Answer:** **PRNG (pseudorandom number generator)**

**Reason:** A PRNG (pseudorandom number generator) is a deterministic algorithm: given the same seed, it always produces the same output sequence, and it's judged mainly by whether that output passes statistical randomness tests, not by whether it resists a determined attacker.

---

### 64. A generator whose output is computationally unpredictable is a ______.

**Correct Answer:** **CSPRNG (cryptographically secure PRNG)**

**Reason:** A CSPRNG (cryptographically secure PRNG) adds the stronger requirement that predicting past or future output is computationally infeasible even given a substantial chunk of the sequence, which an ordinary PRNG (like a linear congruential generator) does not guarantee.

---

### 65. A generator drawing on physical entropy is a ______.

**Correct Answer:** **TRNG (true random number generator)**

**Reason:** A TRNG (true random number generator) samples genuine physical entropy, thermal noise, timing jitter, radioactive decay, rather than running a deterministic algorithm, so its output isn't reproducible even in principle given the same starting conditions.

---

### 66. The formula Xₙ₊₁ = (aXₙ + c) mod m defines a ______ generator.

**Correct Answer:** **linear congruential**

**Reason:** This recurrence defines a linear congruential generator (LCG); it's fast and simple but cryptographically broken, since observing just a handful of consecutive outputs lets an attacker solve for a, c and m and then predict the entire sequence.

---

### 67. RC4 stands for ______.

**Correct Answer:** **Rivest Cipher 4**

**Reason:** RC4 stands for Rivest Cipher 4, designed by Ron Rivest in 1987; it was once widely used in protocols like WEP and early SSL/TLS before statistical biases in its keystream led to its deprecation.

---

### 68. RC4's two phases are ______ and ______.

**Correct Answer:** **Key Scheduling Algorithm (KSA); Pseudo-Random Generation Algorithm (PRGA)**

**Reason:** The KSA initializes a 256-byte state array and shuffles it into a key-dependent permutation using the secret key. The PRGA then continuously swaps entries in that state using two index pointers and emits one keystream byte per step, which is XORed with the plaintext. RC4's known biases live mostly in the KSA's handling of the earliest PRGA output bytes.

---

### 69. RC4's state array contains ______ bytes.

**Correct Answer:** **256**

**Reason:** RC4's internal state is a 256-byte array (indexed 0 to 255) that the Key Scheduling Algorithm shuffles into a key-dependent permutation before the PRGA starts emitting keystream bytes from it.

---

### 70. In a stream cipher, plaintext and keystream are combined using ______.

**Correct Answer:** **XOR**

**Reason:** A stream cipher XORs the plaintext with a pseudorandom keystream, one bit or byte at a time, to produce ciphertext; decryption XORs the same keystream against the ciphertext to recover the plaintext, since XOR is its own inverse.

---

### 71. Reusing a keystream allows an attacker to recover the ______ of two plaintexts.

**Correct Answer:** **XOR**

**Reason:** If two messages are encrypted with the same keystream K, XORing the two resulting ciphertexts together cancels K out entirely, leaving the XOR of the two plaintexts, which, combined with language statistics or crib-dragging, is often enough to recover both messages without ever learning K.

---

### 72. Fermat's Little Theorem states that for prime p and a not divisible by p, ______.

**Correct Answer:** **a^(p−1) ≡ 1 (mod p)**

**Reason:** This holds because the nonzero residues mod a prime p form a group of order p-1 under multiplication, and by Lagrange's theorem every element's order divides the group's order, so raising any such element to the p-1 power always cycles back to the identity, 1.

---

### 73. Euler's totient function φ(n) counts integers below n that are ______ to n.

**Correct Answer:** **coprime (relatively prime)**

**Reason:** phi(n) counts how many integers in the range 1 to n-1 are coprime to n (share no common factor with it other than 1); those are exactly the residues that have a multiplicative inverse modulo n.

---

### 74. For distinct primes p and q, φ(pq) = ______.

**Correct Answer:** **(p−1)(q−1)**

**Reason:** Euler's totient is multiplicative over coprime factors, and for two distinct primes it reduces to phi(pq) = (p-1)(q-1), which is precisely the identity RSA key generation uses to compute phi(n) from n = pq.

---

### 75. For a prime p, φ(p) = ______.

**Correct Answer:** **p − 1**

**Reason:** Every integer from 1 to p-1 is automatically coprime to a prime p, so phi(p) simply equals p-1, this is the special case that makes Fermat's Little Theorem a special case of Euler's Theorem.

---

### 76. Euler's Theorem states that if gcd(a,n) = 1 then ______.

**Correct Answer:** **a^φ(n) ≡ 1 (mod n)**

**Reason:** Euler's Theorem generalizes Fermat's Little Theorem from a prime modulus to any modulus n, replacing the group order p-1 with φ(n), the count of integers coprime to n. Fermat's is just the special case where n is prime, since φ(p) = p-1. This is the identity RSA's correctness proof leans on, since n = pq is composite.

---

### 77. The probabilistic primality test used in RSA key generation is ______.

**Correct Answer:** **Miller-Rabin**

**Reason:** Miller-Rabin repeatedly tests a candidate against random witnesses; a composite number fails at least one witness's test with probability at least 3/4, so running enough independent rounds drives the chance of a false "probably prime" verdict down to negligible levels, fast enough to be practical for generating the very large primes p and q that RSA needs.

---

### 78. The theorem used to speed up RSA decryption is the ______.

**Correct Answer:** **Chinese Remainder Theorem**

**Reason:** The Chinese Remainder Theorem lets RSA decryption be computed separately modulo p and modulo q (both much smaller than n) and then recombined, which is roughly four times faster than a single full-size modular exponentiation mod n.

---

### 79. Given α, q and α^x mod q, recovering x is the ______ problem.

**Correct Answer:** **discrete logarithm**

**Reason:** Computing α^x mod q from x is fast (repeated squaring), but the reverse direction, recovering x given only α, q and the result, has no known efficient classical algorithm for well-chosen groups. That asymmetry, easy forward, hard backward, is exactly what Diffie-Hellman and ElGamal build their security on.

---

### 80. RSA security rests on the difficulty of ______.

**Correct Answer:** **factoring large integers (integer factorisation)**

**Reason:** RSA's security relies on integer factorization: multiplying two large primes p and q to get n is easy, but recovering p and q from n alone is assumed computationally infeasible for a large enough modulus using current classical algorithms.

---

### 81. The RSA public key is the pair ______ and the private key is the pair ______.

**Correct Answer:** **(e, n); (d, n)**

**Reason:** Both keys share the same modulus n; the public key is (e, n), where e is the public encryption/verification exponent, and the private key is (d, n), where d is e's modular inverse used for decryption/signing.

---

### 82. RSA encryption is C = ______ and decryption is P = ______.

**Correct Answer:** **C = P^e mod **n** ; P = C^d mod **n****

**Reason:** Encryption computes C = P^e mod n; decryption computes P = C^d mod n. Because d is e's multiplicative inverse modulo phi(n), these two operations undo each other by Euler's Theorem.

---

### 83. The public exponent e must satisfy ______.

**Correct Answer:** **gcd(e, φ(n)) = 1, with 1 < e < φ(n)**

**Reason:** e must satisfy 1 < e < phi(n) and gcd(e, phi(n)) = 1 (e coprime to phi(n)), that coprimality is exactly what guarantees e has a multiplicative inverse d modulo phi(n) for the private key to exist.

---

### 84. The private exponent d is the ______ of e modulo ______.

**Correct Answer:** **multiplicative inverse; φ(n)**

**Reason:** d is the multiplicative inverse of e modulo phi(n), computed via the Extended Euclidean algorithm so that e*d ≡ 1 (mod phi(n)); that inverse relationship is exactly what makes RSA decryption undo encryption.

---

### 85. φ(n) is used only during ______.

**Correct Answer:** **key generation**

**Reason:** phi(n) is needed only when generating the RSA key pair, to derive d from e, it never appears in the encryption or decryption formulas themselves, which is also why phi(n) (and therefore p and q) must be kept secret even though n and e are public.

---

### 86. Diffie-Hellman achieves ______ rather than encryption.

**Correct Answer:** **key exchange (key agreement)**

**Reason:** Diffie-Hellman never encrypts or transmits a message directly; it lets two parties who exchange only public values each independently compute the same shared secret, which is then typically used to derive a symmetric key for a separate encryption step. It's a key-agreement protocol, not a cipher in its own right.

---

### 87. Its two public parameters are a large prime ______ and a ______ of that prime.

**Correct Answer:** **q; primitive root α**

**Reason:** Diffie-Hellman's public parameters are a large prime q and a primitive root (generator) alpha of that prime's multiplicative group, chosen so alpha's powers modulo q cycle through every nonzero residue before repeating.

---

### 88. Its security rests on the ______ problem.

**Correct Answer:** **discrete logarithm**

**Reason:** Diffie-Hellman's security rests on the discrete logarithm problem: computing alpha^x mod q is fast, but recovering x given only alpha, q and alpha^x mod q is assumed computationally infeasible for well-chosen parameters.

---

### 89. Its principal weakness is the absence of ______, which permits the ______ attack.

**Correct Answer:** **authentication; man-in-the-middle**

**Reason:** Plain Diffie-Hellman never authenticates who sent which public value, which is what permits a man-in-the-middle attack: an attacker can intercept the exchange, run a separate DH exchange with each party, and relay/re-encrypt all traffic between them without either party noticing.

---

### 90. The general equation of an elliptic curve is ______.

**Correct Answer:** **y² = x³ + ax + b**

**Reason:** The general (short Weierstrass) form used in cryptography is y^2 = x^3 + ax + b, with the constants a and b (subject to a non-singularity condition) defining the specific curve and its group structure.

---

### 91. The identity element of the elliptic curve group is the ______.

**Correct Answer:** **point at infinity**

**Reason:** Elliptic-curve point addition is defined geometrically (draw a line through two points, find the third intersection, reflect it), and to make every point have an inverse and the operation form a proper group, a special "point at infinity" is added as the identity element, the result of adding a point to its own vertical reflection.

---

### 92. The hard problem underlying ECC is the ______.

**Correct Answer:** **Elliptic Curve Discrete Logarithm Problem (ECDLP)**

**Reason:** Given a base point P and Q = kP (P added to itself k times), recovering k is believed computationally infeasible for well-chosen curves, and unlike integer factorization there's no known sub-exponential attack against it, which is why ECC reaches RSA-equivalent security with much smaller key sizes.

---

### 93. A 256-bit ECC key is roughly equivalent in security to an RSA key of ______ bits.

**Correct Answer:** **3072**

**Reason:** A 256-bit elliptic-curve key is considered roughly equivalent in strength to a 3072-bit RSA key, since ECC's underlying discrete logarithm problem has no known sub-exponential attack the way integer factorization does, letting it reach the same security level with a much smaller key.

---

### 94. A hash function takes ______-length input and produces ______-length output.

**Correct Answer:** **variable; fixed**

**Reason:** A cryptographic hash function accepts an input message of any (variable) length and always produces a fixed-length digest, regardless of how long or short the original message was.

---

### 95. The three security properties required of a cryptographic hash are ______, ______ and ______.

**Correct Answer:** **preimage resistance; second preimage resistance; collision resistance**

**Reason:** Preimage resistance (can't work backward from a hash to find any input producing it), second preimage resistance (given one input, can't find a different input with the same hash), and collision resistance (can't find any two inputs at all that collide) are the three properties a secure hash function must satisfy.

---

### 96. The attack that exploits collision probability rather than brute force is the ______ attack.

**Correct Answer:** **birthday**

**Reason:** The birthday attack exploits the birthday paradox: finding any two inputs that collide only takes roughly the square root of the number of possible hash outputs, far fewer attempts than brute-forcing a specific preimage, which is why hash digests need to be twice as long as the target security level to resist it.

---

### 97. SHA-3 is based on the ______ construction, whereas SHA-1 and SHA-2 use the ______ construction.

**Correct Answer:** **sponge; Merkle-Damgård**

**Reason:** SHA-3 uses the sponge construction, absorbing input into a large internal state and then squeezing out output, with security tunable via the rate/capacity split. SHA-1 and SHA-2 instead chain a compression function block by block (the Merkle-Damgard construction), which is also what makes naive use of them susceptible to length-extension attacks.

---

### 98. A keyed hash providing message authentication is a ______; the standard nested construction is ______.

**Correct Answer:** **MAC (message authentication code); HMAC**

**Reason:** A MAC (message authentication code) combines a secret key with a hash to prove both integrity and authenticity; HMAC is the standard, well-analyzed way to build one, nesting the key into both an inner and outer hash pass specifically to resist length-extension attacks that a naive secret-prefix construction would be vulnerable to.

---

### 99. The two padding constants used in that construction are ______ and ______.

**Correct Answer:** **ipad; opad**

**Reason:** HMAC XORs the key with two fixed byte constants before its inner and outer hash passes: ipad (0x36 repeated) for the inner pass and opad (0x5c repeated) for the outer pass, ensuring the two hash computations use meaningfully different, derived keys rather than the same raw key twice.

---

### 100. The security service a digital signature provides that a MAC cannot is ______.

**Correct Answer:** **non-repudiation**

**Reason:** Non-repudiation: since only the signer holds the private signing key, a valid signature proves the signer specifically produced it, and they can't credibly deny having signed it. A MAC's key is shared between both parties, so either one could have produced a given tag, meaning a MAC can prove authenticity to the other party but can never prove it to a third party the way a signature can.

---
