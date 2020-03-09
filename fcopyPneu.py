#!/usr/bin/env python

import os
import sys
import glob
from csv import reader
import shutil as sh



file_list = []
with open ('Data_Entry_2017_Pneu.csv','r') as infile:
    for row in infile:
        row_split = row.split(',')
        file_list.append(row_split[0])

file_list = file_list[1:]
# print('{} files read from CSV.\n'.format(len(file_list)))


source_dir = sys.argv[1]
target_dir = sys.argv[2]

# print('Copying files from {} to {}.\n'.format(source_dir, target_dir))
for file in file_list:
    source_path = os.path.join(source_dir,file)
    sh.copy(source_path, target_dir)


    
print "Done!"



