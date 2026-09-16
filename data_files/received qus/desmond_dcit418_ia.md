desmond_dcit418_ia.md

TODO: format this md well.then add to ia_offiste.md with necessary analysis, before outputting the clean md and loading into app. 

DCIT418 AI 
1. What distinguishes a symmetric cipher from an asymmetric cipher?  
A. It uses multiple keys for encryption  
B. It uses the same key for both encryption and decryption  
C. It relies on prime factorization  
D. It requires a public key infrastructure  
B. It uses the same key for both encryption and decryption    
2. How does the Kerberos authentication protocol ensure secure user authentication?  
A. It uses public-key cryptography exclusively  
B. It relies on a trusted key distribution center with symmetric encryption  
C. It avoids timestamps for security  
D. It requires no session keys  
B. It relies on a trusted key distribution center with symmetric encryption    
3. How does the security of a linear congruential generator (LCG) as a pseudorandom number 
generator compare to one based on a block cipher?  
A. LCG is more secure due to its simplicity  
B. LCG is predictable with known outputs; block cipher PRNGs resist prediction  
C. LCG requires no seed; block ciphers do  
D. LCG is faster but less flexible  
B. LCG is predictable with known outputs; block cipher PRNGs resist prediction    
4. How does Fermat’s Little Theorem ensure the correctness of RSA’s encryption and decryption 
process?  
A. It generates prime numbers for the modulus  
B. It guarantees modular exponentiation returns the original message  
C. It simplifies discrete logarithm computation  
D. It ensures collision resistance in signatures  
B. It guarantees modular exponentiation returns the original message    
5. Evaluate the suitability of RC4 for modern cryptographic applications.  
A. It is ideal due to its speed and simplicity  
B. It is used in AES-based systems  
C. It is vulnerable to biases in keystream, making it outdated  
D. It is resistant to quantum attacks  
C. It is vulnerable to biases in keystream, making it outdated    
6. Why is XTS-AES mode’s use of a tweak value critical for disk encryption, and what subtle 
vulnerability remains?  
A. Tweak ensures key secrecy; vulnerable to brute-force attacks  
B. Tweak ensures unique ciphertext per sector; vulnerable to chosen-plaintext attacks  
C. Tweak simplifies decryption; vulnerable to key recovery  
D. Tweak eliminates padding; vulnerable to padding oracle attacks  
B. Tweak ensures unique ciphertext per sector; vulnerable to chosen-plaintext attacks    
7. How does the Encapsulating Security Payload (ESP) in IPsec differ from the Authentication 
Header (AH)?  
A. ESP provides authentication only, AH provides confidentiality  
B. ESP provides confidentiality and authentication, AH provides authentication only  
C. ESP is less secure than AH D. ESP does not support tunnel mode  
B. ESP provides confidentiality and authentication, AH provides authentication only    
8. How does Kerberos’ use of tickets enhance security over simple symmetric key distribution? 
A. It eliminates the need for a key distribution center  
B. It provides time-limited, authenticated session keys  
C. It uses asymmetric encryption exclusively  
D. It avoids timestamps  
B. It provides time-limited, authenticated session keys    
9. Why is DomainKeys Identified Mail (DKIM) insufficient for end-to-end email security 
compared to PGP?  
A. DKIM encrypts the email content  
B. DKIM verifies the sender’s domain, not the message content or recipient  
C. DKIM requires no signatures  
D. DKIM is more secure than PGP  
B. DKIM verifies the sender’s domain, not the message content or recipient    
10. Synthesize the security implications of SHA-3’s sponge construction versus SHA-2’s 
Merkle-Damgård for preimage resistance.  
A. SHA-3 is less resistant; sponge simplifies attacks  
B. SHA-3’s capacity enhances preimage resistance; Merkle-Damgård is weaker to extensions  
C. SHA-2 avoids padding; SHA-3 is vulnerable  
D. Both are equally resistant; no differences exist  
B. SHA-3’s capacity enhances preimage resistance; Merkle-Damgård is weaker to 
extensions    
11. Why is RC4’s key scheduling algorithm (KSA) a point of vulnerability in its design?  
A. It uses a fixed key size  
B. It produces biased initial keystream bytes, enabling attacks  
C. It avoids pseudorandom number generation  
D. It requires excessive memory  
B. It produces biased initial keystream bytes, enabling attacks    
12. Synthesize why a triple transposition cipher might still fail against a chosen-plaintext attack 
compared to a modern block cipher.  
A. It uses non-linear substitution; resistant to chosen-plaintext attacks  
B. It only reorders plaintext, preserving patterns; block ciphers use confusion and diffusion  
C. It employs modular arithmetic; vulnerable to key recovery  
D. It reduces key space; resistant to cryptanalysis  
B. It only reorders plaintext, preserving patterns; block ciphers use confusion and diffusion 
13. How does the Schnorr Digital Signature Scheme differ from the NIST Digital Signature 
Algorithm?  
A. Schnorr uses elliptic curves, NIST does not  
B. Schnorr is more efficient with shorter signatures  
C. Schnorr is less secure than NIST  
D. Schnorr relies on prime factorization  
B. Schnorr is more efficient with shorter signatures    
14. Why were rotor machines like the Enigma considered complex for their time?  
A. They used asymmetric encryption  
B. They implemented dynamic polyalphabetic substitution with multiple rotors  
C. They relied on finite field arithmetic  
D. They generated true random numbers  
B. They implemented dynamic polyalphabetic substitution with multiple rotors    
15. Why is HMAC’s use of an outer hash function critical for preventing key recovery attacks? 
A. It simplifies computation; reduces security  
B. It processes the key with the message, obscuring the inner hash output  
C. It eliminates the inner hash; increases vulnerability  
D. It reduces key size; enhances efficiency  
B. It processes the key with the message, obscuring the inner hash output    
16. Evaluate the security trade-offs of TLS 1.3’s removal of RSA key exchange compared to TLS 
1.2.  
A. TLS 1.3 is less secure; RSA is robust  
B. TLS 1.3 enhances forward secrecy by using ephemeral keys; RSA lacks forward secrecy  
C. TLS 1.3 avoids key exchange; TLS 1.2 requires it  
D. TLS 1.3 simplifies encryption; TLS 1.2 is more complex  
B. TLS 1.3 enhances forward secrecy by using ephemeral keys; RSA lacks forward secrecy 
17. Evaluate the Enigma machine’s use of multiple rotors versus a single rotor, focusing on its 
impact on key space and cryptanalysis.  
A. Single rotor increases key space; simplifies cryptanalysis  
B. Multiple rotors exponentially increase key space; complicate pattern detection  
C. Multiple rotors reduce security; simplify decryption  
D. Single rotor ensures randomness; resists frequency analysis  
B. Multiple rotors exponentially increase key space; complicate pattern detection    
18. What is the role of the ShiftRows transformation in AES?  
A. It performs non-linear substitution  
B. It permutes bytes to enhance diffusion  
C. It generates round keys  
D. It compresses the state matrix  
B. It permutes bytes to enhance diffusion    
19. Why is the use of a nonce in GCM mode critical for security?  
A. It replaces the encryption key  
B. It ensures unique ciphertext, preventing reuse attacks  
C. It simplifies authentication  
D. It eliminates the need for a counter  
B. It ensures unique ciphertext, preventing reuse attacks    
20. Synthesize the challenges of symmetric key distribution using asymmetric encryption in a 
post-quantum cryptography context.  
A. Asymmetric encryption is immune to quantum attacks; simplifies distribution  
B. Asymmetric encryption is vulnerable to quantum attacks; requires quantum-resistant 
algorithms  
C. Symmetric keys are quantum-resistant; asymmetric is unnecessary  
D. Quantum attacks simplify key distribution; no challenges exist  
B. Asymmetric encryption is vulnerable to quantum attacks; requires quantum-resistant 
algorithms    
21. Synthesize the trade-offs of DES’s 16-round Feistel structure versus a hypothetical 32-round 
structure in terms of security and performance.  
A. 32 rounds reduce security; improve performance  
B. 32 rounds enhance security against cryptanalysis; significantly degrade performance  
C. 16 rounds are insufficient for diffusion; 32 rounds are optimal  
D. Both provide equivalent security; 16 rounds are faster  
B. 32 rounds enhance security against cryptanalysis; significantly degrade performance    
22. Evaluate the impact of RC4’s state permutation weaknesses on its use in early SSL/TLS 
protocols.  
A. State permutations ensure security; SSL/TLS was unaffected  
B. Weak initial permutations led to biased keystreams, enabling attacks like BEAST  
C. State permutations simplified decryption; SSL/TLS was secure  
D. Weak permutations increased key space; SSL/TLS was robust  
B. Weak initial permutations led to biased keystreams, enabling attacks like BEAST    
23. Why is the Miller-Rabin algorithm used in primality testing for RSA?  
A. It generates random numbers  
B. It efficiently determines if a number is likely prime  
C. It computes discrete logarithms  
D. It ensures collision resistance  
B. It efficiently determines if a number is likely prime    
25. How does AES’s AddRoundKey transformation ensure security without introducing non
linearity?  
A. It permutes the state matrix  
B. It XORs the state with a round key, ensuring key-dependent encryption  
C. It substitutes bytes non-linearly  
D. It compresses the state matrix  
B. It XORs the state with a round key, ensuring key-dependent encryption    
26. Why is the security of a block cipher-based PRNG dependent on the cipher’s key strength? 
A. Weak keys simplify decryption  
B. The PRNG’s output predictability relies on the cipher’s resistance to attacks  
C. The key determines the block size  
D. The PRNG avoids key usage  
B. The PRNG’s output predictability relies on the cipher’s resistance to attacks    
27. Evaluate why AES’s omission of MixColumns in the final round simplifies decryption 
without compromising security.  
A. It reduces diffusion; weakens security  
B. It allows inverse operations to align symmetrically; maintains diffusion from prior rounds  
C. It eliminates non-linearity; enhances security  
D. It simplifies key expansion; reduces performance  
B. It allows inverse operations to align symmetrically; maintains diffusion from prior 
rounds    
28.Why is the AES key expansion’s use of round constants critical for preventing slide attacks? 
A. Round constants simplify key generation; increase vulnerability  
B. Round constants break key symmetry, preventing repetitive patterns  
C. Round constants reduce key size; simplify cryptanalysis  
D. Round constants eliminate non-linearity; enhance security  
B. Round constants break key symmetry, preventing repetitive patterns    
29. Evaluate the advantage of Kerberos over remote user authentication using asymmetric 
encryption.  
A. Kerberos is less secure but faster  
B. Kerberos requires no trusted third party  
C. Kerberos uses symmetric encryption for efficiency in trusted environments  
D. Kerberos supports elliptic curve cryptography  
C. Kerberos uses symmetric encryption for efficiency in trusted environments    
30. Why might a transposition cipher be less secure than a substitution cipher when used alone? 
A. It uses a smaller key space  
B. It preserves letter frequency, making it vulnerable to frequency analysis  
C. It requires complex hardware  
D. It cannot be combined with other ciphers  
B. It preserves letter frequency, making it vulnerable to frequency analysis    
31.Why is S/MIME’s reliance on X.509 certificates both a strength and a limitation?  
A. It simplifies key management; limits scalability  
B. It ensures trust via CAs; requires complex certificate management  
C. It avoids certificates; reduces security  
D. It eliminates encryption; simplifies implementation  
B. It ensures trust via CAs; requires complex certificate management    
32. Why is the Output Feedback (OFB) mode suitable for error-prone channels?  
A. It self-synchronizes like CFB  
B. It generates a keystream independently of ciphertext  
C. It requires no initialization vector  
D. It is faster than CTR mode  
B. It generates a keystream independently of ciphertext    
33. How does IEEE 802.11i’s use of the Counter Mode with CBC-MAC Protocol (CCMP) 
improve security over TKIP?  
A. TKIP uses stronger encryption; CCMP is faster  
B. CCMP uses AES with authenticated encryption; TKIP uses weaker RC4  
C. CCMP avoids key management; TKIP requires it  
D. CCMP is less secure; TKIP supports modern devices  
B. CCMP uses AES with authenticated encryption; TKIP uses weaker RC4    
34. How does the AES key expansion process ensure security?  
A. It compresses the key to reduce size  
B. It generates unique round keys from the original key  
C. It encrypts the key with a hash function  
D. It uses a single key for all rounds  
B. It generates unique round keys from the original key    
35.Why is the use of a counter in CTR mode critical for its security, and what happens if the 
counter repeats?  
A. Counter simplifies decryption; repetition has no impact  
B. Counter ensures unique keystreams; repetition causes keystream reuse, enabling XOR attacks 
C. Counter increases key size; repetition enhances security  
D. Counter eliminates IVs; repetition simplifies cryptanalysis  
B. Counter ensures unique keystreams; repetition causes keystream reuse, enabling XOR 
attacks    
36. How does Fermat’s Little Theorem support RSA encryption?  
A. It generates random numbers  
B. It ensures modular exponentiation properties for key generation  
C. It computes discrete logarithms  
D. It defines elliptic curves  
B. It ensures modular exponentiation properties for key generation    
37. Why is the X.509 certificate revocation list (CRL) critical in PKI?  
A. It generates new certificates  
B. It tracks compromised or expired certificates  
C. It encrypts private keys  
D. It authenticates users directly  
B. It tracks compromised or expired certificates    
38. Why is Kerberos’ ticket-granting ticket (TGT) mechanism vulnerable to key compromise at 
the Key Distribution Center (KDC)?  
A. TGT uses no encryption; easily intercepted  
B. TGT relies on the KDC’s master key; compromise leaks all session keys  
C. TGT avoids timestamps; increases security  
D. TGT simplifies authentication; reduces vulnerability  
B. TGT relies on the KDC’s master key; compromise leaks all session keys    
39. Why is the X.509 certificate’s hierarchical trust model critical for PKI scalability?  
A. It eliminates the need for revocation lists  
B. It enables trusted certificate authorities to delegate trust efficiently  
C. It simplifies key generation  
D. It avoids public key distribution  
B. It enables trusted certificate authorities to delegate trust efficiently    
40. Why is the AES key schedule designed to prevent related-key attacks?  
A. It uses a linear transformation only  
B. It incorporates non-linear operations to diversify round keys  
C. It reduces the number of rounds  
D. It avoids key expansion  
B. It incorporates non-linear operations to diversify round keys    
41. Why is the Schnorr signature scheme considered efficient for elliptic curve cryptography?  
A. It uses larger keys than ECDSA  
B. It produces shorter signatures with simpler computations  
C. It avoids elliptic curve arithmetic  
D. It requires no hash functions  
B. It produces shorter signatures with simpler computations    
42.Why is the AES SubBytes transformation considered non-linear?  
A. It shifts rows of the state matrix  
B. It uses an S-box to map inputs to outputs in a non-linear way  
C. It performs modular exponentiation  
D. It mixes columns linearly  
B. It uses an S-box to map inputs to outputs in a non-linear way    
43. How does IEEE 802.11i (WPA2) improve security over WEP for wireless networks?  
A. WEP uses stronger encryption  
B. WPA2 uses AES and robust key management, unlike WEP’s weak RC4  
C. WPA2 avoids authentication  
D. WPA2 requires no key exchange  
B. WPA2 uses AES and robust key management, unlike WEP’s weak RC4    
44. Evaluate the role of rotor machines like the Enigma in modern cryptography.  
A. They are widely used due to their simplicity  
B. They are secure against quantum attacks  
C. They are obsolete but historically significant for complex substitution  
D. They are used in stream ciphers like RC4  
C. They are obsolete but historically significant for complex substitution    
B. It computes modular inverses for key pair creation in RSA and Elgamal    
45. Evaluate the role of Pretty Good Privacy (PGP) in email security compared to S/MIME.  
A. PGP is less secure but easier to implement  
B. PGP uses a web-of-trust model, S/MIME relies on certificate authorities  
C. PGP avoids encryption entirely  
D. PGP is incompatible with MIME  
B. PGP uses a web-of-trust model, S/MIME relies on certificate authorities    
46. How does the X.509 certificate’s Online Certificate Status Protocol (OCSP) improve upon 
Certificate Revocation Lists (CRLs)?  
A. OCSP stores all revoked certificates; CRLs are real-time  
B. OCSP provides real-time revocation status; CRLs are periodically updated  
C. OCSP avoids certificates; CRLs require them  
D. OCSP is less secure; CRLs are more efficient  
B. OCSP provides real-time revocation status; CRLs are periodically updated    
47. How does Federated Identity Management improve user authentication across domains?  
A. It uses symmetric encryption only  
B. It allows single sign-on with trusted identity providers  
C. It eliminates the need for certificates  
D. It requires manual key exchange  
B. It allows single sign-on with trusted identity providers    
48. In GF(2^8), why is the irreducible polynomial x^8 + x^4 + x^3 + x + 1 used in AES?  
A. It simplifies key expansion  
B. It defines the field’s arithmetic for byte operations  
C. It reduces the key size  
D. It ensures reversibility of encryption  
B. It defines the field’s arithmetic for byte operations    
49. How does the Schnorr Digital Signature Scheme’s use of linear combinations improve 
efficiency over Elgamal? 
A. It increases signature size; reduces computation  
B. It reduces signature size and exponentiations via linear combinations  
C. It avoids discrete logarithms; increases key size  
D. It simplifies verification; reduces security  
B. It reduces signature size and exponentiations via linear combinations    
50. Synthesize the benefit of using elliptic curve arithmetic in cryptographic systems.  
A. It simplifies key generation  
B. It provides strong security with smaller key sizes  
C. It eliminates the need for hash functions  
D. It supports symmetric encryption  
B. It provides strong security with smaller key sizes    
51. Why is the X.509 certificate format critical for public-key infrastructure (PKI)?  
A. It encrypts symmetric keys  
B. It generates pseudorandom numbers  
C. It standardizes public key and identity binding  
D. It authenticates users directly  
52. In elliptic curve cryptography, why is the choice of curve parameters critical for security, and 
what is a subtle risk?  
A. Parameters simplify arithmetic; risk of weak keys  
B. Parameters define the curve’s security; risk of weak curves with low order points  
C. Parameters reduce key size; risk of brute-force attacks  
D. Parameters ensure reversibility; risk of key leakage  
B. Parameters define the curve’s security; risk of weak curves with low order points    
53. Evaluate the trade-offs of using ECDSA over RSA-PSS for digital signatures in resource
constrained devices.  
A. ECDSA requires larger keys, reducing efficiency  
B. ECDSA uses smaller keys, improving efficiency but requiring curve selection  
C. ECDSA avoids hash functions, simplifying signatures  
D. ECDSA is less secure than RSA-PSS  
B. ECDSA uses smaller keys, improving efficiency but requiring curve selection    
54. How does the Schnorr signature scheme’s use of a random nonce affect its security?  
A. It simplifies verification; reduces security  
B. It ensures signature uniqueness; nonce reuse can leak the private key  
C. It avoids hash functions; eliminates vulnerabilities  
D. It increases signature size; enhances security  
B. It ensures signature uniqueness; nonce reuse can leak the private key    
55. Why is HMAC resistant to length extension attacks, unlike a plain hash function?  
A. It uses a smaller hash output  
B. It incorporates a secret key and processes the input twice  
C. It avoids padding the input  
D. It requires no hash function  
B. It incorporates a secret key and processes the input twice    
56. Why is Triple DES (3DES) slower than AES for equivalent security?  
A. It uses a smaller block size  
B. It requires asymmetric keys  
C. It applies DES three times, increasing computational overhead  
D. It lacks finite field arithmetic  
C. It applies DES three times, increasing computational overhead    
57. Evaluate the security implications of using a weak elliptic curve with a low-order point in 
ECC.  
A. It increases efficiency; maintains security  
B. It allows attacks like invalid curve attacks, compromising the private key  
C. It simplifies arithmetic; eliminates vulnerabilities  
D. It reduces key size; enhances security  
B. It allows attacks like invalid curve attacks, compromising the private key    
58. How does SHA-3’s capacity parameter affect its security against collision attacks?  
A. Higher capacity reduces output size; decreases security  
B. Higher capacity increases resistance to collision attacks; reduces performance  
C. Capacity has no impact on collisions  
D. Lower capacity enhances security; improves performance  
B. Higher capacity increases resistance to collision attacks; reduces performance    
59. Evaluate the trade-offs of GCM’s use of a 96-bit nonce versus a random IV in terms of 
security and performance.  
A. Random IV is faster; less secure  
B. 96-bit nonce enables efficient counter increments; nonce reuse compromises security  
C. Random IV eliminates nonce reuse; slower performance  
D. 96-bit nonce simplifies authentication; no trade-offs  
B. 96-bit nonce enables efficient counter increments; nonce reuse compromises security    
60. What is a key requirement for a cryptographic hash function to be secure?  
A. It must be reversible  
B. It must provide preimage resistance  
C. It must use a small output size  
D. It must avoid modular arithmetic  
B. It must provide preimage resistance    
61. How does Cipher Block Chaining (CBC) mode’s dependence on an initialization vector (IV) 
introduce a subtle vulnerability compared to Counter (CTR) mode?  
A. CBC’s IV is deterministic; CTR’s counter is random  
B. CBC’s IV must be unpredictable; reuse enables chosen-ciphertext attacks  
C. CBC avoids IVs; CTR requires them  
D. CBC’s IV simplifies decryption; CTR complicates it  
B. CBC’s IV must be unpredictable; reuse enables chosen-ciphertext attacks    
62. How does the Elliptic Curve Digital Signature Algorithm (ECDSA) compare to RSA-PSS in 
terms of efficiency?  
A. ECDSA is slower but more secure  
B. ECDSA uses smaller keys for equivalent security, improving efficiency  
C. ECDSA requires larger keys  
D. ECDSA is incompatible with hash functions  
B. ECDSA uses smaller keys for equivalent security, improving efficiency    
64. Synthesize the role of HMAC in ensuring message integrity and authentication.  
A. It encrypts the message content  
B. It combines a hash function with a secret key to verify both  
C. It generates pseudorandom numbers  
D. It replaces digital signatures  
B. It combines a hash function with a secret key to verify both    
65. Evaluate the impact of quantum computing on the security of RSA versus elliptic curve 
cryptography.  
A. RSA is resistant to quantum attacks; ECC is vulnerable  
B. RSA is vulnerable to Shor’s algorithm; ECC requires larger keys for resistance  
C. Both are equally resistant to quantum attacks  
D. Neither is affected by quantum computing  
B. RSA is vulnerable to Shor’s algorithm; ECC requires larger keys for resistance    
66. In AES, how does the MixColumns transformation contribute to diffusion, and why is it 
absent in the final round?  
A. It substitutes bytes; included in all rounds  
B. It mixes bytes across columns; omitted in the final round to simplify decryption  
C. It generates round keys; always included  
D. It compresses the state; omitted for speed  
B. It mixes bytes across columns; omitted in the final round to simplify decryption    
67. In modular arithmetic, what is the significance of the modulus in GF(p)?  
A. It defines the block size  
B. It specifies the prime number for the finite field  
C. It determines the key length  
D. It sets the polynomial degree  
B. It specifies the prime number for the finite field    
68. Why is the DES S-box design resistant to differential cryptanalysis, and what subtle flaw still 
exists?  
A. It uses linear mappings; vulnerable to linear cryptanalysis  
B. It employs non-linear mappings with specific difference distribution tables; vulnerable to 
linear cryptanalysis  
C. It avoids substitution; susceptible to brute-force attacks  
D. It uses fixed permutations; vulnerable to key recovery  
B. It employs non-linear mappings with specific difference distribution tables; vulnerable 
to linear cryptanalysis    
69. Why is collision resistance a critical requirement for cryptographic hash functions?  
A. It ensures reversible hashing  
B. It prevents two different inputs from producing the same hash  
C. It reduces computational complexity  
D. It eliminates the need for keys  
B. It prevents two different inputs from producing the same hash    
70. How does the use of modular exponentiation in RSA differ from its use in Diffie-Hellman? 
A. RSA uses it for key exchange, Diffie-Hellman for encryption  
B. RSA uses it for encryption/decryption, Diffie-Hellman for key agreement  
C. RSA avoids modular exponentiation  
D. Diffie-Hellman requires smaller exponents  
B. RSA uses it for encryption/decryption, Diffie-Hellman for key agreement    
71.What distinguishes IEEE 802.1X from the Extensible Authentication Protocol (EAP)?  
A. 802.1X is a cryptographic algorithm, EAP is a framework  
B. 802.1X is a port-based access control, EAP is an authentication framework  
C. 802.1X is less secure than EAP  
D. 802.1X does not support wireless networks  
B. 802.1X is a port-based access control, EAP is an authentication framework    
72. How does a rail fence cipher differ from a columnar transposition cipher?  
A. Rail fence uses substitution, columnar uses permutation  
B. Rail fence arranges letters in a zigzag pattern, columnar uses a grid  
C. Rail fence is more secure than columnar  
D. Rail fence requires a numerical key  
B. Rail fence arranges letters in a zigzag pattern, columnar uses a grid    
73. Evaluate the role of IPsec’s Internet Key Exchange (IKE) in establishing secure VPNs.  
A. It encrypts data directly  
B. It negotiates security associations and keys for secure communication  
C. It replaces ESP and AH  
D. It simplifies packet processing  
B. It negotiates security associations and keys for secure communication    
74. In AES, why is the absence of MixColumns in the final round critical for decryption 
efficiency?  
A. It simplifies encryption; increases decryption complexity  
B. It allows the inverse operation to start with AddRoundKey, simplifying decryption  
C. It reduces security; simplifies key expansion  
D. It eliminates diffusion; speeds up encryption  
B. It allows the inverse operation to start with AddRoundKey, simplifying decryption    
75. Evaluate the security implications of using CCM versus GCM for authenticated encryption in 
constrained environments.  
A. CCM is faster; less secure than GCM  
B. CCM is simpler but less efficient due to sequential processing; GCM supports parallelism  
C. CCM avoids authentication; GCM requires it  
D. CCM uses larger keys; GCM is more secure  
B. CCM is simpler but less efficient due to sequential processing; GCM supports 
parallelism    
76. In modular arithmetic, why is the use of a prime modulus in GF(p) essential for 
cryptographic operations, and what happens with a composite modulus?  
A. Composite modulus increases security; ensures inverses  
B. Prime modulus ensures unique inverses; composite modulus allows factorization, breaking 
security  
C. Prime modulus reduces key space; composite modulus is secure  
D. Composite modulus simplifies arithmetic; enhances security  
B. Prime modulus ensures unique inverses; composite modulus allows factorization, 
breaking security    
77. In elliptic curve cryptography, why is the choice of a non-singular curve critical, and what 
subtle attack exploits a singular curve?  
A. Singular curves increase efficiency; no attacks exist  
B. Non-singular curves ensure group structure; singular curves enable point factorization attacks 
C. Singular curves enhance security; resist cryptanalysis  
D. Non-singular curves simplify arithmetic; vulnerable to key recovery  
B. Non-singular curves ensure group structure; singular curves enable point factorization 
attacks    
78. How does the structure of a finite field in GF(2^8) support AES operations?  
A. It simplifies key expansion  
B. It enables efficient polynomial arithmetic for S-boxes  
C. It reduces key size  
D. It avoids modular arithmetic  
B. It enables efficient polynomial arithmetic for S-boxes    
77. How does Kerberos’ replay cache prevent unauthorized access in authentication?  
A. It encrypts session keys  
B. It detects and blocks reused authentication tickets  
C. It generates random timestamps  
D. It eliminates the need for a KDC  
B. It detects and blocks reused authentication tickets   
: 
78. Synthesize the security benefits of GCM over CCM for authenticated encryption.  
A. GCM is slower but more secure  
B. GCM supports parallel processing and better performance with equivalent security  
C. GCM avoids authentication tags  
D. GCM requires no counter mechanism  
B. GCM supports parallel processing and better performance with equivalent security    