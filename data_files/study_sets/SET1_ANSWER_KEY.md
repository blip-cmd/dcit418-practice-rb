# DCIT418 MOCK — SET 1 ANSWER KEY
## Knowledge, Factual Recall & Vocabulary

**Do not open until you have attempted the full paper.**

---

## SECTION A — MULTIPLE CHOICE

| Q | Ans | Note |
|---|---|---|
| A1 | d | The three pillars are attack, mechanism, service. "Protocol" is not one. |
| A2 | b | Passive: eavesdropping without alteration. |
| A3 | c | Nothing changes, so you must stop it happening at all. |
| A4 | c | Authentication = entity is who it claims to be. |
| A5 | b | The key is independent input controlling the transformation. |
| A6 | b | Letter frequencies survive the substitution. |
| A7 | b | Digraphs, via the 5×5 matrix. |
| A8 | c | One-Time Pad has perfect secrecy. |
| A9 | b | Reorders letters, does not substitute them. |
| A10 | c | 64-bit block. |
| A11 | b | 56 effective bits; 64 stored, 8 are parity. |
| A12 | b | Same structure, reversed subkey order. |
| A13 | c | 16 rounds. |
| A14 | b | S-boxes are the only nonlinear step. |
| A15 | b | Small change in, large change out (~50% of bits). |
| A16 | c | Prime p guarantees every nonzero element has an inverse. |
| A17 | b | Inverse exists iff gcd = 1. |
| A18 | c | This is exactly the ring/field boundary. |
| A19 | b | 128-bit block always, regardless of key size. |
| A20 | b | 128→10, 192→12, 256→14. |
| A21 | c | SPN, not Feistel. |
| A22 | c | MixColumns. |
| A23 | b | ECB — deterministic per block. |
| A24 | d | CTR — counters are independent. |
| A25 | b | E only ever generates keystream. |
| A26 | b | Rivest Cipher 4 (Ron Rivest, 1987). |
| A27 | c | (p−1)(q−1). |
| A28 | b | a^(p−1) ≡ 1 (mod p). |
| A29 | b | Factoring large integers. |
| A30 | b | Discrete logarithm problem. |

---

## SECTION B — FILL IN THE BLANKS

**B1.** Confidentiality, Integrity, Availability

**B2.** Authenticity, Non-repudiation

**B3.** Masquerade, Replay, Modification of messages, Denial of Service (DoS)

**B4.** Release of message contents, Traffic analysis

**B5.** Authentication, Access Control, Data Confidentiality, Data Integrity, Non-repudiation, Availability
*(This is your repeat weak spot. Availability is the one you keep dropping.)*

**B6.** C = (P + k) mod 26

**B7.** Polyalphabetic

**B8.** Truly random; the same length; only once

**B9.** L_i = R_(i−1) ; R_i = L_(i−1) ⊕ F(R_(i−1), K_i)

**B10.** 48

**B11.** 8 S-boxes; 6 bits in; 4 bits out

**B12.** Greatest common divisor (GCD)

**B13.** Group

**B14.** Abelian

**B15.** x^8 + x^4 + x^3 + x + 1
*(Repeat weak spot. Note the x^4 term — not x^2 — and the trailing +1.)*

**B16.** XOR

**B17.** SubBytes, ShiftRows, MixColumns, AddRoundKey
*(Repeat weak spot: it is ShiftRows, never "ShiftCols".)*

**B18.** State

**B19.** AddRoundKey

**B20.** ECB, CBC, CFB, OFB, CTR

**B21.** Initialization Vector (IV)

**B22.** Counter value (or the nonce/counter pair with a given key)

**B23.** C_i = E(K, P_i ⊕ C_(i−1))

**B24.** Key Scheduling Algorithm (KSA); Pseudo-Random Generation Algorithm (PRGA)

**B25.** 256

**B26.** a^φ(n) ≡ 1 (mod n)

**B27.** Public key = (e, n); Private key = (d, n)

**B28.** C = P^e mod n ; P = C^d mod n
*(Repeat weak spot: the modulus is n, NOT φ(n). φ(n) appears only during key generation.)*

**B29.** q ; primitive root α

**B30.** Elliptic Curve Discrete Logarithm Problem (ECDLP)

---

## SECTION C — SHORT ANSWER

**C1.** A **security attack** is any action that compromises the security of information. A **security mechanism** is a process designed to detect, prevent, or recover from an attack. A **security service** is a processing or communication service that enhances security, implemented using one or more mechanisms.

**C2.** Passive attacks do not alter data or system state, so there is nothing observable to detect — the emphasis must be on prevention (typically encryption). Active attacks alter data or state, which makes them detectable, but they are extremely difficult to prevent absolutely given the range of possible vulnerabilities, so the emphasis shifts to detecting them and recovering from any damage.

**C3.** The OTP is unbreakable because the key is truly random, at least as long as the message, and never reused — this means the ciphertext is statistically independent of the plaintext, so no amount of ciphertext gives any information about the plaintext (perfect secrecy). It is impractical because generating and securely distributing a truly random key as long as the message is at least as hard as the original problem of securely sending the message.

**C4.** L_i = R_(i−1) and R_i = L_(i−1) ⊕ F(R_(i−1), K_i). The same algorithm works for decryption because XOR is its own inverse: running the identical round structure with the subkeys applied in reverse order (K_n down to K_1) exactly undoes each round. This means no separate decryption circuitry or code is required.

**C5.** Any five of: block size, key size, number of rounds, subkey generation algorithm complexity, round function F complexity, fast software encryption/decryption, ease of analysis.

**C6.** A 56-bit key gives only 2^56 ≈ 7.2 × 10^16 possible keys, which specialized hardware and distributed brute-force attacks have been able to exhaust in days or less since the late 1990s. The direct successor addressing this was Triple DES (applying DES three times to extend the effective key length), and later AES replaced it entirely.

**C7.** A **group** is a set with one operation satisfying closure, associativity, an identity element, and inverses. A **ring** is a set with two operations, forming an abelian group under addition, with multiplication that is associative and distributes over addition. A **field** is a ring in which multiplication is also commutative, has an identity, and — the key difference — every nonzero element has a multiplicative inverse, meaning division is possible.

**C8.** GF(2^n) needs every nonzero element to have a multiplicative inverse to qualify as a field. An irreducible polynomial cannot be factored into lower-degree polynomials, which is the polynomial analogue of a prime number. Exactly as GF(p) requires p to be prime (mod 6 fails because 2 has no inverse), GF(2^n) requires the modulus polynomial to be irreducible, or some nonzero elements lose their inverses and the structure is no longer a field.

**C9.** **SubBytes**: byte-by-byte substitution using a fixed S-box derived from GF(2^8) inverses, providing nonlinearity/confusion. **ShiftRows**: cyclic left shift of rows 0,1,2,3 by 0,1,2,3 positions, providing diffusion across columns. **MixColumns**: each column multiplied by a fixed matrix in GF(2^8), providing diffusion within a column. **AddRoundKey**: XOR of the State with the round subkey, the only step using the secret key.

**C10.** In a Feistel cipher only half the block is transformed each round while the other half passes through unchanged and the halves swap. AES transforms the entire 128-bit block every round through substitution and permutation layers — it is a substitution-permutation network, not a Feistel structure.

**C11.** MixColumns provides diffusion that is only useful when further rounds follow to compound it. Including it in the final round would add computation with no security benefit, and would also require an extra InvMixColumns step in decryption, complicating the inverse cipher for no gain.

**C12.** In ECB each block is encrypted independently as C_i = E(K, P_i), with no dependence on any other block, IV, or counter. Because E with a fixed key is a deterministic function, identical plaintext blocks always produce identical ciphertext blocks (if P_i = P_j then C_i = C_j). This leaks the structure and repetition pattern of the plaintext directly into the ciphertext. All other modes fix this by mixing in something that varies block to block.

**C13.** In CFB, the block cipher E is never applied to the plaintext — it is applied only to the IV or the previous ciphertext block to generate a keystream, which is then XORed with the plaintext: C_i = P_i ⊕ E(K, C_(i−1)). To decrypt, you regenerate the identical keystream using E again and XOR it against the ciphertext. Since XOR is self-inverse, the same keystream recovers plaintext from ciphertext, so D is never needed.

**C14.** The IV in CBC/CFB/OFB must be unpredictable (random-looking) and must not be reused with the same key, because its role is to randomize the first block so identical messages encrypt differently. The counter in CTR does not need to be unpredictable — it needs to be **unique**: the (key, counter) pair must never repeat across the system's lifetime. Uniqueness rather than randomness is the requirement.

**C15.** A PRNG is a deterministic algorithm producing statistically random-looking output from a seed, but observing its output may allow an attacker to deduce the internal parameters and predict future values. A CSPRNG is designed so that predicting future or past output is computationally infeasible even given a substantial portion of the sequence. An LCG (X_(n+1) = (aX_n + c) mod m) fails cryptographically because observing a few consecutive outputs lets an attacker solve for a, c, and m and then predict the entire sequence.

**C16.** **KSA (Key Scheduling Algorithm)** initializes a 256-byte state array S with values 0–255 and shuffles it into a key-dependent permutation using the secret key (cycled to fill 256 bytes if shorter). **PRGA (Pseudo-Random Generation Algorithm)** then continuously swaps entries in S using two index pointers and emits one keystream byte per step, which is XORed with plaintext. RC4 is deprecated because statistical biases in its early keystream bytes allow attackers to recover key or plaintext information given enough ciphertext.

**C17.** **Fermat's Little Theorem**: if p is prime and a is not divisible by p, then a^(p−1) ≡ 1 (mod p). **Euler's Theorem**: if gcd(a,n) = 1, then a^φ(n) ≡ 1 (mod n). Euler's Theorem generalizes Fermat's to any modulus n, not just primes. Fermat's is the special case where n = p is prime, since φ(p) = p − 1.

**C18.**
1. Choose two large distinct primes p and q.
2. Compute n = p × q.
3. Compute φ(n) = (p−1)(q−1).
4. Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1.
5. Compute d as the multiplicative inverse of e mod φ(n), i.e. e × d ≡ 1 (mod φ(n)).
Public key = (e, n); private key = (d, n).

**C19.** Condition 1: gcd(e, φ(n)) = 1 — e must be coprime to φ(n). Condition 2: e × d ≡ 1 (mod φ(n)) — d is the multiplicative inverse of e modulo φ(n). The second depends on the first because a multiplicative inverse mod φ(n) exists only when the element is coprime to φ(n); if e were not coprime, no valid d would exist.

**C20.** An attacker intercepts the exchange and conducts a separate Diffie-Hellman exchange with each party, substituting their own public value in each direction. Alice ends up sharing a key with the attacker believing it is Bob, and Bob does the same, letting the attacker decrypt, read, and re-encrypt all traffic. It is possible because plain Diffie-Hellman provides **no authentication** — nothing binds a public value to a verified identity.

**C21.** ECC achieves equivalent security to RSA with substantially smaller key sizes — for example a 256-bit ECC key offers security comparable to a 3072-bit RSA key. This means faster computation, lower storage, and less bandwidth, which is why ECC is preferred in mobile and constrained environments.

---

## SCORING GUIDE

| Total | Grade band |
|---|---|
| 90–100 | A — exam ready |
| 80–89 | A/B — minor gaps, drill the misses |
| 70–79 | B — solid but revisit weak sections |
| 60–69 | C — re-read the weakest 2–3 chapters |
| Below 60 | Re-teach needed before the exam |

Log every question you got wrong. Those become your Set 2 focus areas.
