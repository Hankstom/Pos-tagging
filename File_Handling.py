# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:00:39 2020

@author: Nihal Choudhary
"""

import xml.etree.ElementTree as ET
from os.path import isdir
from os.path import isfile
from os import mkdir
from os import listdir


# function filehandler handles single xml file
def filehandler(source, dest):
    # opening xml file
    xmlfile = open(source, "r", encoding="utf-8")
    # storing text into a variable
    xmlfiletext = xmlfile.read();

    # closing xmlfile
    xmlfile.close()

    # make xml tree from that text variable
    tree = ET.fromstring(xmlfiletext)

    # making list of word('w') tags
    wlist = tree.iter('w')



    # open destination file with overwriting mode
    destfile = open(dest[:-4] + ".txt", "w+", encoding="utf-8")

    # store the data in the destfile
    for word in wlist:

        text = word.text

        text = text.rstrip()
        pos = word.get('pos')

        word_tag =  text +"_"+ pos

        destfile.write(word_tag + "\n")

    # close destfile
    destfile.close()


def extractWordTags(source, dest):
    # check if source is a file
    if isfile(source):
        # if yes, then process the file
        # if destination is not there, then function will create it, and if it is there, it will overrite it.
        filehandler(source, dest)
    else:
        # so the source is a folder, we need to make corresponding folder in the dest
        # check if dest has the folder
        if not isdir(dest):
            mkdir(dest)

        # now enumerate all the items in the source directory
        for item in listdir(source):
            extractWordTags(source + '/' + item, dest + '/' + item)


s = "./Test-corpus"
d = "./Processed_train_corpus5"

extractWordTags(s, d)
