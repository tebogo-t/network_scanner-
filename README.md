
# Network Vulnerability Scanner

This Python script performs a network vulnerability scan by checking if specific ports on a range of IP addresses are vulnerable based on a provided vulnerability file.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:

   ```bash
   python3 network_scanner.py
You will be prompted to provide the following information:

Vulnerability Filename: Enter the name of the vulnerability file to use for scanning. The file should contain a list of known vulnerabilities.
IP Range: Enter the range of IP addresses to scan in the format start_ip-end_ip (e.g., 192.168.0.1-10).

Vulnerability File Format:

The vulnerability file should be a plain text file containing a list of known vulnerabilities. 
Each vulnerability should be listed on a separate line. The script will compare the retrieved banner from the service with the lines in the vulnerability file to determine if the server is vulnerable.

## Disclaimer
This script is intended for educational and testing purposes only. Use it responsibly and only on systems that you have permission to scan. The script may produce false positives or miss vulnerabilities. The authors are not responsible for any misuse or damage caused by this script.


Feel free to modify and customize the README.md file according to your specific needs and preferences.

