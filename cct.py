# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 11:22:44 2020

@author: Nihal Choudhary
"""

import glob
with open("concatenatedTrainRealFinal.txt",'w') as outfile:
    for filename in glob.glob('C:\\Users\\Nihal Choudhary\\Downloads\\Processed_train_corpus5\\AN\\*.txt'):
        with open(filename) as infile:
            for line in infile:
                outfile.write(line)