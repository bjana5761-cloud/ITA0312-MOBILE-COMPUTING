import os
import subprocess

for q in range(1, 8):
    folder = f'q{q}'
    print(f'\n===== Q{q} =====')
    subprocess.run(['python', 'code.py'], cwd=folder, check=True)
print('\nAll Assignment 3 programs completed.')
