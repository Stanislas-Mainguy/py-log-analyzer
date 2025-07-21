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
    """Analyze HTTP status codes in the log lines and display a summary."""
    
    status_counts = {
        "2xx": {"count": 0, "label": "Success"},
        "3xx": {"count": 0, "label": "Redirection"},
        "4xx": {"count": 0, "label": "Client Error"},
        "5xx": {"count": 0, "label": "Server Error"}
    }

    for line in log_lines:
        parts = line.split()
        if len(parts) > 8:
            status_code = parts[8]
            if status_code.startswith("2"):
                status_counts["2xx"]["count"] += 1
            elif status_code.startswith("3"):
                status_counts["3xx"]["count"] += 1
            elif status_code.startswith("4"):
                status_counts["4xx"]["count"] += 1
            elif status_code.startswith("5"):
                status_counts["5xx"]["count"] += 1

    print("\n📊 HTTP Status Summary:\n")
    for group, data in status_counts.items():
        print(f"{group:<5} ({data['label']}) : {data['count']}")

def main():
    log_path = os.path.join("samples", "sample_logs.txt")
    logs = load_logs(log_path)

    # Display first 5 lines
    print("\n--- First 5 lines ---")
    for line in logs[:5]:
        print(line.strip())

    # Analyze HTTP status codes
    analyze_logs(logs)

if __name__ == "__main__":
    main()
