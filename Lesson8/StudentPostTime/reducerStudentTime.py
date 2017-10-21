#!/usr/bin/python

import sys
import csv

def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar=None)
    author_id = None
    spam = []
   
    for line in sys.stdin:
        data = line.strip().split('\t')
        #print (data)
        #inserting a new line at the end to ignore the last change of author id
        #data.append('ignoreignore') 
        
        if len(data) != 2:
            # something is wrong
            continue
        #print (data)
        
        thisauthour_id, thisHour = data
        
        if author_id and author_id != thisauthour_id:
    
            '''finding the max count among the hours
               if spam=[1,2,1,4,4,4,1], then count of each hour is [3,3,2,3,3,3,3] and maxCountOfHour is 3'''
            maxCountOfHour= max(map(lambda x:spam.count(x),spam))
            
            '''finding the hours with maxCountOfHour..in the above example this will
               return a list [1,4] using set to keep the uniq values'''
            HoursWithHighestCount = list(set(filter(lambda y: spam.count(y)==maxCountOfHour,spam)))
            
            '''printing the output with author and the hour details'''
            for i in HoursWithHighestCount:
                writer.writerow([author_id,i])
            
            '''changing the author and hour due to the key(author_id) change'''
            author_id = thisauthour_id
            spam = [thisHour]
            
        else:   
            author_id = thisauthour_id
            spam.append(thisHour)
        
if __name__=='__main__':reducer()
