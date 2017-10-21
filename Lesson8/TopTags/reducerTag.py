#!/usr/bin/python

import sys
import csv


def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar=None)
    tagId = None
    tagCount = 0
    tagDict = {}
    
    for line in sys.stdin:
        data = line.strip().split('\t')
       
        if len(data) != 2:
            # something is wrong
            continue

        thisTag, thisType = data
        
        if tagId and tagId != thisTag:
           # writer.writerow([tagId,tagCount])
            tagDict[tagId] = tagCount
            tagId = thisTag
            tagCount = 0
            
            
        tagId = thisTag
        tagCount+=1
        
            
    #Taking care of the last PostId where there is no change of key        
    if tagId != None:
       #writer.writerow([tagId,tagCount])
       tagDict[tagId] = tagCount
       
    #sorting the dictionaries fro top 10 values   
    spamList = sorted(tagDict.items(), key=lambda x: x[1],reverse = True)[:10]
    
    
    for i in spamList:
        writer.writerow([i[0], i[1]])
        
    
if __name__=='__main__':reducer()

