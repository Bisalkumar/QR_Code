import qrcode
import os

def get_user_input(prompt, max_value=None, min_value=1):
    """Get validated user input."""
    while True:
        try:
            value = int(input(prompt))
            if max_value and (value > max_value or value < min_value):
                raise ValueError
            return value
        except ValueError:
            print(f"Please enter a valid number between {min_value} and {max_value}.")

def generate_qr_code(data, box_size):
    """Generate a QR code image from given data."""
    qr = qrcode.QRCode(version=None, box_size=box_size, border=5)  # Note the version=None
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color='black', back_color='white')


def save_qr_image(img):
    """Save the QR code image with user-provided name."""
    filename = input("Name it as (without extension): ")
    full_filename = f"{filename}.png"

    # Check if the file already exists
    if os.path.exists(full_filename):
        print("Warning: A file with the same name already exists.")
        overwrite = input("Do you want to overwrite it? (y/n): ").lower()
        if overwrite != 'y':
            save_qr_image(img)
            return

    img.save(full_filename)
    print(f'QR code generated and saved as {full_filename}.')

def main():
    data = input('Enter the Data to be encoded in QR: ')
    box_size = get_user_input('Enter the box size (between 1 and 10): ', max_value=10)

    img = generate_qr_code(data, box_size)
    save_qr_image(img)


if __name__ == "__main__":
    main()
