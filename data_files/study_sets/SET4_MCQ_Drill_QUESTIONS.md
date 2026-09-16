# DCIT418 — SET 4
## MCQ Drill
**Chapters 1–13 | 100 questions | Suggested time: 50 minutes | Closed book**

Sakai MCQs reward breadth, not depth. Work fast. Mark anything you guessed with a dot so you can separate real knowledge from luck when you mark it.

---

## CHAPTER 1 — Overview

**1.** Which is NOT part of the CIA triad?
a) Confidentiality b) Integrity c) Authentication d) Availability

**2.** Assuring that a communicating entity is who it claims to be is:
a) Integrity b) Authentication c) Access control d) Availability

**3.** Traffic analysis is:
a) An active attack b) A passive attack c) A denial of service d) A masquerade

**4.** Which attack type is hardest to prevent but easiest to detect?
a) Passive b) Active c) Both equally d) Neither

**5.** The three pillars of the OSI Security Architecture are attack, mechanism and:
a) Protocol b) Policy c) Service d) Standard

**6.** Replay attacks fall under:
a) Passive attacks b) Active attacks c) Traffic analysis d) Steganography

**7.** Which service prevents a sender denying having sent a message?
a) Access control b) Data integrity c) Non-repudiation d) Authentication

**8.** System integrity refers to:
a) Data being unmodified b) The system performing as intended, unimpaired c) Uptime percentage d) Access logging

---

## CHAPTER 2 — Classical Encryption

**9.** The five components of the symmetric cipher model include all EXCEPT:
a) Plaintext b) Secret key c) Public key d) Ciphertext

**10.** The Caesar cipher is a:
a) Transposition cipher b) Monoalphabetic substitution c) Polyalphabetic substitution d) Product cipher

**11.** The Playfair cipher encrypts:
a) Single letters b) Digraphs c) Trigraphs d) Whole words

**12.** In the Playfair 5×5 matrix, which letters are combined?
a) U and V b) I and J c) C and K d) X and Y

**13.** The Vigenère cipher resists frequency analysis because it is:
a) A transposition cipher b) Polyalphabetic c) Unbreakable d) A block cipher

**14.** A cipher offering perfect secrecy is:
a) Vigenère b) Playfair c) One-time pad d) Rail Fence

**15.** The Rail Fence cipher is an example of:
a) Substitution b) Transposition c) Steganography d) A rotor machine

**16.** Steganography differs from cryptography in that it:
a) Uses stronger keys b) Conceals the existence of the message c) Is always unbreakable d) Requires no key

**17.** Rotor machines were significant because they:
a) Introduced public-key cryptography b) Implemented complex polyalphabetic substitution mechanically c) Used transposition only d) Were unbreakable

**18.** A brute-force attack on a monoalphabetic cipher is impractical, yet the cipher is weak because:
a) The key is too short b) Letter frequencies survive encryption c) It uses transposition d) The algorithm is secret

---

## CHAPTER 3 — Block Ciphers and DES

**19.** DES block size is:
a) 32 bits b) 56 bits c) 64 bits d) 128 bits

**20.** DES effective key size is:
a) 48 bits b) 56 bits c) 64 bits d) 128 bits

**21.** The number of DES rounds is:
a) 8 b) 10 c) 16 d) 32

**22.** In a Feistel cipher, decryption uses:
a) A separate inverse algorithm b) The same algorithm with subkeys reversed c) Inverted S-boxes d) A different key entirely

**23.** The only nonlinear element of the DES round function is:
a) Expansion b) The S-boxes c) The P-box d) The subkey XOR

**24.** The DES initial permutation contributes:
a) Confusion b) Diffusion c) Nothing cryptographically d) Key mixing

**25.** The avalanche effect means:
a) Errors cascade across blocks b) A small input change causes a large output change c) Keys grow with rounds d) Encryption slows over time

**26.** Claude Shannon's two principles of cipher design are:
a) Speed and simplicity b) Confusion and diffusion c) Substitution and rotation d) Entropy and redundancy

**27.** Diffusion refers to:
a) Hiding the relationship between key and ciphertext b) Spreading plaintext statistics across the ciphertext c) Slowing encryption d) Expanding key length

**28.** Confusion refers to:
a) Obscuring the relationship between key and ciphertext b) Spreading plaintext statistics c) Random padding d) Key rotation

**29.** In the DES round function, the right half is expanded from 32 bits to:
a) 40 b) 48 c) 56 d) 64

**30.** DES S-boxes take how many bits in and out?
a) 4 in, 6 out b) 6 in, 4 out c) 8 in, 4 out d) 6 in, 6 out

---

## CHAPTER 4 — Finite Fields

**31.** GF(p) is a field only when p is:
a) Even b) Odd c) Prime d) Composite

**32.** A multiplicative inverse of a mod n exists only if:
a) a < n b) gcd(a, n) = 1 c) n is even d) a is prime

**33.** A set with one operation satisfying closure, associativity, identity and inverse is a:
a) Ring b) Field c) Group d) Lattice

**34.** A commutative group is called:
a) Cyclic b) Abelian c) Finite d) Simple

**35.** The key property a field has that a ring may lack is:
a) Associativity b) Distributivity c) Multiplicative inverses for all nonzero elements d) An additive identity

**36.** In GF(2ⁿ), polynomial addition is equivalent to:
a) Integer addition b) XOR c) AND d) Rotation

**37.** The AES irreducible polynomial is:
a) x⁸+x⁴+x³+x+1 b) x⁸+x⁴+x²+1 c) x⁴+x+1 d) x⁸+x⁷+x+1

**38.** An irreducible polynomial plays the role in GF(2ⁿ) that is played in GF(p) by:
a) The identity element b) A prime modulus c) The generator d) The order

**39.** The Euclidean algorithm computes:
a) Modular inverses directly b) The greatest common divisor c) Prime factorisations d) Discrete logarithms

**40.** The extended Euclidean algorithm is used in cryptography chiefly to:
a) Test primality b) Find multiplicative inverses c) Generate random numbers d) Compute hashes

---

## CHAPTER 5 — AES

**41.** AES block size is always:
a) 64 bits b) 128 bits c) 192 bits d) Variable

**42.** AES-192 uses how many rounds?
a) 10 b) 12 c) 14 d) 16

**43.** AES is structurally:
a) A Feistel cipher b) A substitution-permutation network c) A stream cipher d) A transposition cipher

**44.** The AES State is arranged as:
a) A 4×4 matrix of bytes b) An 8×8 matrix of bits c) A 16-byte vector d) Two 64-bit halves

**45.** Which AES transformation provides nonlinearity?
a) ShiftRows b) MixColumns c) SubBytes d) AddRoundKey

**46.** Which AES transformation is omitted in the final round?
a) SubBytes b) ShiftRows c) MixColumns d) AddRoundKey

**47.** The only AES transformation using the secret key is:
a) SubBytes b) ShiftRows c) MixColumns d) AddRoundKey

**48.** In ShiftRows, row 3 is cyclically shifted by:
a) 0 bytes b) 1 byte c) 2 bytes d) 3 bytes

**49.** The AES S-box is constructed using:
a) Random selection b) Multiplicative inverses in GF(2⁸) plus an affine transformation c) A Feistel function d) A linear congruential generator

**50.** AES key expansion produces how many round keys for AES-128?
a) 10 b) 11 c) 12 d) 14

---

## CHAPTER 6 — Modes of Operation

**51.** Which mode encrypts each block independently?
a) CBC b) ECB c) CFB d) CTR

**52.** Which mode is unsuitable for long messages due to pattern leakage?
a) ECB b) CBC c) OFB d) CTR

**53.** In CBC, the first plaintext block is XORed with:
a) The key b) The IV c) A counter d) Nothing

**54.** Which mode allows random-access decryption?
a) CBC b) CFB c) OFB d) CTR

**55.** In OFB the keystream is produced by encrypting:
a) The plaintext b) The previous ciphertext c) The previous keystream block d) A counter

**56.** In CFB the keystream is produced by encrypting:
a) The plaintext b) The previous ciphertext c) The previous keystream d) A counter

**57.** Which modes do NOT propagate errors?
a) ECB and CBC b) CBC and CFB c) OFB and CTR d) CFB and OFB

**58.** CFB decryption uses:
a) The decryption function D b) The encryption function E c) Both d) Neither

**59.** The counter in CTR must above all be:
a) Secret b) Unique with a given key c) Prime d) Even

**60.** Triple DES applies DES:
a) Twice with one key b) Three times c) Once with a tripled key d) In parallel

**61.** Triple DES remains limited because of its:
a) Key size b) 64-bit block size c) Round count d) S-boxes

**62.** Which mode turns a block cipher into a stream cipher?
a) ECB b) CBC c) CFB d) None

---

## CHAPTER 7 — PRNG and Stream Ciphers

**63.** A PRNG is:
a) Truly random b) Deterministic given a seed c) Hardware-based d) Always cryptographically secure

**64.** The key property of a CSPRNG is:
a) Uniform distribution b) Unpredictability of output c) Speed d) Short period

**65.** A linear congruential generator is unsuitable for cryptography because:
a) It is slow b) Its parameters can be deduced from output c) It has no seed d) It produces only even numbers

**66.** A true random number generator draws on:
a) A mathematical formula b) A physical source of entropy c) A fixed seed d) A hash function

**67.** RC4 stands for:
a) Random Cipher 4 b) Rivest Cipher 4 c) Rotational Cipher 4 d) Round Cipher 4

**68.** The RC4 state array S contains:
a) 128 bytes b) 256 bytes c) 512 bytes d) 1024 bytes

**69.** The RC4 phase that produces keystream bytes is:
a) KSA b) PRGA c) MixColumns d) Key expansion

**70.** RC4 is deprecated mainly because of:
a) Slow performance b) Biases in its keystream c) Large key size d) Patent issues

**71.** In a stream cipher, plaintext is combined with the keystream using:
a) Addition mod 26 b) XOR c) Multiplication d) Substitution

**72.** Reusing a stream cipher keystream allows an attacker to obtain:
a) The key b) The XOR of two plaintexts c) The IV d) Nothing useful

---

## CHAPTER 8 — Number Theory

**73.** Fermat's Little Theorem states, for prime p and a not divisible by p:
a) aᵖ ≡ 1 (mod p) b) a^(p−1) ≡ 1 (mod p) c) a^φ(p) ≡ 0 (mod p) d) a² ≡ a (mod p)

**74.** φ(n) for n = pq with p, q distinct primes is:
a) pq b) p+q c) (p−1)(q−1) d) (p+1)(q+1)

**75.** φ(17) equals:
a) 15 b) 16 c) 17 d) 18

**76.** Euler's Theorem generalises Fermat's Theorem to:
a) Prime moduli only b) Any modulus n with gcd(a,n)=1 c) Even moduli d) Polynomial rings

**77.** Miller-Rabin is:
a) A deterministic primality test b) A probabilistic primality test c) A factoring algorithm d) A hash function

**78.** A Miller-Rabin result of "probably prime" means:
a) Certainly prime b) Composite c) Prime with high probability d) Unknown

**79.** The Chinese Remainder Theorem is used in RSA to:
a) Generate primes b) Speed up decryption c) Choose e d) Compute hashes

**80.** The discrete logarithm problem is:
a) Easy in both directions b) Easy forward, hard backward c) Hard forward, easy backward d) Solved in polynomial time

---

## CHAPTER 9 — RSA

**81.** RSA security rests on the difficulty of:
a) Discrete logarithms b) Factoring large integers c) Inverting hashes d) Solving linear systems

**82.** The RSA public key is:
a) (d, n) b) (e, n) c) (p, q) d) (e, φ(n))

**83.** RSA encryption is:
a) C = P^d mod n b) C = P^e mod n c) C = P^e mod φ(n) d) C = P × e mod n

**84.** φ(n) in RSA is used:
a) In every encryption b) In every decryption c) Only during key generation d) For padding

**85.** e must satisfy:
a) e is prime b) gcd(e, φ(n)) = 1 c) e > n d) e divides n

**86.** d is defined as:
a) The inverse of e mod n b) The inverse of e mod φ(n) c) e squared d) p × q

**87.** If an attacker learns φ(n), they can:
a) Do nothing useful b) Compute d and break the system c) Only verify signatures d) Only encrypt

---

## CHAPTER 10 — Diffie-Hellman and ECC

**88.** Diffie-Hellman provides:
a) Encryption b) Key exchange c) Digital signatures d) Hashing

**89.** Diffie-Hellman's main weakness is:
a) Slow speed b) No authentication c) Small keys d) Weak randomness

**90.** A 256-bit ECC key is roughly comparable in security to an RSA key of:
a) 512 bits b) 1024 bits c) 2048 bits d) 3072 bits

**91.** The elliptic curve group identity element is:
a) The origin b) The point at infinity c) The generator d) Zero

**92.** ElGamal encryption produces a ciphertext consisting of:
a) One value b) Two values c) Three values d) A hash

---

## CHAPTER 11 — Hash Functions

**93.** A cryptographic hash function produces:
a) Variable-length output b) Fixed-length output c) Encrypted output d) A keyed digest

**94.** The property that it is infeasible to find any two inputs hashing to the same value is:
a) Preimage resistance b) Second preimage resistance c) Collision resistance d) Avalanche

**95.** The birthday attack targets:
a) Preimage resistance b) Collision resistance c) Key length d) Block size

**96.** A hash function is sometimes called a one-way function because of:
a) Collision resistance b) Preimage resistance c) Its fixed output d) Its speed

**97.** SHA-3 is based on which construction?
a) Merkle-Damgård b) Feistel c) Sponge d) SPN

---

## CHAPTERS 12–13 — MACs and Digital Signatures

**98.** A MAC differs from a hash in that it:
a) Produces variable output b) Uses a secret key c) Is reversible d) Is faster

**99.** HMAC is constructed by:
a) Encrypting a hash b) Nesting a hash function with a key and two padding constants c) XORing two hashes d) Using a block cipher directly

**100.** A digital signature provides authentication, integrity and:
a) Confidentiality b) Availability c) Non-repudiation d) Anonymity

---

**END OF SET 4**
