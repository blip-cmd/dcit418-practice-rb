# DCIT418: Christian's Exam Review (Parser Format)

100 high-quality exam review questions from Christian's comprehensive study bank,
formatted for parse_security_bank.py. These questions emphasize synthesis and reasoning.

### 1. GF(2^8) arithmetic is directly used inside which widely deployed algorithm?

- A. The Euclidean Algorithm, when computing a greatest common divisor
- B. RSA, when selecting the two large prime factors of its modulus
- C. AES, in its byte substitution and column mixing steps
- D. The plain Caesar cipher, in choosing its shift amount

**Correct Answer:** **C. AES, in its byte substitution and column mixing steps**

**Intuition:** AES operates on 8-bit bytes defined as elements in GF(2^8). SubBytes uses multiplicative inverses in GF(2^8), and MixColumns performs polynomial matrix multiplication over GF(2^8).

---

### 2. The theorem guaranteeing that every integer greater than 1 factors into primes in exactly one way is called

**Correct Answer:** **fundamental-theorem**

**Intuition:** The Fundamental Theorem of Arithmetic states that every integer greater than 1 has a unique prime factorization up to the order of factors.

---

### 3. The set of points on an elliptic curve, together with a defined addition rule and a point at infinity, forms an

**Correct Answer:** **abelian**

**Intuition:** Elliptic curve point addition satisfies closure, associativity, identity, inverses, and commutativity, forming an abelian group.

---

### 4. The square-and-multiply technique for RSA is valuable because it computes a large modular

- A. Addition alone, avoiding multiplication entirely
- B. Repeated squaring, needing only a handful of multiplications instead of performing the full exponent's worth
- C. A random guess-and-check process repeated until the result matches
- D. A single lookup table indexed by the exponent value

**Correct Answer:** **B. Repeated squaring, needing only a handful of multiplications instead of performing the full**

**Intuition:** Square-and-multiply computes modular exponentiation in O(log e) operations using repeated squarings and conditional multiplications.

---

### 5. A base g whose successive powers modulo a prime p cycle through every nonzero remainder before

**Correct Answer:** **primitive-root**

**Intuition:** A primitive root modulo p generates all p - 1 non-zero elements in Z_p^*.

---

### 6. AddRoundKey is the only AES transformation that:

- A. Requires computation in GF(2^8) using a fixed multiplication matrix
- B. Provides nonlinearity through a substitution table
- C. Reorders bytes without changing any of their values
- D. Directly incorporates the secret key material into the State, via XOR with the round key

**Correct Answer:** **D. Directly incorporates the secret key material into the State, via XOR with the round key**

**Intuition:** SubBytes, ShiftRows, and MixColumns do not use key material; AddRoundKey is the only round operation that XORs the round key into the State.

---

### 7. For a positive integer n, arithmetic performed modulo n confines every result to the range:

- A. {0, 1, ..., 2n-1}, doubling the usual modular range for security
- B. {1, 2, ..., n}, excluding zero entirely from every calculation
- C. {-n, ..., 0, ..., n}, allowing both positive and negative remainders freely
- D. {0, 1, ..., n-1}, wrapping around whenever a value would leave that range

**Correct Answer:** **D. {0, 1, ..., n-1}, wrapping around whenever a value would leave that range**

**Intuition:** Arithmetic modulo n maps all results into the standard complete set of residues {0, 1, ..., n-1}.

---

### 8. The attack that defeats Double DES by working forward from the plaintext and backward from the

**Correct Answer:** **meet-in-the-middle**

**Intuition:** Meet-in-the-middle matches forward encryption E_K1(P) with backward decryption D_K2(C) in an intermediate table, reducing effective security to ~2^57.

---

### 9. The problem of finding the exponent x that solves g^x ≡ b (mod p), believed to be computationally

**Correct Answer:** **discrete-logarithm**

**Intuition:** The Discrete Logarithm Problem (DLP) is the one-way hard mathematical problem underlying classical Diffie- Hellman and ElGamal.

---

### 10. The final round of AES encryption differs from the earlier rounds in that it:

- A. Omits the AddRoundKey transformation entirely
- B. Repeats SubBytes twice in succession
- C. Omits the MixColumns transformation
- D. Uses a different, smaller S-box than earlier rounds

**Correct Answer:** **C. Omits the MixColumns transformation**

**Intuition:** The final round consists only of SubBytes, ShiftRows, and AddRoundKey, omitting MixColumns to make decryption structurally symmetrical

---

### 11. In RSA key generation, once primes p and q have been chosen, the public modulus is computed as n =

- A. phi(n) = p*q - 1
- B. phi(n) = (p-1)(q-1)
- C. phi(n) = p + q - 1
- D. phi(n) = (p-1) + (q-1)

**Correct Answer:** **B. phi(n) = (p-1)(q-1)**

**Intuition:** Euler's totient function for the product of two distinct primes p and q is phi(n) = phi(p)*phi(q) = (p-1)(q-1).

---

### 12. The fast, widely used probabilistic primality test that repeatedly tests random witnesses against a

**Correct Answer:** **Miller-Rabin**

**Intuition:** The Miller-Rabin test checks whether candidate witnesses satisfy modular square root properties of primes.

---

### 13. Elliptic curve cryptography is attractive compared to RSA mainly because, for a comparable level of

- A. Requires substantially smaller key sizes, reducing processing overhead
- B. Has a longer and more thoroughly tested track record than RSA
- C. Does not require the two communicating parties to agree on any shared curve parameters
- D. Eliminates the need for any private key on either side of the exchange

**Correct Answer:** **A. Requires substantially smaller key sizes, reducing processing overhead**

**Intuition:** ECC provides equivalent cryptographic security with much smaller keys (e.g., 256-bit ECC matches 3072-bit RSA), saving compute and bandwidth.

---

### 14. In a stream cipher, the pseudorandom sequence of bits combined with the plaintext via XOR to produce

**Correct Answer:** **keystream**

**Intuition:** Stream ciphers generate a pseudorandom keystream that is XORed bitwise with the plaintext.

---

### 15. In GF(2^m), addition of two field elements is performed using the bitwise operation ____.

**Correct Answer:** **XOR**

**Intuition:** Polynomial addition over GF(2) corresponds to coefficient addition modulo 2, which is equivalent to bitwise XOR.

---

### 16. Diffie and Hellman's 1976 breakthrough addressed which two problems inherent in purely symmetric

- A. The need for a trusted certificate authority and the cost of hardware acceleration
- B. Resistance to brute-force attacks and resistance to differential cryptanalysis
- C. Encryption speed and the size of the ciphertext produced for short messages
- D. Secure key distribution without a pre-shared secret, and the lack of a scheme equivalent to a handwritten digital

**Correct Answer:** **D. Secure key distribution without a pre-shared secret, and the lack of a scheme equivalent to a**

**Intuition:** Public-key cryptography solved key exchange over insecure channels and created digital signature mechanisms.

---

### 17. Why is MixColumns skipped in the final AES round rather than in every round?

- A. Because skipping it doubles the effective key length of the cipher
- B. Because MixColumns cannot be computed on the very last block of a message
- C. To keep encryption invertible and simple while still ensuring the earlier rounds provide adequate diffusion
- D. Because the final round always uses a 256-bit key regardless of the chosen AES variant

**Correct Answer:** **C. To keep encryption invertible and simple while still ensuring the earlier rounds provide**

**Intuition:** Skipping MixColumns in the last round makes the inverse cipher structurally identical to the forward cipher without compromising diffusion.

---

### 18. According to the design-parameter discussion of Feistel ciphers, below a certain number of rounds a

- A. The S-boxes lose their nonlinear behavior entirely
- B. Differential cryptanalysis can become cheaper than an exhaustive key search
- C. The block size effectively shrinks with each additional round
- D. The key schedule stops generating distinct subkeys for each round

**Correct Answer:** **B. Differential cryptanalysis can become cheaper than an exhaustive key search**

**Intuition:** Too few rounds leave statistical differentials and linear paths detectable, making cryptanalysis faster than brute force.

---

### 19. The Blum Blum Shub (BBS) generator produces each output bit by:

- A. Computing the discrete logarithm of the previous output modulo a large prime
- B. XORing the previous two output bits together, similar to a shift register
- C. Directly encrypting a counter value using AES in CTR mode
- D. Repeatedly squaring a value modulo n = p*q and taking the least significant bit of the result each round

**Correct Answer:** **D. Repeatedly squaring a value modulo n = p*q and taking the least significant bit of the result**

**Intuition:** BBS evaluates x_{i+1} = x_i^2 mod n (n = p*q) and outputs the least significant bit (or parity bit) at each step.

---

### 20. The AES State array arranges the 16 bytes of a block into a matrix of:

- A. 8 rows by 2 columns
- B. 2 rows by 8 columns
- C. 4 rows by 4 columns
- D. 16 rows by 1 column

**Correct Answer:** **C. 4 rows by 4 columns**

**Intuition:** The 16 bytes of a 128-bit block are arranged in a 4-row by 4-column column-major matrix.

---

### 21. The AES round transformation that performs a non-linear byte-by-byte substitution using a fixed lookup

**Correct Answer:** **SubBytes**

**Intuition:** SubBytes uses an S-box lookup based on GF(2^8) inversion and an affine mapping to provide non-linear confusion.

---

### 22. A deterministic algorithm that takes a seed and produces a long sequence of numbers that statistically

**Correct Answer:** **pseudorandom-number-generator**

**Intuition:** A Pseudorandom Number Generator (PRNG) deterministically expands a short random seed into a longer pseudorandom sequence.

---

### 23. A finite field, or Galois field GF(q), is a finite set of elements with addition and multiplication such that:

- A. Every element, including zero, is required to have a multiplicative inverse
- B. Only addition is guaranteed to have inverses; multiplication need not be invertible
- C. The number of elements q must always be an even number
- D. Every nonzero element has a multiplicative inverse and the usual algebraic laws (associativity, commutativity,

**Correct Answer:** **D. Every nonzero element has a multiplicative inverse and the usual algebraic laws**

**Intuition:** A field is an algebraic structure where addition and multiplication are commutative and every non-zero element has a multiplicative inverse.

---

### 24. In an extension field GF(2^m), each element can be represented as:

- A. A single decimal digit between 0 and m
- B. A polynomial of degree less than m with binary (0 or 1) coefficients, equivalent to an m-bit string
- C. An ordered pair of prime numbers whose product is less than 2^m
- D. A matrix of size m by m containing only prime entries

**Correct Answer:** **B. A polynomial of degree less than m with binary (0 or 1) coefficients, equivalent to an m-bit**

**Intuition:** Elements of GF(2^m) are polynomials of degree <= m - 1 with binary coefficients {0, 1}.

---

### 25. The efficient method that finds the greatest common divisor of two integers through repeated division is

**Correct Answer:** **Euclidean**

**Intuition:** The Euclidean Algorithm finds gcd(a, b) in logarithmic time by repeatedly taking division remainders.

---

### 26. The block cipher mode that XORs each plaintext block with the previous ciphertext block before

**Correct Answer:** **Cipher-Block-Chaining**

**Intuition:** Cipher Block Chaining (CBC) encrypts C_i = E_K(P_i XOR C_{i-1}) with C_0 = IV.

---

### 27. RSA was developed in 1977 by Ron Rivest, Adi Shamir, and Len ____, whose initials give the algorithm its

**Correct Answer:** **Adleman**

**Intuition:** RSA is named after its creators: Ron Rivest, Adi Shamir, and Leonard Adleman.

---

### 28. Applying Fermat's Little Theorem with a = 3 and p = 7, the value of 3^6 mod 7 must equal:

- A. 6
- B. 3
- C. 1
- D. 0

**Correct Answer:** **C. 1**

**Intuition:** Fermat's Little Theorem states that a^{p-1} = 1 mod p for prime p coprime to a. Here 3^6 = 1 mod 7.

---

### 29. The block cipher mode specifically designed for encrypting data on sector-based block storage devices

**Correct Answer:** **XTS-AES**

**Intuition:** XTS-AES is the tweakable block cipher standard designed for sector-level storage encryption.

---

### 30. Feistel's design goal was to approximate the security of an ideal block cipher while avoiding its main

- A. A key large enough to select among 2^n! possible transformations, which is computationally unmanageable
- B. A separate physical key exchange for every message sent
- C. A trusted third party to certify the block size in advance
- D. Hardware capable of performing floating-point arithmetic

**Correct Answer:** **A. A key large enough to select among 2^n! possible transformations, which is**

**Intuition:** An ideal block cipher requires specifying an arbitrary permutation from (2^n)! possibilities, requiring an impractical key length of ~n*2^n bits.

---

### 31. An element a is called a primitive root of a prime p when:

- A. a raised to any power always produces the same remainder modulo p
- B. The successive powers of a, taken modulo p, cycle through every nonzero remainder before repeating
- C. a is the smallest prime factor of p minus one
- D. a itself must also be prime and strictly greater than p

**Correct Answer:** **B. The successive powers of a, taken modulo p, cycle through every nonzero remainder before**

**Intuition:** A primitive root generates the complete set of non-zero residues modulo p.

---

### 32. An integer p greater than 1 is defined as prime when:

- A. It cannot be expressed as the product of any two smaller integers at all
- B. Its only positive divisors are 1 and itself
- C. It has exactly three distinct positive divisors, including itself
- D. It is odd and also not divisible by 3 or 5

**Correct Answer:** **B. Its only positive divisors are 1 and itself**

**Intuition:** A prime number is an integer greater than 1 with exactly two distinct positive divisors: 1 and itself.

---

### 33. The value that provides variability so that identical plaintext blocks do not produce identical ciphertext at

**Correct Answer:** **initialization-vector**

**Intuition:** The Initialization Vector (IV) provides uniqueness and randomness to prevent identical ciphertexts under the same key.

---

### 34. In a stream cipher, ciphertext is produced by:

- A. Substituting each plaintext block with a fixed-size hash of that block
- B. Passing the plaintext through several parallel S-boxes without any key material
- C. Multiplying the plaintext by the key modulo a large prime number
- D. XORing the plaintext with a keystream generated from the secret key by a PRNG

**Correct Answer:** **D. XORing the plaintext with a keystream generated from the secret key by a PRNG**

**Intuition:** Stream ciphers encrypt by XORing plaintext bits directly with pseudorandom keystream bits.

---

### 35. The statement a ≡ b (mod n) means that:

- A. a multiplied by b is always evenly divisible by n
- B. n divides (a - b), so a and b leave the same remainder when divided by n
- C. a and b are both prime numbers that happen to share the modulus n
- D. a and b must be equal integers before applying the modulus operation

**Correct Answer:** **B. n divides (a - b), so a and b leave the same remainder when divided by n**

**Intuition:** a = b mod n implies n divides (a - b) without remainder.

---

### 36. XTS-AES ties encryption to a particular physical storage location by using:

- A. A running counter that resets to zero once per day
- B. A separate hash function computed over the entire disk
- C. A second, independently generated AES key for every sector
- D. A tweak value derived from the sector or block address, alongside the key

**Correct Answer:** **D. A tweak value derived from the sector or block address, alongside the key**

**Intuition:** XTS-AES encrypts the sector address as a tweak value to make ciphertext dependent on disk physical locations.

---

### 37. DES uses an initial permutation, ____ rounds of processing, and then the inverse of the initial

**Correct Answer:** **16**

**Intuition:** Standard DES executes 16 Feistel rounds between the Initial Permutation and Inverse Initial Permutation.

---

### 38. A message encrypted only with the sender's private key, as in a basic digital signature scheme, provides

- A. Digital signatures are only ever applied to a hash of the message, never its content
- B. Anyone who has the sender's public key can decrypt and read the message
- C. The message is never actually transformed, only tagged with a plaintext label
- D. The private key used is always shorter than the key used for encryption alone

**Correct Answer:** **B. Anyone who has the sender's public key can decrypt and read the message**

**Intuition:** Because the corresponding public key is openly available, any observer can decrypt and read the message.

---

### 39. The elliptic curve discrete logarithm problem, the hard problem underlying ECC security, asks an attacker

- A. Recover the integer k given a base point P and the point kP obtained by repeated point addition
- B. Factor the coefficients a and b that define the elliptic curve equation
- C. Compute the y-coordinate of a point given only its x-coordinate, without a curve equation
- D. Find two distinct points on the curve that sum to the point at infinity

**Correct Answer:** **A. Recover the integer k given a base point P and the point kP obtained by repeated point**

**Intuition:** ECDLP is the challenge of determining scalar integer k given base point P and scalar multiple Q = kP.

---

### 40. The recommended padding scheme that randomizes RSA plaintext before encryption, defending against

**Correct Answer:** **OAEP**

**Intuition:** Optimal Asymmetric Encryption Padding (OAEP) provides semantic security and chosen-ciphertext resistance for RSA.

---

### 41. Concern about the DES S-boxes containing a deliberate weakness arose mainly because:

- A. IBM and the NSA never publicly disclosed the exact criteria used to design them
- B. They were replaced entirely in the final published version of the standard
- C. They were later shown to reduce the effective key length to under 40 bits
- D. Independent researchers had mathematically proven a fatal structural flaw in them

**Correct Answer:** **A. IBM and the NSA never publicly disclosed the exact criteria used to design them**

**Intuition:** Classified S-box design criteria led to suspicions of trapdoors, though they were actually optimized against differential attacks.

---

### 42. Euler's Theorem, a^phi(n) is congruent to 1 (mod n) provided that gcd(a, n) = 1, is best described as:

- A. An unrelated result used exclusively for testing whether n is a perfect square
- B. A generalization of Fermat's Little Theorem that applies to any modulus n, not only prime moduli
- C. A restatement of the Euclidean Algorithm using exponents instead of remainders
- D. A special case of Fermat's Little Theorem that only applies when n itself is prime

**Correct Answer:** **B. A generalization of Fermat's Little Theorem that applies to any modulus n, not only prime**

**Intuition:** Euler's Totient Theorem generalizes Fermat's Little Theorem from prime moduli to arbitrary composite moduli.

---

### 43. Claude Shannon's principle by which each plaintext digit affects many digits of the ciphertext, hiding

**Correct Answer:** **diffusion**

**Intuition:** Diffusion spreads single-bit plaintext differences across multiple ciphertext output bits.

---

### 44. RC4's real-world downfall in Wi-Fi security came primarily through WEP because:

- A. WEP replaced RC4 with a much weaker, custom-designed stream cipher
- B. RC4 cannot process variable-length keys, forcing WEP to use a single fixed key
- C. WEP's method of generating and reusing keys fed into RC4 was flawed, not the RC4 algorithm itself in isolation
- D. RC4 itself was mathematically broken and could be reversed without any key at all

**Correct Answer:** **C. WEP's method of generating and reusing keys fed into RC4 was flawed, not the RC4**

**Intuition:** WEP concatenated 24-bit predictable IVs with the key, causing keystream reuse and enabling FMS key recovery.

---

### 45. A common misconception about public-key cryptography, according to the chapter, is the belief that it:

- A. Cannot be used for digital signatures, only for encrypting messages directly
- B. Requires exactly the same amount of computation as symmetric encryption for bulk data
- C. Makes symmetric encryption obsolete, when in fact its overhead confines it mainly to signatures and key management
- D. Was invented decades after RSA, rather than being the concept RSA itself is built on

**Correct Answer:** **C. Makes symmetric encryption obsolete, when in fact its overhead confines it mainly to**

**Intuition:** Public-key cryptography is computationally slow, so symmetric encryption remains essential for bulk data encryption.

---

### 46. NIST's CTR_DRBG, the modern standard block-cipher-based PRNG, operates through which three

- A. Initialize (seed from entropy), Generate (encrypt and increment a counter), and Update (periodically reseed with fresh
- B. Shuffle, Swap, and Output, exactly as in the RC4 algorithm
- C. Encrypt, Decrypt, and Re-encrypt, exactly as in Triple DES
- D. Select primes, Compute totient, and Generate keys, exactly as in RSA

**Correct Answer:** **A. Initialize (seed from entropy), Generate (encrypt and increment a counter), and Update**

**Intuition:** NIST SP 800-90A CTR_DRBG defines instantiation (initialize), generate (produce pseudorandom output), and reseed/update.

---

### 47. For an elliptic curve defined over the real numbers as y^2 = x^3 + ax + b, adding two distinct points P and

- A. Multiplying the x-coordinates of P and Q together to get the new x-coordinate
- B. Drawing the line through P and Q, finding its third intersection with the curve, and reflecting that point across the x-
- C. Reflecting P alone across the y-axis without ever considering Q's position
- D. Averaging the x-coordinates and y-coordinates of P and Q directly

**Correct Answer:** **B. Drawing the line through P and Q, finding its third intersection with the curve, and reflecting**

**Intuition:** The chord-and-tangent rule finds the third intersection point R of line PQ with the curve and reflects it across the x-axis.

---

### 48. The widely deployed stream cipher designed by Ron Rivest in 1987, later used in SSL/TLS and WEP, is

**Correct Answer:** **RC4**

**Intuition:** RC4 (Rivest Cipher 4) is the byte-oriented stream cipher designed by Ron Rivest.

---

### 49. Multiplication in GF(2^m) is performed by:

- A. Multiplying the polynomials and then reducing the result modulo a fixed irreducible polynomial
- B. Simply XORing the two operands together, exactly as in addition
- C. Looking up the product directly in a table of prime factorizations
- D. Adding the two polynomials and discarding any bits beyond position m

**Correct Answer:** **A. Multiplying the polynomials and then reducing the result modulo a fixed irreducible**

**Intuition:** GF(2^m) multiplication multiplies binary polynomials and reduces the result modulo an irreducible polynomial of degree m.

---

### 50. RC4 begins with a Key Scheduling Algorithm (KSA) that:

- A. Fixes the state array S to a constant, unchanging table for every key
- B. Directly encrypts the plaintext without ever touching a state array
- C. Uses the secret key to scramble a 256-byte state array S into a key-dependent permutation
- D. Generates a brand-new AES key for every byte of output produced

**Correct Answer:** **C. Uses the secret key to scramble a 256-byte state array S into a key-dependent permutation**

**Intuition:** The KSA initializes state S[0..255] and performs 256 key-dependent swaps.

---

### 51. In evaluating candidate round functions F for a block cipher, the strict avalanche criterion (SAC)

- A. Each output bit should change with probability one-half whenever a single input bit is inverted
- B. The round function should use exactly the same number of rounds as the key length in bits
- C. Every output bit should be a linear combination of the input bits
- D. The ciphertext should always be exactly the same length as the plaintext

**Correct Answer:** **A. Each output bit should change with probability one-half whenever a single input bit is**

**Intuition:** SAC requires that inverting any single input bit flips each output bit with independent probability 0.5.

---

### 52. The Chinese Remainder Theorem allows a number to be uniquely reconstructed within a given range

- A. Its binary representation alone, without reference to any modulus
- B. A single large modulus formed by adding all the smaller moduli together
- C. Its remainders with respect to a set of moduli that share no common factors with one another
- D. Its prime factorization expressed in base two

**Correct Answer:** **C. Its remainders with respect to a set of moduli that share no common factors with one**

**Intuition:** CRT guarantees a unique integer solution modulo the product of pairwise coprime moduli.

---

### 53. In RSA, the public key is the pair {e, n} and the private key is the pair {____, n}.

**Correct Answer:** **d**

**Intuition:** The private decryption key pair in RSA is {d, n} where d = e^{-1} mod phi(n).

---

### 1. A standard defense against RSA timing attacks is to:

- A. Ensure exponentiation always takes constant time, or add blinding by masking the ciphertext with a random factor
- B. Disable the use of the Chinese Remainder Theorem during decryption entirely
- C. Switch to a smaller RSA key size so that decryption completes faster
- D. Encrypt every message twice in succession using the same public key

**Correct Answer:** **A. Ensure exponentiation always takes constant time, or add blinding by masking the**

**Intuition:** Blinding multiplies ciphertext by r^e mod n prior to decryption, removing data-dependent timing signatures.

---

### 1. Using the LCG recurrence Xn+1 = (5*Xn + 3) mod 16 with seed X0 = 7, the first two outputs X1 and X2 are:

- A. X1 = 1, X2 = 6
- B. X1 = 7, X2 = 3
- C. X1 = 6, X2 = 1
- D. X1 = 3, X2 = 6

**Correct Answer:** **C. X1 = 6, X2 = 1**

**Intuition:** X1 = (5*7 + 3) mod 16 = 38 mod 16 = 6; X2 = (5*6 + 3) mod 16 = 33 mod 16 = 1.

---

### 1. The security of the Blum Blum Shub generator rests on:

- A. The unpredictability of thermal noise sampled from physical hardware
- B. The difficulty of solving a system of linear congruential equations
- C. The length of the AES key used inside its internal encryption step
- D. The difficulty of factoring n back into its two large prime factors, the same hard problem underlying RSA

**Correct Answer:** **D. The difficulty of factoring n back into its two large prime factors, the same hard problem**

**Intuition:** BBS security reduces to the computational difficulty of calculating quadratic residues, equivalent to factoring n = p*q.

---

### 1. Given 84 = 2^2 x 3 x 7 and 126 = 2 x 3^2 x 7, gcd(84, 126) equals:

- A. 21
- B. 42
- C. 84
- D. 126

**Correct Answer:** **B. 42**

**Intuition:** gcd(84, 126) = 2^1 * 3^1 * 7^1 = 42.

---

### 1. Shannon's principle of diffusion is achieved mainly by:

- A. Replacing the round function with a simple table lookup
- B. Making the ciphertext statistics depend on the key in a highly complex way
- C. Reducing the key length needed to resist brute-force search
- D. Spreading the influence of each plaintext bit over many bits of the ciphertext

**Correct Answer:** **D. Spreading the influence of each plaintext bit over many bits of the ciphertext**

**Intuition:** Diffusion dissipates individual plaintext bit patterns across large regions of ciphertext.

---

### 1. Using the Chinese Remainder Theorem to split RSA decryption into two smaller modular exponentiations,

**Correct Answer:** **4**

**Intuition:** CRT modular exponentiations are on half-sized moduli with cubic-complexity multiplication, yielding ~4x speedup.

---

### 1. In a Feistel cipher, the relationship that generates the right half of round i is:

- A. Ri = F(Li-1, Ki) XOR Ri-1 XOR Li-1
- B. Ri = Li-1 XOR F(Ri-1, Ki)
- C. Ri = Li-1 AND F(Ri-1, Ki)
- D. Ri = F(Ri-1, Ki-1) XOR Li

**Correct Answer:** **B. Ri = Li-1 XOR F(Ri-1, Ki)**

**Intuition:** In a Feistel round, R_i = L_{i-1} XOR F(R_{i-1}, K_i).

---

### 1. Given x ≡ 2 (mod 3) and x ≡ 3 (mod 5), the Chinese Remainder Theorem gives the unique solution in the

- A. x = 11
- B. x = 8
- C. x = 13
- D. x = 2

**Correct Answer:** **B. x = 8**

**Intuition:** 8 mod 3 = 2 and 8 mod 5 = 3; 8 is the unique integer solution in [0, 14].

---

### 1. The block cipher mode that turns a block cipher into a stream cipher by encrypting a counter value for

**Correct Answer:** **Counter**

**Intuition:** Counter (CTR) mode turns a block cipher into a stream cipher by encrypting sequential counter values.

---

### 1. The points on an elliptic curve, together with a defined addition rule and a point at infinity, form:

- A. An abelian group, satisfying closure, associativity, an identity element, inverses, and commutativity
- B. A Feistel structure, alternating substitution and permutation at each point
- C. A finite field in the same sense as GF(p), with every point having a multiplicative inverse
- D. A simple ring with no guarantee that every point has an inverse

**Correct Answer:** **A. An abelian group, satisfying closure, associativity, an identity element, inverses, and**

**Intuition:** Under chord-and-tangent addition with point at infinity O, elliptic curve points form an abelian group.

---

### 1. A trap-door one-way function is defined as a function that is:

- A. A function that produces the exact same output regardless of its input
- B. Easy to invert for everyone, regardless of whether they hold any secret information
- C. Impossible to compute in both directions under any circumstances
- D. Easy to compute in one direction, and easy to invert only if you possess a secret piece of extra information

**Correct Answer:** **D. Easy to compute in one direction, and easy to invert only if you possess a secret piece of**

**Intuition:** A trapdoor function is easy forward, hard to invert, but efficiently invertible with special trapdoor knowledge.

---

### 1. Which pair correctly matches an AES key size with its corresponding number of rounds?

- A. 192-bit key -> 10 rounds
- B. 256-bit key -> 12 rounds
- C. 192-bit key -> 12 rounds
- D. 128-bit key -> 14 rounds

**Correct Answer:** **C. 192-bit key -> 12 rounds**

**Intuition:** AES-128 uses 10 rounds, AES-192 uses 12 rounds, and AES-256 uses 14 rounds.

---

### 1. The avalanche effect, as illustrated by flipping a single bit of DES plaintext, refers to the property that:

- A. A small change in the key always leaves the ciphertext completely unchanged
- B. A small change in the input produces a large, seemingly unrelated change in the output ciphertext
- C. The ciphertext becomes shorter as more plaintext bits are altered
- D. Every round of DES must be repeated twice to detect tampering

**Correct Answer:** **B. A small change in the input produces a large, seemingly unrelated change in the output**

**Intuition:** The avalanche effect ensures a 1-bit input flip alters approximately 50% of the ciphertext bits.

---

### 1. AES was selected by NIST through an open competition, with the winning algorithm originally named

**Correct Answer:** **Rijndael**

**Intuition:** Rijndael, created by Vincent Rijmen and Joan Daemen, was standardized as AES.

---

### 1. Basic, unauthenticated Diffie-Hellman is vulnerable to a man-in-the-middle attack because:

- A. The discrete logarithm problem becomes trivially easy once two parties are involved
- B. The primitive root alpha must be kept secret, and any leak instantly reveals the key
- C. The protocol does not authenticate either party, allowing an attacker to establish separate shared keys with each side
- D. Diffie-Hellman transmits the shared secret key directly, in plaintext, over the channel

**Correct Answer:** **C. The protocol does not authenticate either party, allowing an attacker to establish separate**

**Intuition:** Unauthenticated Diffie-Hellman does not verify sender identities, allowing active adversaries to intercept and negotiate split keys.

---

### 1. Double DES (encrypting twice with two different 56-bit keys) is considered insufficient mainly because it

- A. A chosen-plaintext attack that recovers the key from a single ciphertext block
- B. A simple brute-force search that is no harder than breaking single DES
- C. A meet-in-the-middle attack, which reduces its effective strength far below a true 112-bit key
- D. An attack that only works if ECB mode is used alongside it

**Correct Answer:** **C. A meet-in-the-middle attack, which reduces its effective strength far below a true 112-bit key**

**Intuition:** Meet-in-the-middle attacks find table collisions between forward and reverse encryptions in ~2^57 steps.

---

### 1. Inside a DES round, the 32-bit right half is expanded to 48 bits mainly so that it can be:

- A. Directly output as the new left half without further processing
- B. Combined via XOR with the 48-bit round subkey before passing through the S-boxes
- C. Compared bit-by-bit against the original plaintext for error checking
- D. Split evenly between the eight S-boxes without any subkey involved

**Correct Answer:** **B. Combined via XOR with the 48-bit round subkey before passing through the S-boxes**

**Intuition:** The E-box expands 32 bits to 48 bits to match the 48-bit subkey for XORing before substitution in the 8 S-boxes.

---

### 1. The block cipher mode in which each plaintext block is encrypted independently with the same key, and

**Correct Answer:** **Electronic-Codebook**

**Intuition:** Electronic Codebook (ECB) encrypts each block in isolation, leaking statistical patterns.

---

### 1. If plaintext bit P = 1 is XORed with keystream bit K = 0, and the resulting ciphertext bit C is later XORed

- A. 0, because two XOR operations always cancel out to zero
- B. 1, recovering the original plaintext bit exactly
- C. Undefined, since XOR cannot be reversed without also knowing P in advance
- D. 1, but only if K had instead been equal to 1

**Correct Answer:** **B. 1, recovering the original plaintext bit exactly**

**Intuition:** C = 1 XOR 0 = 1; C XOR K = 1 XOR 0 = 1, restoring P since P XOR K XOR K = P.

---

### 1. Using the Chinese Remainder Theorem to speed up RSA's private-key operations works by:

- A. Splitting the decryption exponentiation into two smaller computations modulo p and modulo q, then recombining the
- B. Replacing modular exponentiation entirely with simple XOR operations
- C. Avoiding the need to know either p or q once the public key has been published
- D. Reducing the RSA key size requirement from 2048 bits down to 512 bits

**Correct Answer:** **A. Splitting the decryption exponentiation into two smaller computations modulo p and modulo**

**Intuition:** RSA-CRT evaluates C^{d mod p-1} mod p and C^{d mod q-1} mod q separately, recombining via CRT.

---

### 1. After the KSA, RC4's Pseudo-Random Generation Algorithm (PRGA) produces the keystream by:

- A. Continuously swapping entries within the permuted state array S and combining selected entries to output one byte at
- B. Applying the SHA-1 hash function repeatedly to the previous keystream byte
- C. Reading the secret key directly, byte by byte, without any further processing
- D. Encrypting a running counter with a block cipher and outputting the ciphertext bytes

**Correct Answer:** **A. Continuously swapping entries within the permuted state array S and combining selected**

**Intuition:** PRGA updates pointer indices i and j, swaps S[i] and S[j], and outputs S[(S[i]+S[j]) mod 256] per loop.

---

### 1. A network structure built from alternating layers of substitution and permutation across multiple rounds,

**Correct Answer:** **permutation**

**Intuition:** A Substitution-Permutation Network (SPN) alternates S-boxes (confusion) and P-boxes (diffusion).

---

### 1. Which mode of operation is generally considered to have no safe use case for general-purpose

- A. CTR
- B. ECB
- C. CBC
- D. OFB

**Correct Answer:** **B. ECB**

**Intuition:** ECB mode encrypts identical plaintext blocks to identical ciphertext blocks, failing semantic security.

---

### 1. Choosing a very small public exponent such as e = 3 without message padding creates a risk known as:

- A. A doubling of the ciphertext length compared to using a larger exponent
- B. An immediate leak of the private exponent d to any observer of the ciphertext
- C. A complete loss of the ability to decrypt the message even with the correct key
- D. A cube-root attack, where the same message sent to multiple recipients can be recovered without factoring n

**Correct Answer:** **D. A cube-root attack, where the same message sent to multiple recipients can be recovered**

**Intuition:** Without padding, small exponent RSA (e=3) is vulnerable to Håstad's broadcast attack via CRT and direct root extraction.

---

### 1. When selecting a mode of operation for high-throughput, parallelizable, general-purpose encryption, the

- A. ECB mode
- B. XTS-AES, regardless of whether the data is stored or transmitted
- C. CFB mode with a very small segment size
- D. CTR mode

**Correct Answer:** **D. CTR mode**

**Intuition:** CTR keystream generation depends solely on the block index counter, enabling full parallelization across CPU cores.

---

### 1. A mode of operation is best defined as:

- A. A set of rules describing how a block cipher should be applied to encrypt data longer than a single block
- B. An alternative block cipher algorithm used only for very large files
- C. A method for generating the encryption key from a user-supplied password
- D. A hardware-only technique that cannot be implemented in software

**Correct Answer:** **A. A set of rules describing how a block cipher should be applied to encrypt data longer than a**

**Intuition:** A mode of operation defines algorithms and feedback chaining to securely encrypt sequences of arbitrary length.

---

### 1. Which requirement is essential when parameterizing an RSA-based PRNG such as Micali-Schnorr?

- A. e must be chosen equal to the private exponent d used for RSA decryption
- B. gcd(e, phi(n)) = 1, mirroring the same requirement used for ordinary RSA key generation
- C. The modulus n must be chosen to be a small prime number, unlike ordinary RSA
- D. The output length r must always exceed the modulus n's bit length

**Correct Answer:** **B. gcd(e, phi(n)) = 1, mirroring the same requirement used for ordinary RSA key generation**

**Intuition:** For x |-> x^e mod n to be an invertible permutation over Z_n^*, e must be coprime to phi(n).

---

### 1. Given public parameters q = 353 and alpha = 3, with Alice's private key XA = 97 and public key YA = 40,

- A. K = XA * XB mod q = 97 * 233 mod 353
- B. K = YA^XB mod q = 40^233 mod 353
- C. K = YB^XA mod q = 248^97 mod 353
- D. K = alpha^(XA+XB) mod q, computed without ever using YA or YB

**Correct Answer:** **C. K = YB^XA mod q = 248^97 mod 353**

**Intuition:** In DH, Alice computes the shared secret as K = Y_B^{X_A} mod q = 248^97 mod 353.

---

### 1. In Cipher Block Chaining (CBC) mode, the input to the encryption function for a given block is:

- A. The XOR of the current plaintext block with the next plaintext block
- B. The previous plaintext block encrypted a second time
- C. The XOR of the current plaintext block with the previous ciphertext block (or the IV, for the first block)
- D. The plaintext block alone, exactly as in ECB mode

**Correct Answer:** **C. The XOR of the current plaintext block with the previous ciphertext block (or the IV, for the**

**Intuition:** In CBC mode, Input_i = P_i XOR C_{i-1} (with C_0 = IV).

---

### 1. The AES key expansion algorithm's g() function, applied to certain words, involves:

- A. Rotating the bytes of the word, applying the S-box to each byte, then XORing in a round constant
- B. Reversing the entire 128-bit key and discarding half of it
- C. Multiplying the word by the AES modulus polynomial directly
- D. Applying the inverse ShiftRows transformation to the word

**Correct Answer:** **A. Rotating the bytes of the word, applying the S-box to each byte, then XORing in a round**

**Intuition:** The AES key schedule g(w) routine applies RotWord (cyclic shift), SubWord (S-box), and XOR with Rcon.

---

### 1. Which of the following was NOT one of the finalist algorithms in the AES selection process?

- A. Twofish
- B. MARS
- C. Blowfish
- D. Serpent

**Correct Answer:** **C. Blowfish**

**Intuition:** Blowfish is a 64-bit cipher designed in 1993. The 5 AES finalists were Rijndael, Serpent, Twofish, MARS, and RC6.

---

### 1. NIST's selection of Rijndael as AES was notable because it was:

- A. Chosen without any competing candidate algorithms being considered
- B. The result of an open, multi-round public competition rather than an algorithm designed internally by the government
- C. The first cipher ever to be patented by a government standards body
- D. Selected purely on the basis of being the fastest candidate in hardware

**Correct Answer:** **B. The result of an open, multi-round public competition rather than an algorithm designed**

**Intuition:** NIST hosted an open multi-round international competition with transparent public cryptanalysis.

---

### 1. In the Micali-Schnorr RSA-based PRNG, each stage encrypts the current internal state and then splits the

- A. Some bits feed back to seed the next stage while the remaining bits form part of the pseudorandom output
- B. All of the output bits are discarded and only the feedback bits are ever kept
- C. Half of the RSA modulus n is regenerated fresh at every single stage
- D. The entire output becomes the feedback value for the next stage, with nothing output

**Correct Answer:** **A. Some bits feed back to seed the next stage while the remaining bits form part of the**

**Intuition:** Micali-Schnorr splits x_i^e mod n into pseudorandom output bits and seed feedback for the next stage.

---

### 1. Increasing the block size of a Feistel cipher generally:

- A. Improves security through greater diffusion, at the cost of more processing time per block
- B. Has no measurable effect on either security or processing time
- C. Removes the need for multiple rounds of processing
- D. Weakens security because larger blocks leak more statistical structure

**Correct Answer:** **A. Improves security through greater diffusion, at the cost of more processing time per block**

**Intuition:** Larger blocks improve diffusion and resist birthday/dictionary attacks, but increase register size and compute cycles.

---

### 1. Triple DES (3DES), typically applying Encrypt-Decrypt-Encrypt with two or three keys, achieves an

- A. 168 bits, using three independent keys
- B. 56 bits, the same as single DES
- C. 224 bits, matching twice the length of AES-256's key
- D. 112 bits, even when three independent keys are used

**Correct Answer:** **A. 168 bits, using three independent keys**

**Intuition:** 3DES using 3 independent 56-bit DES keys has a nominal total key length of 3 * 56 = 168 bits.

---

### 1. The Diffie-Hellman key exchange allows two parties to establish a shared secret key by:

- A. Directly transmitting the shared secret key encrypted under RSA
- B. Meeting in person beforehand to physically exchange the key on paper
- C. Using a trusted third party to generate and distribute the key to both sides
- D. Exchanging public values computed from private exponents over an insecure channel, without ever transmitting the

**Correct Answer:** **D. Exchanging public values computed from private exponents over an insecure channel,**

**Intuition:** Both sides exchange only modular exponentiations alpha^X mod q, computing the shared secret independently.

---

### 1. A common practical design pairs a TRNG with a PRNG by:

- A. Alternating output bits strictly one-for-one between the TRNG and the PRNG
- B. Using the PRNG to produce entropy that is then fed back into the TRNG's hardware
- C. Using the TRNG's physical entropy to seed the PRNG, combining true unpredictability with the PRNG's speed and
- D. Running both generators completely independently and never combining their outputs

**Correct Answer:** **C. Using the TRNG's physical entropy to seed the PRNG, combining true unpredictability with**

**Intuition:** A physical TRNG harvests hardware entropy to seed/reseed a high-throughput deterministic PRNG.

---

### 1. The Prime Number Theorem indicates that, near a large integer n, prime numbers occur on average about

- A. 2 integers checked, since every other integer is prime past a certain point
- B. ln(n) integers checked
- C. n integers checked, regardless of how large n becomes
- D. sqrt(n) integers checked, matching the trial-division bound

**Correct Answer:** **B. ln(n) integers checked**

**Intuition:** The Prime Number Theorem establishes that prime density near integer n is asymptotically 1 / ln(n).

---

### 1. The Intel Digital Random Number Generator (DRNG), used in Intel processors since 2012, combines

- A. A thermal-noise entropy source, a bias-removing conditioner, and a CTR_DRBG stage exposed through the RDRAND
- B. A user-supplied password hashed once with SHA-1 and output directly
- C. Two independent TRNGs whose raw, unconditioned outputs are simply concatenated
- D. An LCG seeded from the system clock, followed directly by RC4 encryption

**Correct Answer:** **A. A thermal-noise entropy source, a bias-removing conditioner, and a CTR_DRBG stage**

**Intuition:** Intel DRNG features a thermal noise entropy source latch, CBC-MAC conditioner, and AES-CTR DRBG engine.

---

### 1. Which AES round transformation is the only one that is non-linear, providing the algorithm's confusion?

- A. SubBytes
- B. ShiftRows
- C. AddRoundKey
- D. MixColumns

**Correct Answer:** **A. SubBytes**

**Intuition:** SubBytes uses inversion in GF(2^8) to provide the cipher's essential non-linear confusion.

---

### 1. Testing whether 29 is prime by checking divisibility only up to sqrt(29) ≈ 5.4 works because:

- A. Any factor larger than the square root of a number must be paired with a factor smaller than the square root
- B. Numbers greater than the square root are automatically assumed to be prime
- C. The square root always equals exactly half of the number being tested
- D. 29 is a special case, and this shortcut does not generalize to any other number

**Correct Answer:** **A. Any factor larger than the square root of a number must be paired with a factor smaller than**

**Intuition:** If n = a * b, both factors cannot exceed sqrt(n); at least one factor must be <= sqrt(n).

---

### 1. A mode of operation that allows random access to any individual block without first decrypting all

- A. ECB mode used together with an initialization vector
- B. CTR mode, since each block's keystream depends only on its own counter value
- C. CFB mode, since it processes data in variable-size segments
- D. CBC mode, since each block depends on the ciphertext immediately before it

**Correct Answer:** **B. CTR mode, since each block's keystream depends only on its own counter value**

**Intuition:** CTR keystream blocks are computed directly from block counter indices, allowing instant random access.

---

### 1. A defining advantage of the Feistel structure is that:

- A. No subkey schedule is required, since the same key is reused every round
- B. Decryption uses the identical algorithm as encryption, only with the subkeys applied in reverse order
- C. The round function F must itself be a reversible, invertible operation
- D. Encryption and decryption each require a completely separate algorithm

**Correct Answer:** **B. Decryption uses the identical algorithm as encryption, only with the subkeys applied in**

**Intuition:** Feistel networks decrypt using the identical forward circuit simply by reversing the subkey schedule.

---

### 1. In Diffie-Hellman, both public parameters q (a prime) and alpha (a primitive root of q) are:

- A. Derived mathematically from each party's private exponent after the exchange
- B. Generated fresh for every single message exchanged between the parties
- C. Kept secret and known only to the two communicating parties
- D. Known publicly to everyone, including any potential attacker

**Correct Answer:** **D. Known publicly to everyone, including any potential attacker**

**Intuition:** Modulus q and generator alpha are public parameters known to everyone.

---

### 1. A True Random Number Generator (TRNG) differs from a PRNG chiefly in that a TRNG:

- A. Draws its randomness from an unpredictable physical process, such as thermal noise, rather than a deterministic
- B. Cannot be used to seed any other type of random number generator
- C. Requires a secret key to be shared in advance between sender and receiver
- D. Always produces output faster than any PRNG can achieve

**Correct Answer:** **A. Draws its randomness from an unpredictable physical process, such as thermal noise,**

**Intuition:** TRNGs harvest nondeterministic physical noise, whereas PRNGs apply deterministic mathematical algorithms to expand seeds.

---

### 1. An ideal block cipher mapping n bits to n bits allows how many possible reversible mappings?

- A. 2^n
- B. n!
- C. (2^n)!
- D. 2^(2n)

**Correct Answer:** **C. (2^n)!**

**Intuition:** There are 2^n possible input states, and any reversible mapping is a permutation of these states, yielding (2^n)! possible bijections.

---

### 1. The primary advantage of asymmetric key cryptography over symmetric key cryptography in large

- A. Asymmetric cryptography is computationally faster for bulk file transfers
- B. It scales with N key pairs for N users instead of N*(N-1)/2 shared secret keys
- C. It uses shorter keys to achieve the same bit-strength security as AES
- D. It eliminates the need for mathematical modular arithmetic

**Correct Answer:** **B. It scales with N key pairs for N users instead of N*(N-1)/2 shared secret keys**

**Intuition:** In a network of N users, symmetric encryption requires N*(N-1)/2 pre-shared secret keys, whereas public-key cryptography requires only N key pairs.

---
