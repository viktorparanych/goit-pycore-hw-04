# Cкрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів.
import sys
from pathlib import Path
from colorama import init, Fore

init (autoreset=True)
#Рекурсивна функція для візуалізації структури директорії.
def display_tree(path, indent=""):
    for item in path.iterdir():
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            display_tree(item, indent + "    ")
        else:
            print(indent + Fore.YELLOW + f"📜 {item.name}")
# Головна функція програми. Обробляє аргументи командного рядка, перевіряє їх на помилки та запускає процес сканування директорії.
def main():
    if len(sys.argv) < 2:
        print(Fore.RED +  "Помилка: ви не вказали шлях до директорії!")
        return 
    folder_path = Path(sys.argv[1])

    if not folder_path.exists():
        print(Fore.RED + f"Помилка: Такого шляху не існує!")
        return
    if not folder_path.is_dir():
        print (Fore.RED + f"Помилка: Це файл, а не папка!")
        return
# Якщо всі перевірки пройдені успішно, повідомляємо про старт
    print (Fore.GREEN + f"Усе супер! Починаємо сканувати папку: {folder_path}\n")
    display_tree(folder_path)
if __name__ == "__main__":
    main()

# Приклад використання: python exercise3.py C:\Users\YourUsername\Documents\YourFolder