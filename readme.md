# QR Code Generator

## Details
This is a simple Python script to generate QR codes based on the user input. To run this script, you need to have Python installed and a few additional modules. 

### Required Modules
- `qrcode`: Used for generating QR code images.
- `os`: Provides a portable way of using operating system-dependent functionality.

To install the necessary modules, you can run: pip install qrcode

## Features
- **User Customization**: The program takes user input for the data to be encoded and the box size of the QR code.
- **File Overwrite Protection**: Before saving the QR code image, it checks if a file with the chosen name already exists. If it does, the user is prompted to decide whether they want to overwrite it or choose a different name.
- **Flexibility**: It supports generating QR codes for any string input.

## Getting Started
1. Clone the repository: git clone https://github.com/Bisalkumar/QR_Code.git
2. Navigate to the repository: QR_Code
3. Install the required modules as mentioned above.

## How to Use
1. Run the script using: python qr_code_generator.py
2. Follow the on-screen prompts to generate your QR code.

## Screenshots
![QR_Code.png](QR_Code.png)

## Contributions
We welcome contributions to improve this tool. To contribute:
1. Fork the repository.
2. Make your changes.
3. Create a pull request with a description of your improvements.

## License
This project is under the MIT License. See `LICENSE` file for more details.

## Acknowledgement
Special thanks to the `qrcode` library developers and the Python community for their constant support and invaluable resources.
