# DCIT 418 — SYSTEMS AND NETWORK SECURITY
## MOCK EXAMINATION — SET 3
### Time allowed: ONE (1) hour | Total: 100 marks | Chapters 1–13

**INSTRUCTIONS**
- Answer **ALL** questions in Sections A and B.
- Answer **ANY TWO (2)** questions from Section C.
- No calculators or rough working required; this paper contains no calculation questions.

**Suggested budget:** Section A 18 minutes · Section B 12 minutes · Section C 27 minutes · 3 minutes review.

*Note: this is a different paper from Set 9. Sit whichever you have not yet seen, and keep the other for a second attempt.*

---

# SECTION A — MULTIPLE CHOICE (30 marks)
*One mark each.*

**1.** Modification of messages is classified as:
a) A passive attack b) An active attack c) Traffic analysis d) Steganography

**2.** The OSI Security Architecture's three pillars are attack, service and:
a) Policy b) Protocol c) Mechanism d) Standard

**3.** Which security objective concerns a system performing as intended, unimpaired?
a) Data integrity b) System integrity c) Availability d) Authenticity

**4.** Frequency analysis defeats a monoalphabetic cipher because the cipher:
a) Has a small keyspace b) Preserves plaintext letter statistics c) Uses transposition d) Reuses its key

**5.** Which cipher varies the substitution alphabet by position?
a) Caesar b) Playfair c) Vigenère d) Rail Fence

**6.** Steganography differs from cryptography in that it conceals:
a) The key b) The algorithm c) The existence of the message d) The recipient

**7.** In a Feistel cipher the round function F:
a) Must be invertible b) Need not be invertible c) Must be a permutation d) Must be linear

**8.** DES's 64-bit stored key contains how many parity bits?
a) 4 b) 8 c) 16 d) 0

**9.** Obscuring the relationship between the key and the ciphertext is called:
a) Diffusion b) Confusion c) Avalanche d) Whitening

**10.** The DES round function expands the right half to how many bits?
a) 32 b) 40 c) 48 d) 64

**11.** A structure with two operations in which multiplication need not have inverses is a:
a) Group b) Ring c) Field d) Monoid

**12.** In GF(2ⁿ), adding two elements is equivalent to:
a) Integer addition b) XOR c) AND d) Modular multiplication

**13.** An irreducible polynomial plays the role played in GF(p) by:
a) The generator b) A prime modulus c) The identity d) The order

**14.** AES arranges its block as:
a) Two 64-bit halves b) A 4×4 byte matrix c) An 8×8 bit matrix d) A 16-byte queue

**15.** Which AES transformation provides diffusion across columns?
a) SubBytes b) ShiftRows c) MixColumns d) AddRoundKey

**16.** AES-128 requires how many round keys in total?
a) 10 b) 11 c) 12 d) 14

**17.** Which mode makes encryption probabilistic by seeding the chain with a random value?
a) ECB b) CBC c) CTR d) None

**18.** An error in one CBC ciphertext block affects the decryption of:
a) That block only b) That block and the next c) All later blocks d) No blocks

**19.** Which mode's keystream can be precomputed entirely before the plaintext is known?
a) ECB b) CBC c) CFB d) CTR

**20.** Triple DES was introduced primarily to address DES's:
a) Block size b) Key size c) Round count d) Slow speed

**21.** A true random number generator derives its output from:
a) A seed and formula b) Physical entropy c) A block cipher d) A counter

**22.** RC4's KSA phase is responsible for:
a) Emitting keystream bytes b) Initialising the state array from the key c) Expanding round keys d) Reducing polynomials

**23.** Euler's totient φ(n) counts the integers below n that are:
a) Prime b) Even c) Coprime to n d) Divisors of n

**24.** Miller-Rabin returning "probably prime" means the number is:
a) Certainly prime b) Certainly composite c) Prime with high probability d) Indeterminate

**25.** The Chinese Remainder Theorem is applied in RSA to:
a) Choose e b) Generate primes c) Accelerate decryption d) Pad messages

**26.** In RSA the private exponent d is:
a) The inverse of e mod n b) The inverse of e mod φ(n) c) Equal to p × q d) A large prime

**27.** ElGamal ciphertext consists of:
a) A single value b) A pair of values c) A digest d) Three values

**28.** The identity element of an elliptic curve group is:
a) The generator point b) The point at infinity c) The origin d) Zero

**29.** Which hash property does the birthday attack target?
a) Preimage resistance b) Second preimage resistance c) Collision resistance d) Determinism

**30.** A digital signature is verified using the sender's:
a) Private key b) Public key c) Shared secret d) Session key

---

# SECTION B — FILL IN THE BLANKS (25 marks)
*One mark per blank.*

**31.** The four categories of active attack are ______, ______, ______ and ______. *(4)*

**32.** The six X.800 security services are ______, ______, ______, ______, ______ and ______. *(6)*

**33.** The two Feistel round equations are Lᵢ = ______ and Rᵢ = ______. *(2)*

**34.** The four AES round transformations in order are ______, ______, ______ and ______, and the one omitted in the final round is ______. *(5)*

**35.** The RSA encryption formula is C = ______ and the decryption formula is P = ______. *(2)*

**36.** The requirement on a CBC IV is that it be ______, while the requirement on a CTR counter is that it be ______. *(2)*

**37.** The three security properties required of a cryptographic hash function are ______, ______ and ______. *(3)*

**38.** A MAC is verified using a ______ key, whereas a digital signature is verified using a ______ key. *(2)*

---

# SECTION C — ESSAY (45 marks)
*Answer ANY TWO. Each carries 22 marks. One mark is awarded for overall structure and clarity across the section.*

**39.** Discuss the distinction between passive and active attacks. Define both categories, give the specific attack types belonging to each, and explain why the two demand opposite defensive strategies. Conclude by explaining why traffic analysis remains a threat even against fully encrypted communications.

**40.** Explain the Feistel cipher structure, stating its round equations and describing how decryption is performed. Discuss why the design was significant for block cipher development, and contrast it with the structure adopted by AES, identifying what AES gains and what it gives up.

**41.** Describe the four AES round transformations and the role each plays in the cipher. Explain why MixColumns is omitted from the final round, and explain why the three key-independent transformations and AddRoundKey are each insufficient on their own but secure in combination.

**42.** Compare the five block cipher modes of operation with respect to error propagation, stream behaviour and parallelisability. Explain rigorously why ECB is unsafe for long messages, and argue why the choice of mode can matter more in practice than the choice between AES-128 and AES-256.

**43.** Describe the RSA algorithm from key generation through to encryption and decryption. Explain why decryption recovers the original plaintext, naming the theorem involved and stating why Fermat's Little Theorem does not apply. Explain why p, q and φ(n) must each be kept secret.

**44.** Compare a cryptographic hash function, a message authentication code and a digital signature in terms of the keys used, the security services provided and who is able to verify. Explain why only one of the three can provide non-repudiation, and explain why a signature's security depends on the collision resistance of the hash it is built on.

---

**END OF PAPER**
