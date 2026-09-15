# DCIT418 MOCK — SET 2
## Reasoning & Application
**Chapters 1–10 | Time limit: 60 minutes | Closed book**

This set is compressed and moderate in number, but each question demands reasoning, not recall. Show full working for every calculation.

---

## SECTION A — APPLIED CALCULATION (50 marks)

**A1.** (5 marks) Encrypt the plaintext **CRYPTO** using a Caesar cipher with shift k = 5. Show the numeric value of each letter, the shifted value, and the resulting ciphertext letter.

**A2.** (6 marks) Encrypt the plaintext **SECURE** using a Vigenère cipher with the key **KEY**. Present your work as a table: plaintext letter, plaintext value, key letter, key value, sum, sum mod 26, ciphertext letter.

**A3.** (4 marks) Encode the plaintext **CRYPTOGRAPHY** using a Rail Fence cipher of depth 3. Draw the zigzag layout, then give the final ciphertext.

**A4.** (5 marks) Compute **gcd(2024, 748)** using the Euclidean algorithm. Show every division step in the form a = qn + r.

**A5.** (4 marks) Find the multiplicative inverse of **7 mod 26**. Show your method and verify your answer.

**A6.** (4 marks) Working in GF(2^4) with irreducible polynomial x^4 + x + 1, compute the **sum** of the elements `1101` and `1011`. Show both the polynomial form and the bitwise result.

**A7.** (6 marks) Working in GF(2^4) with irreducible polynomial x^4 + x + 1, compute the **product** (x^3 + 1) × (x + 1). Show the raw product, then the reduction step if one is required, and give the final answer in both polynomial and binary form.

**A8.** (4 marks) Compute **φ(84)**. Show the prime factorisation you used.

**A9.** (4 marks) Verify Fermat's Little Theorem for p = 11 and a = 3 by computing 3^10 mod 11. Show your intermediate powers — do not simply assert the result.

**A10.** (8 marks) **Full RSA walkthrough.** Given p = 3 and q = 11:
   a) Compute n.
   b) Compute φ(n).
   c) Choose a valid public exponent e, stating why your choice is valid.
   d) Compute the corresponding private exponent d. Show your working.
   e) Encrypt the plaintext P = 4.
   f) State the public key and private key pairs.

---

## SECTION B — REASONING & EXPLANATION (50 marks)

**B1.** (5 marks) An engineer proposes encrypting a large database backup using AES in ECB mode, arguing "AES is a modern, secure cipher, so the mode does not matter." Explain precisely why this reasoning is wrong, and state which mode you would recommend instead and why.

**B2.** (5 marks) A developer reuses the same IV with the same key for every message in CBC mode, arguing "the IV is transmitted in the clear anyway, so it is not secret and reusing it costs nothing." Explain the flaw in this argument and describe concretely what an attacker learns.

**B3.** (5 marks) Explain why an irreducible polynomial must be used as the modulus in GF(2^n), and identify what specifically breaks if a reducible polynomial such as x^4 is used instead. Draw the parallel to the choice of p in GF(p).

**B4.** (5 marks) A student claims: "AES must be a Feistel cipher, because like DES it uses multiple rounds with round keys derived from a master key." Rebut this claim, identifying the specific structural property that distinguishes the two designs.

**B5.** (5 marks) Both OFB and CTR generate a keystream independently of the ciphertext, and neither propagates errors. Explain why, despite this similarity, only CTR can be parallelised.

**B6.** (5 marks) Explain why RSA's decryption formula P = C^d mod n correctly recovers the original plaintext. Your answer must reference the specific theorem involved and the relationship between e, d, and φ(n).

**B7.** (5 marks) In RSA, suppose an attacker learns the value of φ(n) for a given public key (e, n). Explain step by step how this allows them to recover the private key, and state what this implies about why p and q must be kept secret.

**B8.** (5 marks) Alice and Bob complete a Diffie-Hellman exchange and begin communicating with the resulting key, believing it is private. Describe how an attacker could be reading everything despite neither party's private value ever being transmitted. State the specific missing property that permits this.

**B9.** (5 marks) An organisation is deploying cryptography to low-power IoT sensors with limited memory and battery life. They currently plan to use 3072-bit RSA. Recommend an alternative, justify it quantitatively, and state the underlying hard problem your recommendation relies on.

**B10.** (5 marks) A system encrypts messages with a stream cipher whose keystream is produced by a linear congruential generator, arguing "the output passes every statistical randomness test we ran, so it is secure." Explain why passing statistical tests is insufficient, and name the property the generator actually needs.

---

**END OF SET 2**
