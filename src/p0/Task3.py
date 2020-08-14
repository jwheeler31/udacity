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


# Comments to reviewer:
#   - Parenthesis on line 19 is out of place (should most likely be removed).
#   - The wording in the introduction to this problem makes it sound like
#       there are potentially non-fixed lines in Bangalore that start with
#       "080"

def part_a():
    """
    Part A description:

    Part A: Find all of the area codes and mobile prefixes called by people in Bangalore.
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

    @return: None
    """
    # Want: area codes/mobile prefixes that people in bangalore called
    # Data identifiers:
    #   - Area codes:
    #       - Fixed line:
    #           - start at beginning of number
    #           - encloses in parenthesis
    #           - variable length, but first digit is zero
    #       - Mobile:
    #           - have a space in the number
    #           - first 4 digits
    #               - begins with 7, 8, or 9
    #       - Telemarketers:
    #           - only include a single "140", if encountered
    # Useful data:
    #   - Caller (call[0]) should match a Bangalorian land line
    #       - Number starts with: "(080)"
    match = 0
    area_codes = set()
    for call in calls:
        # Call originated in bangalore
        if call[0].startswith("(080)"):
            # Telemarketer
            if call[1].startswith("140"):
                match += 1
                area_codes.add("140")

            if call[1].startswith(("7", "8", "9")) and " " in call[1]:
                match += 1
                area_code = call[1][0:4]
                area_codes.add(area_code)

            # Area-code prefix format: "\(0[0-9]+\)";
            if call[1].startswith("(0"):
                last_paren_idx = call[1].find(")")
                # With parenthesis:
                #   area_code = call[1][0:last_paren_idx + 1]
                area_code = call[1][1:last_paren_idx]
                area_codes.add(area_code)
                match += 1

    print("The numbers called by people in Bangalore have codes:")
    for area_code in sorted(area_codes):
        print(area_code)


def part_b():
    """
    Part B description:

    Part B: What percentage of calls from fixed lines in Bangalore are made
    to fixed lines also in Bangalore? In other words, of all the calls made
    from a number starting with "(080)", what percentage of these calls
    were made to a number also starting with "(080)"?

    Print the answer as a part of a message::
    "<percentage> percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore."
    The percentage should have 2 decimal digits

    @return: None
    """

    # In other words, of all the calls made
    # from a number starting with "(080)", what percentage of these calls
    # were made to a number also starting with "(080)"?
    landline_calls = 0
    for call in calls:
        if call[0].startswith("(080)") and call[1].startswith("(080)"):
            landline_calls += 1
    percent_landline = landline_calls / float(len(calls)) * 100
    print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
          .format(percent_landline))


def main():
    part_a()
    part_b()


main()
