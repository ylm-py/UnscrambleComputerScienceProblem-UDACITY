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

incoming_number1 , answering_number1 , time1 = texts[0]
incoming_number2 , answering_number2 , time2 , during = calls[-1]


print(f'First record of texts, {incoming_number1} texts {answering_number1} at time {time1}')
print(f'Last record of calls, {incoming_number2} calls {answering_number2} at time {time2}, lasting {during} seconds')



"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

