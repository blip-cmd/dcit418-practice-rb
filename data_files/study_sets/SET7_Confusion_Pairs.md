# DCIT418 — SET 7
## Confusion Pairs
**Chapters 1–13 | Suggested time: 30 minutes**

Sakai MCQ distractors are built from near-misses. This drill targets the pairs most likely to be set against each other.

**Part 1** is the drill: cover the right-hand column and state the distinction for each pair in one sentence. **Part 2** is a discrimination test. **Part 3** is the reference table — the answers to Part 1.

---

# PART 1 — THE DRILL

For each pair, say aloud in one sentence what separates them. Then check Part 3.

1. Confidentiality vs Integrity
2. Authenticity vs Non-repudiation
3. Passive vs Active attack
4. Masquerade vs Replay
5. Security service vs Security mechanism
6. Substitution vs Transposition
7. Monoalphabetic vs Polyalphabetic
8. Cryptography vs Steganography
9. Confusion vs Diffusion
10. Block cipher vs Stream cipher
11. Feistel vs SPN
12. Group vs Ring vs Field
13. GF(p) vs GF(2ⁿ)
14. Prime vs Irreducible
15. ShiftRows vs MixColumns
16. SubBytes vs AddRoundKey
17. ECB vs CBC
18. CBC vs CFB
19. CFB vs OFB
20. OFB vs CTR
21. IV vs Counter vs Nonce
22. PRNG vs CSPRNG vs TRNG
23. KSA vs PRGA
24. Fermat's vs Euler's Theorem
25. φ(n) vs n as a modulus
26. e vs d
27. Factorisation vs Discrete logarithm
28. Diffie-Hellman vs RSA
29. Diffie-Hellman vs ElGamal
30. DLP vs ECDLP
31. Preimage vs Second preimage vs Collision resistance
32. Hash vs MAC
33. MAC vs Digital signature
34. Merkle-Damgård vs Sponge
35. Encryption vs Encoding vs Hashing

---

# PART 2 — DISCRIMINATION TEST

State which of the pair each statement describes.

**T1.** Protects against alteration of data. *(confidentiality / integrity)*

**T2.** Cannot be provided by a MAC. *(authentication / non-repudiation)*

**T3.** Defended against primarily by prevention. *(passive / active)*

**T4.** Preserves the plaintext's letter frequency distribution exactly. *(substitution / transposition)*

**T5.** Obscures the relationship between the key and the ciphertext. *(confusion / diffusion)*

**T6.** Only half the block is transformed per round. *(Feistel / SPN)*

**T7.** Requires every transformation to be individually invertible. *(Feistel / SPN)*

**T8.** Multiplication need not have inverses. *(ring / field)*

**T9.** The polynomial analogue of a prime number. *(irreducible / monic)*

**T10.** Shifts rows cyclically by 0, 1, 2 and 3 bytes. *(ShiftRows / MixColumns)*

**T11.** Omitted from the final AES round. *(ShiftRows / MixColumns)*

**T12.** The only AES step that uses the secret key. *(SubBytes / AddRoundKey)*

**T13.** Identical plaintext blocks give identical ciphertext blocks. *(ECB / CBC)*

**T14.** Keystream generated from the previous ciphertext block. *(CFB / OFB)*

**T15.** Keystream generated from the previous keystream block. *(CFB / OFB)*

**T16.** Cannot be parallelised despite having no error propagation. *(OFB / CTR)*

**T17.** Must be unpredictable, not merely unique. *(CBC IV / CTR counter)*

**T18.** Must be unique, but need not be unpredictable. *(CBC IV / CTR counter)*

**T19.** Passes statistical randomness tests but is trivially predictable. *(LCG / CSPRNG)*

**T20.** Initialises the 256-byte state array. *(KSA / PRGA)*

**T21.** Applies to a composite modulus. *(Fermat's / Euler's)*

**T22.** The modulus for RSA encryption and decryption. *(n / φ(n))*

**T23.** The modulus in which e and d are inverses. *(n / φ(n))*

**T24.** The hard problem underlying RSA. *(factorisation / discrete log)*

**T25.** Establishes a shared secret but cannot encrypt a message directly. *(Diffie-Hellman / ElGamal)*

**T26.** Given a digest, find any input producing it. *(preimage / collision)*

**T27.** Find any two inputs producing the same digest. *(second preimage / collision)*

**T28.** The property attacked by the birthday attack. *(preimage / collision)*

**T29.** Uses a shared secret key. *(hash / MAC)*

**T30.** Uses the sender's private key. *(MAC / digital signature)*

**T31.** The construction used by SHA-3. *(Merkle-Damgård / sponge)*

**T32.** Reversible without any key. *(encoding / encryption)*

---

# PART 3 — REFERENCE TABLE

| Pair | The distinction |
|---|---|
| **1. Confidentiality vs Integrity** | Confidentiality stops unauthorised *reading*; integrity stops unauthorised *alteration*. |
| **2. Authenticity vs Non-repudiation** | Authenticity establishes who the party is *now*; non-repudiation stops them denying it *later*, which needs asymmetric keys. |
| **3. Passive vs Active** | Passive observes without altering (undetectable, so prevent); active alters state (detectable, so detect and recover). |
| **4. Masquerade vs Replay** | Masquerade is impersonating an entity; replay is retransmitting captured data. Replay is one technique for achieving masquerade. |
| **5. Service vs Mechanism** | The service is *what* is delivered (e.g. data integrity); the mechanism is *how* (e.g. a MAC). One service usually needs several mechanisms. |
| **6. Substitution vs Transposition** | Substitution replaces letters, changing frequencies; transposition reorders positions, leaving frequencies untouched. |
| **7. Mono- vs Polyalphabetic** | Monoalphabetic maps each plaintext letter to one fixed ciphertext letter; polyalphabetic varies the mapping by position, flattening frequencies. |
| **8. Cryptography vs Steganography** | Cryptography hides the *content* of a message; steganography hides the *existence* of it. |
| **9. Confusion vs Diffusion** | Confusion obscures the key–ciphertext relationship (achieved by substitution); diffusion spreads plaintext statistics across the ciphertext (achieved by permutation). |
| **10. Block vs Stream** | Block ciphers process fixed-size blocks through a keyed permutation; stream ciphers generate a keystream and XOR it bit or byte at a time. |
| **11. Feistel vs SPN** | Feistel transforms half the block per round, so F need not be invertible and decryption is the same algorithm with reversed subkeys. SPN transforms the whole block, so every step must be invertible and decryption needs a separate inverse cipher. |
| **12. Group vs Ring vs Field** | Group: one operation, closure, associativity, identity, inverses. Ring: two operations, abelian under addition, multiplication associative and distributive, but *no* guaranteed multiplicative inverses. Field: a ring where every nonzero element also has a multiplicative inverse, so division works. |
| **13. GF(p) vs GF(2ⁿ)** | GF(p) uses integers modulo a prime. GF(2ⁿ) uses polynomials with binary coefficients modulo an irreducible polynomial. Same requirement, different objects. |
| **14. Prime vs Irreducible** | Prime is the integer notion (no smaller integer factors); irreducible is the polynomial notion (no lower-degree factors). Both guarantee multiplicative inverses exist. |
| **15. ShiftRows vs MixColumns** | ShiftRows is a cyclic byte permutation of rows, diffusing across columns. MixColumns is a GF(2⁸) matrix multiplication within each column. MixColumns is dropped in the final round; ShiftRows is not. |
| **16. SubBytes vs AddRoundKey** | SubBytes is a fixed, public, nonlinear substitution supplying confusion. AddRoundKey is a XOR with the round subkey and is the only key-dependent step. |
| **17. ECB vs CBC** | ECB encrypts each block independently, so equal blocks give equal ciphertext. CBC XORs each plaintext block with the previous ciphertext block, seeded by an IV, making encryption probabilistic. |
| **18. CBC vs CFB** | CBC XORs *then* encrypts (the plaintext enters the cipher). CFB encrypts *then* XORs (the plaintext never enters the cipher, so decryption uses E). |
| **19. CFB vs OFB** | CFB's keystream derives from the previous *ciphertext*, so errors propagate. OFB's derives from the previous *keystream*, so they do not — but that makes OFB strictly serial. |
| **20. OFB vs CTR** | Both build a ciphertext-independent keystream and so have no error propagation. OFB chains keystream to keystream (serial); CTR derives each block from an independent counter (parallel, random access). |
| **21. IV vs Counter vs Nonce** | Nonce is the general term for a number used once. A CBC IV must be *unpredictable* because it is XORed with plaintext. A CTR counter need only be *unique*, since repetition reuses a keystream. |
| **22. PRNG vs CSPRNG vs TRNG** | PRNG: deterministic from a seed, statistically good. CSPRNG: a PRNG that is additionally computationally unpredictable. TRNG: draws on physical entropy, typically used to *seed* a CSPRNG. |
| **23. KSA vs PRGA** | KSA sets up the 256-byte state as a key-dependent permutation. PRGA then emits keystream bytes from that state. Setup versus output. |
| **24. Fermat's vs Euler's** | Fermat's applies to a *prime* modulus: a^(p−1) ≡ 1 (mod p). Euler's generalises to *any* modulus with gcd(a,n) = 1: a^φ(n) ≡ 1 (mod n). RSA needs Euler's because n is composite. |
| **25. φ(n) vs n as modulus** | n is the modulus for *values* — plaintexts, ciphertexts, the encryption and decryption operations. φ(n) is the modulus for *exponents* — it is where e and d are inverses, and it is secret. |
| **26. e vs d** | e is public, chosen first, and must be coprime to φ(n). d is private, computed second, and is e's multiplicative inverse mod φ(n). d exists only because e is coprime. |
| **27. Factorisation vs Discrete log** | Factorisation: given n = pq, find p and q — underlies RSA. Discrete log: given α^x mod q, find x — underlies Diffie-Hellman, ElGamal and (in curve form) ECC. |
| **28. Diffie-Hellman vs RSA** | DH is key *agreement* only and rests on discrete logarithms. RSA encrypts and signs, and rests on factorisation. DH establishes a shared secret; RSA transports or signs data. |
| **29. Diffie-Hellman vs ElGamal** | Same discrete-log foundation. DH agrees a shared secret between two parties. ElGamal uses that structure to actually encrypt a message, producing a ciphertext pair (C₁, C₂). |
| **30. DLP vs ECDLP** | DLP works in the multiplicative group of integers mod q and admits sub-exponential attacks. ECDLP works in an elliptic curve group and admits only exponential attacks, which is why ECC keys can be far smaller. |
| **31. Preimage vs Second preimage vs Collision** | Preimage: given h, find *any* x with H(x) = h. Second preimage: given a *specific* x, find a different x′ with the same digest. Collision: find *any* colliding pair, with both inputs free — the easiest of the three, hence the birthday bound. |
| **32. Hash vs MAC** | A hash is unkeyed and gives integrity only — anyone can recompute it, including an attacker who alters the message. A MAC is keyed, so only key holders can produce a valid tag, giving integrity *and* authentication. |
| **33. MAC vs Digital signature** | Both authenticate. A MAC uses a shared secret, so either party could have made the tag, and non-repudiation is impossible. A signature uses the sender's private key, so only they could have made it — hence non-repudiation. |
| **34. Merkle-Damgård vs Sponge** | Merkle-Damgård iterates a compression function over padded blocks (MD5, SHA-1, SHA-2). The sponge absorbs input into a state then squeezes output (SHA-3/Keccak), and resists length-extension attacks that affect Merkle-Damgård. |
| **35. Encryption vs Encoding vs Hashing** | Encryption is reversible *with a key* and provides confidentiality. Encoding is reversible *without any key* (Base64, ASCII) and provides no security at all. Hashing is *not* reversible and provides integrity. Calling Base64 "encryption" is a classic error. |

---

# ANSWERS TO PART 2

T1 integrity · T2 non-repudiation · T3 passive · T4 transposition · T5 confusion · T6 Feistel · T7 SPN · T8 ring · T9 irreducible · T10 ShiftRows · T11 MixColumns · T12 AddRoundKey · T13 ECB · T14 CFB · T15 OFB · T16 OFB · T17 CBC IV · T18 CTR counter · T19 LCG · T20 KSA · T21 Euler's · T22 n · T23 φ(n) · T24 factorisation · T25 Diffie-Hellman · T26 preimage · T27 collision · T28 collision · T29 MAC · T30 digital signature · T31 sponge · T32 encoding

---

**Scoring.** Under 28 of 32 on Part 2 means the pairs are not yet separated in your mind, and MCQ distractors will catch you. Redo Part 1 aloud before moving on.
