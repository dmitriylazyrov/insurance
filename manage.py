import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'insurancemanagement.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не вдалося імпортувати Django. Ви впевнені, що його встановлено та "
            "доступна у вашій змінній середовища PYTHONPATH? Ви "
            "забули активувати віртуальне середовище?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
