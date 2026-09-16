# DCIT418 — SET 4 ANSWER KEY
## MCQ Drill, Chapters 1–13

Mark strictly. Any question you dotted as a guess counts as wrong even if correct — you want your score to reflect knowledge, not luck.

---

| Q | Ans | Note |
|---|---|---|
| 1 | c | CIA is Confidentiality, Integrity, Availability. Authentication is an additional objective, not part of the triad. |
| 2 | b | Authentication. |
| 3 | b | Passive — observation without alteration. |
| 4 | b | Active attacks alter state so they are detectable, but the attack surface is too broad to prevent absolutely. |
| 5 | c | Attack, mechanism, service. |
| 6 | b | Replay alters the communication, so it is active. |
| 7 | c | Non-repudiation. |
| 8 | b | System integrity concerns the system functioning unimpaired; data integrity concerns the data. |
| 9 | c | The symmetric model has no public key. |
| 10 | b | A fixed shift is monoalphabetic. |
| 11 | b | Digraphs via the 5×5 matrix. |
| 12 | b | I and J share a cell. |
| 13 | b | Polyalphabetic — one plaintext letter maps to several ciphertext letters. |
| 14 | c | One-time pad. |
| 15 | b | Reorders without substituting. |
| 16 | b | Steganography hides that a message exists at all. |
| 17 | b | Mechanical polyalphabetic substitution with a very long effective period. |
| 18 | b | Frequency analysis, not brute force, is the attack. |
| 19 | c | 64 bits. |
| 20 | b | 56 effective; 64 stored with 8 parity bits. |
| 21 | c | 16. |
| 22 | b | Same algorithm, reversed subkey order. |
| 23 | b | S-boxes. Everything else is linear. |
| 24 | c | IP and IP⁻¹ are key-independent and public, so they add no security. |
| 25 | b | Small in, large out. |
| 26 | b | Confusion and diffusion. |
| 27 | b | Diffusion spreads plaintext statistics. |
| 28 | a | Confusion obscures the key–ciphertext relationship. |
| 29 | b | 48, to match the subkey width. |
| 30 | b | 6 in, 4 out, eight of them, 48 → 32. |
| 31 | c | Prime. |
| 32 | b | gcd = 1. |
| 33 | c | Group. |
| 34 | b | Abelian. |
| 35 | c | Multiplicative inverses for every nonzero element. |
| 36 | b | XOR. |
| 37 | a | x⁸+x⁴+x³+x+1. Note the x⁴ term and the trailing 1. |
| 38 | b | A prime modulus. Irreducible is the polynomial analogue of prime. |
| 39 | b | GCD. |
| 40 | b | Multiplicative inverses — used to compute d in RSA. |
| 41 | b | 128 bits always, whatever the key size. |
| 42 | b | 12. |
| 43 | b | SPN. |
| 44 | a | 4×4 byte matrix, filled column by column. |
| 45 | c | SubBytes. |
| 46 | c | MixColumns. |
| 47 | d | AddRoundKey. |
| 48 | d | Rows shift by 0, 1, 2, 3 respectively. |
| 49 | b | GF(2⁸) inverse plus affine transformation. |
| 50 | b | 11 — one initial AddRoundKey plus ten rounds. |
| 51 | b | ECB. |
| 52 | a | ECB. |
| 53 | b | The IV. |
| 54 | d | CTR — counters are independent. |
| 55 | c | The previous keystream block, which is why OFB cannot parallelise. |
| 56 | b | The previous ciphertext block. |
| 57 | c | OFB and CTR. |
| 58 | b | E — it only ever generates keystream. |
| 59 | b | Unique with a given key. Unpredictability is the IV's requirement, not the counter's. |
| 60 | b | Three times. |
| 61 | b | The 64-bit block size, which key lengthening cannot fix. |
| 62 | c | CFB. (OFB and CTR also do; CFB is the only one offered here.) |
| 63 | b | Deterministic given a seed. |
| 64 | b | Unpredictability, not merely good statistics. |
| 65 | b | A few outputs reveal a, c and m. |
| 66 | b | Physical entropy. |
| 67 | b | Rivest Cipher 4. |
| 68 | b | 256 bytes. |
| 69 | b | PRGA. KSA does the setup. |
| 70 | b | Keystream biases. |
| 71 | b | XOR. |
| 72 | b | The XOR of two plaintexts — the key cancels. |
| 73 | b | a^(p−1) ≡ 1 (mod p). |
| 74 | c | (p−1)(q−1). |
| 75 | b | 16, since 17 is prime. |
| 76 | b | Any n with gcd(a,n) = 1. |
| 77 | b | Probabilistic. |
| 78 | c | Prime with high probability; composites are never wrongly certified after a failed test. |
| 79 | b | Speed up decryption via mod p and mod q separately. |
| 80 | b | Easy forward, hard backward. |
| 81 | b | Factoring. |
| 82 | b | (e, n). |
| 83 | b | C = P^e mod n. The modulus is n. |
| 84 | c | Only during key generation. |
| 85 | b | gcd(e, φ(n)) = 1. |
| 86 | b | Inverse of e mod φ(n). |
| 87 | b | d follows immediately from e and φ(n). |
| 88 | b | Key exchange, not encryption. |
| 89 | b | No authentication, hence man-in-the-middle. |
| 90 | d | 3072 bits. |
| 91 | b | The point at infinity. |
| 92 | b | A pair (C₁, C₂), so ciphertext is twice the plaintext size. |
| 93 | b | Fixed-length digest from variable-length input. |
| 94 | c | Collision resistance (strong collision resistance). |
| 95 | b | Collision resistance — it halves the effective security in bits. |
| 96 | b | Preimage resistance: hard to invert the digest. |
| 97 | c | Sponge construction (Keccak). SHA-1 and SHA-2 use Merkle-Damgård. |
| 98 | b | A MAC is keyed; a plain hash is not. |
| 99 | b | Nested hashing with the key and the ipad/opad constants. |
| 100 | c | Non-repudiation — the property a MAC cannot provide. |

---

## MARKING AND DIAGNOSIS

| Score | Band |
|---|---|
| 90–100 | A — breadth is there |
| 80–89 | A/B — tidy up the misses |
| 70–79 | B — revisit the two weakest chapters |
| 60–69 | C — recall is patchy across several chapters |
| Below 60 | Re-read before attempting the simulation |

Tally your wrong answers **by chapter**, not by question number. The chapter with the most misses gets your next revision hour. Do not revise chapters you scored full marks on.
