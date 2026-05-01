# Login Brute-Force Simulator

## Overview
This is a Python-based security research tool designed to simulate a **dictionary-based brute-force attack** against a mock login system. It serves as an educational demonstration of how automated scripts iterate through password lists to gain unauthorized access.

## Technical Goals
The primary purpose of this project is to highlight vulnerabilities in authentication systems, specifically:
* **Predictable Passwords:** Demonstrating why using common words (found in wordlists) is a major security risk.
* **Lack of Rate Limiting:** Showing how an attacker can make hundreds of attempts per minute if a system does not have account lockout policies.
* **Response Analysis:** Understanding the logic of comparing user input against stored credentials.

## How it Works
1. **Wordlist Loading:** The script reads a text file (`passwords.txt`) containing common passwords.
2. **Iteration:** It loops through each entry, simulating a login request with a slight delay (`time.sleep`) to mimic network latency.
3. **Validation:** It compares each guess to a target password. Upon a match, the script identifies the password and the number of attempts taken.

## Features
- **Simulated Latency:** Includes a delay to reflect real-world server response times.
- **Attempt Tracking:** Provides feedback on every failed attempt and a final summary upon success.
- **Error Handling:** Safely manages missing wordlist files.

## How to Run
1. Clone the repository.
2. Create a file named `passwords.txt` in the root directory and add one password per line.
3. Run the simulator:
   ```bash
   python brute_force.py
