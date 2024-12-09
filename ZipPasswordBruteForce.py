import zipfile
from datetime import datetime, timedelta

# Path to the encrypted ZIP file
zip_path = "YourFile.zip"

# Start and end dates for brute-force range
start_date = datetime(2023, 1, 1)  # Adjust year if needed
end_date = datetime(2025, 12, 31)  # Adjust year if needed

# Function to attempt to extract the ZIP file
def try_password(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        print(f"Password found: {password}")
        return True
    except (RuntimeError, zipfile.BadZipFile):
        return False

# Main brute-force logic
with zipfile.ZipFile(zip_path) as zip_file:
    current_date = start_date
    while current_date <= end_date:
        # Generate password in dd-mm-yyyy format
        password = current_date.strftime("%d-%m-%Y")
        if try_password(zip_file, password):
            break  # Stop if the password is found
        current_date += timedelta(days=1)
    else:
        print("Password not found within the given range.")
