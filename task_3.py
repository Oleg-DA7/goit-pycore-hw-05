# Завдання 3
# 
import sys
import pandas as pd

class LogEngine:
    def __init__(self, file):
        self.file = file
        self._df_log = pd.DataFrame(columns=['date', 'time', 'type', 'message'])
        self._load_logs(file)
        if self._loaded:
            self.count_logs_by_level()
            self.display_log_counts()
        else:
            sys.exit

    def count_logs_by_level(self) -> dict: 
        self._df_stat = self._df_log.groupby('type')['message'].count()
        return self._df_stat.to_list()

    def _parse_log_line(self, line: str) -> dict:
        result = line.replace('\n', '').split(' ', 3)        
        return result

    def _load_logs(self, file_path: str) -> list:
        result = []
        try:
            with open(file_path) as file:    
                for line in file:                     
                    l_list = self._parse_log_line(line)                
                    result.append(l_list)
                    self._df_log.loc[len(self._df_log)] = l_list
        except FileNotFoundError:
            print(f'Can`t find file {file_path}')
            sys.exit
        except IOError:
            print(f'An error occurred while reading the file {file_path}')
            sys.exit
        self._loaded = True
        return result

    def filter_logs_by_level(self, level: str) -> list:
        result = []
        df_filtered = self._df_log[self._df_log['type'] == level]
        for i, r in df_filtered.iterrows():
            print(f'{r['date']} {r['time']} - {r['message']}')
            result.append(f'{r['date']} {r['time']} - {r['message']}')
        return result

    def display_log_counts(self):
        print('Рівень логування | Кількість')
        print('-----------------|----------')
        for i, v in self._df_stat.items():
            print(f'{'{: <17}'.format(i)}|  {v}')
    
def main():
    if len(sys.argv) < 2 | len(sys.argv) > 3:
        print("Invalid count of parameters!")
        sys.exit(1)
    le = LogEngine(sys.argv[1])
    if len(sys.argv) == 3:
        le.filter_logs_by_level(sys.argv[2])

if __name__ == "__main__":
    main()