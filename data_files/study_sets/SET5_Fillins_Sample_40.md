# DCIT 418: SET 5, Sample 40

Closed book, roughly 15-20 minutes, exact terminology required. If you genuinely don't know one, write "?" rather than guessing invisibly, then check it against the reveal below and log the miss.

A curated 40-question sample pulled from the fuller SET5 fill-in bank, since the exam is now rumored to carry only 10 fill-ins. Working this set end to end should surface exactly which chapters are still shaky before the real thing.

---

### 1. The three components of the CIA triad are ______, ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** Confidentiality; Integrity; Availability

*Intuition:* Confidentiality keeps information from unauthorized readers, integrity keeps it from unauthorized modification, and availability keeps it accessible to authorized users when they need it. Every other security service Stallings lists is usually explained as supporting one of these three.
</details>

---

### 2. The four categories of active attack are ______, ______, ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** Masquerade; Replay; Modification of messages; Denial of service

*Intuition:* All four alter system state or data, which is what makes them "active" rather than "passive." Masquerade means pretending to be someone else, replay resends captured legitimate data, modification alters a message in transit, and denial of service degrades or blocks availability.
</details>

---

### 3. Passive attacks are countered primarily by ______, while active attacks are countered by ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** prevention; detection; recovery

*Intuition:* A passive attack (eavesdropping, traffic analysis) leaves no trace to detect, so the only real defense is preventing it in the first place, mainly through encryption. An active attack does alter something, so it can in principle be detected, and the practical goal shifts to detecting it and recovering from the damage, since preventing every possible active attack outright is unrealistic.
</details>

---

### 4. A cipher in which a plaintext letter may map to several different ciphertext letters is called ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** a polyalphabetic (substitution) cipher

*Intuition:* A monoalphabetic cipher uses one fixed substitution for the whole message, so letter frequencies survive intact. A polyalphabetic cipher (the Vigenere cipher is the classic example) cycles through multiple substitution alphabets, so the same plaintext letter can map to different ciphertext letters depending on position, which is exactly what flattens the frequency profile and resists simple frequency analysis.
</details>

---

### 5. The cipher offering perfect secrecy is the ______, also known as the ______ cipher.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** One-Time Pad; Vernam

*Intuition:* The One-Time Pad XORs plaintext with a truly random key at least as long as the message, used only once. Because the key is uniformly random and never reused, the ciphertext gives an attacker zero statistical information about the plaintext, which is the definition of perfect (information-theoretic) secrecy. It's impractical precisely because distributing a key as long as the message is its own hard problem.
</details>

---

### 6. Concealing the very existence of a message is called ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** steganography

*Intuition:* Cryptography scrambles a message so its content is unreadable but its presence is obvious; steganography hides the message inside an innocuous carrier (an image, audio file, or similar) so an observer doesn't even know communication is happening. The two are complementary, not competing, techniques.
</details>

---

### 7. DES has a block size of ______ bits, a stored key of ______ bits and an effective key of ______ bits.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** 64; 64; 56

*Intuition:* DES operates on 64-bit blocks. The key is stored as 64 bits, but 8 of those bits are parity bits (one per byte) that carry no security-relevant information, leaving an effective key length of 56 bits, which is also why DES's 2^56 keyspace became brute-forceable and drove the move to Triple DES and then AES.
</details>

---

### 8. DES uses ______ S-boxes, each taking ______ bits and producing ______ bits.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** 8; 6; 4

*Intuition:* The 48-bit expanded half-block from the E-table is split into eight 6-bit chunks, one per S-box, and each S-box compresses its 6 input bits down to a 4-bit output, recombining into a 32-bit result. That 6-to-4 compression, chosen via a fixed lookup table rather than a formula, is what supplies DES's nonlinearity.
</details>

---

### 9. The only nonlinear component of the DES round function is the ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** S-boxes (substitution boxes)

*Intuition:* The expansion permutation, the P-box permutation, and the XOR with the round key are all linear operations, so if DES only used those, the whole cipher would collapse into a linear function solvable directly. The S-boxes are the sole non-linear step, and that nonlinearity is exactly what makes differential and linear cryptanalysis hard rather than trivial.
</details>

---

### 10. Obscuring the relationship between the key and ciphertext is ______; spreading plaintext statistics across the ciphertext is ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** confusion; diffusion

*Intuition:* Shannon's two design principles: confusion makes the ciphertext's dependence on the key as complex and non-obvious as possible (substitution supplies this), while diffusion spreads the influence of each plaintext bit across many ciphertext bits so statistical structure gets washed out (permutation/mixing supplies this). AES gets confusion from SubBytes and diffusion from ShiftRows plus MixColumns.
</details>

---

### 11. The algorithm used to compute the GCD of two integers is the ______ algorithm; the variant used to compute multiplicative inverses is the ______ algorithm.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** Euclidean; Extended Euclidean

*Intuition:* The Euclidean algorithm repeatedly replaces the larger of two numbers with the remainder of dividing it by the smaller, converging on their gcd. The Extended Euclidean algorithm runs the same recursion but also tracks the Bezout coefficients x and y satisfying ax + by = gcd(a,b), and when gcd(a,n)=1 that x is exactly a's multiplicative inverse mod n, which is how RSA computes d from e.
</details>

---

### 12. A multiplicative inverse of a mod n exists only when ______ = 1.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** gcd(a, n)

*Intuition:* An inverse a⁻¹ satisfying a * a⁻¹ ≡ 1 (mod n) exists exactly when a and n share no common factor other than 1, i.e. they're coprime. If gcd(a,n) = d > 1, then a can only ever reach multiples of d modulo n, never 1, so no inverse exists.
</details>

---

### 13. A structure in which every nonzero element has a multiplicative inverse is a ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** field

*Intuition:* A ring only guarantees an additive group plus associative, distributive multiplication, nothing about multiplicative inverses. A field adds exactly that guarantee, every nonzero element is invertible, which is what makes division well-defined and is why GF(p) and GF(2^n) (fields, not just rings) are what cryptographic arithmetic is built on.
</details>

---

### 14. The modulus polynomial in GF(2ⁿ) must be ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** irreducible

*Intuition:* An irreducible polynomial cannot be factored into lower-degree polynomials over GF(2), which is the polynomial analogue of a prime number. Just as GF(p) needs p prime for every nonzero residue to have an inverse, GF(2^n) needs the modulus polynomial irreducible, otherwise some nonzero elements would share a factor with the modulus and lose their inverse, breaking the field structure.
</details>

---

### 15. AES supports key sizes of ______, ______ and ______ bits, with corresponding round counts ______, ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** 128, 192, 256; 10, 12, 14

*Intuition:* All three AES variants operate on the same fixed 128-bit block regardless of key size, but longer keys buy more rounds of mixing to keep the security margin comfortable against cryptanalysis as the key grows: 128-bit keys get 10 rounds, 192-bit get 12, 256-bit get 14.
</details>

---

### 16. AES is structurally a ______ network, not a Feistel cipher.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** substitution-permutation (SPN)

*Intuition:* A Feistel cipher only transforms half the block each round while the other half passes through unchanged. AES instead transforms the entire 128-bit state every round through substitution (SubBytes) and permutation/mixing (ShiftRows, MixColumns) layers, which is the defining shape of a substitution-permutation network.
</details>

---

### 17. The four AES round transformations in order are ______, ______, ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** SubBytes; ShiftRows; MixColumns; AddRoundKey

*Intuition:* SubBytes supplies nonlinear confusion via the S-box, ShiftRows shifts each row of the state to diffuse bytes across columns, MixColumns mixes the four bytes within each column via matrix multiplication in GF(2^8) for diffusion within a column, and AddRoundKey XORs in the round's key material, the only step that actually depends on the secret key.
</details>

---

### 18. The AES transformation omitted from the final round is ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** MixColumns

*Intuition:* MixColumns' diffusion is only useful if further rounds follow to compound it; at the final round there's nothing left to compound into, and including it would just force decryption to add an extra InvMixColumns step for no security benefit, so it's dropped to keep the encryption/decryption structure symmetric.
</details>

---

### 19. The only AES transformation using the secret key is ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** AddRoundKey

*Intuition:* SubBytes, ShiftRows and MixColumns are all fixed, key-independent operations; AddRoundKey is the single step where the round's derived key material is XORed into the state, which is why it's the only step that couldn't be precomputed without knowing the key.
</details>

---

### 20. AES-128 requires ______ round keys in total.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** 11

*Intuition:* AES-128 runs 10 rounds, but there's also an initial AddRoundKey applied before round 1 even starts, so the key schedule must produce Nr + 1 = 11 separate 128-bit round keys (44 words of 32 bits each) to cover the initial whitening step plus all 10 rounds.
</details>

---

### 21. The five block-cipher modes are ______, ______, ______, ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** ECB; CBC; CFB; OFB; CTR

*Intuition:* Electronic Codebook encrypts each block independently (and leaks plaintext structure); Cipher Block Chaining XORs each plaintext block with the previous ciphertext before encrypting; Cipher Feedback and Output Feedback turn the block cipher into a self-synchronizing or synchronous stream cipher respectively; Counter mode encrypts successive counter values to form a keystream, enabling parallel encryption and decryption.
</details>

---

### 22. In OFB, the keystream is generated by repeatedly encrypting the previous ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** keystream output (the previous encryption output, not the ciphertext)

*Intuition:* OFB feeds the block cipher's own output back in as the next input, generating a keystream that is completely independent of the ciphertext or plaintext. That's what gives OFB its "no error propagation" property, and also why the keystream can be precomputed before the plaintext is even available.
</details>

---

### 23. In CFB, the keystream is generated by encrypting the previous ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** ciphertext block

*Intuition:* CFB feeds the previous ciphertext block back through the block cipher to produce the next keystream segment. Because the feedback is the ciphertext rather than the raw output, CFB is self-synchronizing, an error in one ciphertext block corrupts a bounded run of subsequent plaintext but then resynchronizes, unlike OFB's fully independent keystream.
</details>

---

### 24. The two modes with no error propagation are ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** OFB; CTR

*Intuition:* In both modes, the keystream is generated independently of the ciphertext (from repeated encryption in OFB, from encrypting a counter in CTR), and recovery is a simple XOR. A flipped ciphertext bit therefore flips exactly the corresponding plaintext bit and nothing else, no full-block corruption and no bleed into neighboring blocks, unlike ECB, CBC or CFB, where decryption runs the corrupted ciphertext through the block cipher itself and scrambles the whole affected block.
</details>

---

### 25. A CBC IV must be ______, whereas a CTR counter must be ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** unpredictable; unique

*Intuition:* CBC's IV is XORed with the first plaintext block before encryption, so a predictable IV lets an attacker test guesses about that first block's content (a chosen-plaintext style weakness). CTR's counter doesn't need to be secret or random at all, it just must never repeat under the same key, since a repeated (key, counter) pair produces the same keystream block twice and lets an attacker XOR two ciphertexts to cancel it out. Uniqueness is a strictly weaker, easier requirement than unpredictability.
</details>

---

### 26. A generator producing random-looking output deterministically from a seed is a ______; one whose output is computationally unpredictable is a ______; one drawing on physical entropy is a ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** PRNG; CSPRNG; TRNG

*Intuition:* A plain PRNG only needs to pass statistical randomness tests, it can still be predictable to an attacker who knows the algorithm and observes enough output (a linear congruential generator is the classic broken example). A CSPRNG adds the cryptographic requirement that predicting past or future output is computationally infeasible even given a chunk of the sequence. A TRNG skips algorithms entirely and samples genuine physical entropy (thermal noise, timing jitter) for its randomness.
</details>

---

### 27. RC4's two phases are ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** KSA (Key Scheduling Algorithm); PRGA (Pseudo-Random Generation Algorithm)

*Intuition:* The KSA initializes a 256-byte state array and shuffles it into a key-dependent permutation using the secret key. The PRGA then continuously swaps entries in that state using two index pointers and emits one keystream byte per step, which is XORed with the plaintext. RC4's known biases live mostly in the KSA's handling of the earliest PRGA output bytes.
</details>

---

### 28. Reusing a stream-cipher keystream allows an attacker to recover the ______ of two plaintexts.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** XOR

*Intuition:* If C1 = P1 XOR K and C2 = P2 XOR K use the same keystream K, then C1 XOR C2 = P1 XOR P2, the keystream cancels out entirely. That XOR of the two plaintexts is often enough, combined with language statistics or crib-dragging, to recover both plaintexts without ever knowing K, which is exactly why reusing a one-time pad or stream-cipher keystream destroys its security.
</details>

---

### 29. Fermat's Little Theorem states that, for prime p and a not divisible by p, ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** a^(p-1) ≡ 1 (mod p)

*Intuition:* This holds because the nonzero residues mod a prime p form a group of order p-1 under multiplication, and by Lagrange's theorem every element's order divides the group's order, so raising any such element to the p-1 power always cycles back to the identity, 1.
</details>

---

### 30. Euler's Theorem states that if gcd(a,n)=1, then ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** a^φ(n) ≡ 1 (mod n)

*Intuition:* Euler's Theorem generalizes Fermat's Little Theorem from a prime modulus to any modulus n, replacing the group order p-1 with φ(n), the count of integers coprime to n. Fermat's is just the special case where n is prime, since φ(p) = p-1. This is the identity RSA's correctness proof leans on, since n = pq is composite.
</details>

---

### 31. The probabilistic primality test used in RSA key generation is ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** Miller-Rabin

*Intuition:* Miller-Rabin repeatedly tests a candidate against random witnesses; a composite number fails at least one witness's test with probability at least 3/4, so running enough independent rounds drives the chance of a false "probably prime" verdict down to negligible levels, fast enough to be practical for generating the very large primes p and q that RSA needs.
</details>

---

### 32. Given α, q and αˣ mod q, recovering x is the ______ problem.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** discrete logarithm

*Intuition:* Computing α^x mod q from x is fast (repeated squaring), but the reverse direction, recovering x given only α, q and the result, has no known efficient classical algorithm for well-chosen groups. That asymmetry, easy forward, hard backward, is exactly what Diffie-Hellman and ElGamal build their security on.
</details>

---

### 33. The RSA public key is ______ and the private key is ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** (e, n); (d, n)

*Intuition:* Both keys share the same modulus n = pq; what differs is the exponent, e for encryption/verification (chosen to be coprime to φ(n)) and d for decryption/signing (e's modular inverse mod φ(n)). n itself can be public since factoring it back into p and q is assumed to be infeasible for large enough primes.
</details>

---

### 34. The private RSA exponent d is the ______ of e modulo ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** multiplicative inverse; φ(n)

*Intuition:* Key generation picks e coprime to φ(n) and then solves e*d ≡ 1 (mod φ(n)) for d via the Extended Euclidean algorithm. That inverse relationship is exactly what makes decryption undo encryption: raising a ciphertext to d after it was raised to e composes back to the original message modulo n, by Euler's Theorem.
</details>

---

### 35. Diffie-Hellman achieves ______ rather than encryption.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** key exchange (agreement on a shared secret)

*Intuition:* Diffie-Hellman never encrypts or transmits a message directly; it lets two parties who exchange only public values each independently compute the same shared secret, which is then typically used to derive a symmetric key for a separate encryption step. It's a key-agreement protocol, not a cipher in its own right.
</details>

---

### 36. Diffie-Hellman's principal weakness is the absence of ______, permitting a ______ attack.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** authentication; man-in-the-middle

*Intuition:* Plain Diffie-Hellman never binds a public value to a verified identity, so an attacker can intercept the exchange, run a separate DH exchange with each party, and relay/re-encrypt traffic between them, with neither party any the wiser. The discrete logarithm problem is never actually solved, the protocol is simply bypassed because nothing authenticates who sent which public value.
</details>

---

### 37. The identity element of the elliptic-curve group is the ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** point at infinity

*Intuition:* Elliptic-curve point addition is defined geometrically (draw a line through two points, find the third intersection, reflect it), and to make every point have an inverse and the operation form a proper group, a special "point at infinity" is added as the identity element, the result of adding a point to its own vertical reflection.
</details>

---

### 38. The hard problem underlying ECC is the ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** elliptic curve discrete logarithm problem (ECDLP)

*Intuition:* Given a base point P and Q = kP (P added to itself k times), recovering k is believed computationally infeasible for well-chosen curves, and unlike integer factorization there's no known sub-exponential attack against it, which is why ECC reaches RSA-equivalent security with much smaller key sizes.
</details>

---

### 39. A cryptographic hash requires three security properties: ______, ______ and ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** preimage resistance; second preimage resistance; collision resistance

*Intuition:* Preimage resistance means you can't work backward from a hash to find any input producing it; second preimage resistance means, given one input, you can't find a different input with the same hash; collision resistance means you can't find any two inputs at all that collide. Collision resistance is the strongest of the three and implies second preimage resistance, but all three get stated separately because different applications lean on different ones.
</details>

---

### 40. SHA-3 uses the ______ construction, whereas SHA-1/SHA-2 use the ______ construction. A keyed hash providing message authentication is a ______; the standard nested construction is ______; and the security property a digital signature provides that a MAC cannot is ______.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** sponge; Merkle-Damgard; MAC; HMAC; non-repudiation

*Intuition:* SHA-3's sponge construction absorbs input into a large internal state and then squeezes out output, with security tunable via the rate/capacity split. SHA-1 and SHA-2 instead chain a compression function block by block (Merkle-Damgard), which is also what makes naive use of them vulnerable to length-extension. A MAC adds a shared secret key to a hash to prove both integrity and authenticity; HMAC is the standard way to nest that key into the hash safely (inner and outer hash passes) to resist length-extension. A digital signature adds non-repudiation on top, since only the signer holds the private key, whereas a MAC's shared key means either party could have produced the tag.
</details>

---
