import os
def clear_console():
    os_name = os.name
    if os_name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')
import shutil
import subprocess
import time
print("Сборка начнётся через 3 секунды")
time.sleep(5)
clear_console()

# Удаление старой папки dist и файла приложения, если они существуют
if os.path.exists('dist'):
    shutil.rmtree('dist')
if os.path.exists('my_app.spec'):
    os.remove('my_app.spec')

# Создание exe-файла с помощью PyInstaller
subprocess.call(['pyinstaller', '--onefile', 'Main.py'])

# Удаление временных файлов и папок
if os.path.exists('__pycache__'):
    shutil.rmtree('__pycache__')
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('your_script.spec'):
    os.remove('your_script.spec')

# Копирование жизнено важных для игры файлов
files_to_copy = ["names.txt", "subnames.txt", "story.txt"]
destination_folder = "Игра тут!!!"
for file_name in files_to_copy:
    command = ["copy", file_name, destination_folder]
    subprocess.run(command)
    print(f"Файл '{file_name}' скопирован в папку 'Игра тут!!!'")

clear_console()
print("Сборка завершена, завершение через 3 секунды")
time.sleep(3)
