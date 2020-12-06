"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


    
marketers_nums = []
calling_numbers = []
for calling_number , receiving_number , date , duration in calls:
  calling_numbers.append(calling_number)
num = map(lambda num : num , calling_numbers)
for y in num:
    if y[0:3] == '140':
        marketers_nums.append(y)
marketers_nums.sort(reverse=True)
final_list = set(marketers_nums)
print("These numbers could be telemarketers: ",*final_list , sep='\n')


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

