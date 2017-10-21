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
        if line[0] !='id':
            if line[5]=='question':
                writer.writerow([line[0],line[3]])
            else:
                writer.writerow([line[6],line[3]])
    
if __name__=='__main__':mapper()  
       
        
