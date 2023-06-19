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


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

seen_numbers = set()
for incoming, receiving, _ in texts:
    for number in incoming, receiving:
        seen_numbers.add(number)

for incoming, receiving, _, _ in calls:
    for number in incoming, receiving:
        seen_numbers.add(number)

print(f"There are {len(seen_numbers)} different telephone numbers in the records.")
