# DCIT 418: Systems and Network Security
## Interim Assessment (IA): Sakai Offsite 2026
**Department of Computer Science, University of Ghana**  
**Course Code:** DCIT 418 | **Credits:** 3 Credits  
**Prepared by:** Ryan Brown  
**Source / Links Provided by:** Bayat, Christian, Eugene, and Ryan  
**Source Format / Reference:** Sakai Offsite IA Exam Consolidated Question Bank & Solutions  

---

### 📝 Study Checklist & Progress Tracker
- [ ] **I have done the MCQs (118 Questions)** *(Last attempted: )*
- [ ] **I have done the Fill-in-the-Blank questions (40 Questions)** *(Last attempted: )*

---

> [!NOTE]
> **Prepared by:** Ryan Brown  
> **Source / Links Provided by:** Bayat, Christian, Eugene, and Ryan  
> This document contains the consolidated question pool (158 Questions), verified answer keys, and detailed solutions for the **DCIT 418: Interim Assessment (Sakai Offsite 2026)**.
> - A complete **Answer Summary Table** (12-column grid format) is provided at the top for rapid revision.
> - A comprehensive **Question Frequency & Repetition Analysis Table** highlights repeated questions and occurrence counts across all student test takes (**Bayat's Take**, **Christian's Take**, **Eugene's Take**, and **Ryan's Take**).
> - Each question features an interactive **"Reveal Answer"** drop-down containing the verified answer, exact option text, and thorough engineering/conceptual intuition based on William Stallings' *Cryptography and Network Security*.

## Complete Answer Summary Table

| Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|---|--------|---|--------|
| **1** | AKS | **28** | C | **55** | D | **82** | B | **109** | Key Expansion | **136** | D |
| **2** | State | **29** | B | **56** | D | **83** | A | **110** | C | **137** | Keystream |
| **3** | B | **30** | ECB mode | **57** | D | **84** | B | **111** | C | **138** | Keystream |
| **4** | B | **31** | CTR mode | **58** | Primitive Root | **85** | A | **112** | C | **139** | B |
| **5** | C | **32** | CBC mode | **59** | D | **86** | B | **113** | OAEP | **140** | A |
| **6** | C | **33** | D | **60** | C | **87** | A | **114** | A | **141** | Fundamental Thm |
| **7** | D | **34** | C | **61** | Euclidean | **88** | D | **115** | ShiftRows | **142** | C |
| **8** | D | **35** | D | **62** | C | **89** | A | **116** | B | **143** | D |
| **9** | A | **36** | C | **63** | B | **90** | B | **117** | C | **144** | D |
| **10** | D | **37** | LCG | **64** | C | **91** | A | **118** | d | **145** | A |
| **11** | A | **38** | Diffusion | **65** | D | **92** | D | **119** | B | **146** | A |
| **12** | A | **39** | Confusion | **66** | A | **93** | A | **120** | D | **147** | A |
| **13** | MixColumns | **40** | C | **67** | B | **94** | B | **121** | C | **148** | 4 (or 4x) |
| **14** | SubBytes | **41** | C | **68** | A | **95** | B | **122** | d | **149** | A |
| **15** | C | **42** | C | **69** | B | **96** | A | **123** | Adleman | **150** | C |
| **16** | C | **43** | D | **70** | A | **97** | Permutation | **124** | D | **151** | IV |
| **17** | C | **44** | A | **71** | B | **98** | A | **125** | B | **152** | D |
| **18** | Rijndael | **45** | C | **72** | Miller-Rabin | **99** | B | **126** | Abelian group | **153** | C |
| **19** | A | **46** | D | **73** | B | **100** | BBS | **127** | D | **154** | C |
| **20** | Field | **47** | B | **74** | A | **101** | C | **128** | D | **155** | RC4 |
| **21** | C | **48** | C | **75** | B | **102** | B | **129** | B | **156** | B |
| **22** | B | **49** | C | **76** | C | **103** | C | **130** | B | **157** | A |
| **23** | Meet-in-the-Middle | **50** | B | **77** | D | **104** | C | **131** | A | **158** | D |
| **24** | Timing Attack | **51** | B | **78** | Trapdoor | **105** | A | **132** | A |  |  |
| **25** | B | **52** | 48 bits | **79** | TRNG | **106** | D | **133** | B |  |  |
| **26** | Primitive Root | **53** | 16 rounds | **80** | C | **107** | B | **134** | D |  |  |
| **27** | C | **54** | PRNG | **81** | XOR | **108** | Discrete Log | **135** | B |  |  |

---

## 📊 Question Frequency & Repetition Analysis Table

| Q# | Question Topic / Core Concept | Type | Answer | Repetition Count | Test Occurrences / Source Takes |
|:---|:------------------------------|:----:|:------:|:----------------:|:--------------------------------|
| **1** | AKS deterministic polynomial-time primality test | FIB | AKS | **1x** | Bayat's Take |
| **2** | The 4x4 byte matrix that AES | FIB | State | **1x** | Bayat's Take |
| **3** | Euclidean Algorithm and Greatest Common Divisor (GCD) | MCQ | B | **5x** | Christian's Take, Ryan's Take |
| **4** | Feistel cipher round count & differential cryptanalysis | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **5** | Digital signatures: Authentication vs Confidentiality | MCQ | C | **2x** | Bayat's Take, Ryan's Take |
| **6** | Addition of two elements in GF2m | MCQ | C | **1x** | Bayat's Take |
| **7** | AddRoundKey transformation role & secret key mixing | MCQ | D | **4x** | Christian's Take, Ryan's Take |
| **8** | AES always operates on a fixed | MCQ | D | **1x** | Bayat's Take |
| **9** | AES is best classified structurally as | MCQ | A | **1x** | Bayat's Take |
| **10** | AES security foundation & 128+ bit keyspace | MCQ | D | **1x** | Bayat's Take |
| **11** | The AES key expansion algorithms g | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **12** | Shannon's principle of confusion | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **13** | Galois field GF(2^8) arithmetic in AES | FIB | MixColumns | **1x** | Bayat's Take |
| **14** | The AES round transformation that performs | FIB | SubBytes | **4x** | Bayat's Take, Christian's Take |
| **15** | SubBytes S-box transformation in AES | MCQ | C | **1x** | Ryan's Take |
| **16** | AES State array 4x4 matrix representation | MCQ | C | **4x** | Bayat's Take, Christian's Take |
| **17** | Triple DES (3DES) key length and performance | MCQ | C | **2x** | Eugene's Take, Ryan's Take |
| **18** | AES selection of Rijndael by Daemen and Rijmen | FIB | Rijndael | **5x** | Bayat's Take, Christian's Take, Eugene's Take |
| **19** | Stream cipher keystream generation and XOR | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **20** | Initialization Vector (IV) variability in block ciphers | FIB | Field | **1x** | Bayat's Take |
| **21** | Fermat's Little Theorem formulation and powers | MCQ | C | **3x** | Christian's Take |
| **22** | ECC vs. RSA key size and efficiency advantages | MCQ | B | **2x** | Bayat's Take, Ryan's Take |
| **23** | Meet-in-the-middle attack on Double DES | FIB | Meet-in-the-Middle | **4x** | Bayat's Take, Christian's Take |
| **24** | An attack that infers secret key | FIB | Timing Attack | **1x** | Bayat's Take |
| **25** | Avalanche effect in block ciphers | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **26** | Definition of a primitive root modulo a prime | FIB | Primitive Root | **3x** | Christian's Take |
| **27** | Basic unauthenticated DiffieHellman is vulnerable to | MCQ | C | **6x** | Bayat's Take, Christian's Take, Eugene's Take, Ryan's Take |
| **28** | Output Feedback (OFB) mode transmission error behavior | MCQ | C | **1x** | Ryan's Take |
| **29** | A block cipher differs from a | MCQ | B | **1x** | Bayat's Take |
| **30** | The block cipher mode in which | FIB | ECB mode | **4x** | Christian's Take, Eugene's Take |
| **31** | The block cipher mode that turns | FIB | CTR mode | **4x** | Bayat's Take, Christian's Take |
| **32** | Initialization Vector (IV) variability in block ciphers | FIB | CBC mode | **3x** | Christian's Take |
| **33** | Blum Blum Shub (BBS) generator security & bit extraction | MCQ | D | **6x** | Bayat's Take, Christian's Take, Ryan's Take |
| **34** | Chinese Remainder Theorem (CRT) unique reconstruction | MCQ | C | **7x** | Bayat's Take, Christian's Take |
| **35** | Choosing a very small public exponent | MCQ | D | **3x** | Christian's Take |
| **36** | Cipher Block Chaining (CBC) mode mechanics | MCQ | C | **3x** | Christian's Take |
| **37** | The classic simple algorithm defined by | FIB | LCG | **1x** | Bayat's Take |
| **38** | Claude Shannons principle by which each | FIB | Diffusion | **4x** | Bayat's Take, Christian's Take |
| **39** | Claude Shannons principle by which the | FIB | Confusion | **1x** | Bayat's Take |
| **40** | Combining secrecy and authentication (Sign-then-Encrypt) | MCQ | C | **2x** | Bayat's Take, Ryan's Take |
| **41** | A common misconception about publickey cryptography | MCQ | C | **3x** | Christian's Take |
| **42** | True Random Number Generators (TRNG) physical entropy | MCQ | C | **3x** | Christian's Take |
| **43** | Discrete logarithm problem computational hardness | MCQ | D | **1x** | Ryan's Take |
| **44** | DES S-box design criteria & NSA controversy | MCQ | A | **5x** | Bayat's Take, Christian's Take, Eugene's Take |
| **45** | RSA decryption calculation (n=187, d=23, C=11) | MCQ | C | **1x** | Bayat's Take |
| **46** | A cryptographic hashlike construction can be | MCQ | D | **1x** | Bayat's Take |
| **47** | For cryptographic use elliptic curve arithmetic | MCQ | B | **1x** | Ryan's Take |
| **48** | Statistical randomness vs. cryptographic unpredictability | MCQ | C | **1x** | Bayat's Take |
| **49** | Counter (CTR) mode stream behavior and parallelization | MCQ | C | **2x** | Bayat's Take, Ryan's Take |
| **50** | A defining advantage of the Feistel | MCQ | B | **3x** | Christian's Take |
| **51** | DES processes plaintext through which overall | MCQ | B | **2x** | Eugene's Take, Ryan's Take |
| **52** | The DES round function expands the | FIB | 48 bits | **2x** | Bayat's Take, Eugene's Take |
| **53** | DES uses an initial permutation rounds | FIB | 16 rounds | **4x** | Christian's Take, Eugene's Take |
| **54** | True Random Number Generators (TRNG) physical entropy | FIB | PRNG | **4x** | Bayat's Take, Christian's Take |
| **55** | Diffie-Hellman 1976 asymmetric breakthrough problems | MCQ | D | **3x** | Christian's Take |
| **56** | Definition of a primitive root modulo a prime | MCQ | D | **5x** | Christian's Take, Eugene's Take, Ryan's Take |
| **57** | The DiffieHellman key exchange allows two | MCQ | D | **4x** | Bayat's Take, Christian's Take |
| **58** | The DiffieHellman protocol requires two public | FIB | Primitive Root | **1x** | Bayat's Take |
| **59** | Discrete logarithm problem computational hardness | MCQ | D | **1x** | Bayat's Take |
| **60** | Meet-in-the-middle attack on Double DES | MCQ | C | **3x** | Christian's Take |
| **61** | Initialization Vector (IV) variability in block ciphers | FIB | Euclidean | **3x** | Christian's Take |
| **62** | Electronic Codebook (ECB) pattern leakage | MCQ | C | **1x** | Bayat's Take |
| **63** | Definition of a primitive root modulo a prime | MCQ | B | **3x** | Christian's Take |
| **64** | ElGamal cryptosystem foundation & discrete logarithms | MCQ | C | **1x** | Bayat's Take |
| **65** | ElGamal ephemeral key k reuse vulnerability | MCQ | D | **2x** | Bayat's Take, Ryan's Take |
| **66** | ECC vs. RSA key size and efficiency advantages | MCQ | A | **3x** | Christian's Take |
| **67** | For an elliptic curve defined over | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **68** | Discrete logarithm problem computational hardness | MCQ | A | **3x** | Christian's Take |
| **69** | Modular congruence definition: n divides (a - b) | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **70** | Strict Avalanche Criterion (SAC) in round functions | MCQ | A | **5x** | Bayat's Take, Christian's Take, Eugene's Take |
| **71** | In an extension field GF2m each | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **72** | Miller-Rabin probabilistic primality test | FIB | Miller-Rabin | **4x** | Bayat's Take, Christian's Take |
| **73** | In a Feistel cipher the relationship | MCQ | B | **5x** | Bayat's Take, Christian's Take, Ryan's Take |
| **74** | Ideal block cipher 2^n! transformation key complexity | MCQ | A | **4x** | Christian's Take, Eugene's Take |
| **75** | Fermat's Little Theorem formulation and powers | MCQ | B | **2x** | Bayat's Take, Ryan's Take |
| **76** | The final round of AES encryption | MCQ | C | **3x** | Christian's Take |
| **77** | A finite field or Galois field | MCQ | D | **4x** | Bayat's Take, Christian's Take |
| **78** | A function that is easy to | FIB | Trapdoor | **1x** | Bayat's Take |
| **79** | True Random Number Generators (TRNG) physical entropy | FIB | TRNG | **1x** | Bayat's Take |
| **80** | GF(2^8) arithmetic operations | MCQ | C | **3x** | Christian's Take |
| **81** | In GF2m addition of two field | FIB | XOR | **4x** | Bayat's Take, Christian's Take |
| **82** | Stream cipher keystream generation and XOR | MCQ | B | **3x** | Christian's Take |
| **83** | Increasing the block size of a | MCQ | A | **3x** | Christian's Take |
| **84** | Inside a DES round the 32bit | MCQ | B | **3x** | Christian's Take |
| **85** | Initialization Vector (IV) variability in block ciphers | MCQ | A | **1x** | Bayat's Take |
| **86** | An integer p greater than 1 | MCQ | B | **5x** | Bayat's Take, Christian's Take, Ryan's Take |
| **87** | The Intel Digital Random Number Generator | MCQ | A | **3x** | Christian's Take |
| **88** | CBC vs CTR mode error propagation comparison | MCQ | D | **1x** | Bayat's Take |
| **89** | Electronic Codebook (ECB) pattern leakage | MCQ | A | **1x** | Bayat's Take |
| **90** | Digital signatures: Authentication vs Confidentiality | MCQ | B | **3x** | Christian's Take |
| **91** | Pseudorandom Number Generators (PRNG) determinism | MCQ | A | **3x** | Christian's Take |
| **92** | Shannon's principle of diffusion | MCQ | D | **1x** | Bayat's Take |
| **93** | Definition of a block cipher mode of operation | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **94** | Which mode of operation is generally | MCQ | B | **3x** | Christian's Take |
| **95** | Initialization Vector (IV) variability in block ciphers | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **96** | Multiplication in GF2m is performed by | MCQ | A | **3x** | Christian's Take |
| **97** | A network structure built from alternating | FIB | Permutation | **4x** | Bayat's Take, Christian's Take |
| **98** | NIST CTR_DRBG operating phases (Init, Gen, Update) | MCQ | A | **5x** | Bayat's Take, Christian's Take, Ryan's Take |
| **99** | AES selection of Rijndael by Daemen and Rijmen | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **100** | Pseudorandom Number Generators (PRNG) determinism | FIB | BBS | **2x** | Bayat's Take, Eugene's Take |
| **101** | Which of the following was NOT | MCQ | C | **3x** | Christian's Take |
| **102** | RSA-OAEP padding against chosen-ciphertext attacks | MCQ | B | **1x** | Bayat's Take |
| **103** | Which pair correctly matches an AES | MCQ | C | **4x** | Bayat's Take, Christian's Take |
| **104** | Plain unpadded RSA is described as | MCQ | C | **1x** | Bayat's Take |
| **105** | The points on an elliptic curve | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **106** | Modular arithmetic range confinement {0, 1, ..., n-1} | MCQ | D | **4x** | Christian's Take, Ryan's Take |
| **107** | The Prime Number Theorem indicates that | MCQ | B | **3x** | Christian's Take |
| **108** | Discrete logarithm problem computational hardness | FIB | Discrete Log | **3x** | Christian's Take |
| **109** | The process that stretches the original | FIB | Key Expansion | **1x** | Bayat's Take |
| **110** | Initialization Vector (IV) variability in block ciphers | MCQ | C | **5x** | Bayat's Take, Christian's Take, Ryan's Take |
| **111** | RC4 stream cipher & WEP key scheduling vulnerability | MCQ | C | **4x** | Bayat's Take, Christian's Take |
| **112** | RC4 stream cipher & WEP key scheduling vulnerability | MCQ | C | **3x** | Christian's Take |
| **113** | The recommended padding scheme that randomizes | FIB | OAEP | **5x** | Bayat's Take, Christian's Take, Eugene's Take |
| **114** | Remember the distinction | MCQ | A | **1x** | Ryan's Take |
| **115** | AES selection of Rijndael by Daemen and Rijmen | FIB | ShiftRows | **1x** | Ryan's Take |
| **116** | Pseudorandom Number Generators (PRNG) determinism | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **117** | Stream cipher keystream generation and XOR | MCQ | C | **1x** | Bayat's Take |
| **118** | In RSA encryption of message M | FIB | d | **1x** | Bayat's Take |
| **119** | RSA totient phi(n) calculation from primes p and q | MCQ | B | **3x** | Christian's Take |
| **120** | RSAs underlying trapdoor oneway function relies | MCQ | D | **1x** | Eugene's Take |
| **121** | RSA private exponent d as multiplicative inverse of e mod phi(n) | MCQ | C | **2x** | Eugene's Take, Ryan's Take |
| **122** | Initialization Vector (IV) variability in block ciphers | FIB | d | **4x** | Christian's Take, Eugene's Take |
| **123** | RSA creators: Ron Rivest, Adi Shamir, and Leonard Adleman | FIB | Adleman | **4x** | Bayat's Take, Christian's Take |
| **124** | Blum Blum Shub (BBS) generator security & bit extraction | MCQ | D | **3x** | Christian's Take |
| **125** | Modular congruence definition: n divides (a - b) | MCQ | B | **2x** | Bayat's Take, Ryan's Take |
| **126** | Elliptic curve points algebraic structure (Abelian group) | FIB | Abelian group | **4x** | Bayat's Take, Christian's Take |
| **127** | Shannon's principle of confusion | MCQ | D | **1x** | Bayat's Take |
| **128** | Shannon's principle of diffusion | MCQ | D | **3x** | Christian's Take |
| **129** | ShiftRows row cyclic shifting in AES | MCQ | B | **1x** | Bayat's Take |
| **130** | Square-and-multiply modular exponentiation efficiency | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **131** | RSA timing side-channel attack (Kocher) | MCQ | A | **3x** | Christian's Take |
| **132** | The standard practical fix for the | MCQ | A | **1x** | Bayat's Take |
| **133** | The statement a b mod n | MCQ | B | **4x** | Bayat's Take, Christian's Take |
| **134** | CBC vs CTR mode error propagation comparison | MCQ | D | **2x** | Eugene's Take, Ryan's Take |
| **135** | True Random Number Generators (TRNG) physical entropy | MCQ | B | **2x** | Bayat's Take, Eugene's Take |
| **136** | In a stream cipher ciphertext is | MCQ | D | **3x** | Christian's Take |
| **137** | Pseudorandom Number Generators (PRNG) determinism | FIB | Keystream | **3x** | Christian's Take |
| **138** | For a stream cipher to be | FIB | Keystream | **1x** | Eugene's Take |
| **139** | Permutation definition in classical/modern ciphers | MCQ | B | **1x** | Bayat's Take |
| **140** | Initialization Vector (IV) variability in block ciphers | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **141** | The theorem guaranteeing that every integer | FIB | Fundamental Thm | **3x** | Christian's Take |
| **142** | RSA timing side-channel attack (Kocher) | MCQ | C | **3x** | Bayat's Take, Eugene's Take, Ryan's Take |
| **143** | Timingattack research on DES found that | MCQ | D | **1x** | Ryan's Take |
| **144** | A trapdoor oneway function is defined | MCQ | D | **6x** | Christian's Take |
| **145** | Triple DES (3DES) key length and performance | MCQ | A | **3x** | Christian's Take |
| **146** | True Random Number Generators (TRNG) physical entropy | MCQ | A | **4x** | Bayat's Take, Christian's Take |
| **147** | Initialization Vector (IV) variability in block ciphers | MCQ | A | **3x** | Christian's Take |
| **148** | Using the Chinese Remainder Theorem to | FIB | 4 (or 4x) | **3x** | Christian's Take |
| **149** | Euclidean Algorithm and Greatest Common Divisor (GCD) | MCQ | A | **2x** | Bayat's Take, Eugene's Take |
| **150** | Linear Congruential Generator (LCG) predictability | MCQ | C | **4x** | Bayat's Take, Christian's Take |
| **151** | Cipher Block Chaining (CBC) mode mechanics | FIB | IV | **4x** | Bayat's Take, Christian's Take |
| **152** | When selecting a mode of operation | MCQ | D | **4x** | Christian's Take, Eugene's Take |
| **153** | Euclidean Algorithm and Greatest Common Divisor (GCD) | MCQ | C | **1x** | Bayat's Take |
| **154** | Omission of MixColumns in the final AES round | MCQ | C | **4x** | Bayat's Take, Christian's Take |
| **155** | RC4 stream cipher & WEP key scheduling vulnerability | FIB | RC4 | **3x** | Christian's Take |
| **156** | Initialization Vector (IV) variability in block ciphers | MCQ | B | **4x** | Christian's Take, Eugene's Take |
| **157** | XTS-AES mode for block storage and tweak values | MCQ | A | **2x** | Bayat's Take, Eugene's Take |
| **158** | XTS-AES mode for block storage and tweak values | MCQ | D | **5x** | Bayat's Take, Christian's Take, Eugene's Take |

---

## Exam Questions & Detailed Solutions

### 1. The 2002 algorithm that was the first ever proven to determine primality with total certainty in polynomial time is called the ____ algorithm.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **AKS algorithm (or Agrawal–Kayal–Saxena algorithm)**

*Intuition:* Published in 2002 by Manindra Agrawal, Neeraj Kayal, and Nitin Saxena, the AKS primality test was the first deterministic algorithm that can determine whether a given number is prime or composite in polynomial time (specifically, $\mathcal{O}((\log n)^{12})$ time, later improved to $\mathcal{O}((\log n)^6)$), without relying on any unproven assumptions like the Generalized Riemann Hypothesis.
</details>

---

### 2. The 4x4 byte matrix that AES loads the plaintext block into, and which every round transformation operates on, is called the ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **State (or state array)**

*Intuition:* In AES, the plaintext block is loaded into a 4×4 matrix of bytes (for a 128-bit block), and this matrix is referred to as the State. Every round transformation (SubBytes, ShiftRows, MixColumns, and AddRoundKey) operates directly on this State matrix throughout the encryption process.
</details>

---

### 3. Given 84 = 2^2 x 3 x 7 and 126 = 2 x 3^2 x 7, gcd(84, 126) equals:
- A. 21
- B. 42
- C. 84
- D. 126

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 42**

*Intuition:* Using prime factorizations: $84 = 2^2 \times 3 \times 7$ and $126 = 2 \times 3^2 \times 7$. Taking the lowest power of each common prime factor: $\gcd(84, 126) = 2^{\min(2,1)} \times 3^{\min(1,2)} \times 7^{\min(1,1)} = 2^1 \times 3^1 \times 7^1 = 42$.
</details>

---

### 4. According to the design-parameter discussion of Feistel ciphers, below a certain number of rounds a cipher becomes more vulnerable because:
- A. The S-boxes lose their nonlinear behavior entirely
- B. Differential cryptanalysis can become cheaper than an exhaustive key search
- C. The block size effectively shrinks with each additional round
- D. The key schedule stops generating distinct subkeys for each round

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Differential cryptanalysis can become cheaper than an exhaustive key search**

*Intuition:* In Feistel ciphers, each round provides diffusion and confusion. If the number of rounds is too low, the cipher may not have enough diffusion to fully obscure the relationships between plaintext, ciphertext, and the key. This allows advanced attacks like differential cryptanalysis or linear cryptanalysis to break the cipher with less computational effort than a brute-force exhaustive key search. Increasing the number of rounds makes such attacks impractical by ensuring that the probability of useful differential or linear characteristics becomes so low that the attack requires more work than simply trying all possible keys. The design discussion typically notes that the minimum number of rounds must be set high enough so that the best known cryptanalytic attack is no better than brute force.
</details>

---

### 5. To achieve authentication (a digital signature) using a public-key cryptosystem, a sender encrypts a message using:
- A. The recipient's public key, so that only the recipient can later decrypt and verify it
- B. The recipient's private key, shared with the sender ahead of time for this purpose
- C. Their own private key, so that anyone with the matching public key can verify the message's origin
- D. A key derived by hashing the recipient's public key together with a nonce

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Their own private key, so that anyone with the matching public key can verify the message's origin**

*Intuition:* To create a digital signature (achieve authentication and non-repudiation), the sender encrypts (or more precisely, signs) the message using their own private key. Anyone who has the corresponding public key can then decrypt/verify the signature and confirm that the message originated from the sender (since only the sender possesses the private key). This is the core principle of public-key digital signatures: Signing: Signature = E ( P R a , message ) Signature=E(PR a ​ ,message) or Signature = E ( P R a , hash(message) ) Signature=E(PR a ​ ,hash(message)) Verification: Anyone computes D ( P U a , Signature ) D(PU a ​ ,Signature) and compares it to the message or its hash. The other options are incorrect: A: Encrypting with the recipient's public key provides confidentiality (secrecy), not authentication. B: The recipient's private key is never shared with anyone; it must remain secret. D: Hashing with a nonce is not how standard digital signatures work; it would not provide the binding to the sender's identity.
</details>

---

### 6. Addition of two elements in $GF(2^m)$ is carried out as:
- A. Concatenation of the two bit strings into one longer string
- B. Ordinary decimal addition followed by reduction modulo m
- C. Bitwise XOR of the corresponding binary coefficients, with no carrying
- D. Multiplication of the two elements' polynomial representations

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Bitwise XOR of the corresponding binary coefficients, with no carrying**

*Intuition:* In G F ( 2 m ) GF(2 m ), each field element is represented as a polynomial over G F ( 2 ) GF(2) (or equivalently, a binary bit string). Addition is performed by adding the coefficients of like powers of x x modulo 2. Since 1 + 1 = 0 1+1=0 in G F ( 2 ) GF(2), this results in a simple bitwise XOR of the two bit strings, with no carry propagation involved.
</details>

---

### 7. AddRoundKey is the only AES transformation that:
- A. Requires computation in GF(2^8) using a fixed multiplication matrix
- B. Provides nonlinearity through a substitution table
- C. Reorders bytes without changing any of their values
- D. Directly incorporates the secret key material into the State, via XOR with the round key

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Directly incorporates the secret key material into the State, via XOR with the round key**

*Intuition:* Why D is correct: In AES, AddRoundKey is the only round operation where the State array is combined directly with the expanded key schedule (by performing a bitwise XOR with the 128-bit round key). Without AddRoundKey, the other three transformations (SubBytes, ShiftRows, MixColumns) are purely deterministic permutations and substitutions with no dependence on the secret key. Why the others are incorrect: A describes the MixColumns transformation. B describes the SubBytes transformation (which uses the S-box). C describes the ShiftRows transformation. Given public parameters q = 353 and alpha = 3, with Alice's private key XA = 97 and public key YA = 3^97 mod 353 = 40, and Bob's private key XB = 233 and public key YB = 3^233 mod 353 = 248, Alice computes the shared secret as:
</details>

---

### 8. AES always operates on a fixed block size of:
- A. 64 bits
- B. 192 bits
- C. 256 bits
- D. 128 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. 128 bits**

*Intuition:* AES (Advanced Encryption Standard) always operates on a fixed block size of 128 bits (16 bytes), regardless of the key size used (128, 192, or 256 bits). The block size is invariant and is the same for all variants of AES. The key sizes vary (128, 192, or 256 bits), and the number of rounds depends on the key size (10, 12, or 14 rounds respectively), but the block size remains 128 bits throughout. This is in contrast to its predecessor, the Rijndael algorithm, which supported variable block sizes; NIST standardized only the 128-bit block size version as AES.
</details>

---

### 9. AES is best classified structurally as a:
- A. Substitution-permutation network operating on the full block every round, not a Feistel cipher
- B. Hash-based construction with no dependency on a secret key
- C. Stream cipher that produces one keystream byte at a time
- D. Feistel cipher that splits its block into two halves each round

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Substitution-permutation network operating on the full block every round, not a Feistel cipher**

*Intuition:* AES is structurally a Substitution-Permutation Network (SPN). In each round, it applies: SubBytes (substitution using an S-box) — provides confusion, ShiftRows and MixColumns (permutations/diffusion) — provide diffusion, AddRoundKey (XOR with the round key) — mixes in the key. Crucially, AES operates on the entire 128-bit block in parallel during every round, rather than splitting the block into halves and applying a Feistel structure (as in DES, which is a Feistel cipher). The other options are incorrect because: B: AES is a block cipher that depends on a secret key, not a hash function. C: AES is a block cipher, not a stream cipher (though it can be used in stream-like modes like CTR). D: AES does not use a Feistel structure; it uses an SPN.
</details>

---

### 10. AES is generally considered secure today mainly because:
- A. Its block size grows automatically as computing power increases
- B. Its algorithm and S-box design have never been published or reviewed publicly
- C. It uses a Feistel structure, which is inherently immune to differential cryptanalysis
- D. Its 2^128 (or larger) keyspace makes brute force infeasible, and decades of public cryptanalysis have found no effective shortcut attack

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Its 2^128 (or larger) keyspace makes brute force infeasible, and decades of public cryptanalysis have found no effective shortcut attack**

*Intuition:* AES is considered secure because: The key space (128, 192, or 256 bits) is sufficiently large to make exhaustive brute-force search completely infeasible with current and foreseeable technology. Since its selection as the Advanced Encryption Standard in 2001, it has undergone extensive public scrutiny and cryptanalysis, and no practical shortcut attacks (significantly better than brute force) have been found against the full AES algorithm. The other options are incorrect because: A: AES has a fixed block size of 128 bits; it does not grow automatically. B: AES's algorithm and S-box design were fully published and openly reviewed during the standardization process. C: AES uses a substitution-permutation network (SPN), not a Feistel structure; and no structure is "inherently immune" to differential cryptanalysis—though AES was specifically designed to resist it.
</details>

---

### 11. The AES key expansion algorithm's g() function, applied to certain words, involves:
- A. Rotating the bytes of the word, applying the S-box to each byte, then XORing in a round constant
- B. Reversing the entire 128-bit key and discarding half of it
- C. Multiplying the word by the AES modulus polynomial directly
- D. Applying the inverse ShiftRows transformation to the word

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Rotating the bytes of the word, applying the S-box to each byte, then XORing in a round constant**

*Intuition:* In the AES key expansion algorithm, the g() function (also called the key schedule core or RotWord-SubWord-Rcon) is applied to every fourth word of the expanded key schedule. The function consists of three steps: RotWord: Perform a cyclic left shift (rotation) of the 4-byte word by one byte (e.g., [a, b, c, d] → [b, c, d, a]). SubWord: Apply the AES S-box (SubBytes) to each of the four bytes individually. Rcon (Round Constant): XOR the resulting word with a round constant (Rcon) — a fixed value from G F ( 2 8 ) GF(2 8 ) that depends on the round number. The result is then XORed with the appropriate word from the previous group to produce the next word in the expanded key schedule. This process ensures that the round keys are distinct and that there is no simple linear relationship between them. The other options are incorrect: B: Reversing and discarding is not part of AES key expansion. C: Multiplying by the AES modulus polynomial is part of MixColumns, not key expansion. D: Inverse ShiftRows is a transformation used in decryption, not in key expansion. The AES-based mode approved by NIST in 2010 specifically for encrypting block-oriented storage devices such as disks is called ____. Answer: XTS-AES Maximum number of characters (including HTML tags added by text editor): 32,000 Your answer is correct. The NIST-approved mode specifically designed for encrypting block-oriented storage devices (such as hard disks and solid-state drives) is XTS-AES (XEX-based Tweaked Codebook mode with Ciphertext Stealing). It was officially standardized by NIST in 2010 as Special Publication 800-38E. XTS-AES uses a tweak derived from the logical block address to ensure that identical plaintext blocks at different disk locations encrypt to different ciphertexts, providing security against attacks like block shuffling.
</details>

---

### 12. Which AES round transformation is the only one that is non-linear, providing the algorithm's confusion?
- A. SubBytes
- B. ShiftRows
- C. AddRoundKey
- D. MixColumns

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. SubBytes**

*Intuition:* The SubBytes transformation is the only non-linear step in the AES round function. It applies a fixed S-box (substitution table) to each byte of the State independently, performing a non-linear mapping over G F ( 2 8 ) GF(2 8 ). This non-linearity is essential for providing confusion, which obscures the relationship between the plaintext, ciphertext, and the key—making it resistant to linear and differential cryptanalysis. The other transformations are linear or affine: ShiftRows – is a linear permutation (byte transposition). MixColumns – is a linear transformation over G F ( 2 8 ) GF(2 8 ). AddRoundKey – is an XOR operation, which is linear. Together, the combination of non-linear SubBytes with the linear/diffusion steps gives AES its strength.
</details>

---

### 13. The AES round transformation that mixes the four bytes within each column using matrix multiplication over $GF(2^8)$ is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **MixColumns (or Mix Column transformation)**

*Intuition:* In AES, the MixColumns step operates independently on each column of the state array, treating each column as a four-term polynomial and multiplying it by a fixed polynomial a ( x ) = { 03 } x 3 + { 01 } x 2 + { 01 } x + { 02 } a(x)={03}x 3 +{01}x 2 +{01}x+{02} over G F ( 2 8 ) GF(2 8 ). This provides diffusion by mixing the four bytes within each column.
</details>

---

### 14. The AES round transformation that performs a non-linear byte-by-byte substitution using a fixed lookup table is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **SubBytes (or SubByte transformation)**

*Intuition:* The SubBytes transformation is the non-linear step in AES that substitutes each byte of the State independently using a fixed 16×16 lookup table called the S-box. This S-box is constructed using inversion in G F ( 2 8 ) GF(2 8 ) followed by an affine transformation over G F ( 2 ) GF(2), providing the confusion essential to AES's security.
</details>

---

### 15. The AES S-box used in SubBytes is constructed from:
- A. A simple Caesar-style shift applied to each byte value
- B. The XOR of each byte with the AES key expansion constant
- C. The multiplicative inverse in GF(2^8) followed by an affine transformation
- D. A random permutation generated fresh for every encryption session

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The multiplicative inverse in GF(2^8) followed by an affine transformation**

*Intuition:* Why C is correct: The AES S-box is designed algebraically to maximize non-linearity and minimize resistance to differential and linear cryptanalysis. Each byte is mapped to its multiplicative inverse in the finite field GF(2 8 ) (with the element {00} mapped to itself), followed by an invertible affine transformation over GF(2). Why the others are incorrect: A is linear and provides zero non-linear cryptographic confusion. B confuses the S-box substitution with the AddRoundKey step. D is false because the AES S-box is fixed, standardized, and deterministic, not dynamically generated per session.
</details>

---

### 16. The AES State array arranges the 16 bytes of a block into a matrix of:
- A. 8 rows by 2 columns
- B. 2 rows by 8 columns
- C. 4 rows by 4 columns
- D. 16 rows by 1 column

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. 4 rows by 4 columns**

*Intuition:* The AES state array arranges the 128-bit (16-byte) plaintext block into a 4×4 matrix of bytes. The bytes are loaded column by column (the first 4 bytes form the first column, the next 4 bytes form the second column, and so on). This 4×4 matrix is the fundamental data structure that all AES round transformations (SubBytes, ShiftRows, MixColumns, and AddRoundKey) operate on.
</details>

---

### 17. AES was adopted as a replacement for DES/Triple DES mainly because:
- A. NIST wanted an algorithm based on a Feistel network rather than a substitution-permutation network
- B. DES had a mathematically proven flaw that made every message recoverable
- C. Triple DES was too slow for many applications while still relying on a 64-bit block, and DES's 56-bit key was no longer safe
- D. AES was the only submitted candidate that supported a 128-bit key at all

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Triple DES was too slow for many applications while still relying on a 64-bit block, and DES's 56-bit key was no longer safe**

*Intuition:* Why C is correct: DES's 56-bit key had become vulnerable to exhaustive brute-force search attacks by the late 1990s. While Triple DES (3DES) solved the key-length problem, it required three full passes of DES per block, making it computationally inefficient in software, and its 64-bit block size left it vulnerable to collision-based birthday attacks on large data streams. Why the others are incorrect: A is false because AES (Rijndael) is built on a Substitution-Permutation Network (SPN), not a Feistel structure. B is false because DES fell to brute-force key search rather than a fundamental mathematical breakdown of its round structure. D is false because all final AES candidates (such as Twofish, Serpent, and RC6) supported 128-bit blocks along with 128, 192, and 256-bit key sizes.
</details>

---

### 18. AES was selected by NIST through an open competition, with the winning algorithm originally named ____, designed by Daemen and Rijmen.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Rijndael**

*Intuition:* The winning algorithm was originally named Rijndael (a portmanteau of the names of its designers, Joan Daemen and Vincent Rijmen). It was selected by NIST in 2001 and then standardized as the Advanced Encryption Standard (AES).
</details>

---

### 19. After the KSA, RC4's Pseudo-Random Generation Algorithm (PRGA) produces the keystream by:
- A. Continuously swapping entries within the permuted state array S and combining selected entries to output one byte at a time
- B. Applying the SHA-1 hash function repeatedly to the previous keystream byte
- C. Reading the secret key directly, byte by byte, without any further processing
- D. Encrypting a running counter with a block cipher and outputting the ciphertext bytes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Continuously swapping entries within the permuted state array S and combining selected entries to output one byte at a time**

*Intuition:* After the Key Scheduling Algorithm (KSA) initializes and permutes the 256-byte state array S S based on the secret key, the Pseudo-Random Generation Algorithm (PRGA) generates the keystream by: Incrementing an index i i (mod 256). Adding S [ i ] S[i] to another index j j (mod 256). Swapping S [ i ] S[i] and S [ j ] S[j] (continuing the permutation of the state). Selecting an output byte as S [ S [ i ] + S [ j ] mod 256 ] S[S[i]+S[j]mod256]. This process produces one keystream byte per iteration, which is then XORed with the plaintext (or ciphertext) for encryption/decryption. The state continuously evolves, ensuring that the keystream appears random and is not trivially predictable from the key alone. The other options are incorrect: B: RC4 does not use SHA-1 or any hash function in its PRGA. C: The secret key is only used during the KSA; the PRGA operates on the permuted state array, not directly on the key. D: RC4 is a stream cipher, not a block cipher in counter mode; it uses its own internal state, not a block cipher.
</details>

---

### 20. An algebraic structure with two operations in which every nonzero element has a multiplicative inverse (such as GF(p) for a prime p) is called a ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **a field (specifically, a finite field or Galois field)**

*Intuition:* An algebraic structure with two operations (typically addition and multiplication) where: It forms an abelian group under addition, The nonzero elements form an abelian group under multiplication, And multiplication distributes over addition, is called a field. When the field has a finite number of elements, it is specifically called a finite field or Galois field, denoted as G F ( p ) GF(p) for prime fields (where p p is prime) or G F ( p m ) GF(p m ) for extension fields. The condition that "every nonzero element has a multiplicative inverse" is the defining property that distinguishes a field from a ring.
</details>

---

### 21. Applying Fermat's Little Theorem with a = 3 and p = 7, the value of 3^6 mod 7 must equal:
- A. 6
- B. 3
- C. 1
- D. 0

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. 1**

*Intuition:* Explanation: Fermat's Little Theorem states that if p is a prime and a is an integer not divisible by p, then: a p−1 ≡1(modp) Setting a=3 and p=7 gives 3 7−1 =3 6
</details>

---

### 22. Asymmetric ciphers such as RSA and ECC are not typically used to generate long, open-ended pseudorandom bit streams because:
- A. They require a hardware TRNG to be present, unlike every symmetric-cipher-based PRNG
- B. Asymmetric operations are comparatively slow, so they are better suited to producing a short pseudorandom function output per invocation
- C. They are mathematically incapable of producing any output that looks statistically random
- D. Their output is always shorter than the modulus n, regardless of the number of invocations

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Asymmetric operations are comparatively slow, so they are better suited to producing a short pseudorandom function output per invocation**

*Intuition:* Asymmetric ciphers like RSA and ECC are based on expensive modular exponentiation or elliptic curve scalar multiplication, which are orders of magnitude slower than symmetric operations like AES or block-cipher-based PRNGs (e.g., CTR_DRBG or Hash_DRBG). While they can produce pseudorandom output (e.g., RSA can be used in a block cipher mode like OFB or CTR, or ECC can be used for key derivation), it is highly inefficient for generating long bitstreams. Instead, they are typically used for short operations such as: Encrypting a small session key (hybrid encryption), Generating a short pseudorandom value for a challenge-response, Deriving a key via a key exchange (e.g., ECDH), Digital signatures. For long, open-ended pseudorandom streams, symmetric ciphers or dedicated PRNGs are vastly more efficient and practical.
</details>

---

### 23. The attack that defeats Double DES by working forward from the plaintext and backward from the ciphertext to find a matching intermediate value is called the ____ attack.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **meet-in-the-middle attack**

*Intuition:* The meet-in-the-middle (MITM) attack is a cryptographic attack that defeats Double DES (and other double-encryption schemes) by exploiting the fact that encrypting with two different keys, C = E K 2 ( E K 1 ( P ) ) C=E K2 ​ (E K1 ​ (P)), can be broken with much less work than a brute-force search over 2 112 2 112 keys for 2-DES. The attack works as follows: Encrypt forward: The attacker encrypts the known plaintext P P under all possible 2 56 2 56 keys for the first encryption (key K 1 K1), storing each intermediate result X = E K 1 ( P ) X=E K1 ​ (P) in a table. Decrypt backward: The attacker decrypts the known ciphertext C C under all possible 2 56 2 56 keys for the second encryption (key K 2 K2), computing X ′ = D K 2 ( C ) X ′ =D K2 ​ (C). Match: The attacker looks for a match between the forward-computed values X X and the backward-computed values X ′ X ′ . When a match is found, the corresponding keys K 1 K1 and K 2 K2 are the likely correct pair. This attack reduces the complexity from 2 112 2 112 (brute force on double-DES) to 2 56 + 2 56 = 2 57 2 56 +2 56 =2 57 operations, with moderate storage ( 2 56 2 56 ). This is why Double DES provides only about 57 bits of security, not 112 bits, and why Triple DES (with three keys) was adopted instead.
</details>

---

### 24. An attack that infers secret key information by measuring how long RSA decryption takes for different ciphertexts is called a ____ attack.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **a timing attack (or timing side-channel attack)**

*Intuition:* A timing attack is a type of side-channel attack in which the attacker observes the time it takes for a cryptographic operation (such as RSA decryption or modular exponentiation) to complete for different ciphertext inputs. Because operations like modular exponentiation or Chinese Remainder Theorem (CRT) reductions can take variable amounts of time depending on the bits of the private key, an attacker can use statistical analysis of these timing differences to recover the private key bit by bit. This attack was famously demonstrated by Paul Kocher in 1996 against RSA and other cryptosystems. Defenses against timing attacks include constant-time algorithms, blinding (adding randomness to the input before decryption), and masking operations to ensure uniform execution time regardless of the key or input.
</details>

---

### 25. The avalanche effect, as illustrated by flipping a single bit of DES plaintext, refers to the property that:
- A. A small change in the key always leaves the ciphertext completely unchanged
- B. A small change in the input produces a large, seemingly unrelated change in the output ciphertext
- C. The ciphertext becomes shorter as more plaintext bits are altered
- D. Every round of DES must be repeated twice to detect tampering

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A small change in the input produces a large, seemingly unrelated change in the output ciphertext**

*Intuition:* The avalanche effect is a desirable property of cryptographic algorithms where a minor change in the input (e.g., flipping a single bit of the plaintext or the key) results in a significant and unpredictable change in the output ciphertext—typically about half of the output bits change. This ensures that similar plaintexts or closely related keys produce completely different ciphertexts, making statistical attacks much harder. DES was specifically designed to exhibit a strong avalanche effect.
</details>

---

### 26. A base g whose successive powers modulo a prime p cycle through every nonzero remainder before repeating is called a ____ of p.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **primitive-root**

*Intuition:* The correct answer is **primitive-root**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 27. Basic, unauthenticated Diffie-Hellman is vulnerable to a man-in-the-middle attack because:
- A. The discrete logarithm problem becomes trivially easy once two parties are involved
- B. The primitive root alpha must be kept secret, and any leak instantly reveals the key
- C. The protocol does not authenticate either party, allowing an attacker to establish separate shared keys with each side while relaying and altering messages
- D. Diffie-Hellman transmits the shared secret key directly, in plaintext, over the channel

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The protocol does not authenticate either party, allowing an attacker to establish separate shared keys with each side while relaying and altering messages**

*Intuition:* Explanation: Classical Diffie-Hellman Key Exchange provides secrecy against passive eavesdroppers based on the computational difficulty of the Discrete Logarithm Problem. However, because it lacks digital signatures, certificates, or pre-shared secrets to authenticate the communicating identities, an active adversary positioned on the communication path can intercept public key values and exchange independent keys with Alice and Bob separately, decrypting and re-encrypting traffic undetectably.
</details>

---

### 28. Because OFB feeds back the encryption output rather than the ciphertext, it offers the practical advantage that:
- A. It becomes fully immune to any form of cryptanalysis
- B. It automatically compresses the ciphertext to a smaller size than the plaintext
- C. A bit error introduced during transmission affects only the corresponding plaintext bit, without cascading into later blocks
- D. No initialization vector or key is required to begin decryption

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A bit error introduced during transmission affects only the corresponding plaintext bit, without cascading into later blocks**

*Intuition:* Why C is correct: In Output Feedback (OFB) mode, the keystream is generated by repeatedly encrypting the previous cipher output independently of the ciphertext or plaintext (O i ​ =E K ​ (O i−1
</details>

---

### 29. A block cipher differs from a stream cipher primarily in that it:
- A. Always runs faster than a stream cipher on the same hardware
- B. Encrypts a fixed-size group of plaintext bits at once, rather than one bit or byte at a time
- C. Uses a longer key than any stream cipher can support
- D. Cannot be combined with a chaining or feedback mechanism

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Encrypts a fixed-size group of plaintext bits at once, rather than one bit or byte at a time**

*Intuition:* A block cipher (e.g., AES, DES) processes plaintext in fixed-size chunks (blocks), typically 64 or 128 bits. A stream cipher (e.g., RC4, ChaCha20) encrypts data one bit or byte at a time, generating a keystream that is XORed with the plaintext. The other options are incorrect because: A: Block ciphers are not always faster; stream ciphers are often faster in software. C: Block ciphers do not inherently use longer keys; both types can support various key lengths. D: Block ciphers are commonly combined with chaining modes (e.g., CBC, CTR, GCM) to handle messages longer than a single block.
</details>

---

### 30. The block cipher mode in which each plaintext block is encrypted independently with the same key, and which reveals repeated patterns in the plaintext, is called ____ mode.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **ECB (Electronic Codebook) mode**

*Intuition:* The correct answer is **ECB (Electronic Codebook) mode**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 31. The block cipher mode that turns a block cipher into a stream cipher by encrypting a counter value for each block and XORing it with the plaintext is called ____ mode.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **CTR (or Counter) mode**

*Intuition:* In CTR (Counter) mode, a block cipher is turned into a stream cipher by encrypting a sequence of counter values (which are incremented for each block) and then XORing the resulting keystream with the plaintext to produce the ciphertext. Key features of CTR mode: Parallelizable (both encryption and decryption can be done in parallel). Random access (any block can be decrypted independently). Requires a unique nonce/initial counter value to prevent keystream reuse. This mode is widely used in practice (e.g., in TLS, IPsec, and disk encryption).
</details>

---

### 32. The block cipher mode that XORs each plaintext block with the previous ciphertext block before encryption, requiring an initialization vector for the first block, is called ____ mode.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Cipher-Block-Chaining (or CBC)**

*Intuition:* The correct answer is **Cipher-Block-Chaining (or CBC)**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 33. The Blum Blum Shub (BBS) generator produces each output bit by:
- A. Computing the discrete logarithm of the previous output modulo a large prime
- B. XORing the previous two output bits together, similar to a shift register
- C. Directly encrypting a counter value using AES in CTR mode
- D. Repeatedly squaring a value modulo n = p*q and taking the least significant bit of the result each round

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Repeatedly squaring a value modulo n = p*q and taking the least significant bit of the result each round**

*Intuition:* The Blum Blum Shub (BBS) generator operates as follows: Choose two large primes p p and q q, both congruent to 3 mod 4 (Blum integers), and set n = p ⋅ q n=p⋅q. Choose a seed X 0 X 0 ​ that is coprime to n n. Generate the sequence iteratively: X i + 1 = X i 2 mod n X i+1 ​ =X i 2 ​ modn At each iteration, output the least significant bit (or up to O ( log ⁡ log ⁡ n ) O(loglogn) bits) of X i + 1 X i+1 ​ . The security of BBS is provably reducible to the difficulty of factoring n n (specifically, the quadratic residuosity problem), making it a cryptographically strong PRNG—though relatively slow compared to other generators. The other options are incorrect: A: BBS uses modular squaring, not discrete logarithms. B: XORing previous outputs is characteristic of linear-feedback shift registers (LFSRs), not BBS. C: AES-CTR is a different kind of PRNG (symmetric-cipher-based), not BBS.
</details>

---

### 34. The Chinese Remainder Theorem allows a number to be uniquely reconstructed within a given range from:
- A. Its binary representation alone, without reference to any modulus
- B. A single large modulus formed by adding all the smaller moduli together
- C. Its remainders with respect to a set of moduli that share no common factors with one another
- D. Its prime factorization expressed in base two

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Its remainders with respect to a set of moduli that share no common factors with one another**

*Intuition:* The Chinese Remainder Theorem (CRT) states that if you have a set of moduli that are pairwise coprime (i.e., share no common factors with one another), then a number can be uniquely reconstructed modulo the product of those moduli from its remainders upon division by each modulus.
</details>

---

### 35. Choosing a very small public exponent such as e = 3 without message padding creates a risk known as:
- A. A doubling of the ciphertext length compared to using a larger exponent
- B. An immediate leak of the private exponent d to any observer of the ciphertext
- C. A complete loss of the ability to decrypt the message even with the correct key
- D. A cube-root attack, where the same message sent to multiple recipients can be recovered without factoring n

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A cube-root attack, where the same message sent to multiple recipients can be recovered without factoring n**

*Intuition:* Explanation: When e=3 and no padding is used, two common low-exponent vulnerabilities arise: Håstad's Broadcast Attack: If the same message M is sent to 3 different recipients with e=3, an attacker can combine the 3 ciphertexts using the Chinese Remainder Theorem to obtain M 3 (modn 1 ​ n 2
</details>

---

### 36. In Cipher Block Chaining (CBC) mode, the input to the encryption function for a given block is:
- A. The XOR of the current plaintext block with the next plaintext block
- B. The previous plaintext block encrypted a second time
- C. The XOR of the current plaintext block with the previous ciphertext block (or the IV, for the first block)
- D. The plaintext block alone, exactly as in ECB mode

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The XOR of the current plaintext block with the previous ciphertext block (or the IV, for the first block)**

*Intuition:* Explanation: In CBC (Cipher Block Chaining) mode, each plaintext block P i ​ is chained with the previous ciphertext block before encryption: For block i=1: Input 1 ​ =P
</details>

---

### 37. The classic, simple algorithm defined by the recurrence Xn+1 = (aXn + c) mod m is called a ____ generator.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **a linear congruential generator (or LCG)**

*Intuition:* The recurrence X n + 1 = ( a X n + c ) m o d m X n+1 ​ =(aX n ​ +c)modm defines the classic Linear Congruential Generator (LCG), which is one of the oldest and simplest pseudorandom number generator algorithms. It was introduced by D. H. Lehmer in 1949. The parameters are: m m — the modulus (defines the range of output values and the period), a a — the multiplier, c c — the increment, X 0 X 0 ​ — the seed (starting value). While LCGs are fast and easy to implement, they are not cryptographically secure because their linear structure makes them predictable given a few consecutive outputs.
</details>

---

### 38. Claude Shannon's principle by which each plaintext digit affects many digits of the ciphertext, hiding statistical structure, is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **diffusion**

*Intuition:* Claude Shannon introduced two fundamental principles for secure ciphers in his 1949 paper "Communication Theory of Secrecy Systems": Diffusion: This principle aims to spread the statistical structure of the plaintext throughout the ciphertext so that each plaintext digit affects many digits of the ciphertext. This makes it difficult for an attacker to use statistical patterns in the plaintext to deduce the key or the plaintext itself. In modern block ciphers, diffusion is typically achieved through permutations (e.g., ShiftRows and MixColumns in AES, or the permutation (P) box in DES). Confusion: This principle aims to make the relationship between the ciphertext and the encryption key as complex as possible, typically achieved through substitution (e.g., S-boxes).
</details>

---

### 39. Claude Shannon's principle by which the relationship between the ciphertext and the encryption key is made as complex as possible is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **confusion**

*Intuition:* Claude Shannon introduced two fundamental principles for secure ciphers in his 1949 paper "Communication Theory of Secrecy Systems": Confusion: The encryption key's relationship to the ciphertext is made as complex and involved as possible, making it difficult to determine the key from the ciphertext. This is typically achieved through substitution (non-linear S-boxes) in modern ciphers. Diffusion: The statistical structure of the plaintext is spread out and dissipated throughout the ciphertext, so that small changes in the plaintext produce large changes in the ciphertext. This is typically achieved through permutations (e.g., ShiftRows and MixColumns in AES). Together, confusion and diffusion are the twin pillars of secure block cipher design.
</details>

---

### 40. To combine both secrecy and authentication for a message X sent from A to B, the correct construction is:
- A. Z = E(PUa, E(PUb, X)) -- encrypt twice using both parties' public keys only
- B. Z = E(PUb, X) alone, since encrypting with B's public key already signs the message
- C. Z = E(PUb, E(PRa, X)) -- sign with A's private key, then encrypt the result with B's public key
- D. Z = E(PRa, E(PRb, X)) -- encrypt twice using both parties' private keys only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Z = E(PUb, E(PRa, X)) -- sign with A's private key, then encrypt the result with B's public key**

*Intuition:* To achieve both secrecy and authentication for a message sent from A to B: Authentication (digital signature): A encrypts (or signs) the message with A's own private key (PRa). This ensures that only A could have created it, providing non-repudiation. Secrecy (confidentiality): A then encrypts the signed message with B's public key (PUb). This ensures that only B (who possesses the corresponding private key) can decrypt and read it. The order is important: sign first, then encrypt. This prevents various attacks (e.g., signature stripping) and ensures that the signature covers the original message, not the encrypted form.
</details>

---

### 41. A common misconception about public-key cryptography, according to the chapter, is the belief that it:
- A. Cannot be used for digital signatures, only for encrypting messages directly
- B. Requires exactly the same amount of computation as symmetric encryption for bulk data
- C. Makes symmetric encryption obsolete, when in fact its overhead confines it mainly to signatures and key management
- D. Was invented decades after RSA, rather than being the concept RSA itself is built on

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Makes symmetric encryption obsolete, when in fact its overhead confines it mainly to signatures and key management**

*Intuition:* Explanation: A well-known misconception in standard cryptography literature (such as William Stallings' Cryptography and Network Security) is that public-key encryption has rendered symmetric encryption obsolete. In reality, because public-key algorithms are computationally intensive and orders of magnitude slower than symmetric block/stream ciphers, they are primarily utilized for key distribution, key exchange, and digital signatures rather than bulk data encryption.
</details>

---

### 42. A common practical design pairs a TRNG with a PRNG by:
- A. Alternating output bits strictly one-for-one between the TRNG and the PRNG
- B. Using the PRNG to produce entropy that is then fed back into the TRNG's hardware
- C. Using the TRNG's physical entropy to seed the PRNG, combining true unpredictability with the PRNG's speed and reproducibility
- D. Running both generators completely independently and never combining their outputs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Using the TRNG's physical entropy to seed the PRNG, combining true unpredictability with the PRNG's speed and reproducibility**

*Intuition:* Explanation: True Random Number Generators (TRNGs) collect entropy from nondeterministic physical phenomena (e.g., thermal noise, radioactive decay, clock jitter), but they are relatively slow and resource-intensive. Pseudorandom Number Generators (PRNGs / CPRNGs) are fast and deterministic. A standard cryptographic architecture collects high-quality physical entropy from the TRNG to initialize and periodically re-seed the PRNG, achieving both high cryptographic security/unpredictability and high-throughput byte generation.
</details>

---

### 43. Computing g^x mod p for a large exponent x is considered computationally easy mainly because:
- A. Modular exponentiation avoids using multiplication entirely
- B. x is always chosen to be smaller than the base g in practical schemes
- C. The result is always small, regardless of how large x or p may be
- D. Repeated squaring allows the result to be computed in a number of steps proportional to the number of bits in x

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Repeated squaring allows the result to be computed in a number of steps proportional to the number of bits in x**

*Intuition:* Why D is correct: Algorithms like square-and-multiply compute g x (modp) in O(logx) multiplications by breaking the exponent down into its binary representation (bits). Why the others are incorrect: A is false because modular exponentiation heavily relies on multiplication combined with modulo operations. B is false because x is typically a very large secret exponent (e.g., 256 to 2048 bits), far larger than small generators like g=2. C is false because the result can be as large as p−1, which is huge in practical cryptographic systems (e.g., 2048-bit numbers). A timing attack against RSA, as described by Kocher, works by:
</details>

---

### 44. Concern about the DES S-boxes containing a deliberate weakness arose mainly because:
- A. IBM and the NSA never publicly disclosed the exact criteria used to design them
- B. They were replaced entirely in the final published version of the standard
- C. They were later shown to reduce the effective key length to under 40 bits
- D. Independent researchers had mathematically proven a fatal structural flaw in them

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. IBM and the NSA never publicly disclosed the exact criteria used to design them**

*Intuition:* When DES was first published in the 1970s, the design criteria for its S-boxes were classified and not publicly disclosed. This secrecy led to widespread suspicion and concern that the S-boxes might contain a hidden "trapdoor" or deliberate weakness that could allow the NSA (who participated in the design review) to break DES more easily than the public could, while still keeping the algorithm secure enough against commercial attackers. It was only years later that the design criteria were declassified and published, revealing that the S-boxes were specifically designed to resist differential cryptanalysis—a technique that was not publicly known at the time (it was discovered independently in the late 1980s by Biham and Shamir). Far from containing a deliberate weakness, the S-boxes were actually carefully crafted to be stronger against this attack. However, the initial lack of transparency fueled the controversy.
</details>

---

### 45. Continuing the same RSA example (n = 187, d = 23), decrypting the ciphertext C = 11 is computed as:
- A. M = 11^23 mod 160 = 88
- B. M = 88^23 mod 187 = 11
- C. M = 11^23 mod 187 = 88
- D. M = 11^7 mod 187 = 88

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. M = 11^23 mod 187 = 88**

*Intuition:* In RSA, decryption is performed by computing $M = C^d \pmod n$ d n $M = C^d \pmod n$dn. Given C = 11 C=11, d = 23 d=23, and n = 187 n=187: M = 11 23 m o d 187 = 88 M=11 23 mod187=88. (Option A uses the wrong modulus 160 160, which is ϕ ( n ) ϕ(n), not n n. Option B reverses the encryption operation. Option D uses an incorrect exponent.)
</details>

---

### 46. A cryptographic hash-like construction can be built from cipher block chaining by:
- A. XORing the plaintext with a random initialization vector and discarding the key
- B. Applying the Caesar cipher repeatedly until the output length matches the input
- C. Running RSA directly on the message digest instead of on the message
- D. Encrypting the message with a fixed key and using the final ciphertext block as the hash value

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Encrypting the message with a fixed key and using the final ciphertext block as the hash value**

*Intuition:* This describes the basic idea behind constructing a one-way hash function from a block cipher, such as the Davies-Meyer construction or the Matyas-Meyer-Oseas construction. In the simplest form (using CBC mode with a fixed key): The message is processed block by block using a block cipher (like DES or AES) in CBC mode with a fixed, publicly known key. The final ciphertext block (the last output of the CBC chain) serves as the hash value. Variations of this approach were used in early hash functions like MDC-2 (Modification Detection Code) and the Davies-Meyer construction (which underlies many modern hash functions like SHA-1 and SHA-2, though those use dedicated compression functions rather than directly using a block cipher). The resulting hash is a fixed-size digest that depends on the entire message, with the property that it is computationally infeasible to find two different messages producing the same final block.
</details>

---

### 47. For cryptographic use, elliptic curve arithmetic is restricted to a finite field mainly so that:
- A. The curve automatically becomes symmetric about the x-axis for every choice of a and b
- B. The resulting group of curve points has a finite, countable number of elements suitable for cryptographic computation
- C. Point addition can be replaced entirely by ordinary integer addition
- D. The curve equation no longer needs coefficients a and b at all

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. The resulting group of curve points has a finite, countable number of elements suitable for cryptographic computation**

*Intuition:* Why B is correct: Defined over the real numbers (R), an elliptic curve contains an infinite, continuous set of points, making exact computation and discrete trapdoor one-way functions impossible. Restricting the curve to a finite field (such as F p ​ or F 2 m ​ ) produces a finite, discrete algebraic group of points with a fixed size (governed by Hasse's Theorem). This enables the construction of the Elliptic Curve Discrete Logarithm Problem (ECDLP), which is computationally hard.
</details>

---

### 48. In cryptography, randomness and unpredictability are best distinguished as follows:
- A. They are simply two different names for the exact same property of a number sequence
- B. Randomness applies only to hardware generators, while unpredictability applies only to software algorithms
- C. Randomness refers to statistical uniformity and independence, while unpredictability means future values cannot be guessed even after observing many past values
- D. Unpredictability means the sequence never repeats, while randomness means it always repeats

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Randomness refers to statistical uniformity and independence, while unpredictability means future values cannot be guessed even after observing many past values**

*Intuition:* This distinction is important in cryptography: Randomness (or statistical randomness) is about the properties of a sequence itself—it should be uniformly distributed over the possible values, with no discernible patterns or correlations between elements (i.e., independence). Unpredictability is about the sequence from an attacker's perspective—even if the sequence passes all statistical tests for randomness, an adversary who has observed many past outputs should still be unable to predict the next output with any advantage over random guessing. A cryptographically secure pseudorandom number generator (CSPRNG) must satisfy both conditions: its output must appear statistically random, and it must be computationally infeasible to predict future outputs (or recover past outputs) from the observed stream.
</details>

---

### 49. CTR mode is particularly well suited to high-speed, multi-core systems because:
- A. It never needs to compute an initialization vector or nonce for any block
- B. It automatically detects and corrects any transmission errors in the ciphertext
- C. Blocks have no sequential dependency, so they can be encrypted and decrypted in parallel
- D. It uses a smaller effective key length, so less computation is required per block

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Blocks have no sequential dependency, so they can be encrypted and decrypted in parallel**

*Intuition:* CTR (Counter) mode is highly suitable for high-speed, multi-core systems because each block's encryption or decryption is independent of every other block. The keystream for each block is generated by encrypting a unique counter value (which can be precomputed), and then the plaintext (or ciphertext) is XORed with that keystream. Since there is no chaining between blocks, multiple blocks can be processed simultaneously across different CPU cores or hardware pipelines, greatly improving throughput. The other options are incorrect: A: CTR mode does require a unique nonce/initial counter value to prevent keystream reuse. B: CTR mode does not automatically detect or correct transmission errors; it provides confidentiality only (and no built-in integrity). D: CTR mode uses the same key length as the underlying block cipher; it does not use a smaller effective key length.
</details>

---

### 50. A defining advantage of the Feistel structure is that:
- A. No subkey schedule is required, since the same key is reused every round
- B. Decryption uses the identical algorithm as encryption, only with the subkeys applied in reverse order
- C. The round function F must itself be a reversible, invertible operation
- D. Encryption and decryption each require a completely separate algorithm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Decryption uses the identical algorithm as encryption, only with the subkeys applied in reverse order**

*Intuition:* Explanation: In a Feistel network (used in ciphers like DES and Blowfish), decryption is performed using the exact same structural hardware/software algorithm as encryption—the only difference is that the round subkeys are applied in reverse order (K n ​ ,K n−1 ​ ,…,K 1
</details>

---

### 51. DES processes plaintext through which overall sequence of steps?
- A. A single large substitution table applied directly to the full 64-bit block
- B. An initial permutation, sixteen Feistel rounds, a swap of the two halves, then the inverse initial permutation
- C. Byte substitution, row shifting, column mixing, and a round-key XOR, repeated ten times
- D. A key expansion, eight parallel Feistel rounds, then a single final substitution

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. An initial permutation, sixteen Feistel rounds, a swap of the two halves, then the inverse initial permutation**

*Intuition:* Why B is correct: Standard DES operates on a 64-bit plaintext block through: Initial Permutation (IP): Bit transposition before round processing. 16 Feistel Rounds: Iterative substitution, permutation, and key mixing on the two 32-bit halves. 32-bit Swap: The left and right halves are swapped after round 16 (pre-output swap). Inverse Initial Permutation (IP −1 ): The final transposition producing the 64-bit ciphertext. Why the others are incorrect:
</details>

---

### 52. The DES round function expands the 32-bit right half of the data to ____ bits before it is combined with the round subkey.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **48 bits**

*Intuition:* The Expansion Permutation ($E$ table) in the DES round function takes the 32-bit right half of the 64-bit data block ($R_{i-1}$) and expands it to **48 bits** by cyclically duplicating 16 outer bits. This allows the expanded data to be combined via bitwise XOR with the 48-bit round subkey $K_i$ before passing into the eight $6 \times 4$ S-boxes.
</details>

---

### 53. DES uses an initial permutation, ____ rounds of processing, and then the inverse of the initial permutation to produce the ciphertext.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **16 rounds**

*Intuition:* The correct answer is **16 rounds**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 54. A deterministic algorithm that takes a seed and produces a long sequence of numbers that statistically resemble true randomness is called a ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **a pseudorandom number generator (or PRNG)**

*Intuition:* A PRNG (Pseudorandom Number Generator) is a deterministic algorithm that takes a finite initial value (called a seed) and produces a long output sequence that appears statistically random—meaning it passes various statistical tests for uniformity, independence, and lack of patterns—but is entirely reproducible given the same seed. When the PRNG is designed to be cryptographically secure (i.e., unpredictable to an adversary), it is specifically called a CSPRNG (Cryptographically Secure Pseudorandom Number Generator). However, the basic general term for any deterministic algorithm producing statistically random-looking output is PRNG.
</details>

---

### 55. Diffie and Hellman's 1976 breakthrough addressed which two problems inherent in purely symmetric cryptography?
- A. The need for a trusted certificate authority and the cost of hardware acceleration
- B. Resistance to brute-force attacks and resistance to differential cryptanalysis
- C. Encryption speed and the size of the ciphertext produced for short messages
- D. Secure key distribution without a pre-shared secret, and the lack of a scheme equivalent to a handwritten digital signature

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Secure key distribution without a pre-shared secret, and the lack of a scheme equivalent to a handwritten digital signature**

*Intuition:* The correct choice is **D. Secure key distribution without a pre-shared secret, and the lack of a scheme equivalent to a handwritten digital signature**. This follows directly from the foundational principles and technical specifications detailed in William Stallings' *Cryptography and Network Security*.
</details>

---

### 56. In Diffie-Hellman, both public parameters q (a prime) and alpha (a primitive root of q) are:
- A. Derived mathematically from each party's private exponent after the exchange
- B. Generated fresh for every single message exchanged between the parties
- C. Kept secret and known only to the two communicating parties
- D. Known publicly to everyone, including any potential attacker

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Known publicly to everyone, including any potential attacker**

*Intuition:* Explanation: In the Diffie-Hellman protocol, the modulus q (a large prime number) and the generator α (a primitive root modulo q) are global, public domain parameters. They do not need to be kept secret and can be published openly or agreed upon in plaintext, as the protocol's security relies entirely on the secrecy of the private exponents (X A ​ and X B ​ ) and the hardness of the Discrete Logarithm Problem (DLP).
</details>

---

### 57. The Diffie-Hellman key exchange allows two parties to establish a shared secret key by:
- A. Directly transmitting the shared secret key encrypted under RSA
- B. Meeting in person beforehand to physically exchange the key on paper
- C. Using a trusted third party to generate and distribute the key to both sides
- D. Exchanging public values computed from private exponents over an insecure channel, without ever transmitting the secret key itself

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Exchanging public values computed from private exponents over an insecure channel, without ever transmitting the secret key itself**

*Intuition:* The Diffie-Hellman key exchange allows two parties (Alice and Bob) to agree on a shared secret key over an insecure communication channel without having to exchange the actual secret key. The process works as follows: They agree publicly on a large prime p p and a primitive root g g modulo p p. Alice chooses a private exponent a a, computes A = g a m o d p A=g a modp, and sends A A to Bob. Bob chooses a private exponent b b, computes B = g b m o d p B=g b modp, and sends B B to Alice. Alice computes K = B a m o d p = g a b m o d p K=B a modp=g ab modp. Bob computes K = A b m o d p = g a b m o d p K=A b modp=g ab modp. They now both share the same secret key K K, while an eavesdropper who sees only p , g , A , p,g,A, and B B cannot feasibly compute K K due to the computational difficulty of the discrete logarithm problem. The shared secret key is never transmitted over the channel.
</details>

---

### 58. The Diffie-Hellman protocol requires two public parameters known to everyone: a prime q and a ____ root of q.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **primitive (or primitive root)**

*Intuition:* The Diffie-Hellman protocol requires two public parameters: A large prime q q, and A primitive root α α (also called a generator) of q q. A primitive root α α modulo q q is an integer whose powers α 1 , α 2 , α 3 , … , α q − 1 m o d q α 1 ,α 2 ,α 3 ,…,α q−1 modq generate all nonzero elements of the multiplicative group Z q ∗ Z q ∗ ​ . This property ensures that the discrete logarithm problem is hard and that the key exchange can produce a uniform distribution of values.
</details>

---

### 59. The discrete logarithm problem asks, given a base g, a prime p, and a value b, to find x such that:
- A. x^g is congruent to b modulo p
- B. g + x is congruent to b modulo p
- C. x is congruent to gcd(g, b) modulo p
- D. g^x is congruent to b modulo p

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. g^x is congruent to b modulo p**

*Intuition:* The discrete logarithm problem is defined as follows: Given: A prime p p, A primitive root (or generator) g g modulo p p, A value b b in the multiplicative group Z p ∗ Z p ∗ ​ , find the integer x x (the discrete logarithm) such that: g x ≡ b ( m o d p ) g x ≡b(modp) In other words, x x is the exponent to which the base g g must be raised (modulo p p) to obtain the value b b. The problem is considered computationally hard for large primes, which forms the security basis for the Diffie-Hellman key exchange, ElGamal encryption, and digital signature algorithms like DSA. The other options are incorrect: A: x g ≡ b ( m o d p ) x g ≡b(modp) would be a different (and generally easier) problem. B: g + x ≡ b ( m o d p ) g+x≡b(modp) is a simple linear congruence, easily solved. C: x ≡ gcd ⁡ ( g , b ) ( m o d p ) x≡gcd(g,b)(modp) is not a meaningful formulation of the problem.
</details>

---

### 60. Double DES (encrypting twice with two different 56-bit keys) is considered insufficient mainly because it is vulnerable to:
- A. A chosen-plaintext attack that recovers the key from a single ciphertext block
- B. A simple brute-force search that is no harder than breaking single DES
- C. A meet-in-the-middle attack, which reduces its effective strength far below a true 112-bit key
- D. An attack that only works if ECB mode is used alongside it

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A meet-in-the-middle attack, which reduces its effective strength far below a true 112-bit key**

*Intuition:* Explanation: In Double DES, C=E K 2 ​ ​ (E K 1
</details>

---

### 61. The efficient method that finds the greatest common divisor of two integers through repeated division is called the ____ Algorithm.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Euclidean**

*Intuition:* The correct answer is **Euclidean**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 62. In Electronic Codebook (ECB) mode, each plaintext block is:
- A. XORed with the previous ciphertext block before being encrypted
- B. Split into two halves and processed through a Feistel-like structure
- C. Encrypted independently with the same key, with no chaining or feedback between blocks
- D. Combined with a running counter before being encrypted

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Encrypted independently with the same key, with no chaining or feedback between blocks**

*Intuition:* In Electronic Codebook (ECB) mode, each plaintext block is encrypted separately using the same key, and there is no chaining or feedback between blocks. This means that identical plaintext blocks will always encrypt to identical ciphertext blocks, which can reveal patterns in the data. This is why ECB is generally not recommended for encrypting data with repetitive patterns (e.g., images), as the structure of the plaintext may still be visible in the ciphertext. The other options are incorrect: A: This describes CBC (Cipher Block Chaining) mode, where each plaintext block is XORed with the previous ciphertext block before encryption. B: This describes a Feistel structure, not ECB mode. D: This describes CTR (Counter) mode, where a counter value is combined with the plaintext.
</details>

---

### 63. An element a is called a primitive root of a prime p when:
- A. a raised to any power always produces the same remainder modulo p
- B. The successive powers of a, taken modulo p, cycle through every nonzero remainder before repeating
- C. a is the smallest prime factor of p minus one
- D. a itself must also be prime and strictly greater than p

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. The successive powers of a, taken modulo p, cycle through every nonzero remainder before repeating**

*Intuition:* Explanation: An element a is a primitive root modulo a prime p if its powers a 1 ,a 2 ,…,a p−1 (modp) generate all integers in the set {1,2,…,p−1} exactly once before repeating (i.e., a is a generator of the multiplicative group Z p
</details>

---

### 64. The ElGamal cryptosystem, published in 1984, is most accurately described as:
- A. An improved factoring algorithm used to attack RSA moduli directly
- B. A hash-based signature scheme that does not rely on any modular exponentiation
- C. A public-key encryption scheme closely related to Diffie-Hellman, resting on the same discrete-logarithm hardness assumption
- D. A symmetric block cipher unrelated to any discrete-logarithm-based scheme

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A public-key encryption scheme closely related to Diffie-Hellman, resting on the same discrete-logarithm hardness assumption**

*Intuition:* The ElGamal cryptosystem is indeed a public-key encryption scheme that relies on the computational difficulty of the discrete logarithm problem in a finite cyclic group. It is a direct extension of the Diffie-Hellman key exchange protocol, using the same underlying mathematical principles.
</details>

---

### 65. In ElGamal encryption, the sender picks a random value k for each message mainly because:
- A. A fixed, reused k actually improves security by simplifying the ciphertext
- B. k determines the size of the recipient's public key, so it must vary each time
- C. k must equal the recipient's private key for decryption to succeed at all
- D. Reusing the same k across two messages lets an attacker who knows one plaintext recover the other

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Reusing the same k across two messages lets an attacker who knows one plaintext recover the other**

*Intuition:* In ElGamal encryption, the randomness k k is crucial for semantic security. If the same k k is reused for two different messages, the ciphertexts share the same ephemeral key component ( g k g k and y k y k ), allowing an attacker who knows one plaintext to easily compute the other by XORing or dividing the ciphertexts. This is a well-known vulnerability, which is why a fresh random k k must be chosen for each encryption.
</details>

---

### 66. Elliptic curve cryptography is attractive compared to RSA mainly because, for a comparable level of security, ECC:
- A. Requires substantially smaller key sizes, reducing processing overhead
- B. Has a longer and more thoroughly tested track record than RSA
- C. Does not require the two communicating parties to agree on any shared curve parameters
- D. Eliminates the need for any private key on either side of the exchange

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Requires substantially smaller key sizes, reducing processing overhead**

*Intuition:* The correct choice is **A. Requires substantially smaller key sizes, reducing processing overhead**. This follows directly from the foundational principles and technical specifications detailed in William Stallings' *Cryptography and Network Security*.
</details>

---

### 67. For an elliptic curve defined over the real numbers as y^2 = x^3 + ax + b, adding two distinct points P and Q geometrically involves:
- A. Multiplying the x-coordinates of P and Q together to get the new x-coordinate
- B. Drawing the line through P and Q, finding its third intersection with the curve, and reflecting that point across the x-axis
- C. Reflecting P alone across the y-axis without ever considering Q's position
- D. Averaging the x-coordinates and y-coordinates of P and Q directly

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Drawing the line through P and Q, finding its third intersection with the curve, and reflecting that point across the x-axis**

*Intuition:* This is the geometric definition of point addition on an elliptic curve (in Weierstrass form y 2 = x 3 + a x + b y 2 =x 3 +ax+b): Draw the line through the two distinct points P P and Q Q. This line will intersect the elliptic curve at exactly one additional point (by Bézout's theorem, counting multiplicities). Reflect that third intersection point across the x-axis (i.e., negate its y-coordinate). The reflected point is P + Q P+Q. If P = Q P=Q (point doubling), the line is replaced by the tangent line at P P, and the same process applies. The other options are incorrect: A: Multiplying x-coordinates is not how elliptic curve addition works. C: Only reflecting P P is not the correct operation. D: Averaging coordinates is not geometrically meaningful for elliptic curves.
</details>

---

### 68. The elliptic curve discrete logarithm problem, the hard problem underlying ECC security, asks an attacker to:
- A. Recover the integer k given a base point P and the point kP obtained by repeated point addition
- B. Factor the coefficients a and b that define the elliptic curve equation
- C. Compute the y-coordinate of a point given only its x-coordinate, without a curve equation
- D. Find two distinct points on the curve that sum to the point at infinity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Recover the integer k given a base point P and the point kP obtained by repeated point addition**

*Intuition:* Explanation: The Elliptic Curve Discrete Logarithm Problem (ECDLP) is defined as: given a base point P on an elliptic curve over a finite field and a scalar multiple Q=kP (computed via repeated elliptic curve point additions), find the integer scalar k. Computing Q from k and P (scalar multiplication) is computationally easy, but recovering k given P and Q is computationally infeasible for appropriately chosen cryptographically secure curves.
</details>

---

### 69. Euler's Theorem, a^$\$\phi(n)$ is congruent to 1 (mod n) provided that gcd(a, n) = 1, is best described as:
- A. An unrelated result used exclusively for testing whether n is a perfect square
- B. A generalization of Fermat's Little Theorem that applies to any modulus n, not only prime moduli
- C. A restatement of the Euclidean Algorithm using exponents instead of remainders
- D. A special case of Fermat's Little Theorem that only applies when n itself is prime

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A generalization of Fermat's Little Theorem that applies to any modulus n, not only prime moduli**

*Intuition:* Euler's Theorem states that for any integer n > 1 n>1 and any integer a a such that gcd ⁡ ( a , n ) = 1 gcd(a,n)=1: a ϕ ( n ) ≡ 1 ( m o d n ) a ϕ(n) ≡1(modn) where ϕ ( n ) ϕ(n) is Euler's totient function (the number of positive integers less than n n that are coprime to n n). This is a direct generalization of Fermat's Little Theorem, which is the special case where n n is prime. When n = p n=p (prime), ϕ ( p ) = p − 1 ϕ(p)=p−1, and Euler's Theorem reduces to: a p − 1 ≡ 1 ( m o d p ) a p−1 ≡1(modp) which is exactly Fermat's Little Theorem. The other options are incorrect: A: Euler's Theorem is foundational to RSA and many number-theoretic cryptographic schemes, not used for testing perfect squares. C: Euler's Theorem involves exponentiation, not the Euclidean Algorithm (which is about gcd computation). D: It's the reverse: Fermat's Little Theorem is a special case of Euler's Theorem, not the other way around.
</details>

---

### 70. In evaluating candidate round functions F for a block cipher, the strict avalanche criterion (SAC) specifically requires that:
- A. Each output bit should change with probability one-half whenever a single input bit is inverted
- B. The round function should use exactly the same number of rounds as the key length in bits
- C. Every output bit should be a linear combination of the input bits
- D. The ciphertext should always be exactly the same length as the plaintext

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Each output bit should change with probability one-half whenever a single input bit is inverted**

*Intuition:* The Strict Avalanche Criterion (SAC) is a property of boolean functions and cryptographic round functions. It requires that when a single input bit is complemented (inverted), each output bit should change with a probability of exactly 1/2 (or very close to it). This ensures that the function provides strong diffusion and that small changes in the input propagate unpredictably throughout the output—a key requirement for resisting differential and linear cryptanalysis. The other options are incorrect because: B: The number of rounds is not tied to the key length in bits; it's a design choice based on security margins. C: SAC explicitly requires non-linearity; output bits should not be linear combinations of input bits. D: This is a general property of block ciphers (fixed block size), not specifically SAC.
</details>

---

### 71. In an extension field $GF(2^m)$, each element can be represented as:
- A. A single decimal digit between 0 and m
- B. A polynomial of degree less than m with binary (0 or 1) coefficients, equivalent to an m-bit string
- C. An ordered pair of prime numbers whose product is less than 2^m
- D. A matrix of size m by m containing only prime entries

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A polynomial of degree less than m with binary (0 or 1) coefficients, equivalent to an m-bit string**

*Intuition:* In an extension field G F ( 2 m ) GF(2 m ), each element is represented as a polynomial of the form: a m − 1 x m − 1 + a m − 2 x m − 2 + ⋯ + a 1 x + a 0 a m−1 ​ x m−1 +a m−2 ​ x m−2 +⋯+a 1 ​ x+a 0 ​ where each coefficient a i ∈ { 0 , 1 } a i ​ ∈{0,1}. This polynomial has degree at most m − 1 m−1, and it is equivalent to an m m-bit binary string ( a m − 1 a m − 2 ⋯ a 1 a 0 ) (a m−1 ​ a m−2 ​ ⋯a 1 ​ a 0 ​ ). Addition is performed as bitwise XOR (coefficient-wise modulo 2), and multiplication is performed modulo a chosen irreducible polynomial of degree m m. This representation is fundamental to many cryptographic algorithms, including AES (which uses G F ( 2 8 ) GF(2 8 )). The other options are incorrect because: A: Elements are not single decimal digits; they are m m-bit vectors. C: Elements are not pairs of primes. D: Elements are not matrices of primes.
</details>

---

### 72. The fast, widely used probabilistic primality test that repeatedly tests random witnesses against a candidate number is called the ____ test.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Miller-Rabin (or formatted for fill-in: Miller-Rabin / Miller-Rabin-test)**

*Intuition:* The Miller–Rabin test is a fast, probabilistic primality test that works by selecting random bases (witnesses) and testing whether certain congruences hold for the candidate number n n. If the test says "composite," the number is definitely composite. If it says "probably prime," the probability of error can be made arbitrarily small by repeating the test with multiple independent random bases. It is widely used in cryptographic key generation (e.g., for RSA primes) because it is efficient and the error probability can be driven down to negligible levels (e.g., 2 − 80 2 −80 or less).
</details>

---

### 73. In a Feistel cipher, the relationship that generates the right half of round i is:
- A. Ri = F(Li-1, Ki) XOR Ri-1 XOR Li-1
- B. Ri = Li-1 XOR F(Ri-1, Ki)
- C. Ri = Li-1 AND F(Ri-1, Ki)
- D. Ri = F(Ri-1, Ki-1) XOR Li

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Ri = Li-1 XOR F(Ri-1, Ki)**

*Intuition:* In a Feistel cipher, the round transformation for round i i is defined as: L i = R i − 1 L i ​ =R i−1 ​ R i = L i − 1 ⊕ F ( R i − 1 , K i ) R i ​ =L i−1 ​ ⊕F(R i−1 ​ ,K i ​ ) where: L i − 1 L i−1 ​ and R i − 1 R i−1 ​ are the left and right halves from the previous round, K i K i ​ is the round subkey for round i i, F F is the round function (which typically includes substitution, permutation, and key mixing), ⊕ ⊕ denotes XOR. The left half of the next round is simply a copy of the previous right half, while the new right half is the previous left half XORed with the output of the round function applied to the previous right half and the round key. The other options are incorrect: A: Includes R i − 1 R i−1 ​ twice and also L i − 1 L i−1 ​ in the XOR, which is not the Feistel structure. C: Uses AND instead of XOR, which would not be invertible and is not how Feistel ciphers work. D: Incorrectly indexes K i − 1 K i−1 ​ and uses L i L i ​ (which is not yet defined) in the expression.
</details>

---

### 74. Feistel's design goal was to approximate the security of an ideal block cipher while avoiding its main practical drawback, which is that an ideal cipher with an n-bit block requires:
- A. A key large enough to select among 2^n! possible transformations, which is computationally unmanageable
- B. A separate physical key exchange for every message sent
- C. A trusted third party to certify the block size in advance
- D. Hardware capable of performing floating-point arithmetic

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. A key large enough to select among 2^n! possible transformations, which is computationally unmanageable**

*Intuition:* Explanation: An ideal (general reversible substitution) block cipher mapping an n-bit input to an n-bit output allows for (2 n )! possible reversible mappings (permutations). Specifying any arbitrary mapping requires a key length proportional to log 2 ​ ((2 n )!)≈n⋅2
</details>

---

### 75. Fermat's Little Theorem states that, for a prime p and an integer a not divisible by p:
- A. a^p is congruent to a modulo (p-1)
- B. a^(p-1) is congruent to 1 modulo p
- C. a^(p+1) is congruent to a modulo p
- D. p^(a-1) is congruent to 1 modulo a

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. a^(p-1) is congruent to 1 modulo p**

*Intuition:* Fermat's Little Theorem states that if p p is a prime number and a a is any integer not divisible by p p, then: a p − 1 ≡ 1 ( m o d p ) a p−1 ≡1(modp) An equivalent formulation (without the coprime condition) is: a p ≡ a ( m o d p ) a p ≡a(modp) for all integers a a. The other options are incorrect: A: Uses the wrong modulus ( p − 1 p−1 instead of p p). C: Uses p + 1 p+1 in the exponent, which is not the theorem. D: Reverses the roles of p p and a a, which is not correct.
</details>

---

### 76. The final round of AES encryption differs from the earlier rounds in that it:
- A. Omits the AddRoundKey transformation entirely
- B. Repeats SubBytes twice in succession
- C. Omits the MixColumns transformation
- D. Uses a different, smaller S-box than earlier rounds

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Omits the MixColumns transformation**

*Intuition:* The correct choice is **C. Omits the MixColumns transformation**. This follows directly from the foundational principles and technical specifications detailed in William Stallings' *Cryptography and Network Security*.
</details>

---

### 77. A finite field, or Galois field GF(q), is a finite set of elements with addition and multiplication such that:
- A. Every element, including zero, is required to have a multiplicative inverse
- B. Only addition is guaranteed to have inverses; multiplication need not be invertible
- C. The number of elements q must always be an even number
- D. Every nonzero element has a multiplicative inverse and the usual algebraic laws (associativity, commutativity, distributivity) hold

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Every nonzero element has a multiplicative inverse and the usual algebraic laws (associativity, commutativity, distributivity) hold**

*Intuition:* A finite field (Galois field) G F ( q ) GF(q) is a set with two operations (addition and multiplication) that satisfies: It forms an abelian group under addition (closure, associativity, identity 0, inverses for all elements, commutativity). The nonzero elements form an abelian group under multiplication (closure, associativity, identity 1, inverses for every nonzero element, commutativity). Multiplication distributes over addition. The other options are incorrect because: A: Zero does not have a multiplicative inverse; only the nonzero elements do. B: Multiplication must also be invertible for all nonzero elements; this is a defining property of a field. C: The number of elements q q in a finite field is always p m p m where p p is a prime and m ≥ 1 m≥1. This can be odd (e.g., G F ( 3 ) GF(3), G F ( 9 ) GF(9)) or even (e.g., G F ( 2 m ) GF(2 m )), so it is not required to be even.
</details>

---

### 78. A function that is easy to compute in one direction but infeasible to invert without secret extra information is called a ____ one-way function.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **a trapdoor one-way function (or trapdoor)**

*Intuition:* A trapdoor one-way function is a function that is: Easy to compute in the forward direction (given an input x x, computing f ( x ) f(x) is efficient). Infeasible to invert (given f ( x ) f(x), finding x x) without some additional secret information, known as the trapdoor. This is the foundational concept behind most public-key cryptosystems: In RSA, the function f ( x ) = x e mod n f(x)=x e modn is easy to compute, but inverting it (decryption) is hard unless you know the private exponent d d (the trapdoor) or the factorization of n n. In other schemes like Diffie-Hellman and ECC, the trapdoor concept is analogous (though the underlying one-way function is exponentiation or scalar multiplication). The term "trapdoor" distinguishes these functions from one-way functions (which have no secret trapdoor and are used in hash functions and symmetric crypto).
</details>

---

### 79. A generator that derives its randomness from a genuinely unpredictable physical process, such as thermal noise, rather than from a deterministic algorithm, is called a ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **a True Random Number Generator (or TRNG)**

*Intuition:* A TRNG (True Random Number Generator) derives its randomness from genuinely unpredictable physical processes, such as: Thermal noise (Johnson–Nyquist noise) in semiconductor junctions, Atmospheric noise, Radioactive decay, Quantum effects (e.g., photon arrival times), Other physical phenomena that are inherently non-deterministic. This contrasts with a Pseudo-Random Number Generator (PRNG) or Cryptographically Secure Pseudo-Random Number Generator (CSPRNG), which generate randomness deterministically from an initial seed value using an algorithm. TRNGs are typically used as the source of entropy to seed PRNGs in cryptographic systems.
</details>

---

### 80. $GF(2^8)$ arithmetic is directly used inside which widely deployed algorithm?
- A. The Euclidean Algorithm, when computing a greatest common divisor
- B. RSA, when selecting the two large prime factors of its modulus
- C. AES, in its byte substitution and column mixing steps
- D. The plain Caesar cipher, in choosing its shift amount

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. AES, in its byte substitution and column mixing steps**

*Intuition:* Explanation: The Advanced Encryption Standard (AES) operates on 8-bit bytes defined as elements in the Galois field GF(2 8 ). In particular, the SubBytes step uses multiplicative inverses in GF(2 8 ) to construct the S-box, and the MixColumns step performs matrix multiplication where polynomial arithmetic is carried out modulo an irreducible polynomial over GF(2 8 ).
</details>

---

### 81. In $GF(2^m)$, addition of two field elements is performed using the bitwise operation ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **XOR (or bitwise XOR / exclusive OR)**

*Intuition:* In G F ( 2 m ) GF(2 m ), field elements are represented as binary polynomials (or bit vectors of length m m). Addition of two elements is performed by adding the corresponding coefficients modulo 2, which is equivalent to a bitwise XOR operation. There is no carry propagation, making it a simple and fast operation in hardware and software.
</details>

---

### 82. If plaintext bit P = 1 is XORed with keystream bit K = 0, and the resulting ciphertext bit C is later XORed again with the same keystream bit K, the result is:
- A. 0, because two XOR operations always cancel out to zero
- B. 1, recovering the original plaintext bit exactly
- C. Undefined, since XOR cannot be reversed without also knowing P in advance
- D. 1, but only if K had instead been equal to 1

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 1, recovering the original plaintext bit exactly**

*Intuition:* Calculation: Encryption: C=P⊕K=1⊕0=1 Decryption: C⊕K=1⊕0=1 Because XOR is its own inverse (P⊕K⊕K=P⊕0=P), XORing twice with the same keystream bit restores the original plaintext bit (1).
</details>

---

### 83. Increasing the block size of a Feistel cipher generally:
- A. Improves security through greater diffusion, at the cost of more processing time per block
- B. Has no measurable effect on either security or processing time
- C. Removes the need for multiple rounds of processing
- D. Weakens security because larger blocks leak more statistical structure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Improves security through greater diffusion, at the cost of more processing time per block**

*Intuition:* Explanation: In block cipher design (including Feistel ciphers): Larger block sizes (e.g., 128 bits vs. 64 bits) make statistical cryptanalysis, dictionary attacks, and birthday attacks (such as collision attacks in modes like CBC) significantly harder because the space of possible blocks grows exponentially (2 n ). It also enhances diffusion across the block. Trade-off: Larger blocks require more memory, larger intermediate registers, and more computational operations/cycles per block, leading to higher complexity and processing time per block.
</details>

---

### 84. Inside a DES round, the 32-bit right half is expanded to 48 bits mainly so that it can be:
- A. Directly output as the new left half without further processing
- B. Combined via XOR with the 48-bit round subkey before passing through the S-boxes
- C. Compared bit-by-bit against the original plaintext for error checking
- D. Split evenly between the eight S-boxes without any subkey involved

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Combined via XOR with the 48-bit round subkey before passing through the S-boxes**

*Intuition:* Explanation: In the DES round function F(R i−1 ​ ,K i ​ ), the Expansion Permutation (E-box) expands the 32-bit right half into 48 bits so its dimension matches the 48-bit round subkey (K i
</details>

---

### 85. An integer in Z8 fails to have a multiplicative inverse modulo 8 precisely when it:
- A. Shares a common factor greater than 1 with 8
- B. Is an odd number less than 8
- C. Is larger than half of 8
- D. Is itself equal to zero or to one

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Shares a common factor greater than 1 with 8**

*Intuition:* In modular arithmetic, an integer a a has a multiplicative inverse modulo m m if and only if gcd ⁡ ( a , m ) = 1 gcd(a,m)=1 (i.e., a a and m m are coprime). For m = 8 m=8, the integers in Z 8 = { 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 } Z 8 ​ ={0,1,2,3,4,5,6,7} that are coprime to 8 (i.e., gcd ⁡ ( a , 8 ) = 1 gcd(a,8)=1) are: 1 1 (gcd(1,8)=1) → has inverse 3 3 (gcd(3,8)=1) → has inverse 5 5 (gcd(5,8)=1) → has inverse 7 7 (gcd(7,8)=1) → has inverse The integers that fail to have an inverse are those that share a common factor with 8: 0 0 (gcd(0,8)=8) 2 2 (gcd(2,8)=2) 4 4 (gcd(4,8)=4) 6 6 (gcd(6,8)=2) Thus, the condition is precisely that the integer shares a common factor > 1 with 8. The other options are incorrect: B: Odd numbers like 1, 3, 5, 7 do have inverses modulo 8. C: Being larger than half of 8 is irrelevant (e.g., 5 and 7 are larger than 4 but have inverses; 6 is larger but does not). D: Zero has no inverse; one does have an inverse (itself), so this is not a unified condition.
</details>

---

### 86. An integer p greater than 1 is defined as prime when:
- A. It cannot be expressed as the product of any two smaller integers at all
- B. Its only positive divisors are 1 and itself
- C. It has exactly three distinct positive divisors, including itself
- D. It is odd and also not divisible by 3 or 5

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Its only positive divisors are 1 and itself**

*Intuition:* This is the standard definition of a prime number: an integer greater than 1 that has no positive divisors other than 1 and itself. The other options are incorrect because: A: This is too strict—a prime cannot be expressed as the product of two smaller positive integers greater than 1, but it can be expressed as 1 × p 1×p (which are two smaller integers if you count 1, but 1 is not considered a proper factor in the definition). C: A prime has exactly two distinct positive divisors (1 and itself), not three. (A number with exactly three divisors would be a square of a prime, e.g., 9 has divisors 1, 3, 9.) D: This describes numbers coprime to 30, not primes (e.g., 25 is odd and not divisible by 3 or 5, but 25 is composite).
</details>

---

### 87. The Intel Digital Random Number Generator (DRNG), used in Intel processors since 2012, combines which stages in its pipeline?
- A. A thermal-noise entropy source, a bias-removing conditioner, and a CTR_DRBG stage exposed through the RDRAND instruction
- B. A user-supplied password hashed once with SHA-1 and output directly
- C. Two independent TRNGs whose raw, unconditioned outputs are simply concatenated
- D. An LCG seeded from the system clock, followed directly by RC4 encryption

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. A thermal-noise entropy source, a bias-removing conditioner, and a CTR_DRBG stage exposed through the RDRAND instruction**

*Intuition:* Explanation: Intel's on-chip hardware DRNG architecture consists of three main hardware components: Entropy Source (ES): A high-speed True Random Number Generator (TRNG) based on thermal noise inside a dual-inverter metastable latch circuit. Conditioner: Uses AES-CBC-MAC / hardware hashing to debias and distill the raw physical entropy. Deterministic Random Bit Generator (DRBG): An SP 800-90A compliant CTR_DRBG (using AES-128 in CTR mode) that cryptographically expands the entropy and serves random data directly to instructions like RDRAND (and RDSEED).
</details>

---

### 88. A key limitation of CBC mode compared to CTR mode is that CBC encryption:
- A. Cannot use an initialization vector, unlike every other mode
- B. Reveals identical plaintext blocks as identical ciphertext blocks, just like ECB
- C. Requires a completely different block cipher algorithm for each block
- D. Cannot be parallelized, because each block depends on the ciphertext of the block before it

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Cannot be parallelized, because each block depends on the ciphertext of the block before it**

*Intuition:* In CBC (Cipher Block Chaining) mode, encryption of each plaintext block depends on the ciphertext of the previous block (via XOR before encryption). This creates a sequential dependency, meaning you cannot encrypt multiple blocks in parallel—block i i cannot be processed until block i − 1 i−1 has been fully encrypted. In contrast, CTR (Counter) mode encrypts each block independently by XORing the plaintext with a counter value that is encrypted using the block cipher. Since the counter values can be precomputed and processed in parallel, CTR mode supports parallel encryption (and decryption) of all blocks, making it more efficient on multi-core systems. The other options are incorrect because: A: CBC does use an initialization vector (IV). B: Unlike ECB, CBC with a randomized IV ensures that identical plaintext blocks encrypt to different ciphertext blocks. C: CBC uses the same block cipher algorithm for all blocks, just with chaining.
</details>

---

### 89. The main security weakness of ECB mode is that:
- A. Identical plaintext blocks always produce identical ciphertext blocks, revealing patterns in the underlying data
- B. It cannot be used with block ciphers larger than 64 bits
- C. It exposes the entire secret key after only two blocks are encrypted
- D. It requires a new key to be generated for every single block encrypted

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Identical plaintext blocks always produce identical ciphertext blocks, revealing patterns in the underlying data**

*Intuition:* This is the main security weakness of Electronic Codebook (ECB) mode. Because each plaintext block is encrypted independently with the same key, identical plaintext blocks will always encrypt to identical ciphertext blocks. This deterministic property means that patterns and repetitions in the plaintext data (such as in images, formatted documents, or structured data) remain visible in the ciphertext. An attacker can analyze the ciphertext for repeated blocks and potentially deduce information about the plaintext structure, which is why ECB is generally discouraged for encrypting data with predictable patterns. The other options are incorrect: B: ECB can be used with any block cipher size (64, 128, etc.), though it's not secure. C: ECB does not expose the encryption key; the key remains secure under the block cipher's security. D: ECB uses the same key for all blocks, not a new key per block.
</details>

---

### 90. A message encrypted only with the sender's private key, as in a basic digital signature scheme, provides authentication but NOT confidentiality because:
- A. Digital signatures are only ever applied to a hash of the message, never its content
- B. Anyone who has the sender's public key can decrypt and read the message
- C. The message is never actually transformed, only tagged with a plaintext label
- D. The private key used is always shorter than the key used for encryption alone

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Anyone who has the sender's public key can decrypt and read the message**

*Intuition:* Explanation: In asymmetric cryptography, anyone can access the sender's public key to decrypt and verify the message. Since anyone can decrypt it, confidentiality is lost, but authentication and non-repudiation are preserved because only the sender possessing the corresponding private key could have encrypted it.
</details>

---

### 91. In the Micali-Schnorr RSA-based PRNG, each stage encrypts the current internal state and then splits the result so that:
- A. Some bits feed back to seed the next stage while the remaining bits form part of the pseudorandom output
- B. All of the output bits are discarded and only the feedback bits are ever kept
- C. Half of the RSA modulus n is regenerated fresh at every single stage
- D. The entire output becomes the feedback value for the next stage, with nothing output

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Some bits feed back to seed the next stage while the remaining bits form part of the pseudorandom output**

*Intuition:* Explanation: In each iteration of the Micali-Schnorr PRNG: The current state x i ​ is mapped via the RSA one-way function: y=x i e ​
</details>

---

### 92. MixColumns provides diffusion by:
- A. XORing every column with the same fixed round key value
- B. Swapping entire columns of the State with one another
- C. Reversing the byte order within each row of the State
- D. Treating each column as a polynomial over GF(2^8) and multiplying it by a fixed matrix, so every output byte depends on all four input bytes of that column

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Treating each column as a polynomial over GF(2^8) and multiplying it by a fixed matrix, so every output byte depends on all four input bytes of that column**

*Intuition:* The MixColumns transformation in AES provides diffusion by operating independently on each column of the State. Each column is treated as a 4-term polynomial over G F ( 2 8 ) GF(2 8 ) and is multiplied modulo x 4 + 1 x 4 +1 by a fixed polynomial a ( x ) = { 03 } x 3 + { 01 } x 2 + { 01 } x + { 02 } a(x)={03}x 3 +{01}x 2 +{01}x+{02}, which is equivalent to multiplying the column by a fixed 4 × 4 4×4 matrix over G F ( 2 8 ) GF(2 8 ). The result is that every output byte in a column is a linear combination of all four input bytes of that column, spreading the influence of each plaintext byte throughout the column. This is a key source of diffusion in AES, complementing the ShiftRows transformation which diffuses bytes across columns. The other options are incorrect: A: XORing with a round key is AddRoundKey, not MixColumns. B: Swapping columns is not part of MixColumns (ShiftRows swaps rows, not columns). C: Reversing byte order within rows is not part of AES.
</details>

---

### 93. A mode of operation is best defined as:
- A. A set of rules describing how a block cipher should be applied to encrypt data longer than a single block
- B. An alternative block cipher algorithm used only for very large files
- C. A method for generating the encryption key from a user-supplied password
- D. A hardware-only technique that cannot be implemented in software

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. A set of rules describing how a block cipher should be applied to encrypt data longer than a single block**

*Intuition:* A mode of operation (e.g., ECB, CBC, CTR, GCM) defines how to securely encrypt messages that are longer than the block size of the underlying block cipher. It specifies how to handle multiple blocks, incorporate initialization vectors (IVs), and provide properties like confidentiality, and in some cases, authentication.
</details>

---

### 94. Which mode of operation is generally considered to have no safe use case for general-purpose encryption of typical application data?
- A. CTR
- B. ECB
- C. CBC
- D. OFB

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. ECB**

*Intuition:* Explanation: ECB encrypts identical plaintext blocks into identical ciphertext blocks under the same key. Because it preserves structural data patterns and leaks statistical information (as famously illustrated by the ECB Penguin), it does not provide semantic security and is unsafe for general application data.
</details>

---

### 95. A mode of operation that allows random access to any individual block without first decrypting all preceding blocks is best exemplified by:
- A. ECB mode used together with an initialization vector
- B. CTR mode, since each block's keystream depends only on its own counter value
- C. CFB mode, since it processes data in variable-size segments
- D. CBC mode, since each block depends on the ciphertext immediately before it

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. CTR mode, since each block's keystream depends only on its own counter value**

*Intuition:* Counter (CTR) mode allows random access to any individual block without needing to decrypt all preceding blocks. This is because each block's encryption is independent — the keystream for each block is generated by encrypting a unique counter value associated with that specific block. Therefore, you can decrypt any block directly by computing the counter for that position, encrypting it, and XORing it with the ciphertext block. The other options do not support random access: A: ECB mode does support independent block access (no chaining), but it does not use an IV and has serious security weaknesses due to identical plaintext blocks producing identical ciphertext blocks. It is not typically considered a secure mode for general use. C: CFB (Cipher Feedback) mode has sequential dependency like CBC; each block depends on the previous ciphertext, so random access is not possible. D: CBC mode has a sequential dependency (each block depends on the previous ciphertext), so you must decrypt all previous blocks to decrypt a specific one (with the exception of the first block, which uses the IV).
</details>

---

### 96. Multiplication in $GF(2^m)$ is performed by:
- A. Multiplying the polynomials and then reducing the result modulo a fixed irreducible polynomial
- B. Simply XORing the two operands together, exactly as in addition
- C. Looking up the product directly in a table of prime factorizations
- D. Adding the two polynomials and discarding any bits beyond position m

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Multiplying the polynomials and then reducing the result modulo a fixed irreducible polynomial**

*Intuition:* Explanation: In the Galois field GF(2 m ), elements are represented as polynomials of degree less than m with coefficients in GF(2) (where addition is XOR and multiplication is AND). Multiplication of two elements is carried out by performing standard polynomial multiplication followed by polynomial division to find the remainder modulo an irreducible polynomial m(x) of degree m.
</details>

---

### 97. A network structure built from alternating layers of substitution and permutation across multiple rounds, as proposed by Shannon and used in ciphers such as DES, is called a substitution-____ network.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **permutation (or substitution-permutation network)**

*Intuition:* The full term is substitution-permutation network (SPN), which is the structure proposed by Claude Shannon that alternates layers of substitution (S-boxes) and permutation (P-boxes) across multiple rounds to provide confusion and diffusion. (Note: DES actually uses a Feistel network, not a pure SPN, but SPNs are used in ciphers like AES. However, the question mentions "proposed by Shannon and used in ciphers such as DES" – Shannon's concept of "mixing" layers applies broadly, and the blank asks for the second half of the classic "substitution-permutation" pairing.)
</details>

---

### 98. NIST's CTR_DRBG, the modern standard block-cipher-based PRNG, operates through which three phases?
- A. Initialize (seed from entropy), Generate (encrypt and increment a counter), and Update (periodically reseed with fresh entropy)
- B. Shuffle, Swap, and Output, exactly as in the RC4 algorithm
- C. Encrypt, Decrypt, and Re-encrypt, exactly as in Triple DES
- D. Select primes, Compute totient, and Generate keys, exactly as in RSA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Initialize (seed from entropy), Generate (encrypt and increment a counter), and Update (periodically reseed with fresh entropy)**

*Intuition:* NIST's CTR_DRBG (Counter-mode Deterministic Random Bit Generator) is a block-cipher-based pseudorandom number generator specified in NIST Special Publication 800-90A. It operates through three main phases: Initialize (Instantiate): The DRBG is seeded with entropy from a trusted entropy source, along with optional nonce and personalization string. This sets up the internal state (including the counter and the key). Generate: When random bits are requested, the DRBG encrypts the current counter value using the block cipher (e.g., AES), produces the keystream, increments the counter, and returns the requested number of bits. This can be repeated as long as the security strength permits before requiring reseeding. Update (Reseed): Periodically (or on request), the DRBG is reseeded with fresh entropy to maintain security and protect against state compromise. This updates the internal key and counter values. The other options are incorrect: B: Shuffle, Swap, and Output describe RC4's PRGA, not CTR_DRBG. C: Encrypt, Decrypt, Re-encrypt describe Triple DES (3DES) operation, not a PRNG. D: Select primes, Compute totient, Generate keys describe RSA key generation, not a PRNG.
</details>

---

### 99. NIST's selection of Rijndael as AES was notable because it was:
- A. Chosen without any competing candidate algorithms being considered
- B. The result of an open, multi-round public competition rather than an algorithm designed internally by the government
- C. The first cipher ever to be patented by a government standards body
- D. Selected purely on the basis of being the fastest candidate in hardware

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. The result of an open, multi-round public competition rather than an algorithm designed internally by the government**

*Intuition:* The selection of Rijndael as the Advanced Encryption Standard (AES) in 2001 was notable because it was the result of an open, transparent, international competition run by NIST. Unlike DES, which was developed internally by IBM and the NSA with limited public input, the AES process: Invited submissions from cryptographers worldwide, Held multiple public conferences to analyze and discuss the candidate algorithms, Considered security, performance (in both hardware and software), and implementation characteristics, Involved extensive public cryptanalysis over several years before narrowing down from 15 candidates to 5 finalists (MARS, RC6, Rijndael, Serpent, and Twofish), Ultimately selected Rijndael in a public announcement. This open process was a landmark in cryptographic standardization and helped build confidence in the security of AES. The other options are incorrect because: A: There were many competing candidates (15 initial submissions). C: AES was not patented by the government; the Rijndael algorithm was unpatented and free to use. D: While efficiency was a factor, the selection was based on a combination of security, performance, and flexibility—not solely on hardware speed.
</details>

---

### 100. A number-theoretic PRNG whose security rests on the difficulty of factoring n = p times q, the same hard problem underlying RSA, is called the ____ generator.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Blum Blum Shub (or BBS) generator**

*Intuition:* The Blum Blum Shub (BBS) generator, proposed by Lenore Blum, Manuel Blum, and Michael Shub in 1986, is a number-theoretic pseudorandom number generator whose security is reducible to the difficulty of the quadratic residuosity problem, which is closely related to the hardness of factoring n = p ⋅ q n=p⋅q. Its recurrence is: X n + 1 = X n 2 mod n X n+1 ​ =X n 2 ​ modn where n = p ⋅ q n=p⋅q is the product of two large primes (typically Blum integers, i.e., primes congruent to 3 mod 4). The output is typically the least significant bit (or several bits) of each X n X n ​ . BBS is provably secure in the sense that predicting its output is as hard as factoring n n, making it cryptographically strong—though it is slower than other PRNGs, so it's mostly used in theoretical contexts or applications where provable security is paramount.
</details>

---

### 101. Which of the following was NOT one of the finalist algorithms in the AES selection process?
- A. Twofish
- B. MARS
- C. Blowfish
- D. Serpent

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Blowfish**

*Intuition:* Explanation: The five finalists in the NIST AES selection process (1997–2000) were: Rijndael (the winner, standardized as AES) Serpent Twofish MARS RC6 Blowfish was designed earlier (in 1993 by Bruce Schneier) with a 64-bit block size, whereas the AES competition required a 128-bit block size. Schneier designed Twofish specifically for the AES process.
</details>

---

### 102. Optimal Asymmetric Encryption Padding (OAEP) is recommended for RSA mainly because it:
- A. Removes the need to generate two distinct large prime numbers
- B. Randomizes the plaintext before encryption, defeating the malleability exploited by chosen-ciphertext attacks
- C. Allows RSA to be used without ever computing a private exponent d
- D. Increases the size of the RSA modulus n automatically at encryption time

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Randomizes the plaintext before encryption, defeating the malleability exploited by chosen-ciphertext attacks**

*Intuition:* Optimal Asymmetric Encryption Padding (OAEP) is a padding scheme for RSA that introduces randomness and structured encoding to the plaintext before encryption. This randomization ensures that: Encrypting the same message twice produces different ciphertexts (probabilistic encryption). The scheme provides semantic security and non-malleability, meaning an attacker cannot modify a ciphertext in a predictable way to produce a valid related plaintext. It defends against adaptive chosen-ciphertext attacks (CCA2) in the random oracle model. The other options are incorrect: A: OAEP does not eliminate the need for two large primes; RSA still requires key generation with n = p ⋅ q n=p⋅q. C: OAEP does not remove the need for the private exponent d d; decryption still requires it. D: OAEP does not change the modulus size; n n is fixed at key generation time.
</details>

---

### 103. Which pair correctly matches an AES key size with its corresponding number of rounds?
- A. 192-bit key -> 10 rounds
- B. 256-bit key -> 12 rounds
- C. 192-bit key -> 12 rounds
- D. 128-bit key -> 14 rounds

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. 192-bit key -> 12 rounds**

*Intuition:* The AES standard defines the following key sizes and corresponding number of rounds: Key Size	Number of Rounds 128-bit	10 rounds 192-bit	12 rounds 256-bit	14 rounds So the only option that correctly matches a key size with its round count is C (192-bit key → 12 rounds). The other options are incorrect: A and D have the rounds reversed, and B incorrectly states 12 rounds for a 256-bit key (which actually uses 14).
</details>

---

### 104. Plain (unpadded) RSA is described as malleable because:
- A. Encrypting the same message twice with the same key always changes the ciphertext
- B. Any two different plaintexts always encrypt to the exact same ciphertext under plain RSA
- C. E(PU, M1) x E(PU, M2) = E(PU, M1*M2), letting an attacker manipulate a ciphertext by a known factor without knowing the plaintext
- D. The private key can be recovered directly from any single intercepted ciphertext

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. E(PU, M1) x E(PU, M2) = E(PU, M1*M2), letting an attacker manipulate a ciphertext by a known factor without knowing the plaintext**

*Intuition:* This is the multiplicative homomorphic property of plain (unpadded) RSA: E ( M 1 ) ⋅ E ( M 2 ) ≡ ( M 1 e mod n ) ⋅ ( M 2 e mod n ) ≡ ( M 1 ⋅ M 2 ) e mod n ≡ E ( M 1 ⋅ M 2 ) ( m o d n ) E(M 1 ​ )⋅E(M 2 ​ )≡(M 1 e ​ modn)⋅(M 2 e ​ modn)≡(M 1 ​ ⋅M 2 ​ ) e modn≡E(M 1 ​ ⋅M 2 ​ )(modn) This property makes plain RSA malleable—an attacker can take an intercepted ciphertext C = M e mod n C=M e modn, multiply it by r e mod n r e modn (for a chosen r r), and obtain a valid ciphertext for M ⋅ r mod n M⋅rmodn, all without knowing the original plaintext M M. This enables chosen-ciphertext attacks and is why proper padding (like OAEP) is essential for RSA in practice. The other options are incorrect: A: Plain RSA is deterministic (no randomness), so encrypting the same message twice gives the same ciphertext. B: RSA is a bijective mapping; different plaintexts encrypt to different ciphertexts (as long as they are in Z n ∗ Z n ∗ ​ ). D: Recovering the private key from a single ciphertext is not possible; the hardness of factoring is what keeps RSA secure.
</details>

---

### 105. The points on an elliptic curve, together with a defined addition rule and a point at infinity, form:
- A. An abelian group, satisfying closure, associativity, an identity element, inverses, and commutativity
- B. A Feistel structure, alternating substitution and permutation at each point
- C. A finite field in the same sense as GF(p), with every point having a multiplicative inverse
- D. A simple ring with no guarantee that every point has an inverse

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. An abelian group, satisfying closure, associativity, an identity element, inverses, and commutativity**

*Intuition:* The points on an elliptic curve (including the point at infinity, which serves as the identity element), together with the geometric "chord-and-tangent" addition rule, form an abelian group. This means they satisfy: Closure: Adding two points on the curve yields another point on the curve. Associativity: ( P + Q ) + R = P + ( Q + R ) (P+Q)+R=P+(Q+R). Identity element: The point at infinity O O acts as the identity, such that P + O = P P+O=P. Inverses: Every point P P has an inverse − P −P such that P + ( − P ) = O P+(−P)=O. Commutativity: P + Q = Q + P P+Q=Q+P. This abelian group structure is the foundation of elliptic curve cryptography (ECC). The other options are incorrect because: B: Feistel structures relate to block ciphers, not elliptic curves. C: The points form a group, not a field (the underlying coordinates come from a field, but the points themselves are not a field). D: Rings require two operations (addition and multiplication); elliptic curve points only have one operation (addition).
</details>

---

### 106. For a positive integer n, arithmetic performed modulo n confines every result to the range:
- A. {0, 1, ..., 2n-1}, doubling the usual modular range for security
- B. {1, 2, ..., n}, excluding zero entirely from every calculation
- C. {-n, ..., 0, ..., n}, allowing both positive and negative remainders freely
- D. {0, 1, ..., n-1}, wrapping around whenever a value would leave that range

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. {0, 1, ..., n-1}, wrapping around whenever a value would leave that range**

*Intuition:* Why D is correct: In standard modular arithmetic modulo n, the complete set of residues is the set of non-negative remainders when divided by n, which is Z n ​ ={0,1,2,…,n−1}. Whenever an operation produces a value outside this set, it wraps around via division by n. Why the others are incorrect: A spans a range of 2n elements, which does not represent standard modulo n reduction. B excludes 0, which is a valid remainder (e.g., when a number is exactly divisible by n). C includes negative numbers and values ≥n, which are not the standard canonical set of least non-negative residues.
</details>

---

### 107. The Prime Number Theorem indicates that, near a large integer n, prime numbers occur on average about once every:
- A. 2 integers checked, since every other integer is prime past a certain point
- B. ln(n) integers checked
- C. n integers checked, regardless of how large n becomes
- D. sqrt(n) integers checked, matching the trial-division bound

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. ln(n) integers checked**

*Intuition:* Explanation: The Prime Number Theorem (PNT) states that the prime counting function π(n), which gives the number of primes less than or equal to n, asymptotically satisfies: π(n)≈ ln(n) n ​ Consequently, the probability that a randomly chosen integer near n is prime is approximately ln(n) 1
</details>

---

### 108. The problem of finding the exponent x that solves g^x ≡ b (mod p), believed to be computationally infeasible for large p, is called the ____ problem.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **discrete-logarithm**

*Intuition:* The correct answer is **discrete-logarithm**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 109. The process that stretches the original AES cipher key into a separate 128-bit round key for every round is called key ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **expansion (or key expansion)**

*Intuition:* In AES, the key expansion (also known as the key schedule) algorithm takes the original cipher key and expands it into a linear array of 128-bit round keys (one for each round, plus an initial AddRoundKey). For example: A 128-bit key produces 11 round keys (10 rounds + 1 initial). A 192-bit key produces 13 round keys (12 rounds + 1 initial). A 256-bit key produces 15 round keys (14 rounds + 1 initial). The key expansion process involves rotations, substitutions (using the S-box), and XOR operations with round constants (Rcon) to ensure that each round key is distinct and exhibits no simple relationship to the original key.
</details>

---

### 110. Given public parameters q = 353 and alpha = 3, with Alice's private key XA = 97 and public key YA = 3^97 mod 353 = 40, and Bob's private key XB = 233 and public key YB = 3^233 mod 353 = 248, Alice computes the shared secret as:
- A. K = XA * XB mod q = 97 * 233 mod 353
- B. K = YA^XB mod q = 40^233 mod 353
- C. K = YB^XA mod q = 248^97 mod 353
- D. K = alpha^(XA+XB) mod q, computed without ever using YA or YB

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. K = YB^XA mod q = 248^97 mod 353**

*Intuition:* In the Diffie-Hellman key exchange, the shared secret is computed as follows: Alice computes K = Y B X A m o d q K=Y B X A ​ ​ modq, where Y B = α X B m o d q Y B ​ =α X B ​ modq. This gives K = ( α X B ) X A = α X A X B m o d q K=(α X B ​ ) X A ​ =α X A ​ X B ​ modq. Bob computes K = Y A X B m o d q K=Y A X B ​ ​ modq, where Y A = α X A m o d q Y A ​ =α X A ​ modq. This gives K = ( α X A ) X B = α X A X B m o d q K=(α X A ​ ) X B ​ =α X A ​ X B ​ modq. So with the given values: Alice: K = 248 97 m o d 353 K=248 97 mod353 Bob: K = 40 233 m o d 353 K=40 233 mod353 Both yield the same shared secret α X A X B m o d q α X A ​ X B ​ modq. The other options are incorrect: A: Multiplying private keys is not how DH works. B: Alice would use Bob's public key Y B Y B ​ , not her own Y A Y A ​ raised to Bob's private exponent. D: The shared secret is α X A X B α X A ​ X B ​ , not α X A + X B α X A ​ +X B ​ , and the computation does use the public keys.
</details>

---

### 111. RC4 begins with a Key Scheduling Algorithm (KSA) that:
- A. Fixes the state array S to a constant, unchanging table for every key
- B. Directly encrypts the plaintext without ever touching a state array
- C. Uses the secret key to scramble a 256-byte state array S into a key-dependent permutation
- D. Generates a brand-new AES key for every byte of output produced

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Uses the secret key to scramble a 256-byte state array S into a key-dependent permutation**

*Intuition:* The RC4 Key Scheduling Algorithm (KSA) initializes a 256-byte state array S S with values 0 through 255. It then uses the secret key to repeatedly swap entries in S S based on the key bytes, producing a key-dependent permutation of the array. This permutation is then used by the Pseudo-Random Generation Algorithm (PRGA) to generate the keystream. The other options are incorrect: A: The state array is not constant; it is scrambled based on the key. B: RC4 does use the state array; the KSA is an essential step. D: RC4 does not generate AES keys; it uses its own keystream generation process.
</details>

---

### 112. RC4's real-world downfall in Wi-Fi security came primarily through WEP because:
- A. WEP replaced RC4 with a much weaker, custom-designed stream cipher
- B. RC4 cannot process variable-length keys, forcing WEP to use a single fixed key
- C. WEP's method of generating and reusing keys fed into RC4 was flawed, not the RC4 algorithm itself in isolation
- D. RC4 itself was mathematically broken and could be reversed without any key at all

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. WEP's method of generating and reusing keys fed into RC4 was flawed, not the RC4 algorithm itself in isolation**

*Intuition:* Explanation: WEP used a short 24-bit Initialization Vector (IV) concatenated directly with a pre-shared master key to form the RC4 key. The small IV space led to frequent IV/key reuse (keystream reuse), and concatenating predictable IVs exposed known weaknesses in RC4's Key Scheduling Algorithm (KSA)—such as the Fluhrer, Mantin, and Shamir (FMS) attack—allowing passive eavesdroppers to recover the master secret key.
</details>

---

### 113. The recommended padding scheme that randomizes RSA plaintext before encryption, defending against chosen-ciphertext attacks, is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **OAEP (or Optimal Asymmetric Encryption Padding / RSA-OAEP)**

*Intuition:* More fully, it is often referred to as RSA-OAEP (RSA with Optimal Asymmetric Encryption Padding). It was introduced by Bellare and Rogaway and is standardized in PKCS#1 v2.0 and later versions. OAEP adds randomness and structured padding to the plaintext before RSA encryption, which provides semantic security and defends against adaptive chosen-ciphertext attacks (CCA2) under the random oracle model.
</details>

---

### 114. Remember the distinction:
- A. Statistical randomness → "Does it look random?"
- B. Cryptographic randomness → "Can an attacker predict future outputs?"
- C. An LCG may satisfy the first but fails the second, which is why it is considered cryptographically worthless.
- D. AES was selected by NIST through an open competition, with the winning algorithm originally named ____, designed by Daemen and Rijmen.

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Statistical randomness → "Does it look random?"**

*Intuition:* ✅ Rijndael Complete sentence: AES was selected by NIST through an open competition, with the winning algorithm originally named Rijndael, designed by Daemen and Rijmen. Quick facts Original algorithm: Rijndael Designers: Joan Daemen and Vincent Rijmen Selected by NIST: 2000 Published as AES (FIPS 197): 2001
</details>

---

### 115. Remember the name Rijndael comes from combining the surnames Rijmen and Daemen. After it won the competition, it was standardized as the Advanced Encryption Standard (AES). The AES round transformation that cyclically shifts each row of the State to the left by an amount equal to the row index is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **ShiftRows**

*Intuition:* ✅ ShiftRows Complete sentence: The AES round transformation that cyclically shifts each row of the State to the left by an amount equal to the row index is called ShiftRows. Quick reminder AES has four main round transformations: SubBytes – Substitute each byte using the S-box. ShiftRows – Cyclically shift each row to the left: Row 0: 0 positions
</details>

---

### 116. Which requirement is essential when parameterizing an RSA-based PRNG such as Micali-Schnorr?
- A. e must be chosen equal to the private exponent d used for RSA decryption
- B. gcd(e, phi(n)) = 1, mirroring the same requirement used for ordinary RSA key generation
- C. The modulus n must be chosen to be a small prime number, unlike ordinary RSA
- D. The output length r must always exceed the modulus n's bit length

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. gcd(e, phi(n)) = 1, mirroring the same requirement used for ordinary RSA key generation**

*Intuition:* In the Micali-Schnorr PRNG (and any RSA-based pseudorandom number generator), the RSA public exponent e e must be coprime to ϕ ( n ) ϕ(n) (i.e., gcd ⁡ ( e , ϕ ( n ) ) = 1 gcd(e,ϕ(n))=1). This is the same fundamental requirement as in standard RSA key generation, ensuring that the encryption function x ↦ x e mod n x↦x e modn is a permutation over the multiplicative group Z n ∗ Z n ∗ ​ , which guarantees that the mapping is bijective and properly invertible (though inversion is not needed for the PRNG's forward direction, the permutation property is essential for the security analysis). The other options are incorrect because: A: e e is the public exponent, not the private exponent d d; they serve different roles. C: The modulus n n must be a large composite (product of two large primes), not a small prime. D: The output length r r is typically less than the bit length of n n; the generator outputs the least significant r r bits of x e mod n x e modn, with r r chosen to balance efficiency and security (typically r ≈ log ⁡ 2 n − safety margin r≈log 2 ​ n−safety margin).
</details>

---

### 117. Reusing the same keystream to encrypt two different messages in a stream cipher is dangerous because:
- A. It doubles the length of the ciphertext for the second message only
- B. It causes the second message to be encrypted with a weaker, shorter effective key
- C. XORing the two resulting ciphertexts together cancels the keystream and exposes the XOR of the two plaintexts
- D. It has no security impact as long as the two plaintexts are of different lengths

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. XORing the two resulting ciphertexts together cancels the keystream and exposes the XOR of the two plaintexts**

*Intuition:* This is the classic keystream reuse attack. In a stream cipher, encryption is C 1 = P 1 ⊕ K C 1 ​ =P 1 ​ ⊕K and C 2 = P 2 ⊕ K C 2 ​ =P 2 ​ ⊕K (using the same keystream K K). If an attacker intercepts both ciphertexts, they can XOR them: C 1 ⊕ C 2 = ( P 1 ⊕ K ) ⊕ ( P 2 ⊕ K ) = P 1 ⊕ P 2 C 1 ​ ⊕C 2 ​ =(P 1 ​ ⊕K)⊕(P 2 ​ ⊕K)=P 1 ​ ⊕P 2 ​ The keystream K K cancels out, leaving the XOR of the two plaintexts. An attacker can then use statistical analysis (e.g., frequency analysis of ASCII text) to recover the original plaintexts. This is why stream ciphers must use a unique, non-repeating keystream for each message — typically achieved through a unique nonce/IV per encryption. The other options are incorrect: A: Reusing the keystream does not double the ciphertext length; it produces ciphertexts of the same length as the plaintexts. B: Reuse does not shorten the effective key length; the problem is keystream repetition, not key strength. D: Even if the plaintexts are of different lengths, the overlapping portion is still exposed, which is a serious security vulnerability.
</details>

---

### 118. In RSA, encryption of message M is computed as C = M^e mod n, and decryption of ciphertext C is computed as M = C^____ mod n.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **d (private exponent)**

*Intuition:* In RSA, decryption is computed as: $M = C^d \pmod n$d n $M = C^d \pmod n$dn where: C C is the ciphertext, d d is the private exponent (the modular multiplicative inverse of e e modulo ϕ ( n ) ϕ(n)), n n is the modulus. Together, encryption C = M e mod n C=M e modn and decryption $M = C^d \pmod n$d n $M = C^d \pmod n$dn are inverse operations because e ⋅ d ≡ 1 ( m o d ϕ ( n ) ) e⋅d≡1(modϕ(n)), ensuring that ( M e ) d ≡ M ( m o d n ) (M e ) d ≡M(modn).
</details>

---

### 119. In RSA key generation, once primes p and q have been chosen, the public modulus is computed as n = p*q and the totient is computed as:
- A. phi(n) = p*q - 1
- B. phi(n) = (p-1)(q-1)
- C. phi(n) = p + q - 1
- D. phi(n) = (p-1) + (q-1)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. phi(n) = (p-1)(q-1)**

*Intuition:* The correct choice is **B. phi(n) = (p-1)(q-1)**. This follows directly from the foundational principles and technical specifications detailed in William Stallings' *Cryptography and Network Security*.
</details>

---

### 120. RSA's underlying trap-door one-way function relies on the difficulty of:
- A. Computing discrete logarithms in a finite field
- B. Generating large pseudo-random prime numbers
- C. Finding collisions in cryptographic hash functions
- D. Factoring the product of two large prime numbers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Factoring the product of two large prime numbers**

*Intuition:* RSA's public-key encryption and digital signature schemes rest on the computational hardness of the **integer factorization problem**. Specifically, given the public modulus $n = p \times q$, it is computationally infeasible for classical computers to determine the distinct prime factors $p$ and $q$ when they are sufficiently large (e.g., 2048+ bits), whereas computing $n$ from $p$ and $q$ is trivial.
</details>

---

### 121. In RSA, the private exponent d is chosen so that it satisfies:
- A. d is simply equal to phi(n) divided by e, with any remainder discarded
- B. d must equal n minus e, computed without any modular reduction
- C. d is the multiplicative inverse of e, modulo phi(n)
- D. d is chosen as any prime number larger than both p and q

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. d is the multiplicative inverse of e, modulo phi(n)**

*Intuition:* Why C is correct: In RSA key generation, the public exponent e and private exponent d satisfy the congruence: e⋅d≡1(modϕ(n)) This means d is the modular multiplicative inverse of e modulo ϕ(n) (or modulo λ(n)=lcm(p−1,q−1)), computed using the Extended Euclidean Algorithm. Why the others are incorrect: A describes integer division, not a modular inverse. B has no mathematical relationship to the required modular arithmetic condition. D is incorrect because d cannot be chosen arbitrarily; it is deterministically derived from e and ϕ(n).
</details>

---

### 122. In RSA, the public key is the pair {e, n} and the private key is the pair {____, n}.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **d (private exponent)**

*Intuition:* The correct answer is **d (private exponent)**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 123. RSA was developed in 1977 by Ron Rivest, Adi Shamir, and Len ____, whose initials give the algorithm its name.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Adleman**

*Intuition:* The full name is Ron Rivest, Adi Shamir, and Leonard Adleman — their initials (Rivest–Shamir–Adleman) form the acronym RSA.
</details>

---

### 124. The security of the Blum Blum Shub generator rests on:
- A. The unpredictability of thermal noise sampled from physical hardware
- B. The difficulty of solving a system of linear congruential equations
- C. The length of the AES key used inside its internal encryption step
- D. The difficulty of factoring n back into its two large prime factors, the same hard problem underlying RSA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The difficulty of factoring n back into its two large prime factors, the same hard problem underlying RSA**

*Intuition:* Explanation: The Blum Blum Shub (BBS) pseudorandom bit generator operates using the recurrence X n+1 ​ =X n 2 ​ (modn), where n=p×q is a Blum integer (the product of two large prime numbers p and q, both congruent to 3(mod4)). The security of BBS has a provable reduction to the computational difficulty of calculating quadratic residues modulo n, which is equivalent to the integer factorization problem.
</details>

---

### 125. A sequence produced by a linear congruential generator can pass every standard statistical randomness test and still be considered cryptographically worthless because:
- A. LCG output is always shorter than the plaintext it is meant to protect
- B. An attacker who recovers a handful of consecutive outputs can solve for the generator's parameters and predict all future values
- C. Statistical tests are incapable of evaluating any algorithmically generated sequence
- D. LCGs cannot produce output that is uniformly distributed under any parameter choice

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. An attacker who recovers a handful of consecutive outputs can solve for the generator's parameters and predict all future values**

*Intuition:* This is the fundamental cryptographic weakness of linear congruential generators (LCGs). Even though an LCG may produce output that passes standard statistical tests for randomness (uniformity, independence, etc.), it is entirely deterministic and linear. Given just a few consecutive outputs, an attacker can set up a system of linear congruences to solve for the unknown modulus m m, multiplier a a, increment c c, and the internal state. Once these parameters are recovered, all past and future outputs can be predicted with certainty. This makes LCGs completely unsuitable for cryptographic applications, where unpredictability (not just statistical randomness) is required. The other options are incorrect: A: LCG output length is not inherently limited; it can produce arbitrarily long streams. C: Statistical tests can evaluate algorithmically generated sequences; they just can't guarantee cryptographic security. D: LCGs can be uniformly distributed over their full period if parameters are chosen correctly (e.g., full-period conditions).
</details>

---

### 126. The set of points on an elliptic curve, together with a defined addition rule and a point at infinity, forms an algebraic structure called an ____ group.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **an abelian group**

*Intuition:* The set of points on an elliptic curve (including the point at infinity as the identity element), together with the geometric "chord-and-tangent" addition rule, forms an abelian group (also called a commutative group). This means the group operation is: Closure: Adding two points on the curve yields another point on the curve. Associative: ( P + Q ) + R = P + ( Q + R ) (P+Q)+R=P+(Q+R). Identity: There is a point at infinity O O such that P + O = P P+O=P. Inverse: For every point P P, there exists a point − P −P such that P + ( − P ) = O P+(−P)=O. Commutative: P + Q = Q + P P+Q=Q+P. This abelian group structure is the foundation of elliptic curve cryptography (ECC).
</details>

---

### 127. Shannon's principle of confusion is achieved mainly by:
- A. Spreading each plaintext bit's influence across the whole ciphertext block
- B. Choosing a block size larger than the key size
- C. Repeating the plaintext block several times before encryption begins
- D. Making the relationship between the ciphertext and the key as complex as possible, typically through substitution

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Making the relationship between the ciphertext and the key as complex as possible, typically through substitution**

*Intuition:* Claude Shannon's principle of confusion aims to make the relationship between the encryption key and the ciphertext as intricate and involved as possible, so that even if an attacker knows the statistical structure of the plaintext, they cannot easily deduce the key from the ciphertext. In modern block ciphers, confusion is primarily achieved through non-linear substitution (e.g., S-boxes), which obscures the algebraic relationship between the key and the ciphertext. The other option describes diffusion, not confusion: Diffusion (option A) spreads each plaintext bit's influence across many output bits (e.g., through permutations like ShiftRows and MixColumns in AES), making it harder to trace small changes in the plaintext through to the ciphertext. The remaining options are incorrect: B: Block size is not directly tied to confusion; it's a separate design parameter. C: Repeating the plaintext is not a security principle; it would actually weaken the cipher by introducing redundancy.
</details>

---

### 128. Shannon's principle of diffusion is achieved mainly by:
- A. Replacing the round function with a simple table lookup
- B. Making the ciphertext statistics depend on the key in a highly complex way
- C. Reducing the key length needed to resist brute-force search
- D. Spreading the influence of each plaintext bit over many bits of the ciphertext

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Spreading the influence of each plaintext bit over many bits of the ciphertext**

*Intuition:* Explanation: Claude Shannon defined diffusion as the cryptographic technique of spreading the statistical structure and influence of individual plaintext digits across many ciphertext digits (frequently implemented via permutations, transpositions, and bit-mixing operations). By contrast, making the relationship between the key and the ciphertext complex is Shannon's principle of confusion (typically achieved via substitution / S-boxes).
</details>

---

### 129. In ShiftRows, row r of the State is cyclically shifted left by:
- A. One byte for every row without exception
- B. r bytes, so row 0 is unshifted, row 1 shifts by 1, row 2 by 2, and row 3 by 3
- C. r bits rather than r bytes, applied to every row equally
- D. A fixed 4 bytes regardless of which row it is

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. r bytes, so row 0 is unshifted, row 1 shifts by 1, row 2 by 2, and row 3 by 3**

*Intuition:* In the ShiftRows transformation of AES, the 4×4 State array is shifted row by row as follows: Row 0: Shifted left by 0 bytes (no shift). Row 1: Shifted left by 1 byte. Row 2: Shifted left by 2 bytes. Row 3: Shifted left by 3 bytes. This cyclic left shift (with wrap-around) is applied on a byte basis, not bitwise. The effect is that bytes in each row are moved to different column positions, providing diffusion by spreading the influence of each column across multiple columns when combined with MixColumns. The other options are incorrect: A: The shift amount varies by row (0, 1, 2, 3 bytes). C: The shift is in bytes, not bits, and the amount varies by row. D: The shift amount is not fixed at 4 bytes for all rows; it depends on the row index.
</details>

---

### 130. The square-and-multiply technique for RSA is valuable because it computes a large modular exponentiation such as x^16 using:
- A. Addition alone, avoiding multiplication entirely
- B. Repeated squaring, needing only a handful of multiplications instead of performing the full exponent's worth
- C. A random guess-and-check process repeated until the result matches
- D. A single lookup table indexed by the exponent value

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Repeated squaring, needing only a handful of multiplications instead of performing the full exponent's worth**

*Intuition:* The square-and-multiply (also called exponentiation by squaring) algorithm is valuable because it reduces the number of multiplications needed for modular exponentiation from O ( e ) O(e) (where e e is the exponent) to O ( log ⁡ 2 e ) O(log 2 ​ e). For example, computing x 16 x 16 naively would require 15 multiplications ( x ⋅ x ⋅ x ⋯ x⋅x⋅x⋯). With repeated squaring, you compute: x 2 x 2 (1 multiplication) x 4 = ( x 2 ) 2 x 4 =(x 2 ) 2 (2nd multiplication) x 8 = ( x 4 ) 2 x 8 =(x 4 ) 2 (3rd multiplication) x 16 = ( x 8 ) 2 x 16 =(x 8 ) 2 (4th multiplication) So only 4 multiplications are needed instead of 15. For larger exponents like those used in RSA (e.g., 2048-bit exponents), this technique is computationally essential.
</details>

---

### 131. A standard defense against RSA timing attacks is to:
- A. Ensure exponentiation always takes constant time, or add blinding by masking the ciphertext with a random factor before exponentiating
- B. Disable the use of the Chinese Remainder Theorem during decryption entirely
- C. Switch to a smaller RSA key size so that decryption completes faster
- D. Encrypt every message twice in succession using the same public key

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Ensure exponentiation always takes constant time, or add blinding by masking the ciphertext with a random factor before exponentiating**

*Intuition:* Explanation: Timing attacks exploit the variance in execution time of private-key modular exponentiation operations (such as modular multiplication steps that depend on private key bits). Standard defenses include: Blinding (Cryptographic Blinding): Multiplying the ciphertext by a random secret value r e (modn) before performing the private-key exponentiation, and then dividing out r afterward, effectively masking the execution timing from an attacker. Constant-Time Implementations: Ensuring that the modular exponentiation algorithm executes in a fixed number of clock cycles regardless of the private key bits or input data.
</details>

---

### 132. The standard practical fix for the Diffie-Hellman man-in-the-middle vulnerability is to add:
- A. Digital signatures and public-key certificates to authenticate each party's exchanged value
- B. A symmetric pre-shared key used instead of the discrete logarithm exchange
- C. Multiple additional unauthenticated rounds of the identical exchange
- D. A longer prime modulus q, with no other changes required to the protocol

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Digital signatures and public-key certificates to authenticate each party's exchanged value**

*Intuition:* The standard and practical fix for the Diffie-Hellman man-in-the-middle (MITM) vulnerability is to authenticate the exchanged public values (or the entire Diffie-Hellman messages) using digital signatures. This is typically done by: Each party signing their ephemeral public value (or the entire transcript) with their long-term private key, The receiving party verifying the signature using the sender's public key certificate (issued by a trusted Certificate Authority). This ensures that each party knows they are communicating with the genuine owner of the public key, rather than an attacker. This approach is used in protocols like Station-to-Station (STS) protocol, IPsec IKE, TLS (with certificate-based authentication), and SSH. The other options are incorrect: B: Using a pre-shared symmetric key avoids the MITM issue but is not practical for large-scale open systems (key distribution problem) and is not a "fix" to the DH protocol itself. C: Adding more unauthenticated rounds does nothing to prevent MITM, since the attacker can still intercept and relay all messages. D: A longer prime modulus increases security against discrete logarithm attacks but does nothing to authenticate the parties; the MITM attack remains possible regardless of the modulus size.
</details>

---

### 133. The statement a ≡ b (mod n) means that:
- A. a multiplied by b is always evenly divisible by n
- B. n divides (a - b), so a and b leave the same remainder when divided by n
- C. a and b are both prime numbers that happen to share the modulus n
- D. a and b must be equal integers before applying the modulus operation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. n divides (a - b), so a and b leave the same remainder when divided by n**

*Intuition:* The notation a ≡ b ( m o d n ) a≡b(modn) means that a a and b b are congruent modulo n n, which is defined as: n n divides a − b a−b (i.e., a − b = k ⋅ n a−b=k⋅n for some integer k k), Equivalently, a a and b b leave the same remainder when divided by n n. For example, 17 ≡ 5 ( m o d 6 ) 17≡5(mod6) because 17 − 5 = 12 17−5=12, and 12 12 is divisible by 6 6. Both 17 and 5 leave a remainder of 5 when divided by 6. The other options are incorrect: A: a ⋅ b a⋅b being divisible by n n is not the definition of congruence; that's a different condition. C: Congruence does not require a a or b b to be prime. D: a a and b b do not need to be equal; they only need to differ by a multiple of n n.
</details>

---

### 134. Which statement correctly compares CBC and CTR mode with respect to error propagation from a single corrupted ciphertext bit?
- A. Neither mode is affected at all by a single corrupted ciphertext bit
- B. Both modes propagate a corrupted bit through every subsequent block indefinitely
- C. CTR always corrupts the entire remaining message, while CBC corrupts nothing
- D. In CBC, a corrupted bit affects that block and flips the corresponding bit in the next block's decrypted plaintext; in CTR, it affects only the corresponding bit of that same block

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. In CBC, a corrupted bit affects that block and flips the corresponding bit in the next block's decrypted plaintext; in CTR, it affects only the corresponding bit of that same block**

*Intuition:* **Why D is correct:**
- **CBC Mode:** Plaintext decryption is computed as $P_i = D_K(C_i) \oplus C_{i-1}$. If a single bit in $C_i$ is corrupted during transmission, passing it through the block cipher decryption function $D_K(C_i)$ completely scrambles/corrupts block $P_i$ due to the avalanche effect. When $C_i$ is subsequently XORed into the next block ($P_{i+1} = D_K(C_{i+1}) \oplus C_i$), only the exact corresponding bit in $P_{i+1}$ flips. Error propagation strictly stops after block $i+1$.
- **CTR Mode:** Plaintext decryption is computed as $P_i = C_i \oplus E_K(\text{Counter}_i)$. Since keystream generation is completely independent of the ciphertext and the operation is bitwise XOR, a single corrupted ciphertext bit in $C_i$ flips only the exact corresponding bit in $P_i$, with zero cascading into subsequent blocks.

**Why the others are incorrect:**
- **A** is false because bit errors directly impact the decrypted output in both modes.
- **B** confuses CBC/CTR with continuous feedback modes where errors might persist indefinitely, whereas standard CBC stops propagating after block $i+1$.
- **C** reverses and exaggerates the behavior; CTR exhibits no multi-block error propagation.
</details>

---

### 135. Which statement correctly compares PRNG output with TRNG output?
- A. PRNG output never repeats, while TRNG output repeats after a fixed period
- B. PRNG output is fast, deterministic, and eventually periodic, while TRNG output is slower, non-deterministic, and does not repeat
- C. Both PRNG and TRNG output are fully reproducible from the same starting seed
- D. TRNG output is always faster to generate than PRNG output, but less secure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. PRNG output is fast, deterministic, and eventually periodic, while TRNG output is slower, non-deterministic, and does not repeat**

*Intuition:* This correctly captures the essential differences: PRNG (Pseudo-Random Number Generator): Fast (computationally efficient). Deterministic (given the same seed, it produces the exact same sequence). Eventually periodic (its output sequence will repeat after a finite period, though the period can be made very large with good design). Suitable for cryptographic applications when seeded with sufficient entropy and cryptographically secure (CSPRNG). TRNG (True Random Number Generator): Slower (relies on physical processes like thermal noise, which are typically slower than arithmetic operations). Non-deterministic (outputs are not reproducible; even with the same initial conditions, the output differs because the physical process is inherently unpredictable). Does not repeat (in practice, it is aperiodic and does not have a guaranteed finite period). The other options are incorrect: A: PRNGs do repeat (eventually), while TRNGs do not have a fixed period. C: TRNG output is not reproducible from a seed; only PRNG output is. D: TRNG is slower, not faster, than PRNG.
</details>

---

### 136. In a stream cipher, ciphertext is produced by:
- A. Substituting each plaintext block with a fixed-size hash of that block
- B. Passing the plaintext through several parallel S-boxes without any key material
- C. Multiplying the plaintext by the key modulo a large prime number
- D. XORing the plaintext with a keystream generated from the secret key by a PRNG

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. XORing the plaintext with a keystream generated from the secret key by a PRNG**

*Intuition:* The correct choice is **D. XORing the plaintext with a keystream generated from the secret key by a PRNG**. This follows directly from the foundational principles and technical specifications detailed in William Stallings' *Cryptography and Network Security*.
</details>

---

### 137. In a stream cipher, the pseudorandom sequence of bits combined with the plaintext via XOR to produce ciphertext is called the ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **keystream**

*Intuition:* The correct answer is **keystream**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 138. For a stream cipher to be considered secure, all of the following are generally required EXCEPT:
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The keystream must be shorter than plaintext so it can be reused efficiently across several messages**

*Intuition:* The correct answer is **C. The keystream must be shorter than plaintext so it can be reused efficiently across several messages**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 139. In the terminology Stallings uses for classical and modern ciphers, permutation is best described as an operation that:
- A. Compresses the plaintext into a shorter, fixed-length representation
- B. Rearranges the order of plaintext elements without adding, removing, or replacing any of them
- C. Splits the plaintext into independent blocks that are encrypted with different keys
- D. Replaces each plaintext element with a different symbol drawn from a fixed alphabet

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Rearranges the order of plaintext elements without adding, removing, or replacing any of them**

*Intuition:* In Stallings' terminology, a permutation (or transposition) changes the position of elements in the plaintext but leaves the actual elements unchanged.
</details>

---

### 140. Testing whether 29 is prime by checking divisibility only up to sqrt(29) ≈ 5.4 works because:
- A. Any factor larger than the square root of a number must be paired with a factor smaller than the square root
- B. Numbers greater than the square root are automatically assumed to be prime
- C. The square root always equals exactly half of the number being tested
- D. 29 is a special case, and this shortcut does not generalize to any other number

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Any factor larger than the square root of a number must be paired with a factor smaller than the square root**

*Intuition:* This is the fundamental reason for the square root shortcut in primality testing. If a composite number n n has a factor a > n a> n ​ , then the complementary factor b = n / a b=n/a must satisfy b < n b< n ​ . Therefore, if no factor is found up to n n ​ , no factor can exist at all. This principle applies universally to all integers, not just 29. The other options are incorrect because: B: Numbers larger than the square root are not automatically prime (e.g., 49 has factors 7 and 7, both equal to the square root). C: The square root is not "exactly half" except for the number 4. D: This shortcut generalizes to every positive integer; 29 is not a special case.
</details>

---

### 141. The theorem guaranteeing that every integer greater than 1 factors into primes in exactly one way is called the ____ Theorem of Arithmetic.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **fundamental-theorem**

*Intuition:* The correct answer is **fundamental-theorem**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 142. A timing attack against RSA, as described by Kocher, works by:
- A. Directly factoring the public modulus n using a quantum computer
- B. Guessing the plaintext message and checking it against a list of common phrases
- C. Measuring how long decryption takes for different ciphertexts to leak information about the private key, bit by bit
- D. Exploiting a mathematically proven flaw in the RSA encryption formula itself

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Measuring how long decryption takes for different ciphertexts to leak information about the private key, bit by bit**

*Intuition:* In Kocher's timing attack, the attacker exploits the fact that the time taken to perform modular exponentiation (or other operations like CRT reduction) varies depending on the bits of the private exponent. By measuring these timing differences across many carefully chosen ciphertexts, the attacker can statistically deduce the private key bits one by one.
</details>

---

### 143. Timing-attack research on DES found that measuring decryption time can reveal:
- A. Nothing useful at all, since DES executes in constant time by design
- B. The plaintext directly, without needing to know anything about the key
- C. The complete 56-bit key after only a handful of timed decryptions
- D. The Hamming weight of the key (how many key bits are set to one), but not the key itself

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The Hamming weight of the key (how many key bits are set to one), but not the key itself**

*Intuition:* Why D is correct: In early timing-attack research on symmetric algorithms like DES (e.g., studies evaluating conditional operations or bit-manipulation delays in software implementations), timing variations correlated with the Hamming weight (the total count of 1-bits) in the secret key. While timing attacks against modular exponentiation in RSA/Diffie-Hellman can reconstruct the exact secret key bit-by-bit, timing analysis on standard DES implementations generally leaked only aggregate properties like the Hamming weight rather than determining individual key bit positions directly. Why the others are incorrect: A is false because naive software implementations of DES often exhibit slight timing variations due to data/key-dependent conditional branches, memory cache lookups, or instruction timings. B is false because timing attacks exploit side-channel leakage to gain information about secret key material, not direct algebraic decryption of the plaintext without a key. C is false because recovering the entire 56-bit DES key purely through a handful of generic timing measurements is not achievable.
</details>

---

### 144. A trap-door one-way function is defined as a function that is:
- A. A function that produces the exact same output regardless of its input
- B. Easy to invert for everyone, regardless of whether they hold any secret information
- C. Impossible to compute in both directions under any circumstances
- D. Easy to compute in one direction, and easy to invert only if you possess a secret piece of extra information

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Easy to compute in one direction, and easy to invert only if you possess a secret piece of extra information**

*Intuition:* Explanation: A trapdoor one-way function is easy to compute in the forward direction y=f(x), computationally infeasible to invert without additional knowledge, but easy to invert x=f −1 (y) given a specific piece of auxiliary secret information (known as the "trapdoor"). This concept forms the mathematical foundation of asymmetric (public-key) cryptography algorithms like RSA.
</details>

---

### 145. Triple DES (3DES), typically applying Encrypt-Decrypt-Encrypt with two or three keys, achieves an effective key length of up to:
- A. 168 bits, using three independent keys
- B. 56 bits, the same as single DES
- C. 224 bits, matching twice the length of AES-256's key
- D. 112 bits, even when three independent keys are used

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 168 bits, using three independent keys**

*Intuition:* **Where did the rest of the bits go?**
1. **Raw Key Size vs. Effective Key Material:** In the original Data Encryption Standard (DES), each 64-bit key consists of 8 bytes. Within each byte, the 8th bit (bits 8, 16, 24, 32, 40, 48, 56, 64) is an **odd parity bit** used strictly for hardware error detection. During the key scheduling algorithm's initial Permuted Choice 1 (PC-1) stage, these 8 parity bits are stripped and discarded, leaving exactly **56 bits of effective cryptographic key material** per DES key.
2. **3-Key 3DES Calculation ($K_1, K_2, K_3$):**
   - **Total raw bits:** $3 \times 64 = 192\text{ bits}$
   - **Parity bits discarded:** $3 \times 8 = 24\text{ bits}$ (this is where the missing 24 bits pass!)
   - **Effective key length:** $3 \times 56 = \mathbf{168\text{ bits}}$
3. **2-Key 3DES Calculation ($K_1, K_2, K_1$):**
   - **Total raw bits:** $2 \times 64 = 128\text{ bits}$
   - **Parity bits discarded:** $2 \times 8 = 16\text{ bits}$
   - **Effective key length:** $2 \times 56 = \mathbf{112\text{ bits}}$
4. **Key Length vs. Cryptanalytic Security:** While the nominal key length of 3-key 3DES is 168 bits, meet-in-the-middle (MITM) attacks allow an attacker with known plaintext-ciphertext pairs to break 3DES in $2^{112}$ operations (112 bits of effective security), which is why 112 bits is a common exam distractor and why NIST deprecated 3DES.
</details>

---

### 146. A True Random Number Generator (TRNG) differs from a PRNG chiefly in that a TRNG:
- A. Draws its randomness from an unpredictable physical process, such as thermal noise, rather than a deterministic algorithm
- B. Cannot be used to seed any other type of random number generator
- C. Requires a secret key to be shared in advance between sender and receiver
- D. Always produces output faster than any PRNG can achieve

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Draws its randomness from an unpredictable physical process, such as thermal noise, rather than a deterministic algorithm**

*Intuition:* A True Random Number Generator (TRNG) obtains randomness from inherently unpredictable physical phenomena—such as thermal noise, atmospheric noise, radioactive decay, or quantum effects—that are non-deterministic in nature. This makes the output truly random and not reproducible. In contrast, a Pseudorandom Number Generator (PRNG) uses a deterministic algorithm to produce a sequence of numbers from a seed. While the output may statistically resemble randomness, it is entirely reproducible if the seed is known, and it is eventually periodic. The other options are incorrect: B: TRNGs are commonly used to seed PRNGs (e.g., a TRNG provides the initial entropy to seed a CSPRNG). C: TRNGs do not require a shared secret key; they are not a cryptographic key exchange mechanism. D: TRNGs are typically slower than PRNGs because they rely on physical processes, whereas PRNGs are fast arithmetic operations.
</details>

---

### 147. Using the Chinese Remainder Theorem to speed up RSA's private-key operations works by:
- A. Splitting the decryption exponentiation into two smaller computations modulo p and modulo q, then recombining the results
- B. Replacing modular exponentiation entirely with simple XOR operations
- C. Avoiding the need to know either p or q once the public key has been published
- D. Reducing the RSA key size requirement from 2048 bits down to 512 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Splitting the decryption exponentiation into two smaller computations modulo p and modulo q, then recombining the results**

*Intuition:* Explanation: Since n=p×q, RSA-CRT computes: M p ​ =C d(modp−1) (modp) M
</details>

---

### 148. Using the Chinese Remainder Theorem to split RSA decryption into two smaller modular exponentiations, one modulo p and one modulo q, speeds up decryption by roughly a factor of ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **4 (or 4x)**

*Intuition:* The correct answer is **4 (or 4x)**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 149. Using the Euclidean Algorithm on 252 and 105 (252 = 2*105 + 42, 105 = 2*42 + 21, 42 = 2*21 + 0), gcd(252, 105) equals:
- A. 21
- B. 105
- C. 7
- D. 42

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 21**

*Intuition:* The Euclidean Algorithm proceeds as follows: 252 = 2 × 105 + 42 252=2×105+42 → remainder 42 105 = 2 × 42 + 21 105=2×42+21 → remainder 21 42 = 2 × 21 + 0 42=2×21+0 → remainder 0 When the remainder reaches 0, the last non-zero remainder is the greatest common divisor (gcd). The last non-zero remainder here is 21. So, gcd ⁡ ( 252 , 105 ) = 21 gcd(252,105)=21.
</details>

---

### 150. Using the LCG recurrence Xn+1 = (5*Xn + 3) mod 16 with seed X0 = 7, the first two outputs X1 and X2 are:
- A. X1 = 1, X2 = 6
- B. X1 = 7, X2 = 3
- C. X1 = 6, X2 = 1
- D. X1 = 3, X2 = 6

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. X1 = 6, X2 = 1**

*Intuition:* Let's compute step by step using the LCG recurrence X n + 1 = ( 5 ⋅ X n + 3 ) m o d 16 X n+1 ​ =(5⋅X n ​ +3)mod16, with seed X 0 = 7 X 0 ​ =7. X₁: X 1 = ( 5 ⋅ 7 + 3 ) m o d 16 = ( 35 + 3 ) m o d 16 = 38 m o d 16 = 6 X 1 ​ =(5⋅7+3)mod16=(35+3)mod16=38mod16=6 X₂: X 2 = ( 5 ⋅ 6 + 3 ) m o d 16 = ( 30 + 3 ) m o d 16 = 33 m o d 16 = 1 X 2 ​ =(5⋅6+3)mod16=(30+3)mod16=33mod16=1 So X 1 = 6 X 1 ​ =6 and X 2 = 1 X 2 ​ =1, which matches option C.
</details>

---

### 151. The value that provides variability so that identical plaintext blocks do not produce identical ciphertext at the start of CBC or CFB encryption is called the ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Initialization Vector (or initialization vector / IV)**

*Intuition:* In CBC (Cipher Block Chaining) and CFB (Cipher Feedback) modes, the initialization vector (IV) is a random or pseudorandom value that is XORed with the first plaintext block (in CBC) or used as the initial input to the feedback shift register (in CFB) before encryption. The IV provides variability so that: Identical plaintext blocks do not produce identical ciphertext blocks (even for the same key), The same message encrypted twice with the same key produces different ciphertexts, It prevents precomputation attacks and pattern analysis. The IV does not need to be kept secret, but it must be unpredictable (for CBC mode) or unique (for CFB mode) and should be transmitted along with the ciphertext (usually in the clear).
</details>

---

### 152. When selecting a mode of operation for high-throughput, parallelizable, general-purpose encryption, the most appropriate recommendation is typically:
- A. ECB mode
- B. XTS-AES, regardless of whether the data is stored or transmitted
- C. CFB mode with a very small segment size
- D. CTR mode

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. CTR mode**

*Intuition:* Explanation: In CTR (Counter) mode, keystream blocks are generated independently by encrypting incrementing counter values (E K ​ (Counter i ​ )). Because there are no sequential data dependencies between blocks, both encryption and decryption are fully parallelizable across multi-core processors and hardware pipelines, making CTR (and its authenticated derivative, GCM) the standard choice for high-throughput applications. ECB (A) is insecure.
</details>

---

### 153. Why is factoring huge numbers considered computationally hard even when a shortcut like the shared-prime-factor rule can quickly find a gcd once factorizations are already known?
- A. Because the gcd shortcut only ever works for numbers smaller than 1,000
- B. Because gcd computation requires knowledge of the discrete logarithm first
- C. That shortcut assumes the factorizations are already available; obtaining those factorizations for very large numbers in the first place is itself the hard step
- D. Because factoring and computing a gcd are mathematically the identical operation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. That shortcut assumes the factorizations are already available; obtaining those factorizations for very large numbers in the first place is itself the hard step**

*Intuition:* The Euclidean algorithm can compute the gcd of two numbers very efficiently (in polynomial time) if you have the numbers themselves. However, in cryptographic contexts like RSA, the hardness lies in obtaining the prime factorization of a large composite number n = p ⋅ q n=p⋅q in the first place. Once the factorizations are known, finding a shared factor (gcd) is trivial. But finding those factors—i.e., factoring a 2048-bit or larger number—is computationally infeasible with current algorithms and hardware. That is the core assumption underpinning the security of RSA and other factoring-based cryptosystems. The other options are incorrect: A: The gcd shortcut works for numbers of any size, not just small ones. B: GCD computation does not require discrete logarithms; it's a different problem. D: Factoring and gcd are not identical operations; factoring is hard, gcd is easy.
</details>

---

### 154. Why is MixColumns skipped in the final AES round rather than in every round?
- A. Because skipping it doubles the effective key length of the cipher
- B. Because MixColumns cannot be computed on the very last block of a message
- C. To keep encryption invertible and simple while still ensuring the earlier rounds provide adequate diffusion
- D. Because the final round always uses a 256-bit key regardless of the chosen AES variant

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. To keep encryption invertible and simple while still ensuring the earlier rounds provide adequate diffusion**

*Intuition:* In AES, MixColumns is skipped in the final round (but performed in all previous rounds) for structural and security reasons: Invertibility: The final round of AES is designed to be structurally symmetric to the initial AddRoundKey and the inverse cipher. Omitting MixColumns in the final round makes the decryption process match the encryption structure more cleanly—it allows the final round to consist only of SubBytes, ShiftRows, and AddRoundKey (the inverse operations in reverse order during decryption). Security: The full diffusion provided by MixColumns in the earlier rounds (especially combined with ShiftRows) is already sufficient to ensure that every output bit depends on every input bit and every key bit. Adding MixColumns in the final round would not provide any additional security benefit, because: The final round is followed by no further rounds to diffuse its output. The final AddRoundKey already mixes the key in directly. The omission does not weaken the cipher, as all the necessary diffusion has already been achieved by the previous N r − 1 N r ​ −1 rounds. Simplicity and Efficiency: Skipping MixColumns in the final round reduces computational cost slightly without compromising security. The other options are incorrect: A: Skipping MixColumns does not double the key length. B: MixColumns is defined for any block of 16 bytes; it is not limited by message position. D: The number of rounds and key size are determined by the AES variant; the final round always skips MixColumns regardless of key size.
</details>

---

### 155. The widely deployed stream cipher designed by Ron Rivest in 1987, later used in SSL/TLS and WEP, is called ____.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **RC4**

*Intuition:* The correct answer is **RC4**. This reflects the standard technical terminology established in the course syllabus and cryptographic standards.
</details>

---

### 156. Given x ≡ 2 (mod 3) and x ≡ 3 (mod 5), the Chinese Remainder Theorem gives the unique solution in the range 0 to 14 as:
- A. x = 11
- B. x = 8
- C. x = 13
- D. x = 2

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. x = 8**

*Intuition:* Calculation: Testing integers congruent to 3(mod5): x=3⟹3(mod3)=0  =2 x=8⟹8(mod3)=2 and 8(mod5)=3 Modulo M=3×5=15, the unique solution in the range [0,14] is x=8.
</details>

---

### 157. XTS-AES is a specialized mode designed primarily for:
- A. Block-oriented storage devices such as hard drives and SSDs
- B. Producing message authentication codes for email
- C. Generating session keys for TLS handshakes
- D. Streaming voice and video data over unreliable wireless links

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Block-oriented storage devices such as hard drives and SSDs**

*Intuition:* XTS-AES (XEX-based Tweaked Codebook mode with Ciphertext Stealing) is a specialized mode of operation designed by NIST (SP 800-38E) specifically for block-oriented storage encryption—such as hard drives, solid-state drives (SSDs), and other disk storage devices. Key features of XTS-AES: It uses a tweak derived from the logical block address (sector/block index) to ensure that identical plaintext data stored at different locations encrypts to different ciphertexts. It provides length-preserving encryption (ciphertext is the same length as plaintext), which is essential for storage devices where data must fit exactly into fixed-size sectors. It uses Ciphertext Stealing to handle data that is not a multiple of the block size, ensuring efficient use of storage without padding. XTS-AES is not designed for: B: Message authentication (it provides confidentiality only, not integrity or authentication). C: Key exchange or session key generation (that's the domain of key establishment protocols). D: Streaming data over unreliable links (where modes like CTR or GCM are more appropriate).
</details>

---

### 158. XTS-AES ties encryption to a particular physical storage location by using:
- A. A running counter that resets to zero once per day
- B. A separate hash function computed over the entire disk
- C. A second, independently generated AES key for every sector
- D. A tweak value derived from the sector or block address, alongside the key

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A tweak value derived from the sector or block address, alongside the key**

*Intuition:* XTS-AES (XEX-based Tweaked Codebook mode with Ciphertext Stealing) is a mode of operation specifically designed for disk and storage encryption. It uses a tweak—a value derived from the sector or block address—along with the encryption key to ensure that the same plaintext data stored at different physical locations encrypts to different ciphertexts. This prevents block shuffling attacks and ties the ciphertext to its specific location on the storage medium. The tweak is typically generated using the sector index and a second key (the "tweak key"), which together provide both location-dependent encryption and strong security properties for storage devices.
</details>

---
