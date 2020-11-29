# import packages
import datetime
from datetime import timedelta
import re
import calendar

# open txt file
fp = open('bestsellers2.txt')

# initialize variables
all_list = []

# read data
for line in fp:
    # separates data by tab
    line_list = line.split('\t')
    # add the separated data to the list
    all_list.append(line_list)


# add spaces before capital letters
# function that adds a space before every capital letter [A-Z]
def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


# add spaces to columns for title, author and publisher (column 1, 2 and 3)
for l in all_list:
    l[0] = (capital_words_spaces(l[0]))
    l[1] = (capital_words_spaces(l[1]))
    l[2] = (capital_words_spaces(l[2]))


# function to print the entire list in a more beautiful way
def print_book(l):
    for l in all_list:
        print('{0}, by {1}, {2}'.format(l[0], l[1], l[3]))


# function to search by title
def search_by_title():
    # initialize counter variable that displays number of results
    count = 0
    t = str(input("Title: "))
    for l in all_list:
        if re.findall(t.lower(), l[0].lower()):
            result = re.findall(t.lower(), l[0].lower())
            for match in result:
                print('{0}, by {1}, {2}'.format(l[0], l[1], l[3]))
                count = count + 1
    if count == 0:
        print("There is no book with that Title")
    print(count, "result(s) found")


# function to search by author
def search_by_author():
    # initialize counter variable that displays number of results
    count = 0
    # ask for author search input
    author = input("Author: ")
    for l in all_list:
        # matches lowercase characters of input to lowercase characters of title in library to get result irrespective of capitalization
        if re.findall(author.lower(), l[1].lower()):
            result = re.findall(author.lower(), l[1].lower())
            for match in result:
                print('{0}, by {1}, {2}'.format(l[0], l[1], l[3]))
                # increases counter by one for every match
                count = count + 1
    # prints output when there was no match
    if count == 0:
        print("There is no book written by that Author")
    # prints number of results
    print(count, "result(s) found")


def search_by_year():
    while True:
        try:
            start_year = int(input("First year: "))
            if start_year in list(range(1000, 10000)):
                break
            if start_year not in list(range(1000, 10000)):
                print("Please only use 4-digit year numbers.")
                continue
        except ValueError:
            print("Please provide integers only.")
    while True:
        try:
            end_year = int(input("Second year: "))
            if end_year in list(range(1000, 10000)):
                break
            if end_year not in list(range(1000, 10000)):
                print("Please only use 4-digit year numbers.")
                continue
        except ValueError:
            print("Please provide integers only.")
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    range_dates = []
    count = 0
    # transform dates from library to MM/DD/YYYY-format
    for l in all_list:
        a = datetime.datetime.strptime(str(l[3]), '%m/%d/%Y')
        b = datetime.datetime.strftime(a, "%m/%d/%Y")
        l[3] = b
    # create a list for the time between user input (i.e. between start date and end date)
    for single_date in daterange(start_date, end_date):
        range_dates.append(single_date.strftime("%m/%d/%Y"))
    # loop that compares all dates between user input with the dates in the library
    list_in_yearrange = []
    for l in all_list:
        for date in range_dates:
            if date in l[3]:
                list_in_yearrange.append(l)
                count = count + 1
    # sorts list according to date it reached bestseller
    sorted_list = sorted(list_in_yearrange, key=lambda x: datetime.datetime.strptime(str(x[3]), '%m/%d/%Y'))
    # prints library entry for every match, sorted by date
    for item in sorted_list:
        print('{0}, {1}, by {2}'.format(item[3], item[0], item[1]))
    # prints output if there was no match
    if count == 0:
        print("There was no book written between {0} and {1}.".format(start_year, end_year))
    # prints number of results
    print(count, 'result(s) found')


def daterange(start_date, end_date):
    for n in range(int((end_date + datetime.timedelta(days=1) - start_date).days)):
        yield start_date + timedelta(n)

def search_by_month():
    while True:
        try:
            month = int(input("Please enter a month (1-12): "))
            if month in list(range(1, 13)):
                break
            if month not in list(range(1, 13)):
                print("Please only use integers between 1 and 12.")
                continue
        except ValueError:
            print("Please provide integers only.")
    while True:
        try:
            year = int(input("Please enter a year: "))
            if year in list(range(1000, 10000)):
                break
            if year not in list(range(1000, 10000)):
                print("Please only use 4-digit year numbers.")
                continue
        except ValueError:
            print("Please provide integers only.")
    start_date = datetime.date(year, month, 1)
    # end date for each month
    # monthrange returns the start and end date of each month, its maximum is thus the month end day
    end_date = datetime.date(year, month, max(calendar.monthrange(year, month)))
    range_dates = []
    count = 0
    # transform dates from library to MM/DD/YYYY-format
    for l in all_list:
        a = datetime.datetime.strptime(str(l[3]), '%m/%d/%Y')
        b = datetime.datetime.strftime(a, "%m/%d/%Y")
        l[3] = b
    # create a list for the time between user input (i.e. between start date and end date)
    for single_date in daterange(start_date, end_date):
        range_dates.append(single_date.strftime("%m/%d/%Y"))
    # prints library entry for every match
    for l in all_list:
        for date in range_dates:
            if date in l[3]:
                print('{0}, by {1}, {2}'.format(l[0], l[1], l[3]))
                count = count + 1
    # prints output if there was no match
    if count == 0:
        print("No bestseller found in {0} {1}.".format(start_date.strftime("%B"), end_date.strftime("%Y")))
    # prints number of results
    print(count, 'result(s) found')


while True:
    try:
        a = input("\n What task do you want to perform?\n "
                      "1: Search for Title\n "
                      "2: Search for Author\n "
                      "3: Look up year range\n "
                      "4: Look up month/year\n ")
        if a == '1':
            print("Search for Title")
            search_by_title()
            continue
        elif a == '2':
            search_by_author()
            continue
        elif a == '3':
            search_by_year()
            continue
        elif a == '4':
            search_by_month()
            continue
        elif a == 'q':
            quit()
        else:
            print("Please only provide integers from 1 to 4.")
    except ValueError:
        print("Please enter an integer between 1 and 4.")