#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar= None)

    for line in reader:
        if len(line) != 19:
            continue
        if line[5]=='question':
            length =len(line[4])
            writer.writerow([line[0],length,line[5]])
        elif line[5]=='answer':
            length = len(line[4])
            writer.writerow([line[6],length,line[5]])
        else:
            None
     
if __name__=='__main__':mapper()  
       
        
