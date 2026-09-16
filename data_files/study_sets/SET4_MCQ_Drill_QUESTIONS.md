# DCIT418 — Systems and Network Security
## Set 4: Multiple-Choice Practice Examination

**Coverage:** Chapters 1–13  
**Number of questions:** 100  
**Suggested time:** 50 minutes  
**Conditions:** Closed book

**Name:** ________________________________________  
**Student ID:** ___________________________________  
**Date:** _________________________________________

### Instructions to candidates

1. Answer all 100 questions.
2. Select **one best answer**, A, B, C or D, for each question.
3. Record your chosen letter beside the question number or on a separate answer sheet.
4. Use no notes, textbooks or answer keys during the examination.
5. For revision, mark any guessed answer with a dot and review it after completing the paper.

*This is the full 100-question MCQ practice set. It is not the updated 50-MCQ, 10-fill-in, 2-practical examination paper.*

---

## CHAPTER 1 — Overview

**1.** Which is NOT part of the CIA triad?

- **A.** Confidentiality
- **B.** Integrity
- **C.** Authentication
- **D.** Availability

**2.** Assuring that a communicating entity is who it claims to be is:

- **A.** Integrity
- **B.** Authentication
- **C.** Access control
- **D.** Availability

**3.** Traffic analysis is:

- **A.** An active attack
- **B.** A passive attack
- **C.** A denial of service
- **D.** A masquerade

**4.** Which attack type is hardest to prevent but easiest to detect?

- **A.** Passive
- **B.** Active
- **C.** Both equally
- **D.** Neither

**5.** The three pillars of the OSI Security Architecture are attack, mechanism and:

- **A.** Protocol
- **B.** Policy
- **C.** Service
- **D.** Standard

**6.** Replay attacks fall under:

- **A.** Passive attacks
- **B.** Active attacks
- **C.** Traffic analysis
- **D.** Steganography

**7.** Which service prevents a sender denying having sent a message?

- **A.** Access control
- **B.** Data integrity
- **C.** Non-repudiation
- **D.** Authentication

**8.** System integrity refers to:

- **A.** Data being unmodified
- **B.** The system performing as intended, unimpaired
- **C.** Uptime percentage
- **D.** Access logging

---

## CHAPTER 2 — Classical Encryption

**9.** The five components of the symmetric cipher model include all EXCEPT:

- **A.** Plaintext
- **B.** Secret key
- **C.** Public key
- **D.** Ciphertext

**10.** The Caesar cipher is a:

- **A.** Transposition cipher
- **B.** Monoalphabetic substitution
- **C.** Polyalphabetic substitution
- **D.** Product cipher

**11.** The Playfair cipher encrypts:

- **A.** Single letters
- **B.** Digraphs
- **C.** Trigraphs
- **D.** Whole words

**12.** In the Playfair 5×5 matrix, which letters are combined?

- **A.** U and V
- **B.** I and J
- **C.** C and K
- **D.** X and Y

**13.** The Vigenère cipher resists frequency analysis because it is:

- **A.** A transposition cipher
- **B.** Polyalphabetic
- **C.** Unbreakable
- **D.** A block cipher

**14.** A cipher offering perfect secrecy is:

- **A.** Vigenère
- **B.** Playfair
- **C.** One-time pad
- **D.** Rail Fence

**15.** The Rail Fence cipher is an example of:

- **A.** Substitution
- **B.** Transposition
- **C.** Steganography
- **D.** A rotor machine

**16.** Steganography differs from cryptography in that it:

- **A.** Uses stronger keys
- **B.** Conceals the existence of the message
- **C.** Is always unbreakable
- **D.** Requires no key

**17.** Rotor machines were significant because they:

- **A.** Introduced public-key cryptography
- **B.** Implemented complex polyalphabetic substitution mechanically
- **C.** Used transposition only
- **D.** Were unbreakable

**18.** A brute-force attack on a monoalphabetic cipher is impractical, yet the cipher is weak because:

- **A.** The key is too short
- **B.** Letter frequencies survive encryption
- **C.** It uses transposition
- **D.** The algorithm is secret

---

## CHAPTER 3 — Block Ciphers and DES

**19.** DES block size is:

- **A.** 32 bits
- **B.** 56 bits
- **C.** 64 bits
- **D.** 128 bits

**20.** DES effective key size is:

- **A.** 48 bits
- **B.** 56 bits
- **C.** 64 bits
- **D.** 128 bits

**21.** The number of DES rounds is:

- **A.** 8
- **B.** 10
- **C.** 16
- **D.** 32

**22.** In a Feistel cipher, decryption uses:

- **A.** A separate inverse algorithm
- **B.** The same algorithm with subkeys reversed
- **C.** Inverted S-boxes
- **D.** A different key entirely

**23.** The only nonlinear element of the DES round function is:

- **A.** Expansion
- **B.** The S-boxes
- **C.** The P-box
- **D.** The subkey XOR

**24.** The DES initial permutation contributes:

- **A.** Confusion
- **B.** Diffusion
- **C.** Nothing cryptographically
- **D.** Key mixing

**25.** The avalanche effect means:

- **A.** Errors cascade across blocks
- **B.** A small input change causes a large output change
- **C.** Keys grow with rounds
- **D.** Encryption slows over time

**26.** Claude Shannon's two principles of cipher design are:

- **A.** Speed and simplicity
- **B.** Confusion and diffusion
- **C.** Substitution and rotation
- **D.** Entropy and redundancy

**27.** Diffusion refers to:

- **A.** Hiding the relationship between key and ciphertext
- **B.** Spreading plaintext statistics across the ciphertext
- **C.** Slowing encryption
- **D.** Expanding key length

**28.** Confusion refers to:

- **A.** Obscuring the relationship between key and ciphertext
- **B.** Spreading plaintext statistics
- **C.** Random padding
- **D.** Key rotation

**29.** In the DES round function, the right half is expanded from 32 bits to:

- **A.** 40
- **B.** 48
- **C.** 56
- **D.** 64

**30.** DES S-boxes take how many bits in and out?

- **A.** 4 in, 6 out
- **B.** 6 in, 4 out
- **C.** 8 in, 4 out
- **D.** 6 in, 6 out

---

## CHAPTER 4 — Finite Fields

**31.** GF(p) is a field only when p is:

- **A.** Even
- **B.** Odd
- **C.** Prime
- **D.** Composite

**32.** A multiplicative inverse of a mod n exists only if:

- **A.** a < n
- **B.** gcd(a, n) = 1
- **C.** n is even
- **D.** a is prime

**33.** A set with one operation satisfying closure, associativity, identity and inverse is a:

- **A.** Ring
- **B.** Field
- **C.** Group
- **D.** Lattice

**34.** A commutative group is called:

- **A.** Cyclic
- **B.** Abelian
- **C.** Finite
- **D.** Simple

**35.** The key property a field has that a ring may lack is:

- **A.** Associativity
- **B.** Distributivity
- **C.** Multiplicative inverses for all nonzero elements
- **D.** An additive identity

**36.** In GF(2ⁿ), polynomial addition is equivalent to:

- **A.** Integer addition
- **B.** XOR
- **C.** AND
- **D.** Rotation

**37.** The AES irreducible polynomial is:

- **A.** x⁸+x⁴+x³+x+1
- **B.** x⁸+x⁴+x²+1
- **C.** x⁴+x+1
- **D.** x⁸+x⁷+x+1

**38.** An irreducible polynomial plays the role in GF(2ⁿ) that is played in GF(p) by:

- **A.** The identity element
- **B.** A prime modulus
- **C.** The generator
- **D.** The order

**39.** The Euclidean algorithm computes:

- **A.** Modular inverses directly
- **B.** The greatest common divisor
- **C.** Prime factorisations
- **D.** Discrete logarithms

**40.** The extended Euclidean algorithm is used in cryptography chiefly to:

- **A.** Test primality
- **B.** Find multiplicative inverses
- **C.** Generate random numbers
- **D.** Compute hashes

---

## CHAPTER 5 — AES

**41.** AES block size is always:

- **A.** 64 bits
- **B.** 128 bits
- **C.** 192 bits
- **D.** Variable

**42.** AES-192 uses how many rounds?

- **A.** 10
- **B.** 12
- **C.** 14
- **D.** 16

**43.** AES is structurally:

- **A.** A Feistel cipher
- **B.** A substitution-permutation network
- **C.** A stream cipher
- **D.** A transposition cipher

**44.** The AES State is arranged as:

- **A.** A 4×4 matrix of bytes
- **B.** An 8×8 matrix of bits
- **C.** A 16-byte vector
- **D.** Two 64-bit halves

**45.** Which AES transformation provides nonlinearity?

- **A.** ShiftRows
- **B.** MixColumns
- **C.** SubBytes
- **D.** AddRoundKey

**46.** Which AES transformation is omitted in the final round?

- **A.** SubBytes
- **B.** ShiftRows
- **C.** MixColumns
- **D.** AddRoundKey

**47.** The only AES transformation using the secret key is:

- **A.** SubBytes
- **B.** ShiftRows
- **C.** MixColumns
- **D.** AddRoundKey

**48.** In ShiftRows, row 3 is cyclically shifted by:

- **A.** 0 bytes
- **B.** 1 byte
- **C.** 2 bytes
- **D.** 3 bytes

**49.** The AES S-box is constructed using:

- **A.** Random selection
- **B.** Multiplicative inverses in GF(2⁸) plus an affine transformation
- **C.** A Feistel function
- **D.** A linear congruential generator

**50.** AES key expansion produces how many round keys for AES-128?

- **A.** 10
- **B.** 11
- **C.** 12
- **D.** 14

---

## CHAPTER 6 — Modes of Operation

**51.** Which mode encrypts each block independently?

- **A.** CBC
- **B.** ECB
- **C.** CFB
- **D.** CTR

**52.** Which mode is unsuitable for long messages due to pattern leakage?

- **A.** ECB
- **B.** CBC
- **C.** OFB
- **D.** CTR

**53.** In CBC, the first plaintext block is XORed with:

- **A.** The key
- **B.** The IV
- **C.** A counter
- **D.** Nothing

**54.** Which mode allows random-access decryption?

- **A.** CBC
- **B.** CFB
- **C.** OFB
- **D.** CTR

**55.** In OFB the keystream is produced by encrypting:

- **A.** The plaintext
- **B.** The previous ciphertext
- **C.** The previous keystream block
- **D.** A counter

**56.** In CFB the keystream is produced by encrypting:

- **A.** The plaintext
- **B.** The previous ciphertext
- **C.** The previous keystream
- **D.** A counter

**57.** Which modes do NOT propagate errors?

- **A.** ECB and CBC
- **B.** CBC and CFB
- **C.** OFB and CTR
- **D.** CFB and OFB

**58.** CFB decryption uses:

- **A.** The decryption function D
- **B.** The encryption function E
- **C.** Both
- **D.** Neither

**59.** The counter in CTR must above all be:

- **A.** Secret
- **B.** Unique with a given key
- **C.** Prime
- **D.** Even

**60.** Triple DES applies DES:

- **A.** Twice with one key
- **B.** Three times
- **C.** Once with a tripled key
- **D.** In parallel

**61.** Triple DES remains limited because of its:

- **A.** Key size
- **B.** 64-bit block size
- **C.** Round count
- **D.** S-boxes

**62.** Which mode turns a block cipher into a stream cipher?

- **A.** ECB
- **B.** CBC
- **C.** CFB
- **D.** None

---

## CHAPTER 7 — PRNG and Stream Ciphers

**63.** A PRNG is:

- **A.** Truly random
- **B.** Deterministic given a seed
- **C.** Hardware-based
- **D.** Always cryptographically secure

**64.** The key property of a CSPRNG is:

- **A.** Uniform distribution
- **B.** Unpredictability of output
- **C.** Speed
- **D.** Short period

**65.** A linear congruential generator is unsuitable for cryptography because:

- **A.** It is slow
- **B.** Its parameters can be deduced from output
- **C.** It has no seed
- **D.** It produces only even numbers

**66.** A true random number generator draws on:

- **A.** A mathematical formula
- **B.** A physical source of entropy
- **C.** A fixed seed
- **D.** A hash function

**67.** RC4 stands for:

- **A.** Random Cipher 4
- **B.** Rivest Cipher 4
- **C.** Rotational Cipher 4
- **D.** Round Cipher 4

**68.** The RC4 state array S contains:

- **A.** 128 bytes
- **B.** 256 bytes
- **C.** 512 bytes
- **D.** 1024 bytes

**69.** The RC4 phase that produces keystream bytes is:

- **A.** KSA
- **B.** PRGA
- **C.** MixColumns
- **D.** Key expansion

**70.** RC4 is deprecated mainly because of:

- **A.** Slow performance
- **B.** Biases in its keystream
- **C.** Large key size
- **D.** Patent issues

**71.** In a stream cipher, plaintext is combined with the keystream using:

- **A.** Addition mod 26
- **B.** XOR
- **C.** Multiplication
- **D.** Substitution

**72.** Reusing a stream cipher keystream allows an attacker to obtain:

- **A.** The key
- **B.** The XOR of two plaintexts
- **C.** The IV
- **D.** Nothing useful

---

## CHAPTER 8 — Number Theory

**73.** Fermat's Little Theorem states, for prime p and a not divisible by p:

- **A.** aᵖ ≡ 1 (mod p)
- **B.** a^(p−1) ≡ 1 (mod p)
- **C.** a^φ(p) ≡ 0 (mod p)
- **D.** a² ≡ a (mod p)

**74.** φ(n) for n = pq with p, q distinct primes is:

- **A.** pq
- **B.** p+q
- **C.** (p−1)(q−1)
- **D.** (p+1)(q+1)

**75.** φ(17) equals:

- **A.** 15
- **B.** 16
- **C.** 17
- **D.** 18

**76.** Euler's Theorem generalises Fermat's Theorem to:

- **A.** Prime moduli only
- **B.** Any modulus n with gcd(a,n)=1
- **C.** Even moduli
- **D.** Polynomial rings

**77.** Miller-Rabin is:

- **A.** A deterministic primality test
- **B.** A probabilistic primality test
- **C.** A factoring algorithm
- **D.** A hash function

**78.** A Miller-Rabin result of "probably prime" means:

- **A.** Certainly prime
- **B.** Composite
- **C.** Prime with high probability
- **D.** Unknown

**79.** The Chinese Remainder Theorem is used in RSA to:

- **A.** Generate primes
- **B.** Speed up decryption
- **C.** Choose e
- **D.** Compute hashes

**80.** The discrete logarithm problem is:

- **A.** Easy in both directions
- **B.** Easy forward, hard backward
- **C.** Hard forward, easy backward
- **D.** Solved in polynomial time

---

## CHAPTER 9 — RSA

**81.** RSA security rests on the difficulty of:

- **A.** Discrete logarithms
- **B.** Factoring large integers
- **C.** Inverting hashes
- **D.** Solving linear systems

**82.** The RSA public key is:

- **A.** (d, n)
- **B.** (e, n)
- **C.** (p, q)
- **D.** (e, φ(n))

**83.** RSA encryption is:

- **A.** C = P^d mod n
- **B.** C = P^e mod n
- **C.** C = P^e mod φ(n)
- **D.** C = P × e mod n

**84.** φ(n) in RSA is used:

- **A.** In every encryption
- **B.** In every decryption
- **C.** Only during key generation
- **D.** For padding

**85.** e must satisfy:

- **A.** e is prime
- **B.** gcd(e, φ(n)) = 1
- **C.** e > n
- **D.** e divides n

**86.** d is defined as:

- **A.** The inverse of e mod n
- **B.** The inverse of e mod φ(n)
- **C.** e squared
- **D.** p × q

**87.** If an attacker learns φ(n), they can:

- **A.** Do nothing useful
- **B.** Compute d and break the system
- **C.** Only verify signatures
- **D.** Only encrypt

---

## CHAPTER 10 — Diffie-Hellman and ECC

**88.** Diffie-Hellman provides:

- **A.** Encryption
- **B.** Key exchange
- **C.** Digital signatures
- **D.** Hashing

**89.** Diffie-Hellman's main weakness is:

- **A.** Slow speed
- **B.** No authentication
- **C.** Small keys
- **D.** Weak randomness

**90.** A 256-bit ECC key is roughly comparable in security to an RSA key of:

- **A.** 512 bits
- **B.** 1024 bits
- **C.** 2048 bits
- **D.** 3072 bits

**91.** The elliptic curve group identity element is:

- **A.** The origin
- **B.** The point at infinity
- **C.** The generator
- **D.** Zero

**92.** ElGamal encryption produces a ciphertext consisting of:

- **A.** One value
- **B.** Two values
- **C.** Three values
- **D.** A hash

---

## CHAPTER 11 — Hash Functions

**93.** A cryptographic hash function produces:

- **A.** Variable-length output
- **B.** Fixed-length output
- **C.** Encrypted output
- **D.** A keyed digest

**94.** The property that it is infeasible to find any two inputs hashing to the same value is:

- **A.** Preimage resistance
- **B.** Second preimage resistance
- **C.** Collision resistance
- **D.** Avalanche

**95.** The birthday attack targets:

- **A.** Preimage resistance
- **B.** Collision resistance
- **C.** Key length
- **D.** Block size

**96.** A hash function is sometimes called a one-way function because of:

- **A.** Collision resistance
- **B.** Preimage resistance
- **C.** Its fixed output
- **D.** Its speed

**97.** SHA-3 is based on which construction?

- **A.** Merkle-Damgård
- **B.** Feistel
- **C.** Sponge
- **D.** SPN

---

## CHAPTERS 12–13 — MACs and Digital Signatures

**98.** A MAC differs from a hash in that it:

- **A.** Produces variable output
- **B.** Uses a secret key
- **C.** Is reversible
- **D.** Is faster

**99.** HMAC is constructed by:

- **A.** Encrypting a hash
- **B.** Nesting a hash function with a key and two padding constants
- **C.** XORing two hashes
- **D.** Using a block cipher directly

**100.** A digital signature provides authentication, integrity and:

- **A.** Confidentiality
- **B.** Availability
- **C.** Non-repudiation
- **D.** Anonymity

---

**END OF PAPER**

Check that you have answered all 100 questions before consulting the separate answer key.
