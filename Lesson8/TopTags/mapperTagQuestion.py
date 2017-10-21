#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar= None)
    tags=[]

    for line in reader:
        if len(line) != 19:
            continue
        if line[2] != 'tagnames':
            tags=line[2].split()
        for i in tags:
            if line[5] == 'question':
                writer.writerow([i,line[5]])
    
if __name__=='__main__':mapper()  
       
        
