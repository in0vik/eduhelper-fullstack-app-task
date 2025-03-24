#!/usr/bin/env python
import os
import sys

def main():
    """Runs Django's administrative tasks (migrations, runserver, etc.)."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eduhelper_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and "
            "available on your PYTHONPATH environment. "
            "Did you forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
