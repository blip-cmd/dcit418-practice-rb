# DCIT 418: Systems and Network Security
## Quiz 5: Comprehensive Question Bank & Review (Bayat's Take - 70 Questions)
**Department of Computer Science, University of Ghana**  
**Course Code:** DCIT 418 | **Credits:** 3 Credits  
**Quiz:** Quiz 5 | **Topic:** Network Security Protocols (EAP, SSH, IPsec, SSL/TLS, WEP, WPA2/802.11i), Cryptographic Hash Functions & MACs (SHA-1/2/3, HMAC, CMAC, Collision Resistance), Public Key Infrastructures (PKI, X.509, Web of Trust, PGP), and Authentication Services (Kerberos, PIV)

---

### 📝 Study Checklist & Progress Tracker
- [ ] **I have done the MCQs** *(Last attempted: )*
- [ ] **I have done the essay / short answer questions** *(Last attempted: )*

---

> [!NOTE]
> This document contains the complete master question bank and detailed solutions for **DCIT 418: Quiz 5 (Bayat's Take - 70 Questions)**.
> - A complete **Answer Summary Table** is provided at the top for quick reference.
> - A **Question Frequency & Repetition Analysis Table** tracks occurrence counts across source takes.
> - Each question features an interactive **"Reveal Answer"** drop-down containing the correct option and detailed engineering/conceptual intuition.

## Complete Answer Summary Table

| Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer | Q | Answer |
|---|--------|---|--------|---|--------|---|--------|---|--------|---|--------|
| **1** | D | **13** | C | **25** | B | **37** | B | **49** | B | **61** | C |
| **2** | D | **14** | D | **26** | C | **38** | C | **50** | D | **62** | D |
| **3** | C | **15** | Auth | **27** | A | **39** | 802.1X | **51** | B | **63** | A |
| **4** | C | **16** | A | **28** | A | **40** | A | **52** | A | **64** | C |
| **5** | B | **17** | A | **29** | B | **41** | D | **53** | A | **65** | B |
| **6** | A | **18** | B | **30** | D | **42** | D | **54** | C | **66** | C |
| **7** | C | **19** | PGP | **31** | A | **43** | C | **55** | A | **67** | C |
| **8** | C | **20** | IPsec | **32** | Sponge | **44** | B | **56** | D | **68** | B |
| **9** | D | **21** | A | **33** | D | **45** | C | **57** | C | **69** | A |
| **10** | A | **22** | D | **34** | B | **46** | A | **58** | B | **70** | D |
| **11** | D | **23** | B | **35** | B | **47** | B | **59** | D | | |
| **12** | D | **24** | C | **36** | B | **48** | D | **60** | B | | |

---

## 📊 Question Frequency & Repetition Analysis Table

| Q# | Question Topic / Core Concept | Answer | Repetition Count | Test Occurrences / Source Takes |
|:---|:------------------------------|:------:|:----------------:|:--------------------------------|
| **1-70** | Full Master Set (Symmetric and Asymmetric Security) | Various | **1x** | Bayat's Take (Q1-Q70) |

---

## Exam Questions & Detailed Solutions

### 1. The Extensible Authentication Protocol (EAP) is designed to:
- A. Replace TLS entirely
- B. Provide a single fixed authentication method
- C. Only work with wireless networks
- D. Support multiple authentication methods within a common framework

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Support multiple authentication methods within a common framework**

*Intuition:* The **Extensible Authentication Protocol (EAP)** (RFC 3748) is an authentication framework rather than a specific authentication mechanism. It provides a generalized structure that allows network access hardware (such as 802.1X switches, wireless access points, or VPN gateways) to negotiate diverse authentication methods (e.g., EAP-TLS, EAP-PEAP, EAP-TTLS, EAP-MSCHAPv2) between clients and backend AAA servers (like RADIUS).
</details>

---

### 2. The SSH Transport Layer Protocol provides:
- A. Certificate revocation services
- B. User authentication only
- C. Application-layer routing
- D. Server authentication, confidentiality, and integrity for the underlying connection

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Server authentication, confidentiality, and integrity for the underlying connection**

*Intuition:* The **SSH Transport Layer Protocol** (RFC 4253) operates directly over TCP to establish a secure cryptographic channel. It guarantees server authentication (verifying server public host keys), data confidentiality (symmetric stream/block encryption), and data integrity (using Message Authentication Codes like HMAC). User authentication is handled by the higher-layer SSH User Authentication Protocol (RFC 4252).
</details>

---

### 3. IPsec operates primarily at which layer of the protocol stack?
- A. The session layer
- B. The data link layer only
- C. The IP (network) layer
- D. The application layer

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The IP (network) layer**

*Intuition:* **IPsec (Internet Protocol Security)** operates at Layer 3 (Network Layer) of the OSI model. By encrypting and authenticating packets directly at the IP layer (using Authentication Header [AH] and Encapsulating Security Payload [ESP]), IPsec transparently secures all higher-layer application traffic (TCP, UDP, ICMP) without requiring application-level modifications.
</details>

---

### 4. A cryptographic hash function takes an input of arbitrary length and produces:
- A. An encrypted ciphertext of equal length
- B. A variable-length output
- C. A fixed-length output (message digest)
- D. A digital certificate

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A fixed-length output (message digest)**

*Intuition:* A **cryptographic hash function** (e.g., SHA-256, SHA-3) deterministically processes arbitrary-length binary inputs to output a fixed-size byte string known as a message digest or hash fingerprint. The output size is strictly governed by the algorithm choice (e.g., 256 bits for SHA-256) regardless of input size.
</details>

---

### 5. Symmetric key distribution using a Key Distribution Center (KDC) relies on:
- A. Public-key certificates exclusively
- B. A trusted server that shares a master key with each user and issues session keys
- C. Each pair of users pre-sharing a key directly with every other user
- D. No shared secrets of any kind

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A trusted server that shares a master key with each user and issues session keys**

*Intuition:* A **Key Distribution Center (KDC)** acts as a trusted centralized authority that shares a secret master key with each registered principal. When two entities wish to establish a secure connection, the KDC dynamically generates a temporary session key and distributes it encrypted under each party's respective master key, eliminating the $O(N^2)$ key-management bottleneck of direct pre-shared key pairs.
</details>

---

### 6. SHA-1 produces a message digest of:
- A. 160 bits
- B. 128 bits
- C. 256 bits
- D. 512 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 160 bits**

*Intuition:* **SHA-1 (Secure Hash Algorithm 1)** produces a 160-bit (20-byte) hash output, commonly rendered as a 40-digit hexadecimal string. For comparison, MD5 outputs 128 bits, SHA-256 outputs 256 bits, and SHA-512 outputs 512 bits.
</details>

---

### 7. A key motivation for Kerberos is to allow a user to authenticate once and then access multiple services without:
- A. Ever having tickets expire
- B. Using any shared secret
- C. Re-entering a password for every individual service
- D. Encrypting any traffic

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Re-entering a password for every individual service**

*Intuition:* The primary design goal of **Kerberos** is Single Sign-On (SSO). Once a user authenticates to the Kerberos Authentication Server (AS) to obtain a Ticket-Granting Ticket (TGT), they present that TGT to the Ticket-Granting Server (TGS) to acquire service-specific tickets automatically without re-prompting the user for their password.
</details>

---

### 8. A major security weakness of simple password-based remote authentication over an insecure network is that:
- A. Passwords are too long to remember
- B. Passwords cannot be hashed
- C. Passwords may be intercepted (eavesdropped) if sent without protection
- D. Passwords never expire

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Passwords may be intercepted (eavesdropped) if sent without protection**

*Intuition:* Transmitting passwords in cleartext or without transport encryption (e.g., via HTTP, Telnet, or FTP) exposes credentials to passive network eavesdropping, packet sniffing, and man-in-the-middle (MitM) attacks. Secure authentication frameworks mandate challenge-response schemes, zero-knowledge proofs, or TLS encryption to protect passwords on the wire.
</details>

---

### 9. GCM (Galois/Counter Mode) achieves message authentication using:
- A. The Playfair matrix
- B. RSA signatures
- C. An HMAC construction
- D. A universal hash function based on multiplication in GF(2^128)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A universal hash function based on multiplication in GF(2^128)**

*Intuition:* **Galois/Counter Mode (GCM)** is an authenticated encryption mode (AEAD) combining Counter (CTR) mode encryption with a Galois message authentication mechanism. Message integrity is verified using GHASH, a universal hash function that performs multiplication over the binary Galois Field $GF(2^{128})$, allowing high-throughput, parallelizable hardware acceleration.
</details>

---

### 10. DKIM allows a receiving mail server to verify that an email was not altered in transit and originated from the claimed domain.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **DomainKeys Identified Mail (DKIM)** adds a cryptographic digital signature to the headers of outgoing emails. The receiving mail transfer agent (MTA) queries the sender's public key via DNS to verify the signature, proving both message origin (authenticity) and that headers/body were not modified in transit (integrity).
</details>

---

### 11. The birthday attack exploits which phenomenon to find hash collisions faster than a naive brute-force search?
- A. Fermat's Little Theorem
- B. The Chinese Remainder Theorem
- C. The pigeonhole principle alone
- D. The birthday paradox, where collisions become likely with far fewer than 2^n attempts

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The birthday paradox, where collisions become likely with far fewer than 2^n attempts**

*Intuition:* The **birthday attack** exploits the probability statistics of the birthday paradox: in a set of randomly chosen inputs, the probability of a hash collision (finding any $x_1 \neq x_2$ such that $H(x_1) = H(x_2)$) exceeds $50\%$ after approximately $2^{n/2}$ evaluations, rather than the full $2^n$ attempts required by a naive preimage search.
</details>

---

### 12. If a digital signature private key is compromised, the most direct consequence is that an attacker can:
- A. Break the underlying hash function
- B. Recover other users' private keys
- C. Decrypt all previously encrypted traffic
- D. Forge signatures that appear to originate from the legitimate signer

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Forge signatures that appear to originate from the legitimate signer**

*Intuition:* In asymmetric signature schemes, the private key is a secret credential used exclusively to generate cryptographic signatures. If compromised, an adversary can sign any arbitrary file or transaction, successfully impersonating the owner. It does not break the hash algorithm, expose independent third-party keys, or decrypt unrelated traffic.
</details>

---

### 13. Which of these is NOT typically listed among the standard applications of cryptographic hash functions?
- A. Digital signatures
- B. Password storage
- C. Providing confidentiality by encrypting data
- D. Message authentication

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Providing confidentiality by encrypting data**

*Intuition:* Hash functions are deterministic, one-way mathematical functions with no decryption key. Because they cannot be reversed, they do not provide confidentiality (which is the domain of symmetric/asymmetric encryption). They are strictly used for integrity (digital signatures, password verification, and MACs).
</details>

---

### 14. The Digital Signature Algorithm (DSA), as standardized by NIST, is based on the difficulty of:
- A. Finding hash collisions
- B. Elliptic curve point addition only
- C. Factoring large integers
- D. Computing discrete logarithms

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Computing discrete logarithms**

*Intuition:* The standard **Digital Signature Algorithm (DSA)** relies on the computational hardness of the discrete logarithm problem over a multiplicative group of integers modulo a large prime. While RSA is based on integer factorization, DSA is based on discrete logarithms.
</details>

---

### 15. HMAC stands for Hash-based Message ____ Code. (Fill in the blank)
*Answer:* **Authentication**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Authentication**

*Intuition:* **HMAC** stands for **Hash-based Message Authentication Code**. It is a symmetric cryptographic construction that uses a cryptographic hash function in combination with a secret key to authenticate both the origin and integrity of data.
</details>

---

### 16. RSA-PSS was introduced as a signature scheme mainly to address:
- A. Weaknesses in basic textbook RSA signatures by adding randomized padding
- B. Weaknesses specific to SHA-1 alone
- C. The need for a shared secret key
- D. The speed of elliptic curve arithmetic

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Weaknesses in basic textbook RSA signatures by adding randomized padding**

*Intuition:* Textbook RSA signatures are deterministic ($s = m^d \pmod n$), making them vulnerable to mathematical manipulation and existential forgery. **RSA-PSS (Probabilistic Signature Scheme)** integrates a randomized salt and structured padding, providing provable security in the random oracle model.
</details>

---

### 17. A digital signature can be verified by anyone who has access to the signer's public key.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Asymmetric cryptography designates signing as a private-key operation, while verification is public. Because the signer's public key is distributed openly, any third party can verify the digital signature's authenticity without needing access to the signer's secret private key.
</details>

---

### 18. Authenticated encryption modes such as GCM and CCM are valued because they provide:
- A. Authentication only, with no confidentiality
- B. Both confidentiality and message authentication in a single operation
- C. Confidentiality only
- D. Key exchange services only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Both confidentiality and message authentication in a single operation**

*Intuition:* Authenticated encryption (AEAD) modes like GCM and CCM combine encryption (confidentiality) and MAC calculation (integrity/authenticity) in a single integrated pass. This avoids the security vulnerabilities of implementing separate Encrypt-then-MAC or MAC-then-Encrypt schemes.
</details>

---

### 19. In email security, ____ uses a decentralized web-of-trust model for key management instead of a formal CA hierarchy. (Fill in the blank)
*Answer:* **PGP (or OpenPGP)**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **PGP (or OpenPGP)**

*Intuition:* **Pretty Good Privacy (PGP)** implements a decentralized **Web of Trust** model. Users sign one another's public keys to vouch for identity bindings directly, bypassing the need for a centralized, hierarchical Certificate Authority (CA) PKI.
</details>

---

### 20. The protocol suite that secures IP traffic at the network layer, including the AH and ESP protocols, is called ____. (Fill in the blank)
*Answer:* **IPsec**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **IPsec**

*Intuition:* **IPsec (Internet Protocol Security)** is the Layer 3 protocol suite that secures IP traffic. It utilizes two main protocols: **Authentication Header (AH)** for connectionless integrity/authentication, and **Encapsulating Security Payload (ESP)** for confidentiality and authentication.
</details>

---

### 21. The Internet Key Exchange (IKE) protocol is used within IPsec to:
- A. Negotiate and establish security associations and session keys
- B. Encrypt application data directly
- C. Provide email encryption
- D. Route IP packets

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Negotiate and establish security associations and session keys**

*Intuition:* **IKE** serves as the control-plane protocol for IPsec. It executes a Diffie-Hellman exchange to establish cryptographic keys and negotiates the Security Associations (SAs) containing encryption/integrity parameters, which the data-plane protocols (ESP/AH) subsequently use to secure traffic.
</details>

---

### 22. In cloud computing terminology, "IaaS" refers to:
- A. Internet as a Service
- B. Identity as a Service
- C. Integration as a Service
- D. Infrastructure as a Service

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Infrastructure as a Service**

*Intuition:* **IaaS** stands for **Infrastructure as a Service**. It is a cloud service delivery model that provides virtualized computing infrastructure (VMs, storage, network interfaces) over the internet, giving users raw resource provisioning without physical hardware overhead.
</details>

---

### 23. Non-repudiation is a property provided by MACs but generally not by digital signatures.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* This statement is inverted. **Digital signatures** provide non-repudiation because they use asymmetric cryptography: only the signer possesses the private key. **MACs** use symmetric cryptography (a shared key); since both the sender and receiver hold the same key, either could have generated the MAC, meaning the sender can plausibly deny message creation to a third party.
</details>

---

### 24. A Security Association (SA) in IPsec defines:
- A. A physical network cable
- B. A wireless channel
- C. A one-way relationship specifying the security services and parameters applied to traffic
- D. A DNS zone

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A one-way relationship specifying the security services and parameters applied to traffic**

*Intuition:* An **SA** is a logical, simplex (one-way) connection between two IPsec endpoints. It acts as a database record containing the cryptographic algorithms, keys, initialization vectors, lifetimes, and Security Parameter Index (SPI) used to process incoming or outgoing packets.
</details>

---

### 25. Kerberos tickets typically include a timestamp and lifetime primarily to protect against:
- A. Man-in-the-middle certificate forgery only
- B. Replay attacks
- C. Frequency analysis
- D. Brute-force key search

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Replay attacks**

*Intuition:* In Kerberos, authentication tickets are intercepted on insecure networks. If a ticket lacked a expiration timeframe, an attacker could capture and re-transmit (replay) it indefinitely. Timestamps and short ticket lifetimes (typically 8–10 hours) restrict the validity window to prevent replay attempts.
</details>

---

### 26. ECDSA differs from standard DSA mainly in that it:
- A. Uses RSA instead of discrete logarithms
- B. Does not require a hash function
- C. Operates over elliptic curve groups instead of modular integer groups
- D. Uses only symmetric keys

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Operates over elliptic curve groups instead of modular integer groups**

*Intuition:* **ECDSA** (Elliptic Curve Digital Signature Algorithm) is mathematically equivalent to the standard DSA, but it executes over finite-field elliptic curve groups rather than modular integers ($Z_p^*$). This enables equal cryptographic strength at dramatically smaller key sizes (e.g., 256-bit ECC vs 3072-bit RSA/DSA).
</details>

---

### 27. The TLS Handshake Protocol allows the client and server to negotiate a cipher suite before exchanging application data.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The **TLS Handshake Protocol** negotiates session parameters (protocol version, bulk encryption algorithms, key exchange methods, and MAC/PRF hash functions) via the ClientHello and ServerHello exchanges prior to transmitting encrypted application-layer data.
</details>

---

### 28. In wireless network security, the four-way handshake in 802.11i is used to:
- A. Derive and confirm fresh session keys between a client and access point
- B. Distribute the original network SSID
- C. Encrypt the SSID broadcast
- D. Replace the need for a password entirely

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Derive and confirm fresh session keys between a client and access point**

*Intuition:* In **802.11i (WPA2/WPA3)**, the four-way handshake uses the pre-established Pairwise Master Key (PMK) to dynamically derive a unique, ephemeral Pairwise Transient Key (PTK). This session-specific key encrypts unicast data traffic and validates that both sides possess the correct PMK without transmitting the key material directly.
</details>

---

### 29. Pretty Good Privacy (PGP) provides email security services including:
- A. Only message compression
- B. Confidentiality and authentication using a combination of public-key and symmetric cryptography
- C. Only spam filtering
- D. Only DNS-based validation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Confidentiality and authentication using a combination of public-key and symmetric cryptography**

*Intuition:* **PGP** is a hybrid cryptosystem. It provides confidentiality by encrypting email contents with an ephemeral symmetric key (e.g., AES), which is then encrypted with the recipient's public key. It provides authentication and integrity by signing a hash of the message with the sender's private key.
</details>

---

### 30. IPsec's tunnel mode, compared to transport mode, differs in that it:
- A. Does not support the ESP protocol
- B. Cannot be used to build VPNs
- C. Only protects the payload, leaving the original IP header exposed
- D. Encapsulates and protects the entire original IP packet inside a new IP packet

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Encapsulates and protects the entire original IP packet inside a new IP packet**

*Intuition:* In **tunnel mode**, the entire original IP packet (header and payload) is encrypted and authenticated, then encapsulated inside a completely new outer IP packet. In contrast, **transport mode** only encrypts the payload, leaving the original IP header visible. Tunnel mode is the standard implementation for Site-to-Site and Remote Access VPNs.
</details>

---

### 31. Downgrade attacks against SSL/TLS attempt to:
- A. Force the use of weaker, older cryptographic protocol versions
- B. Replace TCP with UDP
- C. Increase the overall encryption strength
- D. Bypass the need for certificates entirely

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Force the use of weaker, older cryptographic protocol versions**

*Intuition:* A **downgrade attack** is a Man-in-the-Middle (MitM) technique where the attacker intercepts the initial handshake and tricks the client/server into negotiating obsolete protocol versions (e.g., SSL 3.0) or weaker cipher suites (e.g., export-grade ciphers) to subsequently exploit known cryptographic vulnerabilities (such as POODLE).
</details>

---

### 32. The ____ construction underlies SHA-3 (Keccak), absorbing input blocks and squeezing out the digest. (Fill in the blank)
*Answer:* **sponge**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **sponge**

*Intuition:* SHA-3 (Keccak) uses a **sponge construction**. It works by "absorbing" input blocks into its internal state through a series of permutations, and then "squeezing" output blocks from that state to produce a hash digest of the desired length.
</details>

---

### 33. PGP uses which approach for key management, rather than relying on a formal hierarchical PKI?
- A. Kerberos tickets exclusively
- B. No key management at all
- C. A strict CA hierarchy only
- D. A decentralized "web of trust" model

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A decentralized "web of trust" model**

*Intuition:* Instead of using hierarchical Certificate Authorities (as in S/MIME or SSL/TLS), **PGP** relies on a decentralized **Web of Trust**. Individual users validate and sign each other's keys, building a distributed, peer-to-peer web of endorsements.
</details>

---

### 34. The Schnorr digital signature scheme is notable for:
- A. Requiring no hash function at all
- B. Its efficiency and simple structure based on discrete logarithms
- C. Being the very first commercial signature scheme
- D. Being based on integer factoring

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Its efficiency and simple structure based on discrete logarithms**

*Intuition:* The **Schnorr signature** scheme is based on discrete logarithms. It is highly valued for its mathematical simplicity, efficiency, and its linear algebraic structure, which enables signature aggregation (such as MuSig in Bitcoin protocols) where multiple signatures can be combined into a single, compact signature.
</details>

---

### 35. WEP's main cryptographic weakness stemmed from:
- A. Not using any encryption whatsoever
- B. Weak use of RC4 combined with short, reused initialization vectors
- C. Using AES incorrectly
- D. Requiring digital certificates

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Weak use of RC4 combined with short, reused initialization vectors**

*Intuition:* **WEP** used the RC4 stream cipher but paired it with a short 24-bit Initialization Vector (IV) sent in plaintext. On busy networks, this short IV space leads to rapid IV reuse. When the same key and IV are used, the same keystream is generated, allowing attackers to XOR two ciphertexts and recover the plaintext (keystream reuse vulnerability).
</details>

---

### 36. IPsec's ESP in transport mode encrypts the entire original IP header along with the payload.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* In **transport mode**, ESP encrypts only the IP packet payload (Layer 4 and above data), leaving the original IP header in plaintext. Encrypting the entire original IP header is unique to **tunnel mode**.
</details>

---

### 37. Kerberos relies exclusively on public-key cryptography and does not use symmetric encryption.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Kerberos is built fundamentally on **symmetric-key cryptography** (using algorithms like AES). In its core design, the KDC, client, and application server authenticate using shared secrets and symmetric session keys. (While PKINIT allows public keys for initial login, the protocol itself is symmetric-first).
</details>

---

### 38. S/MIME extends standard email primarily to add:
- A. HTML formatting support
- B. Faster mail delivery times
- C. Cryptographic security services such as confidentiality and digital signatures, based on X.509 certificates
- D. Larger attachment size limits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Cryptographic security services such as confidentiality and digital signatures, based on X.509 certificates**

*Intuition:* **S/MIME** (Secure/Multipurpose Internet Mail Extensions) adds security services (confidentiality via encryption, authentication/non-repudiation via signatures) to MIME email. It relies on a formal PKI structure utilizing X.509 certificates issued by trusted CAs.
</details>

---

### 39. IEEE ____ defines the standard for port-based network access control. (Fill in the blank)
*Answer:* **802.1X**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **802.1X**

*Intuition:* **IEEE 802.1X** is the standard for Port-Based Network Access Control (PNAC). It blocks all traffic on a switch port or wireless SSID until a Supplicant authenticates via an Authenticator to an Authentication Server (typically running RADIUS).
</details>

---

### 40. Secure Shell (SSH) is primarily used for:
- A. Secure remote login and command execution over an insecure network
- B. Wireless network encryption
- C. Email encryption
- D. DNS security

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Secure remote login and command execution over an insecure network**

*Intuition:* **SSH** was designed to replace insecure plaintext protocols like Telnet, rlogin, and rsh. It establishes a secure channel over TCP to provide remote command-line login, secure file transfers (SFTP), and port forwarding.
</details>

---

### 41. DomainKeys Identified Mail (DKIM) is designed mainly to:
- A. Encrypt the entire body of an email
- B. Compress email attachments
- C. Replace SMTP entirely
- D. Allow a receiving mail server to verify an email genuinely originated from the claimed sending domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Allow a receiving mail server to verify an email genuinely originated from the claimed sending domain**

*Intuition:* **DKIM** provides domain-level validation. It does not encrypt the message body for privacy; rather, it signs headers and body hashes so that destination servers can verify the message authenticity and check if it was tampered with in transit.
</details>

---

### 42. SHA-3 (Keccak) differs structurally from SHA-2 in that it is based on a:
- A. Feistel network
- B. Modular exponentiation scheme
- C. Elliptic curve group
- D. Sponge construction

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Sponge construction**

*Intuition:* While SHA-2 uses the Merkle-Damgård iterative compression construction, **SHA-3** uses a completely different architecture known as the **Sponge construction** (absorbing phase and squeezing phase). This protects SHA-3 against length extension attacks.
</details>

---

### 43. CMAC is a MAC algorithm based on:
- A. A stream cipher
- B. Public-key encryption
- C. A block cipher operating in a chaining mode
- D. A hash function only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A block cipher operating in a chaining mode**

*Intuition:* **CMAC** (Cipher-based Message Authentication Code) is a symmetric MAC that uses a block cipher (e.g., AES) operating in Cipher Block Chaining (CBC) mode. It applies subkeys to the final block to prevent length extension vulnerabilities present in standard CBC-MAC when handling variable-length messages.
</details>

---

### 44. A major security concern specific to multi-tenant cloud environments is:
- A. Lack of any network connectivity
- B. Ensuring data isolation between different customers sharing the same physical infrastructure
- C. Inability to use passwords at all
- D. The complete absence of encryption standards

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Ensuring data isolation between different customers sharing the same physical infrastructure**

*Intuition:* In a multi-tenant cloud, different users run workloads on the same physical CPUs, RAM, and disk systems. Ensuring strict logical **data isolation** is critical to prevent hypervisor escape, side-channel attacks, or memory leaks from exposing one customer's private data to another.
</details>

---

### 45. TLS improves on earlier SSL versions partly through the use of a more secure:
- A. Physical transport medium
- B. Compression-only algorithm
- C. Key derivation (pseudorandom) function
- D. IP addressing scheme

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Key derivation (pseudorandom) function**

*Intuition:* TLS modernized SSL's cryptographic foundation by refining the **Pseudorandom Function (PRF)** used to derive master keys and session keys. In TLS 1.2 and 1.3, this was upgraded to HKDF (HMAC-based Key Derivation Function) to guarantee key independence and cryptographically strong entropy.
</details>

---

### 46. SHA-3 is based on the Keccak sponge construction.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **Keccak** was the winning algorithm of the NIST SHA-3 competition. The core design is built entirely upon a sponge function, which represents a major structural divergence from the Merkle-Damgård construction of SHA-1/SHA-2.
</details>

---

### 47. Key distribution using asymmetric encryption can be used to securely distribute:
- A. Only digital certificates
- B. A symmetric session key, encrypted with the recipient's public key
- C. Only public keys
- D. Only hash digests

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A symmetric session key, encrypted with the recipient's public key**

*Intuition:* In hybrid cryptosystems, asymmetric encryption solves the key exchange problem. The sender generates a random symmetric session key (e.g., for AES) and encrypts it using the recipient's **public key**. Only the recipient can decrypt this session key using their corresponding **private key**.
</details>

---

### 48. SSL/TLS operates primarily at which layer to secure application traffic such as HTTP?
- A. The network layer
- B. The data link layer
- C. The physical layer
- D. The transport layer, between the application and TCP

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The transport layer, between the application and TCP**

*Intuition:* **SSL/TLS** acts as a security shim layer positioned directly between the application layer (e.g., HTTP) and the transport protocol (TCP). It receives plaintext data from applications, encrypts it, and passes it to TCP for transmission.
</details>

---

### 49. The property that it should be computationally infeasible to find two different inputs producing the same hash output is called:
- A. Weak diffusion
- B. Collision resistance
- C. Preimage resistance
- D. Second preimage resistance only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Collision resistance**

*Intuition:* **Collision resistance** guarantees that it is computationally infeasible to find *any* two arbitrary inputs $x \neq y$ such that $H(x) = H(y)$. Preimage resistance refers to finding an input matching a *fixed* hash value, while second preimage resistance refers to finding a collision with a *fixed* input.
</details>

---

### 50. To resist birthday attacks effectively, a hash function's output length should generally be:
- A. Equal to the desired security level in bits
- B. Independent of the security level
- C. Half the block cipher key size
- D. About twice the desired security level in bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. About twice the desired security level in bits**

*Intuition:* By the birthday paradox, finding a hash collision requires only $O(2^{n/2})$ operations for an $n$-bit hash. Therefore, to achieve a security strength of $S$ bits (requiring $2^S$ operations to break), the hash output size $n$ must be double the security target ($n = 2S$). This is why a 256-bit hash (SHA-256) is needed to achieve 128-bit collision resistance.
</details>

---

### 51. HMAC constructs a MAC by combining a hash function with:
- A. An elliptic curve group
- B. A secret key, used in a nested (inner/outer) hashing construction
- C. A public key
- D. A block cipher exclusively

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A secret key, used in a nested (inner/outer) hashing construction**

*Intuition:* **HMAC** nests hash function executions to prevent length-extension attacks: $\text{HMAC}(K, M) = H(K \oplus \text{opad} \parallel H(K \oplus \text{ipad} \parallel M))$. The secret symmetric key is padded to form inner and outer keys, which sandwich the message in a two-stage hash.
</details>

---

### 52. Cipher block chaining can be adapted to build a simple hash function by:
- A. Encrypting the message with a fixed key and using the final block as the hash value
- B. Repeating the Caesar cipher on the message
- C. Applying RSA directly to the message digest
- D. Running the Diffie-Hellman protocol on the message

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Encrypting the message with a fixed key and using the final block as the hash value**

*Intuition:* In CBC mode, each ciphertext block depends on all preceding plaintext blocks due to chaining. By using a public, fixed key and executing CBC encryption, the final block ($C_N$) acts as a basic hash digest of the entire message.
</details>

---

### 53. The X.509 standard defines the format for:
- A. Public-key certificates
- B. Password hashing schemes
- C. MAC algorithms
- D. Symmetric session keys

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Public-key certificates**

*Intuition:* **X.509** is the ITU-T standard defining the format for digital public-key certificates. It binds public keys to identities (such as websites or users) and specifies header fields, extension standards, and digital signature bindings.
</details>

---

### 54. A digital signature scheme primarily provides:
- A. Key distribution only
- B. Compression of the transmitted data
- C. Authentication, data integrity, and non-repudiation
- D. Confidentiality only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Authentication, data integrity, and non-repudiation**

*Intuition:* **Digital signatures** use asymmetric key pairs (signing with a private key, verifying with a public key). This guarantees authentication (verifying signer identity), data integrity (detecting changes to the signed content), and non-repudiation (the signer cannot deny the transaction).
</details>

---

### 55. A certificate revocation list (CRL) is used to:
- A. Identify certificates that should no longer be trusted before their expiration date
- B. Encrypt certificate data
- C. Distribute new public keys
- D. List all valid certificates currently in use

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Identify certificates that should no longer be trusted before their expiration date**

*Intuition:* If a user's private key is compromised, or a domain name changes, a CA must invalidate the certificate before its scheduled expiration. The CA publishes these invalidated certificate serial numbers in a signed **Certificate Revocation List (CRL)** or via OCSP responders.
</details>

---

### 56. In key wrapping, the primary goal is to:
- A. Distribute public keys via certificates
- B. Generate brand-new random keys
- C. Compress a cryptographic key for storage
- D. Protect cryptographic keys during storage or transmission by encrypting them

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Protect cryptographic keys during storage or transmission by encrypting them**

*Intuition:* **Key wrapping** uses symmetric key-encryption keys (KEK) to encrypt other cryptographic keys (like session keys or private keys). This secures sensitive keys when they are stored in database backends or transmitted over untrusted channels.
</details>

---

### 57. Public-key certificates chiefly solve which key distribution problem?
- A. The need for digital watermarking
- B. The need for symmetric encryption in general
- C. The need for out-of-band key exchange between every pair of communicating parties
- D. The need for hash functions

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The need for out-of-band key exchange between every pair of communicating parties**

*Intuition:* Without certificates, establishing trust on the internet would require every user to verify and exchange public keys out-of-band. Certificates solve this by letting trusted CAs vouch for public keys, allowing secure public key distribution over public, unencrypted channels.
</details>

---

### 58. Which of the following best describes CCM mode?
- A. A pure public-key encryption scheme
- B. Counter with CBC-MAC, combining CTR mode encryption with CBC-based authentication
- C. A key exchange protocol
- D. A stand-alone hash function

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Counter with CBC-MAC, combining CTR mode encryption with CBC-based authentication**

*Intuition:* **CCM** (Counter with CBC-MAC) is an AEAD (Authenticated Encryption with Associated Data) mode that pairs Counter (CTR) mode encryption for confidentiality with CBC-MAC for authentication, commonly used in Wi-Fi security.
</details>

---

### 59. Which of the following is a common basis for user authentication?
- A. Only a digital certificate
- B. Only biometric data
- C. Only a smart card
- D. Something the individual knows, such as a password

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Something the individual knows, such as a password**

*Intuition:* User authentication factors are categorized into three: **something you know** (passwords/PINs), **something you have** (tokens/smart cards), and **something you are** (biometrics). Passwords (something you know) are the most common historical and foundational basis for access control.
</details>

---

### 60. The security of HMAC depends most directly on the properties of the:
- A. Public-key infrastructure in use
- B. Underlying embedded hash function
- C. Block cipher used for bulk encryption
- D. Digital certificate authority involved

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Underlying embedded hash function**

*Intuition:* Because **HMAC** is built directly around an embedded cryptographic hash function (e.g., SHA-256 or SHA-512), the strength of the MAC (such as preimage and collision resistance) depends on the mathematical security and design properties of that specific hash function.
</details>

---

### 61. In a hierarchical PKI trust model, trust ultimately derives from:
- A. Each individual user's own key pair
- B. The message digest algorithm used
- C. A root certificate authority that other CAs and users trust
- D. The symmetric session key in use

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A root certificate authority that other CAs and users trust**

*Intuition:* In hierarchical PKI, intermediate Certificate Authorities form a chain of trust. This chain must anchor at a self-signed **Root Certificate Authority (CA)**. Operating systems and web browsers pre-install and trust these Root CA public keys to validate the entire tree.
</details>

---

### 62. Mobile device security concerns highlighted by Stallings include risks arising from:
- A. Devices being too large to lose
- B. Excessive built-in encryption
- C. A complete absence of wireless connectivity
- D. Lack of physical security control, since mobile devices are easily lost or stolen

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Lack of physical security control, since mobile devices are easily lost or stolen**

*Intuition:* Unlike locked server rooms, mobile devices exist in uncontrolled public spaces. The **lack of physical security control** makes devices highly susceptible to theft or loss, exposing local cached credentials and corporate data.
</details>

---

### 63. Personal Identity Verification (PIV), as standardized by NIST, is primarily used for:
- A. Standardized identity credentials for federal employees and contractors
- B. Consumer online banking only
- C. Wireless network encryption
- D. Email spam filtering

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Standardized identity credentials for federal employees and contractors**

*Intuition:* **PIV** (FIPS 201) is the NIST standard specifying the smart card-based identity credentials used across the U.S. federal government. It regulates credentials for logical computer access and physical building entries.
</details>

---

### 64. A Message Authentication Code (MAC) differs from a plain hash function primarily in that a MAC:
- A. Cannot detect message alteration
- B. Is always longer than the original message
- C. Uses a secret key shared between sender and receiver
- D. Produces a variable-length digest

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Uses a secret key shared between sender and receiver**

*Intuition:* While anyone can compute a plain hash function to verify integrity, only parties holding the **secret key** can generate or verify a **MAC**. This key dependency guarantees data authenticity (proof of origin) in addition to integrity.
</details>

---

### 65. IEEE 802.1X provides port-based network access control primarily by:
- A. Filtering traffic at the application layer
- B. Controlling access at the physical or data-link layer before higher-layer access is granted
- C. Managing DNS records
- D. Encrypting email messages

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Controlling access at the physical or data-link layer before higher-layer access is granted**

*Intuition:* **IEEE 802.1X** operates at Layer 2 (Data-Link) to secure the network edge. It prevents raw IP packet flow on switch ports or wireless associations until EAP-based authentication occurs, blocking access at the lowest layers.
</details>

---

### 66. Remote user authentication using asymmetric encryption can rely on a user proving possession of:
- A. A shared password only
- B. A symmetric session key generated by the server
- C. The private key corresponding to a certified public key
- D. A hash digest only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The private key corresponding to a certified public key**

*Intuition:* In asymmetric remote authentication (e.g., SSH public-key login), the user must sign a challenge sent by the server using their private key. By verifying the signature with the user's registered public key, the server validates identity possession without the user transmitting the secret key itself.
</details>

---

### 67. The SHA-2 family of hash functions includes variants such as:
- A. SHA-0 and SHA-3 only
- B. MD4 and MD5 only
- C. SHA-224, SHA-256, SHA-384, and SHA-512

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. SHA-224, SHA-256, SHA-384, and SHA-512**

*Intuition:* **SHA-2** is a family of cryptographic hash functions standardizing four primary variants: SHA-224, SHA-256, SHA-384, and SHA-512, which output digests matching their respective bit lengths.
</details>

---

### 68. A "chain of trust" in PKI refers to:
- A. A single certificate signed by itself
- B. A sequence of certificates, each signed by the next higher authority up to a trusted root
- C. A hash chain used for MACs
- D. A symmetric key exchange sequence

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A sequence of certificates, each signed by the next higher authority up to a trusted root**

*Intuition:* A **chain of trust** validates an end-entity certificate by verifying the digital signature of its issuing intermediate CA, repeating this validation upward sequentially until terminating at a pre-installed, trusted self-signed Root CA.
</details>

---

### 69. A key requirement for MACs, distinguishing them from ordinary hash functions, is resistance to:
- A. Forgery even when an attacker can request MACs on chosen messages
- B. Collision attacks only
- C. Data compression
- D. Key generation errors

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Forgery even when an attacker can request MACs on chosen messages**

*Intuition:* A secure MAC must be **unforgeable** under chosen-message attacks. An attacker allowed to query MAC tags for various chosen messages must remain computationally unable to forge a valid tag for any new, unqueried message without knowing the secret key.
</details>

---

### 70. Kerberos is best described as:
- A. A cryptographic hash function
- B. A public-key certificate format
- C. A firewall configuration standard
- D. A trusted third-party authentication service using symmetric-key cryptography and tickets

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A trusted third-party authentication service using symmetric-key cryptography and tickets**

*Intuition:* **Kerberos** is a trusted third-party authentication protocol. It uses symmetric-key cryptography (specifically utilizing a Key Distribution Center split into an Authentication Server and Ticket Granting Server) to issue time-limited ticket credentials for Single Sign-On.
</details>

---
