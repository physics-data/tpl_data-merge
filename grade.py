#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import json
import subprocess
import time
from os.path import isfile, join
import filecmp
import random
import string


def write_grade(grade):
    if os.isatty(1):
        print('Removing all output files')
        os.system('rm -f data/*.out.h5')

    data = {}
    data['grade'] = grade
    if os.isatty(1):
        print('Grade: {}/90'.format(grade))
    else:
        print(json.dumps(data))

    sys.exit(0)


if __name__ == '__main__':

    if sys.version_info[0] != 3:
        print("Plz use python3")
        sys.exit()

    if os.isatty(1):
        print('Removing all output files')
    os.system('rm -f data/*.out.h5')

    grade = 0

    # Part 1
    if os.isatty(1):
        print('Running \'make\'')
    p = subprocess.Popen(['make'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    start_time = time.time()

    while p.poll() is None:
        if time.time() - start_time > 1:
            p.kill()

    stdout, stderr = p.communicate(timeout=1)
    if len(stderr) == 0:
        try:
            for i in range(1, 11):
                path = 'data/{}.out.h5'.format(i)
                if not os.path.exists(path):
                    if os.isatty(1):
                        print('File missing: {}'.format(path))
                    break

        except Exception:
            if os.isatty(1):
                print('Unexpected stdout:')
                sys.stdout.buffer.write(stdout)
    elif os.isatty(1):
        print('Your program exited with:')
        sys.stdout.buffer.write(stderr)


    # Part 2
    if os.isatty(1):
        print('Running \'make clean\'')
    p = subprocess.Popen(['make', 'clean'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    start_time = time.time()

    while p.poll() is None:
        if time.time() - start_time > 1:
            p.kill()

    stdout, stderr = p.communicate(timeout=1)
    if len(stderr) == 0:
        try:
            flag = 1
            for i in range(1, 11):
                path = 'data/{}.out.h5'.format(i)
                if os.path.exists(path):
                    flag = 0
                    if os.isatty(1):
                        print('File still exists: {}'.format(path))
                
            if flag:
                grade += 10
        except Exception:
            if os.isatty(1):
                print('Unexpected stdout:')
                sys.stdout.buffer.write(stdout)
    elif os.isatty(1):
        print('Your program exited with:')
        sys.stdout.buffer.write(stderr)

    write_grade(grade)

