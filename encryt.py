from cryptography.fernet import Fernet
import os

# Function to load or generate the encryption key
def load_or_generate_key(key_file='C:/Users/alber/Documents/Olaso/key.key'):
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return key

# Function to encrypt a file
def encrypt_file(input_file_path, output_file_path, key):
    cipher_suite = Fernet(key)
    with open(input_file_path, 'rb') as f:
        data = f.read()
    encrypted_data = cipher_suite.encrypt(data)
    with open(output_file_path, 'wb') as f:
        f.write(encrypted_data)

# Main function
def main():
    base_dir = 'C:/Users/alber/Documents/Olaso/'
    data_dir = os.path.join(base_dir, 'data')

    # Create data directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Load or generate encryption key
    key = load_or_generate_key()

    # Encrypt text file
    input_text_path = os.path.join(data_dir, 'doc.txt')
    encrypted_text_path = os.path.join(data_dir, 'doc_encrypted.txt')
    encrypt_file(input_text_path, encrypted_text_path, key)
    os.remove(input_text_path)  # Remove original text file after encryption

    # Encrypt image files
    image_files = ['o.jpeg', 'a.jpeg']
    for image_file in image_files:
        input_image_path = os.path.join(base_dir, image_file)
        encrypted_image_path = os.path.join(data_dir, f'{os.path.splitext(image_file)[0]}_encrypted.jpeg')
        encrypt_file(input_image_path, encrypted_image_path, key)
        os.remove(input_image_path)  # Remove original image file after encryption

    print("Encryption completed.")

if __name__ == "__main__":
    main()
