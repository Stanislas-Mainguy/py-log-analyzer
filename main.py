# main.py

import os

def load_logs(filepath):
    """Load and return the log lines from a file."""
    if not os.path.exists(filepath):
        print(f"[!] File not found: {filepath}")
        return []

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print(f"[+] Loaded {len(lines)} log lines.")
    return lines

def main():
    # Modify path if needed
    log_path = os.path.join("samples", "sample_logs.txt")
    logs = load_logs(log_path)

    # Display first 5 lines for preview
    print("\n--- First 5 lines ---")
    for line in logs[:5]:
        print(line.strip())

if __name__ == "__main__":
    main()
