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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_times = dict()

for incoming, receiving, _, duration in calls:
    for number in incoming, receiving:
        call_times[number] = call_times.get(number, 0) + int(duration)

max_number = max(call_times, key=call_times.get)
max_duration = call_times[max_number]

print(f'{max_number} spent the longest time, {max_duration} seconds, on the phone during September 2016')




