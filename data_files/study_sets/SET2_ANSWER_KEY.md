# DCIT418 MOCK — SET 2 ANSWER KEY
## Reasoning & Application

**Do not open until you have attempted the full paper.**

---

## SECTION A — APPLIED CALCULATION

### A1. Caesar cipher, CRYPTO, k = 5

| Letter | Value | +5 | mod 26 | Cipher |
|---|---|---|---|---|
| C | 2 | 7 | 7 | H |
| R | 17 | 22 | 22 | W |
| Y | 24 | 29 | 3 | D |
| P | 15 | 20 | 20 | U |
| T | 19 | 24 | 24 | Y |
| O | 14 | 19 | 19 | T |

**Ciphertext: HWDUYT**

---

### A2. Vigenère, SECURE, key KEY

| P | P val | K | K val | Sum | mod 26 | C |
|---|---|---|---|---|---|---|
| S | 18 | K | 10 | 28 | 2 | C |
| E | 4 | E | 4 | 8 | 8 | I |
| C | 2 | Y | 24 | 26 | 0 | A |
| U | 20 | K | 10 | 30 | 4 | E |
| R | 17 | E | 4 | 21 | 21 | V |
| E | 4 | Y | 24 | 28 | 2 | C |

**Ciphertext: CIAEVC**

---

### A3. Rail Fence depth 3, CRYPTOGRAPHY

```
Row 0:  C . . . T . . . A . . .
Row 1:  . R . P . O . R . P . Y
Row 2:  . . Y . . . G . . . H .
```

Row 0: C T A
Row 1: R P O R P Y
Row 2: Y G H

**Ciphertext: CTARPORPYYGH**

---

### A4. gcd(2024, 748)

```
2024 = 2 × 748 + 528
 748 = 1 × 528 + 220
 528 = 2 × 220 +  88
 220 = 2 ×  88 +  44
  88 = 2 ×  44 +   0
```

**gcd = 44** (last nonzero remainder)

---

### A5. Multiplicative inverse of 7 mod 26

Need b such that 7b ≡ 1 (mod 26).
7 × 15 = 105 = 4 × 26 + 1 ≡ 1 (mod 26)

**Inverse = 15.** Verification: 105 mod 26 = 1 ✓
(An inverse exists because gcd(7,26) = 1.)

---

### A6. GF(2^4) addition: 1101 + 1011

Polynomial form:
`1101` = x³ + x² + 1
`1011` = x³ + x + 1

Sum: (x³+x³) + x² + x + (1+1) = x² + x
(coefficients reduce mod 2, so the x³ pair and the constant pair both vanish)

Bitwise check (XOR):
```
1101
1011
----
0110
```

**Answer: x² + x = `0110`** — confirming that addition in GF(2^n) is exactly XOR.

---

### A7. GF(2^4) multiplication: (x³ + 1)(x + 1), modulus x⁴ + x + 1

**Step 1 — raw product:**
(x³ + 1)(x + 1) = x⁴ + x³ + x + 1

**Step 2 — degree check:** degree 4, which exceeds the maximum degree 3 for GF(2^4). Reduction required.

**Step 3 — reduce modulo x⁴ + x + 1** (subtract = XOR the coefficients):
```
  x⁴ + x³ + x + 1
− x⁴      + x + 1
-----------------
       x³
```
Remainder is x³, degree 3 < 4, so we stop.

**Answer: x³ = `1000`**

---

### A8. φ(84)

Prime factorisation: 84 = 2² × 3 × 7

φ(84) = 84 × (1 − 1/2) × (1 − 1/3) × (1 − 1/7)
= 84 × 1/2 × 2/3 × 6/7
= 42 × 2/3 = 28; 28 × 6/7 = 24

**φ(84) = 24**

---

### A9. Fermat's Little Theorem, p = 11, a = 3

Compute 3^10 mod 11:
```
3^1 = 3
3^2 = 9
3^3 = 27 ≡ 5   (27 − 22)
3^4 = 3×5 = 15 ≡ 4
3^5 = 3×4 = 12 ≡ 1
3^10 = (3^5)² ≡ 1² = 1
```

**3^10 ≡ 1 (mod 11)** ✓ Theorem verified.

---

### A10. Full RSA walkthrough, p = 3, q = 11

**a)** n = p × q = 3 × 11 = **33**

**b)** φ(n) = (p−1)(q−1) = 2 × 10 = **20**

**c)** Choose e = **3**. Valid because 1 < 3 < 20 and gcd(3, 20) = 1 (3 does not divide 20).

**d)** Find d such that 3d ≡ 1 (mod 20):
```
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
3 × 4 = 12
3 × 5 = 15
3 × 6 = 18
3 × 7 = 21 = 20 + 1 ≡ 1  ✓
```
**d = 7**

**e)** Encrypt P = 4: C = P^e mod n = 4³ mod 33 = 64 mod 33 = **31**

*(Sanity check on decryption: C^d mod n = 31^7 mod 33. Since 31 ≡ −2 (mod 33), (−2)^7 = −128, and 128 = 3×33 + 29 so 128 ≡ 29, giving −29 ≡ 4 (mod 33) ✓ — recovers P = 4.)*

**f)** Public key = **(e, n) = (3, 33)** ; Private key = **(d, n) = (7, 33)**

---

## SECTION B — REASONING & EXPLANATION

### B1. AES in ECB mode for a database backup

The strength of the underlying block cipher is irrelevant to the weakness being introduced. In ECB, each block is encrypted independently as C_i = E(K, P_i), with no dependence on position, IV, or any other block. Because E under a fixed key is deterministic, identical plaintext blocks always yield identical ciphertext blocks. A database backup contains enormous structural repetition (repeated field values, padding, null regions, repeated record headers), so the ciphertext exposes the plaintext's repetition pattern even though no key is recovered. The cipher is not broken; the mode leaks. **Recommend CBC or, better, CTR** — CBC chains each block against the previous ciphertext so identical plaintext blocks encrypt differently, while CTR XORs against a per-block counter-derived keystream, giving the same protection plus parallelisation and random access for large backups.

### B2. IV reuse in CBC

The argument confuses *secret* with *unpredictable and unique*. The IV need not be secret, but it must not repeat with the same key. In CBC, C_1 = E(K, P_1 ⊕ IV). With a fixed key and fixed IV, two messages sharing the same first plaintext block produce the same first ciphertext block, and this extends: identical leading blocks produce identical leading ciphertext until the messages first diverge. An attacker therefore learns whether two messages begin identically and exactly how many blocks they share before diverging — a direct plaintext information leak. With structured messages (fixed headers, repeated templates) this can reveal a great deal. The IV must be unpredictable and fresh per message.

### B3. Why the modulus in GF(2^n) must be irreducible

A field requires every nonzero element to have a multiplicative inverse. An irreducible polynomial cannot be factored into lower-degree polynomials, which is the polynomial analogue of primality. If a reducible modulus such as x⁴ is used, it factors trivially (x·x·x·x), and reduction becomes mere truncation of high-degree terms rather than true modular reduction; nonzero elements sharing a factor with the modulus then have no multiplicative inverse, so the structure collapses from a field to a ring. This is exactly the GF(p) situation: mod 6 fails as a field because 2 has no inverse (2×1..5 never yields 1 mod 6), while mod 7 succeeds because 7 is prime. Prime for integers, irreducible for polynomials — same requirement, same reason.

### B4. Rebutting "AES must be Feistel"

Multiple rounds and a key schedule are common to almost all modern block ciphers; neither is diagnostic of a Feistel structure. The defining property of a Feistel cipher is that the block is **split into halves**, with only one half transformed per round via the round function while the other passes through unchanged, the halves then swapping — which is what allows encryption and decryption to share one algorithm with reversed subkey order. AES splits nothing: the entire 128-bit State passes through SubBytes, ShiftRows, MixColumns and AddRoundKey every round. AES is a substitution-permutation network, and consequently its decryption requires genuinely inverse transformations (InvSubBytes, InvShiftRows, InvMixColumns), not merely reversed key ordering.

### B5. Why only CTR parallelises

In OFB the keystream is generated by iterated encryption of the previous keystream block: O_i = E(K, O_(i−1)). Each keystream block therefore depends on its predecessor, forming a strictly sequential chain — block i's keystream cannot be computed until blocks 1 through i−1 have been computed, regardless of the plaintext. In CTR the keystream for block i is E(K, Counter_i), and counter values are known independently and in advance for every i. Any block's keystream can therefore be computed immediately and in any order, enabling full parallelisation and random access. The shared property (keystream independent of *ciphertext*) gives both modes no error propagation; the differing property (keystream dependent on *previous keystream* vs. an independent counter) is what separates them on parallelism.

### B6. Why RSA decryption recovers the plaintext

Decryption computes C^d mod n = (P^e)^d mod n = P^(ed) mod n. By construction, d is the multiplicative inverse of e modulo φ(n), so ed ≡ 1 (mod φ(n)), which means ed = 1 + kφ(n) for some integer k. Therefore P^(ed) = P^(1 + kφ(n)) = P × (P^φ(n))^k. By **Euler's Theorem**, if gcd(P, n) = 1 then P^φ(n) ≡ 1 (mod n), so the whole bracketed term reduces to 1 and the expression collapses to P mod n. The correctness of RSA is thus a direct consequence of Euler's Theorem combined with the deliberate choice of d as e's inverse mod φ(n).

### B7. Attacker who learns φ(n)

Given (e, n) publicly and φ(n) leaked, the attacker computes d directly as the multiplicative inverse of e modulo φ(n) using the extended Euclidean algorithm — the exact computation the legitimate key owner performed. This yields the private key (d, n) and the system is fully broken. Further, knowing both n and φ(n) lets the attacker recover p and q outright: since n = pq and φ(n) = (p−1)(q−1) = n − p − q + 1, the sum p + q = n − φ(n) + 1 is known along with the product pq = n, so p and q are the roots of a solvable quadratic. This is why φ(n) is as sensitive as the private key itself, and why p and q must be discarded or protected after key generation — computing φ(n) requires knowing p and q, and the difficulty of obtaining them from n alone (integer factorisation) is precisely what RSA's security rests on.

### B8. Attacker reading Diffie-Hellman traffic

The attacker performs a **man-in-the-middle** attack: intercepting Y_A en route to Bob and substituting their own Y_M, and intercepting Y_B en route to Alice and substituting Y_M likewise. Alice then derives a shared key with the attacker while believing it is shared with Bob, and Bob derives a different shared key with the attacker believing it is shared with Alice. The attacker decrypts each incoming message with one key, reads it, re-encrypts with the other, and forwards it; both parties see coherent traffic and detect nothing. No private exponent was ever transmitted, and the discrete logarithm problem was never attacked — it was simply bypassed. The missing property is **authentication**: plain Diffie-Hellman provides no binding between a public value and a verified identity. The fix is to authenticate the exchange (digital signatures, certificates, or a pre-shared authenticated channel).

### B9. IoT recommendation

Recommend **elliptic curve cryptography**, specifically a 256-bit ECC key in place of 3072-bit RSA. Quantitatively, a 256-bit ECC key provides security comparable to a 3072-bit RSA key — roughly a twelvefold reduction in key size, with correspondingly smaller keys and signatures to store and transmit, and substantially cheaper arithmetic for a battery-constrained processor. These savings matter directly on devices limited in memory, bandwidth, and power. The security rests on the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**: given a base point G and Q = kG on the curve, recovering the scalar k is computationally infeasible, even though computing Q from k is cheap.

### B10. LCG keystream passing statistical tests

Statistical randomness and cryptographic unpredictability are different requirements. Statistical tests check that output is well distributed — uniform frequencies, no obvious correlations — which an LCG satisfies well, which is why it is fine for simulations and games. Cryptography additionally requires that an adversary who has already observed part of the output cannot predict the rest. An LCG fails this completely: from X_(n+1) = (aX_n + c) mod m, a handful of consecutive observed outputs is enough to solve for a, c, and m, after which the attacker reproduces the entire keystream and decrypts everything. Since a stream cipher's ciphertext is just plaintext XORed with the keystream, recovering the keystream recovers all plaintext. The property actually required is that of a **CSPRNG**: computational unpredictability of future (and past) output given any feasible amount of observed output.

---

## SCORING GUIDE

| Total /100 | Grade band |
|---|---|
| 85+ | A — reasoning is exam ready |
| 75–84 | A/B — sound, tighten precision on explanations |
| 65–74 | B — concepts held, application shaky; redo Section A |
| 55–64 | C — re-teach the weakest topics before the exam |
| Below 55 | Return to the chapters behind the missed questions |

**Marking note for Section B:** award partial credit generously for correct core reasoning even if phrasing is loose, but deduct where the answer states a fact without the *why*. Every Section B question is testing whether you can explain a mechanism, not name it.
