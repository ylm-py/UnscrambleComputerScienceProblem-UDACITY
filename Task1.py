import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


sending_numbers = []
for sending_number, receiving_number, time in texts:
    sending_numbers.append(sending_number)
number_of_sending_numbers = len(set(sending_numbers))
print(number_of_sending_numbers)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

