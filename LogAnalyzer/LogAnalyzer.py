from collections import defaultdict
import re

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.data = defaultdict(int)

    def parse_logs(self):
        with open(self.log_file, 'r') as file:
            for line in file:
                self.process_line(line)

    def process_line(self, line):
        # Example regex for parsing a common log format
        pattern = r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.+?)\] "(?P<method>\w+) (?P<url>.+?) HTTP/\d\.\d" (?P<status>\d+) (?P<size>\d+)'
        match = re.match(pattern, line)
        if match:
            ip = match.group('ip')
            self.data[ip] += 1  # Count requests per IP

    def report(self):
        print("Requests per IP:")
        for ip, count in self.data.items():
            print(f"{ip}: {count}")

if __name__ == "__main__":
    # Replace 'access.log' with the path to your log file
    analyzer = LogAnalyzer("logfile.log")
    analyzer.parse_logs()
    analyzer.report()
