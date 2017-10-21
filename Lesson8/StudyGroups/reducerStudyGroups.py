#!/usr/bin/python

import sys
import csv


def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar=None)
    studentsWhoPosted =[]
    post_id = None
    
    for line in sys.stdin:
        data = line.strip().split('\t')
       
        if len(data) != 2:
            # something is wrong
            continue

        thisId, thisAuthor = data
        
        if  post_id and post_id!= thisId:
            writer.writerow([post_id,studentsWhoPosted])
            
            post_id = thisId
            studentsWhoPosted = [thisAuthor]
            
        else:   
            post_id = thisId
            studentsWhoPosted.append(thisAuthor)
        
            
    #Taking care of the last PostId where there is no change of key        
    if post_id != None:
        writer.writerow([post_id,studentsWhoPosted])
        
if __name__=='__main__':reducer()

