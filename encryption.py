
from cryptography.fernet import Fernet

def encrypt(key,input):
    key = keygen(key)
    message = input
    fernet = Fernet(key)
    encMessage = fernet.encrypt(message.encode())
    #print("original string: ", message)
    #print("encrypted string: ", encMessage)
    return encMessage

def decrypt(key,input):
    key = keygen(key)
    fernet = Fernet(key)
    decMessage = fernet.decrypt(input).decode()
    #print("decrypted string: ", decMessage)
    return decMessage

def keygen(key):

    import hashlib
    client=key
    result = hashlib.sha256(client.encode()) 
    final_hash=result.hexdigest()
    import base64
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    password = b"client-secret"
    salt = bytes(final_hash.encode())
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=200,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

