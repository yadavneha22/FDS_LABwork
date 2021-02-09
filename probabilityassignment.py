# -*- coding: utf-8 -*-
"""ProbabilityAssignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qxhr2ZTuBFRi0KbPqdix3URBjIoQoPDu
"""

#Q1
n=36 # rolling 2 dice
#Probability of getting sum as 4
outcome1=3
p1=outcome1/n
print(p1)
#probability of getting sum less than 13
outcome2=2
p2=outcome2/n
print(p2)

#Q2
Sample=[1,2,3,4,5,6]
e1=[1,2,3]
e2=[2,4,6]
e3=[1,3,5]
#1)E1 or E2 or E3
event1=e3+list(set(e2)-set(e1))
print(event1)
#2)E1 and E2 and E3
event2=set(e1)-set(e2)-set(e3)
print(event2)
#3)E1 but not E3
event3=set(e1)-set(e3)
print(event3)

#Q3
from itertools import permutations
#ther eare 4 consonents
FisrtPosition=4
lastPosition=3
#first and last  position for consonent is fixed
seq = permutations(['a', 't', 'i', 'c', 'e',], 5)
count=0
for p in list(seq):
   count=count+1
p=FisrtPosition*lastPosition*count  #FisrtPosition=4consonents #LastPosition=3 Consonents
p

#Q4
#1 Number of four letter words
letters=['A','B','C','D','E']
seq = permutations(letters, 4)
count1=0
for p in list(seq):
   count1=count1+1
print(count1)
seq = permutations(letters, 3)
count2=0
for p in list(seq):
   count2=count2+1
print(count2)
letters=['A','B','C','D','E']
seq = permutations(letters, 2)
count3=0
for p in list(seq):
   count3=count3+1
print(count3)

#Q5
# therre are 4 seats and 2 of them seated as a pair and can be treated as one unit
arrange=[1,2,3,4]
seq = permutations(arrange, 2)
count1=0
for p in list(seq):
   count1=count1+1
print(count1)

#Q6
# there are 4 math books and 5 hsitory books 
#total 5 slots available 3 for math and 2 for history
math=[1,2,3,4]
history=[5,4,3,2,1]
seq = permutations(math, 3)
count1=0
for p in list(seq):
   count1=count1+1
print(count1)

seq = permutations(history, 2)
count2=0
for p in list(seq):
   count2=count2+1
print(count2)
TotalPermutations=count1*count2
TotalPermutations

#Q7
#mall has 5 flagpoles,in that 3 green and 2 yellow
flags=['G','G','G','Y','Y']
seq = permutations(flags, 5)
for p in list(seq):
   print(p)

import numpy as np
from datascience import * 
N = 365
def p_no_match(n):
    individuals_array = np.arange(n)
    return np.prod( (N - individuals_array)/N )
results = Table().with_columns('Trials', np.arange(1, N+1, 2))
different = results.apply(p_no_match, 'Trials')
results = results.with_columns('P(all different)', different,'P(at least two match)', 1 - different)
results