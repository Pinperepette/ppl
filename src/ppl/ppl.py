#!/usr/bin/env python
import os
import subprocess

def pypocessgrep():
    args = ["pgrep", 'python']
    out = os.popen(" ".join(args)).read().strip()
    return list(map(int, out.splitlines()))

def start(command):
    first = pypocessgrep()
    subprocess.Popen(command, shell=True)
    after = pypocessgrep()
    for k in after:
        if k not in first:
            return k

def stop(process):
    command = f'kill {process}'
    os.system(command)
