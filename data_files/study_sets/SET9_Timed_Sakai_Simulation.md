# DCIT418 — SET 9
## Timed Sakai Simulation
### 60 MINUTES | 100 MARKS | CHAPTERS 1–13

**Do this ONCE, and do it last.** Its value comes entirely from being the first time you see these questions. Phone away, timer running, no notes, no scrolling back.

**Suggested budget:** Section A 18 min · Section B 12 min · Section C 27 min · 3 min review.

---

# SECTION A — MULTIPLE CHOICE (30 marks)
*One mark each.*

**1.** Which is a passive attack?
a) Masquerade b) Replay c) Traffic analysis d) Denial of service

**2.** The security service that prevents a sender denying a message was sent is:
a) Authentication b) Access control c) Non-repudiation d) Integrity

**3.** A cipher whose ciphertext preserves the plaintext's letter frequencies exactly is:
a) Monoalphabetic substitution b) Transposition c) Polyalphabetic substitution d) A block cipher

**4.** The one-time pad requires the key to be:
a) Random, message-length, used once b) Prime and secret c) Short and memorable d) Reused for efficiency

**5.** In a Feistel cipher, the round function F:
a) Must be invertible b) Need not be invertible c) Must be linear d) Must be a permutation

**6.** DES's effective key length is:
a) 48 bits b) 56 bits c) 64 bits d) 128 bits

**7.** Spreading the statistical structure of the plaintext across the ciphertext is:
a) Confusion b) Diffusion c) Avalanche d) Padding

**8.** The DES component responsible for nonlinearity is the:
a) Expansion permutation b) P-box c) S-box d) Initial permutation

**9.** A field differs from a ring in that a field guarantees:
a) Associativity b) An additive identity c) Multiplicative inverses for nonzero elements d) Distributivity

**10.** GF(2ⁿ) requires its modulus polynomial to be:
a) Monic b) Of even degree c) Irreducible d) Primitive

**11.** AES is structurally:
a) A Feistel cipher b) A substitution-permutation network c) A stream cipher d) A product transposition

**12.** AES-256 uses how many rounds?
a) 10 b) 12 c) 14 d) 16

**13.** Which AES transformation is omitted in the final round?
a) SubBytes b) ShiftRows c) MixColumns d) AddRoundKey

**14.** The only AES transformation that depends on the secret key is:
a) SubBytes b) ShiftRows c) MixColumns d) AddRoundKey

**15.** Identical plaintext blocks produce identical ciphertext blocks in:
a) CBC b) ECB c) CFB d) CTR

**16.** Which mode permits random-access decryption?
a) CBC b) CFB c) OFB d) CTR

**17.** In OFB mode the keystream is produced by encrypting:
a) The plaintext b) The previous ciphertext c) The previous keystream d) A counter

**18.** CFB decryption requires:
a) The decryption function D b) The encryption function E c) Both d) A separate keystream cipher

**19.** The principal requirement on a CTR counter is that it be:
a) Secret b) Prime c) Unique with a given key d) Unpredictable

**20.** Triple DES remains limited chiefly by its:
a) Key size b) Block size c) Round count d) S-box design

**21.** A generator is cryptographically secure if its output is:
a) Uniformly distributed b) Computationally unpredictable c) Non-repeating d) Hardware-derived

**22.** The RC4 phase that emits keystream bytes is:
a) KSA b) PRGA c) Key expansion d) Whitening

**23.** Reusing a stream cipher keystream reveals:
a) The key b) The XOR of two plaintexts c) The IV d) Nothing

**24.** Euler's Theorem applies where Fermat's does not because Euler's permits:
a) Even exponents b) A composite modulus c) Negative bases d) Polynomial moduli

**25.** In RSA, φ(n) is used:
a) During encryption b) During decryption c) Only in key generation d) For padding

**26.** RSA encryption computes:
a) C = P^d mod n b) C = P^e mod n c) C = P^e mod φ(n) d) C = P·e mod n

**27.** Diffie-Hellman's vulnerability to man-in-the-middle arises from the absence of:
a) Large primes b) Authentication c) Randomness d) Forward secrecy

**28.** A 256-bit ECC key is roughly comparable in strength to an RSA key of:
a) 1024 bits b) 2048 bits c) 3072 bits d) 4096 bits

**29.** The birthday attack targets which hash property?
a) Preimage resistance b) Second preimage resistance c) Collision resistance d) Determinism

**30.** Which cannot be provided by a MAC?
a) Integrity b) Authentication c) Non-repudiation d) Efficient verification

---

# SECTION B — FILL IN THE BLANKS (25 marks)
*One mark per blank.*

**31.** The six X.800 security services are ______, ______, ______, ______, ______ and ______. *(6)*

**32.** The two Feistel round equations are Lᵢ = ______ and Rᵢ = ______. *(2)*

**33.** The four AES round transformations in order are ______, ______, ______ and ______. *(4)*

**34.** The irreducible polynomial used by AES is ______. *(1)*

**35.** The RSA encryption and decryption formulas are C = ______ and P = ______. *(2)*

**36.** In RSA, e must satisfy ______ and d is defined as the ______ of e modulo ______. *(3)*

**37.** The five block cipher modes are ______, ______, ______, ______ and ______. *(5)*

**38.** The three required security properties of a cryptographic hash function are ______, ______ and ______. *(3)*

---

# SECTION C — ESSAY (45 marks)
*Answer any THREE. Fifteen marks each. Plan before you write.*

**39.** Compare passive and active attacks, and explain why each category demands a fundamentally different defensive strategy. Illustrate with examples of each type.

**40.** Explain the Feistel structure, state its round equations, and discuss why the design was significant for block cipher development. Contrast it with the structure adopted by AES.

**41.** Describe the four AES round transformations and explain the role each plays. Explain why MixColumns is omitted from the final round and why AddRoundKey alone would be insufficient.

**42.** Compare the five block cipher modes of operation. Explain why ECB is unsafe for long messages, and why the choice of mode can matter more in practice than the choice of key size.

**43.** Describe the RSA algorithm from key generation through encryption and decryption. Explain why decryption recovers the original plaintext, naming the theorem involved, and state why p, q and φ(n) must be kept secret.

**44.** Describe the Diffie-Hellman key exchange, explain why both parties arrive at the same shared secret, and explain how a man-in-the-middle attack succeeds without solving the discrete logarithm problem.

**45.** Compare a hash function, a message authentication code and a digital signature in terms of keys used, services provided and who can verify. Explain why only one of the three can provide non-repudiation.

---

**END OF PAPER**

*Stop your timer. Mark honestly against Set 9's key before reviewing anything.*
