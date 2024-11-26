import subprocess
import os
import random
os.environ["DISPLAY"] = ":0"
os.environ["DBUS_SESSION_BUS_ADDRESS"] = "unix:path=/run/user/1000/bus"


def get_random_image(directory):
    """
    Возвращает случайный файл изображения из указанной директории.
    
    :param directory: Путь к директории с изображениями
    :return: Путь к случайному изображению или None, если подходящих файлов нет
    """
    try:
        # Получаем список файлов в директории
        files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not files:
            print("В указанной папке нет изображений.")
            return None
        
        # Случайно выбираем файл
        return os.path.join(directory, random.choice(files))
    except Exception as e:
        print(f"Ошибка при получении изображения: {e}")
        return None

def set_dark_mode_wallpaper(image_path):
    """
    Устанавливает обои для тёмного режима в GNOME.
    
    :param image_path: Абсолютный путь к изображению
    """
    try:
        # Проверяем путь к файлу
        command = [
            "gsettings", 
            "set", 
            "org.gnome.desktop.background", 
            "picture-uri-dark", 
            f"file://{image_path}"
        ]
        
        # Выполняем команду
        subprocess.run(command, check=True)
        print(f"Обои успешно установлены: {image_path}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Основной алгоритм
def main():
    # Укажите директорию с изображениями
    image_directory = "/home/opidhorn/Pictures/wellpeper"
    
    # Получаем случайное изображение
    random_image = get_random_image(image_directory)
    
    if random_image:
        # Устанавливаем обои
        set_dark_mode_wallpaper(random_image)
        print(f"DISPLAY: {os.environ.get('DISPLAY')}")
        print(f"DBUS_SESSION_BUS_ADDRESS: {os.environ.get('DBUS_SESSION_BUS_ADDRESS')}")
    else:
        print("Не удалось выбрать случайное изображение.")

if __name__ == "__main__":
    main()