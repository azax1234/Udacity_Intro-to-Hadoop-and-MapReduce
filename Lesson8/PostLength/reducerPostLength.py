#!/usr/bin/python
from __future__ import division #This line is required only in Python2 for division
import sys
import csv


def reducer():
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar=None)
    PostId = None
    TotalAnswerLength = 0
    TotalQuestionLength = 0
    CountOfAnswers = 0
    
    print('QuestionNodeID| QuestionLength| AverageAnswerLength')
    print('---------------------------------------------------')
    
    
    for line in sys.stdin:
        data = line.strip().split('\t')
       
        if len(data) != 3:
            # something is wrong
            continue

        thisId, thisLength, thisType = data
        
        if PostId and PostId != thisId:
            if CountOfAnswers > 0:
                avgAnserLength = float(TotalAnswerLength/CountOfAnswers)
            else:
                avgAnserLength = TotalAnswerLength
            writer.writerow([PostId,'    ', TotalQuestionLength,'    ', avgAnserLength])
            
            PostId = thisId
            CountOfAnswers = 0
            TotalAnswerLength = 0
            TotalQuestionLength =0
    
        PostId = thisId
        if thisType == 'answer':
            TotalAnswerLength = TotalAnswerLength + int(thisLength)
            CountOfAnswers = CountOfAnswers + 1
            #print (PostId, TotalAnswerLength, CountOfAnswers)
        else:
            TotalQuestionLength = int(thisLength)
            
        #Taking care of the last PostId where there is no change of key        
    if PostId != None:
        if CountOfAnswers > 0:
            avgAnserLength = TotalAnswerLength/CountOfAnswers
        else:
            avgAnserLength = TotalAnswerLength
           
        writer.writerow([PostId,'    ', TotalQuestionLength,'    ', avgAnserLength])
 
if __name__=='__main__':reducer()

