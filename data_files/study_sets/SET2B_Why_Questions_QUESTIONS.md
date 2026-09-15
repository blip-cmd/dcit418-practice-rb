# DCIT418 MOCK — SET 2B
## The "Why" Paper: Design Rationale & Justification
**Chapters 1–10 | Time limit: 60 minutes | Closed book**

Every question here asks **why** something is done the way it is. Naming the fact earns nothing; the marks are in the justification. If your answer could be written by someone who had memorised a glossary but never understood the design, it is not a full answer.

Answer all questions. 5 marks each, 100 marks total.

---

## PART 1 — FOUNDATIONS AND CLASSICAL CIPHERS

**1.** Why is the secret key in the symmetric cipher model specified as being *independent* of both the plaintext and the algorithm? What would be lost if the algorithm itself were the secret instead?

**2.** Why does a monoalphabetic substitution cipher remain breakable despite having a keyspace of 26! (roughly 4 × 10²⁶) possible keys, when a modern 56-bit DES key gives only about 7 × 10¹⁶ possibilities and is considered too small?

**3.** Why does the Vigenère cipher resist frequency analysis in a way the Caesar cipher cannot? Identify the specific structural change responsible.

**4.** Why must a one-time pad key be used only once? Describe concretely what an attacker gains if the same key encrypts two different messages.

**5.** Why is the Rail Fence cipher classified separately from the substitution ciphers, and why does that classification matter for how it is attacked?

---

## PART 2 — BLOCK CIPHERS, DES AND AES

**6.** Why is the Feistel structure designed so that only half the block is transformed per round, when transforming the whole block would seem to give more mixing per round? What specific practical benefit does the design buy?

**7.** Why are the S-boxes described as the component that gives DES its security, when the expansion and permutation stages also scramble the bits?

**8.** Why does DES include an initial permutation and a final permutation if they contribute nothing cryptographically?

**9.** Why is the avalanche effect a *desirable* property rather than an incidental one? What attack becomes easier if a cipher lacks it?

**10.** Why did increasing DES's key length via Triple DES prove to be only an interim solution rather than a permanent fix?

**11.** Why does AES abandon the Feistel structure that DES used? What does it gain, and what does it give up?

**12.** Why is MixColumns omitted from the final AES round, and why is this omission safe rather than a weakening of the cipher?

**13.** Why does AES need a key expansion step at all, rather than simply XORing the same master key into every round?

**14.** Why is AddRoundKey the only transformation in AES that uses the secret key, given that the other three are entirely public and fixed?

---

## PART 3 — FINITE FIELDS

**15.** Why does cryptography require a *field* specifically, rather than a ring being sufficient? Name the operation that becomes possible and where it is actually needed.

**16.** Why must p be prime for GF(p) to be a field? Demonstrate with a concrete counterexample using a composite modulus.

**17.** Why must the modulus polynomial in GF(2ⁿ) be irreducible rather than merely of the correct degree?

**18.** Why does AES perform its arithmetic in GF(2⁸) rather than simply doing ordinary integer arithmetic mod 256?

---

## PART 4 — MODES OF OPERATION AND STREAM CIPHERS

**19.** Why does ECB mode leak plaintext structure when the underlying block cipher may be perfectly strong? Locate the fault precisely.

**20.** Why does CBC mode need an IV at all, when chaining alone already makes each block depend on the one before it?

**21.** Why must the IV be unpredictable in CBC but the counter in CTR need only be unique? Explain what each requirement is actually defending against.

**22.** Why does CFB decryption use the encryption function E rather than the decryption function D? Your answer must identify what E is actually being applied to.

**23.** Why can CTR be parallelised when OFB cannot, given that both generate a keystream independently of the ciphertext?

**24.** Why is the ability to decrypt blocks out of order a practically significant advantage, and why can CBC not offer it?

**25.** Why is a linear congruential generator acceptable for a simulation but unacceptable for a stream cipher keystream, even when its output passes standard statistical randomness tests?

**26.** Why is a stream cipher's reuse of a keystream catastrophic in a way that a block cipher's reuse of a key is not?

---

## PART 5 — NUMBER THEORY AND PUBLIC-KEY CRYPTOGRAPHY

**27.** Why is Euler's Theorem, rather than Fermat's Little Theorem, the result that RSA correctness actually depends on?

**28.** Why must p and q in RSA be kept secret after key generation, when only their product n is published and n is public anyway?

**29.** Why is e required to be coprime to φ(n)? What specifically fails at the next step if this condition is violated?

**30.** Why is the modulus in RSA encryption n rather than φ(n), given that φ(n) is what governs the relationship between e and d?

**31.** Why are probabilistic primality tests such as Miller-Rabin used in RSA key generation instead of deterministic trial division, and why is the resulting uncertainty acceptable?

**32.** Why is the Chinese Remainder Theorem used in RSA implementations, and why does it not weaken security despite being a shortcut?

**33.** Why does Diffie-Hellman succeed in establishing a shared secret without ever transmitting it? Identify the algebraic property that makes this possible.

**34.** Why is Diffie-Hellman vulnerable to a man-in-the-middle attack despite the discrete logarithm problem remaining unbroken throughout the attack?

**35.** Why is public-key cryptography not simply used for everything, given that it solves the key distribution problem that symmetric cryptography suffers from?

**36.** Why does ECC achieve equivalent security to RSA at a fraction of the key size? Point to the difference in the underlying hard problem.

---

## PART 6 — SYNTHESIS

**37.** Why is "the algorithm is strong" an insufficient basis for claiming a system is secure? Draw on at least three distinct examples from across this course.

**38.** Why does almost every construction in this course — Feistel decryption, CFB, OFB, CTR, stream ciphers, the one-time pad — rely on XOR rather than some other combining operation?

**39.** Why do both RSA and Diffie-Hellman depend on one-way functions, and why is "hard to reverse" not the same as "impossible to reverse"?

**40.** Why does the choice of block cipher mode matter more in practice than the choice between AES-128 and AES-256?

---

**END OF SET 2B**
