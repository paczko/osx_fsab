#!/usr/bin/env python3
import subprocess

result = subprocess.run(['diskutil', 'list'], capture_output=True, text=True)

print("xxxx", result.stdout, "ddd")
