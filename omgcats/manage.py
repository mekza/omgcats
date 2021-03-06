#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, PROJECT_PATH + "/../src/")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omgcats.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
