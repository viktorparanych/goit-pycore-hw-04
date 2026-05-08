# Функція длля читання інформації про котів з файлу 
from pathlib import Path

def get_cats_info(path):
    try:
        cats = []
        with open(path, 'r', encoding='utf-8')as file: # відкриваємо фай розділяємо комою і зберігоємо в словник інформацію про котів
            for line in file:  #
                data = line.strip().split(',')
                cat_info = {
                    'id': data[0],
                    'name': data[1],
                    'age': data[2]
                }
                cats.append(cat_info)
        return cats

    except FileNotFoundError:
        print ("Файл не знайдено")
        return []

cats_info = get_cats_info("cats_file.txt")
print(cats_info)