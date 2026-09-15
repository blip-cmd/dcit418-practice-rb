# DCIT 418: Systems and Network Security
## Quiz 4: Cryptography & Block Cipher Modes (Bayat's Take - 68 Questions)
**Department of Computer Science, University of Ghana**  
**Course Code:** DCIT 418 | **Credits:** 3 Credits  
**Quiz:** Quiz 4 | **Topic:** Cryptographic Fundamentals, Active/Passive Attacks, Symmetric Block Ciphers (DES, 3DES, AES), Block Cipher Modes of Operation (ECB, CBC, CFB, CTR), Number Theory (Euler's Totient, Fermat's Little Theorem, CRT, Euclidean Algorithm), Public Key Cryptography (RSA, ElGamal, ECC, Diffie-Hellman), and CSPRNGs (BBS, TRNGs)

---

### 📝 Study Checklist & Progress Tracker
- [ ] **I have done the MCQs** *(Last attempted: )*
- [ ] **I have done the essay / short answer questions** *(Last attempted: )*

---

> [!NOTE]
> This document contains the complete master question bank and detailed solutions for **DCIT 418: Quiz 4 (Bayat's Take - 68 Questions)**.
> - A complete **Answer Summary Table** is provided at the top for quick reference.
> - A **Question Frequency & Repetition Analysis Table** tracks occurrence counts across source takes.
> - Each question features an interactive **"Reveal Answer"** drop-down containing the correct option and detailed engineering/conceptual intuition.

## Complete Answer Summary Table

| Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|---|--------|---|--------|
| **1** | C | **13** | D | **25** | A | **37** | B | **49** | D | **61** | B |
| **2** | A | **14** | Trans | **26** | D | **38** | A | **50** | D | **62** | B |
| **3** | CFB | **15** | B | **27** | A | **39** | C | **51** | A | **63** | B |
| **4** | Meet | **16** | C | **28** | D | **40** | A | **52** | B | **64** | B |
| **5** | RSA | **17** | B | **29** | C | **41** | A | **53** | A | **65** | B |
| **6** | A | **18** | D | **30** | A | **42** | B | **54** | A | **66** | D |
| **7** | D | **19** | B | **31** | C | **43** | B | **55** | A | **67** | C |
| **8** | A | **20** | A | **32** | B | **44** | A | **56** | B | **68** | A |
| **9** | B | **21** | D | **33** | D | **45** | B | **57** | B | | |
| **10** | A | **22** | Round | **34** | A | **46** | A | **58** | A | | |
| **11** | B | **23** | C | **35** | C | **47** | C | **59** | B | | |
| **12** | D | **24** | A | **36** | C | **48** | A | **60** | B | | |

---

## 📊 Question Frequency & Repetition Analysis Table

| Q# | Question Topic / Core Concept | Answer | Repetition Count | Test Occurrences / Source Takes |
|:---|:------------------------------|:------:|:----------------:|:--------------------------------|
| **1-68** | Complete Cryptography Basics | Various | **1x** | Bayat's Take (Q1-Q68) |

---

## Exam Questions & Detailed Solutions

### 1. Which of the following is classified as an active attack?
- A. Traffic analysis
- B. Wiretapping
- C. Denial of service
- D. Release of message contents

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Denial of service**

*Intuition:* An **active attack** involves an attacker directly altering, modifying, or disrupting system operations, data, or network availability (e.g., Denial of Service, message modification, replay attacks, spoofing). Passive attacks (such as Traffic Analysis, Wiretapping, and Release of message contents) involve monitoring or eavesdropping on transmissions without altering data or affecting system state.
</details>

---

### 2. Counter (CTR) mode is popular in high-speed applications mainly because it allows:
- A. Parallel encryption and decryption of blocks
- B. Operation without an initialization vector
- C. Unlimited key reuse
- D. Sequential-only processing

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Parallel encryption and decryption of blocks**

*Intuition:* **CTR (Counter) mode** turns a block cipher into a stream cipher by encrypting a unique counter value concatenated with a nonce ($E_K(\text{Nonce} \parallel i)$). Because each block's key stream generation is completely independent of previous plaintext or ciphertext blocks, encryption and decryption of multiple blocks can occur simultaneously in parallel pipelines, making it extremely fast for high-speed protocols (e.g., IPsec, TLS 1.3).
</details>

---

### 3. The ____ mode of operation converts a block cipher into a self-synchronizing stream cipher by feeding ciphertext back into the encryption function. (Fill in the blank)
*Answer:* **Cipher Feedback (CFB)**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Cipher Feedback (CFB)**

*Intuition:* **Cipher Feedback (CFB) mode** converts a block cipher into a self-synchronizing stream cipher by encrypting the preceding ciphertext block and XORing the output with the current plaintext block. Because decryption depends only on the preceding $b$ bits of received ciphertext, any bit errors or lost bits in transit automatically self-synchronize after a full block length of valid ciphertext is received.
</details>

---

### 4. The ____ attack on double encryption reduces its effective security roughly to that of single encryption by storing intermediate results. (Fill in the blank)
*Answer:* **meet-in-the-middle**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **meet-in-the-middle**

*Intuition:* A **meet-in-the-middle attack** targets double encryption ($C = E_{K_2}(E_{K_1}(P))$) by encrypting $P$ under all possible first keys $K_1$ and storing intermediate values $X = E_{K_1}(P)$ in a hash table, while decrypting $C$ under all possible second keys $K_2$ to find matches where $D_{K_2}(C) = X$. This space-time tradeoff reduces time complexity from $O(2^{2n})$ to $O(2^{n+1})$ operations, rendering double encryption (like 2DES) virtually no more secure than single encryption.
</details>

---

### 5. Fermat's Little Theorem and Euler's Theorem are foundational to the correctness of the ____ public-key algorithm. (Fill in the blank)
*Answer:* **RSA**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **RSA**

*Intuition:* **RSA** public-key encryption depends directly on Euler's Totient Theorem ($m^{\phi(n)} \equiv 1 \pmod n$) and Fermat's Little Theorem. In RSA, keys are selected such that $e \cdot d \equiv 1 \pmod{\phi(n)}$, ensuring that decryption reverses encryption: $c^d \equiv (m^e)^d = m^{1 + k\phi(n)} \equiv m \pmod n$.
</details>

---

### 6. The Vigenère cipher is an example of a:
- A. Polyalphabetic cipher
- B. Product cipher
- C. Transposition cipher
- D. Monoalphabetic cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Polyalphabetic cipher**

*Intuition:* The **Vigenère cipher** is a polyalphabetic substitution cipher that uses a repeating keyword to apply distinct Caesar cipher shifts to sequential characters. Because the substitution rule changes per character position based on key letters, it flattens simple single-letter frequency distributions.
</details>

---

### 7. An encryption scheme is said to be "computationally secure" if:
- A. It uses a 1000-bit key
- B. It has never been publicly attacked
- C. It requires no key at all
- D. The cost or time of breaking it exceeds the value or useful lifetime of the information

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The cost or time of breaking it exceeds the value or useful lifetime of the information**

*Intuition:* An encryption scheme is **computationally secure** (practical security) if the best-known cryptanalytic attack requires an infeasible volume of computing resources (time, money, hardware, energy) relative to either the commercial/military value of the data or the time duration for which the data must remain confidential.
</details>

---

### 8. Which cryptanalytic technique uses linear approximations of a cipher's operation to recover key bits?
- A. Linear cryptanalysis
- B. Timing analysis
- C. Differential cryptanalysis
- D. Meet-in-the-middle attack

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Linear cryptanalysis**

*Intuition:* **Linear cryptanalysis** is a known-plaintext attack that constructs high-probability linear approximations (XOR relationships) between plaintext, ciphertext, and key bits. By analyzing a high volume of plaintext-ciphertext pairs, statistical deviations from random behavior reveal bits of the secret key.
</details>

---

### 9. Fermat's Little Theorem states that if p is prime and a is not divisible by p, then:
- A. a^p is congruent to a (mod p)
- B. a^(p-1) is congruent to 1 (mod p)
- C. a is congruent to p (mod a)
- D. a^p is congruent to 0 (mod p)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. a^(p-1) is congruent to 1 (mod p)**

*Intuition:* Fermat's Little Theorem states that for any prime $p$ and integer $a$ coprime to $p$, the relation $a^{p-1} \equiv 1 \pmod p$ holds. Multiplying both sides by $a$ yields the alternate form $a^p \equiv a \pmod p$, which holds for all integers $a$, but option B is the exact direct expression under the condition that $a$ is not divisible by $p$.
</details>

---

### 10. Which mode of block cipher operation encrypts blocks independently without chaining, so identical plaintext blocks produce identical ciphertext blocks?
- A. ECB
- B. CBC
- C. CTR
- D. CFB

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. ECB**

*Intuition:* **ECB (Electronic Codebook)** mode encrypts each block independently using the same key. Because there is no feedback or chaining between blocks, identical plaintext blocks encrypt to identical ciphertext blocks, leaking structural patterns of the plaintext.
</details>

---

### 11. RC4 is best described as a:
- A. Public-key algorithm
- B. Stream cipher
- C. Hash function
- D. Block cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Stream cipher**

*Intuition:* **RC4** is a symmetric stream cipher that generates a pseudo-random keystream on a byte-by-byte basis which is then XORed with the plaintext. It does not operate on large fixed-size blocks (unlike AES or DES) and does not use asymmetric key pairs.
</details>

---

### 12. Which block cipher mode turns a block cipher into a self-synchronizing stream-like cipher via ciphertext feedback, avoiding the need for padding?
- A. None of these
- B. ECB
- C. CBC
- D. Cipher Feedback (CFB)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Cipher Feedback (CFB)**

*Intuition:* **CFB (Cipher Feedback)** mode feeds the generated ciphertext segment back into the cipher shift register to produce the keystream for the next segment. It operates on arbitrary segment sizes (like bytes or bits) without requiring block padding, and recovers from transmission errors after receiving a full block of valid ciphertext.
</details>

---

### 13. Euler's totient function phi(n) counts:
- A. The divisors of n
- B. All integers less than n
- C. The prime factors of n
- D. The positive integers less than n that are relatively prime to n

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The positive integers less than n that are relatively prime to n**

*Intuition:* Euler's totient function $\phi(n)$ counts the cardinality of the multiplicative group of integers modulo $n$, which corresponds to the number of positive integers $k < n$ such that $\gcd(k, n) = 1$.
</details>

---

### 14. A cipher in which plaintext bits or letters are rearranged without changing their values is called a ____ cipher. (Fill in the blank)
*Answer:* **transposition**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **transposition**

*Intuition:* A **transposition cipher** performs a permutation of plaintext elements (moving letters or bits to different positions) without changing their actual values. This contrasts with substitution ciphers, which alter character values.
</details>

---

### 15. Which of the following best defines "computer security" as presented in Stallings' framework?
- A. Physical protection of hardware only
- B. Measures and controls that ensure confidentiality, integrity, and availability of information system assets
- C. Encryption of all stored data
- D. Protection only against unauthorized data access

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Measures and controls that ensure confidentiality, integrity, and availability of information system assets**

*Intuition:* Stallings defines computer security through the core pillars of the **CIA Triad**: Confidentiality (protecting from unauthorized access), Integrity (protecting from unauthorized modification), and Availability (ensuring system/service uptime for authorized users).
</details>

---

### 16. A cipher that replaces each plaintext letter with a fixed, different letter throughout the message is called a:
- A. Rotor cipher
- B. Transposition cipher
- C. Monoalphabetic substitution cipher
- D. Polyalphabetic cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Monoalphabetic substitution cipher**

*Intuition:* A **monoalphabetic substitution cipher** uses a single, fixed mapping (key alphabet) to replace every occurrence of a specific plaintext letter with a corresponding ciphertext letter. Unlike polyalphabetic ciphers, the shift value does not vary by character position.
</details>

---

### 17. The AES SubBytes transformation provides:
- A. Block chaining
- B. Nonlinear byte substitution using an S-box
- C. Key mixing
- D. Diffusion via row shifting

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Nonlinear byte substitution using an S-box**

*Intuition:* In AES, the **SubBytes** transformation uses an S-box constructed from multiplicative inversion in $GF(2^8)$ followed by an affine mapping. This provides the cipher's core **confusion** by introducing nonlinearity, preventing algebraic cryptanalysis.
</details>

---

### 18. Which statement about ECB mode is TRUE?
- A. It is the most secure mode for large messages
- B. It requires no key
- C. It automatically randomizes output
- D. Identical plaintext blocks always produce identical ciphertext blocks, which can leak patterns

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Identical plaintext blocks always produce identical ciphertext blocks, which can leak patterns**

*Intuition:* Because **ECB** mode encrypts each block independently without chaining, a given plaintext block always maps to the same ciphertext block under the same key. This leaks structured information and data patterns (e.g., in images).
</details>

---

### 19. In the Playfair cipher, when two plaintext letters fall in the same row of the matrix, each is replaced by:
- A. The letter above it
- B. The letter to its right, wrapping to the start of the row
- C. The letter below it
- D. The letter diagonally opposite it

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. The letter to its right, wrapping to the start of the row**

*Intuition:* The rules of the **Playfair cipher** state that if two plaintext letters occupy the same row in the 5x5 key matrix, they are replaced by the letters immediately to their right, with the rightmost column wrapping around to the leftmost column.
</details>

---

### 20. Euler's totient function of a prime number p is equal to p minus 1.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* A prime number $p$ has no positive divisors other than $1$ and $p$. Therefore, all positive integers strictly less than $p$ (which total $p-1$) are relatively prime to $p$, meaning $\phi(p) = p - 1$.
</details>

---

### 21. Compared to symmetric encryption, public-key encryption is generally:
- A. Impossible to implement in software
- B. Faster for bulk data encryption
- C. Not used for digital signatures
- D. Computationally slower, so it is often used to encrypt keys rather than bulk data

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Computationally slower, so it is often used to encrypt keys rather than bulk data**

*Intuition:* Asymmetric encryption algorithms (like RSA and ECC) rely on complex number-theoretic operations like modular exponentiation, making them significantly slower than symmetric algorithms (like AES). Consequently, hybrid systems encrypt bulk data symmetrically and encrypt/exchange the symmetric keys asymmetrically.
</details>

---

### 22. In the Feistel cipher structure, the function applied within each round is called the ____ function. (Fill in the blank)
*Answer:* **round**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **round**

*Intuition:* In Feistel networks, the **round function** ($F$) takes the right half of the data block and a round subkey to output a value that is XORed with the left half. The function itself does not need to be invertible.
</details>

---

### 23. The main practical drawback of the one-time pad is:
- A. It is vulnerable to frequency analysis
- B. It cannot encrypt binary data
- C. The difficulty of generating and distributing truly random keys as long as the message
- D. It is easy to cryptanalyze

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The difficulty of generating and distributing truly random keys as long as the message**

*Intuition:* Although the **One-Time Pad** offers perfect information-theoretic security, it requires a key that is truly random, used only once, and equal in length to the plaintext. Distributing and managing keys under these constraints is highly impractical for mass data networks.
</details>

---

### 24. In a Feistel cipher structure, encryption and decryption are:
- A. Essentially identical, with the subkeys used in reverse order for decryption
- B. Impossible to reverse
- C. Completely different algorithms
- D. Only possible with the same key length

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Essentially identical, with the subkeys used in reverse order for decryption**

*Intuition:* The Feistel structure is mathematically designed to be self-reversing. Decryption uses the exact same algorithmic round steps as encryption, with the sole difference being that the round subkeys are applied in reverse sequence (from $K_n$ down to $K_1$).
</details>

---

### 25. DES uses a Feistel structure with 16 rounds of processing.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The Data Encryption Standard (DES) is a classic Feistel cipher that processes 64-bit plaintext blocks through exactly 16 rounds of substitution and permutation using subkeys derived from the master key.
</details>

---

### 26. Triple DES (3DES) with two keys typically uses which encryption sequence?
- A. Decrypt-Decrypt-Decrypt
- B. Encrypt-Encrypt-Encrypt with three different keys
- C. A single DES pass repeated three times with the same key
- D. Encrypt-Decrypt-Encrypt (EDE) using K1, K2, K1

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Encrypt-Decrypt-Encrypt (EDE) using K1, K2, K1**

*Intuition:* Two-key 3DES uses the EDE sequence: $C = E_{K_1}(D_{K_2}(E_{K_1}(P)))$. The decryption stage with $K_2$ enables backward compatibility with single DES if $K_1 = K_2$, while offering an effective 112-bit key strength when $K_1 \neq K_2$.
</details>

---

### 27. The Chinese Remainder Theorem is useful in cryptography chiefly because it:
- A. Allows faster modular exponentiation by working with smaller moduli
- B. Computes discrete logarithms efficiently
- C. Generates prime numbers directly
- D. Breaks RSA encryption

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Allows faster modular exponentiation by working with smaller moduli**

*Intuition:* The **CRT** allows computation modulo a large composite product $n = pq$ to be performed independently modulo the smaller primes $p$ and $q$. This reduces the computational cost of RSA decryption/signing by roughly $4\times$.
</details>

---

### 28. Which AES transformation cyclically shifts the rows of the state array?
- A. AddRoundKey
- B. SubBytes
- C. MixColumns
- D. ShiftRows

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. ShiftRows**

*Intuition:* The **ShiftRows** step in AES cyclically shifts the second, third, and fourth rows of the 4x4 state matrix by 1, 2, and 3 bytes respectively. This ensures bytes from the same column are distributed into different columns in subsequent rounds, facilitating **diffusion**.
</details>

---

### 29. The Playfair cipher encrypts:
- A. Trigrams
- B. Whole words
- C. Digrams (pairs of letters)
- D. Single letters

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Digrams (pairs of letters)**

*Intuition:* **Playfair** is the first practical symmetric digraph substitution cipher. It processes plaintext in 2-letter blocks (digrams) using rules based on their relative coordinates in a 5x5 key matrix.
</details>

---

### 30. The Euclidean algorithm is used primarily to compute:
- A. The greatest common divisor of two integers
- B. Discrete logarithms
- C. The prime factorization of a number
- D. Modular exponentiation directly

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The greatest common divisor of two integers**

*Intuition:* The **Euclidean algorithm** is a highly efficient recursive technique for calculating the Greatest Common Divisor ($\gcd$) of two integers by exploiting the property that $\gcd(a, b) = \gcd(b, a \pmod b)$ until the remainder is zero.
</details>

---

### 31. The Diffie-Hellman protocol allows two parties to:
- A. Compute prime factorizations
- B. Encrypt messages directly without a symmetric cipher
- C. Establish a shared secret key over an insecure channel
- D. Sign documents digitally

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Establish a shared secret key over an insecure channel**

*Intuition:* **Diffie-Hellman (DH)** key exchange enables two parties to securely compute a shared symmetric key over a public network. Its mathematical security is anchored on the computational hardness of the discrete logarithm problem.
</details>

---

### 32. A rail fence cipher is an example of a:
- A. Substitution technique
- B. Transposition technique
- C. Product cipher
- D. Stream cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Transposition technique**

*Intuition:* The **rail fence cipher** writes plaintext characters in a zigzag pattern across multiple imaginary rails and reads them off row-by-row. Because characters are reordered rather than replaced, it is classified as a transposition cipher.
</details>

---

### 33. The "model for network security" presented by Stallings assumes that communicating parties need which two things to counter an opponent?
- A. A router and a switch
- B. A backup system and an encryption key
- C. A firewall and antivirus software
- D. A trusted third party and an appropriate security transformation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A trusted third party and an appropriate security transformation**

*Intuition:* Stallings' security model dictates that to protect a message, the parties must apply a **security transformation** (e.g., encryption) and rely on a **trusted third party** (e.g., KDC/CA) to distribute keys or confirm identities.
</details>

---

### 34. Which of these is classified as a security mechanism rather than a security service under X.800?
- A. Encipherment
- B. Access control
- C. Authentication
- D. Non-repudiation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Encipherment**

*Intuition:* Under X.800, **security services** define the high-level security objectives (e.g., Access Control, Confidentiality), whereas **security mechanisms** (like Encipherment/Encryption or Digital Signatures) are the concrete cryptographic algorithms used to implement those services.
</details>

---

### 35. In the ElGamal public-key cryptosystem, security is based on the difficulty of computing:
- A. Square roots modulo n
- B. Cube roots modulo n
- C. Discrete logarithms in a finite field
- D. Modular inverses only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Discrete logarithms in a finite field**

*Intuition:* The **ElGamal** cryptosystem (used for encryption and signatures) derives its security directly from the difficulty of the discrete logarithm problem in finite fields (or elliptic curve groups).
</details>

---

### 36. Blum Blum Shub (BBS) is an example of a PRNG built on:
- A. The Hill cipher
- B. The Playfair cipher
- C. Number-theoretic quadratic residue problems believed to be computationally hard
- D. The DES algorithm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Number-theoretic quadratic residue problems believed to be computationally hard**

*Intuition:* **Blum Blum Shub (BBS)** is a cryptographically secure pseudorandom number generator (CSPRNG) whose mathematical security is proven to be as hard as integer factorization, specifically using modular quadratic residues.
</details>

---

### 37. A pseudorandom number generator (PRNG) is considered cryptographically secure if:
- A. It passes only basic statistical tests
- B. An adversary cannot practically distinguish its output from true randomness or predict other outputs
- C. It uses a publicly known seed
- D. Its period is shorter than the key length

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. An adversary cannot practically distinguish its output from true randomness or predict other outputs**

*Intuition:* A **CSPRNG** must satisfy the next-bit test (unpredictability) and be indistinguishable from a truly random sequence. Passing standard empirical statistical tests is necessary but not sufficient for cryptographic applications.
</details>

---

### 38. Triple DES using three independent keys effectively provides a key length of 168 bits.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Three-key 3DES utilizes three distinct 56-bit DES keys ($K_1, K_2, K_3$). Thus, the nominal/effective key length is $3 \times 56 = 168$ bits, although the actual cryptographic security level is capped at 112 bits due to meet-in-the-middle attacks.
</details>

---

### 39. True random number generators typically derive entropy from:
- A. Deterministic software algorithms only
- B. The encryption key only
- C. Physical noise sources such as thermal or electronic noise
- D. The plaintext itself

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Physical noise sources such as thermal or electronic noise**

*Intuition:* **TRNGs** harvest entropy from non-deterministic physical phenomena (e.g., thermal noise, avalanche diode noise, or radioactive decay) to guarantee that outputs cannot be mathematically predicted or reproduced.
</details>

---

### 40. In modular exponentiation, the "square-and-multiply" algorithm improves efficiency by:
- A. Reducing the number of multiplications needed to compute a^k mod n
- B. Avoiding multiplication altogether
- C. Using only addition operations
- D. Working exclusively with small primes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Reducing the number of multiplications needed to compute a^k mod n**

*Intuition:* The **square-and-multiply** algorithm reduces the time complexity of computing $a^k \pmod n$ from linear $O(k)$ to logarithmic $O(\log k)$ operations by scanning the binary representation of the exponent $k$.
</details>

---

### 41. Elliptic curve cryptography (ECC) is attractive because it can achieve security comparable to RSA with:
- A. Significantly smaller key sizes
- B. No underlying mathematical hard problem
- C. No public key at all
- D. Larger key sizes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Significantly smaller key sizes**

*Intuition:* Because the Elliptic Curve Discrete Logarithm Problem (ECDLP) is significantly harder to solve than RSA integer factorization, ECC provides equivalent security with far smaller keys (e.g., 256-bit ECC is comparable to 3072-bit RSA), reducing processing overhead.
</details>

---

### 42. What is the main weakness that makes monoalphabetic substitution ciphers easy to break?
- A. They require a computer to implement
- B. They preserve the frequency distribution of the underlying language
- C. A very small key space only
- D. They cannot encrypt numbers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. They preserve the frequency distribution of the underlying language**

*Intuition:* Because a monoalphabetic cipher replaces every occurrence of a plaintext letter with the exact same ciphertext letter, the underlying statistical frequency of the language (e.g., 'E' being the most common letter in English) is preserved, exposing it to **frequency analysis**.
</details>

---

### 43. Public-key cryptography, unlike symmetric cryptography, uses:
- A. No key at all
- B. A mathematically related key pair, one public and one private
- C. Only a shared secret established in advance
- D. The same key for both encryption and decryption

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A mathematically related key pair, one public and one private**

*Intuition:* Asymmetric systems utilize two distinct keys: a **public key** for encryption/verification and a mathematically linked **private key** for decryption/signing.
</details>

---

### 44. In the Caesar cipher, if the shift key is 3, the plaintext letter 'A' encrypts to:
- A. 'D'
- B. 'C'
- C. 'X'
- D. 'B'

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 'D'**

*Intuition:* The Caesar cipher shifts characters forward by the key value. Shifting 'A' forward by 3 steps ($0 + 3 = 3$) yields 'D' (position 3 in a 0-indexed alphabet).
</details>

---

### 45. A passive attack attempts to alter system resources or affect their normal operation.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Passive attacks (monitoring, traffic analysis) do *not* modify system resources or traffic. An attack that alters resources or interrupts services is classified as an **active attack**.
</details>

---

### 46. The Miller-Rabin test is used for:
- A. Probabilistic primality testing
- B. Factoring large numbers
- C. Computing discrete logarithms
- D. Generating S-boxes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Probabilistic primality testing**

*Intuition:* The **Miller-Rabin** algorithm is a fast probabilistic test used in RSA key generation to verify if a randomly chosen large integer is prime.
</details>

---

### 47. DES operates on plaintext blocks of:
- A. 32 bits
- B. 128 bits
- C. 64 bits
- D. 56 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. 64 bits**

*Intuition:* The Data Encryption Standard (DES) is designed with a fixed block size of 64 bits. It encrypts and decrypts data in 64-bit segments.
</details>

---

### 48. The effective key length used by DES for encryption is:
- A. 56 bits
- B. 48 bits
- C. 64 bits
- D. 128 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 56 bits**

*Intuition:* Although a DES key is represented as 64 bits, 8 of those bits are used exclusively as parity bits for error detection. The cryptographic strength of DES rests solely on the remaining 56 bits.
</details>

---

### 49. In the context of security attacks, which category includes eavesdropping and traffic analysis?
- A. Replay attacks
- B. Masquerade attacks
- C. Active attacks
- D. Passive attacks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Passive attacks**

*Intuition:* **Passive attacks** involve eavesdropping and traffic analysis, as they monitor data streams without modifying contents or injecting malicious traffic.
</details>

---

### 50. The "period" of a pseudorandom generator refers to:
- A. The number of rounds
- B. The length of the seed
- C. The block size
- D. The length of the sequence before it starts repeating

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The length of the sequence before it starts repeating**

*Intuition:* Since PRNGs are finite-state deterministic machines, their outputs eventually repeat. The **period** is the length of the pseudorandom sequence generated before it enters a repeating loop.
</details>

---

### 51. A key advantage of the Feistel structure is that:
- A. The same hardware or software can be used for both encryption and decryption
- B. It requires two different algorithms for encryption and decryption
- C. It cannot use a round function
- D. It only works with 64-bit blocks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The same hardware or software can be used for both encryption and decryption**

*Intuition:* Because the Feistel structure is self-reversing, the exact same hardware/software block execution paths are reused for both encryption and decryption, only requiring the subkeys to be supplied in reverse order.
</details>

---

### 52. A brute-force attack on an encryption algorithm involves:
- A. Intercepting the key during exchange
- B. Trying every possible key until the correct one is found
- C. Guessing the plaintext based on context
- D. Exploiting mathematical weaknesses in the algorithm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Trying every possible key until the correct one is found**

*Intuition:* A **brute-force attack** is an exhaustive key search that tests every possible key combination in the keyspace until the correct key recovers legible plaintext.
</details>

---

### 53. In block cipher design, "confusion" as described by Shannon aims to:
- A. Make the relationship between the key and ciphertext as complex as possible
- B. Increase the block size
- C. Spread plaintext statistics through the ciphertext
- D. Reduce the number of rounds needed

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Make the relationship between the key and ciphertext as complex as possible**

*Intuition:* **Confusion** obscures the relationship between the encryption key and the ciphertext, usually implemented via S-boxes, so that attackers cannot deduce key bits even if they analyze plaintext/ciphertext pairs.
</details>

---

### 54. Cipher Block Chaining (CBC) mode XORs each plaintext block with:
- A. The previous ciphertext block before encryption
- B. A fixed nonce only
- C. The secret key
- D. The next plaintext block

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The previous ciphertext block before encryption**

*Intuition:* **CBC** mode chains blocks by XORing each plaintext block with the preceding ciphertext block ($C_{i-1}$) before feeding it to the block cipher, ensuring that duplicate plaintext blocks produce different ciphertexts.
</details>

---

### 55. In modular arithmetic, what is 17 mod 5?
- A. 2
- B. 5
- C. 12
- D. 3

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 2**

*Intuition:* $17 \pmod 5$ finds the remainder of $17$ divided by $5$. Since $5 \times 3 = 15$, the remainder is $17 - 15 = 2$.
</details>

---

### 56. The one-time pad remains perfectly secure even if the same key is reused for multiple messages.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Reusing a one-time pad key results in the "two-time pad" vulnerability. An attacker can XOR the two ciphertexts together ($C_1 \oplus C_2 = P_1 \oplus P_2$), removing the key entirely and exposing the plaintexts to frequency analysis.
</details>

---

### 57. The discrete logarithm problem is considered computationally hard because:
- A. It requires floating-point precision
- B. Given g, p, and g^x mod p, finding x is infeasible for large p
- C. Multiplication is undefined in modular arithmetic
- D. Addition modulo n is difficult to perform

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Given g, p, and g^x mod p, finding x is infeasible for large p**

*Intuition:* The **Discrete Logarithm Problem (DLP)** is the one-way mathematical function where computing modular exponentiation ($y = g^x \pmod p$) is easy, but reversing it to find $x$ is computationally infeasible for sufficiently large primes $p$.
</details>

---

### 58. In the RSA algorithm, the public key consists of:
- A. The exponent e and modulus n
- B. Only the modulus n
- C. The private exponent d and modulus n
- D. The two secret primes p and q

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The exponent e and modulus n**

*Intuition:* In RSA, the public key used for encryption or signature verification consists of the public exponent $e$ and the modulus $n$ ($n = pq$).
</details>

---

### 59. AES with a 128-bit key uses how many rounds?
- A. 14
- B. 10
- C. 12
- D. 8

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 10**

*Intuition:* The number of rounds in AES is determined by key length: 10 rounds for a 128-bit key, 12 rounds for a 192-bit key, and 14 rounds for a 256-bit key.
</details>

---

### 60. RSA's security is based primarily on the difficulty of computing discrete logarithms.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* RSA's mathematical security is based on the **integer factorization problem** (factoring a large composite number $n$ into its prime factors $p$ and $q$), not discrete logarithms.
</details>

---

### 61. AES supports key lengths of:
- A. 56 bits only
- B. 128, 192, or 256 bits
- C. Only 128 bits
- D. 64 or 128 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 128, 192, or 256 bits**

*Intuition:* The Advanced Encryption Standard (AES) specifies three supported key sizes: 128 bits, 192 bits, and 256 bits, all sharing a fixed 128-bit block size.
</details>

---

### 62. Double DES is largely negated in its expected security improvement by which attack?
- A. Differential cryptanalysis
- B. Meet-in-the-middle attack
- C. Birthday attack
- D. Frequency analysis

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Meet-in-the-middle attack**

*Intuition:* The **meet-in-the-middle attack** reduces the security of Double DES from a theoretical 112 bits down to an effective 57 bits of security by computing and storing intermediate values from both ends of the double cipher.
</details>

---

### 63. AES, selected by NIST to replace DES, operates on a block size of:
- A. 256 bits
- B. 128 bits
- C. 64 bits
- D. 192 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 128 bits**

*Intuition:* AES operates on a fixed block size of 128 bits (16 bytes) organized as a 4x4 state array, replacing DES's smaller 64-bit block size.
</details>

---

### 64. Stream ciphers, like block ciphers, always process plaintext in large fixed-size blocks.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Stream ciphers generate a continuous keystream to encrypt plaintext bit-by-bit or byte-by-byte, whereas block ciphers require parsing data in fixed-size blocks (e.g., 64 or 128 bits) with padding.
</details>

---

### 65. The main criticism of DES that eventually led to its replacement was:
- A. It only worked on ASCII text
- B. Its 56-bit key length is vulnerable to brute-force attack
- C. Its block size was too large
- D. It could not be implemented in hardware

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Its 56-bit key length is vulnerable to brute-force attack**

*Intuition:* DES's 56-bit keyspace ($2^{56}$ options) became vulnerable to brute-force key exhaustive searches by custom hardware crackers in the late 1990s, forcing the migration to AES.
</details>

---

### 66. An initialization vector (IV) is used in most chaining modes primarily to:
- A. Authenticate the sender
- B. Replace the secret key
- C. Compress the plaintext
- D. Ensure that identical plaintexts encrypted with the same key produce different ciphertexts

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Ensure that identical plaintexts encrypted with the same key produce different ciphertexts**

*Intuition:* The **Initialization Vector (IV)** randomizes the first encryption block, preventing duplicate messages from yielding identical ciphertext blocks, defending against pattern analysis.
</details>

---

### 67. Availability, as a security objective, means:
- A. Information is disclosed only to authorized parties
- B. Data cannot be altered improperly
- C. Systems work promptly and service is not denied to authorized users
- D. Data origin can be verified

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Systems work promptly and service is not denied to authorized users**

*Intuition:* **Availability** ensures that systems, services, and data are promptly accessible and functional for authorized users whenever needed.
</details>

---

### 68. "Diffusion" in a block cipher refers to:
- A. Dissipating the statistical structure of plaintext over the bulk of the ciphertext
- B. Reducing the avalanche effect
- C. Encrypting with multiple keys simultaneously
- D. Making the statistical relationship between key and ciphertext complex

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Dissipating the statistical structure of plaintext over the bulk of the ciphertext**

*Intuition:* **Diffusion** spreads the influence of single plaintext or key bits across multiple output bits (e.g., via ShiftRows and MixColumns), hiding plaintext statistical redundancy in the ciphertext.
</details>

---
