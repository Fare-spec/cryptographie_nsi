from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

def encrypt_message(key, plaintext):
    cipher = Salsa20.new(key)
    ciphertext = cipher.encrypt(plaintext.encode('utf-8'))
    return ciphertext

def decrypt_message(key, ciphertext):
    cipher = Salsa20.new(key)
    plaintext = cipher.decrypt(ciphertext).decode('utf-8')
    return plaintext

def main():
    # Générer une clé aléatoire de 32 octets
    key = get_random_bytes(32)

    # Message à crypter
    message = "Bonjour, ceci est un message secret."

    # Chiffrer le message
    encrypted_message = encrypt_message(key, message)
    print(f"Message chiffré: {encrypted_message.hex()}")

    # Déchiffrer le message
    decrypted_message = decrypt_message(key, encrypted_message)
    print(f"Message déchiffré: {decrypted_message}")

if __name__ == "__main__":
    main()
