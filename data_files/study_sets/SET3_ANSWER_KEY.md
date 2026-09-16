# DCIT 418 — SET 3 ANSWER KEY AND MARKING SCHEME

**Do not open until you have attempted the paper under timed conditions.**

---

# SECTION A — MULTIPLE CHOICE (30 marks)

| Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|
| 1 | b | 11 | b | 21 | b |
| 2 | c | 12 | b | 22 | b |
| 3 | b | 13 | b | 23 | c |
| 4 | b | 14 | b | 24 | c |
| 5 | c | 15 | b | 25 | c |
| 6 | c | 16 | b | 26 | b |
| 7 | b | 17 | b | 27 | b |
| 8 | b | 18 | b | 28 | b |
| 9 | b | 19 | d | 29 | c |
| 10 | c | 20 | b | 30 | b |

**The ones built to catch you:**
- **Q7** — F need *not* be invertible. That property is the entire reason the Feistel design mattered.
- **Q15** — ShiftRows diffuses *across* columns; MixColumns diffuses *within* a column. The direction is the discriminator.
- **Q16** — 11, not 10: one initial AddRoundKey plus ten rounds.
- **Q19** — CTR. OFB's keystream can also be precomputed in principle, but only serially; CTR is the intended answer because each block is independently derivable. (Accept OFB with a correct justification.)
- **Q20** — Triple DES addressed the *key* size. It could not fix the 64-bit block, which is why it remained a stopgap.
- **Q26** — inverse of e mod **φ(n)**, not mod n.

---

# SECTION B — FILL IN THE BLANKS (25 marks)

**31.** Masquerade; Replay; Modification of messages; Denial of Service *(4)*

**32.** Authentication; Access Control; Data Confidentiality; Data Integrity; Non-repudiation; **Availability** *(6)*

**33.** Lᵢ = Rᵢ₋₁ ; Rᵢ = Lᵢ₋₁ ⊕ F(Rᵢ₋₁, Kᵢ) *(2)*

**34.** SubBytes; **ShiftRows**; MixColumns; AddRoundKey; MixColumns omitted *(5)*

**35.** C = P^e mod **n** ; P = C^d mod **n** *(2)*

**36.** unpredictable ; unique *(2)*

**37.** Preimage resistance; second preimage resistance; collision resistance *(3)*

**38.** shared secret ; public *(2)*

---

# SECTION C — ESSAY (45 marks)

Mark each answer out of 22 using the bands below.

### Q39 — Passive vs active attacks
- Definitions of both categories *(3)*
- Passive types: release of message contents, traffic analysis *(3)*
- Active types: masquerade, replay, modification of messages, DoS, each with a one-line explanation *(5)*
- The strategic contrast, argued not asserted: passive attacks alter nothing so there is no trace to detect, making prevention (encryption) the only viable route; active attacks alter state so they are detectable, but the attack surface is unbounded so absolute prevention is unattainable and detection plus recovery dominate *(6)*
- Traffic analysis under encryption: the payload is hidden but source, destination, packet size, timing and frequency remain visible, permitting inference about who communicates with whom, how often and how much; hence padding, traffic shaping and cover traffic as countermeasures *(5)*

### Q40 — Feistel structure
- Split into halves; both equations stated correctly *(4)*
- Decryption: same algorithm, subkeys in reverse order, working because XOR is self-inverse *(4)*
- Significance: F need never be inverted and need not be invertible, so it can be arbitrarily complex and chosen purely for cryptographic strength; one implementation serves both directions *(6)*
- Design parameters, any three of block size, key size, round count, subkey generation, complexity of F *(3)*
- Contrast with AES: SPN transforming the whole block, hence fewer rounds needed; but every transformation must be invertible, so a separate inverse cipher is required. AES gains speed and per-round diffusion, gives up the single-algorithm convenience *(5)*

### Q41 — AES transformations
- All four named in correct order *(4)*
- Correct role for each: SubBytes nonlinearity and confusion, via an S-box built from GF(2⁸) inverses; ShiftRows cyclic row shifts of 0/1/2/3 giving diffusion across columns; MixColumns GF(2⁸) matrix multiply giving diffusion within a column; AddRoundKey XOR with the round subkey *(6)*
- MixColumns omission: its diffusion is only useful when further rounds follow to compound it, so including it in the last round costs computation with no security gain, and it would also force a pointless InvMixColumns step in the inverse cipher *(5)*
- The combination argument: SubBytes, ShiftRows and MixColumns are fixed and public, so anyone can compute or invert them — they supply mixing but no secrecy. AddRoundKey supplies secrecy but a bare XOR with key material is trivially broken on its own. Security comes from injecting key material between rounds of complex public mixing, so that an attacker who understands the mixing perfectly still cannot proceed without the key *(7)*

### Q42 — Modes of operation
- All five named with formulas or accurate descriptions *(5)*
- Comparison across error propagation, stream behaviour, parallelisability, presented as a table or structured prose *(6)*
- ECB rigour: C_i = E(K, P_i) with no dependence on position, IV or any other block; E under a fixed key is deterministic, so P_i = P_j forces C_i = C_j; real data repeats heavily, so the plaintext's repetition structure is copied into the ciphertext. Locate the fault in the *mode*, not the cipher *(5)*
- Mode over key size: AES-128 already gives a 2¹²⁸ work factor beyond reach, so AES-256 raises an already unreachable number; mode and parameter errors (ECB, predictable IVs, repeated counters, keystream reuse) create attacks that never touch the key and succeed identically against AES-256; attackers take the cheapest route *(6)*

*An answer that explains ECB only as "patterns leak" caps at half marks on that portion.*

### Q43 — RSA
- Five key generation steps in order, with public key (e, n) and private key (d, n) identified *(6)*
- Both formulas, modulus correctly given as n *(3)*
- Correctness: ed ≡ 1 (mod φ(n)) so ed = 1 + kφ(n); therefore P^(ed) = P·(P^φ(n))^k ≡ P (mod n) by **Euler's Theorem** *(6)*
- Why not Fermat's: Fermat's holds only for a prime modulus, and n = pq is composite; Fermat's is the special case of Euler's where n is prime, and it underpins primality testing rather than the correctness proof *(3)*
- Secrecy of p, q and φ(n): any one yields d immediately via the extended Euclidean algorithm; further, n together with φ(n) recovers p and q as roots of a quadratic, since p + q = n − φ(n) + 1 and pq = n. All three are as sensitive as the private key, and n is safe to publish only because factoring it is infeasible *(4)*

### Q44 — Hash vs MAC vs signature
- Keys used: none; shared secret; sender's private key for signing and public key for verification *(4)*
- Services: integrity; integrity plus authentication; integrity plus authentication plus non-repudiation *(4)*
- Who can verify: anyone; holders of the shared key only; anyone holding the public key *(3)*
- Non-repudiation argument: a MAC's key is shared, so both parties could have produced any valid tag and a third party has no basis to attribute it; a signature's private key is held by exactly one party, so only they could have produced it and this is independently verifiable. The asymmetry of key possession is the deciding factor *(6)*
- Collision dependence: the signature is computed over the digest, not the message, so any two messages sharing a digest share a valid signature. An attacker able to construct a collision obtains a signature on an innocuous document and attaches it to a malicious one, which verifies — without the signing algorithm being attacked or the private key exposed. A signature scheme's real strength is the minimum of the signing algorithm's strength and the hash's collision resistance *(5)*

---

# ESSAY BANDS (per question, out of 22)

| Marks | Standard |
|---|---|
| 19–22 | Complete and accurate; structure matches the verb; mechanisms explained rather than named |
| 15–18 | Sound and largely complete; some claims asserted without justification |
| 11–14 | Core facts present, reasoning thin, structure loose |
| 6–10 | Fragments of correct material, significant omissions or errors |
| 0–5 | Largely off-target |

---

# FINAL DIAGNOSTIC

| Total | Band |
|---|---|
| 70+ | A |
| 60–69 | B |
| 50–59 | C |
| 40–49 | D |
| Below 40 | Fail |

Record two numbers: your total, and your **Section C average**. Strong A and B with weak C means your problem is production under time pressure, not knowledge — fix it with the Set 6 skeletons, not by re-reading chapters. Weak A and B means recall is the gap, and Sets 4, 5 and 7 are the remedy.
