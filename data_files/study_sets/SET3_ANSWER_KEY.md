# DCIT418 MOCK EXAMINATION — SET 3
## ANSWER KEY AND MARKING SCHEME

**Do not open until you have attempted the full paper under timed conditions.**

---

# SECTION A — OBJECTIVE (20 marks)

| Q | Ans | Note |
|---|---|---|
| 1 | c | DoS is active: visible in effect, but near-impossible to prevent absolutely. The others are passive. |
| 2 | b | Substitution-permutation network — the AES structure. |
| 3 | c | 8 S-boxes, 6 bits in, 4 bits out each. |
| 4 | b | Prime for GF(p), irreducible for GF(2^n) — same requirement. |
| 5 | c | 14 rounds for a 256-bit key. |
| 6 | b | CFB: stream-like, errors span two blocks. |
| 7 | c | The mode does not alter the underlying cipher's strength — a common misconception. |
| 8 | c | O_i = E(K, O_(i−1)), which is why OFB cannot parallelise. |
| 9 | b | PRGA produces keystream; KSA does the initialisation. |
| 10 | b | 17 is prime, so φ(17) = 16. |
| 11 | b | Multiplicative inverse requires gcd = 1. |
| 12 | b | Modulus is n, never φ(n). |
| 13 | c | φ(n) appears only in key generation, to compute d. |
| 14 | b | Y_A is public; X_A never leaves the party. |
| 15 | d | 256-bit ECC ≈ 3072-bit RSA. |
| 16 | b | Identity element of the elliptic curve group. |
| 17 | c | Non-repudiation. |
| 18 | b | Polyalphabetic: one plaintext letter maps to different ciphertext letters. |
| 19 | b | That block and the next. |
| 20 | c | Small input change, large output change. |

---

# SECTION B — SHORT ANSWER (30 marks)

**21.** (4) Authentication, Access Control, Data Confidentiality, Data Integrity, Non-repudiation, Availability.
*Award 4 for all six; 2 for four or five; 0 for three or fewer.*

**22.** (4) L_i = R_(i−1) ; R_i = L_(i−1) ⊕ F(R_(i−1), K_i). *(2 marks)*
Decryption uses the same algorithm because XOR is self-inverse, so applying the identical round structure with the subkeys in reverse order (K_n … K_1) exactly undoes each round. *(2 marks)*

**23.** (4) SubBytes, ShiftRows, MixColumns, AddRoundKey. *(2 marks)*
MixColumns is omitted in the final round because its diffusion is only useful if further rounds follow; including it would cost computation with no security gain and would complicate the inverse cipher. *(2 marks)*

**24.** (4) C = P^e mod **n** ; P = C^d mod **n**. *(2 marks for formulas, 2 for correctly identifying n — not φ(n) — as the modulus in both.)*

**25.** (4)
Condition 1: gcd(e, φ(n)) = 1. *(1)*
Condition 2: e × d ≡ 1 (mod φ(n)), i.e. d is the multiplicative inverse of e mod φ(n). *(1)*
The second cannot hold without the first because a multiplicative inverse modulo φ(n) exists only for elements coprime to φ(n); if gcd(e, φ(n)) ≠ 1 then no such d exists at all. *(2)*

**26.** (4) The IV in CBC must be **unpredictable** (random-looking) and not reused with the same key, because its role is to randomise the first block so identical messages produce different ciphertext. *(2)* The counter in CTR need not be unpredictable but must be **unique** — the (key, counter) pair must never repeat over the system's lifetime. Uniqueness, not randomness, is the requirement. *(2)*

**27.** (3) Euler's Theorem: if gcd(a, n) = 1 then a^φ(n) ≡ 1 (mod n). *(2)* It generalises Fermat's Little Theorem, which is the special case where n = p is prime, since φ(p) = p − 1 giving a^(p−1) ≡ 1 (mod p). *(1)*

**28.** (3) x⁸ + x⁴ + x³ + x + 1. *(2)* It is the irreducible polynomial modulo which all GF(2^8) multiplication in AES is reduced, ensuring the byte values form a proper field so that every nonzero element has a multiplicative inverse and the transformations are invertible. *(1)*

---

# SECTION C — LONG ANSWER

## Q29 — Symmetric cipher structure

**a) (5)** Diagram must show: block split into L_(i−1) and R_(i−1); R_(i−1) fed into F together with subkey K_i; output of F XORed with L_(i−1); the halves crossing so that L_i = R_(i−1) and R_i = L_(i−1) ⊕ F(R_(i−1), K_i).
*1 mark each for: correct split, F with subkey input, XOR placement, correct crossover, both equations stated.*

**b) (4)** Block size 64 bits; stored key 64 bits; effective key 56 bits; 16 rounds. *(3)* The discrepancy is because every eighth bit of the stored key is a parity bit, not used in the cryptographic transformation, leaving 56 bits of actual key material. *(1)*

**c) (4)** In order:
1. **Expansion (E)**: 32-bit right half expanded to 48 bits by duplicating certain bits.
2. **Subkey XOR**: the 48-bit expanded value is XORed with the 48-bit round subkey K_i.
3. **S-box substitution**: the 48 bits pass through 8 S-boxes, each taking 6 bits and producing 4, reducing 48 bits to 32. This is the only nonlinear stage.
4. **Permutation (P)**: the 32 output bits are permuted to spread influence, providing diffusion.
*1 mark per stage, including correct bit widths.*

**d) (3)** A 56-bit key admits only 2^56 ≈ 7.2 × 10^16 keys, which purpose-built hardware and distributed effort have been able to brute-force since the late 1990s. *(1)* The successors were **Triple DES**, which applies DES three times to extend the effective key length, and ultimately **AES**, which replaced DES as the standard. *(2)*

---

## Q30 — Finite field arithmetic and AES

**a) (5)** Group: a set with one operation satisfying closure, associativity, an identity element and inverses. *(1)* Ring: a set with two operations, forming an abelian group under addition, with multiplication associative and distributive over addition. *(2)* Field: a ring in which multiplication is also commutative with an identity, and — the distinguishing property — **every nonzero element has a multiplicative inverse**, so division is defined. *(2)*

**b) (5)**
Raw product: (x³ + x + 1) × x = x⁴ + x² + x *(2)*
Degree 4 exceeds the maximum degree 3 for GF(2^4), so reduce modulo x⁴ + x + 1: *(1)*
```
  x⁴ + x² + x
− x⁴      + x + 1
------------------
       x²     + 1
```
Final answer: **x² + 1 = `0101`** *(2)*

**c) (4)** A field requires every nonzero element to have a multiplicative inverse. An irreducible polynomial cannot be factored into lower-degree polynomials — the polynomial analogue of a prime. *(2)* If a reducible modulus is used, elements sharing a factor with it have no inverse and the structure degrades from a field to a ring. This mirrors GF(p) exactly: mod 6 fails because 2 has no inverse, while mod 7 succeeds because 7 is prime. *(2)*

**d) (2)** **MixColumns** relies on GF(2^8) arithmetic, multiplying each column of the State by a fixed matrix. *(1)* Its purpose is diffusion — spreading the influence of each byte across the whole column. *(1)* *(Credit also given for noting the S-box in SubBytes is constructed from GF(2^8) multiplicative inverses.)*

---

## Q31 — Modes of operation

**a) (5)** *(1 mark each)*
- ECB: C_i = E(K, P_i)
- CBC: C_i = E(K, P_i ⊕ C_(i−1)), with C_0 = IV
- CFB: C_i = P_i ⊕ E(K, C_(i−1)), with C_0 = IV
- OFB: O_i = E(K, O_(i−1)) with O_0 = IV; C_i = P_i ⊕ O_i
- CTR: C_i = P_i ⊕ E(K, Counter_i)

**b) (5)**

| Mode | Error propagation | Stream cipher? | Parallelisable |
|---|---|---|---|
| ECB | Confined to that block | No | Yes |
| CBC | That block + the next | No | Decrypt only |
| CFB | That block + the next | Yes | Decrypt only |
| OFB | None | Yes | No |
| CTR | None | Yes | Yes (both directions) |

*1 mark per correct row.*

**c) (3)** In ECB each block is encrypted independently as C_i = E(K, P_i), with no dependence on position or any other block. *(1)* E under a fixed key is a deterministic function, so identical plaintext blocks necessarily produce identical ciphertext blocks. *(1)* An image contains large regions of repeated pixel values, so this repetition survives into the ciphertext and the image's structure remains visible despite encryption. *(1)*

**d) (3)** In CFB the block cipher is never applied to the plaintext; E is applied only to the IV or previous ciphertext to generate a keystream, which is then XORed with the plaintext. *(1)* To decrypt, the receiver regenerates the identical keystream using E on the same inputs. *(1)* Because XOR is self-inverse, XORing that keystream against the ciphertext returns the plaintext, so D is never required. *(1)*

---

## Q32 — Public-key cryptography and RSA

**a) (4)**
1. Choose two large distinct primes p and q.
2. Compute n = p × q.
3. Compute φ(n) = (p − 1)(q − 1).
4. Choose e with 1 < e < φ(n) and gcd(e, φ(n)) = 1.
5. Compute d as the multiplicative inverse of e mod φ(n).
*1 mark per two steps, plus correct statement that public key = (e, n) and private key = (d, n).*

**b) (6)**
n = 5 × 11 = **55** *(1)*
φ(n) = 4 × 10 = **40** *(1)*
Choose e = **3**: valid because 1 < 3 < 40 and gcd(3, 40) = 1. *(2 — 1 for a valid choice, 1 for the justification)*
Find d with 3d ≡ 1 (mod 40): *(2)*
```
3 × 27 = 81 = 2 × 40 + 1 ≡ 1 (mod 40)
```
**d = 27.** Public key (3, 55); private key (27, 55).
*(Other valid e are acceptable — e.g. e = 7 gives d = 23, since 7 × 23 = 161 = 4 × 40 + 1. Mark on internal consistency.)*

**c) (3)** C = P^e mod n = 3³ mod 55 = 27 mod 55 = **27**.
*2 marks for correct method, 1 for the answer. Note the modulus is n = 55, not φ(n) = 40.*

**d) (3)** C^d mod n = (P^e)^d = P^(ed) mod n. Since ed ≡ 1 (mod φ(n)), we may write ed = 1 + kφ(n), so P^(ed) = P × (P^φ(n))^k. *(2)* By **Euler's Theorem**, P^φ(n) ≡ 1 (mod n) when gcd(P, n) = 1, so the expression collapses to P mod n, recovering the plaintext exactly. *(1)*

---

## Q33 — Key exchange and elliptic curves

**a) (6)**
Public parameters: a large prime q and a primitive root α of q, both known to all parties including attackers. *(1)*
Alice chooses a secret X_A < q and computes Y_A = α^(X_A) mod q, sending Y_A to Bob. *(1)*
Bob chooses a secret X_B < q and computes Y_B = α^(X_B) mod q, sending Y_B to Alice. *(1)*
Alice computes K = Y_B^(X_A) mod q; Bob computes K = Y_A^(X_B) mod q. *(1)*
These agree because: *(2)*
```
Y_B^(X_A) = (α^(X_B))^(X_A) = α^(X_A·X_B)
Y_A^(X_B) = (α^(X_A))^(X_B) = α^(X_A·X_B)
```
Both reduce to the same value mod q, so the shared key is identical without ever transmitting it.

**b) (3)** The **discrete logarithm problem**. *(1)* Computing α^X mod q is cheap by fast modular exponentiation, but recovering X from α, q and α^X mod q is computationally infeasible for large q. *(2)* Easy forward, hard backward — a one-way function.

**c) (4)** The attacker intercepts Y_A and forwards their own value Y_M to Bob, and intercepts Y_B and forwards Y_M to Alice. *(2)* Alice establishes a shared key with the attacker believing it is with Bob, and Bob does likewise; the attacker decrypts, reads, re-encrypts and forwards all traffic, invisible to both. *(1)* This is possible because plain Diffie-Hellman provides **no authentication** — nothing binds a public value to a verified identity. *(1)*

**d) (3)** Equation: y² = x³ + ax + b. *(1)* In cryptography x and y are drawn from a finite field, typically Z_p (so the equation is taken mod p) or GF(2^m), together with a point at infinity serving as the group identity. *(1)* Main advantage: equivalent security at far smaller key sizes — 256-bit ECC ≈ 3072-bit RSA — giving faster computation and lower storage and bandwidth. *(1)*

---

# GRADE BANDS

| Total /100 | Band |
|---|---|
| 70+ | A |
| 60–69 | B |
| 50–59 | C |
| 40–49 | D |
| Below 40 | Fail — return to the chapters behind the missed questions |

## Post-mock diagnostic

For every mark lost, record the **chapter**, not just the question. Then rank chapters by marks lost and spend remaining revision time strictly in that order. Do not revise what you already scored well on — it feels productive and buys nothing.
