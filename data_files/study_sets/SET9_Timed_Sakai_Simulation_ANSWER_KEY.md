# DCIT418 — SET 9 ANSWER KEY
## Timed Sakai Simulation

---

# SECTION A — MULTIPLE CHOICE (30 marks)

| Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|
| 1 | c | 11 | b | 21 | b |
| 2 | c | 12 | c | 22 | b |
| 3 | b | 13 | c | 23 | b |
| 4 | a | 14 | d | 24 | b |
| 5 | b | 15 | b | 25 | c |
| 6 | b | 16 | d | 26 | b |
| 7 | b | 17 | c | 27 | b |
| 8 | c | 18 | b | 28 | c |
| 9 | c | 19 | c | 29 | c |
| 10 | c | 20 | b | 30 | c |

**Notes on the ones designed to catch you:**
- **Q5** — F need *not* be invertible. That is the whole point of the Feistel design.
- **Q17** — OFB chains keystream to keystream. CFB chains off ciphertext. Mixing these up is the single most common modes error.
- **Q19** — the counter needs *uniqueness*; unpredictability is the CBC IV's requirement.
- **Q24** — Euler's covers composite moduli, which is why RSA depends on it rather than Fermat's.
- **Q30** — a MAC uses a shared key, so either party could have produced the tag; non-repudiation is therefore impossible.

---

# SECTION B — FILL IN THE BLANKS (25 marks)

**31.** Authentication; Access Control; Data Confidentiality; Data Integrity; Non-repudiation; **Availability** *(6)*

**32.** Lᵢ = Rᵢ₋₁ ; Rᵢ = Lᵢ₋₁ ⊕ F(Rᵢ₋₁, Kᵢ) *(2)*

**33.** SubBytes; **ShiftRows**; MixColumns; AddRoundKey *(4)*

**34.** x⁸ + x⁴ + x³ + x + 1 *(1)*

**35.** C = P^e mod **n** ; P = C^d mod **n** *(2)*

**36.** gcd(e, φ(n)) = 1 ; multiplicative inverse ; φ(n) *(3)*

**37.** ECB; CBC; CFB; OFB; CTR *(5)*

**38.** Preimage resistance; second preimage resistance; collision resistance *(3)*

---

# SECTION C — ESSAY (45 marks)

Mark each out of 15 using the bands at the foot of this key.

### Q39 — Passive vs active attacks
Expect: definitions of both *(2)*; the two passive types, release of message contents and traffic analysis *(2)*; the four active types, masquerade, replay, modification of messages, DoS *(4)*; the strategic contrast — passive alters nothing so detection is impossible and prevention via encryption is the only route, while active attacks are detectable but the attack surface is unbounded so detection and recovery dominate *(5)*; examples throughout *(2)*.
Credit the observation that traffic analysis survives encryption, which is why padding and traffic shaping exist.

### Q40 — Feistel structure
Expect: the split into halves and both equations *(3)*; the reversed-subkey decryption property and the reason XOR makes it work *(3)*; the significance — F need not be invertible, so it can be arbitrarily complex and chosen purely for strength, and one implementation serves both directions *(4)*; the design parameters, any three of block size, key size, rounds, subkey generation, complexity of F *(2)*; contrast with AES as an SPN transforming the whole block, needing fewer rounds but requiring invertible transformations and a separate inverse cipher *(3)*.

### Q41 — AES transformations
Expect: all four named in order *(4)*; a correct role for each — SubBytes nonlinearity/confusion, ShiftRows diffusion across columns, MixColumns diffusion within a column via GF(2⁸), AddRoundKey the sole key-dependent step *(4)*; MixColumns omitted because its diffusion is only useful if further rounds follow, and its inclusion would also complicate the inverse cipher for no gain *(3)*; why AddRoundKey alone is insufficient — a bare XOR with key material is trivially broken, so the public transformations supply the mixing while AddRoundKey supplies the secrecy, and neither half is secure alone *(4)*.

### Q42 — Modes of operation
Expect: all five named with formulas or accurate descriptions *(5)*; a comparison covering error propagation, stream behaviour and parallelisability *(4)*; ECB's failure located in the *determinism of the mode* — equal plaintext blocks give equal ciphertext blocks because E under a fixed key is a deterministic function, so plaintext repetition structure survives *(3)*; the argument that mode matters more than key size — AES-128 already gives an unreachable work factor while ECB, predictable IVs and repeated counters create attacks that succeed identically against AES-256 because they never touch the key *(3)*.
An answer that says only "patterns leak" for ECB caps at half marks on that portion.

### Q43 — RSA
Expect: five key generation steps in order *(4)*; both formulas with the modulus correctly given as n *(3)*; the correctness argument — ed ≡ 1 (mod φ(n)) so ed = 1 + kφ(n), hence P^(ed) = P·(P^φ(n))^k ≡ P (mod n) by **Euler's Theorem**, with Euler's needed because n is composite *(5)*; secrecy of p, q and φ(n) — any one yields d immediately, and knowing n with φ(n) recovers p and q via a quadratic, so all three are as sensitive as the private key *(3)*.

### Q44 — Diffie-Hellman
Expect: public parameters q and primitive root α *(2)*; each party's actions with Y = α^X mod q *(3)*; the algebra showing both reach α^(X_A·X_B) *(4)*; the man-in-the-middle mechanism, substituting the attacker's public value in each direction and relaying *(4)*; the key insight that no discrete logarithm is solved and the protocol is bypassed rather than broken, because nothing binds a public value to an identity *(2)*.

### Q45 — Hash vs MAC vs signature
Expect: keys used — none, shared secret, sender's private key *(3)*; services — integrity; integrity plus authentication; integrity plus authentication plus non-repudiation *(3)*; who can verify — anyone; shared-key holders; anyone with the public key *(3)*; the non-repudiation argument — both MAC parties hold the same key so either could have produced the tag, whereas only the signer holds the private key *(4)*; credit for mentioning HMAC or for noting that signatures hash first for efficiency *(2)*.

---

# ESSAY BANDS (per question, out of 15)

| Marks | Standard |
|---|---|
| 13–15 | Complete, accurate, correct structure for the verb, mechanism explained not merely named |
| 10–12 | Sound and mostly complete; some mechanisms asserted rather than explained |
| 7–9 | Core facts present, reasoning thin, structure loose |
| 4–6 | Fragments of correct material, significant omissions or errors |
| 0–3 | Largely off-target |

---

# FINAL DIAGNOSTIC

| Total | Band |
|---|---|
| 70+ | A |
| 60–69 | B |
| 50–59 | C |
| 40–49 | D |
| Below 40 | Fail |

Record two numbers: your total, and your **Section C average**. If Section A and B are strong but Section C lags, your problem is production under time pressure, not knowledge — fix it by writing skeletons from Set 6, not by re-reading chapters. If Section A and B lag, the problem is recall, and Sets 4, 5 and 7 are the remedy.
