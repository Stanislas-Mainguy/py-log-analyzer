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

def analyze_logs(log_lines):
    """Count occurrences of each log level and display a summary."""
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
        "DEBUG": 0,
        "CRITICAL": 0
    }

    for line in log_lines:
        for level in log_counts:
            if level in line:
                log_counts[level] += 1

    print("\n📊 Résumé des logs par niveau :\n")
    for level, count in log_counts.items():
        print(f"{level:<10} : {count}")

def main():
    log_path = os.path.join("samples", "sample_logs.txt")
    logs = load_logs(log_path)

    # Display first 5 lines
    print("\n--- First 5 lines ---")
    for line in logs[:5]:
        print(line.strip())

    # Analyze log levels
    analyze_logs(logs)

if __name__ == "__main__":
    main()
