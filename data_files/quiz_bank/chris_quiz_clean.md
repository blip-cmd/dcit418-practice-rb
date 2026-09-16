# DCIT418: Christian's Quiz 1-3 and Quiz 4 (Parser Format)

Christian's Quiz 1-3 (IT security policy/7 domains and IoT topics) and Quiz 4
(cryptography and block cipher topics), formatted for parse_security_bank.py.
Quiz 1-3 were transcribed by hand after an automated parser proved unreliable
on their inconsistent formatting; Quiz 4 was extracted with an anchor-based
parser. Quiz 5 is excluded entirely: it is a garbled multilingual voice
transcript in which the real question text was never captured.

### 1. Which element of the security policy framework requires approval from upper management and applies to the entire organization?

- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

**Correct Answer:** **A. Policy**

**Intuition:** Policies are high-level statements that require senior/upper management approval and apply broadly across the entire organization, setting overall direction and intent. Standards, guidelines, and procedures typically flow from policies and can be approved/managed at lower levels since they support implementation rather than set organizational-wide mandate.

---

### 2. An information system is a safeguard or countermeasure an organization implements to help reduce risk.

- A. True
- B. False

**Correct Answer:** **B. False**

**Intuition:** This describes a control (safeguard/countermeasure to reduce risk), not an information system. An information system is the combination of hardware, software, data, and people used to collect, process, store, and distribute information, typically the asset being protected, not the safeguard itself.

---

### 3. The Local Area Network (LAN)-to-Wide Area Network (WAN) Domain is where the IT infrastructure links to a WAN and the Internet.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** The LAN-to-WAN Domain is exactly the boundary where an organization's internal network connects out to a wide area network and the public internet.

---

### 4. Cryptography is the practice of making data unreadable.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Cryptography transforms plaintext into ciphertext that is unreadable without the correct key, which is the core purpose the statement describes.

---

### 5. Availability is the tenet of information security that deals with uptime and downtime.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Availability, one leg of the CIA triad, means authorized users can access information and systems when needed, which is exactly a matter of uptime versus downtime.

---

### 6. The Sarbanes-Oxley Act (SOX) requires all types of financial institutions to protect customers' private financial information.

- A. True
- B. False

**Correct Answer:** **B. False**

**Intuition:** This describes the Gramm-Leach-Bliley Act (GLBA), not SOX. SOX applies to publicly traded companies and focuses on the accuracy and reliability of financial reporting and corporate governance controls, it isn't specifically about protecting customers' private financial information at financial institutions.

---

### 7. A router is a security appliance that is used to filter Internet Protocol (IP) packets and block unwanted packets.

- A. True
- B. False

**Correct Answer:** **B. False**

**Intuition:** A router's primary function is to forward and route traffic between networks based on IP addresses, it is a networking device, not a security appliance. While routers can use access control lists to filter some traffic, that description more accurately fits a firewall, whose primary purpose is filtering and blocking unwanted packets for security.

---

### 8. Vendors or service providers that have remote access to an Internet of Things (IoT) device may be able to pull information or data from your device without your permission.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Vendors with remote access to an IoT device can typically pull data/telemetry from it as part of normal operation (diagnostics, updates, usage analytics), often under terms buried in a EULA or privacy policy the user never fully reads or meaningfully consents to. So functionally, data can be collected without the user's informed permission, even if it's technically authorized in some fine print.

---

### 9. Which of the following is an example of a business-to-consumer (B2C) application of the Internet of Things (IoT)?

- A. Video conferencing
- B. Infrastructure monitoring
- C. Health monitoring
- D. Traffic monitoring

**Correct Answer:** **C. Health monitoring**

**Intuition:** Health monitoring (like wearable fitness trackers, smartwatches, or remote patient monitoring devices) is a direct B2C application, businesses provide these IoT devices/services directly to individual consumers. Infrastructure and traffic monitoring are typically government/enterprise applications, and video conferencing isn't inherently an IoT application.

---

### 10. Application service providers (ASPs) are software companies that build applications hosted in the cloud and on the Internet.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Application Service Providers develop, host, and deliver software applications to customers over the Internet/cloud rather than requiring users to install and run the software locally, customers access the application remotely, typically via a web browser.

---

### 11. The ownership of Internet of Things (IoT) data, as well as the metadata of that data, is sometimes in question.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Data ownership in IoT is often ambiguous, it's frequently unclear whether the device manufacturer, the service provider, or the end user actually owns the data (and associated metadata) generated by the device, and terms of service agreements don't always clarify this in a way that's favorable or transparent to the consumer.

---

### 12. Internet of Things (IoT) upgrades can be difficult to distribute and deploy, leaving gaps in the remediation of IoT devices or endpoints.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** IoT upgrades and patches can be difficult to distribute and deploy due to device diversity, limited connectivity, vendor support lifecycles, resource-constrained hardware, and devices deployed in hard-to-reach locations, which often leaves security gaps where vulnerabilities remain unremediated for extended periods.

---

### 13. Which organization pursues standards for Internet of Things (IoT) devices and is widely recognized as the authority for creating standards on the Internet?

- A. Internet Society
- B. Internet Engineering Task Force (IETF)
- C. Internet Association
- D. Internet Authority

**Correct Answer:** **B. Internet Engineering Task Force (IETF)**

**Intuition:** The IETF is widely recognized as the leading authority for developing and maintaining Internet standards, including protocols relevant to IoT. The Internet Society is IETF's parent organization but isn't itself the standards-writing body, and the other two options aren't legitimate standards organizations.

---

### 14. Vehicles that have Wi-Fi access and onboard computers require software patches and upgrades from the manufacturer.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Modern vehicles with Wi-Fi connectivity and onboard computers run software just like any connected device, and manufacturers need to issue patches and upgrades to fix bugs, address security vulnerabilities, and add functionality, much like smartphones or computers receive over-the-air updates.

---

### 15. Sharing in the data lifecycle means:

- A. Never share
- B. Sell without consent
- C. Enable reuse
- D. Share only with competitors

**Correct Answer:** **C. Enable reuse**

**Intuition:** In the data lifecycle, the sharing stage refers to making data available for others to access, use, or build on, enabling reuse (internally across teams, or externally with partners or the public), typically under defined permissions or licenses. It's not about selling data, restricting it entirely, or limiting it to competitors.

---

### 16. A benefit of conducting a Data Protection Impact Assessment (DPIA) is:

- A. Builds public trust
- B. Increases data breaches
- C. Ignores privacy risks
- D. Reduces compliance

**Correct Answer:** **A. Builds public trust**

**Intuition:** A DPIA identifies and mitigates privacy risks before a system or process launches, and demonstrating that care publicly signals accountability to users and regulators, which is what builds trust. The other options describe outcomes a DPIA is specifically meant to prevent, not produce.

---

### 17. A DPIA should be reviewed:

- A. When processing changes or regularly
- B. Only once
- C. Every ten years
- D. Never again

**Correct Answer:** **A. When processing changes or regularly**

**Intuition:** A DPIA isn't a one-and-done exercise, it should be revisited whenever there's a significant change to the processing activity (new data types, new purposes, new systems) or on a regular schedule, since risks can evolve over time. Treating it as a single, permanent assessment defeats its purpose of ongoing risk management.

---

### 18. Data localization drives investment in:

- A. Offshore storage
- B. Local data centers
- C. Manual record keeping
- D. Foreign data centers

**Correct Answer:** **B. Local data centers**

**Intuition:** Data localization laws require certain data to be stored and processed within a country's own borders, so complying with them directly drives investment in local data center infrastructure rather than offshore or foreign facilities.

---

### 19. A Data Protection Impact Assessment (DPIA) is:

- A. A process to identify privacy risks before launch
- B. Used only after a breach
- C. Optional under all laws
- D. Only for government agencies

**Correct Answer:** **A. A process to identify privacy risks before launch**

**Intuition:** A DPIA is a proactive process conducted before deployment to identify and mitigate privacy risks, not something used reactively after a breach, and it's legally mandatory (not optional) under laws like Ghana's Act 843 and Nigeria's NDPA, applying broadly rather than only to government agencies.

---

### 20. Many African countries lack:

- A. Internet access completely
- B. Interest in technology
- C. Skilled data-hosting professionals
- D. Basic electricity

**Correct Answer:** **C. Skilled data-hosting professionals**

**Intuition:** A recognized barrier to building local data-hosting capacity across much of Africa is a shortage of professionals skilled in data center operations and hosting infrastructure, not a lack of internet access, interest in technology, or electricity in absolute terms.

---

### 21. Strict localization rules across Africa can:

- A. Remove competition
- B. Create one digital market
- C. Split Africa's digital market
- D. Reduce compliance costs

**Correct Answer:** **C. Split Africa's digital market**

**Intuition:** If different African countries impose strict, inconsistent localization requirements, it creates barriers between national markets rather than unifying them, working against efforts like AfCFTA's Digital Trade Protocol to build an integrated continental digital economy.

---

### 22. The opposite of Privacy by Design is:

- A. Continuous privacy
- B. Proactive privacy
- C. Privacy added at the end
- D. Built-in privacy

**Correct Answer:** **C. Privacy added at the end**

**Intuition:** Privacy by Design means privacy protections are built into a system from the start; its opposite is bolting privacy measures on only after the system is already built, as an afterthought rather than a foundational requirement.

---

### 23. The mathematical hard problem underlying RSA's security is the difficulty of ____ large composite numbers.

**Correct Answer:** **factoring**

**Intuition:** Key Concept RSA relies on the **integer factorization problem**: **Easy direction:** Multiplying two large prime numbers p and q to compute n=p×q is computationally straightforward. **Hard direction:** Given only the large composite modulus n, finding the original prime factors p and q is computationally infeasible for sufficiently large keys (e.g., 2048-bit or 4096-bit RSA) using current classical algorithms.

---

### 24. The mathematical hard problem underlying RSA's security is the difficulty of ____ large composite numbers.

**Correct Answer:** **factoring**

**Intuition:** Completed Sentence: "The mathematical hard problem underlying RSA's security is the difficulty of **factoring** large composite numbers."

---

### 25. In Diffie-Hellman key exchange, both parties agree in advance on a large prime p and a ____ of that prime's multiplicative group.

**Correct Answer:** **generator**

**Intuition:** Completed Sentence: "In Diffie-Hellman key exchange, both parties agree in advance on a large prime p and a **generator** (or **primitive root**) of that prime's multiplicative group."  Key Concept: **p**: A large prime modulus defining the finite field Zp​ (or Galois field GF(p)). **g (Generator / Primitive Root)**: An integer whose successive powers modulo p generate all non-zero elements {1,2,…,p−1} of the multiplicative group Zp×​.

---

### 26. A rail fence cipher is an example of a:

- A. Substitution technique
- B. Transposition technique
- C. Product cipher
- D. Stream cipher

**Correct Answer:** **B. Transposition technique**

**Intuition:** Explanation: A **transposition cipher** works by rearranging (permuting) the order of plaintext characters rather than replacing them with other characters. The **rail fence cipher** is the simplest transposition technique, where plaintext letters are written diagonally across a number of "rails" and then read off row by row.

---

### 27. In Diffie-Hellman key exchange, both parties agree in advance on a large prime p and a ____ of that prime's multiplicative group.

**Correct Answer:** **generator**

**Intuition:** Completed Sentence: "In Diffie-Hellman key exchange, both parties agree in advance on a large prime p and a **generator** of that prime's multiplicative group." Brief Context: **Generator (g):** An element of the cyclic multiplicative group Zp∗​ whose powers modulo p generate every non-zero element in the group. **Why it matters:** Using a generator ensures that the generated public keys span the entire group size (p−1), maximizing the search space and making the Discrete Logarithm Problem (DLP) computationally infeasible to solve.

---

### 28. Which AES transformation cyclically shifts the rows of the state array?

- A. AddRoundKey
- B. SubBytes
- C. MixColumns
- D. ShiftRows

**Correct Answer:** **D. ShiftRows**

**Intuition:** How ShiftRows Works: In the AES state array (a 4×4 matrix of bytes), **ShiftRows** provides diffusion by cyclically shifting each row to the left by a different offset: **Row 0:** Not shifted (shifted by 0 bytes) **Row 1:** Cyclically shifted left by **1 byte** **Row 2:** Cyclically shifted left by **2 bytes** **Row 3:** Cyclically shifted left by **3 bytes** Overview of AES Round Transformations: **AddRoundKey (A):** Performs a bitwise XOR between the state matrix and the round key. **SubBytes (B):** A non-linear substitution step where each byte is replaced with another using a lookup table (S-box). **MixColumns (C):** A linear transformation that mixes the 4 bytes of each column using matrix multiplication in Galois Field GF(28). **ShiftRows (D):** The transposition step that cyclically shifts the state rows.

---

### 29. Blum Blum Shub (BBS) is an example of a PRNG built on:

- A. The Hill cipher
- B. The Playfair cipher
- C. Number-theoretic quadratic residue problems believed to be computationally hard
- D. The DES algorithm

**Correct Answer:** **C. Number-theoretic quadratic residue problems believed to be computationally hard**

**Intuition:** Key Mechanics of Blum Blum Shub (BBS): **Algorithm:** BBS generates pseudorandom bits via the recurrence relation: xn+1​=xn2​modM where M=p⋅q is a **Blum integer** (the product of two large prime numbers p and q, both congruent to 3mod4). **Security Foundation:** The output bits are provably secure under the assumption that the **Quadratic Residuosity Problem (QRP)** and integer factorization are computationally hard. Predicting the next bit is as hard as finding quadratic residues modulo M without knowing the factorization of M. Why the Other Options Are Incorrect: **A & B (Hill & Playfair):** These are classic polyalphabetic/polygraphic substitution ciphers based on matrix algebra and substitution tables, not secure PRNG primitives. **D (DES):** The Data Encryption Standard is a symmetric block cipher based on a Feistel network, not the foundation of the BBS generator.

---

### 30. The one-time pad remains perfectly secure even if the same key is reused for multiple messages.

- A. True
- B. False

**Correct Answer:** **B. False**

**Intuition:** Why It Is False: The One-Time Pad (OTP) offers **perfect secrecy** (information-theoretic security) _if and only if_ the key satisfies four strict conditions: 1. It is truly random. 2. It is at least as long as the message. 3. It is kept completely secret. 4. **It is never reused** (hence the name _one-time_). What Happens When a Key Is Reused (Two-Time Pad): If two plaintexts (P1​ and P2​) are encrypted with the same key (K): C1​=P1​⊕K C2​=P2​⊕K An eavesdropper can XOR the two ciphertexts together: C1​⊕C2​=(P1​⊕K)⊕(P2​⊕K)=P1​⊕P2​ The key cancels out completely, leaving the XOR of the two plaintexts (P1​⊕P2​). From there, attackers can recover both messages using statistical language analysis and **crib-dragging** techniques.

---

### 31. The AES SubBytes transformation provides:

- A. Block chaining
- B. Nonlinear byte substitution using an S-box
- C. Key mixing
- D. Diffusion via row shifting

**Correct Answer:** **B. Nonlinear byte substitution using an S-box**

**Intuition:** How SubBytes Works: **Function:** It operates on each byte of the 4×4 state array independently. **Mechanism:** Each byte is replaced with its corresponding entry from a fixed substitution table called the **S-box** (Substitution Box). **Cryptographic Goal:** It provides **confusion** (non-linearity) in AES, ensuring that the relationship between the key/plaintext and ciphertext is mathematically complex and resistant to linear and differential cryptanalysis. The S-box is algebraically derived from taking the multiplicative inverse in GF(28) followed by an affine transformation. Overview of Other Transformations: **A (Block chaining):** A property of cipher modes of operation (such as CBC mode), not an AES internal round step. **C (Key mixing):** Handled by the **AddRoundKey** transformation (XORing the round key with the state). **D (Diffusion via row shifting):** Handled by the **ShiftRows** transformation.

---

### 32. According to the OSI security architecture, which term refers to something that has the potential to cause harm to a system?

- A. Threat
- B. Risk
- C. Vulnerability
- D. Attack

**Correct Answer:** **A. Threat**

**Intuition:** Key Definitions in the OSI Security Architecture (ITU-T X.800 / RFC 4949): **Threat (A):** A potential for violation of security; any circumstance, capability, action, or event that has the **potential to cause harm** to an asset or system by breaching confidentiality, integrity, or availability. **Attack (D):** An assault on system security that derives from an intelligent threat. It is the **actual realization or execution** of a threat, a deliberate attempt to bypass security controls and exploit a system. **Vulnerability (C):** A **flaw or weakness** in a system’s design, implementation, operation, or management that could be exploited by a threat. **Risk (B):** The **expectation of loss**, calculated as the likelihood (probability) that a threat will exploit a vulnerability multiplied by the resulting impact/harm.

---

### 33. The Euclidean algorithm is used primarily to compute:

- A. The greatest common divisor of two integers
- B. Discrete logarithms
- C. The prime factorization of a number
- D. Modular exponentiation directly

**Correct Answer:** **A. The greatest common divisor of two integers**

**Intuition:** How the Euclidean Algorithm Works: The algorithm is based on the principle that the greatest common divisor (gcd) of two integers a and b (where a≥b) remains the same if a is replaced by the remainder of a divided by b: gcd(a,b)=gcd(b,amodb) This process is repeated iteratively until the remainder reaches zero; the last non-zero remainder is gcd(a,b). **Extended Euclidean Algorithm:** An extension that not only finds gcd(a,b), but also integers x and y such that ax+by=gcd(a,b) (Bézout's identity). This is widely used in cryptography (e.g., RSA) to compute **modular multiplicative inverses**. Why the Other Options Are Incorrect: **B. Discrete logarithms:** Computed using algorithms like the Baby-step Giant-step, Pollard's rho algorithm for logarithms, or the Index Calculus method. **C. Prime factorization:** Computed using integer factorization algorithms such as Pollard's ρ, Fermat's factorization method, or the General Number Field Sieve (GNFS). **D. Modular exponentiation:** Computed efficiently using the **Square-and-Multiply** (binary exponentiation) algorithm.

---

### 34. For two distinct primes p and q, phi(pq) equals:

- A. p+q
- B. (p-1)(q-1)
- C. pq
- D. p-q

**Correct Answer:** **B. (p-1)(q-1)**

**Intuition:** Mathematical Proof: Euler's totient function, ϕ(n), counts the number of integers in the range [1,n−1] that are coprime (relatively prime) to n. 1. **Multiplicative Property:** Euler's totient function is strictly multiplicative. For any two coprime integers a and b where gcd(a,b)=1: ϕ(ab)=ϕ(a)⋅ϕ(b) 2. **Prime Modulus:** For any prime number p, all integers from 1 to p−1 share no common factors with p other than 1. Therefore: ϕ(p)=p−1andϕ(q)=q−1 3. **Combined:** Since p and q are distinct primes, gcd(p,q)=1: ϕ(pq)=ϕ(p)⋅ϕ(q)=(p−1)(q−1) Cryptographic Significance: This identity forms the mathematical foundation of **RSA key generation**, where: The public modulus is n=p⋅q. The totient ϕ(n)=(p−1)(q−1) is used to compute the private decryption exponent d such that: d⋅e≡1(modϕ(n))

---

### 35. In the Feistel cipher structure, the function applied within each round is called the ____ function.

**Correct Answer:** **round**

**Intuition:** Completed Sentence: "In the Feistel cipher structure, the function applied within each round is called the **round** function." Key Properties of the Round Function (F): **Equation:** In each round i, the plaintext block is split into left (L) and right (R) halves: Li​=Ri−1​ Ri​=Li−1​⊕F(Ri−1​,Ki​) **Non-Invertibility Allowed:** The round function F does **not** need to be mathematically reversible (invertible). The structure of the Feistel network guarantees that decryption works identically to encryption (simply using the round subkeys Ki​ in reverse order) because the XOR operation (⊕) cancels itself out.

---

### 36. The security of ECC rests on the difficulty of the:

- A. Elliptic curve discrete logarithm problem
- B. Subset sum problem
- C. Knapsack problem
- D. Integer factorization problem

**Correct Answer:** **A. Elliptic curve discrete logarithm problem**

**Intuition:** What is the ECDLP (Elliptic Curve Discrete Logarithm Problem)? In Elliptic Curve Cryptography (ECC): Given an elliptic curve over a finite field, a base point P, and a scalar multiple point Q such that: Q=kP=k times![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.548em"%20viewBox="0%200%20400000%20548"%20preserveAspectRatio="xMinYMin%20slice"><path%20d="M0%206l6-6h17c12.688%200%2019.313.3%2020%201%204%204%207.313%208.3%2010%2013%0A%2035.313%2051.3%2080.813%2093.8%20136.5%20127.5%2055.688%2033.7%20117.188%2055.8%20184.5%2066.5.688%0A%200%202%20.3%204%201%2018.688%202.7%2076%204.3%20172%205h399450v120H429l-6-1c-124.688-8-235-61.7%0A-331-161C60.687%20138.7%2032.312%2099.3%207%2054L0%2041V6z"></path></svg>)![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.548em"%20viewBox="0%200%20400000%20548"%20preserveAspectRatio="xMidYMin%20slice"><path%20d="M199572%20214%0Ac100.7%208.3%20195.3%2044%20280%20108%2055.3%2042%20101.7%2093%20139%20153l9%2014c2.7-4%205.7-8.7%209-14%0A%2053.3-86.7%20123.7-153%20211-199%2066.7-36%20137.3-56.3%20212-62h199568v120H200432c-178.3%0A%2011.7-311.7%2078.3-403%20201-6%208-9.7%2012-11%2012-.7.7-6.7%201-18%201s-17.3-.3-18-1c-1.3%200%0A-5-4-11-12-44.7-59.3-101.3-106.3-170-141s-145.3-54.3-229-60H0V214z"></path></svg>)![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.548em"%20viewBox="0%200%20400000%20548"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M399994%200l6%206v35l-6%2011c-56%20104-135.3%20181.3-238%20232-57.3%0A%2028.7-117%2045-179%2050H-300V214h399897c43.3-7%2081-15%20113-26%20100.7-33%20179.7-91%20237%0A-174%202.7-5%206-9%2010-13%20.7-1%207.3-1%2020-1h17z"></path></svg>)P+P+⋯+P​​ It is computationally easy to compute Q given k and P (via point addition and doubling algorithms). However, given only P and Q, finding the integer k (the private key) is the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**, which is computationally intractable for sufficiently large curve parameters. Because the best-known algorithms for solving ECDLP require fully exponential time (unlike classical DLP or integer factorization, which have sub-exponential algorithms like GNFS), ECC provides comparable security to RSA with much smaller key sizes (e.g., a 256-bit ECC key offers roughly equivalent security to a 3072-bit RSA key). Why the Other Options Are Incorrect: **B & C (Subset sum / Knapsack problem):** The basis for early lattice/combinatorial public-key schemes such as the **Merkle–Hellman Knapsack Cryptosystem** (most variants of which were later broken). **D (Integer factorization problem):** The mathematical foundation for **RSA** and the **Rabin** cryptosystem.

---

### 37. Rotor machines historically achieve strong security by:

- A. Using a single fixed substitution
- B. Encrypting only vowels
- C. Using modular exponentiation
- D. Cascading multiple substitution ciphers that change with each keystroke

**Correct Answer:** **D. Cascading multiple substitution ciphers that change with each keystroke**

**Intuition:** How Rotor Machines Work: **Cascaded Substitution:** A rotor machine (such as the **Enigma**, **Typex**, or **SIGABA**) contains several wired cylinders (rotors) positioned in series. Each individual rotor acts as an independent monoalphabetic substitution cipher. **Dynamic Stepping Mechanism:** When a key is pressed, an electrical current flows through the series of rotors to produce the ciphertext letter. Before or after the keystroke, one or more rotors step (rotate) by one position. **Polyalphabetic Complexity:** Rotating the cylinders alters the internal wiring pathways for the next character, creating a dynamically changing compound substitution cipher with an extremely long repetition period (e.g., 263=17,576 states for a basic 3-rotor setup, and even higher with stepping odometers and plugboards). Why the Other Options Are Incorrect: **A (Single fixed substitution):** Describes a simple **monoalphabetic substitution cipher** (such as the Caesar cipher or a random substitution alphabet), which is easily broken using frequency analysis. **B (Encrypting only vowels):** Historically untrue; rotor machines encrypted all standard alphabet characters. **C (Modular exponentiation):** The mathematical primitive used in modern public-key cryptography (e.g., RSA, Diffie-Hellman), not mechanical rotor devices.

---

### 38. In the Caesar cipher, if the shift key is 3, the plaintext letter 'A' encrypts to:

- A. 'D'
- B. 'C'
- C. 'X'
- D. 'B'

**Correct Answer:** **A. 'D'**

**Intuition:** Explanation: The Caesar cipher encrypts each plaintext letter by shifting it down the alphabet by a fixed number of positions (the shift key, k=3). **Formula:** C≡(P+k)(mod26) **Step-by-step calculation:** If A=0, then C=(0+3)(mod26)=3 Mapping indices back to letters (0=A,1=B,2=C,3=D): A+1![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.522em"%20viewBox="0%200%20400000%20522"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M0%20241v40h399891c-47.3%2035.3-84%2078-110%20128%0A-16.7%2032-27.7%2063.7-33%2095%200%201.3-.2%202.7-.5%204-.3%201.3-.5%202.3-.5%203%200%207.3%206.7%2011%2020%0A%2011%208%200%2013.2-.8%2015.5-2.5%202.3-1.7%204.2-5.5%205.5-11.5%202-13.3%205.7-27%2011-41%2014.7-44.7%0A%2039-84.5%2073-119.5s73.7-60.2%20119-75.5c6-2%209-5.7%209-11s-3-9-9-11c-45.3-15.3-85%0A-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5%0A-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14%200-21%203.7-21%2011%200%202%202%2010.3%206%2025%2020.7%2083.3%2067%0A%20151.7%20139%20205zm0%200v40h399900v-40z"></path></svg>)​B+2![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.522em"%20viewBox="0%200%20400000%20522"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M0%20241v40h399891c-47.3%2035.3-84%2078-110%20128%0A-16.7%2032-27.7%2063.7-33%2095%200%201.3-.2%202.7-.5%204-.3%201.3-.5%202.3-.5%203%200%207.3%206.7%2011%2020%0A%2011%208%200%2013.2-.8%2015.5-2.5%202.3-1.7%204.2-5.5%205.5-11.5%202-13.3%205.7-27%2011-41%2014.7-44.7%0A%2039-84.5%2073-119.5s73.7-60.2%20119-75.5c6-2%209-5.7%209-11s-3-9-9-11c-45.3-15.3-85%0A-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5%0A-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14%200-21%203.7-21%2011%200%202%202%2010.3%206%2025%2020.7%2083.3%2067%0A%20151.7%20139%20205zm0%200v40h399900v-40z"></path></svg>)​C+3![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.522em"%20viewBox="0%200%20400000%20522"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M0%20241v40h399891c-47.3%2035.3-84%2078-110%20128%0A-16.7%2032-27.7%2063.7-33%2095%200%201.3-.2%202.7-.5%204-.3%201.3-.5%202.3-.5%203%200%207.3%206.7%2011%2020%0A%2011%208%200%2013.2-.8%2015.5-2.5%202.3-1.7%204.2-5.5%205.5-11.5%202-13.3%205.7-27%2011-41%2014.7-44.7%0A%2039-84.5%2073-119.5s73.7-60.2%20119-75.5c6-2%209-5.7%209-11s-3-9-9-11c-45.3-15.3-85%0A-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5%0A-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14%200-21%203.7-21%2011%200%202%202%2010.3%206%2025%2020.7%2083.3%2067%0A%20151.7%20139%20205zm0%200v40h399900v-40z"></path></svg>)​D

---

### 39. Elliptic curve cryptography (ECC) is attractive because it can achieve security comparable to RSA with:

- A. Significantly smaller key sizes
- B. No underlying mathematical hard problem
- C. No public key at all
- D. Larger key sizes

**Correct Answer:** **A. Significantly smaller key sizes**

**Intuition:** Why ECC Requires Smaller Key Sizes: **Underlying Hard Problem:** The security of ECC is based on the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**. The best-known classical algorithms to solve ECDLP (such as Pollard's rho) run in **fully exponential time** (O(n![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="1.08em"%20viewBox="0%200%20400000%201080"%20preserveAspectRatio="xMinYMin%20slice"><path%20d="M95,702%0Ac-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14%0Ac0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54%0Ac44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10%0As173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429%0Ac69,-144,104.5,-217.7,106.5,-221%0Al0%20-0%0Ac5.3,-9.3,12,-14,20,-14%0AH400000v40H845.2724%0As-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7%0Ac-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z%0AM834%2080h400000v40h-400000z"></path></svg>)​)). **Comparison with RSA:** In contrast, the integer factorization problem underlying RSA can be attacked using the **General Number Field Sieve (GNFS)**, which runs in **sub-exponential time**. Because GNFS scales faster against larger RSA moduli, RSA requires exponentially larger key sizes to maintain equivalent security levels. Key Size Comparison for Equivalent Security Levels (NIST Guidelines): |Symmetric Security Level|ECC Key Size|RSA Modulus Size|Key Size Ratio| |---|---|---|---| |**112-bit** (Legacy)|224 bits|2048 bits|~1 : 9| |**128-bit** (Standard)|**256 bits**|**3072 bits**|~1 : 12| |**192-bit** (High)|384 bits|7680 bits|~1 : 20| |**256-bit** (Ultra)|512 bits|15360 bits|~1 : 30| Practical Benefits: Faster mathematical computation and lower processing latency. Reduced power consumption (ideal for mobile, smart cards, and IoT devices). Smaller certificate and digital signature payloads over network transmissions. Why the Other Options Are Incorrect: **B (No underlying mathematical hard problem):** False; ECC relies directly on the hardness of the ECDLP. **C (No public key at all):** False; ECC is an asymmetric public-key cryptosystem (a public key is a point on the curve, and the private key is an integer scalar). **D (Larger key sizes):** Incorrect; ECC's primary advantage is requiring much _smaller_ keys than RSA.

---

### 40. In cryptanalysis, a "known plaintext" attack assumes the analyst has:

- A. The ciphertext plus one or more known plaintext-ciphertext pairs
- B. No information at all
- C. Access to the decryption device to try chosen ciphertexts
- D. Only the ciphertext

**Correct Answer:** **A. The ciphertext plus one or more known plaintext-ciphertext pairs**

**Intuition:** Cryptanalysis Attack Models: **Known-Plaintext Attack (KPA) [Option A]:** The attacker has access to one or more pairs of original plaintext and its corresponding encrypted ciphertext. The goal is to discover the secret key or create an algorithm to decrypt future messages. **Ciphertext-Only Attack (COA) [Option D]:** The attacker has access **only** to a set of ciphertexts, with no corresponding plaintext or decryption capabilities. This is the weakest position for an attacker. **Chosen-Plaintext Attack (CPA):** The attacker can choose arbitrary plaintexts and obtain their corresponding ciphertexts from the encryption system (without knowing the key). **Chosen-Ciphertext Attack (CCA) [Option C]:** The attacker can choose arbitrary ciphertexts and obtain their decrypted plaintexts from a decryption oracle/device.

---

### 41. The Playfair cipher encrypts:

- A. Trigrams
- B. Whole words
- C. Digrams (pairs of letters)
- D. Single letters

**Correct Answer:** **C. Digrams (pairs of letters)**

**Intuition:** How the Playfair Cipher Works: The Playfair cipher is a **polygraphic substitution cipher** that encrypts digraphs (pairs of two letters) instead of single letters, using a 5×5 grid populated with a keyword: 1. **Pairing:** The plaintext is split into two-letter pairs (digrams). If a pair contains duplicate letters (e.g., "EE"), a filler character like 'X' is inserted ("EX", "EX"). 2. **5x5 Matrix Rules:** **Same Row:** Each letter is replaced by the letter to its immediate right (wrapping around to the left). **Same Column:** Each letter is replaced by the letter immediately below it (wrapping around to the top). **Rectangle (Different Row & Column):** Each letter is replaced by the letter on the same row in the column occupied by the other letter. Why It Matters: By encrypting digrams rather than single letters, the Playfair cipher flattens the standard single-letter frequency distribution of the language (e.g., masking the high frequency of 'E' in English), making simple frequency analysis significantly harder.

---

### 42. In ECB mode, identical plaintext blocks always produce identical ciphertext blocks.

- A. True
- B. False

**Correct Answer:** **A. True**

**Intuition:** Why This Is True: In **Electronic Codebook (ECB)** mode, each fixed-size block of plaintext (Pi​) is encrypted independently using the exact same key (K): Ci​=EK​(Pi​) Because the encryption function is deterministic and involves no initialization vector (IV) or chaining with previous blocks, whenever two plaintext blocks are identical (Pa​=Pb​), their corresponding ciphertext blocks are guaranteed to be identical (Ca​=Cb​). Security Implication: This property makes ECB mode **insecure for encrypting structured data or images** (such as the well-known _ECB Penguin_ demonstration), because high-level patterns and repetitions in the plaintext remain clearly visible in the ciphertext.

---

### 43. Steganography differs from encryption in that it:

- A. Scrambles the content of a message
- B. Only works on digital images
- C. Requires a public key
- D. Conceals the very existence of a message

**Correct Answer:** **D. Conceals the very existence of a message**

**Intuition:** Core Difference: Steganography vs. Cryptography |Feature|Steganography|Cryptography (Encryption)| |---|---|---| |**Primary Goal**|**Conceal existence**, hide the fact that a message is being sent at all.|**Conceal meaning**, scramble the message so unauthorized parties cannot read it.| |**Visibility**|Inconspicuous carrier file (e.g., an ordinary-looking image or audio file).|Obvious ciphertext (looks like random, scrambled data).| |**Attacker Awareness**|The adversary typically does not realize communication is occurring.|The adversary knows communication is happening but cannot decipher the contents.| Why the Other Options Are Incorrect: **A. Scrambles the content of a message:** This is the definition of **encryption** (cryptography), which transforms readable plaintext into unreadable ciphertext. **B. Only works on digital images:** Steganography can be applied across many mediums, including audio files, video streams, network packet headers, HTML whitespace, and even physical invisible ink. **C. Requires a public key:** Steganography does not require public-key cryptography; it relies on embedding algorithms and shared embedding keys (stego-keys).

---

### 44. A key advantage of the Feistel structure is that:

- A. The same hardware or software can be used for both encryption and decryption
- B. It requires two different algorithms for encryption and decryption
- C. It cannot use a round function
- D. It only works with 64-bit blocks

**Correct Answer:** **A. The same hardware or software can be used for both encryption and decryption**

**Intuition:** A Feistel cipher's decryption process is structurally identical to encryption, just run with the round subkeys in reverse order, so the same hardware or software implementation can perform both operations, with no need for a separate inverse cipher.

---

### 45. A key advantage of the Feistel structure is that:

- A. The same hardware or software can be used for both encryption and decryption
- B. It requires two different algorithms for encryption and decryption
- C. It cannot use a round function
- D. It only works with 64-bit blocks

**Correct Answer:** **A. The same hardware or software can be used for both encryption and decryption**

**Intuition:** A Feistel cipher's decryption process is structurally identical to encryption, just run with the round subkeys in reverse order, so the same hardware or software implementation can perform both operations, with no need for a separate inverse cipher.

---

### 46. AES was originally designed and submitted to NIST under the name ____

**Correct Answer:** **Rijndael**

**Intuition:** Rijndael, designed by Joan Daemen and Vincent Rijmen, was the algorithm NIST selected through its open competition and standardized as AES.

---

### 47. Fermat's Little Theorem and Euler's Theorem are foundational to the correctness of the ____ public-key algorithm.

**Correct Answer:** **RSA**

**Intuition:** RSA's decryption correctness proof relies on Fermat's Little Theorem for a prime modulus, generalized by Euler's Theorem to RSA's composite modulus n = p times q.

---

### 48. A cipher in which plaintext bits or letters are rearranged without changing their values is called a ____ cipher.

**Correct Answer:** **transposition**

**Intuition:** A transposition (or permutation) cipher only reorders the positions of plaintext symbols; it never substitutes one symbol for another, which is what distinguishes it from a substitution cipher.

---

### 49. Which mode of block cipher operation encrypts blocks independently without chaining, so identical plaintext blocks produce identical ciphertext blocks?

- A. ECB
- B. CBC
- C. CTR
- D. CFB

**Correct Answer:** **A. ECB**

**Intuition:** ECB (Electronic Codebook) encrypts each block independently under the same key with no dependency on previous blocks or an IV, so identical plaintext blocks always produce identical ciphertext blocks, which is exactly the pattern-leakage weakness that makes it unsafe for most data.

---
