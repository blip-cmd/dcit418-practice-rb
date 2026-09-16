# DCIT 418: Systems and Network Security
## Consolidated Quiz Bank — Question Bank (Quizzes 1-5)

366 questions with verified answers and worked solutions, spanning IT security policy & infrastructure domains, IoT/mobile/BYOD, and cryptography (block ciphers, modes of operation) from William Stallings' *Cryptography and Network Security* and course lecture material.

---

## Quiz 1: IT Security Policy Framework & Infrastructure Domains

#### Part A: Core Exam Takes (Questions 1–30)

### 1. Which element of the IT security policy framework provides detailed written definitions for hardware and software and how they are to be used?
- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Standard**

*Intuition:* A **Standard** sets mandatory technical specifications, operational configurations, and baseline hardware/software requirements across an organization. While high-level *Policies* outline governance intent without technical specs and *Guidelines* offer discretionary advice, standards enforce exact compulsory technical baselines.
</details>

---

### 2. The Sarbanes-Oxley Act (SOX) requires all types of financial institutions to protect customers' private financial information.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* The Sarbanes-Oxley Act (SOX) targets **publicly traded companies** to ensure financial reporting accuracy, internal accounting controls, and fraud prevention—not customer privacy across all financial institutions. Protecting customer financial privacy is specifically governed by the **Gramm-Leach-Bliley Act (GLBA)**.
</details>

---

### 3. The User Domain of a typical IT infrastructure defines the people and processes that access an organization's information systems.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The **User Domain** encompasses end-users, system administrators, contractors, and human operational processes interacting with IT assets. Because social engineering, credential theft, and user error target this human element, it represents the most vulnerable perimeter layer in security architecture.
</details>

---

### 4. True or False? A data classification standard provides a consistent definition for how an organization should handle and secure different types of data.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* A **Data Classification Standard** categorizes organizational assets into structured sensitivity tiers (e.g., Public, Internal, Confidential, Restricted) and establishes mandatory handling, encryption, storage, and disposal rules for each tier.
</details>

---

### 5. Which element of the security policy framework offers suggestions rather than mandatory actions?
- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Guideline**

*Intuition:* A **Guideline** provides optional recommendations and industry best practices to assist decision-making. Unlike policies, standards, and procedures—which are compulsory and strictly enforced—guidelines offer operational flexibility when rigid constraints are impractical.
</details>

---

### 6. Hypertext Transfer Protocol (HTTP) is the communications protocol between web browsers and websites with data in cleartext.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Standard HTTP transmits application data between clients and web servers in unencrypted **cleartext (plain text)**, making payload packets vulnerable to network eavesdropping and man-in-the-middle (MitM) attacks. Encrypted communications require **HTTPS** (using TLS/SSL).
</details>

---

### 7. Bob is the information security and compliance manager for a financial institution. Which regulation is most likely to directly apply to Bob's employer?
- A. Federal Information Security Management Act (FISMA)
- B. Health Insurance Portability and Accountability Act (HIPAA)
- C. Children's Internet Protection Act (CIPA)
- D. Gramm-Leach-Bliley Act (GLBA)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Gramm-Leach-Bliley Act (GLBA)**

*Intuition:* **GLBA** specifically regulates financial institutions, requiring them to protect nonpublic personal financial information (NPI) and enforce comprehensive administrative, technical, and physical safeguards programs. FISMA regulates federal agencies, HIPAA governs healthcare, and CIPA applies to schools/libraries.
</details>

---

### 8. An information system is a safeguard or countermeasure an organization implements to help reduce risk.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* An **Information System** is an integrated collection of hardware, software, data, and users designed to collect, store, process, and distribute information. It inherently contains vulnerabilities and creates business risks; security controls/safeguards (e.g., firewalls, access controls) are added *to* the system to reduce risk.
</details>

---

### 9. A brute-force password attack and the theft of a mobile worker's laptop are risks most likely found in which domain of a typical IT infrastructure?
- A. User Domain
- B. Workstation Domain
- C. Remote Access Domain
- D. Local Area Network (LAN) Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Remote Access Domain** *(Note: Also classified under Workstation Domain for physical endpoint hardware)*

*Intuition:* The **Remote Access Domain** governs technologies and security policies enabling off-site employees to connect to corporate resources (e.g., VPNs, remote portals). A brute-force password attack against remote portals/VPNs and physical theft of a mobile worker's laptop off-site specifically jeopardize the Remote Access perimeter.
</details>

---

### 10. Which term describes the level of exposure to some event that has an effect on an asset, usually the likelihood that something bad will happen to an asset?
- A. Risk
- B. Countermeasure
- C. Vulnerability
- D. Threat

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Risk**

*Intuition:* **Risk** quantifies the overall exposure by multiplying the likelihood of a threat occurrence by its potential business impact ($\text{Risk} = \text{Threat} \times \text{Vulnerability} \times \text{Impact}$). A threat is the potential event, a vulnerability is the flaw, and a countermeasure is the mitigating control.
</details>

---

### 11. Which network device is designed to block network connections that are identified as potentially malicious?
- A. Intrusion detection system (IDS)
- B. Intrusion prevention system (IPS)
- C. Router
- D. Web server

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Intrusion prevention system (IPS)**

*Intuition:* An **Intrusion Prevention System (IPS)** is an inline security appliance that inspects live traffic flow and actively drops/blocks malicious connections in real time. In contrast, an Intrusion Detection System (IDS) is passive, monitoring network traffic and generating alerts without blocking packets.
</details>

---

### 12. What is a primary risk to the Workstation Domain, the Local Area Network (LAN) Domain, and the System/Application Domain?
- A. Unauthorized access to systems
- B. Unauthorized network probing and port scanning
- C. Mobile worker token or other authentication stolen
- D. Downtime of IT systems for an extended period after a disaster

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Unauthorized access to systems**

*Intuition:* **Unauthorized access** is a critical cross-domain threat vector that affects endpoint workstations (local unauthorized access), LANs (lateral network movement), and applications/servers (unauthorized data access and privilege escalation).
</details>

---

### 13. Which security control is most helpful in protecting against eavesdropping on wide area network (WAN) transmissions?
- A. Encryption (specifically WAN Encryption / IPsec VPNs)
- B. Access Control Lists (ACLs)
- C. Firewalls
- D. Data Loss Prevention (DLP)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Encryption (specifically WAN Encryption / IPsec VPNs)**

*Intuition:* Wide Area Networks (WANs) traverse untrusted third-party telecom and public internet infrastructure. **Cryptographic Encryption** (such as IPsec or TLS tunnels) transforms payload data into unreadable ciphertext, ensuring confidentiality even if WAN data lines are wiretapped or intercepted.
</details>

---

### 14. Availability is the tenet of information security that deals with uptime and downtime.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **Availability** (the "A" in the CIA Triad) guarantees that systems, data, and networks are accessible to authorized users whenever required. Controls like redundancy, failover clusters, data backups, and DDoS mitigation protect against unplanned system downtime.
</details>

---

### 15. The Local Area Network (LAN) Domain of a typical IT infrastructure includes both physical network components and logical configuration of services for users.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The **LAN Domain** integrates physical hardware assets (switches, Ethernet cabling, wireless access points) with logical network configurations (VLAN segmentation, IP subnetting, local DNS/DHCP, and Network Access Control) to manage internal traffic safely.
</details>

---

### 16. Maria is writing a policy that defines her organization's data classification standard. The policy designates the IT assets that are critical to the organization's mission and defines the organization's systems, uses, and data priorities. It also identifies assets within the seven domains of a typical IT infrastructure. Which policy is Maria writing?
- A. Security awareness policy
- B. Asset classification policy
- C. Asset protection policy
- D. Asset management policy

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Asset classification policy**

*Intuition:* An **Asset Classification Policy** categorizes physical, software, and data assets according to their criticality, value, sensitivity, and business risk across all IT infrastructure domains, laying the groundwork for appropriate risk-aligned safeguards.
</details>

---

### 17. True or False? Service-level agreements (SLAs) are a common part of the Local Area Network (LAN)-to-Wide Area Network (WAN) Domain of a typical IT infrastructure.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The **LAN-to-WAN Domain** relies on external Telecommunication Service Providers (ISPs). **Service-Level Agreements (SLAs)** are legal contracts establishing enforceable baseline standards for network uptime percentage, bandwidth capacity, packet latency, and repair response times.
</details>

---

### 18. Unauthorized access to data centers and downtime of servers are risks to which domain of an IT infrastructure?
- A. Workstation Domain
- B. Wide Area Network (WAN) Domain
- C. Remote Access Domain
- D. System/Application Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. System/Application Domain**

*Intuition:* The **System/Application Domain** houses backend enterprise servers, databases, data center infrastructure, and core software applications. Server downtime and unauthorized physical/logical access to data centers directly endanger this domain.
</details>

---

### 19. Which element of the security policy framework requires approval from upper management and applies to the entire organization?
- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Policy**

*Intuition:* A **Policy** is an executive-level governance document mandated and signed by senior leadership. It establishes organization-wide security goals, compliance mandates, and high-level behavioral/operational expectations without delving into granular technical steps.
</details>

---

### 20. What measures the average amount of time between failures for a particular system?
- A. Uptime
- B. Mean time to failure (MTTF)
- C. Mean time to repair (MTTR)
- D. Recovery time objective (RTO)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Mean time to failure (MTTF)**

*Intuition:* **Mean Time to Failure (MTTF)** calculates the average expected operating lifespan of non-repairable system components before a crash or failure occurs. (For repairable systems, Mean Time Between Failures—MTBF—is used; among given choices, MTTF measures duration prior to failure).
</details>

---

### 21. An IT security policy framework is like an outline that identifies where security controls should be used.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* An **IT Security Policy Framework** provides a structured architectural blueprint (like NIST CSF or ISO 27001) that maps risk management objectives to administrative, technical, and physical security controls across an organization's infrastructure layers.
</details>

---

### 22. True or False? Networks, routers, and equipment require continuous monitoring and management to keep wide area network (WAN) service available.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Because WAN connections cross public/distributed circuits, **continuous monitoring** (tracking throughput, packet loss, and edge router health) is vital to identify bottlenecks, maintain SLA compliance, and prevent extended service outages.
</details>

---

### 23. Chris is writing a document that provides step-by-step instructions for end users seeking to update the security software on their computers. Performing these updates is mandatory. Which type of document is Chris writing?
- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Procedure**

*Intuition:* A **Procedure** is a detailed, sequential "how-to" document that guides users through exact step-by-step actions necessary to perform a task (e.g., executing a software update) mandated by higher-level standards or policies.
</details>

---

### 24. In which domain of a typical IT infrastructure is the first layer of defense for a layered security strategy?
- A. User Domain
- B. Workstation Domain
- C. System/Application Domain
- D. Local Area Network (LAN) Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. User Domain**

*Intuition:* Human personnel constitute the outermost perimeter of enterprise security. Security awareness training, acceptable use policies, and strong authentication in the **User Domain** form the primary front-line defense against phishing, credential harvesting, and social engineering.
</details>

---

### 25. Authorization is the process of granting rights to use an organization's IT assets, systems, applications, and data to a specific user.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **Authorization** takes place after identity authentication; it determines the specific permissions, roles, and resource rights granted to an authenticated user based on the principle of least privilege.
</details>

---

### 26. Cryptography is the practice of making data unreadable.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **Cryptography** uses mathematical algorithms and encryption keys to transform readable plain text into unreadable ciphertext, preserving data confidentiality against unauthorized eavesdroppers and adversaries.
</details>

---

### 27. Encrypting data within databases and storage devices gives an added layer of security.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Database and disk encryption (**Encryption at Rest**) delivers essential defense-in-depth. If physical drives are stolen or perimeter defenses are breached, stored data remains unreadable without valid cryptographic keys.
</details>

---

### 28. The Local Area Network (LAN)-to-Wide Area Network (WAN) Domain is where the IT infrastructure links to a WAN and the Internet.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The **LAN-to-WAN Domain** forms the perimeter boundary hosting edge routers, firewalls, edge switches, and DMZs that manage, filter, and bridge local internal network traffic out to external WAN lines and the public internet.
</details>

---

### 29. True or False? For businesses and organizations under recent compliance laws, data classification standards typically include private, confidential, internal use only, and public-domain categories.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Regulatory frameworks require structured, multi-tiered data classification models (Private, Confidential, Internal Use Only, Public) to ensure organizations apply proportional encryption, access controls, and retention rules based on sensitivity.
</details>

---

### 30. Hypertext Transfer Protocol (HTTP) encrypts data transfers between secure browsers and secure webpages.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Standard **HTTP** operates entirely in plain text without any encryption capabilities. Cryptographic encryption of web traffic requires **HTTPS** (Hypertext Transfer Protocol Secure), which leverages TLS/SSL protocols to secure channel data.
</details>

---

#### Part B: Extended Sakai Question Pool (Questions 31–99)

### 31. Which tenet of the CIA triad ensures that only authorized individuals can view sensitive data?
- A. Availability
- B. Confidentiality
- C. Integrity
- D. Nonrepudiation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Confidentiality**

*Intuition:* Confidentiality restricts access and disclosure of information to authorized parties only.
</details>

---

### 32. Which tenet of the CIA triad ensures data has not been altered in an unauthorized way?
- A. Integrity
- B. Confidentiality
- C. Availability
- D. Authentication

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Integrity**

*Intuition:* Integrity protects data from unauthorized modification, ensuring it remains accurate and trustworthy.
</details>

---

### 33. Which tenet of the CIA triad ensures systems and data are accessible to authorized users when needed?
- A. Confidentiality
- B. Integrity
- C. Availability
- D. Accountability

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Availability**

*Intuition:* Availability ensures authorized users can access resources when required, tied to uptime and resilience.
</details>

---

### 34. A hacker intercepts and reads unencrypted emails containing customer data. Which tenet was violated?
- A. Availability
- B. Confidentiality
- C. Integrity
- D. Nonrepudiation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Confidentiality**

*Intuition:* Unauthorized viewing of data is a breach of confidentiality.
</details>

---

### 35. A DDoS attack takes an e-commerce site offline for six hours. Which tenet was primarily violated?
- A. Confidentiality
- B. Integrity
- C. Availability
- D. Authorization

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Availability**

*Intuition:* A DDoS attack disrupts access to a resource, directly violating availability.
</details>

---

### 36. Which process involves a user claiming an identity, typically with a username?
- A. Authentication
- B. Authorization
- C. Identification
- D. Accountability

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Identification**

*Intuition:* Identification is the act of asserting who you are, such as entering a username.
</details>

---

### 37. Which process verifies that a claimed identity is genuine?
- A. Authentication
- B. Identification
- C. Authorization
- D. Nonrepudiation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Authentication**

*Intuition:* Authentication proves an identity claim using a factor such as a password, token, or biometric.
</details>

---

### 38. Which process determines what an authenticated user is permitted to do?
- A. Identification
- B. Authentication
- C. Authorization
- D. Accountability

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Authorization**

*Intuition:* Authorization grants specific rights and permissions after identity has been verified.
</details>

---

### 39. Which concept ensures a user cannot deny having performed a specific action?
- A. Accountability
- B. Nonrepudiation
- C. Authorization
- D. Authentication

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Nonrepudiation**

*Intuition:* Nonrepudiation uses evidence such as digital signatures and logs to prevent denial of an action.
</details>

---

### 40. Which access control model assigns permissions based on job role within an organization?
- A. Discretionary Access Control (DAC)
- B. Mandatory Access Control (MAC)
- C. Role-Based Access Control (RBAC)
- D. Rule-Based Access Control

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Role-Based Access Control (RBAC)**

*Intuition:* RBAC assigns access rights based on a user's role, simplifying administration for groups with similar needs.
</details>

---

### 41. Which access control model allows the data owner to decide who can access their resources?
- A. Mandatory Access Control (MAC)
- B. Discretionary Access Control (DAC)
- C. Role-Based Access Control (RBAC)
- D. Attribute-Based Access Control (ABAC)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Discretionary Access Control (DAC)**

*Intuition:* In DAC, the resource owner has discretion over granting access to other users.
</details>

---

### 42. Which access control model relies on centrally managed security labels/classifications rather than owner discretion?
- A. Discretionary Access Control (DAC)
- B. Role-Based Access Control (RBAC)
- C. Mandatory Access Control (MAC)
- D. Rule-Based Access Control

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Mandatory Access Control (MAC)**

*Intuition:* MAC enforces access based on fixed classification levels set by a central authority, common in government/military systems.
</details>

---

### 43. Which domain of a typical IT infrastructure includes employees, contractors, and consultants?
- A. Workstation Domain
- B. User Domain
- C. LAN Domain
- D. System/Application Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. User Domain**

*Intuition:* The User Domain covers the people who access an organization's IT systems.
</details>

---

### 44. Which domain of a typical IT infrastructure includes desktops, laptops, and end-user devices?
- A. User Domain
- B. Workstation Domain
- C. LAN Domain
- D. Remote Access Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Workstation Domain**

*Intuition:* The Workstation Domain covers the devices employees use to connect to the network.
</details>

---

### 45. Which domain includes servers, operating systems, and business applications like ERP or database systems?
- A. Workstation Domain
- B. LAN Domain
- C. System/Application Domain
- D. WAN Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. System/Application Domain**

*Intuition:* The System/Application Domain covers the servers and software that process and store organizational data.
</details>

---

### 46. Which domain covers the risks associated with telecommuters and mobile users connecting from outside the office?
- A. LAN-to-WAN Domain
- B. Remote Access Domain
- C. WAN Domain
- D. User Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Remote Access Domain**

*Intuition:* The Remote Access Domain addresses risks tied to mobile/remote connectivity, such as lost laptops and brute-force attacks on VPNs.
</details>

---

### 47. Which domain typically includes long-distance connectivity provided by carriers and ISPs?
- A. LAN Domain
- B. LAN-to-WAN Domain
- C. WAN Domain
- D. Remote Access Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. WAN Domain**

*Intuition:* The WAN Domain covers wide area connectivity, often governed by service-level agreements with external providers.
</details>

---

### 48. Which domain is the boundary where an organization's internal network connects to the Internet?
- A. WAN Domain
- B. LAN Domain
- C. LAN-to-WAN Domain
- D. Remote Access Domain

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. LAN-to-WAN Domain**

*Intuition:* The LAN-to-WAN Domain is the perimeter where firewalls and routers manage traffic entering and leaving the internal network.
</details>

---

### 49. Which element of the security policy framework specifies mandatory, specific technical requirements?
- A. Standard
- B. Guideline
- C. Policy
- D. Baseline

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Standard**

*Intuition:* Standards define mandatory, specific parameters (e.g., minimum password length) that support a policy.
</details>

---

### 50. Which element of the security policy framework provides optional, recommended advice?
- A. Procedure
- B. Standard
- C. Guideline
- D. Policy

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Guideline**

*Intuition:* Guidelines are non-mandatory suggestions for best practice.
</details>

---

### 51. Which element of the security policy framework gives detailed, step-by-step instructions for completing a task?
- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Procedure**

*Intuition:* Procedures provide granular, sequential steps for performing a specific task consistently.
</details>

---

### 52. A minimum acceptable level of security that all systems must meet is best described as a:
- A. Guideline
- B. Baseline
- C. Policy
- D. Threat model

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Baseline**

*Intuition:* A baseline defines the minimum security configuration required across systems of a given type.
</details>

---

### 53. Which term describes the likelihood that a threat will exploit a vulnerability to cause harm to an asset?
- A. Threat
- B. Vulnerability
- C. Risk
- D. Countermeasure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Risk**

*Intuition:* Risk represents the exposure/likelihood of harm, combining threats and vulnerabilities.
</details>

---

### 54. Which term describes a weakness in a system that could be exploited?
- A. Vulnerability
- B. Threat
- C. Risk
- D. Exposure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Vulnerability**

*Intuition:* A vulnerability is a gap or flaw that a threat could exploit.
</details>

---

### 55. Which term describes any circumstance or event with the potential to cause harm to an asset?
- A. Vulnerability
- B. Threat
- C. Countermeasure
- D. Risk

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Threat**

*Intuition:* A threat is a potential danger, such as an attacker, malware, or natural disaster.
</details>

---

### 56. Which term describes a control implemented to reduce risk to an asset?
- A. Vulnerability
- B. Threat
- C. Countermeasure
- D. Exposure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Countermeasure**

*Intuition:* A countermeasure (or safeguard/control) is a mechanism, like a firewall or encryption, that reduces risk.
</details>

---

### 57. Accepting a risk because the cost of mitigation exceeds the potential loss is an example of which risk response strategy?
- A. Risk avoidance
- B. Risk transfer
- C. Risk acceptance
- D. Risk mitigation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Risk acceptance**

*Intuition:* Risk acceptance means acknowledging a risk and choosing not to implement additional controls, often when cost outweighs benefit.
</details>

---

### 58. Purchasing cyber insurance to cover the financial impact of a breach is an example of which risk response strategy?
- A. Risk avoidance
- B. Risk transfer
- C. Risk mitigation
- D. Risk acceptance

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Risk transfer**

*Intuition:* Risk transfer shifts the financial impact of a risk to a third party, such as an insurer.
</details>

---

### 59. Which U.S. law requires financial institutions to protect customers' private financial information?
- A. Sarbanes-Oxley Act (SOX)
- B. Gramm-Leach-Bliley Act (GLBA)
- C. HIPAA
- D. FISMA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Gramm-Leach-Bliley Act (GLBA)**

*Intuition:* GLBA specifically governs how financial institutions handle and protect customer financial data.
</details>

---

### 60. Which U.S. law focuses on the accuracy of corporate financial disclosures for publicly traded companies?
- A. GLBA
- B. HIPAA
- C. Sarbanes-Oxley Act (SOX)
- D. CIPA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Sarbanes-Oxley Act (SOX)**

*Intuition:* SOX was enacted to improve the reliability of corporate financial reporting after accounting scandals.
</details>

---

### 61. Which U.S. law protects the privacy of patient health information?
- A. HIPAA
- B. GLBA
- C. SOX
- D. FERPA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. HIPAA**

*Intuition:* HIPAA governs the protection of protected health information (PHI) by healthcare entities and their business associates.
</details>

---

### 62. Which U.S. law requires schools and libraries receiving federal E-Rate funding to filter harmful internet content?
- A. FISMA
- B. CIPA
- C. GLBA
- D. HIPAA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. CIPA**

*Intuition:* CIPA requires internet filtering in schools/libraries as a condition of certain federal funding.
</details>

---

### 63. Which U.S. law requires federal agencies to develop and implement information security programs?
- A. FISMA
- B. SOX
- C. GLBA
- D. CIPA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. FISMA**

*Intuition:* FISMA applies to federal agencies and their contractors, mandating formal information security programs.
</details>

---

### 64. Which industry standard governs organizations that store, process, or transmit credit card data?
- A. HIPAA
- B. PCI DSS
- C. GLBA
- D. SOX

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. PCI DSS**

*Intuition:* The Payment Card Industry Data Security Standard (PCI DSS) sets security requirements for handling cardholder data.
</details>

---

### 65. Which U.S. law protects the privacy of student education records?
- A. FERPA
- B. CIPA
- C. HIPAA
- D. GLBA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. FERPA**

*Intuition:* The Family Educational Rights and Privacy Act (FERPA) protects the privacy of student records.
</details>

---

### 66. Which port is commonly used by SSH for secure, encrypted remote access?
- A. 20
- B. 22
- C. 23
- D. 80

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 22**

*Intuition:* SSH uses port 22 and encrypts all traffic, including login credentials.
</details>

---

### 67. Which port is commonly used by unencrypted Telnet connections?
- A. 21
- B. 22
- C. 23
- D. 443

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. 23**

*Intuition:* Telnet uses port 23 and transmits all data, including credentials, in plaintext.
</details>

---

### 68. Which port is used by HTTPS for encrypted web traffic?
- A. 80
- B. 443
- C. 8080
- D. 21

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 443**

*Intuition:* HTTPS uses port 443 and encrypts traffic using TLS/SSL.
</details>

---

### 69. Which port is used by unencrypted HTTP web traffic?
- A. 443
- B. 80
- C. 22
- D. 25

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 80**

*Intuition:* HTTP uses port 80 and transmits data in cleartext.
</details>

---

### 70. Which protocol is used to send email between mail servers?
- A. POP3
- B. IMAP
- C. SMTP
- D. FTP

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. SMTP**

*Intuition:* SMTP (Simple Mail Transfer Protocol) is used to route and send email between servers.
</details>

---

### 71. Which protocol translates domain names into IP addresses?
- A. DHCP
- B. DNS
- C. ARP
- D. SNMP

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. DNS**

*Intuition:* DNS (Domain Name System) resolves human-readable domain names to IP addresses.
</details>

---

### 72. Which protocol automatically assigns IP addresses to devices on a network?
- A. DNS
- B. DHCP
- C. SNMP
- D. NTP

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. DHCP**

*Intuition:* DHCP (Dynamic Host Configuration Protocol) automatically assigns IP addressing information to devices.
</details>

---

### 73. Which network device forwards packets between different networks based on IP addresses?
- A. Switch
- B. Router
- C. Hub
- D. Firewall

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Router**

*Intuition:* A router's core function is to forward traffic between networks based on routing tables, not to serve as a dedicated security appliance.
</details>

---

### 74. Which network device is specifically designed to filter and block traffic based on security rules?
- A. Switch
- B. Hub
- C. Firewall
- D. Repeater

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Firewall**

*Intuition:* A firewall's defining purpose is to enforce security policy by filtering and blocking unwanted traffic.
</details>

---

### 75. Which device passively monitors traffic and alerts administrators to suspicious activity without blocking it?
- A. IPS
- B. IDS
- C. Router
- D. Proxy server

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. IDS**

*Intuition:* An Intrusion Detection System (IDS) detects and alerts but does not actively block traffic.
</details>

---

### 76. Which device actively blocks malicious traffic in real time as it flows through the network?
- A. IDS
- B. IPS
- C. Hub
- D. Web server

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. IPS**

*Intuition:* An Intrusion Prevention System (IPS) sits in-line and actively blocks identified malicious traffic.
</details>

---

### 77. Which device acts as an intermediary, forwarding client requests to servers and can cache content or hide internal IPs?
- A. Proxy server
- B. Switch
- C. Repeater
- D. IDS

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Proxy server**

*Intuition:* A proxy server relays requests between clients and servers, often for caching, filtering, or anonymity.
</details>

---

### 78. Which device connects multiple devices within a LAN and forwards traffic based on MAC addresses?
- A. Router
- B. Switch
- C. Gateway
- D. Firewall

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Switch**

*Intuition:* A switch operates at Layer 2, forwarding frames based on MAC addresses within a local network.
</details>

---

### 79. Which security control creates an encrypted tunnel to protect data traveling across a WAN?
- A. Firewall
- B. VPN
- C. IDS
- D. Proxy server

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. VPN**

*Intuition:* A VPN (Virtual Private Network) encrypts traffic in transit, protecting against eavesdropping on WAN links.
</details>

---

### 80. Which type of encryption uses the same key for both encryption and decryption?
- A. Asymmetric encryption
- B. Symmetric encryption
- C. Hashing
- D. Steganography

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Symmetric encryption**

*Intuition:* Symmetric encryption uses a single shared secret key for both encrypting and decrypting data.
</details>

---

### 81. Which type of encryption uses a public key and a private key pair?
- A. Symmetric encryption
- B. Asymmetric encryption
- C. Hashing
- D. Obfuscation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Asymmetric encryption**

*Intuition:* Asymmetric encryption uses a mathematically linked public/private key pair, commonly used in PKI.
</details>

---

### 82. Which cryptographic technique produces a fixed-length output used to verify data integrity, and is not meant to be reversed?
- A. Symmetric encryption
- B. Asymmetric encryption
- C. Hashing
- D. Tokenization

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Hashing**

*Intuition:* Hashing produces a fixed-size digest used to detect changes to data; it is a one-way function.
</details>

---

### 83. Which term describes protecting stored data on hard drives and databases through encryption?
- A. Encryption in transit
- B. Encryption at rest
- C. Tokenization
- D. Data masking

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Encryption at rest**

*Intuition:* Encryption at rest protects stored data, adding a layer of protection even if storage media is stolen.
</details>

---

### 84. Which term describes protecting data as it moves across a network?
- A. Encryption at rest
- B. Encryption in transit
- C. Data masking
- D. Hashing only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Encryption in transit**

*Intuition:* Encryption in transit (e.g., TLS, VPN) protects data while it travels between systems.
</details>

---

### 85. Which infrastructure manages digital certificates and public/private key pairs to support secure communication?
- A. PKI
- B. DNS
- C. VLAN
- D. ACL

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. PKI**

*Intuition:* Public Key Infrastructure (PKI) manages the creation, distribution, and revocation of digital certificates and keys.
</details>

---

### 86. A digital signature primarily provides which security benefits?
- A. Confidentiality only
- B. Availability only
- C. Integrity and nonrepudiation
- D. Anonymity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Integrity and nonrepudiation**

*Intuition:* Digital signatures verify that a message wasn't altered and confirm the sender's identity, supporting nonrepudiation.
</details>

---

### 87. Which U.S. federal classification level applies to information that would cause exceptionally grave damage if disclosed?
- A. Confidential
- B. Secret
- C. Top Secret
- D. Private

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Top Secret**

*Intuition:* Top Secret is the highest classification, reserved for the most sensitive national security information.
</details>

---

### 88. Which U.S. federal classification level applies to information that would cause damage, but not serious or grave damage, if disclosed?
- A. Top Secret
- B. Secret
- C. Confidential
- D. Unclassified

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Confidential**

*Intuition:* Confidential is the lowest of the three formal classification tiers, for information causing general damage.
</details>

---

### 89. Malicious software that replicates itself and spreads across networks without requiring a host file is called a:
- A. Virus
- B. Worm
- C. Trojan horse
- D. Rootkit

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Worm**

*Intuition:* A worm self-replicates and spreads independently across networks, unlike a virus which needs a host file.
</details>

---

### 90. Malicious software disguised as legitimate software to trick users into installing it is called a:
- A. Worm
- B. Trojan horse
- C. Virus
- D. Logic bomb

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Trojan horse**

*Intuition:* A Trojan horse masquerades as legitimate software to deceive users into executing it.
</details>

---

### 91. Malicious software that encrypts a victim's files and demands payment for the decryption key is called:
- A. Spyware
- B. Ransomware
- C. Adware
- D. A worm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Ransomware**

*Intuition:* Ransomware encrypts victim data and extorts payment in exchange for restoring access.
</details>

---

### 92. Software that covertly monitors user activity and collects information without consent is called:
- A. Spyware
- B. Ransomware
- C. A worm
- D. A logic bomb

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Spyware**

*Intuition:* Spyware secretly gathers information about a user's activity, often for advertising or data theft.
</details>

---

### 93. Malicious code hidden at the operating system's kernel level to maintain hidden, privileged access is called a:
- A. Worm
- B. Trojan horse
- C. Rootkit
- D. Adware

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Rootkit**

*Intuition:* A rootkit embeds itself deep in the OS to hide its presence and maintain privileged access.
</details>

---

### 94. An email pretending to be from a trusted source to trick recipients into revealing sensitive information is called:
- A. Phishing
- B. Pharming
- C. Spoofing
- D. Tailgating

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Phishing**

*Intuition:* Phishing uses deceptive emails/messages impersonating trusted entities to steal credentials or data.
</details>

---

### 95. An attacker follows an authorized employee through a secure door without using their own credentials. This is an example of:
- A. Phishing
- B. Tailgating
- C. Pharming
- D. Vishing

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Tailgating**

*Intuition:* Tailgating (piggybacking) is a physical social engineering technique of following someone through a secured entry point.
</details>

---

### 96. A phone-based social engineering attack designed to trick victims into revealing sensitive information is called:
- A. Vishing
- B. Phishing
- C. Smishing
- D. Pharming

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Vishing**

*Intuition:* Vishing (voice phishing) uses phone calls to manipulate victims into disclosing sensitive data.
</details>

---

### 97. A social engineering attack conducted via SMS text messages is called:
- A. Vishing
- B. Pharming
- C. Smishing
- D. Spoofing

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Smishing**

*Intuition:* Smishing is phishing carried out through SMS/text messages.
</details>

---

### 98. Which plan focuses on restoring critical business functions after a disruptive event?
- A. Business Continuity Plan (BCP)
- B. Acceptable Use Policy (AUP)
- C. Change management plan
- D. Data classification policy

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Business Continuity Plan (BCP)**

*Intuition:* A BCP outlines how an organization continues critical operations during and after a disruption.
</details>

---

### 99. Which plan focuses specifically on restoring IT systems and data after a disaster?
- A. Disaster Recovery Plan (DRP)
- B. Acceptable Use Policy
- C. Incident response policy
- D. Security awareness plan

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Disaster Recovery Plan (DRP)**

*Intuition:* A DRP details the technical steps to recover IT infrastructure and data following a disaster.
</details>

---


---

---

## Quiz 2: Internet of Things (IoT), Mobile IP, BYOD & Emerging Technologies

#### Part A: Core Exam Takes (Questions 1–33)

### 1. Smart cities can monitor and report on real-time traffic conditions using Internet of Things (IoT) technology.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Smart city infrastructure relies on network-connected IoT devices, such as traffic camera sensors, embedded road sensors, and smart signals, to aggregate and analyze real-time traffic density, optimize signal timing, and broadcast live transit updates.
</details>

---

### 2. The ownership of Internet of Things (IoT) data, as well as the metadata of that data, is sometimes in question.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* IoT data ownership is frequently contested because multiple parties are involved in the lifecycle of a single device. The consumer, device manufacturer, cloud platform provider, and third-party data brokers often have conflicting legal claims (outlined in complex Terms of Service agreements) over who actually owns raw sensor telemetry and generated metadata.
</details>

---

### 3. What term describes data that has been stripped of personally identifiable information for privacy reasons?
- A. Encrypted
- B. Proprietary
- C. De-identified
- D. Compliant

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. De-identified**

*Intuition:* **De-identification** is the process of removing or masking direct and indirect personally identifiable information (PII) from a dataset so that the remaining data cannot be linked back to a specific individual. Encryption transforms data into ciphertext using a key (where PII remains embedded once decrypted), proprietary refers to owned IP, and compliance denotes adherence to laws.
</details>

---

### 4. Metadata of Internet of Things (IoT) devices is sometimes sold to companies seeking demographic marketing data about users and their spending habits.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* IoT metadata (such as device usage patterns, operational times, and location logs) is frequently aggregated, packaged, and monetized by device manufacturers and third-party data brokers. Marketers purchase this data to infer user behaviors, lifestyle preferences, and spending habits to build targeted demographic profiles.
</details>

---

### 5. Utility companies are incorporating Internet-connected sensors into their business functions.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Utility companies rely heavily on Internet-connected sensors (smart grid infrastructure, connected water meters, and remote pipeline monitors) to track energy consumption in real time, detect leaks or power outages automatically, and dynamically balance utility supply and demand.
</details>

---

### 6. Which of the following is not a market driver for the Internet of Things (IoT)?
- A. Global adoption of Internet Protocol (IP) networking
- B. Smaller and faster computing
- C. A decline in cloud computing
- D. Advancements in data analytics

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A decline in cloud computing**

*Intuition:* The IoT market relies heavily on the expansion and growth of cloud computing, not its decline. Cloud infrastructure provides the elastic storage, processing power, and scalable backends required to manage and analyze massive telemetry streams from billions of IoT endpoints.
</details>

---

### 7. Which action is the best step toward protecting Internet of Things (IoT) devices from becoming the entry point for security vulnerabilities into a network while still meeting business requirements?
- A. Applying security updates promptly
- B. Using encryption for communications
- C. Removing IoT devices from the network
- D. Turning IoT devices off when not in use

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Applying security updates promptly**

*Intuition:* Promptly patching IoT firmware remediates known vulnerabilities before attackers can exploit them as entry vectors into the internal network, securing devices while maintaining operational business utility. Removing or powering off devices eliminates business functionality.
</details>

---

### 8. True or False? A challenge created by the Internet of Things (IoT) is how to protect personal identity and private data from theft or unauthorized access.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* IoT devices continuously harvest sensitive user data and personal telemetry. Because many consumer IoT endpoints lack strong built-in security controls, hardcoded/default credentials, or routine software updates, they introduce widespread vulnerabilities for identity theft and unauthorized data exfiltration.
</details>

---

### 9. Facility automation uses Internet of Things (IoT) to integrate automation into business functions to reduce reliance on machinery.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Facility automation leverages IoT to control, monitor, and optimize physical machinery and building systems (HVAC, lighting, physical security)—it reduces reliance on **manual human labor**, not machinery itself.
</details>

---

### 10. What is key to implementing a consistent Internet of Things (IoT) device, connectivity, and communications environment?
- A. Interoperability and standards
- B. Privacy laws
- C. Proprietary solutions
- D. Broadband capacity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Interoperability and standards**

*Intuition:* IoT environments encompass highly heterogeneous hardware, chipsets, and network protocols. Open standards and interoperability frameworks ensure that disparate devices, platforms, and communication layers can seamlessly exchange data and operate consistently.
</details>

---

### 11. Application service providers (ASPs) are software companies that build applications hosted in the cloud and on the Internet.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Application Service Providers (ASPs) host, manage, and deliver software applications to customers remotely over the Internet from centralized servers—serving as the direct foundational predecessor to modern Software-as-a-Service (SaaS) cloud models.
</details>

---

### 12. Which organization pursues standards for Internet of Things (IoT) devices and is widely recognized as the authority for creating standards on the Internet?
- A. Internet Society
- B. Internet Engineering Task Force (IETF)
- C. Internet Association
- D. Internet Authority

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Internet Engineering Task Force (IETF)**

*Intuition:* The **IETF** is the premier open standards organization responsible for defining and maintaining core Internet and IoT networking protocols (such as IPv6, CoAP, and 6LoWPAN).
</details>

---

### 13. Which of the following is not an example of store-and-forward messaging?
- A. Telephone call
- B. Voicemail
- C. Unified messaging (UM)
- D. Email

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Telephone call**

*Intuition:* A traditional telephone call is a real-time, **synchronous** communication channel requiring both parties to interact simultaneously. Store-and-forward messaging (like email or voicemail) is **asynchronous**, saving messages on intermediate servers for deferred retrieval.
</details>

---

### 14. True or False? Internet of Things (IoT) upgrades can be difficult to distribute and deploy, leaving gaps in the remediation of IoT devices or endpoints.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Constrained processing power, minimal flash memory, lack of automated OTA update agents, and short vendor support lifecycles make distributing and installing security patches to IoT endpoints notoriously difficult, leading to persistent unpatched vulnerabilities across networks.
</details>

---

### 15. With the use of Mobile IP, which device is responsible for keeping track of mobile nodes (MNs) and forwarding packets to the MN's current network?
- A. Home agent (HA)
- B. Foreign agent (FA)
- C. Care of address (COA)
- D. Correspondent node (CN)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Home agent (HA)**

*Intuition:* In Mobile IP architecture, the **Home Agent (HA)** resides on the Mobile Node's home network, maintaining its binding directory (mapping permanent IP to current Care-of Address) and tunneling incoming packets to the node's current location.
</details>

---

### 16. True or False? Bring Your Own Device (BYOD) often replaces the need for the organization to procure limited mobile device model options and issue them to employees for individual use.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* BYOD enables employees to select and purchase their preferred personal hardware for workplace tasks. This eliminates enterprise procurement expenses and avoids maintaining restrictive, standardized corporate hardware fleets.
</details>

---

### 17. Store-and-forward communications should be used when you need to talk to someone immediately.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Store-and-forward protocols are **asynchronous** and introduce inherent storage latency. Real-time (synchronous) channels—such as voice calls, video streams, or active instant messaging—are required for immediate interactive communication.
</details>

---

### 18. In Mobile IP, what term describes a device that would like to communicate with a mobile node (MN)?
- A. Home agent (HA)
- B. Foreign agent (FA)
- C. Care of address (COA)
- D. Correspondent node (CN)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Correspondent node (CN)**

*Intuition:* The **Correspondent Node (CN)** represents any peer entity (host, server, or client) on an IP network initiating or maintaining data communication sessions with a roaming Mobile Node (MN).
</details>

---

### 19. Which of the following is an example of a business-to-consumer (B2C) application of the Internet of Things (IoT)?
- A. Video conferencing
- B. Infrastructure monitoring
- C. Health monitoring
- D. Traffic monitoring

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Health monitoring**

*Intuition:* Consumer wearable devices (such as smartwatches, continuous glucose monitors, and fitness trackers) directly serve individual end-users (B2C) by gathering personal biometric telemetry. Infrastructure and traffic monitoring represent B2B or B2G applications.
</details>

---

### 20. Posting a comment on social media is an example of real-time communication.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Social media comments are **asynchronous**. Content is saved on platform servers, allowing recipients to view and respond at a later time without requiring concurrent active presence.
</details>

---

### 21. Vendors or service providers that have remote access to an Internet of Things (IoT) device may be able to pull information or data from your device without your permission.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Through embedded telemetry software, cloud diagnostic channels, or broad Terms of Service (ToS) agreements, vendors frequently maintain remote access capabilities to exfiltrate operational logs and telemetry without real-time user notification.
</details>

---

### 22. Ron is the IT director at a medium-sized company. He frequently gets requests from employees who want to select customized mobile devices. He decides to allow them to purchase their own devices. Which type of policy should Ron implement to include the requirements and security controls for this arrangement?
- A. Privacy
- B. Bring Your Own Device (BYOD)
- C. Acceptable use
- D. Data classification

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Bring Your Own Device (BYOD)**

*Intuition:* A **BYOD Policy** establishes rules, mandatory security baselines, remote-wipe boundaries, and containerization requirements for personally owned hardware used to access corporate network resources.
</details>

---

### 23. Each 5G device has a unique Internet Protocol (IP) address and appears just like any other wired device on a network.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* 5G architecture leverages native all-IP networking (primarily IPv6). Every 5G endpoint receives a unique IP address, presenting itself to routers and firewalls as a standard addressable node.
</details>

---

### 24. Which of the following would govern the use of Internet of Things (IoT) by health care providers, such as physicians and hospitals?
- A. Payment Card Industry Data Security Standard (PCI DSS)
- B. Federal Financial Institutions Examination Council (FFIEC)
- C. Federal Information Security Management Act (FISMA)
- D. Health Insurance Portability and Accountability Act (HIPAA)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Health Insurance Portability and Accountability Act (HIPAA)**

*Intuition:* **HIPAA** mandates privacy and security controls for Protected Health Information (PHI). IoT medical devices (e.g., smart monitors, infusion pumps) deployed by healthcare providers harvest PHI and fall strictly under HIPAA compliance obligations.
</details>

---

### 25. Bring Your Own Device (BYOD) opens the door to considerable security issues.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* BYOD introduces substantial security risks because employee personal devices operate outside full enterprise IT management. Unpatched OS versions, unauthorized app installations, malware infections, and lost/stolen hardware expose corporate data to compromise.
</details>

---

### 26. From a security perspective, what should organizations expect will occur as they become more dependent on the Internet of Things (IoT)?
- A. Security risks will increase.
- B. Security risks will decrease.
- C. Security risks will stay the same.
- D. Security risks will be eliminated.

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Security risks will increase.**

*Intuition:* Rapid IoT adoption significantly inflates an organization's attack surface. Adding vast numbers of IP-enabled endpoints—many possessing minimal built-in defenses or patch capabilities—exponentially increases cyber exposure.
</details>

---

### 27. Vehicles that have Wi-Fi access and onboard computers require software patches and upgrades from the manufacturer.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Connected modern vehicles rely on software-driven Electronic Control Units (ECUs) and Wi-Fi/cellular gateways. Firmware updates and software patches delivered over-the-air (OTA) or at service centers are critical to remediate vulnerabilities and maintain operational safety.
</details>

---

### 28. Which of the following enables businesses to transform themselves into an Internet of Things (IoT) service offering?
- A. Anything as a Service (AaaS) delivery model
- B. Remote sensoring
- C. Real-time tracking and monitoring
- D. Store-and-forward communications

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Anything as a Service (AaaS) delivery model**

*Intuition:* The **Anything as a Service (AaaS / XaaS)** business delivery model allows physical product manufacturers to convert one-off hardware sales into continuous subscription services combining connected hardware telemetry, cloud analytics, and managed support.
</details>

---

### 29. Which term best describes how a wide variety of objects, devices, sensors, and everyday items can connect and be accessed?
- A. Radio frequency identification (RFID)
- B. Software as a Service (SaaS)
- C. Internet of Things (IoT)
- D. Unified messaging (UM)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Internet of Things (IoT)**

*Intuition:* The **Internet of Things (IoT)** defines the overarching framework of physical devices, sensors, appliances, and items embedded with network connectivity, software, and electronics that allow them to collect, exchange, and process data over the Internet.
</details>

---

### 30. In e-business, secure web applications are one of the critical security controls that each organization must implement to reduce risk.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Secure web applications serve as the public front-end facing customer transactions and internal database backends in e-business. Implementing application security controls (guarding against SQLi, XSS, and broken access controls) is vital to mitigate data breach risks.
</details>

---

### 31. Using Mobile IP, users can move between segments on a local area network (LAN) and stay connected without interruption.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **Mobile IP** allows a roaming mobile node (MN) to transparently transition across different local network segments or subnets without changing its home IP address, preserving active TCP sessions and continuous network connectivity.
</details>

---

### 32. Kaira's company recently switched to a new calendaring system provided by a vendor. Kaira and other users connect to the system, hosted at the vendor's site, using a web browser. Which service delivery model is Kaira's company using?
- A. Platform as a Service (PaaS)
- B. Software as a Service (SaaS)
- C. Communications as a Service (CaaS)
- D. Infrastructure as a Service (IaaS)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Software as a Service (SaaS)**

*Intuition:* Under **Software as a Service (SaaS)**, fully functional applications (such as calendaring or email systems) are hosted and managed by a third-party vendor in the cloud and accessed by end-users via web browsers without requiring software installation or server maintenance.
</details>

---

### 33. With the use of Mobile IP, which device is responsible for assigning each mobile node (MN) a local address?
- A. Home agent (HA)
- B. Foreign agent (FA)
- C. Care of address (COA)
- D. Correspondent node (CN)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Foreign agent (FA)**

*Intuition:* When a Mobile Node roams into a visited network, the **Foreign Agent (FA)** registers the node and assigns it a local **Care-of Address (COA)** to receive tunneled traffic forwarded by its Home Agent (HA).
</details>

---

#### Part B: Extended Sakai Question Pool (Questions 34–35)

### 34. E-commerce systems and applications demand strict confidentiality, integrity, and availability (C-I-A) security controls.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Confidentiality, integrity, and availability are all essential given the sensitive financial data e-commerce systems handle.
</details>

---

### 35. Which term best describes the sale of goods and services on the Internet, whereby online customers buy those goods and services from a vendor's website and enter private data and checking account or credit card information to pay for them?
- A. Software as a Service (SaaS)
- B. E-commerce
- C. Internet of Things (IoT)
- D. Economic development

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. E-commerce**

*Intuition:* E-commerce refers to buying and selling goods and services online, including entering payment and personal data to complete transactions.
</details>

---


---

---

## Quiz 3: Comprehensive Question Bank & Review (All Test Takes & Eugene's Chat Export)

#### Part A: Core Exam Takes (Questions 1–68)

### 1. Data localization differs from data sovereignty because:
- A. They are identical concepts
- B. Neither protects data
- C. Localization = storage location
- D. Sovereignty = legal control

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Sovereignty = legal control** *(Note: C and D both reflect core distinctions; C defines physical location while D defines legal jurisdiction).*

*Intuition:* **Data Localization** mandates *where* data physically resides (physical servers within national geographic borders). **Data Sovereignty** dictates *which laws govern* the data (legal jurisdiction and governance laws of the country where data is collected or stored).
</details>

---

### 2. A PIA is generally:
- A. Only for governments
- B. Always required by law
- C. A best practice
- D. A criminal offense

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A best practice**

*Intuition:* A Privacy Impact Assessment (PIA) is a foundational risk management process used by both public and private entities to evaluate and mitigate privacy risks. While statutory DPIAs under laws like GDPR, NDPA, or Ghana's Act 843 are mandatory for high-risk processing, general PIAs serve as an overall organizational best practice.
</details>

---

### 3. The Privacy by Design lifecycle emphasizes:
- A. Privacy at the end
- B. Ignore privacy until issues
- C. Privacy as an afterthought
- D. Continuous privacy protection

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Continuous privacy protection**

*Intuition:* Privacy by Design (PbD) requires embedding privacy proactively into system architecture, business practices, and software development throughout the entire lifecycle—from initial engineering to final disposal—rather than attempting retroactive fixes.
</details>

---

### 4. Data collection includes:
- A. Delete all sources
- B. Existing data only
- C. Gather new data
- D. Never collect data

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Gather new data**

*Intuition:* Data collection is the systematic process of capturing, generating, and acquiring new information inputs from targeted sources via forms, sensors, user inputs, or system telemetry.
</details>

---

### 5. The digital economy benefit of data localization is:
- A. Reducing cross-border trade
- B. Strengthening AfCFTA's digital protocol
- C. Eliminating fintech services
- D. Lowering internet usage

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Strengthening AfCFTA's digital protocol**

*Intuition:* Balanced data localization policies integrated into frameworks like the African Continental Free Trade Area (AfCFTA) Digital Trade Protocol build local digital infrastructure, retain digital value creation, and establish trusted regional data governance for continental e-commerce.
</details>

---

### 6. Strict localization rules across Africa can:
- A. Remove competition
- B. Create one digital market
- C. Split Africa's digital market
- D. Reduce compliance costs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Split Africa's digital market**

*Intuition:* Enforcing rigid, conflicting data localization laws across 50+ individual African nations creates regulatory fragmentation ("walled gardens"), preventing seamless cross-border data flows and splitting the digital economy into isolated markets.
</details>

---

### 7. Which TWO are requirements for a DPIA under African data protection laws?
- A. Required for high-risk processing
- B. Only for non-profit organizations
- C. Completely voluntary
- D. Identify and reduce privacy risks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Required for high-risk processing** and **D. Identify and reduce privacy risks**

*Intuition:* Statutory data protection frameworks across Africa (such as Ghana's Act 843, Nigeria's NDPA, and South Africa's POPIA) mandate a DPIA when processing activities pose high risks to data subjects. The core operational goal of the assessment is systematically identifying, evaluating, and mitigating those privacy risks before processing begins.
</details>

---

### 8. DPIA is mandatory under which laws?
- A. Only US laws
- B. Only European laws
- C. Ghana's Act 843, NDPA & POPIA
- D. No African law

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Ghana's Act 843, NDPA & POPIA**

*Intuition:* African privacy frameworks explicitly mandate DPIAs or mandatory risk assessments for high-risk data processing operations. Key statutory frameworks include Ghana's Data Protection Act (Act 843), Nigeria's Data Protection Act (NDPA), and South Africa's POPIA.
</details>

---

### 9. The first step in breach response is:
- A. Notify everyone immediately
- B. Delete affected data
- C. Ignore the incident
- D. Detect and record the breach

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Detect and record the breach**

*Intuition:* Before containment, risk evaluation, or regulatory reporting can occur, an incident response team must first identify that a security incident has occurred and record the initial forensic details.
</details>

---

### 10. Which TWO are security measures for records?
- A. Leave records unprotected
- B. Backup plans
- C. No continuity planning
- D. Physical security

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Backup plans** and **D. Physical security**

*Intuition:* **Backup plans** safeguard record availability and integrity against ransomware, hardware failures, or disasters. **Physical security** (biometric locks, guards, surveillance) protects physical and digital storage media from unauthorized access.
</details>

---

### 11. A DPIA must be conducted:
- A. Every ten years
- B. Before deployment
- C. After a data breach
- D. Only if requested

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Before deployment**

*Intuition:* A DPIA is a proactive preventative control. It must be conducted during the design and architecture phase—**before deployment**—so that privacy vulnerabilities can be resolved prior to live data processing.
</details>

---

### 12. Privacy by Design applies to:
- A. Launch only
- B. Maintenance only
- C. Testing only
- D. Every stage

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Every stage**

*Intuition:* Privacy by Design is end-to-end; it requires embedding privacy principles into every phase of the system engineering lifecycle, from concept and development to deployment, operational maintenance, and data destruction.
</details>

---

### 13. Data sovereignty refers to:
- A. Encrypting all personal data
- B. Deleting all foreign data
- C. Subject to laws where data is collected
- D. Storing data anywhere in the world

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Subject to laws where data is collected**

*Intuition:* Data sovereignty establishes that digital data is legally bound to the governance statutes, judicial oversight, and data protection regulations of the country in which it is collected, generated, or processed.
</details>

---

### 14. The data lifecycle refers to:
- A. Collection only
- B. Data from planning to use
- C. Analysis only
- D. Deletion only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Data from planning to use**

*Intuition:* The data lifecycle spans the full operational existence of a data asset—including planning, creation/collection, storage, processing, sharing, archiving, and final destruction.
</details>

---

### 15. Many African countries lack:
- A. Internet access completely
- B. Interest in technology
- C. Skilled data-hosting professionals
- D. Basic electricity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Skilled data-hosting professionals**

*Intuition:* A key operational challenge in executing strict data localization mandates across Africa is the shortage of specialized domestic technical talent required to engineer, secure, and maintain enterprise cloud data center infrastructure.
</details>

---

### 16. Data localization drives investment in:
- A. Offshore storage
- B. Local data centers
- C. Manual record keeping
- D. Foreign data centers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Local data centers**

*Intuition:* Legal requirements mandating that data reside within national borders compel cloud providers and domestic enterprises to invest capital into building local data center facilities, servers, and power systems.
</details>

---

### 17. Which TWO statements best define data sovereignty?
- A. Data follows the country's laws
- B. Jurisdiction follows the data
- C. Data must stay in the cloud
- D. Data cannot cross borders

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Data follows the country's laws** and **B. Jurisdiction follows the data**

*Intuition:* Data sovereignty asserts that data is subject to the legal rights and statutory authority of the nation where it is collected (**A**), and legal jurisdiction remains attached to that data regardless of technical transfer (**B**).
</details>

---

### 18. Which TWO are essential parts of a DPIA template?
- A. Marketing analysis
- B. Financial projections
- C. Processing scope and necessity
- D. Risks and mitigation measures

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Processing scope and necessity** and **D. Risks and mitigation measures**

*Intuition:* Standard DPIA templates require documenting the exact nature, scope, context, and necessity of data processing (**C**), along with a rigorous analysis of privacy threats and proposed technical/administrative mitigations (**D**).
</details>

---

### 19. Data localization means:
- A. Converting data into local currency
- B. Translating data into local languages
- C. Sharing data with neighboring countries
- D. Keeping data within national borders

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Keeping data within national borders**

*Intuition:* Data localization explicitly mandates that digital data (or a required local copy) must be stored and processed on physical server infrastructure situated within national geographic boundaries.
</details>

---

### 20. A DPIA should be reviewed:
- A. When processing changes or regularly
- B. Only once
- C. Every ten years
- D. Never again

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. When processing changes or regularly**

*Intuition:* A DPIA is a living document. It must be reassessed periodically and whenever significant modifications occur in processing activities, technologies, system architecture, or threat landscapes.
</details>

---

### 21. Which TWO challenges are unique to Africa's digital sovereignty?
- A. Uniform regulations
- B. Different national rules
- C. Plenty of infrastructure
- D. Limited technical capacity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Different national rules** and **D. Limited technical capacity**

*Intuition:* African nations face digital sovereignty bottlenecks due to legal fragmentation across 50+ differing national privacy statutes (**B**) and domestic shortages in specialized cybersecurity and cloud engineering capacity (**D**).
</details>

---

### 22. The opposite of Privacy by Design is:
- A. Continuous privacy
- B. Proactive privacy
- C. Privacy added at the end
- D. Built-in privacy

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Privacy added at the end**

*Intuition:* Privacy by Design embeds privacy proactively from inception. The direct anti-pattern is "Privacy by Bolted-On"—treating privacy as an afterthought and trying to retrofit security controls at the end of development.
</details>

---

### 23. Privacy by Design means:
- A. Privacy is optional
- B. Privacy is built in from the start
- C. Privacy is added after deployment
- D. Only physical records are protected

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Privacy is built in from the start**

*Intuition:* Privacy by Design ensures that data protection and privacy mechanisms are integrated directly into system architectures, software engineering, and business workflows from day one.
</details>

---

### 24. A benefit of conducting a DPIA is:
- A. Builds public trust
- B. Increases data breaches
- C. Ignores privacy risks
- D. Reduces compliance

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Builds public trust**

*Intuition:* Systematically identifying and mitigating privacy risks demonstrates corporate accountability, strengthening customer confidence, brand reputation, and regulatory compliance.
</details>

---

### 25. Records must be indexed and titled consistently so they can be:
- A. Deleted immediately
- B. Easily retrieved
- C. Shared publicly
- D. Hidden from users

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Easily retrieved**

*Intuition:* Standardized naming conventions, metadata tagging, and consistent indexing ensure that authorized personnel can quickly locate, audit, and retrieve records when required.
</details>

---

### 26. Secure transfer of records requires:
- A. Public posting
- B. Regular mail
- C. Encryption
- D. No protection

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Encryption**

*Intuition:* Cryptographic encryption (in-transit protocols like TLS or IPsec) converts sensitive records into ciphertext during transmission, ensuring confidentiality against unauthorized network sniffing or interception.
</details>

---

### 27. Access control should be based on:
- A. Full access for everyone
- B. Managers only
- C. No restrictions
- D. Least privilege

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Least privilege**

*Intuition:* The **Principle of Least Privilege (PoLP)** restricts access rights for users, accounts, and processes to only the minimum permissions necessary to complete assigned duties, containing potential security breaches.
</details>

---

### 28. Which TWO are benefits of data sovereignty for Africa?
- A. Better national security and privacy
- B. Increased foreign surveillance
- C. Local infrastructure investment
- D. Reduced government control

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Better national security and privacy** and **C. Local infrastructure investment**

*Intuition:* Data sovereignty shields critical public data from unauthorized foreign intelligence access (**A**) and mandates domestic data hosting, driving capital into local cloud infrastructure and tech jobs (**C**).
</details>

---

### 29. Regulatory fines can result from:
- A. Following regulations
- B. Conducting a DPIA
- C. Skipping a DPIA
- D. Full compliance

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Skipping a DPIA**

*Intuition:* Statutory data protection acts legally require DPIAs for high-risk processing operations. Omitting a mandatory DPIA constitutes statutory non-compliance, exposing entities to severe financial penalties.
</details>

---

### 30. Quality and retention in records management means:
- A. Keep data forever
- B. No quality checks
- C. Keep data only as needed
- D. Retention is optional

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Keep data only as needed**

*Intuition:* Storage limitation principles require that data be retained strictly for the duration necessary to satisfy its initial processing purpose or legal retention mandates, followed by secure destruction.
</details>

---

### 31. Which TWO sensitive data types require protection?
- A. Financial information
- B. Weather data
- C. Traffic patterns
- D. Biometric data

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Financial information** and **D. Biometric data**

*Intuition:* Bank account details (**A**) expose subjects to financial fraud, while biometric traits (**D**) represent immutable personal identifiers; both fall under heightened statutory privacy protections.
</details>

---

### 32. Which TWO steps are part of breach response?
- A. Notify affected people when risk is high
- B. Wait 30 days before acting
- C. Report to the regulator within 72 hours
- D. Never inform the regulator

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Notify affected people when risk is high** and **C. Report to the regulator within 72 hours**

*Intuition:* Primary privacy regulations mandate notifying the supervisory authority without undue delay (typically within 72 hours under GDPR, NDPA, etc.) (**C**) and informing affected individuals when a breach poses high risk to their rights (**A**).
</details>

---

### 33. DPIA originated from:
- A. African Union Charter
- B. GDPR Article 35
- C. UN Declaration
- D. US Constitution

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. GDPR Article 35**

*Intuition:* The formal statutory requirement and terminology for a **Data Protection Impact Assessment (DPIA)** were codified in modern privacy law under Article 35 of the EU General Data Protection Regulation (GDPR).
</details>

---

### 34. Which TWO statements correctly distinguish DPIA from PIA?
- A. They are exactly the same
- B. DPIA is legally defined
- C. PIA is broader and often voluntary
- D. Both are only used in Europe

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. DPIA is legally defined** and **C. PIA is broader and often voluntary**

*Intuition:* A **DPIA** is a specific legal mandate defined under modern data protection statutes (**B**), whereas a **PIA** is a general, historically broader risk assessment framework that organizations often conduct voluntarily as best practice (**C**).
</details>

---

### 35. Which TWO provide regulatory enforcement power?
- A. Voluntary guidelines
- B. Data protection authorities
- C. No enforcement
- D. Data sovereignty laws

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Data protection authorities** and **D. Data sovereignty laws**

*Intuition:* Statutory supervisory bodies (such as Ghana's DPC or South Africa's Information Regulator) (**B**) derive legal powers from national data sovereignty acts (**D**) to audit entities and enforce penalties.
</details>

---

### 36. A Data Protection Impact Assessment (DPIA) is:
- A. A process to identify privacy risks before launch
- B. Used only after a breach
- C. Optional under all laws
- D. Only for government agencies

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. A process to identify privacy risks before launch**

*Intuition:* A DPIA is a proactive evaluation designed to identify, assess, and resolve potential data privacy risks prior to launching new software, systems, or processing activities.
</details>

---

### 37. Which TWO are benefits of DPIA in Africa?
- A. Guarantees zero data breaches
- B. Prevents data breaches early
- C. Eliminates all regulations
- D. Improves legal compliance

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Prevents data breaches early** and **D. Improves legal compliance**

*Intuition:* Conducting a DPIA identifies architectural vulnerabilities early to prevent security incidents (**B**) and ensures alignment with statutory privacy laws across African jurisdictions (**D**).
</details>

---

### 38. Regulatory control in data sovereignty means:
- A. Foreign control
- B. International courts only
- C. Local enforcement
- D. No enforcement

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Local enforcement**

*Intuition:* Data sovereignty establishes that domestic data hosting and processing fall strictly under the jurisdiction, regulatory authorities, and enforcement mechanisms of the local sovereign state.
</details>

---

### 39. Which TWO are outcomes of local data center investment?
- A. Reduce employment
- B. End technical training
- C. More local jobs
- D. Technical skills

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. More local jobs** and **D. Technical skills**

*Intuition:* Expanding local data center infrastructure creates technical employment in facility and network engineering (**C**) while upskilling domestic workforces in cloud operations (**D**).
</details>

---

### 40. DPIA findings must be acted upon:
- A. Only if regulators ask
- B. After the project ends
- C. Before high-risk processing begins
- D. Never

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Before high-risk processing begins**

*Intuition:* Risk mitigations identified during a DPIA must be implemented prior to starting high-risk data processing to protect data subjects from the outset.
</details>

---

### 41. Residual high risks in a DPIA require:
- A. Ignore the risks
- B. Delay action indefinitely
- C. Consult the regulator
- D. Internal review only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Consult the regulator**

*Intuition:* If a DPIA reveals high residual risks that cannot be mitigated by reasonable technical controls, statutory privacy acts legally require the organization to consult the Data Protection Supervisory Authority before launching processing.
</details>

---

### 42. Overly rigid localization rules may:
- A. Attract more foreign investment
- B. Encourage global providers
- C. Keep costs low
- D. Discourage global cloud providers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Discourage global cloud providers**

*Intuition:* Excessive or fragmented data localization mandates increase compliance overhead and operational complexity, discouraging international cloud providers from investing or offering localized services.
</details>

---

### 43. Secure destruction of records means:
- A. Delete from desktop
- B. Burn without oversight
- C. Certified destruction
- D. Shred without records

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Certified destruction**

*Intuition:* Secure destruction requires verifiable proof that physical or digital record media have been permanently sanitized beyond recovery, verified through a formal Certificate of Destruction.
</details>

---

### 44. Which TWO steps are part of the DPIA process?
- A. Wait until launch to assess risks
- B. Build DPIA into the project early
- C. Skip documentation
- D. Identify and manage risks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Build DPIA into the project early** and **D. Identify and manage risks**

*Intuition:* A compliant DPIA process requires integrating privacy assessments early into project planning (**B**) and systematically mapping, identifying, and mitigating privacy risks (**D**).
</details>

---

### 45. Which TWO are consequences of not conducting a DPIA?
- A. Guaranteed system success
- B. Loss of public trust
- C. Automatic legal compliance
- D. Biased outcomes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Loss of public trust** and **D. Biased outcomes**

*Intuition:* Omitting a DPIA increases data breach vulnerabilities, destroying consumer trust (**B**), and fails to evaluate automated profiling algorithms for discriminatory bias (**D**).
</details>

---

### 46. Which TWO are risks of data localization in Africa?
- A. Better connectivity
- B. Internet fragmentation
- C. Limited technical capacity
- D. Lower infrastructure costs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Internet fragmentation** and **C. Limited technical capacity**

*Intuition:* Uncoordinated localization creates regional internet fragmentation (**B**), while domestic technical skill shortages present risks to securing and managing localized facilities (**C**).
</details>

---

### 47. Breach notification to the regulator must occur within:
- A. 30 days
- B. 72 hours
- C. One year
- D. Ten business days

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 72 hours**

*Intuition:* Primary data protection laws mandate reporting personal data breaches to the supervisory authority without undue delay and, where feasible, within **72 hours** of becoming aware of the incident.
</details>

---

### 48. Data sovereignty protects citizens from:
- A. Local governments
- B. International trade agreements
- C. Foreign surveillance
- D. Domestic businesses

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Foreign surveillance**

*Intuition:* By asserting domestic legal jurisdiction over national data, data sovereignty shields citizen data from extraterritorial subpoenas and unauthorized foreign intelligence surveillance.
</details>

---

### 49. POPIA refers to:
- A. Ghana's privacy law
- B. Kenya's privacy law
- C. Nigeria's data law
- D. South Africa's data law

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. South Africa's data law**

*Intuition:* **POPIA** stands for the Protection of Personal Information Act, South Africa's primary statutory data privacy law. (Ghana uses Act 843, Kenya uses DPA 2019, and Nigeria uses NDPA 2023).
</details>

---

### 50. Which TWO are uses of data in the lifecycle?
- A. Ignore insights
- B. Support decisions
- C. Keep data unused
- D. Generate insights

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Support decisions** and **D. Generate insights**

*Intuition:* Data is processed and analyzed during its active lifecycle primarily to drive evidence-based decision-making (**B**) and derive operational insights (**D**).
</details>

---

### 51. A PIA (Privacy Impact Assessment) asks:
- A. How much profit will this make?
- B. What does this mean for people's privacy?
- C. What is the marketing strategy?
- D. How fast is the system?

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. What does this mean for people's privacy?**

*Intuition:* A Privacy Impact Assessment centers fundamentally on evaluating the potential risks, exposures, and privacy impacts a system or project has on individuals' rights.
</details>

---

### 52. The screening checklist in a DPIA is used to:
- A. Hire project staff
- B. Choose software vendors
- C. Approve project funding
- D. Decide whether a DPIA is needed

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Decide whether a DPIA is needed**

*Intuition:* A **DPIA Screening Checklist** serves as an initial threshold filter to determine if proposed data processing involves high-risk factors that legally require conducting a full DPIA.
</details>

---

### 53. When risk is high, affected people should be notified:
- A. After one month
- B. Only if they request it
- C. Through legal documents only
- D. Without delay and in clear language

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Without delay and in clear language**

*Intuition:* Statutory data protection acts mandate that when a data breach poses a high risk to data subjects, the controller must inform affected individuals promptly (**without delay**) using plain, unambiguous language.
</details>

---

### 54. The planning phase of data lifecycle involves:
- A. Random collection
- B. Delete existing data
- C. Define data needs
- D. Share without purpose

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Define data needs**

*Intuition:* The **planning phase** establishes data governance by defining business objectives, data collection requirements, data minimization rules, and compliance boundaries before gathering data.
</details>

---

### 55. External assurance in breach response involves:
- A. Ignoring the incident
- B. Independent assessment
- C. Hiding the breach
- D. Internal reviews only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Independent assessment**

*Intuition:* **External assurance** relies on third-party forensic audits and independent security assessments to objectively verify breach containment, root-cause remediation, and compliance reporting.
</details>

---

### 56. A major challenge of data localization is:
- A. Better internet speed
- B. Lower operational costs
- C. Increased foreign investment
- D. High infrastructure costs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. High infrastructure costs**

*Intuition:* Building, powering, and maintaining domestic server infrastructure and redundant data centers to satisfy local data storage laws requires immense capital expenditure.
</details>

---

### 57. Processing in the data lifecycle includes:
- A. Analysis only
- B. Clean and organize data
- C. Sharing only
- D. Deletion only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Clean and organize data**

*Intuition:* The **data processing phase** involves transforming raw data inputs through cleaning, normalization, structuring, and organizing before downstream analytics or storage.
</details>

---

### 58. Which TWO are phases of the data lifecycle?
- A. Storage only
- B. Processing & analysis
- C. Deletion only
- D. Planning & collection

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Processing & analysis** and **D. Planning & collection**

*Intuition:* The data lifecycle encompasses distinct operational phases, starting with planning and collection (**D**) and proceeding through processing, cleaning, and analysis (**B**).
</details>

---

### 59. Benefits of DPIA in Africa include:
- A. Ignore citizen rights
- B. Reduce public trust
- C. Avoid oversight
- D. Compliance with local laws

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Compliance with local laws**

*Intuition:* Implementing DPIAs ensures organizations align with statutory data privacy mandates across African jurisdictions (such as Ghana's Act 843, Nigeria's NDPA, and South Africa's POPIA), avoiding legal penalties.
</details>

---

### 60. Devaki is capturing traffic on her network. She notices connections using ports 20, 22, 23, and 80. Which port normally hosts a protocol that uses secure, encrypted connections?
- A. 20
- B. 22
- C. 23
- D. 80

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 22**

*Intuition:* **Port 22** runs Secure Shell (SSH), which provides encrypted terminal communication and remote administration. Port 20 is FTP Data, Port 23 is Telnet (unencrypted), and Port 80 is HTTP (unencrypted cleartext).
</details>

---

### 61. What is a U.S. federal government classification level that applies to information that would cause serious damage to national security if it were disclosed?
- A. Top secret
- B. Secret
- C. Confidential
- D. Private

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Secret**

*Intuition:* Government information sensitivity levels are defined as: **Top Secret** (exceptionally grave damage), **Secret** (serious damage), and **Confidential** (damage). "Private" is an enterprise classification tier rather than a government security tier.
</details>

---

### 62. Rachel is investigating an information security incident that took place at the high school where she works. She suspects that students may have broken into the student records system and altered their grades. If that is correct, which one of the tenets of information security did this attack violate?
- A. Confidentiality
- B. Integrity
- C. Availability
- D. Nonrepudiation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Integrity**

*Intuition:* **Integrity** ensures that data remains accurate, complete, and untampered with. Unauthorized modification or altering of academic grades directly compromises data integrity.
</details>

---

### 63. The protocols in the Transmission Control Protocol/Internet Protocol (TCP/IP) suite work together to allow any two computers to be connected and thus create a network.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The **TCP/IP protocol suite** defines standard networking layers, IP addressing, routing, and transport protocols that enable heterogeneous devices across global networks to connect and communicate reliably.
</details>

---

### 64. Access control lists (ACLs) are used to permit and deny traffic in an Internet Protocol (IP) router.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* **Access Control Lists (ACLs)** are packet-filtering rule sets configured on routers and firewalls that inspect source/destination IP addresses and port numbers to permit or deny network traffic.
</details>

---

### 65. Remote access security controls help to ensure that the user connecting to an organization's network is who the user claims to be. A username is commonly used for _______, whereas a biometric scan could be used for _______.
- A. identification, authorization
- B. identification, authentication
- C. authorization, accountability
- D. authentication, authorization

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. identification, authentication**

*Intuition:* A username claims an identity (**Identification**), while a biometric scan (fingerprint/facial scan) verifies that identity claim (**Authentication**).
</details>

---

### 66. Which compliance obligation includes security requirements that apply specifically to the European Union?
- A. Gramm-Leach-Bliley Act (GLBA)
- B. Health Insurance Portability and Accountability Act (HIPAA)
- C. General Data Protection Regulation (GDPR)
- D. Federal Information Security Management Act (FISMA)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. General Data Protection Regulation (GDPR)** *(Note: In raw option lists, C is GDPR; option selection corresponds to General Data Protection Regulation).*

*Intuition:* The **GDPR** is the statutory data protection framework governing personal data privacy across the European Union. GLBA and HIPAA are US-specific acts, while FISMA governs US federal agencies.
</details>

---

### 67. Gwen's company is planning to accept credit cards over the Internet. What governs this type of activity and includes provisions that Gwen should implement before accepting credit card transactions?
- A. Health Insurance Portability and Accountability Act (HIPAA)
- B. Family Educational Rights and Privacy Act (FERPA)
- C. Communications Assistance for Law Enforcement Act (CALEA)
- D. Payment Card Industry Data Security Standard (PCI DSS)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Payment Card Industry Data Security Standard (PCI DSS)** *(Note: Option selection corresponds to Payment Card Industry Data Security Standard).*

*Intuition:* **PCI DSS** is the mandatory security framework established by major payment card brands governing any organization that stores, processes, or transmits credit cardholder data.
</details>

---

### 68. Internet of Things (IoT) devices cannot share and communicate your IoT device data to other systems and applications without your authorization or knowledge.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Embedded background diagnostic software, vendor cloud connectivity, and default firmware permissions often transmit IoT sensor telemetry to third-party brokers without explicit user knowledge or real-time approval.
</details>

---

#### Part B: Extended Sakai Question Pool (Questions 69–75)

### 69. Internal audit and KPIs should track:
- A. Employee attendance
- B. Marketing campaigns
- C. SARs, training, incidents
- D. Financial metrics only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. SARs, training, incidents**

*Intuition:* Compliance-focused KPIs track measurable indicators like Suspicious Activity Reports, training completion, and incident counts.
</details>

---

### 70. The fragmentation risk means:
- A. No regulations exist
- B. All countries have identical rules
- C. Different national rules create barriers
- D. The internet becomes unified

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Different national rules create barriers**

*Intuition:* Divergent national data laws create a patchwork of incompatible rules that hinder cross-border data flow.
</details>

---

### 71. Which TWO laws make DPIA mandatory for high-risk processing?
- A. UK Data Protection Act
- B. Ghana's Act 843
- C. Nigeria's NDPA
- D. US HIPAA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Ghana's Act 843 AND C. Nigeria's NDPA**

*Intuition:* Nigeria's NDPA (Section 28) explicitly mandates DPIAs for high-risk processing; Ghana's DPC guidance (per Act 843) similarly requires DPIAs in specified cases.
</details>

---

### 72. Sharing in the data lifecycle means:
- A. Never share
- B. Sell without consent
- C. Enable reuse
- D. Share only with competitors

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Enable reuse**

*Intuition:* The sharing stage makes data available to authorized parties so it can be reused for legitimate purposes.
</details>

---

### 73. Risks of skipping a DPIA include:
- A. Better system performance
- B. Increased public trust
- C. Regulatory fines
- D. Reduced operational costs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Regulatory fines**

*Intuition:* Unaddressed high-risk processing exposes an organization to regulatory enforcement and fines.
</details>

---

### 74. Which TWO are African data protection laws mentioned?
- A. GDPR
- B. Ghana Act 843
- C. CCPA
- D. Nigeria NDPA

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Ghana Act 843 AND D. Nigeria NDPA**

*Intuition:* Ghana's Act 843 and Nigeria's NDPA are the African-specific laws; GDPR (EU) and CCPA (US) are not.
</details>

---

### 75. Which TWO are records management principles?
- A. Keep records forever
- B. Retention schedules
- C. Never organize records
- D. Quality checks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Retention schedules AND D. Quality checks**

*Intuition:* Retention schedules and quality checks are core principles of sound records management.
</details>

---


---

---

## Quiz 4: Cryptography & Block Cipher Modes (Bayat's Take - 68 Questions)

#### Part A: Core Exam Takes (Questions 1–68)

### 1. Which of the following is classified as an active attack?
- A. Traffic analysis
- B. Wiretapping
- C. Denial of service
- D. Release of message contents

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Denial of service**

*Intuition:* An **active attack** involves an attacker directly altering, modifying, or disrupting system operations, data, or network availability (e.g., Denial of Service, message modification, replay attacks, spoofing). Passive attacks (such as Traffic Analysis, Wiretapping, and Release of message contents) involve monitoring or eavesdropping on transmissions without altering data or affecting system state.
</details>

---

### 2. Counter (CTR) mode is popular in high-speed applications mainly because it allows:
- A. Parallel encryption and decryption of blocks
- B. Operation without an initialization vector
- C. Unlimited key reuse
- D. Sequential-only processing

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Parallel encryption and decryption of blocks**

*Intuition:* **CTR (Counter) mode** turns a block cipher into a stream cipher by encrypting a unique counter value concatenated with a nonce ($E_K(\text{Nonce} \parallel i)$). Because each block's key stream generation is completely independent of previous plaintext or ciphertext blocks, encryption and decryption of multiple blocks can occur simultaneously in parallel pipelines, making it extremely fast for high-speed protocols (e.g., IPsec, TLS 1.3).
</details>

---

### 3. The ____ mode of operation converts a block cipher into a self-synchronizing stream cipher by feeding ciphertext back into the encryption function. (Fill in the blank)
*Answer:* **Cipher Feedback (CFB)**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Cipher Feedback (CFB)**

*Intuition:* **Cipher Feedback (CFB) mode** converts a block cipher into a self-synchronizing stream cipher by encrypting the preceding ciphertext block and XORing the output with the current plaintext block. Because decryption depends only on the preceding $b$ bits of received ciphertext, any bit errors or lost bits in transit automatically self-synchronize after a full block length of valid ciphertext is received.
</details>

---

### 4. The ____ attack on double encryption reduces its effective security roughly to that of single encryption by storing intermediate results. (Fill in the blank)
*Answer:* **meet-in-the-middle**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **meet-in-the-middle**

*Intuition:* A **meet-in-the-middle attack** targets double encryption ($C = E_{K_2}(E_{K_1}(P))$) by encrypting $P$ under all possible first keys $K_1$ and storing intermediate values $X = E_{K_1}(P)$ in a hash table, while decrypting $C$ under all possible second keys $K_2$ to find matches where $D_{K_2}(C) = X$. This space-time tradeoff reduces time complexity from $O(2^{2n})$ to $O(2^{n+1})$ operations, rendering double encryption (like 2DES) virtually no more secure than single encryption.
</details>

---

### 5. Fermat's Little Theorem and Euler's Theorem are foundational to the correctness of the ____ public-key algorithm. (Fill in the blank)
*Answer:* **RSA**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **RSA**

*Intuition:* **RSA** public-key encryption depends directly on Euler's Totient Theorem ($m^{\phi(n)} \equiv 1 \pmod n$) and Fermat's Little Theorem. In RSA, keys are selected such that $e \cdot d \equiv 1 \pmod{\phi(n)}$, ensuring that decryption reverses encryption: $c^d \equiv (m^e)^d = m^{1 + k\phi(n)} \equiv m \pmod n$.
</details>

---

### 6. The Vigenère cipher is an example of a:
- A. Polyalphabetic cipher
- B. Product cipher
- C. Transposition cipher
- D. Monoalphabetic cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Polyalphabetic cipher**

*Intuition:* The **Vigenère cipher** is a polyalphabetic substitution cipher that uses a repeating keyword to apply distinct Caesar cipher shifts to sequential characters. Because the substitution rule changes per character position based on key letters, it flattens simple single-letter frequency distributions.
</details>

---

### 7. An encryption scheme is said to be "computationally secure" if:
- A. It uses a 1000-bit key
- B. It has never been publicly attacked
- C. It requires no key at all
- D. The cost or time of breaking it exceeds the value or useful lifetime of the information

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The cost or time of breaking it exceeds the value or useful lifetime of the information**

*Intuition:* An encryption scheme is **computationally secure** (practical security) if the best-known cryptanalytic attack requires an infeasible volume of computing resources (time, money, hardware, energy) relative to either the commercial/military value of the data or the time duration for which the data must remain confidential.
</details>

---

### 8. Which cryptanalytic technique uses linear approximations of a cipher's operation to recover key bits?
- A. Linear cryptanalysis
- B. Timing analysis
- C. Differential cryptanalysis
- D. Meet-in-the-middle attack

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Linear cryptanalysis**

*Intuition:* **Linear cryptanalysis** is a known-plaintext attack that constructs high-probability linear approximations (XOR relationships) between plaintext, ciphertext, and key bits. By analyzing a high volume of plaintext-ciphertext pairs, statistical deviations from random behavior reveal bits of the secret key.
</details>

---

### 9. Fermat's Little Theorem states that if p is prime and a is not divisible by p, then:
- A. a^p is congruent to a (mod p)
- B. a^(p-1) is congruent to 1 (mod p)
- C. a is congruent to p (mod a)
- D. a^p is congruent to 0 (mod p)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. a^(p-1) is congruent to 1 (mod p)**

*Intuition:* Fermat's Little Theorem states that for any prime $p$ and integer $a$ coprime to $p$, the relation $a^{p-1} \equiv 1 \pmod p$ holds. Multiplying both sides by $a$ yields the alternate form $a^p \equiv a \pmod p$, which holds for all integers $a$, but option B is the exact direct expression under the condition that $a$ is not divisible by $p$.
</details>

---

### 10. Which mode of block cipher operation encrypts blocks independently without chaining, so identical plaintext blocks produce identical ciphertext blocks?
- A. ECB
- B. CBC
- C. CTR
- D. CFB

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. ECB**

*Intuition:* **ECB (Electronic Codebook)** mode encrypts each block independently using the same key. Because there is no feedback or chaining between blocks, identical plaintext blocks encrypt to identical ciphertext blocks, leaking structural patterns of the plaintext.
</details>

---

### 11. RC4 is best described as a:
- A. Public-key algorithm
- B. Stream cipher
- C. Hash function
- D. Block cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Stream cipher**

*Intuition:* **RC4** is a symmetric stream cipher that generates a pseudo-random keystream on a byte-by-byte basis which is then XORed with the plaintext. It does not operate on large fixed-size blocks (unlike AES or DES) and does not use asymmetric key pairs.
</details>

---

### 12. Which block cipher mode turns a block cipher into a self-synchronizing stream-like cipher via ciphertext feedback, avoiding the need for padding?
- A. None of these
- B. ECB
- C. CBC
- D. Cipher Feedback (CFB)

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Cipher Feedback (CFB)**

*Intuition:* **CFB (Cipher Feedback)** mode feeds the generated ciphertext segment back into the cipher shift register to produce the keystream for the next segment. It operates on arbitrary segment sizes (like bytes or bits) without requiring block padding, and recovers from transmission errors after receiving a full block of valid ciphertext.
</details>

---

### 13. Euler's totient function phi(n) counts:
- A. The divisors of n
- B. All integers less than n
- C. The prime factors of n
- D. The positive integers less than n that are relatively prime to n

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The positive integers less than n that are relatively prime to n**

*Intuition:* Euler's totient function $\phi(n)$ counts the cardinality of the multiplicative group of integers modulo $n$, which corresponds to the number of positive integers $k < n$ such that $\gcd(k, n) = 1$.
</details>

---

### 14. A cipher in which plaintext bits or letters are rearranged without changing their values is called a ____ cipher. (Fill in the blank)
*Answer:* **transposition**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **transposition**

*Intuition:* A **transposition cipher** performs a permutation of plaintext elements (moving letters or bits to different positions) without changing their actual values. This contrasts with substitution ciphers, which alter character values.
</details>

---

### 15. Which of the following best defines "computer security" as presented in Stallings' framework?
- A. Physical protection of hardware only
- B. Measures and controls that ensure confidentiality, integrity, and availability of information system assets
- C. Encryption of all stored data
- D. Protection only against unauthorized data access

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Measures and controls that ensure confidentiality, integrity, and availability of information system assets**

*Intuition:* Stallings defines computer security through the core pillars of the **CIA Triad**: Confidentiality (protecting from unauthorized access), Integrity (protecting from unauthorized modification), and Availability (ensuring system/service uptime for authorized users).
</details>

---

### 16. A cipher that replaces each plaintext letter with a fixed, different letter throughout the message is called a:
- A. Rotor cipher
- B. Transposition cipher
- C. Monoalphabetic substitution cipher
- D. Polyalphabetic cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Monoalphabetic substitution cipher**

*Intuition:* A **monoalphabetic substitution cipher** uses a single, fixed mapping (key alphabet) to replace every occurrence of a specific plaintext letter with a corresponding ciphertext letter. Unlike polyalphabetic ciphers, the shift value does not vary by character position.
</details>

---

### 17. The AES SubBytes transformation provides:
- A. Block chaining
- B. Nonlinear byte substitution using an S-box
- C. Key mixing
- D. Diffusion via row shifting

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Nonlinear byte substitution using an S-box**

*Intuition:* In AES, the **SubBytes** transformation uses an S-box constructed from multiplicative inversion in $GF(2^8)$ followed by an affine mapping. This provides the cipher's core **confusion** by introducing nonlinearity, preventing algebraic cryptanalysis.
</details>

---

### 18. Which statement about ECB mode is TRUE?
- A. It is the most secure mode for large messages
- B. It requires no key
- C. It automatically randomizes output
- D. Identical plaintext blocks always produce identical ciphertext blocks, which can leak patterns

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Identical plaintext blocks always produce identical ciphertext blocks, which can leak patterns**

*Intuition:* Because **ECB** mode encrypts each block independently without chaining, a given plaintext block always maps to the same ciphertext block under the same key. This leaks structured information and data patterns (e.g., in images).
</details>

---

### 19. In the Playfair cipher, when two plaintext letters fall in the same row of the matrix, each is replaced by:
- A. The letter above it
- B. The letter to its right, wrapping to the start of the row
- C. The letter below it
- D. The letter diagonally opposite it

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. The letter to its right, wrapping to the start of the row**

*Intuition:* The rules of the **Playfair cipher** state that if two plaintext letters occupy the same row in the 5x5 key matrix, they are replaced by the letters immediately to their right, with the rightmost column wrapping around to the leftmost column.
</details>

---

### 20. Euler's totient function of a prime number p is equal to p minus 1.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* A prime number $p$ has no positive divisors other than $1$ and $p$. Therefore, all positive integers strictly less than $p$ (which total $p-1$) are relatively prime to $p$, meaning $\phi(p) = p - 1$.
</details>

---

### 21. Compared to symmetric encryption, public-key encryption is generally:
- A. Impossible to implement in software
- B. Faster for bulk data encryption
- C. Not used for digital signatures
- D. Computationally slower, so it is often used to encrypt keys rather than bulk data

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Computationally slower, so it is often used to encrypt keys rather than bulk data**

*Intuition:* Asymmetric encryption algorithms (like RSA and ECC) rely on complex number-theoretic operations like modular exponentiation, making them significantly slower than symmetric algorithms (like AES). Consequently, hybrid systems encrypt bulk data symmetrically and encrypt/exchange the symmetric keys asymmetrically.
</details>

---

### 22. In the Feistel cipher structure, the function applied within each round is called the ____ function. (Fill in the blank)
*Answer:* **round**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **round**

*Intuition:* In Feistel networks, the **round function** ($F$) takes the right half of the data block and a round subkey to output a value that is XORed with the left half. The function itself does not need to be invertible.
</details>

---

### 23. The main practical drawback of the one-time pad is:
- A. It is vulnerable to frequency analysis
- B. It cannot encrypt binary data
- C. The difficulty of generating and distributing truly random keys as long as the message
- D. It is easy to cryptanalyze

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. The difficulty of generating and distributing truly random keys as long as the message**

*Intuition:* Although the **One-Time Pad** offers perfect information-theoretic security, it requires a key that is truly random, used only once, and equal in length to the plaintext. Distributing and managing keys under these constraints is highly impractical for mass data networks.
</details>

---

### 24. In a Feistel cipher structure, encryption and decryption are:
- A. Essentially identical, with the subkeys used in reverse order for decryption
- B. Impossible to reverse
- C. Completely different algorithms
- D. Only possible with the same key length

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Essentially identical, with the subkeys used in reverse order for decryption**

*Intuition:* The Feistel structure is mathematically designed to be self-reversing. Decryption uses the exact same algorithmic round steps as encryption, with the sole difference being that the round subkeys are applied in reverse sequence (from $K_n$ down to $K_1$).
</details>

---

### 25. DES uses a Feistel structure with 16 rounds of processing.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* The Data Encryption Standard (DES) is a classic Feistel cipher that processes 64-bit plaintext blocks through exactly 16 rounds of substitution and permutation using subkeys derived from the master key.
</details>

---

### 26. Triple DES (3DES) with two keys typically uses which encryption sequence?
- A. Decrypt-Decrypt-Decrypt
- B. Encrypt-Encrypt-Encrypt with three different keys
- C. A single DES pass repeated three times with the same key
- D. Encrypt-Decrypt-Encrypt (EDE) using K1, K2, K1

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Encrypt-Decrypt-Encrypt (EDE) using K1, K2, K1**

*Intuition:* Two-key 3DES uses the EDE sequence: $C = E_{K_1}(D_{K_2}(E_{K_1}(P)))$. The decryption stage with $K_2$ enables backward compatibility with single DES if $K_1 = K_2$, while offering an effective 112-bit key strength when $K_1 \neq K_2$.
</details>

---

### 27. The Chinese Remainder Theorem is useful in cryptography chiefly because it:
- A. Allows faster modular exponentiation by working with smaller moduli
- B. Computes discrete logarithms efficiently
- C. Generates prime numbers directly
- D. Breaks RSA encryption

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Allows faster modular exponentiation by working with smaller moduli**

*Intuition:* The **CRT** allows computation modulo a large composite product $n = pq$ to be performed independently modulo the smaller primes $p$ and $q$. This reduces the computational cost of RSA decryption/signing by roughly $4\times$.
</details>

---

### 28. Which AES transformation cyclically shifts the rows of the state array?
- A. AddRoundKey
- B. SubBytes
- C. MixColumns
- D. ShiftRows

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. ShiftRows**

*Intuition:* The **ShiftRows** step in AES cyclically shifts the second, third, and fourth rows of the 4x4 state matrix by 1, 2, and 3 bytes respectively. This ensures bytes from the same column are distributed into different columns in subsequent rounds, facilitating **diffusion**.
</details>

---

### 29. The Playfair cipher encrypts:
- A. Trigrams
- B. Whole words
- C. Digrams (pairs of letters)
- D. Single letters

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Digrams (pairs of letters)**

*Intuition:* **Playfair** is the first practical symmetric digraph substitution cipher. It processes plaintext in 2-letter blocks (digrams) using rules based on their relative coordinates in a 5x5 key matrix.
</details>

---

### 30. The Euclidean algorithm is used primarily to compute:
- A. The greatest common divisor of two integers
- B. Discrete logarithms
- C. The prime factorization of a number
- D. Modular exponentiation directly

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The greatest common divisor of two integers**

*Intuition:* The **Euclidean algorithm** is a highly efficient recursive technique for calculating the Greatest Common Divisor ($\gcd$) of two integers by exploiting the property that $\gcd(a, b) = \gcd(b, a \pmod b)$ until the remainder is zero.
</details>

---

### 31. The Diffie-Hellman protocol allows two parties to:
- A. Compute prime factorizations
- B. Encrypt messages directly without a symmetric cipher
- C. Establish a shared secret key over an insecure channel
- D. Sign documents digitally

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Establish a shared secret key over an insecure channel**

*Intuition:* **Diffie-Hellman (DH)** key exchange enables two parties to securely compute a shared symmetric key over a public network. Its mathematical security is anchored on the computational hardness of the discrete logarithm problem.
</details>

---

### 32. A rail fence cipher is an example of a:
- A. Substitution technique
- B. Transposition technique
- C. Product cipher
- D. Stream cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Transposition technique**

*Intuition:* The **rail fence cipher** writes plaintext characters in a zigzag pattern across multiple imaginary rails and reads them off row-by-row. Because characters are reordered rather than replaced, it is classified as a transposition cipher.
</details>

---

### 33. The "model for network security" presented by Stallings assumes that communicating parties need which two things to counter an opponent?
- A. A router and a switch
- B. A backup system and an encryption key
- C. A firewall and antivirus software
- D. A trusted third party and an appropriate security transformation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A trusted third party and an appropriate security transformation**

*Intuition:* Stallings' security model dictates that to protect a message, the parties must apply a **security transformation** (e.g., encryption) and rely on a **trusted third party** (e.g., KDC/CA) to distribute keys or confirm identities.
</details>

---

### 34. Which of these is classified as a security mechanism rather than a security service under X.800?
- A. Encipherment
- B. Access control
- C. Authentication
- D. Non-repudiation

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Encipherment**

*Intuition:* Under X.800, **security services** define the high-level security objectives (e.g., Access Control, Confidentiality), whereas **security mechanisms** (like Encipherment/Encryption or Digital Signatures) are the concrete cryptographic algorithms used to implement those services.
</details>

---

### 35. In the ElGamal public-key cryptosystem, security is based on the difficulty of computing:
- A. Square roots modulo n
- B. Cube roots modulo n
- C. Discrete logarithms in a finite field
- D. Modular inverses only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Discrete logarithms in a finite field**

*Intuition:* The **ElGamal** cryptosystem (used for encryption and signatures) derives its security directly from the difficulty of the discrete logarithm problem in finite fields (or elliptic curve groups).
</details>

---

### 36. Blum Blum Shub (BBS) is an example of a PRNG built on:
- A. The Hill cipher
- B. The Playfair cipher
- C. Number-theoretic quadratic residue problems believed to be computationally hard
- D. The DES algorithm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Number-theoretic quadratic residue problems believed to be computationally hard**

*Intuition:* **Blum Blum Shub (BBS)** is a cryptographically secure pseudorandom number generator (CSPRNG) whose mathematical security is proven to be as hard as integer factorization, specifically using modular quadratic residues.
</details>

---

### 37. A pseudorandom number generator (PRNG) is considered cryptographically secure if:
- A. It passes only basic statistical tests
- B. An adversary cannot practically distinguish its output from true randomness or predict other outputs
- C. It uses a publicly known seed
- D. Its period is shorter than the key length

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. An adversary cannot practically distinguish its output from true randomness or predict other outputs**

*Intuition:* A **CSPRNG** must satisfy the next-bit test (unpredictability) and be indistinguishable from a truly random sequence. Passing standard empirical statistical tests is necessary but not sufficient for cryptographic applications.
</details>

---

### 38. Triple DES using three independent keys effectively provides a key length of 168 bits.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Three-key 3DES utilizes three distinct 56-bit DES keys ($K_1, K_2, K_3$). Thus, the nominal/effective key length is $3 \times 56 = 168$ bits, although the actual cryptographic security level is capped at 112 bits due to meet-in-the-middle attacks.
</details>

---

### 39. True random number generators typically derive entropy from:
- A. Deterministic software algorithms only
- B. The encryption key only
- C. Physical noise sources such as thermal or electronic noise
- D. The plaintext itself

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Physical noise sources such as thermal or electronic noise**

*Intuition:* **TRNGs** harvest entropy from non-deterministic physical phenomena (e.g., thermal noise, avalanche diode noise, or radioactive decay) to guarantee that outputs cannot be mathematically predicted or reproduced.
</details>

---

### 40. In modular exponentiation, the "square-and-multiply" algorithm improves efficiency by:
- A. Reducing the number of multiplications needed to compute a^k mod n
- B. Avoiding multiplication altogether
- C. Using only addition operations
- D. Working exclusively with small primes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Reducing the number of multiplications needed to compute a^k mod n**

*Intuition:* The **square-and-multiply** algorithm reduces the time complexity of computing $a^k \pmod n$ from linear $O(k)$ to logarithmic $O(\log k)$ operations by scanning the binary representation of the exponent $k$.
</details>

---

### 41. Elliptic curve cryptography (ECC) is attractive because it can achieve security comparable to RSA with:
- A. Significantly smaller key sizes
- B. No underlying mathematical hard problem
- C. No public key at all
- D. Larger key sizes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Significantly smaller key sizes**

*Intuition:* Because the Elliptic Curve Discrete Logarithm Problem (ECDLP) is significantly harder to solve than RSA integer factorization, ECC provides equivalent security with far smaller keys (e.g., 256-bit ECC is comparable to 3072-bit RSA), reducing processing overhead.
</details>

---

### 42. What is the main weakness that makes monoalphabetic substitution ciphers easy to break?
- A. They require a computer to implement
- B. They preserve the frequency distribution of the underlying language
- C. A very small key space only
- D. They cannot encrypt numbers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. They preserve the frequency distribution of the underlying language**

*Intuition:* Because a monoalphabetic cipher replaces every occurrence of a plaintext letter with the exact same ciphertext letter, the underlying statistical frequency of the language (e.g., 'E' being the most common letter in English) is preserved, exposing it to **frequency analysis**.
</details>

---

### 43. Public-key cryptography, unlike symmetric cryptography, uses:
- A. No key at all
- B. A mathematically related key pair, one public and one private
- C. Only a shared secret established in advance
- D. The same key for both encryption and decryption

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A mathematically related key pair, one public and one private**

*Intuition:* Asymmetric systems utilize two distinct keys: a **public key** for encryption/verification and a mathematically linked **private key** for decryption/signing.
</details>

---

### 44. In the Caesar cipher, if the shift key is 3, the plaintext letter 'A' encrypts to:
- A. 'D'
- B. 'C'
- C. 'X'
- D. 'B'

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 'D'**

*Intuition:* The Caesar cipher shifts characters forward by the key value. Shifting 'A' forward by 3 steps ($0 + 3 = 3$) yields 'D' (position 3 in a 0-indexed alphabet).
</details>

---

### 45. A passive attack attempts to alter system resources or affect their normal operation.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Passive attacks (monitoring, traffic analysis) do *not* modify system resources or traffic. An attack that alters resources or interrupts services is classified as an **active attack**.
</details>

---

### 46. The Miller-Rabin test is used for:
- A. Probabilistic primality testing
- B. Factoring large numbers
- C. Computing discrete logarithms
- D. Generating S-boxes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Probabilistic primality testing**

*Intuition:* The **Miller-Rabin** algorithm is a fast probabilistic test used in RSA key generation to verify if a randomly chosen large integer is prime.
</details>

---

### 47. DES operates on plaintext blocks of:
- A. 32 bits
- B. 128 bits
- C. 64 bits
- D. 56 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. 64 bits**

*Intuition:* The Data Encryption Standard (DES) is designed with a fixed block size of 64 bits. It encrypts and decrypts data in 64-bit segments.
</details>

---

### 48. The effective key length used by DES for encryption is:
- A. 56 bits
- B. 48 bits
- C. 64 bits
- D. 128 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 56 bits**

*Intuition:* Although a DES key is represented as 64 bits, 8 of those bits are used exclusively as parity bits for error detection. The cryptographic strength of DES rests solely on the remaining 56 bits.
</details>

---

### 49. In the context of security attacks, which category includes eavesdropping and traffic analysis?
- A. Replay attacks
- B. Masquerade attacks
- C. Active attacks
- D. Passive attacks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Passive attacks**

*Intuition:* **Passive attacks** involve eavesdropping and traffic analysis, as they monitor data streams without modifying contents or injecting malicious traffic.
</details>

---

### 50. The "period" of a pseudorandom generator refers to:
- A. The number of rounds
- B. The length of the seed
- C. The block size
- D. The length of the sequence before it starts repeating

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The length of the sequence before it starts repeating**

*Intuition:* Since PRNGs are finite-state deterministic machines, their outputs eventually repeat. The **period** is the length of the pseudorandom sequence generated before it enters a repeating loop.
</details>

---

### 51. A key advantage of the Feistel structure is that:
- A. The same hardware or software can be used for both encryption and decryption
- B. It requires two different algorithms for encryption and decryption
- C. It cannot use a round function
- D. It only works with 64-bit blocks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The same hardware or software can be used for both encryption and decryption**

*Intuition:* Because the Feistel structure is self-reversing, the exact same hardware/software block execution paths are reused for both encryption and decryption, only requiring the subkeys to be supplied in reverse order.
</details>

---

### 52. A brute-force attack on an encryption algorithm involves:
- A. Intercepting the key during exchange
- B. Trying every possible key until the correct one is found
- C. Guessing the plaintext based on context
- D. Exploiting mathematical weaknesses in the algorithm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Trying every possible key until the correct one is found**

*Intuition:* A **brute-force attack** is an exhaustive key search that tests every possible key combination in the keyspace until the correct key recovers legible plaintext.
</details>

---

### 53. In block cipher design, "confusion" as described by Shannon aims to:
- A. Make the relationship between the key and ciphertext as complex as possible
- B. Increase the block size
- C. Spread plaintext statistics through the ciphertext
- D. Reduce the number of rounds needed

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Make the relationship between the key and ciphertext as complex as possible**

*Intuition:* **Confusion** obscures the relationship between the encryption key and the ciphertext, usually implemented via S-boxes, so that attackers cannot deduce key bits even if they analyze plaintext/ciphertext pairs.
</details>

---

### 54. Cipher Block Chaining (CBC) mode XORs each plaintext block with:
- A. The previous ciphertext block before encryption
- B. A fixed nonce only
- C. The secret key
- D. The next plaintext block

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The previous ciphertext block before encryption**

*Intuition:* **CBC** mode chains blocks by XORing each plaintext block with the preceding ciphertext block ($C_{i-1}$) before feeding it to the block cipher, ensuring that duplicate plaintext blocks produce different ciphertexts.
</details>

---

### 55. In modular arithmetic, what is 17 mod 5?
- A. 2
- B. 5
- C. 12
- D. 3

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 2**

*Intuition:* $17 \pmod 5$ finds the remainder of $17$ divided by $5$. Since $5 \times 3 = 15$, the remainder is $17 - 15 = 2$.
</details>

---

### 56. The one-time pad remains perfectly secure even if the same key is reused for multiple messages.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Reusing a one-time pad key results in the "two-time pad" vulnerability. An attacker can XOR the two ciphertexts together ($C_1 \oplus C_2 = P_1 \oplus P_2$), removing the key entirely and exposing the plaintexts to frequency analysis.
</details>

---

### 57. The discrete logarithm problem is considered computationally hard because:
- A. It requires floating-point precision
- B. Given g, p, and g^x mod p, finding x is infeasible for large p
- C. Multiplication is undefined in modular arithmetic
- D. Addition modulo n is difficult to perform

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Given g, p, and g^x mod p, finding x is infeasible for large p**

*Intuition:* The **Discrete Logarithm Problem (DLP)** is the one-way mathematical function where computing modular exponentiation ($y = g^x \pmod p$) is easy, but reversing it to find $x$ is computationally infeasible for sufficiently large primes $p$.
</details>

---

### 58. In the RSA algorithm, the public key consists of:
- A. The exponent e and modulus n
- B. Only the modulus n
- C. The private exponent d and modulus n
- D. The two secret primes p and q

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The exponent e and modulus n**

*Intuition:* In RSA, the public key used for encryption or signature verification consists of the public exponent $e$ and the modulus $n$ ($n = pq$).
</details>

---

### 59. AES with a 128-bit key uses how many rounds?
- A. 14
- B. 10
- C. 12
- D. 8

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 10**

*Intuition:* The number of rounds in AES is determined by key length: 10 rounds for a 128-bit key, 12 rounds for a 192-bit key, and 14 rounds for a 256-bit key.
</details>

---

### 60. RSA's security is based primarily on the difficulty of computing discrete logarithms.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* RSA's mathematical security is based on the **integer factorization problem** (factoring a large composite number $n$ into its prime factors $p$ and $q$), not discrete logarithms.
</details>

---

### 61. AES supports key lengths of:
- A. 56 bits only
- B. 128, 192, or 256 bits
- C. Only 128 bits
- D. 64 or 128 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 128, 192, or 256 bits**

*Intuition:* The Advanced Encryption Standard (AES) specifies three supported key sizes: 128 bits, 192 bits, and 256 bits, all sharing a fixed 128-bit block size.
</details>

---

### 62. Double DES is largely negated in its expected security improvement by which attack?
- A. Differential cryptanalysis
- B. Meet-in-the-middle attack
- C. Birthday attack
- D. Frequency analysis

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Meet-in-the-middle attack**

*Intuition:* The **meet-in-the-middle attack** reduces the security of Double DES from a theoretical 112 bits down to an effective 57 bits of security by computing and storing intermediate values from both ends of the double cipher.
</details>

---

### 63. AES, selected by NIST to replace DES, operates on a block size of:
- A. 256 bits
- B. 128 bits
- C. 64 bits
- D. 192 bits

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. 128 bits**

*Intuition:* AES operates on a fixed block size of 128 bits (16 bytes) organized as a 4x4 state array, replacing DES's smaller 64-bit block size.
</details>

---

### 64. Stream ciphers, like block ciphers, always process plaintext in large fixed-size blocks.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Stream ciphers generate a continuous keystream to encrypt plaintext bit-by-bit or byte-by-byte, whereas block ciphers require parsing data in fixed-size blocks (e.g., 64 or 128 bits) with padding.
</details>

---

### 65. The main criticism of DES that eventually led to its replacement was:
- A. It only worked on ASCII text
- B. Its 56-bit key length is vulnerable to brute-force attack
- C. Its block size was too large
- D. It could not be implemented in hardware

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Its 56-bit key length is vulnerable to brute-force attack**

*Intuition:* DES's 56-bit keyspace ($2^{56}$ options) became vulnerable to brute-force key exhaustive searches by custom hardware crackers in the late 1990s, forcing the migration to AES.
</details>

---

### 66. An initialization vector (IV) is used in most chaining modes primarily to:
- A. Authenticate the sender
- B. Replace the secret key
- C. Compress the plaintext
- D. Ensure that identical plaintexts encrypted with the same key produce different ciphertexts

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Ensure that identical plaintexts encrypted with the same key produce different ciphertexts**

*Intuition:* The **Initialization Vector (IV)** randomizes the first encryption block, preventing duplicate messages from yielding identical ciphertext blocks, defending against pattern analysis.
</details>

---

### 67. Availability, as a security objective, means:
- A. Information is disclosed only to authorized parties
- B. Data cannot be altered improperly
- C. Systems work promptly and service is not denied to authorized users
- D. Data origin can be verified

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Systems work promptly and service is not denied to authorized users**

*Intuition:* **Availability** ensures that systems, services, and data are promptly accessible and functional for authorized users whenever needed.
</details>

---

### 68. "Diffusion" in a block cipher refers to:
- A. Dissipating the statistical structure of plaintext over the bulk of the ciphertext
- B. Reducing the avalanche effect
- C. Encrypting with multiple keys simultaneously
- D. Making the statistical relationship between key and ciphertext complex

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Dissipating the statistical structure of plaintext over the bulk of the ciphertext**

*Intuition:* **Diffusion** spreads the influence of single plaintext or key bits across multiple output bits (e.g., via ShiftRows and MixColumns), hiding plaintext statistical redundancy in the ciphertext.
</details>

---


---

---

## Quiz 5: Comprehensive Question Bank & Review (Bayat's Take - 70 Questions)

#### Part A: Core Exam Takes (Questions 1–70)

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

#### Part B: Extended Sakai Question Pool (Questions 71–90)

### 71. Unlike a MAC, a digital signature:
- A. Requires a symmetric shared secret key
- B. Is always shorter than a MAC
- C. Cannot be verified by a third party
- D. Uses the signer's private key, so anyone with the public key can verify it

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Uses the signer's private key, so anyone with the public key can verify it**

*Intuition:* A digital signature is created with a private key and can be verified using the corresponding public key.
</details>

---

### 72. HMAC's security depends primarily on the strength of the underlying block cipher rather than the embedded hash function.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* HMAC is a hash-based authentication mechanism, so its security depends primarily on the underlying cryptographic hash function and the secrecy of the key.
</details>

---

### 73. HTTPS is essentially:
- A. A completely separate protocol unrelated to HTTP
- B. HTTP combined with Kerberos authentication
- C. HTTP with an additional compression layer
- D. HTTP running over an SSL/TLS-secured connection

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. HTTP running over an SSL/TLS-secured connection**

*Intuition:* HTTPS is HTTP protected by TLS, providing confidentiality, integrity, and authentication.
</details>

---

### 74. The NIST-standardized digital signature algorithm based on discrete logarithms is called the ____.
*Answer:* **DSA**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **DSA**

*Intuition:* Digital Signatures
</details>

---

### 75. X.509 certificates bind a public key to an identity and are digitally signed by a certificate authority.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* An X.509 certificate associates a public key with an identity and is signed by its issuing CA.
</details>

---

### 76. An X.509 certificate primarily binds:
- A. A symmetric key to a password
- B. An IP address to a MAC address
- C. A public key to an identity, digitally signed by a certificate authority
- D. A private key to a single session

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. A public key to an identity, digitally signed by a certificate authority**

*Intuition:* X.509 certificates bind identities to public keys and contain a CA's digital signature.
</details>

---

### 77. In a typical TLS handshake, the server authenticates itself to the client using:
- A. A shared password
- B. A MAC key only
- C. A Kerberos ticket
- D. A digital certificate containing its public key

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. A digital certificate containing its public key**

*Intuition:* The server normally presents a CA-signed digital certificate containing its public key.
</details>

---

### 78. In Kerberos, the component that issues session tickets for specific services after initial authentication is the:
- A. Authentication Server (AS)
- B. Key Distribution Center exclusively
- C. Ticket-Granting Server (TGS)
- D. Certificate Authority

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Ticket-Granting Server (TGS)**

*Intuition:* The TGS issues service tickets after the user has obtained a Ticket-Granting Ticket from the AS.
</details>

---

### 79. In Kerberos, the server that authenticates a user's initial login and issues a ticket-granting ticket is called the ____.
*Answer:* **Authentication Server (AS)**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Authentication Server (AS)**

*Intuition:* Kerberos
</details>

---

### 80. Preimage resistance of a hash function means that given a hash value h, it should be infeasible to:
- A. Compute the hash of a known message
- B. Compress the message further
- C. Find a second input with the same hash as a known input
- D. Find any input x such that H(x) equals h

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Find any input x such that H(x) equals h**

*Intuition:* Preimage resistance means it should be infeasible to find any input x such that H(x) equals a given hash value h.
</details>

---

### 81. A trusted entity that issues and digitally signs public-key certificates in a PKI is called a ____.
*Answer:* **Certificate Authority (CA)**

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Certificate Authority (CA)**

*Intuition:* PKI
</details>

---

### 82. Distribution of public keys by simple public announcement is vulnerable primarily to:
- A. Brute-force key search
- B. Collision attacks
- C. Forgery, since anyone can claim to be a particular user and broadcast a bogus key
- D. Traffic analysis only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Forgery, since anyone can claim to be a particular user and broadcast a bogus key**

*Intuition:* Without a trusted binding between a key and identity, an attacker can announce a fraudulent public key while impersonating another user.
</details>

---

### 83. The SSL/TLS Handshake Protocol is responsible for:
- A. Negotiating cryptographic parameters and authenticating the parties before data exchange
- B. Routing IP packets
- C. Encrypting bulk application data only
- D. Compressing files for transmission

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Negotiating cryptographic parameters and authenticating the parties before data exchange**

*Intuition:* The TLS handshake negotiates cryptographic parameters, authenticates parties as applicable, and establishes session keys.
</details>

---

### 84. In PGP, message confidentiality is typically achieved by encrypting the message with a symmetric session key, which is then:
- A. Encrypted with the recipient's public key and sent along with the message
- B. Discarded after use without any protection
- C. Sent alongside the message in plaintext
- D. Hashed and stored on a server

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Encrypted with the recipient's public key and sent along with the message**

*Intuition:* PGP uses hybrid encryption: the message is symmetrically encrypted, while the session key is encrypted with the recipient's public key.
</details>

---

### 85. User authentication is fundamentally the process of:
- A. Encrypting user data
- B. Generating session keys only
- C. Compressing user credentials
- D. Verifying the claimed identity of a user or system entity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Verifying the claimed identity of a user or system entity**

*Intuition:* Authentication verifies that a user or system entity is who or what it claims to be.
</details>

---

### 86. A Certificate Authority (CA) in a PKI is responsible for:
- A. Storing symmetric session keys
- B. Verifying identities and digitally signing public-key certificates
- C. Encrypting all network traffic
- D. Generating users' private keys only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Verifying identities and digitally signing public-key certificates**

*Intuition:* A CA verifies identities according to its policies and signs certificates to establish trust in public keys.
</details>

---

### 87. A replay attack against a MAC-protected message can be effectively mitigated by including:
- A. A longer hash digest
- B. A sequence number or timestamp within the authenticated data
- C. A weaker MAC algorithm
- D. A larger MAC key only

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. A sequence number or timestamp within the authenticated data**

*Intuition:* A sequence number or timestamp allows the receiver to identify stale or previously used messages.
</details>

---

### 88. Federated identity management allows:
- A. Certificates to be issued without any CA
- B. A single organization to manage all identities in total isolation
- C. Identity and authentication information to be shared across autonomous security domains
- D. Passwords to be eliminated entirely

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Identity and authentication information to be shared across autonomous security domains**

*Intuition:* Federation allows trusted organizations or security domains to share identity and authentication information.
</details>

---

### 89. IEEE 802.11i was developed primarily to address security weaknesses in:
- A. Wired Ethernet networks
- B. Cellular telephone networks
- C. Bluetooth
- D. The original WEP protocol for wireless LANs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. The original WEP protocol for wireless LANs**

*Intuition:* 802.11i strengthened wireless LAN security and addressed major weaknesses in WEP.
</details>

---

### 90. In the ElGamal digital signature scheme, security is grounded in the difficulty of:
- A. Computing discrete logarithms
- B. Solving the knapsack problem
- C. Breaking AES directly
- D. Factoring composite numbers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Computing discrete logarithms**

*Intuition:* ElGamal signatures rely on the computational difficulty of discrete logarithms.
</details>

---


---

---

## Additional Questions (Christian's Quiz 1-4)

### 100. Which element of the security policy framework requires approval from upper management and applies to the entire organization?
- A. Policy
- B. Standard
- C. Guideline
- D. Procedure

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Policy**

*Intuition:* Policies are high-level statements that require senior/upper management approval and apply broadly across the entire organization, setting overall direction and intent. Standards, guidelines, and procedures typically flow from policies and can be approved/managed at lower levels since they support implementation rather than set organizational-wide mandate.
</details>

---

### 101. Internet of Things (IoT) upgrades can be difficult to distribute and deploy, leaving gaps in the remediation of IoT devices or endpoints.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* IoT upgrades and patches can be difficult to distribute and deploy due to device diversity, limited connectivity, vendor support lifecycles, resource-constrained hardware, and devices deployed in hard-to-reach locations, which often leaves security gaps where vulnerabilities remain unremediated for extended periods.
</details>

---

### 102. Which organization pursues standards for Internet of Things (IoT) devices and is widely recognized as the authority for creating standards on the Internet?
- A. Internet Society
- B. Internet Engineering Task Force (IETF)
- C. Internet Association
- D. Internet Authority

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Internet Engineering Task Force (IETF)**

*Intuition:* The IETF is widely recognized as the leading authority for developing and maintaining Internet standards, including protocols relevant to IoT. The Internet Society is IETF's parent organization but isn't itself the standards-writing body, and the other two options aren't legitimate standards organizations.
</details>

---

### 103. A benefit of conducting a Data Protection Impact Assessment (DPIA) is:
- A. Builds public trust
- B. Increases data breaches
- C. Ignores privacy risks
- D. Reduces compliance

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Builds public trust**

*Intuition:* A DPIA identifies and mitigates privacy risks before a system or process launches, and demonstrating that care publicly signals accountability to users and regulators, which is what builds trust. The other options describe outcomes a DPIA is specifically meant to prevent, not produce.
</details>

---

### 104. A DPIA should be reviewed:
- A. When processing changes or regularly
- B. Only once
- C. Every ten years
- D. Never again

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. When processing changes or regularly**

*Intuition:* A DPIA isn't a one-and-done exercise, it should be revisited whenever there's a significant change to the processing activity (new data types, new purposes, new systems) or on a regular schedule, since risks can evolve over time. Treating it as a single, permanent assessment defeats its purpose of ongoing risk management.
</details>

---

### 105. A Data Protection Impact Assessment (DPIA) is:
- A. A process to identify privacy risks before launch
- B. Used only after a breach
- C. Optional under all laws
- D. Only for government agencies

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. A process to identify privacy risks before launch**

*Intuition:* A DPIA is a proactive process conducted before deployment to identify and mitigate privacy risks, not something used reactively after a breach, and it's legally mandatory (not optional) under laws like Ghana's Act 843 and Nigeria's NDPA, applying broadly rather than only to government agencies.
</details>

---

### 106. Elliptic curve cryptography (ECC) is attractive because it can achieve security comparable to RSA with:
- A. Significantly smaller key sizes
- B. No underlying mathematical hard problem
- C. No public key at all
- D. Larger key sizes

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Significantly smaller key sizes**

*Intuition:* Why ECC Requires Smaller Key Sizes: **Underlying Hard Problem:** The security of ECC is based on the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**. The best-known classical algorithms to solve ECDLP (such as Pollard's rho) run in **fully exponential time** (O(n![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="1.08em"%20viewBox="0%200%20400000%201080"%20preserveAspectRatio="xMinYMin%20slice"><path%20d="M95,702%0Ac-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14%0Ac0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54%0Ac44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10%0As173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429%0Ac69,-144,104.5,-217.7,106.5,-221%0Al0%20-0%0Ac5.3,-9.3,12,-14,20,-14%0AH400000v40H845.2724%0As-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7%0Ac-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z%0AM834%2080h400000v40h-400000z"></path></svg>)​)). **Comparison with RSA:** In contrast, the integer factorization problem underlying RSA can be attacked using the **General Number Field Sieve (GNFS)**, which runs in **sub-exponential time**. Because GNFS scales faster against larger RSA moduli, RSA requires exponentially larger key sizes to maintain equivalent security levels. Key Size Comparison for Equivalent Security Levels (NIST Guidelines): |Symmetric Security Level|ECC Key Size|RSA Modulus Size|Key Size Ratio| |---|---|---|---| |**112-bit** (Legacy)|224 bits|2048 bits|~1 : 9| |**128-bit** (Standard)|**256 bits**|**3072 bits**|~1 : 12| |**192-bit** (High)|384 bits|7680 bits|~1 : 20| |**256-bit** (Ultra)|512 bits|15360 bits|~1 : 30| Practical Benefits: Faster mathematical computation and lower processing latency. Reduced power consumption (ideal for mobile, smart cards, and IoT devices). Smaller certificate and digital signature payloads over network transmissions. Why the Other Options Are Incorrect: **B (No underlying mathematical hard problem):** False; ECC relies directly on the hardness of the ECDLP. **C (No public key at all):** False; ECC is an asymmetric public-key cryptosystem (a public key is a point on the curve, and the private key is an integer scalar). **D (Larger key sizes):** Incorrect; ECC's primary advantage is requiring much _smaller_ keys than RSA.
</details>

---

### 107. Vendors or service providers that have remote access to an Internet of Things (IoT) device may be able to pull information or data from your device without your permission.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Vendors with remote access to an IoT device can typically pull data/telemetry from it as part of normal operation (diagnostics, updates, usage analytics), often under terms buried in a EULA or privacy policy the user never fully reads or meaningfully consents to. So functionally, data can be collected without the user's informed permission, even if it's technically authorized in some fine print.
</details>

---

### 108. Which of the following is an example of a business-to-consumer (B2C) application of the Internet of Things (IoT)?
- A. Video conferencing
- B. Infrastructure monitoring
- C. Health monitoring
- D. Traffic monitoring

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Health monitoring**

*Intuition:* Health monitoring (like wearable fitness trackers, smartwatches, or remote patient monitoring devices) is a direct B2C application, businesses provide these IoT devices/services directly to individual consumers. Infrastructure and traffic monitoring are typically government/enterprise applications, and video conferencing isn't inherently an IoT application.
</details>

---

### 109. Application service providers (ASPs) are software companies that build applications hosted in the cloud and on the Internet.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Application Service Providers develop, host, and deliver software applications to customers over the Internet/cloud rather than requiring users to install and run the software locally, customers access the application remotely, typically via a web browser.
</details>

---

### 110. Vehicles that have Wi-Fi access and onboard computers require software patches and upgrades from the manufacturer.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Modern vehicles with Wi-Fi connectivity and onboard computers run software just like any connected device, and manufacturers need to issue patches and upgrades to fix bugs, address security vulnerabilities, and add functionality, much like smartphones or computers receive over-the-air updates.
</details>

---

### 111. Sharing in the data lifecycle means:
- A. Never share
- B. Sell without consent
- C. Enable reuse
- D. Share only with competitors

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Enable reuse**

*Intuition:* In the data lifecycle, the sharing stage refers to making data available for others to access, use, or build on, enabling reuse (internally across teams, or externally with partners or the public), typically under defined permissions or licenses. It's not about selling data, restricting it entirely, or limiting it to competitors.
</details>

---

### 112. Data localization drives investment in:
- A. Offshore storage
- B. Local data centers
- C. Manual record keeping
- D. Foreign data centers

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Local data centers**

*Intuition:* Data localization laws require certain data to be stored and processed within a country's own borders, so complying with them directly drives investment in local data center infrastructure rather than offshore or foreign facilities.
</details>

---

### 113. Many African countries lack:
- A. Internet access completely
- B. Interest in technology
- C. Skilled data-hosting professionals
- D. Basic electricity

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Skilled data-hosting professionals**

*Intuition:* A recognized barrier to building local data-hosting capacity across much of Africa is a shortage of professionals skilled in data center operations and hosting infrastructure, not a lack of internet access, interest in technology, or electricity in absolute terms.
</details>

---

### 114. Strict localization rules across Africa can:
- A. Remove competition
- B. Create one digital market
- C. Split Africa's digital market
- D. Reduce compliance costs

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Split Africa's digital market**

*Intuition:* If different African countries impose strict, inconsistent localization requirements, it creates barriers between national markets rather than unifying them, working against efforts like AfCFTA's Digital Trade Protocol to build an integrated continental digital economy.
</details>

---

### 115. The opposite of Privacy by Design is:
- A. Continuous privacy
- B. Proactive privacy
- C. Privacy added at the end
- D. Built-in privacy

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Privacy added at the end**

*Intuition:* Privacy by Design means privacy protections are built into a system from the start; its opposite is bolting privacy measures on only after the system is already built, as an afterthought rather than a foundational requirement.
</details>

---

### 116. According to the OSI security architecture, which term refers to something that has the potential to cause harm to a system?
- A. Threat
- B. Risk
- C. Vulnerability
- D. Attack

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Threat**

*Intuition:* Key Definitions in the OSI Security Architecture (ITU-T X.800 / RFC 4949): **Threat (A):** A potential for violation of security; any circumstance, capability, action, or event that has the **potential to cause harm** to an asset or system by breaching confidentiality, integrity, or availability. **Attack (D):** An assault on system security that derives from an intelligent threat. It is the **actual realization or execution** of a threat, a deliberate attempt to bypass security controls and exploit a system. **Vulnerability (C):** A **flaw or weakness** in a system’s design, implementation, operation, or management that could be exploited by a threat. **Risk (B):** The **expectation of loss**, calculated as the likelihood (probability) that a threat will exploit a vulnerability multiplied by the resulting impact/harm.
</details>

---

### 117. A router is a security appliance that is used to filter Internet Protocol (IP) packets and block unwanted packets.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* A router's primary function is to forward and route traffic between networks based on IP addresses, it is a networking device, not a security appliance. While routers can use access control lists to filter some traffic, that description more accurately fits a firewall, whose primary purpose is filtering and blocking unwanted packets for security.
</details>

---

### 118. A rail fence cipher is an example of a:
- A. Substitution technique
- B. Transposition technique
- C. Product cipher
- D. Stream cipher

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Transposition technique**

*Intuition:* Explanation: A **transposition cipher** works by rearranging (permuting) the order of plaintext characters rather than replacing them with other characters. The **rail fence cipher** is the simplest transposition technique, where plaintext letters are written diagonally across a number of "rails" and then read off row by row.
</details>

---

### 119. The one-time pad remains perfectly secure even if the same key is reused for multiple messages.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. False**

*Intuition:* Why It Is False: The One-Time Pad (OTP) offers **perfect secrecy** (information-theoretic security) _if and only if_ the key satisfies four strict conditions: 1. It is truly random. 2. It is at least as long as the message. 3. It is kept completely secret. 4. **It is never reused** (hence the name _one-time_). What Happens When a Key Is Reused (Two-Time Pad): If two plaintexts (P1​ and P2​) are encrypted with the same key (K): C1​=P1​⊕K C2​=P2​⊕K An eavesdropper can XOR the two ciphertexts together: C1​⊕C2​=(P1​⊕K)⊕(P2​⊕K)=P1​⊕P2​ The key cancels out completely, leaving the XOR of the two plaintexts (P1​⊕P2​). From there, attackers can recover both messages using statistical language analysis and **crib-dragging** techniques.
</details>

---

### 120. In the Caesar cipher, if the shift key is 3, the plaintext letter 'A' encrypts to:
- A. 'D'
- B. 'C'
- C. 'X'
- D. 'B'

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. 'D'**

*Intuition:* Explanation: The Caesar cipher encrypts each plaintext letter by shifting it down the alphabet by a fixed number of positions (the shift key, k=3). **Formula:** C≡(P+k)(mod26) **Step-by-step calculation:** If A=0, then C=(0+3)(mod26)=3 Mapping indices back to letters (0=A,1=B,2=C,3=D): A+1![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.522em"%20viewBox="0%200%20400000%20522"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M0%20241v40h399891c-47.3%2035.3-84%2078-110%20128%0A-16.7%2032-27.7%2063.7-33%2095%200%201.3-.2%202.7-.5%204-.3%201.3-.5%202.3-.5%203%200%207.3%206.7%2011%2020%0A%2011%208%200%2013.2-.8%2015.5-2.5%202.3-1.7%204.2-5.5%205.5-11.5%202-13.3%205.7-27%2011-41%2014.7-44.7%0A%2039-84.5%2073-119.5s73.7-60.2%20119-75.5c6-2%209-5.7%209-11s-3-9-9-11c-45.3-15.3-85%0A-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5%0A-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14%200-21%203.7-21%2011%200%202%202%2010.3%206%2025%2020.7%2083.3%2067%0A%20151.7%20139%20205zm0%200v40h399900v-40z"></path></svg>)​B+2![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.522em"%20viewBox="0%200%20400000%20522"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M0%20241v40h399891c-47.3%2035.3-84%2078-110%20128%0A-16.7%2032-27.7%2063.7-33%2095%200%201.3-.2%202.7-.5%204-.3%201.3-.5%202.3-.5%203%200%207.3%206.7%2011%2020%0A%2011%208%200%2013.2-.8%2015.5-2.5%202.3-1.7%204.2-5.5%205.5-11.5%202-13.3%205.7-27%2011-41%2014.7-44.7%0A%2039-84.5%2073-119.5s73.7-60.2%20119-75.5c6-2%209-5.7%209-11s-3-9-9-11c-45.3-15.3-85%0A-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5%0A-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14%200-21%203.7-21%2011%200%202%202%2010.3%206%2025%2020.7%2083.3%2067%0A%20151.7%20139%20205zm0%200v40h399900v-40z"></path></svg>)​C+3![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.522em"%20viewBox="0%200%20400000%20522"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M0%20241v40h399891c-47.3%2035.3-84%2078-110%20128%0A-16.7%2032-27.7%2063.7-33%2095%200%201.3-.2%202.7-.5%204-.3%201.3-.5%202.3-.5%203%200%207.3%206.7%2011%2020%0A%2011%208%200%2013.2-.8%2015.5-2.5%202.3-1.7%204.2-5.5%205.5-11.5%202-13.3%205.7-27%2011-41%2014.7-44.7%0A%2039-84.5%2073-119.5s73.7-60.2%20119-75.5c6-2%209-5.7%209-11s-3-9-9-11c-45.3-15.3-85%0A-40.5-119-75.5s-58.3-74.8-73-119.5c-4.7-14-8.3-27.3-11-40-1.3-6.7-3.2-10.8-5.5%0A-12.5-2.3-1.7-7.5-2.5-15.5-2.5-14%200-21%203.7-21%2011%200%202%202%2010.3%206%2025%2020.7%2083.3%2067%0A%20151.7%20139%20205zm0%200v40h399900v-40z"></path></svg>)​D
</details>

---

### 121. The Playfair cipher encrypts:
- A. Trigrams
- B. Whole words
- C. Digrams (pairs of letters)
- D. Single letters

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Digrams (pairs of letters)**

*Intuition:* How the Playfair Cipher Works: The Playfair cipher is a **polygraphic substitution cipher** that encrypts digraphs (pairs of two letters) instead of single letters, using a 5×5 grid populated with a keyword: 1. **Pairing:** The plaintext is split into two-letter pairs (digrams). If a pair contains duplicate letters (e.g., "EE"), a filler character like 'X' is inserted ("EX", "EX"). 2. **5x5 Matrix Rules:** **Same Row:** Each letter is replaced by the letter to its immediate right (wrapping around to the left). **Same Column:** Each letter is replaced by the letter immediately below it (wrapping around to the top). **Rectangle (Different Row & Column):** Each letter is replaced by the letter on the same row in the column occupied by the other letter. Why It Matters: By encrypting digrams rather than single letters, the Playfair cipher flattens the standard single-letter frequency distribution of the language (e.g., masking the high frequency of 'E' in English), making simple frequency analysis significantly harder.
</details>

---

### 122. Steganography differs from encryption in that it:
- A. Scrambles the content of a message
- B. Only works on digital images
- C. Requires a public key
- D. Conceals the very existence of a message

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Conceals the very existence of a message**

*Intuition:* Core Difference: Steganography vs. Cryptography |Feature|Steganography|Cryptography (Encryption)| |---|---|---| |**Primary Goal**|**Conceal existence**, hide the fact that a message is being sent at all.|**Conceal meaning**, scramble the message so unauthorized parties cannot read it.| |**Visibility**|Inconspicuous carrier file (e.g., an ordinary-looking image or audio file).|Obvious ciphertext (looks like random, scrambled data).| |**Attacker Awareness**|The adversary typically does not realize communication is occurring.|The adversary knows communication is happening but cannot decipher the contents.| Why the Other Options Are Incorrect: **A. Scrambles the content of a message:** This is the definition of **encryption** (cryptography), which transforms readable plaintext into unreadable ciphertext. **B. Only works on digital images:** Steganography can be applied across many mediums, including audio files, video streams, network packet headers, HTML whitespace, and even physical invisible ink. **C. Requires a public key:** Steganography does not require public-key cryptography; it relies on embedding algorithms and shared embedding keys (stego-keys).
</details>

---

### 123. In the Feistel cipher structure, the function applied within each round is called the ____ function.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **round**

*Intuition:* Completed Sentence: "In the Feistel cipher structure, the function applied within each round is called the **round** function." Key Properties of the Round Function (F): **Equation:** In each round i, the plaintext block is split into left (L) and right (R) halves: Li​=Ri−1​ Ri​=Li−1​⊕F(Ri−1​,Ki​) **Non-Invertibility Allowed:** The round function F does **not** need to be mathematically reversible (invertible). The structure of the Feistel network guarantees that decryption works identically to encryption (simply using the round subkeys Ki​ in reverse order) because the XOR operation (⊕) cancels itself out.
</details>

---

### 124. A key advantage of the Feistel structure is that:
- A. The same hardware or software can be used for both encryption and decryption
- B. It requires two different algorithms for encryption and decryption
- C. It cannot use a round function
- D. It only works with 64-bit blocks

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The same hardware or software can be used for both encryption and decryption**

*Intuition:* A Feistel cipher's decryption process is structurally identical to encryption, just run with the round subkeys in reverse order, so the same hardware or software implementation can perform both operations, with no need for a separate inverse cipher.
</details>

---

### 125. Which AES transformation cyclically shifts the rows of the state array?
- A. AddRoundKey
- B. SubBytes
- C. MixColumns
- D. ShiftRows

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. ShiftRows**

*Intuition:* How ShiftRows Works: In the AES state array (a 4×4 matrix of bytes), **ShiftRows** provides diffusion by cyclically shifting each row to the left by a different offset: **Row 0:** Not shifted (shifted by 0 bytes) **Row 1:** Cyclically shifted left by **1 byte** **Row 2:** Cyclically shifted left by **2 bytes** **Row 3:** Cyclically shifted left by **3 bytes** Overview of AES Round Transformations: **AddRoundKey (A):** Performs a bitwise XOR between the state matrix and the round key. **SubBytes (B):** A non-linear substitution step where each byte is replaced with another using a lookup table (S-box). **MixColumns (C):** A linear transformation that mixes the 4 bytes of each column using matrix multiplication in Galois Field GF(28). **ShiftRows (D):** The transposition step that cyclically shifts the state rows.
</details>

---

### 126. AES was originally designed and submitted to NIST under the name ____
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **Rijndael**

*Intuition:* Rijndael, designed by Joan Daemen and Vincent Rijmen, was the algorithm NIST selected through its open competition and standardized as AES.
</details>

---

### 127. The AES SubBytes transformation provides:
- A. Block chaining
- B. Nonlinear byte substitution using an S-box
- C. Key mixing
- D. Diffusion via row shifting

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. Nonlinear byte substitution using an S-box**

*Intuition:* How SubBytes Works: **Function:** It operates on each byte of the 4×4 state array independently. **Mechanism:** Each byte is replaced with its corresponding entry from a fixed substitution table called the **S-box** (Substitution Box). **Cryptographic Goal:** It provides **confusion** (non-linearity) in AES, ensuring that the relationship between the key/plaintext and ciphertext is mathematically complex and resistant to linear and differential cryptanalysis. The S-box is algebraically derived from taking the multiplicative inverse in GF(28) followed by an affine transformation. Overview of Other Transformations: **A (Block chaining):** A property of cipher modes of operation (such as CBC mode), not an AES internal round step. **C (Key mixing):** Handled by the **AddRoundKey** transformation (XORing the round key with the state). **D (Diffusion via row shifting):** Handled by the **ShiftRows** transformation.
</details>

---

### 128. In ECB mode, identical plaintext blocks always produce identical ciphertext blocks.
- A. True
- B. False

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. True**

*Intuition:* Why This Is True: In **Electronic Codebook (ECB)** mode, each fixed-size block of plaintext (Pi​) is encrypted independently using the exact same key (K): Ci​=EK​(Pi​) Because the encryption function is deterministic and involves no initialization vector (IV) or chaining with previous blocks, whenever two plaintext blocks are identical (Pa​=Pb​), their corresponding ciphertext blocks are guaranteed to be identical (Ca​=Cb​). Security Implication: This property makes ECB mode **insecure for encrypting structured data or images** (such as the well-known _ECB Penguin_ demonstration), because high-level patterns and repetitions in the plaintext remain clearly visible in the ciphertext.
</details>

---

### 129. Which mode of block cipher operation encrypts blocks independently without chaining, so identical plaintext blocks produce identical ciphertext blocks?
- A. ECB
- B. CBC
- C. CTR
- D. CFB

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. ECB**

*Intuition:* ECB (Electronic Codebook) encrypts each block independently under the same key with no dependency on previous blocks or an IV, so identical plaintext blocks always produce identical ciphertext blocks, which is exactly the pattern-leakage weakness that makes it unsafe for most data.
</details>

---

### 130. Blum Blum Shub (BBS) is an example of a PRNG built on:
- A. The Hill cipher
- B. The Playfair cipher
- C. Number-theoretic quadratic residue problems believed to be computationally hard
- D. The DES algorithm

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **C. Number-theoretic quadratic residue problems believed to be computationally hard**

*Intuition:* Key Mechanics of Blum Blum Shub (BBS): **Algorithm:** BBS generates pseudorandom bits via the recurrence relation: xn+1​=xn2​modM where M=p⋅q is a **Blum integer** (the product of two large prime numbers p and q, both congruent to 3mod4). **Security Foundation:** The output bits are provably secure under the assumption that the **Quadratic Residuosity Problem (QRP)** and integer factorization are computationally hard. Predicting the next bit is as hard as finding quadratic residues modulo M without knowing the factorization of M. Why the Other Options Are Incorrect: **A & B (Hill & Playfair):** These are classic polyalphabetic/polygraphic substitution ciphers based on matrix algebra and substitution tables, not secure PRNG primitives. **D (DES):** The Data Encryption Standard is a symmetric block cipher based on a Feistel network, not the foundation of the BBS generator.
</details>

---

### 131. The mathematical hard problem underlying RSA's security is the difficulty of ____ large composite numbers.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **factoring**

*Intuition:* Key Concept RSA relies on the **integer factorization problem**: **Easy direction:** Multiplying two large prime numbers p and q to compute n=p×q is computationally straightforward. **Hard direction:** Given only the large composite modulus n, finding the original prime factors p and q is computationally infeasible for sufficiently large keys (e.g., 2048-bit or 4096-bit RSA) using current classical algorithms.
</details>

---

### 132. The Euclidean algorithm is used primarily to compute:
- A. The greatest common divisor of two integers
- B. Discrete logarithms
- C. The prime factorization of a number
- D. Modular exponentiation directly

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The greatest common divisor of two integers**

*Intuition:* How the Euclidean Algorithm Works: The algorithm is based on the principle that the greatest common divisor (gcd) of two integers a and b (where a≥b) remains the same if a is replaced by the remainder of a divided by b: gcd(a,b)=gcd(b,amodb) This process is repeated iteratively until the remainder reaches zero; the last non-zero remainder is gcd(a,b). **Extended Euclidean Algorithm:** An extension that not only finds gcd(a,b), but also integers x and y such that ax+by=gcd(a,b) (Bézout's identity). This is widely used in cryptography (e.g., RSA) to compute **modular multiplicative inverses**. Why the Other Options Are Incorrect: **B. Discrete logarithms:** Computed using algorithms like the Baby-step Giant-step, Pollard's rho algorithm for logarithms, or the Index Calculus method. **C. Prime factorization:** Computed using integer factorization algorithms such as Pollard's ρ, Fermat's factorization method, or the General Number Field Sieve (GNFS). **D. Modular exponentiation:** Computed efficiently using the **Square-and-Multiply** (binary exponentiation) algorithm.
</details>

---

### 133. For two distinct primes p and q, phi(pq) equals:
- A. p+q
- B. (p-1)(q-1)
- C. pq
- D. p-q

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **B. (p-1)(q-1)**

*Intuition:* Mathematical Proof: Euler's totient function, ϕ(n), counts the number of integers in the range [1,n−1] that are coprime (relatively prime) to n. 1. **Multiplicative Property:** Euler's totient function is strictly multiplicative. For any two coprime integers a and b where gcd(a,b)=1: ϕ(ab)=ϕ(a)⋅ϕ(b) 2. **Prime Modulus:** For any prime number p, all integers from 1 to p−1 share no common factors with p other than 1. Therefore: ϕ(p)=p−1andϕ(q)=q−1 3. **Combined:** Since p and q are distinct primes, gcd(p,q)=1: ϕ(pq)=ϕ(p)⋅ϕ(q)=(p−1)(q−1) Cryptographic Significance: This identity forms the mathematical foundation of **RSA key generation**, where: The public modulus is n=p⋅q. The totient ϕ(n)=(p−1)(q−1) is used to compute the private decryption exponent d such that: d⋅e≡1(modϕ(n))
</details>

---

### 134. In cryptanalysis, a "known plaintext" attack assumes the analyst has:
- A. The ciphertext plus one or more known plaintext-ciphertext pairs
- B. No information at all
- C. Access to the decryption device to try chosen ciphertexts
- D. Only the ciphertext

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. The ciphertext plus one or more known plaintext-ciphertext pairs**

*Intuition:* Cryptanalysis Attack Models: **Known-Plaintext Attack (KPA) [Option A]:** The attacker has access to one or more pairs of original plaintext and its corresponding encrypted ciphertext. The goal is to discover the secret key or create an algorithm to decrypt future messages. **Ciphertext-Only Attack (COA) [Option D]:** The attacker has access **only** to a set of ciphertexts, with no corresponding plaintext or decryption capabilities. This is the weakest position for an attacker. **Chosen-Plaintext Attack (CPA):** The attacker can choose arbitrary plaintexts and obtain their corresponding ciphertexts from the encryption system (without knowing the key). **Chosen-Ciphertext Attack (CCA) [Option C]:** The attacker can choose arbitrary ciphertexts and obtain their decrypted plaintexts from a decryption oracle/device.
</details>

---

### 135. In Diffie-Hellman key exchange, both parties agree in advance on a large prime p and a ____ of that prime's multiplicative group.
<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **generator**

*Intuition:* Completed Sentence: "In Diffie-Hellman key exchange, both parties agree in advance on a large prime p and a **generator** of that prime's multiplicative group." Brief Context: **Generator (g):** An element of the cyclic multiplicative group Zp∗​ whose powers modulo p generate every non-zero element in the group. **Why it matters:** Using a generator ensures that the generated public keys span the entire group size (p−1), maximizing the search space and making the Discrete Logarithm Problem (DLP) computationally infeasible to solve.
</details>

---

### 136. The security of ECC rests on the difficulty of the:
- A. Elliptic curve discrete logarithm problem
- B. Subset sum problem
- C. Knapsack problem
- D. Integer factorization problem

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **A. Elliptic curve discrete logarithm problem**

*Intuition:* What is the ECDLP (Elliptic Curve Discrete Logarithm Problem)? In Elliptic Curve Cryptography (ECC): Given an elliptic curve over a finite field, a base point P, and a scalar multiple point Q such that: Q=kP=k times![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.548em"%20viewBox="0%200%20400000%20548"%20preserveAspectRatio="xMinYMin%20slice"><path%20d="M0%206l6-6h17c12.688%200%2019.313.3%2020%201%204%204%207.313%208.3%2010%2013%0A%2035.313%2051.3%2080.813%2093.8%20136.5%20127.5%2055.688%2033.7%20117.188%2055.8%20184.5%2066.5.688%0A%200%202%20.3%204%201%2018.688%202.7%2076%204.3%20172%205h399450v120H429l-6-1c-124.688-8-235-61.7%0A-331-161C60.687%20138.7%2032.312%2099.3%207%2054L0%2041V6z"></path></svg>)![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.548em"%20viewBox="0%200%20400000%20548"%20preserveAspectRatio="xMidYMin%20slice"><path%20d="M199572%20214%0Ac100.7%208.3%20195.3%2044%20280%20108%2055.3%2042%20101.7%2093%20139%20153l9%2014c2.7-4%205.7-8.7%209-14%0A%2053.3-86.7%20123.7-153%20211-199%2066.7-36%20137.3-56.3%20212-62h199568v120H200432c-178.3%0A%2011.7-311.7%2078.3-403%20201-6%208-9.7%2012-11%2012-.7.7-6.7%201-18%201s-17.3-.3-18-1c-1.3%200%0A-5-4-11-12-44.7-59.3-101.3-106.3-170-141s-145.3-54.3-229-60H0V214z"></path></svg>)![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="400em"%20height="0.548em"%20viewBox="0%200%20400000%20548"%20preserveAspectRatio="xMaxYMin%20slice"><path%20d="M399994%200l6%206v35l-6%2011c-56%20104-135.3%20181.3-238%20232-57.3%0A%2028.7-117%2045-179%2050H-300V214h399897c43.3-7%2081-15%20113-26%20100.7-33%20179.7-91%20237%0A-174%202.7-5%206-9%2010-13%20.7-1%207.3-1%2020-1h17z"></path></svg>)P+P+⋯+P​​ It is computationally easy to compute Q given k and P (via point addition and doubling algorithms). However, given only P and Q, finding the integer k (the private key) is the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**, which is computationally intractable for sufficiently large curve parameters. Because the best-known algorithms for solving ECDLP require fully exponential time (unlike classical DLP or integer factorization, which have sub-exponential algorithms like GNFS), ECC provides comparable security to RSA with much smaller key sizes (e.g., a 256-bit ECC key offers roughly equivalent security to a 3072-bit RSA key). Why the Other Options Are Incorrect: **B & C (Subset sum / Knapsack problem):** The basis for early lattice/combinatorial public-key schemes such as the **Merkle–Hellman Knapsack Cryptosystem** (most variants of which were later broken). **D (Integer factorization problem):** The mathematical foundation for **RSA** and the **Rabin** cryptosystem.
</details>

---

### 137. Rotor machines historically achieve strong security by:
- A. Using a single fixed substitution
- B. Encrypting only vowels
- C. Using modular exponentiation
- D. Cascading multiple substitution ciphers that change with each keystroke

<details>
<summary>Reveal Answer</summary>

**Correct Answer:** **D. Cascading multiple substitution ciphers that change with each keystroke**

*Intuition:* How Rotor Machines Work: **Cascaded Substitution:** A rotor machine (such as the **Enigma**, **Typex**, or **SIGABA**) contains several wired cylinders (rotors) positioned in series. Each individual rotor acts as an independent monoalphabetic substitution cipher. **Dynamic Stepping Mechanism:** When a key is pressed, an electrical current flows through the series of rotors to produce the ciphertext letter. Before or after the keystroke, one or more rotors step (rotate) by one position. **Polyalphabetic Complexity:** Rotating the cylinders alters the internal wiring pathways for the next character, creating a dynamically changing compound substitution cipher with an extremely long repetition period (e.g., 263=17,576 states for a basic 3-rotor setup, and even higher with stepping odometers and plugboards). Why the Other Options Are Incorrect: **A (Single fixed substitution):** Describes a simple **monoalphabetic substitution cipher** (such as the Caesar cipher or a random substitution alphabet), which is easily broken using frequency analysis. **B (Encrypting only vowels):** Historically untrue; rotor machines encrypted all standard alphabet characters. **C (Modular exponentiation):** The mathematical primitive used in modern public-key cryptography (e.g., RSA, Diffie-Hellman), not mechanical rotor devices.
</details>

---
