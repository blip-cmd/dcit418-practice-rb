# DCIT 418: SET 3 ANSWER KEY AND MARKING SCHEME

**Do not open until you have attempted the paper under timed conditions.**

---

# SECTION A: MULTIPLE CHOICE (50 marks)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|---|---|---|---|---|---|---|---|---|---|
| 1 | b | 11 | b | 21 | b | 31 | b | 41 | b |
| 2 | c | 12 | c | 22 | c | 32 | b | 42 | b |
| 3 | b | 13 | b | 23 | b | 33 | b | 43 | b |
| 4 | b | 14 | b | 24 | c | 34 | b | 44 | b |
| 5 | b | 15 | a | 25 | b | 35 | c | 45 | b |
| 6 | b | 16 | d | 26 | b | 36 | b | 46 | b |
| 7 | b | 17 | b | 27 | b | 37 | b | 47 | b |
| 8 | c | 18 | b | 28 | b | 38 | b | 48 | b |
| 9 | b | 19 | b | 29 | c | 39 | b | 49 | b |
| 10 | b | 20 | b | 30 | b | 40 | b | 50 | b |

**The ones built to catch you:**
- **Q2**: a digital signature is a *mechanism*; authentication, access control and non-repudiation are the *services* it can help deliver. The question is testing the service/mechanism distinction from X.800, not whether the listed items sound security-related.
- **Q11**: avalanche effect is the specific named design criterion; confusion and diffusion are the broader properties it exhibits, so the question wants the named criterion.
- **Q16**: AddRoundKey. The other three transformations are fixed and public; only AddRoundKey injects the secret key material.
- **Q22**: CTR, because each counter block is independently derivable without decrypting anything before it. CFB and OFB chain sequentially and cannot offer true random access.
- **Q35**: either secret prime factor, not the modulus or exponent, since either prime lets an attacker recompute φ(n) and then d directly.
- **Q39**: much smaller. ECC's best known attacks are fully exponential, unlike the sub-exponential attacks on RSA's factoring problem, so ECC keys stay small for equivalent security.

---

# SECTION B: FILL IN THE BLANKS (10 marks)

**51.** availability

**52.** service

**53.** steganography

**54.** diffusion

**55.** SubBytes

**56.** ECB (Electronic Codebook)

**57.** PRGA (Pseudo-Random Generation Algorithm)

**58.** discrete logarithm

**59.** collision resistance

**60.** non-repudiation

---

# SECTION C: PRACTICAL SCENARIOS (10 marks)

Mark each answer out of 5 using the bands below.

### Q61: Replay attack against an encrypted funds transfer
- Category and type: an **active attack**, specifically a **replay** *(2)*
- Why confidentiality alone did not help: the clerk never needed to read or alter the message, only resubmit a validly encrypted, previously observed message, so encryption by itself gives no protection against this attack *(1)*
- Service and mechanism: **data origin authentication combined with freshness (anti-replay) protection**, implemented via a mechanism such as a **sequence number, timestamp, or nonce bound into the message (or its MAC/signature) and checked by the receiver**, so a resubmitted message is rejected as stale or already seen *(2)*

*A full-mark answer names replay specifically, not just "active attack" in general, and names a concrete freshness mechanism, not just "authentication" in the abstract.*

### Q62: RSA used directly to encrypt bulk file transfers
- Problem one: **RSA is far slower than a symmetric cipher** for bulk data, since it relies on modular exponentiation over large numbers rather than simple byte-level operations, so encrypting a large volume of daily files directly with RSA is computationally impractical *(2)*
- Problem two: **RSA can only encrypt data smaller than its modulus**, so a large file cannot be encrypted in one RSA operation at all; splitting the file into many RSA-sized chunks multiplies the speed problem further *(2)*
- Correct approach: **hybrid encryption**, RSA (or another public-key algorithm) is used only to securely establish or transport a **symmetric session key** between the branches, and a fast symmetric cipher such as AES is then used to encrypt the actual file traffic under that session key *(1)*

*Accept "RSA encrypts the key, AES encrypts the data" as the minimum correct statement of the approach; full marks require naming at least one of the two concrete limitations above, not just asserting RSA is "slow."*

---

# FINAL DIAGNOSTIC

| Total | Band |
|---|---|
| 63+ | A |
| 56–62 | B |
| 46–55 | C |
| 35–45 | D |
| Below 35 | Fail |

This paper is almost entirely objective, so a low score on Sections A and B points at recall gaps, not writing-under-pressure gaps. Re-drill the chapter or topic behind each missed question using Sets 4, 5 and 7. A low Section C score despite strong A and B means you know the facts but have not practised applying them to a scenario, which is exactly what Set 6 is for.
