import os

def xor_decode(encoded_file, key_file, output_file):
    """
    XOR decode an encoded file using the bytes from a key file.

    Args:
        encoded_file (str): Path to the XOR-encoded file (e.g., .exe).
        key_file (str): Path to the XOR key file (e.g., .dll).
        output_file (str): Path to save the decoded file.
    """
    try:
        # Read the encoded file content
        with open(encoded_file, 'rb') as ef:
            encoded_data = ef.read()

        # Read the key file content
        with open(key_file, 'rb') as kf:
            key_data = kf.read()

        # Perform XOR decoding
        key_length = len(key_data)
        decoded_data = bytearray(
            encoded_data[i] ^ key_data[i % key_length] for i in range(len(encoded_data))
        )

        # Write the decoded data to the output file
        with open(output_file, 'wb') as of:
            of.write(decoded_data)

        print(f"Decoded file saved to: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # File paths
    encoded_file_path = "/home/kali/downloaded_files/csrss.exe"  # Replace with the actual path to the XOR-encoded file
    key_file_path = "/home/kali/downloaded_files/csrss.dll"     # Replace with the actual path to the XOR key file
    output_file_path = "decoded_exe.exe"   # Path to save the decoded file

    # Check if files exist
    if not os.path.exists(encoded_file_path):
        print(f"Encoded file not found: {encoded_file_path}")
    elif not os.path.exists(key_file_path):
        print(f"Key file not found: {key_file_path}")
    else:
        # Perform decoding
        xor_decode(encoded_file_path, key_file_path, output_file_path)
