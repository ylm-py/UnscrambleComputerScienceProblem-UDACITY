"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

unsorted_duration = []
durations = []
phone_numbers = []


for phone_number , useless , useless2 , duration in calls:
    durations.append(duration)
    unsorted_duration = tuple(durations)
    phone_numbers.append(phone_number)

durations.sort(key=int,reverse=True)
durations_set = set(durations)
longest_time = durations[0]

list_of_time = list(unsorted_duration)
for y in list_of_time:
    if longest_time == y:
        index = list_of_time.index(y)

num = phone_numbers[index]

print(f'{num} spent the longest time, {longest_time} seconds, on the phone during September 2016.')

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

