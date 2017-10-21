#!/usr/bin/python

import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar= None)

    for line in reader:
        #print ('True' if line[0]=='id' else 'False')
        if len(line) != 19:
            continue
        if line[0] != 'id':
             #scrapping the added time into hours when post was added
            hourAdded = int(line[8].split()[1][0:2])
            #printing to stdout- 'author_id'\t'added_hour'
            writer.writerow([line[3], hourAdded])
    
    #inserting a new line at the end to handle the last change of author id in reducer code       
    writer.writerow(['ignore','ignore'])    
       
if __name__=='__main__':mapper()  
       
        
