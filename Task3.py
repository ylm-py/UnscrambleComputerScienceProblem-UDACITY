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
calling_numbers = []
receiving_numbers = []



for calling_number , receiving_number , date , duration in calls:
  calling_numbers.append(calling_number)
  receiving_numbers.append(receiving_number)

indexes = []
bangalore_nums = []
for (index,n) in enumerate(calling_numbers):
  if n[:5] == '(080)':
    bangalore_nums.append(n)
    indexes.append(index)

area_codes = []
receiving_bangalore_nums = []
count = 0
for y in indexes:
  if receiving_numbers[y] in receiving_numbers:
    receiving_bangalore_nums.append(receiving_numbers[y])
for b in receiving_bangalore_nums:
  if b[0:5] == '(080)':
    count += 1
  if b[5] == ' ' :
    area_codes.append(b[:4])
  if b[0] == '(':
    if b[4] == ')':
      area_codes.append(b[:5])
    if b[5] == ')':
      area_codes.append(b[:6])
    if b[6] == ')':
      area_codes.append(b[:7])

filtred = [s if s.isdigit() else s[1:-1] for s in area_codes]

filtred.sort(reverse=True)
set_filtred = set(filtred)


print('The numbers called by people in Bangalore have codes:' ,*set_filtred,sep='\n')\

percent = "{:.2f}".format((count * 100) / len(bangalore_nums))
print(percent,"percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
