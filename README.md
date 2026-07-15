## Description

This Python script automates authentication testing against a local router in a controlled environment. It establishes an HTTP session, retrieves the authentication token from the login page, submits login requests using a password wordlist, detects successful authentications, and periodically refreshes the session token while introducing delays to improve request reliability. The project uses the `requests` and `BeautifulSoup` libraries for HTTP communication and HTML parsing.

**Disclaimer:** This project was developed for educational purposes and authorized security testing only. It should only be used on systems you own or have explicit permission to test.
