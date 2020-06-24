# -*- coding: utf-8 -*-
"""Script for MyPy Check"""

import subprocess
import os

search_folders = [os.path.join(os.getcwd(), '..', 'mamba_utils')]

for search_folder in search_folders:
    #subprocess.call([f'mypy {os.path.abspath(search_folder)}'], shell=True)

    subprocess.call([
        f"mypy --ignore-missing-imports {os.path.abspath(os.path.join(search_folders[0]))}"
    ],
                    shell=True)
