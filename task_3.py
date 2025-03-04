# Завдання 3
# 
import sys


class LogEngine:
    def __init__(self, file):
        self.file = file
        self._load_logs(file)
        
    def _parse_log_line(line: str) -> dict:
        pass    

    def _load_logs(file_path: str) -> list:
        pass

    def filter_logs_by_level(logs: list, level: str) -> list:
        pass

    def count_logs_by_level(logs: list) -> dict: 
        pass

    def display_log_counts(counts: dict):
        pass
    
def main():
    le = LogEngine()
    if len(sys.argv) > 2:
        print("Invalid count of parameters!")
        sys.exit(1)



if __name__ == "__main__":
    main()