"""
Task 4:
 All tasks from list_ex.py, logicals.py and strings.py
"""

#### -->> strings and list task

# a = 'Hello coders'
# ## using slicing and indexing
# 1)Ho co
# 2) Hlocdr
# """

a = 'Hello coders'
"""
      ### Slicing
  0   1   2   3   4   5 6   7   8   9   10  11  12
  | H | e | l | l | o | | C | o | d | e | r | s |

      ### Indexing
 | H | e | l | l | o | | C | o | d | e | r | s |
   0   1   2   3   4  5  6   7   8   9   10  11"""

#  -->> Printing Ho co using Slicing
result1_1 = a[0:5:4] + ' ' + a[6:8]
print(result1_1)

#  -->> Printing Ho co using Indexing
result1_2 = a[0] + a[4] + a[5] + a[6] + a[4]
print(result1_2)

#  -->> Printing Hlocdr using Slicing
result2_1 = a[0:11:2]
print(result2_1)

#  -->> Printing Hlocdr using Indexing
result2_2 = a[0] + a[2] + a[4] + a[6] + a[8] + a[10]
print(result2_2)

#########################################################################################################################

""" a=[[11,22,33],[44,55,66],[77,88,99]]

 1.output:[ [22],[55],[88] ]
 2.output:[22,55,88]
 3.output:[ [11,33],[44,55],[77,88] ]
"""
 ### Given a-->>
a = [[11,22,33],[44,55,66],[77,88,99]]
output1 = [[x[1]] for x in a]
print("output 1 :",output1)

output2 = [x[1] for x in a]
print("output 2 :",output2)

output3 = [[x[0], x[2]] for x in a[:1]] + [[x[0], x[1]] for x in a[1:]]
print("output 3 :",output3)

##########################################################################################################################

"""
            LOGICAL PROBLEMS :

   1. sort the following :

   (i) [[11,22],[34,2],[25,87],[17,17],[21,9]] --- second element
   (ii) [11,22,34,2,25,87,17,21,9]

"""
# (i) [[11,22],[34,2],[25,87],[17,17],[21,9]] --- second element
a = [[11,22],[34,2],[25,87],[17,17],[21,9]]
def second_element(sublist):
    return sublist[1]

sorted_a = sorted(a,key=second_element) # Here the key parameter allows you to control the sorting order
print(sorted_a)                         # by specifying a custom rule for comparing elements.

# (ii) [11, 22, 34, 2, 25, 87, 17, 21, 9]  Sorting

b = [11, 22, 34, 2, 25, 87, 17, 21, 9]
sorted_ = sorted(b)
print(sorted_)