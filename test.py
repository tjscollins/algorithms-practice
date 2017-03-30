#!/usr/bin/python3
import sys
import os
import importlib

sys.path.extend([os.getcwd() + '/Python/Tests'])
python_test = importlib.import_module('python' + '_test')

python_test.main()
