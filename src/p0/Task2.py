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


def main():
    # dict: phone number -> duration
    call_records = {}

    most_time = ("placeholder", 0)
    for call in calls:
        source_phone = call[0]
        dest_phone = call[1]
        duration = int(call[3])

        if source_phone not in call_records.keys():
            call_records[source_phone] = duration
        else:
            call_records[source_phone] += duration

        if dest_phone not in call_records.keys():
            call_records[dest_phone] = duration
        else:
            call_records[dest_phone] += duration

        if most_time[1] < call_records[source_phone]:
            most_time = (source_phone, call_records[source_phone])
        if most_time[1] < call_records[dest_phone]:
            most_time = (dest_phone, call_records[dest_phone])

    print("{} spent the longest time, {} seconds, on the phone during September 2016."
          .format(most_time[0], most_time[1]))


main()
