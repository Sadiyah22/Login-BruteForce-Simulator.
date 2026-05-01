import time

def simulate_login(target_password, wordlist_file):
    print(f"[*] Starting Brute-Force Simulation...")
    print(f"[*] Target Password: {'*' * len(target_password)} (Hidden for simulation)")
    print("-" * 40)

    try:
        with open(wordlist_file, 'r') as file:
            attempts = 0
            for line in file:
                attempts += 1
                guess = line.strip()
                
                # Simulate the delay of a real network request (0.1 seconds)
                time.sleep(0.1)
                
                if guess == target_password:
                    print(f"[+] SUCCESS! Password found: {guess}")
                    print(f"[+] Total attempts: {attempts}")
                    return True
                else:
                    print(f"[-] Attempt {attempts}: '{guess}' failed.")
                    
            print("[-] Simulation ended. Password not found in wordlist.")
            return False

    except FileNotFoundError:
        print("[-] Error: 'passwords.txt' not found. Please create it first.")

# Configuration
target = "secret123"  # The "correct" password
words = "passwords.txt" # Your dictionary file

simulate_login(target, words)
