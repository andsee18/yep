"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    # Устанавливаем переменную окружения для настроек Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_app.settings")
    
    try:
        # Импортируем функцию для выполнения команд Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Обрабатываем ошибку импорта Django
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Выполняем команды Django из командной строки
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()