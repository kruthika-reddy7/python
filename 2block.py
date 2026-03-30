from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
# Generate an ECC private key
private_key = ec.generate_private_key(ec.SECP256R1()) # Using the secp256r1 curve
# Get the public key from the private key
public_key = private_key.public_key()
# Message to be signed
message = b"Secure IoT Data Transmission"
# Sign the message
signature = private_key.sign(
message,
ec.ECDSA(hashes.SHA256()) # ECDSA with SHA-256
Page | 22
)
# Verify the signature
try:
public_key.verify(
signature,
message,
ec.ECDSA(hashes.SHA256())
)
print("Signature is valid. Message is authentic!")
except:
print("Signature verification failed. Data integrity compromised!")