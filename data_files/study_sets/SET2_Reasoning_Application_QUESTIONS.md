# DCIT418 MOCK — SET 2
## Reasoning & Application
**Chapters 1–13 | Time limit: 60 minutes | Closed book**

The exam carries no calculation questions, so Section A has been cut back to the few simple worked examples worth keeping — not because you will be asked to compute them, but because working them by hand is what makes the concepts explainable in words. The weight now sits in Section B.

Chapters 11–13 material is marked. Skip it until those blocks have been taught.

---

## SECTION A — SIMPLE WORKED EXAMPLES (30 marks)

Keep these short. If one takes more than four minutes you are overworking it.

**A1.** (4 marks) Encrypt **CRYPTO** using a Caesar cipher with shift 5. Give the letter values and the result.

**A2.** (5 marks) Encrypt **SECURE** using a Vigenère cipher with key **KEY**. Present plaintext value, key value, sum, sum mod 26, ciphertext letter.

**A3.** (3 marks) Encode **CRYPTOGRAPHY** with a Rail Fence cipher of depth 3. Show the zigzag, then the ciphertext.

**A4.** (4 marks) Compute **gcd(2024, 748)** using the Euclidean algorithm. Show each step as a = qn + r.

**A5.** (3 marks) Find the multiplicative inverse of **7 mod 26**, and verify it.

**A6.** (3 marks) In GF(2⁴), add `1101` and `1011`. Give the polynomial form and the binary result, and state what bitwise operation this is equivalent to.

**A7.** (3 marks) Compute **φ(15)** and **φ(17)**, stating the rule used for each.

**A8.** (5 marks) Given p = 3 and q = 11, compute n and φ(n), choose a valid e with justification, and find the corresponding d.

---

## SECTION B — REASONING & EXPLANATION (70 marks)

Each question presents a flawed claim, a design decision, or a scenario. Marks are for the reasoning, not for naming the concept.

### Chapters 1–3

**B1.** (5 marks) An engineer proposes encrypting a large database backup using AES in ECB mode, arguing that AES is a modern, secure cipher so the mode does not matter. Explain precisely why this reasoning fails, and recommend a mode with justification.

**B2.** (5 marks) A student argues that a monoalphabetic substitution cipher must be secure because its keyspace of 26! vastly exceeds DES's 2⁵⁶. Rebut this, and state the general principle it violates.

**B3.** (5 marks) Explain why the Feistel design transforms only half the block per round, when transforming the whole block would mix faster. State the specific practical benefit the choice buys.

### Chapters 4–5

**B4.** (5 marks) Explain why the modulus polynomial in GF(2ⁿ) must be irreducible, what breaks if a reducible one such as x⁴ is used, and the parallel with the choice of p in GF(p).

**B5.** (5 marks) A student claims AES must be a Feistel cipher because, like DES, it uses multiple rounds with subkeys derived from a master key. Rebut this, naming the structural property that actually distinguishes the two designs.

**B6.** (5 marks) Explain why AES performs its arithmetic in GF(2⁸) rather than simply using integer arithmetic modulo 256.

### Chapters 6–7

**B7.** (5 marks) A developer reuses the same IV with the same key for every CBC message, arguing that the IV travels in the clear anyway so it is not secret and reuse costs nothing. Explain the flaw and describe concretely what an attacker learns.

**B8.** (5 marks) Both OFB and CTR generate a keystream independently of the ciphertext and neither propagates errors. Explain why only CTR can be parallelised.

**B9.** (5 marks) A system uses a stream cipher whose keystream comes from a linear congruential generator, on the grounds that its output passes every statistical randomness test. Explain why that is insufficient and name the property actually required.

### Chapters 8–10

**B10.** (5 marks) Explain why RSA decryption recovers the plaintext. Name the theorem involved and state why Fermat's Little Theorem is not the one that applies.

**B11.** (5 marks) An attacker learns φ(n) for a published RSA public key (e, n). Explain step by step what they can now do, and what this implies about the secrecy of p and q.

**B12.** (5 marks) Alice and Bob complete a Diffie-Hellman exchange and begin communicating, believing the key is private. Explain how an attacker could be reading everything despite no private value being transmitted and the discrete logarithm problem remaining unsolved.

**B13.** (5 marks) An organisation deploying cryptography to low-power IoT sensors plans to use 3072-bit RSA. Recommend an alternative, justify it quantitatively, and name the underlying hard problem.

### Chapters 11–13

**B14.** (5 marks) A developer sends a file along with its SHA-256 digest over an insecure channel, arguing that the recipient can recompute the digest and so detect any tampering. Explain why this fails against a deliberate attacker and what construction fixes it.

**B15.** (5 marks) A team stores user passwords as unsalted SHA-256 digests, arguing that hashes are one-way so the passwords are safe. Explain what an attacker with the stolen file can still do, and which hash property is and is not doing the work here.

**B16.** (5 marks) Two parties share a MAC key and use MAC tags on every message. One later denies having sent a particular message. Explain why the MAC cannot settle the dispute and what would have been needed instead.

---

**END OF SET 2**
