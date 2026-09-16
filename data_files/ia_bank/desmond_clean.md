# DCIT418: Desmond's Comprehensive IA Review (Parser Format)

77 IA-style review questions covering the full course range, formatted
for parse_security_bank.py. Explanations were written from scratch since
the source carried none.

### 1. What distinguishes a symmetric cipher from an asymmetric cipher?

- A. It uses multiple keys for encryption
- B. It uses the same key for both encryption and decryption
- C. It relies on prime factorization
- D. It requires a public key infrastructure

**Correct Answer:** **B. It uses the same key for both encryption and decryption**

**Intuition:** A symmetric cipher uses one shared key for both encryption and decryption; an asymmetric cipher uses a mathematically linked key pair, a public key for encryption and a private key for decryption.

---

### 2. How does the Kerberos authentication protocol ensure secure user authentication?

- A. It uses public-key cryptography exclusively
- B. It relies on a trusted key distribution center with symmetric encryption
- C. It avoids timestamps for security
- D. It requires no session keys

**Correct Answer:** **B. It relies on a trusted key distribution center with symmetric encryption**

**Intuition:** Kerberos authenticates users through a trusted Key Distribution Center (KDC) that issues time-limited tickets encrypted with symmetric keys, so neither party ever transmits a password over the network.

---

### 3. How does the security of a linear congruential generator (LCG) as a pseudorandom number generator compare to one based on a block cipher?

- A. LCG is more secure due to its simplicity
- B. LCG is predictable with known outputs; block cipher PRNGs resist prediction
- C. LCG requires no seed; block ciphers do
- D. LCG is faster but less flexible

**Correct Answer:** **B. LCG is predictable with known outputs; block cipher PRNGs resist prediction**

**Intuition:** An LCG's next output is a simple linear function of its previous state, so observing a handful of outputs lets an attacker solve for the generator's parameters and predict the rest of the sequence; a block-cipher-based PRNG's output is only as predictable as the cipher itself, which resists exactly this kind of algebraic recovery.

---

### 4. How does Fermat's Little Theorem ensure the correctness of RSA's encryption and decryption process?

- A. It generates prime numbers for the modulus
- B. It guarantees modular exponentiation returns the original message
- C. It simplifies discrete logarithm computation
- D. It ensures collision resistance in signatures

**Correct Answer:** **B. It guarantees modular exponentiation returns the original message**

**Intuition:** Fermat's Little Theorem underlies the correctness proof that raising a ciphertext to the private exponent recovers the original plaintext modulo a prime; RSA generalizes this to a composite modulus via Euler's Theorem, but the same modular-exponentiation identity is what guarantees decryption undoes encryption.

---

### 5. Evaluate the suitability of RC4 for modern cryptographic applications.

- A. It is ideal due to its speed and simplicity
- B. It is used in AES-based systems
- C. It is vulnerable to biases in keystream, making it outdated
- D. It is resistant to quantum attacks

**Correct Answer:** **C. It is vulnerable to biases in keystream, making it outdated**

**Intuition:** RC4's keystream exhibits statistical biases, most notably in its early output bytes, that let attackers recover plaintext or key material given enough ciphertext, which is why it has been deprecated for use in TLS and WEP.

---

### 6. Why is XTS-AES mode's use of a tweak value critical for disk encryption, and what subtle vulnerability remains?

- A. Tweak ensures key secrecy; vulnerable to brute-force attacks
- B. Tweak ensures unique ciphertext per sector; vulnerable to chosen-plaintext attacks
- C. Tweak simplifies decryption; vulnerable to key recovery
- D. Tweak eliminates padding; vulnerable to padding oracle attacks

**Correct Answer:** **B. Tweak ensures unique ciphertext per sector; vulnerable to chosen-plaintext attacks**

**Intuition:** XTS-AES mixes a per-sector tweak into each block so that identical plaintext blocks in different sectors, or at different offsets, encrypt to different ciphertext, defeating the pattern leakage of a plain block cipher; despite this, XTS still permits some malleability within a sector, since the tweak does not chain block to block the way CBC's IV does.

---

### 7. How does the Encapsulating Security Payload (ESP) in IPsec differ from the Authentication Header (AH)?

- A. ESP provides authentication only, AH provides confidentiality
- B. ESP provides confidentiality and authentication, AH provides authentication only
- C. ESP is less secure than AH
- D. ESP does not support tunnel mode

**Correct Answer:** **B. ESP provides confidentiality and authentication, AH provides authentication only**

**Intuition:** ESP encrypts and optionally authenticates the payload, giving both confidentiality and integrity, while AH only authenticates the packet (including parts of the IP header) and provides no encryption at all.

---

### 8. How does Kerberos' use of tickets enhance security over simple symmetric key distribution?

- A. It eliminates the need for a key distribution center
- B. It provides time-limited, authenticated session keys
- C. It uses asymmetric encryption exclusively
- D. It avoids timestamps

**Correct Answer:** **B. It provides time-limited, authenticated session keys**

**Intuition:** A Kerberos ticket bundles a session key together with a short validity window and cryptographic proof of the KDC's involvement, so a stolen ticket is useless once it expires, unlike a raw shared password that remains valid indefinitely if leaked.

---

### 9. Why is DomainKeys Identified Mail (DKIM) insufficient for end-to-end email security compared to PGP?

- A. DKIM encrypts the email content
- B. DKIM verifies the sender's domain, not the message content or recipient
- C. DKIM requires no signatures
- D. DKIM is more secure than PGP

**Correct Answer:** **B. DKIM verifies the sender's domain, not the message content or recipient**

**Intuition:** DKIM cryptographically verifies that a message's headers were signed by the claimed sending domain, but it says nothing about who actually wrote the content or whether the visible "From" address matches the recipient's expectation, so it cannot fully replace end-to-end content encryption and authentication like PGP.

---

### 10. Synthesize the security implications of SHA-3's sponge construction versus SHA-2's Merkle-Damgård for preimage resistance.

- A. SHA-3 is less resistant; sponge simplifies attacks
- B. SHA-3's capacity enhances preimage resistance; Merkle-Damgård is weaker to extensions
- C. SHA-2 avoids padding; SHA-3 is vulnerable
- D. Both are equally resistant; no differences exist

**Correct Answer:** **B. SHA-3's capacity enhances preimage resistance; Merkle-Damgård is weaker to extensions**

**Intuition:** SHA-3's sponge construction lets a designer tune the ratio between the rate and the capacity, and a hash function's preimage resistance scales with capacity, giving SHA-3 headroom that a fixed Merkle-Damgard chain like SHA-2 lacks; that same fixed chaining is also what makes SHA-2 (without a construction like HMAC) susceptible to length-extension.

---

### 11. Why is RC4's key scheduling algorithm (KSA) a point of vulnerability in its design?

- A. It uses a fixed key size
- B. It produces biased initial keystream bytes, enabling attacks
- C. It avoids pseudorandom number generation
- D. It requires excessive memory

**Correct Answer:** **B. It produces biased initial keystream bytes, enabling attacks**

**Intuition:** RC4's key scheduling algorithm initializes its internal permutation from the key in a way that leaves statistical correlations between the key and the first few keystream bytes, which is the flaw that enabled practical key-recovery and plaintext-recovery attacks such as those exploited against WEP.

---

### 12. Synthesize why a triple transposition cipher might still fail against a chosen-plaintext attack compared to a modern block cipher.

- A. It uses non-linear substitution; resistant to chosen-plaintext attacks
- B. It only reorders plaintext, preserving patterns; block ciphers use confusion and diffusion
- C. It employs modular arithmetic; vulnerable to key recovery
- D. It reduces key space; resistant to cryptanalysis

**Correct Answer:** **B. It only reorders plaintext, preserving patterns; block ciphers use confusion and diffusion**

**Intuition:** A transposition cipher only rearranges plaintext characters, so the same letters (and their frequency distribution) remain in the ciphertext; a chosen-plaintext attacker who controls the input can still recover the permutation, whereas a modern block cipher's rounds of substitution and permutation destroy that structural correspondence entirely.

---

### 13. How does the Schnorr Digital Signature Scheme differ from the NIST Digital Signature Algorithm?

- A. Schnorr uses elliptic curves, NIST does not
- B. Schnorr is more efficient with shorter signatures
- C. Schnorr is less secure than NIST
- D. Schnorr relies on prime factorization

**Correct Answer:** **B. Schnorr is more efficient with shorter signatures**

**Intuition:** Schnorr signatures are built directly around a simple, provably secure sigma protocol and produce a single compact (challenge, response) pair, whereas NIST's DSA requires an extra modular inversion step and, in its classic form, cannot be batch-verified or trivially made non-malleable the way Schnorr's linear structure allows.

---

### 14. Why were rotor machines like the Enigma considered complex for their time?

- A. They used asymmetric encryption
- B. They implemented dynamic polyalphabetic substitution with multiple rotors
- C. They relied on finite field arithmetic
- D. They generated true random numbers

**Correct Answer:** **B. They implemented dynamic polyalphabetic substitution with multiple rotors**

**Intuition:** The Enigma's rotors implemented a polyalphabetic substitution that changed with every keystroke, and combining several rotors (plus a plugboard) multiplied the number of possible wirings into the billions, making the cipher far harder to break by hand than a fixed monoalphabetic or single-rotor substitution.

---

### 15. Why is HMAC's use of an outer hash function critical for preventing key recovery attacks?

- A. It simplifies computation; reduces security
- B. It processes the key with the message, obscuring the inner hash output
- C. It eliminates the inner hash; increases vulnerability
- D. It reduces key size; enhances efficiency

**Correct Answer:** **B. It processes the key with the message, obscuring the inner hash output**

**Intuition:** HMAC's outer hash re-hashes the inner digest together with the secret key, so an attacker who only sees the tag cannot invert the outer layer to recover any information that would let them forge a valid tag for a different message, unlike a naive secret-prefix MAC that is vulnerable to length-extension.

---

### 16. Evaluate the security trade-offs of TLS 1.3's removal of RSA key exchange compared to TLS 1.2.

- A. TLS 1.3 is less secure; RSA is robust
- B. TLS 1.3 enhances forward secrecy by using ephemeral keys; RSA lacks forward secrecy
- C. TLS 1.3 avoids key exchange; TLS 1.2 requires it
- D. TLS 1.3 simplifies encryption; TLS 1.2 is more complex

**Correct Answer:** **B. TLS 1.3 enhances forward secrecy by using ephemeral keys; RSA lacks forward secrecy**

**Intuition:** TLS 1.3 removed static RSA key exchange and mandates ephemeral Diffie-Hellman, so a compromise of the server's long-term private key cannot be used to decrypt previously recorded sessions; RSA key exchange in TLS 1.2 offered no such forward secrecy, since every session key was derived from the same static private key.

---

### 17. Evaluate the Enigma machine's use of multiple rotors versus a single rotor, focusing on its impact on key space and cryptanalysis.

- A. Single rotor increases key space; simplifies cryptanalysis
- B. Multiple rotors exponentially increase key space; complicate pattern detection
- C. Multiple rotors reduce security; simplify decryption
- D. Single rotor ensures randomness; resists frequency analysis

**Correct Answer:** **B. Multiple rotors exponentially increase key space; complicate pattern detection**

**Intuition:** Each additional rotor multiplies the number of possible wirings and scrambling patterns, exponentially expanding the effective key space and making the letter-by-letter substitution pattern change far more often, which frustrates the frequency and pattern analysis that broke simpler single-rotor or non-rotor ciphers.

---

### 18. What is the role of the ShiftRows transformation in AES?

- A. It performs non-linear substitution
- B. It permutes bytes to enhance diffusion
- C. It generates round keys
- D. It compresses the state matrix

**Correct Answer:** **B. It permutes bytes to enhance diffusion**

**Intuition:** ShiftRows cyclically shifts each row of the AES state by a different offset, moving bytes between columns so that MixColumns, which only mixes within a column, ends up mixing data that originated in different columns across rounds, providing diffusion across the whole block.

---

### 19. Why is the use of a nonce in GCM mode critical for security?

- A. It replaces the encryption key
- B. It ensures unique ciphertext, preventing reuse attacks
- C. It simplifies authentication
- D. It eliminates the need for a counter

**Correct Answer:** **B. It ensures unique ciphertext, preventing reuse attacks**

**Intuition:** GCM derives its keystream and authentication tag from a nonce that must never repeat under the same key; reusing a nonce lets an attacker XOR two ciphertexts to cancel the keystream, exposing the plaintext relationship and letting them forge valid authentication tags.

---

### 20. Synthesize the challenges of symmetric key distribution using asymmetric encryption in a post-quantum cryptography context.

- A. Asymmetric encryption is immune to quantum attacks; simplifies distribution
- B. Asymmetric encryption is vulnerable to quantum attacks; requires quantum-resistant algorithms
- C. Symmetric keys are quantum-resistant; asymmetric is unnecessary
- D. Quantum attacks simplify key distribution; no challenges exist

**Correct Answer:** **B. Asymmetric encryption is vulnerable to quantum attacks; requires quantum-resistant algorithms**

**Intuition:** Shor's algorithm on a sufficiently large quantum computer would efficiently factor RSA moduli or solve the discrete-log problem underlying most asymmetric schemes, breaking the hard problems public-key distribution currently relies on, which is why key exchange must migrate to post-quantum, quantum-resistant algorithms.

---

### 21. Synthesize the trade-offs of DES's 16-round Feistel structure versus a hypothetical 32-round structure in terms of security and performance.

- A. 32 rounds reduce security; improve performance
- B. 32 rounds enhance security against cryptanalysis; significantly degrade performance
- C. 16 rounds are insufficient for diffusion; 32 rounds are optimal
- D. Both provide equivalent security; 16 rounds are faster

**Correct Answer:** **B. 32 rounds enhance security against cryptanalysis; significantly degrade performance**

**Intuition:** More Feistel rounds increase resistance to differential and linear cryptanalysis by compounding diffusion and confusion, but each extra round also adds a full pass of computation, so doubling DES's 16 rounds to 32 would meaningfully strengthen it against known attacks at the cost of roughly doubling encryption and decryption time.

---

### 22. Evaluate the impact of RC4's state permutation weaknesses on its use in early SSL/TLS protocols.

- A. State permutations ensure security; SSL/TLS was unaffected
- B. Weak initial permutations led to biased keystreams, enabling attacks like BEAST
- C. State permutations simplified decryption; SSL/TLS was secure
- D. Weak permutations increased key space; SSL/TLS was robust

**Correct Answer:** **B. Weak initial permutations led to biased keystreams, enabling attacks like BEAST**

**Intuition:** Because RC4's key scheduling leaves biases in its earliest keystream bytes, and SSL/TLS re-keyed RC4 for every new record using a related key, those early biased bytes were repeatedly exposed across many sessions, which is exactly the weakness attacks like BEAST exploited to recover plaintext.

---

### 23. Why is the Miller-Rabin algorithm used in primality testing for RSA?

- A. It generates random numbers
- B. It efficiently determines if a number is likely prime
- C. It computes discrete logarithms
- D. It ensures collision resistance

**Correct Answer:** **B. It efficiently determines if a number is likely prime**

**Intuition:** Miller-Rabin is a fast probabilistic test that repeatedly checks a candidate against random witnesses; a composite number fails at least one witness's test with high probability, so a handful of rounds gives extremely high confidence a large candidate for RSA's p and q is actually prime without the cost of a deterministic proof.

---

### 24. How does AES's AddRoundKey transformation ensure security without introducing non linearity?

- A. It permutes the state matrix
- B. It XORs the state with a round key, ensuring key-dependent encryption
- C. It substitutes bytes non-linearly
- D. It compresses the state matrix

**Correct Answer:** **B. It XORs the state with a round key, ensuring key-dependent encryption**

**Intuition:** AddRoundKey is a simple bitwise XOR between the state and the round key, which is linear and introduces no nonlinearity; AES's security instead comes from combining this key-dependent step with the nonlinear SubBytes transformation elsewhere in the round, so together the cipher is both key-dependent and nonlinear.

---

### 25. Why is the security of a block cipher-based PRNG dependent on the cipher's key strength?

- A. Weak keys simplify decryption
- B. The PRNG's output predictability relies on the cipher's resistance to attacks
- C. The key determines the block size
- D. The PRNG avoids key usage

**Correct Answer:** **B. The PRNG's output predictability relies on the cipher's resistance to attacks**

**Intuition:** A block-cipher-based PRNG (as in counter-mode generation) produces its output by encrypting successive counter values, so predicting the next output requires breaking the underlying cipher; if the cipher's key were weak or recoverable, an attacker could reproduce the entire keystream, making the PRNG's unpredictability entirely dependent on the cipher's own strength.

---

### 26. Evaluate why AES's omission of MixColumns in the final round simplifies decryption without compromising security.

- A. It reduces diffusion; weakens security
- B. It allows inverse operations to align symmetrically; maintains diffusion from prior rounds
- C. It eliminates non-linearity; enhances security
- D. It simplifies key expansion; reduces performance

**Correct Answer:** **B. It allows inverse operations to align symmetrically; maintains diffusion from prior rounds**

**Intuition:** Skipping MixColumns in the final round lets AES decryption begin by simply inverting AddRoundKey and then the other transformations in reverse order without needing a MixColumns step whose only purpose would be to mix data that no further round will use, so security is unaffected while the structure stays symmetric between encryption and decryption.

---

### 27. Why is the AES key expansion's use of round constants critical for preventing slide attacks?

- A. Round constants simplify key generation; increase vulnerability
- B. Round constants break key symmetry, preventing repetitive patterns
- C. Round constants reduce key size; simplify cryptanalysis
- D. Round constants eliminate non-linearity; enhance security

**Correct Answer:** **B. Round constants break key symmetry, preventing repetitive patterns**

**Intuition:** Round constants (Rcon) are XORed into the key schedule at specific points so that otherwise-identical or symmetric key material does not produce repeating patterns in the derived round keys, which closes off slide-attack style shortcuts that exploit self-similarity between rounds.

---

### 28. Evaluate the advantage of Kerberos over remote user authentication using asymmetric encryption.

- A. Kerberos is less secure but faster
- B. Kerberos requires no trusted third party
- C. Kerberos uses symmetric encryption for efficiency in trusted environments
- D. Kerberos supports elliptic curve cryptography

**Correct Answer:** **C. Kerberos uses symmetric encryption for efficiency in trusted environments**

**Intuition:** Kerberos relies on fast symmetric encryption and a trusted third party (the KDC) that both sides already share a key with, which is far cheaper computationally than setting up and verifying asymmetric key pairs for every session, making it efficient inside a single trusted realm such as a corporate network.

---

### 29. Why might a transposition cipher be less secure than a substitution cipher when used alone?

- A. It uses a smaller key space
- B. It preserves letter frequency, making it vulnerable to frequency analysis
- C. It requires complex hardware
- D. It cannot be combined with other ciphers

**Correct Answer:** **B. It preserves letter frequency, making it vulnerable to frequency analysis**

**Intuition:** A transposition cipher only reorders the plaintext letters, so the ciphertext still contains the same letter frequencies as the original language; a cryptanalyst can use frequency analysis, or simply anagram short blocks, whereas a substitution cipher used alone has already broken that direct letter-count correspondence within a block.

---

### 30. Why is S/MIME's reliance on X.509 certificates both a strength and a limitation?

- A. It simplifies key management; limits scalability
- B. It ensures trust via CAs; requires complex certificate management
- C. It avoids certificates; reduces security
- D. It eliminates encryption; simplifies implementation

**Correct Answer:** **B. It ensures trust via CAs; requires complex certificate management**

**Intuition:** S/MIME's use of X.509 certificates ties every signature and encryption key to a certificate authority-verified identity, giving strong, centrally-verifiable trust, but that same reliance means users need a working PKI, certificate issuance and revocation infrastructure to participate, which is considerably more overhead than PGP's decentralized web of trust.

---

### 31. Why is the Output Feedback (OFB) mode suitable for error-prone channels?

- A. It self-synchronizes like CFB
- B. It generates a keystream independently of ciphertext
- C. It requires no initialization vector
- D. It is faster than CTR mode

**Correct Answer:** **B. It generates a keystream independently of ciphertext**

**Intuition:** OFB generates its keystream by repeatedly encrypting the previous keystream block rather than the ciphertext, so a bit error in one transmitted ciphertext block only corrupts the corresponding plaintext bits and does not propagate into later blocks, unlike CBC or CFB where an error in one block corrupts the next.

---

### 32. How does IEEE 802.11i's use of the Counter Mode with CBC-MAC Protocol (CCMP) improve security over TKIP?

- A. TKIP uses stronger encryption; CCMP is faster
- B. CCMP uses AES with authenticated encryption; TKIP uses weaker RC4
- C. CCMP avoids key management; TKIP requires it
- D. CCMP is less secure; TKIP supports modern devices

**Correct Answer:** **B. CCMP uses AES with authenticated encryption; TKIP uses weaker RC4**

**Intuition:** CCMP is built around AES in counter mode with CBC-MAC for authenticated encryption, giving both confidentiality and integrity with a strong cipher, whereas TKIP was a stopgap that patched the original WEP design around RC4, inheriting much of RC4's key-scheduling weakness.

---

### 33. How does the AES key expansion process ensure security?

- A. It compresses the key to reduce size
- B. It generates unique round keys from the original key
- C. It encrypts the key with a hash function
- D. It uses a single key for all rounds

**Correct Answer:** **B. It generates unique round keys from the original key**

**Intuition:** AES key expansion derives a distinct round key for every round from the original cipher key using a combination of word rotation, S-box substitution and round constants, so each round applies different key material even though only one key was ever supplied.

---

### 34. Why is the use of a counter in CTR mode critical for its security, and what happens if the counter repeats?

- A. Counter simplifies decryption; repetition has no impact
- B. Counter ensures unique keystreams; repetition causes keystream reuse, enabling XOR attacks
- C. Counter increases key size; repetition enhances security
- D. Counter eliminates IVs; repetition simplifies cryptanalysis

**Correct Answer:** **B. Counter ensures unique keystreams; repetition causes keystream reuse, enabling XOR attacks**

**Intuition:** CTR mode turns a block cipher into a stream cipher by encrypting successive counter values to form the keystream; the counter must never repeat under the same key, because a repeated counter value produces the same keystream block twice, and XORing the two resulting ciphertexts cancels the keystream and exposes the XOR of the two plaintexts.

---

### 35. How does Fermat's Little Theorem support RSA encryption?

- A. It generates random numbers
- B. It ensures modular exponentiation properties for key generation
- C. It computes discrete logarithms
- D. It defines elliptic curves

**Correct Answer:** **B. It ensures modular exponentiation properties for key generation**

**Intuition:** RSA decryption's correctness (that raising a ciphertext to the private exponent recovers the plaintext) is proved using Fermat's Little Theorem for prime moduli, generalized by Euler's Theorem to RSA's composite modulus n = p times q, which is why the primality of p and q during key generation matters so much.

---

### 36. Why is the X.509 certificate revocation list (CRL) critical in PKI?

- A. It generates new certificates
- B. It tracks compromised or expired certificates
- C. It encrypts private keys
- D. It authenticates users directly

**Correct Answer:** **B. It tracks compromised or expired certificates**

**Intuition:** A Certificate Revocation List lets relying parties check whether a certificate was invalidated before its natural expiry, for example after a private key is compromised, which is essential because a certificate's validity period alone cannot account for a key being stolen partway through its lifetime.

---

### 37. Why is Kerberos' ticket-granting ticket (TGT) mechanism vulnerable to key compromise at the Key Distribution Center (KDC)?

- A. TGT uses no encryption; easily intercepted
- B. TGT relies on the KDC's master key; compromise leaks all session keys
- C. TGT avoids timestamps; increases security
- D. TGT simplifies authentication; reduces vulnerability

**Correct Answer:** **B. TGT relies on the KDC's master key; compromise leaks all session keys**

**Intuition:** The Ticket-Granting Ticket is itself encrypted under the KDC's own long-term master key, so if that master key is ever compromised, an attacker can forge or decrypt any TGT (and therefore any session key derived from it) for any user in the realm, making the KDC a single point of catastrophic failure.

---

### 38. Why is the X.509 certificate's hierarchical trust model critical for PKI scalability?

- A. It eliminates the need for revocation lists
- B. It enables trusted certificate authorities to delegate trust efficiently
- C. It simplifies key generation
- D. It avoids public key distribution

**Correct Answer:** **B. It enables trusted certificate authorities to delegate trust efficiently**

**Intuition:** X.509's hierarchical trust model lets a small set of trusted root certificate authorities delegate signing authority to intermediate CAs, so relying parties only need to trust a manageable set of roots while still being able to verify certificates issued by many different organizations down the chain, which is what lets PKI scale to the whole internet.

---

### 39. Why is the AES key schedule designed to prevent related-key attacks?

- A. It uses a linear transformation only
- B. It incorporates non-linear operations to diversify round keys
- C. It reduces the number of rounds
- D. It avoids key expansion

**Correct Answer:** **B. It incorporates non-linear operations to diversify round keys**

**Intuition:** The AES key schedule mixes round constants and a nonlinear S-box substitution into every generated round key, so two related input keys produce round keys that diverge unpredictably rather than differing by the same simple relationship throughout, which is what defeats related-key cryptanalysis.

---

### 40. Why is the Schnorr signature scheme considered efficient for elliptic curve cryptography?

- A. It uses larger keys than ECDSA
- B. It produces shorter signatures with simpler computations
- C. It avoids elliptic curve arithmetic
- D. It requires no hash functions

**Correct Answer:** **B. It produces shorter signatures with simpler computations**

**Intuition:** Schnorr signatures need only a single scalar multiplication and a linear combination to verify, and their structure allows batching and aggregation, so on an elliptic curve group they produce shorter signatures with less computation than schemes like ElGamal or classic DSA that require more modular exponentiations.

---

### 41. Why is the AES SubBytes transformation considered non-linear?

- A. It shifts rows of the state matrix
- B. It uses an S-box to map inputs to outputs in a non-linear way
- C. It performs modular exponentiation
- D. It mixes columns linearly

**Correct Answer:** **B. It uses an S-box to map inputs to outputs in a non-linear way**

**Intuition:** SubBytes replaces each byte of the state with the output of a fixed S-box built from multiplicative inversion in GF(2^8) followed by an affine transformation, and that inversion step is not expressible as a linear function of the input, which is exactly what makes the transformation nonlinear and provides AES's confusion.

---

### 42. How does IEEE 802.11i (WPA2) improve security over WEP for wireless networks?

- A. WEP uses stronger encryption
- B. WPA2 uses AES and robust key management, unlike WEP's weak RC4
- C. WPA2 avoids authentication
- D. WPA2 requires no key exchange

**Correct Answer:** **B. WPA2 uses AES and robust key management, unlike WEP's weak RC4**

**Intuition:** WPA2 (IEEE 802.11i) replaced WEP's weak RC4-based encryption and static keys with AES-CCMP and a proper key-management handshake that derives fresh session keys, closing the keystream-reuse and key-scheduling weaknesses that made WEP trivially breakable.

---

### 43. Evaluate the role of rotor machines like the Enigma in modern cryptography.

- A. They are widely used due to their simplicity
- B. They are secure against quantum attacks
- C. They are obsolete but historically significant for complex substitution
- D. They are used in stream ciphers like RC4

**Correct Answer:** **C. They are obsolete but historically significant for complex substitution**

**Intuition:** Rotor machines like the Enigma are no longer used for real security, since modern computers can brute-force their comparatively small key space in a fraction of a second, but they remain historically significant as the first widely deployed electromechanical implementation of a complex, frequently-changing polyalphabetic substitution.

---

### 44. Evaluate the role of Pretty Good Privacy (PGP) in email security compared to S/MIME.

- A. PGP is less secure but easier to implement
- B. PGP uses a web-of-trust model, S/MIME relies on certificate authorities
- C. PGP avoids encryption entirely
- D. PGP is incompatible with MIME

**Correct Answer:** **B. PGP uses a web-of-trust model, S/MIME relies on certificate authorities**

**Intuition:** PGP establishes trust through a decentralized web of trust where users vouch for each other's keys directly, while S/MIME relies on a hierarchical PKI of certificate authorities to bind identities to keys, so the two differ mainly in who is trusted to vouch for a public key rather than in the cryptography they use.

---

### 45. How does the X.509 certificate's Online Certificate Status Protocol (OCSP) improve upon Certificate Revocation Lists (CRLs)?

- A. OCSP stores all revoked certificates; CRLs are real-time
- B. OCSP provides real-time revocation status; CRLs are periodically updated
- C. OCSP avoids certificates; CRLs require them
- D. OCSP is less secure; CRLs are more efficient

**Correct Answer:** **B. OCSP provides real-time revocation status; CRLs are periodically updated**

**Intuition:** OCSP lets a client query a certificate's status in real time against the issuing authority, whereas a CRL is a list published and refreshed only periodically, so a certificate revoked moments after the last CRL update would still appear valid to a client checking only the CRL, a gap OCSP closes.

---

### 46. How does Federated Identity Management improve user authentication across domains?

- A. It uses symmetric encryption only
- B. It allows single sign-on with trusted identity providers
- C. It eliminates the need for certificates
- D. It requires manual key exchange

**Correct Answer:** **B. It allows single sign-on with trusted identity providers**

**Intuition:** Federated identity management lets a user authenticate once with a trusted identity provider and then access multiple independent services without re-entering credentials at each one, since the relying services accept a signed assertion from the identity provider instead of managing their own password databases.

---

### 47. In GF(2^8), why is the irreducible polynomial x^8 + x^4 + x^3 + x + 1 used in AES?

- A. It simplifies key expansion
- B. It defines the field's arithmetic for byte operations
- C. It reduces the key size
- D. It ensures reversibility of encryption

**Correct Answer:** **B. It defines the field's arithmetic for byte operations**

**Intuition:** AES arithmetic treats each byte as an element of GF(2^8), and multiplication in that field must be reduced modulo an irreducible polynomial so the result always stays within the 256-element field; x^8 + x^4 + x^3 + x + 1 was the specific irreducible polynomial chosen by the Rijndael designers to define that field's multiplication.

---

### 48. How does the Schnorr Digital Signature Scheme's use of linear combinations improve efficiency over Elgamal?

- A. It increases signature size; reduces computation
- B. It reduces signature size and exponentiations via linear combinations
- C. It avoids discrete logarithms; increases key size
- D. It simplifies verification; reduces security

**Correct Answer:** **B. It reduces signature size and exponentiations via linear combinations**

**Intuition:** Schnorr signatures reduce verification to a single linear equation in the exponent, which needs only one multi-exponentiation, whereas ElGamal-style signatures require more separate exponentiations and a modular inverse, so the Schnorr construction's simpler linear combination yields both smaller signatures and faster verification.

---

### 49. Synthesize the benefit of using elliptic curve arithmetic in cryptographic systems.

- A. It simplifies key generation
- B. It provides strong security with smaller key sizes
- C. It eliminates the need for hash functions
- D. It supports symmetric encryption

**Correct Answer:** **B. It provides strong security with smaller key sizes**

**Intuition:** Elliptic curve cryptography's underlying hard problem, the elliptic curve discrete logarithm problem, has no known sub-exponential attack the way integer factorization does for RSA, so ECC reaches equivalent security with far smaller key sizes, for example a 256-bit ECC key roughly matching a 3072-bit RSA key.

---

### 50. Why is the X.509 certificate format critical for public-key infrastructure (PKI)?

- A. It encrypts symmetric keys
- B. It generates pseudorandom numbers
- C. It standardizes public key and identity binding
- D. It authenticates users directly

**Correct Answer:** **C. It standardizes public key and identity binding**

**Intuition:** X.509 defines a standard structure that cryptographically binds a public key to a verified identity (and other attributes) and is signed by a certificate authority, giving every application a common, interoperable format for exchanging and verifying that binding, which is the basic building block PKI is built on.

---

### 51. Evaluate the trade-offs of using ECDSA over RSA-PSS for digital signatures in resource constrained devices.

- A. ECDSA requires larger keys, reducing efficiency
- B. ECDSA uses smaller keys, improving efficiency but requiring curve selection
- C. ECDSA avoids hash functions, simplifying signatures
- D. ECDSA is less secure than RSA-PSS

**Correct Answer:** **B. ECDSA uses smaller keys, improving efficiency but requiring curve selection**

**Intuition:** ECDSA achieves the same security level as RSA-PSS with much smaller keys and faster signing, which matters directly on resource-constrained devices, but it does require the implementer to pick a well-vetted curve, since a poorly chosen curve can introduce subtle weaknesses that RSA's simpler modulus-based structure does not share.

---

### 52. How does the Schnorr signature scheme's use of a random nonce affect its security?

- A. It simplifies verification; reduces security
- B. It ensures signature uniqueness; nonce reuse can leak the private key
- C. It avoids hash functions; eliminates vulnerabilities
- D. It increases signature size; enhances security

**Correct Answer:** **B. It ensures signature uniqueness; nonce reuse can leak the private key**

**Intuition:** Each Schnorr signature must use a fresh random nonce, since the private key can be algebraically derived from just two signatures that reused the same nonce on different messages, exactly as happened in several real-world key-recovery incidents caused by reused or predictable nonces.

---

### 53. Why is HMAC resistant to length extension attacks, unlike a plain hash function?

- A. It uses a smaller hash output
- B. It incorporates a secret key and processes the input twice
- C. It avoids padding the input
- D. It requires no hash function

**Correct Answer:** **B. It incorporates a secret key and processes the input twice**

**Intuition:** HMAC folds the secret key into both an inner and an outer hash computation (nesting the hash rather than simply prepending the key once), so an attacker who observes a valid tag cannot extend the message and compute a new valid tag the way they could against a hash function used with a naive secret-prefix construction.

---

### 54. Why is Triple DES (3DES) slower than AES for equivalent security?

- A. It uses a smaller block size
- B. It requires asymmetric keys
- C. It applies DES three times, increasing computational overhead
- D. It lacks finite field arithmetic

**Correct Answer:** **C. It applies DES three times, increasing computational overhead**

**Intuition:** Triple DES applies the DES algorithm three times in sequence to get an effective key strength beyond a single DES pass, but DES's 64-bit block size and relatively simple Feistel round function were never designed for speed at modern data rates, so three full passes of that structure make 3DES noticeably slower than AES's single, hardware-optimized rounds at comparable security.

---

### 55. Evaluate the security implications of using a weak elliptic curve with a low-order point in ECC.

- A. It increases efficiency; maintains security
- B. It allows attacks like invalid curve attacks, compromising the private key
- C. It simplifies arithmetic; eliminates vulnerabilities
- D. It reduces key size; enhances security

**Correct Answer:** **B. It allows attacks like invalid curve attacks, compromising the private key**

**Intuition:** A point of low order on a poorly chosen or non-validated curve can let an attacker submit a maliciously crafted point that leaks information about the private key through an invalid-curve attack, which is why implementations must validate that received points actually lie on the intended, non-singular curve.

---

### 56. How does SHA-3's capacity parameter affect its security against collision attacks?

- A. Higher capacity reduces output size; decreases security
- B. Higher capacity increases resistance to collision attacks; reduces performance
- C. Capacity has no impact on collisions
- D. Lower capacity enhances security; improves performance

**Correct Answer:** **B. Higher capacity increases resistance to collision attacks; reduces performance**

**Intuition:** SHA-3's sponge construction lets its security level be tuned by the split between the rate (how much data is absorbed per permutation) and the capacity (the hidden internal state); increasing the capacity raises resistance to collision and preimage attacks at the cost of processing less data per permutation call, so there is a direct security-versus-throughput trade-off.

---

### 57. Evaluate the trade-offs of GCM's use of a 96-bit nonce versus a random IV in terms of security and performance.

- A. Random IV is faster; less secure
- B. 96-bit nonce enables efficient counter increments; nonce reuse compromises security
- C. Random IV eliminates nonce reuse; slower performance
- D. 96-bit nonce simplifies authentication; no trade-offs

**Correct Answer:** **B. 96-bit nonce enables efficient counter increments; nonce reuse compromises security**

**Intuition:** A 96-bit nonce in GCM is the recommended size because it lets the internal counter be derived directly and efficiently without an extra hashing step, but exactly like any GCM nonce, reusing it under the same key catastrophically breaks both confidentiality and the authentication tag, so the efficiency gain comes with the same strict never-reuse requirement as any other nonce length.

---

### 58. What is a key requirement for a cryptographic hash function to be secure?

- A. It must be reversible
- B. It must provide preimage resistance
- C. It must use a small output size
- D. It must avoid modular arithmetic

**Correct Answer:** **B. It must provide preimage resistance**

**Intuition:** A secure cryptographic hash function must be preimage resistant (given a hash, it should be infeasible to find any input producing it), alongside second-preimage and collision resistance, since without preimage resistance an attacker could work backward from a stored hash to recover the original input.

---

### 59. How does Cipher Block Chaining (CBC) mode's dependence on an initialization vector (IV) introduce a subtle vulnerability compared to Counter (CTR) mode?

- A. CBC's IV is deterministic; CTR's counter is random
- B. CBC's IV must be unpredictable; reuse enables chosen-ciphertext attacks
- C. CBC avoids IVs; CTR requires them
- D. CBC's IV simplifies decryption; CTR complicates it

**Correct Answer:** **B. CBC's IV must be unpredictable; reuse enables chosen-ciphertext attacks**

**Intuition:** CBC requires an unpredictable IV for every message because a predictable or reused IV lets an attacker test guesses about the plaintext of the first block (enabling chosen-plaintext style attacks), whereas CTR mode only requires its counter to be unique, not unpredictable, making CTR's requirement strictly weaker and easier to satisfy correctly.

---

### 60. How does the Elliptic Curve Digital Signature Algorithm (ECDSA) compare to RSA-PSS in terms of efficiency?

- A. ECDSA is slower but more secure
- B. ECDSA uses smaller keys for equivalent security, improving efficiency
- C. ECDSA requires larger keys
- D. ECDSA is incompatible with hash functions

**Correct Answer:** **B. ECDSA uses smaller keys for equivalent security, improving efficiency**

**Intuition:** ECDSA relies on the elliptic curve discrete logarithm problem, which has no known sub-exponential attack, so it reaches equivalent security to RSA-PSS with much smaller keys, faster signing, and smaller signatures overall.

---

### 61. Synthesize the role of HMAC in ensuring message integrity and authentication.

- A. It encrypts the message content
- B. It combines a hash function with a secret key to verify both
- C. It generates pseudorandom numbers
- D. It replaces digital signatures

**Correct Answer:** **B. It combines a hash function with a secret key to verify both**

**Intuition:** HMAC combines a hash function with a secret key by nesting the key into both an inner and outer hash computation, so verifying a tag proves both that the message was not altered (integrity) and that it was produced by someone holding the shared key (authentication).

---

### 62. Evaluate the impact of quantum computing on the security of RSA versus elliptic curve cryptography.

- A. RSA is resistant to quantum attacks; ECC is vulnerable
- B. RSA is vulnerable to Shor's algorithm; ECC requires larger keys for resistance
- C. Both are equally resistant to quantum attacks
- D. Neither is affected by quantum computing

**Correct Answer:** **B. RSA is vulnerable to Shor's algorithm; ECC requires larger keys for resistance**

**Intuition:** A sufficiently powerful quantum computer running Shor's algorithm would efficiently factor RSA's modulus, breaking it outright, whereas the same algorithm applied to elliptic curve discrete logarithms still runs in polynomial time but against a smaller problem, so ECC's practical response is to move to substantially larger curve sizes rather than being broken as completely as RSA.

---

### 63. In AES, how does the MixColumns transformation contribute to diffusion, and why is it absent in the final round?

- A. It substitutes bytes; included in all rounds
- B. It mixes bytes across columns; omitted in the final round to simplify decryption
- C. It generates round keys; always included
- D. It compresses the state; omitted for speed

**Correct Answer:** **B. It mixes bytes across columns; omitted in the final round to simplify decryption**

**Intuition:** MixColumns treats each column of the AES state as a vector and multiplies it by a fixed matrix over GF(2^8), mixing the four bytes within a column so that a single changed input byte affects multiple output bytes; it is omitted from the final round purely because any further mixing at that point would need to be undone by an extra step during decryption for no additional security benefit.

---

### 64. In modular arithmetic, what is the significance of the modulus in GF(p)?

- A. It defines the block size
- B. It specifies the prime number for the finite field
- C. It determines the key length
- D. It sets the polynomial degree

**Correct Answer:** **B. It specifies the prime number for the finite field**

**Intuition:** In GF(p), the modulus p (required to be prime) defines the size of the field and guarantees that every nonzero element has a multiplicative inverse, which is the property that makes GF(p) a field rather than merely a ring, and is essential for the modular arithmetic RSA, Diffie-Hellman and related schemes depend on.

---

### 65. Why is the DES S-box design resistant to differential cryptanalysis, and what subtle flaw still exists?

- A. It uses linear mappings; vulnerable to linear cryptanalysis
- B. It employs non-linear mappings with specific difference distribution tables; vulnerable to linear cryptanalysis
- C. It avoids substitution; susceptible to brute-force attacks
- D. It uses fixed permutations; vulnerable to key recovery

**Correct Answer:** **B. It employs non-linear mappings with specific difference distribution tables; vulnerable to linear cryptanalysis**

**Intuition:** The DES S-boxes were specifically designed with difference distribution tables that suppress high-probability differential characteristics, giving strong resistance to differential cryptanalysis; the same design goals were not applied against linear cryptanalysis, which was only formalized years later, leaving DES comparatively more exposed to that specific attack.

---

### 66. Why is collision resistance a critical requirement for cryptographic hash functions?

- A. It ensures reversible hashing
- B. It prevents two different inputs from producing the same hash
- C. It reduces computational complexity
- D. It eliminates the need for keys

**Correct Answer:** **B. It prevents two different inputs from producing the same hash**

**Intuition:** Collision resistance means it should be infeasible to find any two distinct inputs that hash to the same output; without it, an attacker could substitute a malicious document for a legitimate one that shares the same hash, defeating any scheme (such as digital signatures) that relies on the hash to uniquely represent the original data.

---

### 67. How does the use of modular exponentiation in RSA differ from its use in Diffie-Hellman?

- A. RSA uses it for key exchange, Diffie-Hellman for encryption
- B. RSA uses it for encryption/decryption, Diffie-Hellman for key agreement
- C. RSA avoids modular exponentiation
- D. Diffie-Hellman requires smaller exponents

**Correct Answer:** **B. RSA uses it for encryption/decryption, Diffie-Hellman for key agreement**

**Intuition:** RSA uses modular exponentiation as the encryption and decryption operation itself, transforming a message directly into ciphertext and back; Diffie-Hellman instead uses modular exponentiation only to let two parties each compute the same shared secret from their private exponents, which is then used to derive keys for a separate encryption step.

---

### 68. What distinguishes IEEE 802.1X from the Extensible Authentication Protocol (EAP)?

- A. 802.1X is a cryptographic algorithm, EAP is a framework
- B. 802.1X is a port-based access control, EAP is an authentication framework
- C. 802.1X is less secure than EAP
- D. 802.1X does not support wireless networks

**Correct Answer:** **B. 802.1X is a port-based access control, EAP is an authentication framework**

**Intuition:** IEEE 802.1X is a port-based network access control standard that decides whether a device is allowed onto the network at all, while EAP is a general authentication framework that 802.1X uses to carry the actual credential exchange, so 802.1X is the gatekeeper and EAP is the protocol it speaks to the gatekeeper.

---

### 69. How does a rail fence cipher differ from a columnar transposition cipher?

- A. Rail fence uses substitution, columnar uses permutation
- B. Rail fence arranges letters in a zigzag pattern, columnar uses a grid
- C. Rail fence is more secure than columnar
- D. Rail fence requires a numerical key

**Correct Answer:** **B. Rail fence arranges letters in a zigzag pattern, columnar uses a grid**

**Intuition:** A rail fence cipher writes the plaintext diagonally across a fixed number of rows in a zigzag and reads it off row by row, while a columnar transposition cipher writes the plaintext into a rectangular grid and reads the columns off in an order defined by a keyword, so both are transpositions but use different geometric patterns to reorder the letters.

---

### 70. Evaluate the role of IPsec's Internet Key Exchange (IKE) in establishing secure VPNs.

- A. It encrypts data directly
- B. It negotiates security associations and keys for secure communication
- C. It replaces ESP and AH
- D. It simplifies packet processing

**Correct Answer:** **B. It negotiates security associations and keys for secure communication**

**Intuition:** IKE is the protocol IPsec uses to authenticate the two endpoints and negotiate the shared keys and security parameters (the security associations) that ESP and AH will later use to actually protect traffic, so IKE handles setup while ESP and AH handle the ongoing data protection.

---

### 71. In AES, why is the absence of MixColumns in the final round critical for decryption efficiency?

- A. It simplifies encryption; increases decryption complexity
- B. It allows the inverse operation to start with AddRoundKey, simplifying decryption
- C. It reduces security; simplifies key expansion
- D. It eliminates diffusion; speeds up encryption

**Correct Answer:** **B. It allows the inverse operation to start with AddRoundKey, simplifying decryption**

**Intuition:** Because MixColumns is skipped in AES's final round, decryption can start by inverting AddRoundKey and then directly undo the other transformations without needing an extra InvMixColumns step at that boundary, keeping the decryption process a clean mirror of encryption without wasted computation.

---

### 72. Evaluate the security implications of using CCM versus GCM for authenticated encryption in constrained environments.

- A. CCM is faster; less secure than GCM
- B. CCM is simpler but less efficient due to sequential processing; GCM supports parallelism
- C. CCM avoids authentication; GCM requires it
- D. CCM uses larger keys; GCM is more secure

**Correct Answer:** **B. CCM is simpler but less efficient due to sequential processing; GCM supports parallelism**

**Intuition:** CCM processes the plaintext twice, once for encryption and once for the CBC-MAC authentication pass, so its two-pass, sequential design cannot be parallelized; GCM instead computes its authentication tag using a fast, parallelizable multiplication in GF(2^128) alongside CTR-mode encryption, giving it a real throughput advantage in constrained or high-speed environments.

---

### 73. In modular arithmetic, why is the use of a prime modulus in GF(p) essential for cryptographic operations, and what happens with a composite modulus?

- A. Composite modulus increases security; ensures inverses
- B. Prime modulus ensures unique inverses; composite modulus allows factorization, breaking security
- C. Prime modulus reduces key space; composite modulus is secure
- D. Composite modulus simplifies arithmetic; enhances security

**Correct Answer:** **B. Prime modulus ensures unique inverses; composite modulus allows factorization, breaking security**

**Intuition:** A prime modulus in GF(p) guarantees every nonzero element has a unique multiplicative inverse, which is what makes GF(p) a field; with a composite modulus, some elements share common factors with the modulus and have no inverse, and knowing the modulus's factorization (as in RSA's n) is exactly what lets an attacker break the cryptosystem.

---

### 74. In elliptic curve cryptography, why is the choice of a non-singular curve critical, and what subtle attack exploits a singular curve?

- A. Singular curves increase efficiency; no attacks exist
- B. Non-singular curves ensure group structure; singular curves enable point factorization attacks
- C. Singular curves enhance security; resist cryptanalysis
- D. Non-singular curves simplify arithmetic; vulnerable to key recovery

**Correct Answer:** **B. Non-singular curves ensure group structure; singular curves enable point factorization attacks**

**Intuition:** A non-singular elliptic curve has a well-defined group structure where every point addition behaves consistently, which the security proofs for ECC rely on; a singular curve loses that structure at certain points, and an attacker can exploit those singular points to reduce or entirely break the discrete logarithm problem through what is known as a point factorization or singular-curve attack.

---

### 75. How does the structure of a finite field in GF(2^8) support AES operations?

- A. It simplifies key expansion
- B. It enables efficient polynomial arithmetic for S-boxes
- C. It reduces key size
- D. It avoids modular arithmetic

**Correct Answer:** **B. It enables efficient polynomial arithmetic for S-boxes**

**Intuition:** AES bytes are treated as elements of the finite field GF(2^8), whose well-defined addition (XOR) and multiplication (polynomial multiplication modulo an irreducible polynomial) give SubBytes' S-box construction and MixColumns' matrix multiplication a consistent, invertible algebraic structure to operate over.

---

### 76. How does Kerberos' replay cache prevent unauthorized access in authentication?

- A. It encrypts session keys
- B. It detects and blocks reused authentication tickets
- C. It generates random timestamps
- D. It eliminates the need for a KDC

**Correct Answer:** **B. It detects and blocks reused authentication tickets**

**Intuition:** Kerberos tickets and authenticators are timestamped and cached briefly by the server that receives them, so a captured ticket that an attacker tries to reuse (a replay attack) is detected and rejected because it either falls outside the valid time window or matches an authenticator the server has already seen.

---

### 77. Synthesize the security benefits of GCM over CCM for authenticated encryption.

- A. GCM is slower but more secure
- B. GCM supports parallel processing and better performance with equivalent security
- C. GCM avoids authentication tags
- D. GCM requires no counter mechanism

**Correct Answer:** **B. GCM supports parallel processing and better performance with equivalent security**

**Intuition:** GCM computes its authentication tag using fast, parallelizable finite-field multiplication alongside CTR-mode encryption, so both encryption and authentication can be pipelined across multiple cores or hardware lanes, giving it better throughput than CCM's sequential two-pass design for the same underlying security guarantees.

---
