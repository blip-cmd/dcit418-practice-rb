# DCIT 418: SYSTEMS AND NETWORK SECURITY
## MOCK EXAMINATION, SET 3 (OBJECTIVE PAPER)
### Time allowed: 55 minutes | Total: 70 marks | Chapters 1–13

**INSTRUCTIONS**
- Answer **ALL** questions in Sections A, B and C.
- This paper has no calculations, no modular arithmetic, no worked cryptographic examples. Sections A and B test concepts, mechanisms and terminology only; Section C tests applying that same material to a short real-world scenario, still without any computation.
- For essay practice on this same material, use Set 6.

**Suggested budget:** Section A 30 minutes · Section B 10 minutes · Section C 10 minutes · 5 minutes review.

*Note: this is a different paper from Set 9. Sit whichever you have not yet seen, and keep the other for a second attempt.*

---

# SECTION A: MULTIPLE CHOICE (50 marks)
*One mark each.*

**1.** In the OSI Security Architecture, a security attack is best defined as:
a) A feature that enhances the security of data processing systems b) Any action that compromises the security of information owned by an organization c) A specific algorithm used to protect data d) A policy enforced by network administrators

**2.** Which of the following is a security mechanism rather than a security service?
a) Authentication b) Access control c) Digital signature d) Non-repudiation

**3.** A passive attack that involves monitoring transmission patterns even when message content is encrypted is called:
a) Masquerade b) Traffic analysis c) Replay d) Repudiation

**4.** The Playfair cipher encrypts:
a) Single letters b) Digrams (pairs of letters) c) Whole words d) Blocks of 8 bits

**5.** In the Vigenère cipher, the same plaintext letter can map to different ciphertext letters because:
a) The alphabet is scrambled once b) A repeating keyword shifts the substitution alphabet by position c) It uses transposition, not substitution d) It operates on digrams

**6.** The Rail Fence cipher is an example of:
a) A substitution technique b) A transposition technique c) A one-time pad d) A stream cipher

**7.** Steganography differs fundamentally from encryption in that it:
a) Uses a stronger key b) Hides the existence of a message rather than its content c) Cannot be automated d) Only works on images

**8.** In a Feistel cipher, increasing the number of rounds primarily increases:
a) The block size b) The key size c) The difficulty of cryptanalysis d) The speed of encryption

**9.** DES is considered vulnerable today mainly because of its:
a) Weak S-boxes b) Short 56-bit effective key length c) Small block permutation d) Use of a Feistel structure

**10.** The purpose of the DES initial and final permutations is:
a) To add cryptographic strength b) To facilitate loading data into hardware, with no cryptographic significance c) To expand the block size d) To generate subkeys

**11.** Which property describes a small change in plaintext or key producing a significant, unpredictable change in the ciphertext?
a) Confusion b) Avalanche effect c) Diffusion only d) Key whitening

**12.** A mathematical structure with two operations in which every nonzero element has a multiplicative inverse is called:
a) A group b) A ring c) A field d) A monoid

**13.** GF(2ⁿ) arithmetic is important in cryptography mainly because it provides:
a) Faster multiplication than integer arithmetic b) A finite field structure suited to byte-oriented operations like those in AES c) Infinite precision arithmetic d) A replacement for modular exponentiation

**14.** An irreducible polynomial in GF(2ⁿ) plays the same structural role as which of the following in GF(p)?
a) A generator b) A prime modulus c) A composite modulus d) An identity element

**15.** AES operates on a state arranged as:
a) A 4×4 matrix of bytes b) A 64-bit linear array c) Two 32-bit halves d) An 8×8 bit array

**16.** Which AES transformation is the only one that depends on the key?
a) SubBytes b) ShiftRows c) MixColumns d) AddRoundKey

**17.** The AES S-box used in SubBytes is constructed from:
a) A simple substitution table with no mathematical structure b) Multiplicative inverses in GF(2⁸) combined with an affine transformation c) A rotation of the plaintext bits d) The DES S-boxes reused

**18.** MixColumns is omitted from the final AES round because:
a) It would corrupt the ciphertext b) Its diffusion effect only pays off when further rounds follow to spread it further c) It is too slow for hardware d) It is not invertible

**19.** Compared to DES, AES uses a structure known as:
a) A Feistel network b) A substitution-permutation network c) A stream cipher construction d) A hash-based construction

**20.** Electronic Codebook (ECB) mode is considered insecure for messages longer than one block mainly because:
a) It is too slow b) Identical plaintext blocks always produce identical ciphertext blocks c) It cannot be parallelised d) It requires an IV

**21.** Cipher Block Chaining (CBC) mode requires:
a) A shared secret counter b) An initialization vector that need not be secret but should be unpredictable c) A separate key for each block d) No key at all

**22.** Which mode of operation allows blocks to be encrypted or decrypted independently and out of order, making it suitable for random access?
a) ECB b) CBC c) CTR d) CFB

**23.** In Output Feedback (OFB) mode, an error in one transmitted ciphertext bit:
a) Propagates to all subsequent blocks b) Affects only the corresponding bit in that one block of plaintext c) Corrupts the entire message d) Cannot be corrected

**24.** A mode of operation that turns a block cipher into a stream cipher by generating a keystream to XOR with the plaintext describes:
a) ECB b) CBC c) CTR and OFB d) None of these

**25.** A cryptographically secure pseudorandom number generator differs from an ordinary PRNG mainly in that it must be:
a) Faster to compute b) Unpredictable to an adversary even with knowledge of earlier outputs c) Based on a linear congruential formula d) Seeded manually before every use

**26.** RC4's Key Scheduling Algorithm (KSA) is responsible for:
a) Producing the keystream bytes used for encryption b) Initializing a 256-byte state array into a key-dependent permutation c) Expanding the round keys for a block cipher d) Reducing a polynomial modulo an irreducible polynomial

**27.** A true random number generator (TRNG) differs from a PRNG in that it:
a) Uses a mathematical recurrence relation b) Draws its output from a physical entropy source rather than a deterministic algorithm c) Is always faster d) Cannot be used for cryptographic purposes

**28.** RC4 has been deprecated primarily because:
a) It is too slow for modern hardware b) Statistical biases in its keystream allow plaintext or key recovery given enough ciphertext c) It cannot be implemented in software d) It requires a fixed 256-bit key

**29.** Euler's totient function φ(n) counts the positive integers less than n that are:
a) Prime b) Even c) Relatively prime to (coprime with) n d) Perfect squares

**30.** The Miller-Rabin test is described as a probabilistic primality test because:
a) It always returns a definite yes-or-no answer b) A "probably prime" result cannot be taken as absolute certainty of primality c) It only works for even numbers d) It replaces the need for prime numbers in cryptography

**31.** The Chinese Remainder Theorem is used in practical RSA implementations mainly to:
a) Choose the public exponent b) Speed up the decryption computation c) Generate the prime factors d) Pad the plaintext before encryption

**32.** RSA is classified as an asymmetric cipher because:
a) It uses two different algorithms for encryption and decryption b) Encryption and decryption use a mathematically related pair of different keys, one public and one private c) It requires two separate communication channels d) It encrypts data twice for extra security

**33.** The security of RSA rests on the computational difficulty of:
a) Solving the discrete logarithm problem b) Factoring the product of two large primes c) Reversing a hash function d) Brute-forcing a symmetric key

**34.** Why must a plain (unpadded) RSA implementation add randomized padding such as OAEP?
a) To make the ciphertext shorter b) Because deterministic encryption leaks information when the same plaintext is encrypted twice c) To speed up decryption d) Padding is not actually necessary for RSA

**35.** In RSA, revealing which value would allow an attacker to immediately compute the private key?
a) The public modulus alone b) The ciphertext alone c) Either of the two secret prime factors d) The public exponent alone

**36.** RSA's public-key approach solves which limitation of purely symmetric cryptosystems?
a) Slow encryption speed b) The need to securely distribute a shared secret key in advance c) The limited block size of ciphers d) The need for a hash function

**37.** The security of the classic Diffie-Hellman key exchange rests on the difficulty of:
a) Factoring large composite numbers b) The discrete logarithm problem c) Finding hash collisions d) Breaking a block cipher

**38.** Diffie-Hellman key exchange, on its own, is vulnerable to man-in-the-middle attacks because:
a) The discrete logarithm problem is actually easy b) The exchanged public values are not bound to verified identities c) It transmits the shared secret in the clear d) It uses a weak symmetric cipher afterward

**39.** Compared to RSA, elliptic curve cryptography can achieve comparable security with:
a) Much larger keys b) Much smaller keys c) No public key at all d) A symmetric key only

**40.** In an elliptic curve group used for cryptography, the identity element is:
a) The generator point b) The point at infinity c) The origin of the coordinate plane d) A randomly chosen point

**41.** A cryptographic hash function takes an input of:
a) Fixed length and produces a fixed-length output b) Variable length and produces a fixed-length digest c) Fixed length and produces a variable-length output d) Variable length and produces a variable-length output

**42.** Which hash property ensures that, given a specific message, it is infeasible to find a different message producing the same digest?
a) Preimage resistance b) Second preimage resistance c) Collision resistance d) Determinism

**43.** The birthday attack exploits:
a) Weak preimage resistance b) The fact that collisions can be found faster than the digest length alone would suggest, due to probability over many pairs c) A flaw specific to one particular hash function only d) Weaknesses in a hash function's key schedule

**44.** Storing a salted hash of a password, rather than the password itself, defends primarily against:
a) Man-in-the-middle attacks b) Precomputed dictionary and rainbow-table attacks c) Traffic analysis d) Replay attacks

**45.** A Message Authentication Code (MAC), unlike a plain hash, requires:
a) No key at all b) A shared secret key known to both sender and receiver c) A public/private key pair d) A digital certificate

**46.** HMAC constructs a MAC by:
a) Encrypting the message with a block cipher b) Nesting a cryptographic hash function around the message and a secret key c) Applying RSA to the digest d) Using only the message length as input

**47.** A MAC alone cannot provide non-repudiation because:
a) It is too slow to verify b) Both communicating parties share the same secret key, so either could have generated a given tag c) It does not use a hash function d) It reveals the plaintext

**48.** A digital signature is created by the signer using their:
a) Public key b) Private key c) A shared secret key d) The recipient's public key

**49.** Anyone can verify a digital signature because verification uses:
a) The signer's private key b) The signer's public key c) A shared secret d) The recipient's private key

**50.** A digital signature scheme is only as strong as the collision resistance of its underlying hash function because:
a) The hash function generates the private key b) The signature is computed over the message digest, so a hash collision lets an attacker transplant a valid signature onto a different message c) The hash function encrypts the message d) Signatures do not actually use a hash function

---

# SECTION B: FILL IN THE BLANKS (10 marks)
*One mark each. No calculations required.*

**51.** The three fundamental security objectives grouped together as the "CIA triad" are confidentiality, integrity and ______.

**52.** In the OSI Security Architecture, the three central concepts are security attack, security mechanism and security ______.

**53.** A technique that hides the existence of a message altogether, rather than its content, is called ______.

**54.** The design property by which the influence of a single plaintext bit spreads over many ciphertext bits is called ______.

**55.** The AES round transformation that provides confusion through a nonlinear byte substitution is called ______.

**56.** A block cipher mode of operation that never uses an initialization vector, and is unsafe for messages longer than one block, is ______.

**57.** RC4 keystream generation is carried out by its second phase, known as the ______.

**58.** The hard mathematical problem underlying both Diffie-Hellman key exchange and the ElGamal cryptosystem is the ______ problem.

**59.** The three required security properties of a cryptographic hash function are preimage resistance, second preimage resistance and ______.

**60.** Unlike a MAC, a digital signature can provide ______, because only the signer holds the private key used to produce it.

---

# SECTION C: PRACTICAL SCENARIOS (10 marks)
*Five marks each. Answer in a few sentences: name the concept, then explain why it applies to this scenario. No calculations.*

**61.** A clerk at a bank intercepts an encrypted funds-transfer message authorizing a ₵500 payment from Client A to Client B. The clerk cannot read or alter the message, since it is properly encrypted, but a week later resubmits the exact same intercepted message to the bank's server, causing a second ₵500 payment to go through without Client A's knowledge. Name the category and specific type of attack this is, and name the security service, together with a mechanism that implements it, that would have prevented it even though the message's confidentiality was never broken.

**62.** A startup wants to let two branch offices securely agree on a shared session key over the open internet, and then use that key to encrypt a large volume of daily file transfers between the branches. A junior developer proposes generating an RSA key pair at each branch and using RSA directly to encrypt every file before transfer. Explain two practical problems with this proposal, and describe the approach that production systems actually use instead, naming where in that approach RSA (or another public-key algorithm) is used and where a symmetric cipher is used.

---

**END OF PAPER**
