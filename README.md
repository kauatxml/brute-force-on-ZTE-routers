## Usage

### Prerequisites

Before running the script, make sure you have:

* Python 3.x installed
* The required Python libraries:

  ```bash
  pip install requests beautifulsoup4
  ```
* A valid password wordlist (the default path is `/usr/share/wordlists/rockyou.txt`)
* Authorization to test the target system

### Configuration

Edit the following variables in the script to match your testing environment:

* `url` – Target login endpoint.
* `username` – Username to be tested.
* `wordlist_path` – Path to the password wordlist.

### Running the Script

Execute the script from the terminal:

```bash
python script.py
```

The script will:

1. Create an HTTP session with the target.
2. Retrieve the authentication token from the login page.
3. Load passwords from the specified wordlist.
4. Attempt authentication using each password.
5. Detect successful authentication based on the server response.
6. Periodically refresh the session token and introduce delays to improve request reliability.
7. Save valid credentials to `login_success.txt` if authentication succeeds.

### Output

During execution, the script displays the status of each authentication attempt in the terminal. If valid credentials are found, they are written to a file named `login_success.txt`.

### Disclaimer

This project is intended **only for educational purposes and authorized security assessments**. Use it exclusively on systems you own or have explicit permission to test. Unauthorized use against third-party systems may be illegal and unethical.
