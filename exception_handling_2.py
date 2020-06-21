"""
Exceptions: every error that python encounters is identified by a `type`
Raising exceptions with raise
"""
import re
def process_date(this_date):
    #this regex makes sure that this date is YYYY-MM-DD
    if not re.search(r'^\d\d\d\d-\d\d-\d\d$', this_date):
        raise ValueError('please submit date in YYYY-MM-DD format')
    print(f"the submitted date is {this_date}")

process_date("2000-01-01")
print('\n\n')
process_date("01/01/2000")


