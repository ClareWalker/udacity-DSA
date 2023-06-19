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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

text_incoming, text_answering, text_timestamp = texts[0]
_, text_time = text_timestamp.split(' ')
print(f'First record of texts, {text_incoming} texts {text_answering} at time {text_time}')

call_incoming, call_answering, call_timestamp, duration = calls[-1]
_, call_time = call_timestamp.split(' ')
print(f'Last record of calls, {call_incoming} calls {call_answering} at time {call_time}, lasting {duration} seconds')
