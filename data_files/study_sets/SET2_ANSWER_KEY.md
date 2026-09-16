# DCIT418 MOCK — SET 2 ANSWER KEY
## Reasoning & Application, Chapters 1–13

**Do not open until you have attempted the paper.**

**Marking principle for Section B:** award marks for the *mechanism*, not the label. An answer that names the right concept without explaining why it follows earns at most half.

---

# SECTION A — SIMPLE WORKED EXAMPLES

### A1. Caesar, CRYPTO, shift 5

| Letter | Value | +5 mod 26 | Cipher |
|---|---|---|---|
| C | 2 | 7 | H |
| R | 17 | 22 | W |
| Y | 24 | 3 | D |
| P | 15 | 20 | U |
| T | 19 | 24 | Y |
| O | 14 | 19 | T |

**HWDUYT**

### A2. Vigenère, SECURE, key KEY

| P | val | K | val | Sum | mod 26 | C |
|---|---|---|---|---|---|---|
| S | 18 | K | 10 | 28 | 2 | C |
| E | 4 | E | 4 | 8 | 8 | I |
| C | 2 | Y | 24 | 26 | 0 | A |
| U | 20 | K | 10 | 30 | 4 | E |
| R | 17 | E | 4 | 21 | 21 | V |
| E | 4 | Y | 24 | 28 | 2 | C |

**CIAEVC**

### A3. Rail Fence depth 3, CRYPTOGRAPHY

```
Row 0:  C . . . T . . . A . . .
Row 1:  . R . P . O . R . P . Y
Row 2:  . . Y . . . G . . . H .
```
**CTARPORPYYGH**

### A4. gcd(2024, 748)

```
2024 = 2 × 748 + 528
 748 = 1 × 528 + 220
 528 = 2 × 220 +  88
 220 = 2 ×  88 +  44
  88 = 2 ×  44 +   0
```
**gcd = 44**

### A5. Inverse of 7 mod 26

7 × 15 = 105 = 4 × 26 + 1 ≡ 1 (mod 26). **Inverse = 15.** It exists because gcd(7, 26) = 1.

### A6. GF(2⁴): 1101 + 1011

`1101` = x³ + x² + 1, `1011` = x³ + x + 1.
Sum: the x³ terms cancel and the constants cancel (coefficients mod 2), leaving **x² + x = `0110`**.
```
1101 XOR 1011 = 0110
```
Equivalent to **XOR**. Addition in GF(2ⁿ) is always XOR.

### A7. Totients

φ(15): 15 = 3 × 5, distinct primes, so φ(15) = (3−1)(5−1) = **8**.
φ(17): 17 is prime, so φ(p) = p − 1 = **16**.

### A8. RSA key generation, p = 3, q = 11

n = 33. φ(n) = 2 × 10 = 20.
e = 3 is valid: 1 < 3 < 20 and gcd(3, 20) = 1.
d: 3d ≡ 1 (mod 20). 3 × 7 = 21 = 20 + 1 ≡ 1, so **d = 7**.
Public key (3, 33); private key (7, 33).
*(e = 7 with d = 3 is equally valid. Mark on internal consistency.)*

---

# SECTION B — REASONING & EXPLANATION

### B1. AES in ECB
The strength of the cipher is irrelevant to the weakness introduced. ECB computes C_i = E(K, P_i) with no dependence on position, IV, or any other block, and E under a fixed key is a deterministic function, so if P_i = P_j then necessarily C_i = C_j. A database backup is full of structural repetition — repeated headers, padding, null regions, recurring field values — so the ciphertext reproduces the plaintext's pattern of repetition exactly. No key is recovered and the cipher is not broken; the information leaks through the pattern of equalities between blocks. **Recommend CBC or CTR**: CBC chains each block against the previous ciphertext, seeded by an IV, so identical plaintext blocks encrypt differently; CTR XORs against a counter-derived keystream, giving the same protection plus parallelism and random access, which matter for a large backup.

### B2. Keyspace size
Keyspace size bounds only the cost of *brute force*; it says nothing about whether a cheaper attack exists. A monoalphabetic cipher maps each plaintext letter to one ciphertext letter consistently, so English letter frequencies, digraph patterns and word shapes pass through the encryption untouched. The attacker never enumerates keys — they read the structure directly off the ciphertext via frequency analysis. DES is criticised on entirely different grounds: it has no comparable structural weakness, so brute force genuinely is the best available attack, which makes the keyspace the binding constraint. **The principle violated:** a large keyspace is necessary but nowhere near sufficient, and security must be assessed against the best known attack, not the most obvious one.

### B3. Half-block transformation in Feistel
The benefit is that **decryption never requires inverting F**. Because only half the block changes per round and the change is applied by XOR, running the identical structure with the subkeys in reverse order exactly undoes the encryption. F is therefore never inverted and need not even be invertible. This is a substantial practical gain: F can be arbitrarily complex, nonlinear and one-way, chosen purely for cryptographic strength rather than constrained by invertibility, and a single implementation in hardware or code serves both directions. Transforming the whole block would mix faster but would force every component to be invertible and would require a separate inverse cipher — precisely the trade-off AES later accepted.

### B4. Irreducible modulus in GF(2ⁿ)
A field requires every nonzero element to have a multiplicative inverse. An irreducible polynomial cannot be factored into lower-degree polynomials, which is the polynomial analogue of primality, so no nonzero element can share a factor with the modulus. If a reducible modulus such as x⁴ is used, it factors trivially, reduction degenerates into mere truncation of high-degree terms rather than genuine modular reduction, and elements sharing a factor with the modulus lose their inverses — the structure collapses from a field to a ring. **The parallel with GF(p) is exact:** mod 6 fails because 2 has no inverse (2 × 1…5 never yields 1), while mod 7 succeeds because 7 is prime and no element below it shares a factor. Prime for integers, irreducible for polynomials, identical reason.

### B5. AES is not Feistel
Multiple rounds and a key schedule are common to nearly all modern block ciphers and are not diagnostic of anything. The defining property of a Feistel cipher is that the block is **split into halves**, with only one half transformed per round while the other passes through unchanged and the halves swap — which is what allows one algorithm with reversed subkeys to serve both directions. AES splits nothing: the entire 128-bit State passes through SubBytes, ShiftRows, MixColumns and AddRoundKey every round. It is a **substitution-permutation network**, and the consequence is visible in decryption, which requires genuinely inverse transformations (InvSubBytes, InvShiftRows, InvMixColumns) rather than merely reversed key ordering.

### B6. Why GF(2⁸) rather than mod 256
The integers modulo 256 do **not** form a field, because 256 is composite: every even value shares the factor 2 with the modulus and therefore has no multiplicative inverse. Since AES requires invertible transformations — its S-box is constructed from multiplicative inverses, and MixColumns must be reversible for decryption — arithmetic mod 256 would leave half the byte values without inverses and the construction would simply fail. GF(2⁸) solves this: it has exactly 256 elements so it still maps onto a byte, but because it is built as polynomials modulo an irreducible polynomial, all 255 nonzero elements have inverses. AES gets byte-sized arithmetic *and* a genuine field, which mod-256 integers cannot deliver.

### B7. IV reuse in CBC
The argument confuses *secret* with *unpredictable and unique*. The IV need not be secret, but it must not repeat with the same key. CBC computes C₁ = E(K, P₁ ⊕ IV), so with a fixed key and fixed IV, two messages sharing a first plaintext block produce an identical first ciphertext block — and because chaining carries forward, they remain identical for as long as the messages agree. The attacker therefore learns whether two messages begin the same way and exactly how many blocks they share before diverging, which with structured messages (fixed headers, templates, forms) can reveal a great deal. A second, sharper problem: the IV is XORed directly with plaintext, so a *predictable* IV lets an attacker who can influence plaintext cancel it and mount a chosen-plaintext distinguishing attack. The IV must be unpredictable and fresh per message.

### B8. Why only CTR parallelises
The difference lies in what each keystream block is derived from. OFB generates its keystream by iterated encryption of the previous keystream block, O_i = E(K, O_(i−1)), so block i's keystream cannot be computed until blocks 1 through i−1 exist — an inherently serial chain that no amount of hardware can shortcut. CTR derives block i's keystream as E(K, Counter_i), and every counter value is known in advance and independently of every other, so any block, or all blocks simultaneously, can be computed in any order. The property they share (keystream independent of the *ciphertext*) is why neither propagates errors; the property that differs (keystream dependent on *itself* versus on an independent counter) is what governs parallelism.

### B9. LCG keystream
Statistical randomness and cryptographic unpredictability are different requirements, and test suites check only the former. An LCG produces well-distributed, uncorrelated-looking output, which is entirely adequate for a simulation where the adversary is sampling error rather than an intelligent attacker. Cryptography additionally demands that an adversary who has seen part of the output cannot predict the rest, and the LCG fails absolutely: X_(n+1) = (aX_n + c) mod m is a simple linear relation, so a handful of consecutive outputs suffices to solve for a, c and m, after which the entire keystream past and future is reproducible. Since a stream cipher's ciphertext is plaintext XORed with the keystream, recovering the keystream recovers every message. **The property required is that of a CSPRNG**: computational unpredictability given any feasible amount of observed output.

### B10. RSA correctness
Decryption computes C^d mod n = (P^e)^d = P^(ed) mod n. By construction d is the multiplicative inverse of e modulo φ(n), so ed ≡ 1 (mod φ(n)), meaning ed = 1 + kφ(n) for some integer k. Therefore P^(ed) = P^(1 + kφ(n)) = P × (P^φ(n))^k. By **Euler's Theorem**, P^φ(n) ≡ 1 (mod n) whenever gcd(P, n) = 1, so the bracketed term reduces to 1 and the whole expression collapses to P mod n. **Fermat's Little Theorem does not apply** because it holds only for a prime modulus, and the RSA modulus n = pq is composite. Fermat's is the special case of Euler's where n is prime; it underpins the primality testing used to find p and q, but it cannot carry the correctness argument for the composite modulus itself.

### B11. Attacker who learns φ(n)
With (e, n) public and φ(n) known, the attacker computes d directly as the multiplicative inverse of e modulo φ(n) using the extended Euclidean algorithm — the very calculation the legitimate key owner performed. That yields the private key (d, n) and the system is fully broken. Worse, knowing both n and φ(n) recovers p and q outright: since φ(n) = (p−1)(q−1) = n − p − q + 1, the sum p + q = n − φ(n) + 1 is known alongside the product pq = n, so p and q are the roots of a solvable quadratic. **Implication:** φ(n), p and q are each exactly as sensitive as the private key. Publishing n is safe only because deriving p and q from n alone requires integer factorisation, and that difficulty is the entirety of RSA's security. p and q should be discarded or protected after key generation.

### B12. Diffie-Hellman man-in-the-middle
The attacker intercepts Y_A en route to Bob and substitutes their own Y_M, and intercepts Y_B en route to Alice and substitutes Y_M likewise. Alice then derives a shared key with the attacker while believing it is shared with Bob; Bob derives a different shared key with the attacker while believing it is shared with Alice. The attacker decrypts each incoming message with one key, reads it, re-encrypts with the other and forwards it, so both parties see coherent traffic and detect nothing. **No private value was transmitted and no discrete logarithm was solved** — the attacker ran two perfectly ordinary, mathematically sound exchanges. The protocol was bypassed rather than broken, because plain Diffie-Hellman provides **no authentication**: nothing binds a public value to a verified identity. The remedy is to authenticate the exchange with signatures or certificates.

### B13. IoT recommendation
Recommend **elliptic curve cryptography**, specifically a 256-bit ECC key in place of 3072-bit RSA. Quantitatively, 256-bit ECC provides security comparable to 3072-bit RSA — roughly a twelvefold reduction in key size, with correspondingly smaller keys and signatures to store and transmit and substantially cheaper arithmetic for a battery-constrained processor. These savings bear directly on devices limited in memory, bandwidth and power. **The hard problem is the Elliptic Curve Discrete Logarithm Problem (ECDLP)**: given a base point G and Q = kG, recovering the scalar k is infeasible even though computing Q from k is cheap. The size gap arises because factorisation admits sub-exponential attacks (the number field sieve) forcing RSA keys to grow quickly, while the best attacks on well-chosen curves remain fully exponential.

### B14. Hash sent alongside the file
A plain hash is **unkeyed**, so anyone can compute it — including an attacker sitting on the channel. They intercept the file, alter it, recompute the SHA-256 digest of the altered file, and forward both. The recipient recomputes the digest, finds it matches, and accepts the tampered file with no indication anything is wrong. A bare hash therefore detects **accidental corruption** — transmission errors, disk faults — but offers nothing against a deliberate adversary who can modify both the file and the digest. **The fix is a MAC**, which incorporates a secret key into the computation so that only key holders can generate a valid tag; an attacker without the key cannot produce a matching tag for their altered message. HMAC is the standard construction. A digital signature also works and additionally gives non-repudiation.

### B15. Unsalted password hashes
Preimage resistance means the attacker cannot *invert* the digest mathematically, and that part holds. But they do not need to: they can **guess**. With the file in hand they hash candidate passwords offline and compare, at billions of attempts per second on commodity hardware, and common passwords fall immediately. Because the hashes are unsalted, two identical digests reveal two users with the same password, and a single precomputed table (a rainbow table) attacks the entire file at once rather than one account at a time — the cost of cracking a thousand accounts is barely more than cracking one. **The property doing the work is preimage resistance; what is missing is anything that makes guessing expensive or per-user.** The fixes are a unique random salt per user, which defeats precomputation and shared-password disclosure, and a deliberately slow, work-factored function such as bcrypt, scrypt or Argon2 rather than a fast general-purpose hash. SHA-256's speed, a virtue elsewhere, is a liability here.

### B16. MAC and the denied message
A MAC is computed with a **single shared secret key held by both parties**, so either of them was equally capable of producing any valid tag. When the sender denies authorship, the receiver can demonstrate that the tag is valid, but not that *the sender* made it — the receiver could have forged it themselves, having the same key. A third party adjudicating the dispute has no basis to prefer one account over the other, so the MAC establishes that the message came from *someone holding the key* and nothing more. It therefore provides integrity and authentication but **not non-repudiation**. **What was needed is a digital signature**: produced with the sender's private key, which only the sender holds, and verifiable by anyone with the corresponding public key. Since no one else could have produced it, the sender cannot credibly deny it and a third party can verify this independently. The asymmetry of key possession is exactly what makes non-repudiation possible.

---

## SCORING GUIDE

| Total /100 | Band |
|---|---|
| 85+ | A — reasoning is exam ready |
| 75–84 | A/B — sound, tighten precision |
| 65–74 | B — concepts held, explanation thin |
| 55–64 | C — re-teach the weakest topics |
| Below 55 | Return to the chapters behind the misses |

**Diagnostic.** Score each Section B answer against one test: did you explain the *mechanism*, or only name the concept? "Because ECB is deterministic" is half an answer. "Because E under a fixed key is deterministic, so equal plaintext blocks force equal ciphertext blocks, and real data repeats" is the whole one. That gap is where essay marks live.
