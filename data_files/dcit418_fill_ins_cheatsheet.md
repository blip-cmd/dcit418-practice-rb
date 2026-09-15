# DCIT 418: Systems and Network Security
## Master Fill-in-the-Blank & Terminology Cheatsheet (Chapters 1 – 13)
**Textbook Reference:** William Stallings, *Cryptography and Network Security: Principles and Practice*  
**Course Code:** DCIT 418 | **Credits:** 3 Credits  
**Scope:** Chapters 1 through 13 (Concepts, Terminology, Fill-in Blanks, Phrases, and Acronyms — *Zero Calculations*)

---

## 📌 Cheatsheet Guide & Exam Strategy
This cheatsheet is engineered specifically for **Fill-in-the-Blank** and **High-Yield Terminology** questions in DCIT 418.
- **Single-Word Fill-ins:** Core nouns and primitives (e.g., *State*, *confusion*, *diffusion*, *keystream*, *tweak*, *nonce*, *Adleman*, *Rijndael*).
- **Double-Word Fill-ins:** Standard compound terminology (e.g., *avalanche effect*, *primitive root*, *discrete logarithm*, *timing attack*, *Feistel cipher*, *one-time pad*).
- **Multi-Word & Phrases:** Formal theorems, modes, and criteria (e.g., *Strict Avalanche Criterion*, *Optimal Asymmetric Encryption Padding*, *Fundamental Theorem of Arithmetic*).
- **Acronyms:** Every standard cryptographic abbreviation decoded with its official textbook expansion.
- **Fixed Numerical Constants:** Memorized block sizes, bit lengths, and round counts that appear as fill-ins without manual calculation.

---

## 🔤 Comprehensive Master Acronym Directory (Chapters 1 – 13)

| Acronym | Full Expansion | Core Definition / Exam Context | Chapter |
| :--- | :--- | :--- | :---: |
| **CIA** | **Confidentiality, Integrity, Availability** | The foundational triad of computer and information security. | 1 |
| **OSI** | **Open Systems Interconnection** | ISO 7498-2 security architecture standardizing security services and mechanisms. | 1 |
| **DOS / DDoS** | **Denial of Service / Distributed Denial of Service** | An attack on system **availability** preventing legitimate user access. | 1 |
| **DES** | **Data Encryption Standard** | Symmetric block cipher developed by IBM/NBS (64-bit block, 56-bit key, 16 rounds). | 3 |
| **SPN** | **Substitution-Permutation Network** | Cipher architecture alternating layers of S-boxes (confusion) and P-boxes (diffusion). | 3, 5 |
| **SAC** | **Strict Avalanche Criterion** | Output bit changes with probability $0.5$ when any single input bit is inverted. | 3 |
| **BIC** | **Bit Independence Criterion** | Output bits $j$ and $k$ change independently when any single input bit is inverted. | 3 |
| **IP / $IP^{-1}$** | **Initial Permutation / Inverse Initial Permutation** | The first and last transposition stages of the Data Encryption Standard (DES). | 3 |
| **AES** | **Advanced Encryption Standard** | NIST FIPS 197 standard based on Rijndael (128-bit block, 128/192/256-bit keys). | 5 |
| **NIST** | **National Institute of Standards and Technology** | US federal agency that organized the open competitions for DES, AES, and SHA-3. | 3, 5, 11 |
| **FIPS** | **Federal Information Processing Standard** | Official US government cryptographic publication standard (e.g., FIPS 46-3, 197, 180, 186). | 3, 5, 11 |
| **ECB** | **Electronic Codebook** | Each 64/128-bit plaintext block is encrypted independently with the exact same key. | 6 |
| **CBC** | **Cipher Block Chaining** | Each plaintext block is XORed with the previous ciphertext block before encryption. | 6 |
| **CFB** | **Cipher Feedback** | Converts a block cipher into a stream cipher; feeds ciphertext blocks back into the cipher. | 6 |
| **OFB** | **Output Feedback** | Feeds block cipher encryption output directly into the next stage; keystream independent of message. | 6 |
| **CTR** | **Counter (Mode)** | Encrypts a sequence of incrementing counter values to produce a keystream; fully parallelizable. | 6 |
| **IV** | **Initialization Vector** | A random or nonce data block used to ensure identical plaintexts produce different ciphertexts. | 6 |
| **3DES / TDEA** | **Triple DES / Triple Data Encryption Algorithm** | Encrypt-Decrypt-Encrypt ($EDE$) scheme using 2 or 3 keys to defeat Meet-in-the-Middle attacks. | 6 |
| **PRNG** | **Pseudorandom Number Generator** | A deterministic algorithm using a fixed seed to produce statistically random-looking bit streams. | 7 |
| **TRNG** | **True Random Number Generator** | Generates non-deterministic, non-periodic numbers from physical entropy sources (e.g., thermal noise). | 7 |
| **PRF** | **Pseudorandom Function** | Takes a secret key and a fixed-length seed to output a fixed-length pseudorandom output block. | 7 |
| **CSPRNG** | **Cryptographically Secure PRNG** | A PRNG that satisfies both forward and backward unpredictability under adversary observation. | 7 |
| **LCG** | **Linear Congruential Generator** | Simple generator $X_{n+1} = (aX_n + c) \bmod m$; statistically uniform but cryptographically predictable. | 7 |
| **BBS** | **Blum Blum Shub** | Provably secure CSPRNG based on the hardness of integer factorization ($x_{i+1} = x_i^2 \bmod n$). | 7, 10 |
| **KSA** | **Key Scheduling Algorithm** | The phase in RC4 that initializes and permuates the 256-byte state array $S$ using the secret key. | 7 |
| **PRGA** | **Pseudo-Random Generation Algorithm** | The phase in RC4 that continuously swaps bytes in array $S$ to output the keystream bytes. | 7 |
| **CRT** | **Chinese Remainder Theorem** | Reconstructs a unique integer modulo $M = \prod m_i$ from its residues modulo pairwise coprime $m_i$. | 8 |
| **DLP** | **Discrete Logarithm Problem** | Finding $x$ given $y = g^x \bmod p$; computationally infeasible for large prime moduli. | 8, 10 |
| **AKS** | **Agrawal–Kayal–Saxena** | The 2002 unconditional, deterministic, polynomial-time algorithm for proving primality. | 8 |
| **RSA** | **Rivest, Shamir, Adleman** | Public-key cryptosystem (1977) whose security rests on the hardness of integer factorization. | 9 |
| **OAEP** | **Optimal Asymmetric Encryption Padding** | Feistel-based padding scheme adding randomness to plaintext before RSA to defeat CCA2. | 9 |
| **CCA / CCA2** | **Chosen Ciphertext Attack (Adaptive)** | Cryptanalytic model where the attacker chooses ciphertexts and analyzes resulting plaintexts. | 9 |
| **DH** | **Diffie-Hellman** | First public-key protocol (1976) allowing two parties to establish a shared secret key. | 10 |
| **MITM** | **Meet-in-the-Middle / Man-in-the-Middle** | Block cipher attack against 2DES ($2^{56}$ steps) OR protocol interception on unauthenticated DH. | 6, 10 |
| **ECC** | **Elliptic Curve Cryptography** | Public-key scheme based on the algebraic structure of elliptic curves over finite fields. | 10 |
| **ECDLP** | **Elliptic Curve Discrete Logarithm Problem** | Given base point $P$ and $Q = kP$, finding the scalar multiplier $k$. | 10 |
| **ECDH** | **Elliptic Curve Diffie-Hellman** | Key agreement protocol using elliptic curve point multiplication ($K = k_A \cdot Q_B$). | 10 |
| **SHA** | **Secure Hash Algorithm** | Family of cryptographic hash functions standardized by NIST (SHA-1, SHA-2, SHA-3). | 11 |
| **MAC** | **Message Authentication Code** | A cryptographic checksum generated using a secret key to ensure message integrity and authenticity. | 12 |
| **HMAC** | **Keyed-Hash Message Authentication Code** | MAC constructed by wrapping any cryptographic hash function (using $ipad$ and $opad$ byte constants). | 12 |
| **DAA** | **Data Authentication Algorithm** | Early ANSI MAC standard based on DES in CBC mode with a fixed IV of zero. | 12 |
| **CMAC** | **Cipher-Based Message Authentication Code** | NIST-approved block-cipher MAC mode resolving DAA's variable-length message extension weakness. | 12 |
| **CCM** | **Counter with CBC-MAC** | NIST authenticated encryption mode combining CTR mode (encryption) with CBC-MAC (integrity). | 12 |
| **GCM** | **Galois/Counter Mode** | High-throughput authenticated encryption mode combining CTR encryption with Galois field GHASH. | 12 |
| **DSA / DSS** | **Digital Signature Algorithm / Standard** | NIST FIPS 186 public-key signature standard based on discrete logarithms in sub-groups. | 13 |
| **ECDSA** | **Elliptic Curve Digital Signature Algorithm** | Elliptic curve analog of DSA providing equal security with significantly shorter signatures and keys. | 13 |
| **PSS** | **Probabilistic Signature Scheme** | Provably secure signature encoding standard for RSA (RSA-PSS) designed by Bellare and Rogaway. | 13 |
| **SSL** | **Secure Sockets Layer** | Netscape security protocol operating between TCP and application layer; predecessor to TLS. | 1, 7 |
| **TLS** | **Transport Layer Security** | IETF standard protocol (RFC 5246/8446) providing channel encryption and authentication over TCP (HTTPS). | 1, 7 |
| **SLS** | **Session Layer Security (or Secure Link Set)** | Security mechanism at OSI Layer 5 / common exam transposition typo for **SSL**. | 1 |

---

## 📖 Chapter-by-Chapter Fill-in-the-Blank Reference Tables

### Chapter 1: Overview & Computer Security Concepts
* **Core Focus:** The CIA Triad, OSI security architecture, attack classifications, security mechanisms, and security services.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| The three fundamental security objectives that form the foundation of information security are ____, ____, and ____. | **Confidentiality, Integrity, Availability** | Triad Phrase | The "CIA Triad". |
| An attack that attempts to learn or make use of information from the system but does not affect system resources is a(n) ____ attack. | **passive** | Single Word | Eavesdropping and traffic analysis; undetectable directly. |
| An attack that attempts to alter system resources or affect their operation is a(n) ____ attack. | **active** | Single Word | Masquerade, replay, modification, denial of service. |
| An active attack where an entity pretends to be a different entity is called a(n) ____. | **masquerade** | Single Word | Attacker assumes the identity of an authorized principal. |
| The passive attack in which an adversary monitors the frequency, length, and origin-destination patterns of encrypted messages is called ____. | **traffic analysis** | Double Word | Works even when payload is completely encrypted. |
| The security service that prevents either sender or receiver from denying having sent or received a transmitted message is ____. | **nonrepudiation** | Single Word | Typically implemented using asymmetric digital signatures. |
| The security goal ensuring that information is accessible and usable upon demand by an authorized entity is ____. | **availability** | Single Word | Defeated by Denial of Service (DoS) attacks. |
| The security property that ensures data has not been altered, destroyed, or inserted in an unauthorized manner is data ____. | **integrity** | Single Word | Verified using hashes, MACs, or digital signatures. |
| ISO 7498-2 defines a systematic framework for security services and mechanisms known as the ____. | **OSI security architecture** | Phrase | Standard model defining services, mechanisms, and attacks. |
| The cryptographic protocol standard that operates between the transport layer (TCP) and application layer to secure web communications (HTTPS) is ____. | **Transport Layer Security (TLS)** | Acronym / Phrase | Standardized by IETF; supersedes Netscape's Secure Sockets Layer (SSL). |
| The historical protocol designed by Netscape in the 1990s to secure web browser transactions before being superseded by TLS is ____. | **Secure Sockets Layer (SSL)** | Acronym / Phrase | Deprecated due to protocol design vulnerabilities (e.g., POODLE). |

---

### Chapter 2: Classical Encryption Techniques
* **Core Focus:** Symmetric cipher model, substitution vs. transposition, cryptanalysis vs. brute force, and classical historical ciphers.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| The original intelligible message fed into an encryption algorithm is called the ____. | **plaintext** | Single Word | Standard input to cipher: $P$ or $M$. |
| The scrambled, unreadable message produced as the output of an encryption algorithm is called the ____. | **ciphertext** | Single Word | Standard output from cipher: $C = E_K(P)$. |
| An encryption scheme where the encryption key and decryption key are identical or easily derived from each other is called ____ encryption. | **symmetric (or conventional / secret-key)** | Single/Double | Single secret key shared between sender and receiver. |
| In a(n) ____ cipher, the letters of the plaintext are replaced by other letters, numbers, or symbols. | **substitution** | Single Word | E.g., Caesar, Playfair, Monoalphabetic, Vigenère. |
| In a(n) ____ cipher, the elements of the plaintext are rearranged in a different order without changing the actual characters. | **transposition (or permutation)** | Single Word | E.g., Rail fence, Row transposition. |
| The ancient substitution cipher that shifts each letter in the plaintext forward by three positions in the alphabet is the ____ cipher. | **Caesar** | Single Word | Key is $k = 3$; formula is $C = (P + 3) \bmod 26$. |
| The first published practical polyalphabetic substitution cipher that uses a repeating keyword to shift letters is the ____ cipher. | **Vigenère** | Single Word | Attacked via Kasiski method or index of coincidence. |
| The only cryptosystem that is mathematically proven to be unconditionally secure (information-theoretically secure) is the ____. | **one-time pad** | Double Word | Key must be truly random, as long as the message, used once. |
| The study of mathematical techniques for attempting to defeat cryptographic techniques without knowing the key is called ____. | **cryptanalysis** | Single Word | Exploits statistical, algebraic, or structural weaknesses. |
| The technique of hiding the very existence of a secret message by embedding it inside an innocuous cover medium (such as an image) is called ____. | **steganography** | Single Word | Contrasted with cryptography (which hides meaning, not existence). |

---

### Chapter 3: Block Ciphers & The Data Encryption Standard (DES)
* **Core Focus:** Feistel network architecture, Shannon's principles of diffusion and confusion, DES internal operations, S-boxes, and permutation tables.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| A cipher that processes an input stream of data continuously, one bit or byte at a time, is classified as a(n) ____ cipher. | **stream** | Single Word | Contrasted with block ciphers; e.g., RC4, A5/1. |
| A cipher that processes an input block of data as a single fixed-size group of bits simultaneously is classified as a(n) ____ cipher. | **block** | Single Word | Typical blocks: 64 bits (DES) or 128 bits (AES). |
| Claude Shannon's principle that spreads the statistical structure of the plaintext across the entire ciphertext is called ____. | **diffusion** | Single Word | Achieved via permutations, transpositions, and bit rotations. |
| Claude Shannon's principle that makes the relationship between the ciphertext and the encryption key as complex as possible is called ____. | **confusion** | Single Word | Achieved via non-linear substitutions (S-boxes). |
| The classic symmetric cipher architecture that splits data into two halves and applies a round function iteratively to one half before swapping is the ____ cipher structure. | **Feistel** | Double Word | Used in DES, Blowfish, CAST-128 (NOT used in AES). |
| The property where a single bit change in the plaintext or key produces a change in approximately half of the ciphertext bits is the ____. | **avalanche effect** | Double Word | Essential design criterion for modern block ciphers. |
| The design criterion requiring that each output bit should invert with probability 0.5 when any single input bit is flipped is the ____. | **Strict Avalanche Criterion (SAC)** | Phrase | Formulated by Webster and Tavares (1986). |
| The standard block length of the Data Encryption Standard (DES) is ____ bits. | **64** | Number | Fixed block size across all DES operations. |
| The effective secret key length used by DES is ____ bits (disregarding parity bits). | **56** | Number | 64 bits total, but 8 bits used for odd parity. |
| The total number of processing rounds executed in DES is ____ rounds. | **16** | Number | Preceded by IP and concluded by 32-bit swap and $IP^{-1}$. |
| In each round of DES, the 32-bit right half is expanded to 48 bits using the ____ table. | **Expansion Permutation (E-box)** | Double Word | Replicates 16 bits so output matches the 48-bit subkey. |
| The only non-linear component in the DES algorithm that provides confusion is the set of ____. | **S-boxes (substitution boxes)** | Single Word | 8 distinct S-boxes; each takes 6 input bits and outputs 4 bits. |
| In timing-attack research on software implementations of DES, measurement of decryption time was found to correlate with the ____ of the secret key (the total count of 1-bits), rather than directly revealing the key itself. | **Hamming weight** | Double Word | Leaks aggregate 1-bit density without identifying exact bit positions. |

---

### Chapter 4: Basic Concepts in Number Theory & Finite Fields
* **Core Focus:** Divisibility, Euclidean algorithm, modular arithmetic, groups, rings, integral domains, fields, and Galois Fields $GF(p)$ and $GF(2^n)$.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| An efficient algorithmic technique for computing the greatest common divisor of two integers without factoring is the ____ algorithm. | **Euclidean** | Single Word | Successive divisions based on $\gcd(a,b) = \gcd(b, a \bmod b)$. |
| Two integers $a$ and $b$ are said to be ____ if their greatest common divisor equals 1. | **relatively prime (or coprime)** | Double Word | $\gcd(a, b) = 1$. |
| A mathematical structure $(G, \cdot)$ that satisfies closure, associativity, identity, and inverse elements is called a(n) ____. | **group** | Single Word | Abstract algebraic structure. |
| A group that additionally satisfies the commutative property ($a \cdot b = b \cdot a$) for all elements is called a(n) ____ group. | **abelian (or commutative)** | Single Word | Named after Niels Henrik Abel; vital in ECC. |
| An algebraic structure with two binary operations (addition and multiplication) in which every nonzero element has a multiplicative inverse is a(n) ____. | **field** | Single Word | Satisfies all arithmetic axioms (addition, multiplication, division). |
| A field that contains a finite number of elements is called a finite field, or a(n) ____ field. | **Galois** | Single Word | Denoted $GF(q)$; order $q$ must be a prime power $p^n$. |
| In the finite field $GF(2^m)$, addition of two field polynomials is performed using the bitwise operation ____. | **XOR (exclusive-OR)** | Single Word | Coefficient addition modulo 2; no carry bits generated. |
| A polynomial $f(x)$ over a field that cannot be factored into the product of two polynomials of lower degree is called a(n) ____ polynomial. | **irreducible (or prime)** | Double Word | Serves as the modulus polynomial for arithmetic in $GF(2^n)$. |
| AES utilizes finite field arithmetic defined over the specific Galois field ____. | **GF(2^8)** | Acronym / Symbol | Elements represented as 8-bit bytes (degree $< 8$). |
| The irreducible polynomial chosen as the modulus for AES finite field multiplication is $m(x) = $ ____. | **x^8 + x^4 + x^3 + x + 1** | Math Expression | In hexadecimal representation: `{01}{1B}`. |

---

### Chapter 5: Advanced Encryption Standard (AES)
* **Core Focus:** Rijndael competition, State matrix, byte substitutions (S-box), ShiftRows, MixColumns, AddRoundKey, and Key Expansion.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| The NIST open competition for AES was won by the cipher originally named ____, designed by Joan Daemen and Vincent Rijmen. | **Rijndael** | Single Word | Selected in Oct 2000; standardized as FIPS 197 in Nov 2001. |
| Unlike DES, AES is structurally classified as a(n) ____ network rather than a Feistel cipher. | **Substitution-Permutation Network (SPN)** | Phrase | Every byte is updated in every round (parallel transformations). |
| The fixed data block length processed by the AES algorithm is always ____ bits. | **128** | Number | Divided into a $4 \times 4$ matrix of 16 bytes. |
| The $4 \times 4$ column-major matrix of 16 bytes that holds intermediate data throughout AES rounds is called the ____. | **State (or State array)** | Single Word | $4$ rows $\times 4$ columns of bytes ($4 \times 4 = 16$ bytes = 128 bits). |
| For key lengths of 128, 192, and 256 bits, AES executes ____, ____, and ____ rounds, respectively. | **10, 12, 14** | Number Sequence | Number of rounds depends solely on the key length. |
| The AES round transformation that performs a non-linear byte-by-byte substitution using an S-box is ____. | **SubBytes** | Single Word | Inverts byte in $GF(2^8)$ then applies an affine transformation. |
| The AES round transformation that cyclically shifts the bytes in the bottom three rows of the State array is ____. | **ShiftRows** | Single Word | Row 0: shift 0; Row 1: shift 1; Row 2: shift 2; Row 3: shift 3. |
| The AES round transformation that treats each column as a four-term polynomial in $GF(2^8)$ and multiplies it by a fixed matrix is ____. | **MixColumns** | Single Word | Provides inter-byte diffusion across columns; omitted in final round. |
| The only round transformation in AES that combines the secret key with the State array is ____. | **AddRoundKey** | Single Word | Bitwise XOR ($\oplus$) of the 128-bit State with the 128-bit round subkey. |
| In AES, the round transformation that is deliberately omitted from the final round is ____. | **MixColumns** | Single Word | Omitted to make decryption symmetrical to encryption. |
| The subroutine in the AES Key Expansion algorithm that cyclically shifts a 4-byte word one byte to the left is called ____. | **RotWord** | Single Word | Part of the $g$-function in key expansion ($[b_0,b_1,b_2,b_3] \rightarrow [b_1,b_2,b_3,b_0]$). |
| The byte value added during AES key expansion to eliminate symmetry across rounds is the ____. | **Round Constant (Rcon)** | Double Word | Word containing $[RC[j], 0x00, 0x00, 0x00]$ in $GF(2^8)$. |

---

### Chapter 6: Block Cipher Operation
* **Core Focus:** Multiple encryption, 3DES, Meet-in-the-Middle, ECB, CBC, CFB, OFB, CTR, XTS-AES, tweak values, and error propagation.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| The cryptanalytic attack that defeats Double DES in $2^{56}$ operations instead of $2^{112}$ by searching from both ends is the ____ attack. | **Meet-in-the-Middle** | Phrase | Discovered by Diffie and Hellman (1977); trades memory for time. |
| To maintain backward compatibility with single DES, Triple DES uses an alternating sequence of three operations known as ____. | **Encrypt-Decrypt-Encrypt (EDE)** | Phrase | $C = E_{K1}(D_{K2}(E_{K1}(P)))$; if $K1 = K2$, it yields standard DES. |
| Triple DES utilizing three independent keys achieves an effective key length of ____ bits. | **168** | Number | 3 × 56 bits; 24 parity bits are discarded from the 192 total raw bits. |
| Triple DES utilizing two independent keys achieves an effective key length of ____ bits. | **112** | Number | 2 × 56 bits; 16 parity bits are discarded from the 128 total raw bits. |
| The simplest block cipher mode where each plaintext block is encrypted independently with the exact same key is ____ mode. | **Electronic Codebook (ECB)** | Acronym / Phrase | Flawed: identical plaintext blocks yield identical ciphertext blocks. |
| The block cipher mode that chains blocks together by XORing each plaintext block with the preceding ciphertext block before encryption is ____ mode. | **Cipher Block Chaining (CBC)** | Acronym / Phrase | Requires an Initialization Vector (IV); sequential encryption. |
| The unpredictable or random block required by CBC and other feedback modes to initialize encryption of the first block is the ____. | **Initialization Vector (IV)** | Double Word | Must be unpredictable/nonce; transmitted in cleartext with ciphertext. |
| The block cipher mode that turns a block cipher into a stream cipher by encrypting a succession of incrementing integers is ____ mode. | **Counter (CTR)** | Acronym / Phrase | High performance: parallelizable encryption/decryption, random access. |
| The block cipher mode designed specifically for protecting stored data on sector-based media (such as hard drives) is ____ mode. | **XTS-AES** | Acronym / Phrase | Standardized in IEEE 1619; uses two keys ($K_1, K_2$) and a tweak. |
| In XTS-AES mode, the sector or block address used to tie encryption to a specific physical storage location is called the ____ value. | **tweak** | Single Word | Prevents replay or relocation of ciphertext sectors across a disk. |
| In ____ mode, a 1-bit transmission error in a ciphertext block corrupts the entire block and inverts the corresponding single bit in the next block. | **Cipher Block Chaining (CBC)** | Acronym / Phrase | Distinctive 2-block error propagation characteristic. |
| In ____ mode, a 1-bit transmission error in the ciphertext corrupts only the corresponding single bit of the decrypted plaintext, with zero error propagation. | **Counter (CTR) / Output Feedback (OFB)** | Acronym / Phrase | Because ciphertext is simply XORed with independent keystream. |

---

### Chapter 7: Pseudorandom Number Generation & Stream Ciphers
* **Core Focus:** TRNG vs PRNG vs PRF, statistical randomness, forward/backward unpredictability, LCG, BBS, keystream reuse attacks, and RC4.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| A generator that uses a non-deterministic physical source of entropy (such as thermal noise or clock drift) to generate numbers is a(n) ____. | **True Random Number Generator (TRNG)** | Acronym / Phrase | Passes statistical tests and is completely unpredictable; slow. |
| A deterministic algorithm that takes a short random input value and expands it into a long sequence of seemingly random bits is a(n) ____. | **Pseudorandom Number Generator (PRNG)** | Acronym / Phrase | Fast and reproducible; periodic; initialized by a secret seed. |
| The secret initial value supplied to a PRNG to determine its output sequence is called the ____. | **seed** | Single Word | Must be generated by a TRNG to be cryptographically secure. |
| The property ensuring that knowledge of previous output bits does not allow an attacker to predict future output bits is ____ unpredictability. | **forward** | Single Word | Essential requirement for cryptographic pseudorandomness. |
| The property ensuring that an adversary who learns the internal state cannot reconstruct the previous seed or prior bits is ____ unpredictability. | **backward** | Single Word | Essential for forward secrecy in PRNG state machines. |
| The classic linear recurrence generator defined by $X_{n+1} = (aX_n + c) \bmod m$ is the ____ generator. | **Linear Congruential Generator (LCG)** | Phrase | Widely used in non-crypto software; cryptographically insecure. |
| The CSPRNG whose security is mathematically proven to rest on the hardness of factoring composite integers $n = pq$ is the ____ generator. | **Blum Blum Shub (BBS)** | Phrase | Outputs the least significant bit ($lsb$) of $x_{i+1} = x_i^2 \bmod n$. |
| In a stream cipher, the pseudo-random bit sequence that is XORed with the plaintext to produce ciphertext is called the ____. | **keystream** | Single Word | Stream cipher equation: $C_i = P_i \oplus K_i$. |
| Reusing the same keystream to encrypt two different plaintexts allows an eavesdropper to compute $C_1 \oplus C_2 = $ ____. | **P_1 ⊕ P_2 (XOR of plaintexts)** | Math / Phrase | Keystream cancels out completely; fatal two-time pad flaw. |
| The widely used stream cipher designed by Ron Rivest in 1987 based on byte-wide permutations is ____. | **RC4** | Acronym / Name | Variable key size (8 to 2048 bits); byte-oriented state array of 256 bytes. |
| In RC4, the algorithm that uses the secret key to initialize and permute the 256-byte array $S$ is the ____. | **Key Scheduling Algorithm (KSA)** | Acronym / Phrase | Initializes $S[i] = i$ then swaps based on key bytes. |
| In RC4, the algorithm that generates the output keystream bytes by continuously updating indices $i$ and $j$ is the ____. | **Pseudo-Random Generation Algorithm (PRGA)**| Acronym / Phrase | Generates byte $K = S[(S[i] + S[j]) \bmod 256]$. |
| The early wireless security standard whose flawed IV reuse and concatenation with RC4 exposed it to the FMS attack was ____. | **Wired Equivalent Privacy (WEP)** | Acronym / Phrase | 24-bit IV space caused rapid keystream reuse over 802.11 Wi-Fi. |

---

### Chapter 8: Number Theory (Primes, Theorems & Primality Testing)
* **Core Focus:** Prime numbers, Fundamental Theorem of Arithmetic, Fermat's Little Theorem, Euler's Totient, Miller-Rabin, AKS, CRT, and Discrete Logarithms.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| The theorem stating that every integer greater than 1 can be factored uniquely as a product of prime numbers is the ____. | **Fundamental Theorem of Arithmetic** | Phrase | Unique prime factorization theorem. |
| Fermat's Little Theorem states that if $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv$ ____ $\pmod p$. | **1** | Number | Key theorem underlying public-key cryptography and primality tests. |
| An alternate formulation of Fermat's Little Theorem valid for all integers $a$ states that $a^p \equiv$ ____ $\pmod p$. | **a** | Symbol | Valid even when $a$ is a multiple of $p$. |
| The arithmetic function that counts the number of positive integers less than $n$ that are relatively prime to $n$ is ____. | **Euler's totient function (or phi function, $\phi(n)$)** | Phrase | For prime $p$, $\phi(p) = p - 1$; for $n = pq$, $\phi(n) = (p-1)(q-1)$. |
| Euler's generalization of Fermat's Little Theorem states that for any coprime integers $a$ and $n$, $a^{\phi(n)} \equiv$ ____ $\pmod n$. | **1** | Number | $a^{\phi(n)} \equiv 1 \pmod n$. |
| The widely used probabilistic primality test that determines if an odd integer is composite with error probability at most $(1/4)^k$ is the ____ test. | **Miller-Rabin** | Double Word | Based on properties of square roots of 1 modulo an odd prime. |
| The breakthrough 2002 algorithm that proved primality could be determined with certainty in polynomial time is the ____ algorithm. | **AKS (Agrawal–Kayal–Saxena)** | Acronym / Name | First deterministic, unconditional, polynomial-time primality test. |
| The classical mathematical theorem that solves for a unique integer modulo $M$ from its simultaneous remainders modulo coprime factors is the ____. | **Chinese Remainder Theorem (CRT)** | Phrase | Speeds up RSA private key operations ($d \bmod p$ and $d \bmod q$). |
| An integer $g$ whose powers modulo $p$ generate every non-zero integer in the range $1$ to $p-1$ is called a(n) ____ of $p$. | **primitive root (or generator)** | Double Word | Generates the cyclic multiplicative group $\mathbb{Z}_p^*$. |
| The problem of finding the exponent $x$ such that $y \equiv g^x \pmod p$ given $g, y,$ and $p$ is the ____ problem. | **Discrete Logarithm Problem (DLP)** | Phrase | The computational hardness assumption underlying Diffie-Hellman and ElGamal. |

---

### Chapter 9: Public-Key Cryptography & RSA
* **Core Focus:** Asymmetric principles, trapdoor one-way functions, RSA key generation, encryption, decryption, attacks, timing attacks, and OAEP.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| Public-key cryptography was publicly introduced in 1976 by researchers ____ and ____. | **Whitfield Diffie and Martin Hellman** | Names | Published in seminal paper "New Directions in Cryptography". |
| A mathematical function $f$ that is easy to compute in one direction but computationally infeasible to invert unless special auxiliary information is known is a(n) ____ function. | **trapdoor one-way** | Phrase | The trapdoor is the private key; without it, inversion is intractable. |
| In public-key encryption, encryption is performed using the recipient's ____ key, and decryption is performed using the recipient's ____ key. | **public, private** | Double Term | Provides confidentiality (secrecy). |
| In a digital signature, the sender signs the message using their own ____ key, and any receiver verifies it using the sender's ____ key. | **private, public** | Double Term | Provides authentication and non-repudiation. |
| RSA was developed in 1977 at MIT by Ron Rivest, Adi Shamir, and Leonard ____. | **Adleman** | Single Word | The three letters R-S-A represent their initials. |
| In RSA key generation, the public modulus $n$ is calculated as the product of two large prime numbers, $n = $ ____. | **p * q (or pq)** | Math Formula | Factoring $n$ back into $p$ and $q$ breaks the entire system. |
| In RSA key generation, the relationship between public exponent $e$ and private exponent $d$ is defined by the congruence ____. | **e * d ≡ 1 (mod φ(n))** | Math Formula | $d$ is the multiplicative inverse of $e$ modulo $\phi(n) = (p-1)(q-1)$. |
| In the RSA algorithm, encryption of plaintext $M$ to ciphertext $C$ is computed as $C = $ ____. | **M^e mod n** | Math Formula | Computed efficiently via square-and-multiply modular exponentiation. |
| In the RSA algorithm, decryption of ciphertext $C$ to recover plaintext $M$ is computed as $M = $ ____. | **C^d mod n** | Math Formula | Requires the secret exponent $d$. |
| The side-channel attack discovered by Paul Kocher that infers private key bits by observing variations in decryption duration is a(n) ____ attack. | **timing** | Single Word | Countered by constant-time algorithms or cryptographic blinding. |
| In square-and-multiply modular exponentiation used in RSA, execution time and power consumption directly correlate with the ____ of the private exponent d (total count of 1-bits). | **Hamming weight** | Double Word | Each 1-bit requires an extra modular multiplication step. |
| The padding scheme standardized in PKCS#1 v2 that adds structured randomness to plaintext before RSA encryption to defeat chosen-ciphertext attacks is ____. | **Optimal Asymmetric Encryption Padding (OAEP)** | Acronym / Phrase | Uses two hash functions and a random seed in a two-round Feistel network. |

---

### Chapter 10: Other Public-Key Cryptosystems
* **Core Focus:** Diffie-Hellman key exchange, ElGamal cryptosystem, Elliptic Curve Cryptography (ECC), Abelian group on elliptic curves, and ECDLP.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| The first public-key key agreement algorithm published in 1976 to allow two parties to create a shared secret over an insecure channel is ____. | **Diffie-Hellman key exchange** | Phrase | Based on the hardness of discrete logarithms. |
| In Diffie-Hellman, if user A has private key $X_A$ and public key $Y_A = \alpha^{X_A} \bmod q$, the shared secret key $K$ established with user B is calculated as $K = $ ____. | **Y_B^(X_A) mod q (or α^(X_A * X_B) mod q)** | Math Formula | Both sides compute the identical value without transmitting it. |
| The fatal vulnerability of basic, unauthenticated Diffie-Hellman key exchange is its susceptibility to a(n) ____ attack. | **Man-in-the-Middle (MITM)** | Phrase | Attacker intercepts public keys and establishes separate keys with each party. |
| The public-key cryptosystem based directly on the Diffie-Hellman discrete logarithm problem that encrypts messages using an ephemeral random key $k$ is the ____ cryptosystem. | **ElGamal** | Single Word | Designed by Taher Elgamal in 1985. |
| In the ElGamal cryptosystem, reusing the same random ephemeral key $k$ across multiple messages completely destroys ____. | **confidentiality (secrecy)** | Single Word | Allows recovery of the plaintext directly through quotient division. |
| Elliptic Curve Cryptography (ECC) was independently proposed in 1985 by mathematicians Victor Miller and Neil ____. | **Koblitz** | Single Word | ECC provides security equivalent to RSA with vastly smaller key lengths. |
| The geometric collection of points $(x, y)$ satisfying the cubic equation $y^2 = x^3 + ax + b$ along with an artificial point at infinity forms a(n) ____. | **elliptic curve** | Double Word | Curve parameters $a$ and $b$ must satisfy $4a^3 + 27b^2 \neq 0$. |
| The points on an elliptic curve, under the chord-and-tangent addition rule and including the point at infinity $\mathcal{O}$, form a mathematical structure called a(n) ____ group. | **abelian** | Single Word | Commutative group satisfying identity $\mathcal{O}$ and inverses. |
| In Elliptic Curve Cryptography, the identity element of the point addition group is the point at ____. | **infinity (denoted O)** | Single Word | Acts as the zero element: $P + \mathcal{O} = P$. |
| The computational problem of finding the integer scalar $k$ given a base point $P$ and $Q = kP$ on an elliptic curve is the ____. | **Elliptic Curve Discrete Logarithm Problem (ECDLP)** | Acronym / Phrase | Much harder than classical DLP; allows 256-bit ECC to match 3072-bit RSA. |

---

### Chapter 11: Cryptographic Hash Functions
* **Core Focus:** One-way hash functions, message digests, preimage resistance, collision resistance, Birthday attack, Merkle-Damgård, SHA-2, and SHA-3 (Keccak/Sponge).

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| A function that maps an arbitrary-length message to a unique, fixed-length bit string is a cryptographic ____ function. | **hash (or one-way hash)** | Single Word | Output is called a message digest, hash code, or fingerprint. |
| The fixed-length output string generated by a cryptographic hash function is referred to as a message ____. | **digest** | Single Word | Typical sizes: 160 bits (SHA-1), 256 bits (SHA-256), 512 bits (SHA-512). |
| The security property that makes it computationally infeasible to find the original input message $x$ given its hash value $h$ ($h = H(x)$) is ____ resistance. | **preimage (or one-way property)** | Double Word | First preimage resistance; brute-force complexity is $2^m$. |
| The property making it computationally infeasible to find a second message $y \neq x$ such that $H(y) = H(x)$ for a given message $x$ is ____ resistance. | **second preimage (or weak collision)** | Double Word | Second preimage resistance; brute-force complexity is $2^m$. |
| The property making it computationally infeasible to find *any* pair of distinct messages $(x, y)$ such that $H(x) = H(y)$ is ____ resistance. | **collision (or strong collision)** | Double Word | Defeats birthday attacks; requires complexity of $2^{m/2}$. |
| The mathematical paradox showing that collisions in an $m$-bit hash function can be found in approximately $2^{m/2}$ operations rather than $2^m$ is the ____ attack. | **birthday** | Double Word | Based on the probability of shared birthdays among a group of people. |
| The iterative compression structure underlying MD5, SHA-1, and SHA-2 is the ____ construction. | **Merkle–Damgård** | Double Word | Processes message blocks sequentially through a compression function $f$. |
| The output digest length produced by the legacy SHA-1 algorithm is ____ bits. | **160** | Number | Deemed cryptographically broken due to practical collision attacks. |
| The winner of the NIST open competition for SHA-3 was the ____ algorithm, based on a sponge construction. | **Keccak** | Single Word | Designed by Bertoni, Daemen, Peeters, and Van Assche. |
| Unlike the Merkle–Damgård construction, SHA-3 is built on a novel architecture called a(n) ____ construction. | **sponge** | Single Word | Composed of two distinct phases: absorbing phase and squeezing phase. |
| In the SHA-3 sponge construction, the phase where input message blocks are iteratively XORed into the state array is the ____ phase. | **absorbing** | Single Word | Followed by the "squeezing" phase where output bits are extracted. |

---

### Chapter 12: Message Authentication Codes (MACs)
* **Core Focus:** Message authentication requirements, MAC functions, HMAC design, CMAC, Authenticated Encryption, CCM, and GCM.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| A cryptographic checksum generated using a secret key and appended to a message to prove data integrity and origin authenticity is a(n) ____. | **Message Authentication Code (MAC)** | Acronym / Phrase | Receiver computes $MAC = C(K, M)$ to verify against received tag. |
| Unlike a digital signature, a traditional symmetric MAC cannot provide ____ because both parties share the exact same secret key. | **nonrepudiation** | Single Word | Either party could have generated the MAC tag. |
| The standardized MAC that constructs a secure authentication tag by wrapping any standard iterative cryptographic hash function is ____. | **HMAC (Keyed-Hash MAC)** | Acronym / Name | Standardized in RFC 2104 and FIPS 198; proven secure against collisions. |
| In the HMAC algorithm, the two fixed byte constants used to pad the key internally and externally are called ____ and ____. | **ipad (0x36) and opad (0x5C)** | Short Terms | Inner pad (0x36 repeated) and Outer pad (0x5C repeated). |
| The NIST-approved Message Authentication Code constructed from a symmetric block cipher (such as AES) in CBC mode is ____. | **CMAC (Cipher-based MAC)** | Acronym / Name | Uses subkeys derived from the cipher key to eliminate DAA length extension. |
| A cryptographic mechanism that provides confidentiality, integrity, and authenticity simultaneously in a single integrated scheme is called ____. | **Authenticated Encryption (AE)** | Phrase | Avoids subtle design bugs of separate encryption-then-MAC combinations. |
| The NIST-approved authenticated encryption mode that combines Counter (CTR) mode encryption with CBC-MAC authentication is ____ mode. | **CCM (Counter with CBC-MAC)** | Acronym / Phrase | Standardized in NIST SP 800-38C; widely used in IEEE 802.11i Wi-Fi. |
| The high-performance authenticated encryption mode that combines Counter mode encryption with Galois field polynomial authentication is ____ mode. | **GCM (Galois/Counter Mode)** | Acronym / Phrase | Standardized in NIST SP 800-38D; hardware-efficient; uses GHASH in $GF(2^{128})$. |

---

### Chapter 13: Digital Signatures
* **Core Focus:** Digital signature properties, direct vs. arbitrated signatures, forgery classifications, DSA, ECDSA, and RSA-PSS.

| Fill-in Sentence / Target Phrase | Correct Fill-in Answer | Type | Key Exam Context |
| :--- | :--- | :---: | :--- |
| An electronic authentication mechanism that binds a message to the identity of the signer and provides nonrepudiation is a(n) ____. | **digital signature** | Double Word | Created with private key, verified with public key. |
| The legal and security property that prevents a signer from falsely denying that they originated a signed message is ____. | **nonrepudiation** | Single Word | Fundamental advantage of digital signatures over symmetric MACs. |
| A digital signature scheme that involves only the communicating sender and receiver without an intermediary authority is a(n) ____ digital signature. | **direct** | Single Word | Vulnerable to compromised private key claims unless timestamped. |
| The level of cryptographic forgery where an attacker finds an algorithm that can successfully forge signatures on *any* arbitrary message is a(n) ____ break. | **total** | Single Word | The attacker has effectively recovered the signer's private signing key. |
| The level of cryptographic forgery where an attacker generates a valid signature for an adversary-selected target message without the private key is ____ forgery. | **selective** | Double Word | More severe than existential forgery, less severe than universal. |
| The level of cryptographic forgery where an attacker generates a valid signature for at least one message, but has no control over what that message says, is ____ forgery. | **existential** | Double Word | The forged message is often random garbage, but mathematically valid. |
| The US government standard for digital signatures published in FIPS 186 is the ____. | **Digital Signature Standard (DSS / DSA)** | Acronym / Phrase | Based on discrete logarithms in a 160-bit sub-group; outputs $(r, s)$. |
| The variant of the Digital Signature Algorithm adapted to operate over the points of an elliptic curve is ____. | **ECDSA** | Acronym / Phrase | Adopted in TLS, Bitcoin, and mobile security for short key and signature size. |
| The provably secure digital signature scheme for RSA designed by Bellare and Rogaway using randomized padding is ____. | **RSA-PSS (Probabilistic Signature Scheme)** | Acronym / Phrase | Standardized in PKCS#1 v2.1; replaces deterministic RSA signing. |

---

## 🔢 Critical Parameters & Fixed Numerical Fill-ins (Zero Calculation)

Exam questions frequently test memorized constants, bit-lengths, and round counts directly from Stallings' tables:

| Parameter Description | Exact Numerical Constant | Cryptosystem / Algorithm |
| :--- | :---: | :--- |
| **DES Block Size** | **64 bits** | Data Encryption Standard (DES) |
| **DES Total Key Size** | **64 bits** (56 effective + 8 parity bits) | Data Encryption Standard (DES) |
| **DES Effective Secret Key Size** | **56 bits** | Data Encryption Standard (DES) |
| **DES Number of Processing Rounds** | **16 rounds** | Data Encryption Standard (DES) |
| **DES Expansion Permutation Output** | **48 bits** (expanded from 32 bits) | DES Round Function (E-box) |
| **DES S-Box Input and Output Sizes** | **6 bits in, 4 bits out** (per S-box) | DES Substitution Layer (8 S-boxes) |
| **DES Subkey Length per Round** | **48 bits** | DES Key Schedule (PC-2 output) |
| **Triple DES 3-Key Effective Key Size** | **168 bits** ($3 \times 56$ effective; 24 parity bits stripped from 192 bits) | Triple DES (3DES / TDEA) |
| **Triple DES 2-Key Effective Key Size** | **112 bits** ($2 \times 56$ effective; 16 parity bits stripped from 128 bits) | Triple DES (3DES / TDEA) |
| **AES Block Size** | **128 bits** (fixed for all variants) | Advanced Encryption Standard (AES) |
| **AES State Array Dimensions** | **4 rows by 4 columns** (16 bytes) | Advanced Encryption Standard (AES) |
| **AES-128 Key Size & Round Count** | **128-bit key $\rightarrow$ 10 rounds** | Advanced Encryption Standard (AES-128) |
| **AES-192 Key Size & Round Count** | **192-bit key $\rightarrow$ 12 rounds** | Advanced Encryption Standard (AES-192) |
| **AES-256 Key Size & Round Count** | **256-bit key $\rightarrow$ 14 rounds** | Advanced Encryption Standard (AES-256) |
| **AES Word Size** | **4 bytes (32 bits)** | AES Columns & Key Schedule words |
| **WEP Initialization Vector (IV) Size** | **24 bits** | 802.11 WEP (flawed short IV space) |
| **RC4 State Array Size** | **256 bytes** (permutations of 0 to 255) | RC4 Stream Cipher (Array $S$) |
| **SHA-1 Message Digest Size** | **160 bits** (20 bytes) | Secure Hash Algorithm 1 |
| **SHA-256 Message Digest Size** | **256 bits** (32 bytes) | SHA-2 Family |
| **SHA-512 Message Digest Size** | **512 bits** (64 bytes) | SHA-2 Family |
| **HMAC Inner Pad Constant (ipad)** | **0x36** (byte repeated across block) | Keyed-Hash Message Authentication Code |
| **HMAC Outer Pad Constant (opad)** | **0x5C** (byte repeated across block) | Keyed-Hash Message Authentication Code |
| **Double DES Effective Key Space Break**| **2^56** operations (Meet-in-the-Middle)| Diffie-Hellman MITM on Double DES |
| **Birthday Attack Collision Complexity**| **2^(m/2)** operations (for $m$-bit hash)| Generic Birthday Paradox Collision Attack |

---

## ⚡ Master High-Yield Single-Word Fill-ins Alphabetical Index

When a Sakai fill-in question requires a concise, single-word or short-phrase entry, look here:

* **Abelian:** A commutative group where $a \cdot b = b \cdot a$; fundamental to elliptic curves.
* **Adleman:** Leonard Adleman, the mathematician representing the letter "A" in **RSA**.
* **Avalanche:** The cryptographic property where a 1-bit input flip changes $\approx 50\%$ of output bits.
* **Caesar:** Ancient monoalphabetic cipher based on a uniform shift of 3 letter positions.
* **Confusion:** Shannon's principle masking the relationship between ciphertext and secret key via S-boxes.
* **Diffusion:** Shannon's principle spreading plaintext statistical patterns across ciphertext via permutations.
* **Digest:** The fixed-length hash output string representing a larger message.
* **Euclidean:** Algorithm computing $\gcd(a, b)$ via successive division steps without factoring.
* **Feistel:** Symmetrical block cipher network splitting data into halves, used in DES.
* **Field:** An algebraic system where nonzero elements possess both additive and multiplicative inverses.
* **Generator:** An element whose powers generate all non-zero elements in a cyclic group (primitive root).
* **Hamming weight:** The total count of 1-bits (non-zero bits) in a binary vector or secret key; leaks through timing and power side channels.
* **Integrity:** The security objective ensuring data is not modified, deleted, or forged in transit.
* **Irreducible:** A polynomial that cannot be factored into smaller non-trivial polynomials.
* **Keystream:** The pseudo-random bit stream XORed with plaintext in a stream cipher.
* **Masquerade:** Active attack where an imposter assumes the authorized identity of another entity.
* **MixColumns:** AES transformation mixing column bytes via matrix multiplication in $GF(2^8)$; omitted in final round.
* **Nonrepudiation:** Security service preventing a sender from denying authorship of a transmitted message.
* **Nonce:** A number used once (such as an IV or counter) to guarantee uniqueness across sessions.
* **OAEP:** Optimal Asymmetric Encryption Padding; randomizes plaintext before RSA encryption.
* **Permutation:** Transposition of elements or bits without changing their individual values.
* **Playfair:** First practical digram substitution cipher treating letter pairs in a $5 \times 5$ matrix.
* **Preimage:** The original message $x$ corresponding to a given hash output $h = H(x)$.
* **Rijndael:** The original name of the Belgian cipher by Daemen and Rijmen that won AES.
* **RotWord:** AES Key Expansion operation cyclically left-shifting a 4-byte word by 1 byte.
* **Seed:** The initial secret entropy value provided to a PRNG to initialize its bitstream.
* **ShiftRows:** AES transformation cyclically shifting the bottom three rows of the $4 \times 4$ State array.
* **State:** The $4 \times 4$ byte matrix holding intermediate round data in the AES cipher.
* **Steganography:** The art of concealing the very presence of communication within cover media.
* **SSL:** Secure Sockets Layer; Netscape protocol securing transport connections, predecessor to TLS.
* **SLS:** Session Layer Security (or Secure Link Set); security at OSI Layer 5 / common transposition typo for SSL.
* **SubBytes:** AES non-linear byte substitution using multiplicative inverses in $GF(2^8)$ and an affine map.
* **Timing:** Side-channel attack measuring execution durations of modular exponentiation to infer secret key bits.
* **TLS:** Transport Layer Security; IETF standard (RFC 5246/8446) providing encryption and authentication over TCP.
* **Trapdoor:** A one-way function that is easily invertible only when auxiliary secret data is known.
* **Tweak:** Address or sector identifier used in XTS-AES mode to tie encryption to a physical storage location.
* **Vigenère:** Classical polyalphabetic substitution cipher using a repeating keyword and a tableau.
* **XOR:** The bitwise operation ($\oplus$) performing addition without carry in $GF(2^m)$ and stream ciphering.


---

## 🖼️ Visual Architecture & Diagram Fill-ins Guide (Chapters 1 – 13)

Sakai exams frequently convert textbook architecture diagrams, block diagrams, and flowcharts directly into fill-in-the-blank questions by blanking out box labels, component names, subkeys, or data flow paths. This section covers every canonical figure across Chapters 1 to 13 of William Stallings.

### 1. Network Security & Cryptosystem Models (Chapters 1 & 2)
* **Model for Network Security (Figure 1.2):**
  - Input: Original intelligible message $X$ (termed **plaintext**).
  - Transformation Box: Encrypted using a(n) **encryption algorithm** and a shared **secret key** ($K$).
  - Transmitted Data: Unreadable output $Y = E_K(X)$ (termed **ciphertext**).
  - Communication Path: Transmitted across an insecure medium termed a(n) **information channel (or communication channel)**.
  - Threat Actor: An unauthorized third party monitoring or modifying the channel is termed the **opponent (or adversary / attacker)**.
  - Key Distribution: Secret keys are distributed securely via a trusted entity termed a(n) **trusted third party (or Key Distribution Center)**.
* **Network Access Security Model (Figure 1.3):**
  - Security perimeter defense component: The barrier screening external access to an information system is the **gatekeeper function** (e.g., firewall / login authenticator).
  - Internal defense components: Mechanisms controlling access once inside are termed **internal security controls**.
* **Three-Rotor Machine Wiring (Figure 2.8):**
  - The three rotating cylinders are designated the **fast rotor**, **medium rotor**, and **slow rotor**.
  - The stationary component that loops the electrical current back through the cylinders in reverse is the **reflector (or reflecting rotor)**.

---

### 2. Block Cipher & DES Architecture Diagrams (Chapter 3)
* **Feistel Encryption and Decryption Structure (Figure 3.3):**
  - Input block of length $2w$ bits is split into two equal halves: **Left half ($LE_0$)** and **Right half ($RE_0$)**.
  - Iteration round equation: In round $i$, the right half is updated as $RE_i = LE_{i-1} \oplus F(RE_{i-1}, K_i)$, and the left half becomes $LE_i = $ **RE_{i-1}**.
  - Round function: The complex non-linear mathematical module is the **round function F**.
  - Inter-round mechanism: At the conclusion of each round, the two halves are swapped in an operation termed the **swap of halves (or 32-bit swap)**.
  - Invertibility: Decryption uses the exact same algorithm as encryption, but the **subkeys are applied in reverse order** ($K_{16}, K_{15}, \dots, K_1$).
* **Overall DES Structure (Figure 3.4 & 3.5):**
  - Step 1 (Input Transposition): The 64-bit plaintext is rearranged by the **Initial Permutation (IP)** table.
  - Step 2 (Iterative Rounds): Data passes through **16** identical Feistel processing rounds.
  - Step 3 (Pre-output Swap): After round 16, the two 32-bit halves are swapped without entering the round function.
  - Step 4 (Final Transposition): The final 64-bit ciphertext is produced by applying the **Inverse Initial Permutation (IP^-1)**.
* **DES Single Round Function & S-Boxes (Figure 3.6):**
  - The 32-bit right half is expanded to 48 bits using the **Expansion Permutation (E-box)**.
  - The 48-bit expanded block is combined with the 48-bit subkey $K_i$ using bitwise **XOR (exclusive-OR)**.
  - The 48-bit result is partitioned into eight 6-bit chunks and fed into eight distinct **S-boxes (S1 to S8)**.
  - In each S-box, the **first and last bits (bits 1 and 6)** determine the row number (0 to 3), and the **middle four bits (bits 2 through 5)** determine the column number (0 to 15).
  - The output of the 8 S-boxes consists of 32 bits, which are then permuted by the 32-bit **Permutation function (P-box)**.
* **DES Key Schedule Diagram (Figure 3.7):**
  - 64-bit master key is reduced to 56 bits (disregarding parity) by **Permuted Choice 1 (PC-1)**.
  - The 56 bits are split into two 28-bit halves designated **C_0 and D_0**.
  - In rounds 1, 2, 9, and 16, each half undergoes a circular left shift of **1 bit**; in all other rounds, the shift is **2 bits**.
  - The 48-bit subkey $K_i$ for each round is selected from the shifted 56 bits by **Permuted Choice 2 (PC-2)**.

---

### 3. AES Architecture & State Diagrams (Chapter 5)
* **Overall AES Architecture (Figure 5.1 & 5.2):**
  - 128-bit input plaintext is loaded column-by-column into a $4 \times 4$ byte matrix called the **State (or State array)**.
  - Pre-round stage: The State undergoes an initial **AddRoundKey** transformation before Round 1.
  - Standard round transformations (Rounds 1 through $N_r - 1$): Each standard round executes four transformations in sequence: **SubBytes**, **ShiftRows**, **MixColumns**, and **AddRoundKey**.
  - Final round: The transformation deliberately excluded from the final round ($N_r$) is **MixColumns**.
* **AES S-Box Generation Diagram (Figure 5.3):**
  - Step 1: Replace byte $a$ with its multiplicative inverse in the finite field **GF(2^8)** (with $\{00\}$ mapped to itself).
  - Step 2: Apply a(n) **affine transformation** over $GF(2)$ involving matrix multiplication and addition of constant $\{63\}$.
* **AES ShiftRows Diagram (Figure 5.5):**
  - Row 0 undergoes a cyclical left shift of **0 bytes** (unchanged).
  - Row 1 undergoes a cyclical left shift of **1 byte**.
  - Row 2 undergoes a cyclical left shift of **2 bytes**.
  - Row 3 undergoes a cyclical left shift of **3 bytes**.
* **AES MixColumns Diagram (Figure 5.6):**
  - Each column of the State is multiplied by a fixed circulant matrix whose elements in hexadecimal are **{02}, {03}, {01}, {01}**.
* **AES Key Expansion Diagram (Figure 5.8):**
  - Operates on 4-byte words ($w[i]$).
  - For words with indices that are multiples of 4, the $g$-function applies:
    1. **RotWord:** Cyclically left-shifts a 4-byte word by 1 byte ($[b_0, b_1, b_2, b_3] \rightarrow [b_1, b_2, b_3, b_0]$).
    2. **SubWord:** Passes each byte of the word through the AES **S-box**.
    3. **Round Constant (Rcon):** Performs bitwise XOR with the word $[RC[j], 00, 00, 00]$ where $RC[j]$ is a power of $\{02\}$ in **GF(2^8)**.

---

### 4. Block Cipher Modes of Operation Diagrams (Chapter 6)
* **Electronic Codebook (ECB) Diagram (Figure 6.1):**
  - Encryption formula: $C_j = E(K, P_j)$.
  - Decryption formula: $P_j = D(K, C_j)$.
  - Diagram feature: Completely isolated parallel paths with **zero feedback or chaining** between blocks.
* **Cipher Block Chaining (CBC) Diagram (Figure 6.3):**
  - Encryption: Plaintext block $P_j$ is XORed with preceding ciphertext $C_{j-1}$ before encryption: $C_j = E(K, P_j \oplus C_{j-1})$.
  - First block initialization: Plaintext block $P_1$ is XORed with the **Initialization Vector (IV)**.
  - Decryption: Ciphertext block $C_j$ is decrypted then XORed with $C_{j-1}$: $P_j = D(K, C_j) \oplus C_{j-1}$.
* **Cipher Feedback (CFB) Diagram (Figure 6.5):**
  - Input to encryption is an $s$-bit **shift register** initialized with an IV.
  - The leftmost $s$ bits of the encryption output are XORed with plaintext $P_j$ to yield $C_j$.
  - Feedback path: The ciphertext $C_j$ is fed back into the rightmost end of the shift register.
* **Output Feedback (OFB) Diagram (Figure 6.7):**
  - Feedback path: The output of the encryption function is fed directly back into the input of the next encryption function, completely **independent of the message stream**.
  - Encryption and decryption both execute only the **encryption function E**, never decryption function D.
* **Counter (CTR) Mode Diagram (Figure 6.9):**
  - Keystream block generation: Encrypts the concatenation of a fixed **Nonce** and an incrementing **Counter** value: $O_j = E(K, T_j)$.
  - Ciphertext generation: Plaintext is XORed with keystream: $C_j = P_j \oplus O_j$.
  - Decryption: Re-encrypts the same counter values and XORs with ciphertext: $P_j = C_j \oplus E(K, T_j)$.
* **XTS-AES Storage Mode Diagram (Figure 6.11):**
  - Operates on fixed 128-bit blocks within a disk sector using two keys: **Key 1 (encryption)** and **Key 2 (tweak derivation)**.
  - Tweak generation: The logical block address (sector number $i$) is encrypted with Key 2 and multiplied by $\alpha^j$ in the finite field **GF(2^128)**.
  - The resulting tweak value is XORed with the plaintext before AES encryption and XORed again after encryption.

---

### 5. PRNG & Stream Cipher Diagrams (Chapter 7)
* **TRNG vs. PRNG Conceptual Model (Figure 7.1 & 7.2):**
  - TRNG stages: Non-deterministic physical process (thermal noise / shot noise) $\rightarrow$ analog-to-digital converter (ADC) $\rightarrow$ **entropy source** $\rightarrow$ conditioning algorithm (deskewing) $\rightarrow$ true random bits.
  - PRNG stages: Fixed-length input **seed** $\rightarrow$ deterministic algorithmic generator $\rightarrow$ long sequence of pseudorandom bits.
* **Stream Cipher Structure Diagram (Figure 7.6):**
  - Inputs to Bit-Stream Generator: A shared secret **key** and an optional initialization vector (**IV** or nonce).
  - Output of Bit-Stream Generator: A continuous sequence of pseudo-random bits termed the **keystream (k_i)**.
  - Encryption: Ciphertext bit $c_i$ is generated by computing $c_i = $ **p_i ⊕ k_i**.
  - Decryption: Plaintext bit $p_i$ is recovered by computing $p_i = $ **c_i ⊕ k_i**.
* **RC4 State Permutation Diagram (Figure 7.7):**
  - Internal memory: A 256-byte array designated **S**, holding a permutation of all bytes from 0 to 255.
  - Two 8-bit pointer variables designated **i** and **j**.
  - Output byte calculation: $t = (S[i] + S[j]) \bmod 256$; output byte is **K = S[t]**.

---

### 6. Public-Key, RSA & Diffie-Hellman Diagrams (Chapters 9 & 10)
* **Public-Key Cryptography Models (Figure 9.1 & 9.2):**
  - Encryption for Secrecy: Plaintext $M$ encrypted using recipient B's **public key (PU_b)**; decrypted using recipient B's **private key (PR_b)**.
  - Encryption for Authentication: Plaintext $M$ signed/encrypted using sender A's **private key (PR_a)**; verified using sender A's **public key (PU_a)**.
* **RSA-OAEP Padding Structure (Figure 9.8):**
  - Plaintext $M$ is concatenated with fixed padding bits to form data block $DB$.
  - A random seed of length $k_0$ bits is generated.
  - Mask generation: The seed is expanded via **MGF1** and XORed with $DB$ to produce **maskedDB**.
  - Feedback: $maskedDB$ is passed through **MGF1** and XORed with the seed to produce **maskedSeed**.
  - Transmitted block: Concatenation of **maskedDB || maskedSeed**, which is then encrypted with RSA.
* **Diffie-Hellman Key Exchange Flowchart (Figure 10.1):**
  - Public Parameters: Global prime number **q** and integer **alpha (α)**, which must be a **primitive root** modulo $q$.
  - Alice selects secret private key $X_A < q$ and sends public value $Y_A = $ **α^(X_A) mod q**.
  - Bob selects secret private key $X_B < q$ and sends public value $Y_B = $ **α^(X_B) mod q**.
  - Alice computes shared secret $K = $ **(Y_B)^(X_A) mod q**.
  - Bob computes shared secret $K = $ **(Y_A)^(X_B) mod q**.
  - Shared secret equality: Both values equal **α^(X_A * X_B) mod q**.
* **Elliptic Curve Point Arithmetic (Figure 10.3 & 10.4):**
  - The geometric rule for adding two points $P$ and $Q$ on an elliptic curve is the **chord-and-tangent rule**.
  - The straight line connecting $P$ and $Q$ intersects the curve at a third point denoted $-R$; the sum $P + Q$ is obtained by **reflecting point -R across the x-axis**.
  - If $P = Q$, the line used is the **tangent line** to the curve at point $P$.
  - If a vertical line connects point $P$ and its reflection, it intersects the curve at the point at **infinity (denoted O)**.

---

### 7. Hash Functions, MACs & Digital Signatures (Chapters 11, 12, 13)
* **Merkle–Damgård Iterated Hash Architecture (Figure 11.5):**
  - The input message is partitioned into $L$ fixed-size blocks of $b$ bits each: **Y_0, Y_1, ..., Y_{L-1}**.
  - Final block padding: The last block is padded with a 1 followed by zeros and appended with the **message length (length padding)**.
  - The fixed initial value loaded into the chaining register is the **Initialization Vector (IV or H_0)**.
  - Chaining module: The core iterative component updating the chaining variable is the **compression function (f)**.
  - Output: The final hash value is the output of the last compression stage, **H_L**.
* **SHA-3 Sponge Construction Diagram (Figure 11.8):**
  - State width: Total internal state width is $b$ bits, divided into two sections: **bitrate (r)** and **capacity (c)** ($b = r + c$).
  - Phase 1 (**Absorbing Phase**): Message blocks of length $r$ bits are iteratively XORed into the first $r$ bits of the state, followed by state permutation function $f$.
  - Security control: The parameter $c$ (capacity) is never directly touched by message inputs, establishing the **security level** of the hash function ($c = 2 \times security\_level$).
  - Phase 2 (**Squeezing Phase**): Output blocks of length $r$ bits are sequentially extracted from the first $r$ bits of the state to form the digest.
* **HMAC Structure Diagram (Figure 12.3):**
  - Secret key $K$ is padded with zeros to match the hash block size $b$, forming padded key **K^+**.
  - Inner hash computation: $K^+$ is XORed with the inner pad byte constant **ipad (0x36)** and concatenated with message $M$.
  - Outer hash computation: $K^+$ is XORed with the outer pad byte constant **opad (0x5C)** and concatenated with the inner hash output.
  - Canonical formula: $HMAC(K, M) = $ **H((K^+ ⊕ opad) || H((K^+ ⊕ ipad) || M))**.
* **Generic Digital Signature Generation & Verification (Figure 13.1):**
  - Sender side: Message $M \rightarrow$ Hash function $H(M) \rightarrow$ Encrypt with sender's **private key (PR_a)** $\rightarrow$ Digital Signature $S$.
  - Transmission: The message and signature are transmitted together as the pair **(M, S)**.
  - Receiver side:
    1. Computes local hash of message: $h = H(M)$.
    2. Decrypts signature using sender's **public key (PU_a)** to recover $h' = D(PU_a, S)$.
    3. Verification test: The signature is declared valid if and only if **h == h'**.
* **NIST Digital Signature Algorithm (DSA) Architecture (Figure 13.3):**
  - Global public parameters: Prime modulus $p$, prime divisor $q$ (where $q$ divides $p-1$), and generator $g$.
  - User keys: Private key $x$ (random integer $< q$), Public key $y = g^x \bmod p$.
  - Per-message parameter: For every signed message, the signer generates an ephemeral, one-time random integer **k** ($k < q$).
  - Signature output: A pair of two integers designated **(r, s)**, where $r = (g^k \bmod p) \bmod q$.
