import logging
from Crypto.PublicKey import RSA

pubkey_path = "./crypto/rsa_key.pub"
prikey_path = "./crypto/rsa_key.pem"

rsa_key = None


def generate_new_key():
    set_keypair(RSA.generate(4096))


def encrypt(s):
    if isinstance(s, str):
        s = s.encode()
    return rsa_key.encrypt(s, 0)


def decrypt(en):
    return rsa_key.decrypt(en)


def set_keypair(new_key):
    global rsa_key
    rsa_key = new_key
    with open(prikey_path, 'w') as f:
        f.write(rsa_key.exportKey().decode())
    with open(pubkey_path, 'w') as f:
        f.write(rsa_key.publickey().exportKey().decode())


try:
    rsa_key = RSA.importKey(open(prikey_path).read())
except:
    logging.critical("No valid RSA key found")
