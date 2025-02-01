import os
import re
import sys

# Список ключевых слов интерфейса
keywords = ["Settings", "Menu", "Save", "Cancel", "OK", "Error", "Success", "Load", "Exit"]

# Словарь перевода
translations = {
    "Settings": "Настройки",
    "Menu": "Меню",
    "Save": "Сохранить",
    "Cancel": "Отмена",
    "OK": "ОК",
    "Error": "Ошибка",
    "Success": "Успешно",
    "Load": "Загрузить",
    "Exit": "Выход"
}

# Функция создания файла локализации
def create_localization_file(path):
    localization_path = os.path.join(path, "lib/gui/localization.h")
    os.makedirs(os.path.dirname(localization_path), exist_ok=True)

    with open(localization_path, "w", encoding="utf-8") as f:
        f.write("#ifndef LOCALIZATION_H\n#define LOCALIZATION_H\n\n")
        f.write("#define LANG_RU 1\n#define LANG_EN 0\n\n")
        f.write("#define LANGUAGE LANG_RU\n\n")

        f.write("#if LANGUAGE == LANG_RU\n")
        for eng, rus in translations.items():
            f.write(f'    #define TEXT_{eng.upper()} "{rus}"\n')
        f.write("#else\n")
        for eng, rus in translations.items():
            f.write(f'    #define TEXT_{eng.upper()} "{eng}"\n')
        f.write("#endif\n\n#endif // LOCALIZATION_H\n")

    print(f"[✔] Файл локализации создан: {localization_path}")

# Функция замены строк в коде
def replace_strings_in_code(path):
    modified_files = []

    # Поиск всех .c и .h файлов
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".c") or file.endswith(".h"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()

                modified = False
                new_lines = []
                
                for line in lines:
                    # Проверяем, есть ли в строке текст для перевода
                    for eng, rus in translations.items():
                        pattern = rf'(["\'])({eng})(["\'])'
                        if re.search(pattern, line):
                            line = re.sub(pattern, rf'\1TEXT_{eng.upper()}\3', line)
                            modified = True

                    new_lines.append(line)

                # Если файл был изменён, создаём резервную копию и записываем изменения
                if modified:
                    backup_path = file_path + ".bak"
                    os.rename(file_path, backup_path)

                    with open(file_path, "w", encoding="utf-8") as f:
                        f.writelines(new_lines)

                    modified_files.append(file_path)

    print(f"[✔] Изменено файлов: {len(modified_files)}")
    return modified_files

# Главная функция
def main():
    if len(sys.argv) < 2:
        print("Использование: python3 translate_momentum.py /путь/к/прошивке/Momentum-Firmware-dev")
        sys.exit(1)

    firmware_path = sys.argv[1]
    if not os.path.isdir(firmware_path):
        print("Ошибка: указанная папка не существует.")
        sys.exit(1)

    print("[✔] Начинаю процесс перевода прошивки Momentum-Firmware на русский язык...")

    # Создаём файл локализации
    create_localization_file(firmware_path)

    # Заменяем строки в исходных кодах
    modified_files = replace_strings_in_code(firmware_path)

    print("[✔] Перевод завершён! Все изменения внесены.")
    print(f"[✔] Изменённые файлы ({len(modified_files)}):")
    for file in modified_files:
        print(f" - {file}")

if __name__ == "__main__":
    main()
