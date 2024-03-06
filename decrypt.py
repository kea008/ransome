from cryptography.fernet import Fernet
import os


def load_key(key_file='key.key'):
    with open(key_file, 'rb') as f:
        key = f.read()
    return key


def decrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file_path, 'wb') as f:
        f.write(decrypted_data)


def check_payment(payment_amount):
    user_payment = float(input("Please enter the payment amount (in pesos): "))
    if user_payment >= payment_amount:
        print("Payment verified. Proceeding with decryption.")
        return True
    else:
        print("Insufficient payment. Cannot proceed with decryption.")
        return False


def main():
    base_dir = 'C:/Users/alber/Documents/Olaso/'
    data_dir = os.path.join(base_dir, 'data')

    
    payment_amount = 10000

   
    key = load_key()

   
    if not check_payment(payment_amount):
        return

 
    encrypted_text_path = os.path.join(data_dir, 'doc_encrypted.txt')
    decrypted_text_path = os.path.join(data_dir, 'doc.txt')
    decrypt_file(encrypted_text_path, decrypted_text_path, key)
    os.remove(encrypted_text_path)

    
    image_files = ['o_encrypted.jpeg', 'a_encrypted.jpeg']
    for image_file in image_files:
        encrypted_image_path = os.path.join(data_dir, image_file)
        decrypted_image_path = os.path.join(data_dir, image_file.replace('_encrypted.jpeg', '.jpeg'))
        decrypt_file(encrypted_image_path, decrypted_image_path, key)
      
        os.remove(encrypted_image_path)

    print("Decryption completed.")

if __name__ == "__main__":
    main()
