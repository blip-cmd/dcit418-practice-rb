# DCIT418 — SET 8
## Tools and Labs (Light)
**Based on the course outline's practical component | Suggested time: 20 minutes**

The exam is theory, so this is insurance, not a priority. Its value is that a lecturer who spent most of the semester in a lab tends to phrase theory questions in lab vocabulary — "which OpenSSL mode would you use" rather than "which block cipher mode". Twenty minutes here, no more.

---

# PART 1 — TOOL TO PURPOSE

Match each tool to what it is used for. Cover the right column first.

| Tool | Used for |
|---|---|
| **Wireshark** | Packet capture and traffic analysis. Inspecting protocols on the wire, identifying attacks, observing plaintext versus encrypted traffic. Ties to Chapter 1: it is how traffic analysis is actually performed. |
| **Nmap** | Network scanning and host or port discovery. Reconnaissance, which is the practical face of passive information gathering. |
| **Kali Linux** | A distribution preloaded with security and penetration testing tools. |
| **Ubuntu Linux** | General-purpose platform for running the toolchain. |
| **OpenSSL** | Command-line cryptography: encrypting and decrypting files, generating keys, inspecting certificates, choosing ciphers and modes. |
| **PyCryptodome / cryptography** | Python libraries implementing AES, DES, RSA, hashes and modes for programmatic use. |
| **SageMath** | Mathematics environment for modular arithmetic, finite fields, primality and number theory experiments. Ties to Chapters 4 and 8. |
| **OpenStego** | Steganography: embedding a payload inside a cover file. Ties to Chapter 2. |
| **VS Code** | Development environment. |

---

# PART 2 — THE HANDFUL OF FACTS WORTH KNOWING

**Wireshark.** Captures and decodes packets on an interface. Relevant observations: HTTP traffic is readable in plaintext while HTTPS is not; a capture shows source, destination, timing and packet size even when content is encrypted, which is precisely what traffic analysis exploits and why encryption alone does not defeat it.

**OpenSSL.** The cipher is named as `algorithm-keysize-mode`, for example `aes-256-cbc` or `aes-128-ctr`. You should recognise that shape and be able to read a mode out of it. Key generation for RSA and inspection of certificates are also done here.

**Python libraries.** PyCryptodome and `cryptography` provide the primitives; you choose the cipher, the mode, and supply the IV or nonce. The exam-relevant point is that the library does not choose the mode for you, and choosing ECB is where students go wrong.

**SageMath.** Used for the mathematics of Chapters 4 and 8: GCDs, modular inverses, totients, primality tests, finite field arithmetic. Nothing to memorise beyond what it is for.

**OpenStego.** Hides a file inside a cover image. Reinforces the Chapter 2 distinction: steganography conceals that a message exists; cryptography conceals what it says. The two are complementary, not alternatives.

**Nmap.** Discovers live hosts and open ports. Sits at the reconnaissance stage that precedes an attack, which is why it appears alongside the attack taxonomy in Chapter 1.

---

# PART 3 — QUICK CHECK

**1.** Which tool would you use to demonstrate that traffic analysis remains possible against encrypted traffic, and what would you point to in the capture?

**2.** In the OpenSSL cipher string `aes-256-cbc`, identify each of the three parts.

**3.** Why is a laboratory demonstration of ECB versus CBC usually done on an image file rather than a text file?

**4.** Which tool belongs to Chapter 2, and what distinction does it illustrate?

**5.** Which tool supports the Chapter 4 and 8 material, and name two operations you would perform with it.

**6.** A lab asks you to encrypt a file with AES and you must supply an IV. Which modes require one, and which mode instead requires a counter or nonce?

---

# ANSWERS

**1.** Wireshark. Even with the payload encrypted, the capture still exposes source and destination addresses, packet sizes, timing and frequency — enough to infer who is communicating with whom, how often, and how much, which is the definition of traffic analysis from Chapter 1.

**2.** `aes` is the algorithm, `256` is the key size in bits, `cbc` is the mode of operation.

**3.** Because ECB's weakness is the leakage of *structure*, and an image makes that visible to the eye: regions of uniform colour produce repeated identical ciphertext blocks, so the outline of the original picture survives encryption. The same leakage occurs with text but is not visually obvious, so the point lands less clearly.

**4.** OpenStego. It illustrates that steganography conceals the *existence* of a message while cryptography conceals its *content* — and that the two can be layered, since an encrypted payload can itself be hidden in a cover file.

**5.** SageMath. Any two of: computing GCDs via the Euclidean algorithm, finding multiplicative inverses, evaluating Euler's totient, running primality tests, performing GF(2ⁿ) polynomial arithmetic.

**6.** CBC, CFB and OFB require an IV. CTR requires a counter, usually built from a nonce plus an incrementing value. ECB requires neither, which is exactly why it is deterministic and unsafe.

---

That is the whole of it. If you have spare time, it belongs in Sets 4, 5 and 7, not here.
