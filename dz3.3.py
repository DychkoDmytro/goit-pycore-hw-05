import sys
import os
from typing import List, Dict, Optional

def parse_log_line(line: str) -> Dict[str, str]:
    
    parts = line.strip().split(' ', 3)
    if len(parts) < 4:
        return {}
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line)
                if log_entry:  # Додаємо лише валідні записи
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
   
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    
    level_counts = {}
    for log in logs:
        level = log['level']
        if level in level_counts:
            level_counts[level] += 1
        else:
            level_counts[level] = 1
    return level_counts

def display_log_counts(counts: Dict[str, int]):
    
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts.keys()):
        print(f"{level:<17} | {counts[level]:<8}")

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до файлу логів.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    
   
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)
    
    if len(sys.argv) == 3:
        level_to_filter = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level_to_filter)
        
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level_to_filter.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Записів для рівня '{level_to_filter.upper()}' не знайдено.")

if __name__ == "__main__":
    main()