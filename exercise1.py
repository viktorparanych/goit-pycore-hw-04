# Функція для обчислення загальної суми та середньої заробітної плати з файлуу
from pathlib import Path

def total_salary(path):
    try:
        total_amount = 0
        count = 0 
        
        with open(path, 'r', encoding='utf-8') as file: # відкриваємо файл для обчислення та повертаємо результат
            for line in file:
                data = (line.strip().split(','))
                data[1] = int(data[1])
                salary = data[1]
                total_amount += salary
                count +=1
            
        if count > 0:
            average = int(total_amount/count)
        else:
            average = 0
            
        return (total_amount, average)
    
    except FileNotFoundError:
        print ("Файл не знайдено")
        return (0, 0)
    
# Виклик функції та виведення результату
total, average = total_salary("salary_data.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")