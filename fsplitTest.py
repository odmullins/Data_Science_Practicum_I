#!/usr/bin/env python

import os
import sys
import glob
from csv import reader
import shutil as sh
import random


source_dir = sys.argv[1]
target_dir = sys.argv[2]

files = os.listdir(source_dir)

for f in files:
    if random.random() < 0.1:
        sh.move(source_dir + '/'+ f, target_dir + '/'+ f)

print "Done!"



