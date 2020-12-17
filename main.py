# import packages
import datetime
from datetime import timedelta
import re
import calendar
from prettytable import PrettyTable
from fpdf import FPDF


# modify class PDF to set custom header and footer for PDF output
class PDF(FPDF):
    # init function for initializing format, row_height and col_widths
    def __init__(self, orientation='P', unit='mm', format='A4'):
        super().__init__(orientation, unit, format)
        # row height for parameter rows
        self.row_height_parameter = 5
        # column width for parameter columns 1 and 2
        self.col_width_parameter = 25
        self.col_width_parameter2 = 80
        # row height for content rows
        self.row_height = 6
        # column width for content columns 1, 2 and 3
        self.col_width1 = 75
        self.col_width2 = 60
        self.col_width3 = 45

    # page header
    def header(self):
        self.set_y(10)
        # Arial normal 8. Used for date
        self.set_font('Arial', '', size=8)
        # retrieve current date and time
        pdf_name_timestamp = datetime.datetime.strftime(datetime.datetime.today(), '%B %d, %Y %H:%M:%S')
        # print date and time, 180mm width, 10mm height, no borders, 10 line break, right-aligned
        self.cell(180, 10, pdf_name_timestamp, 0, 10, 'R')
        # Arial bold 15. Used for title
        self.set_font('Arial', 'B', size=15)
        # print title, 180mm width, 10mm height, no borders, 10 line break, center-aligned
        self.cell(180, 10, 'New York Times Bestsellers', 10, 0, 'C')
        # line break
        self.ln(self.row_height * 2)

    # page footer
    def footer(self):
        # position at 15mm from bottom
        self.set_y(-15)
        # Arial italic 8. Used for page number
        self.set_font('Arial', 'I', size=8)
        # insert page number / total number of pages
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    # function that sets pdf output
    def print_head_pdf(self, search_type, search_term, counter, sort_type, title1, title2, title3):
        # initialize variables
        search_type = search_type
        search_term = search_term
        counter = counter
        sort_type = sort_type
        pdf = PDF()

        # set all margins at 15mm
        pdf.l_margin = 15
        pdf.r_margin = 15
        pdf.t_margin = 15
        pdf.b_margin = 15

        # retrieves total number of pages for footer
        pdf.alias_nb_pages()

        # adds pages
        pdf.add_page()

        # Arial bold 6. Used for parameter title
        pdf.set_font("Arial", 'B', size=6)
        # print search parameters
        pdf.multi_cell(self.col_width_parameter + self.col_width_parameter2, self.row_height_parameter,
                       txt='Search parameter:', align="L", border=1)

        # Arial normal 6. Used for parameters
        pdf.set_font("Arial", '', size=6)

        # print parameter table with type of search query, search term, number of results and sorted by which variable
        # print search query type
        pdf.multi_cell(self.col_width_parameter, self.row_height_parameter,
                       txt='Search query', align="L", border=1)
        # sets x and y coordinates adjacent to the previously written cell
        pdf.set_xy(self.l_margin + self.col_width_parameter + 5, pdf.get_y() - self.row_height_parameter)
        # prints actual search query type
        pdf.multi_cell(self.col_width_parameter2, self.row_height_parameter,
                       txt='{0}'.format(search_type), align="L", border=1)

        # print search term
        pdf.multi_cell(self.col_width_parameter, self.row_height_parameter,
                       txt='Search term', align="L", border=1)
        pdf.set_xy(self.l_margin + self.col_width_parameter + 5, pdf.get_y() - self.row_height_parameter)
        pdf.multi_cell(self.col_width_parameter2, self.row_height_parameter,
                       txt='{0}'.format(search_term), align="L", border=1)

        # print number of results
        pdf.multi_cell(self.col_width_parameter, self.row_height_parameter,
                       txt='Number of Results', align="L", border=1)
        pdf.set_xy(self.l_margin + self.col_width_parameter + 5, pdf.get_y() - self.row_height_parameter)
        pdf.multi_cell(self.col_width_parameter2, self.row_height_parameter,
                       txt='{0}'.format(counter), align="L", border=1)

        # print sorted by
        pdf.multi_cell(self.col_width_parameter, self.row_height_parameter,
                       txt='Sorted by', align="L", border=1)
        pdf.set_xy(self.l_margin + self.col_width_parameter + 5, pdf.get_y() - self.row_height_parameter)
        pdf.multi_cell(self.col_width_parameter2, self.row_height_parameter,
                       txt='{0}'.format(sort_type), align="L", border=1)

        # page break
        pdf.ln(self.row_height * 0.5)

        # header row for table
        # Arial bold 8. Used for header row
        pdf.set_font("Arial", 'B', size=8)
        # prints header row with titles (from functions search_by_title, etc.)
        if counter > 0:
            pdf.cell(self.col_width1, self.row_height, txt=title1, ln=0, align="L", border=1)
            pdf.cell(self.col_width2, self.row_height, txt=title2, ln=0, align="L", border=1)
            pdf.cell(self.col_width3, self.row_height, txt=title3, ln=1, align="L", border=1)
        return pdf

    # function that prints pdf "body" contents
    def print_body_pdf(self, pdf_file, column1, column2, column3):
        # initialize variables
        pdf = pdf_file
        column1 = column1
        column2 = column2
        column3 = column3

        # Arial normal 8. Used for content rows
        pdf.set_font("Arial", '', size=8)

        # tests if table contents are longer than table cell for all three columns
        # tests if table contents are longer than table cell for the first column
        # if table contents are longer, the row heights of the other columns are accordingly adjusted
        if self.get_string_width(column1) > self.col_width1:
            # tests if the cell is almost at the bottom of the page, and thus should continue on the next page
            # this prevents cells from being distributed to two pages (only at the bottom of the page)
            if pdf.get_y() > (297 - pdf.b_margin - 2 * self.row_height):
                # force a line break
                pdf.ln(self.row_height)

            # multi_cell allows for line breaks
            # depending on user query different columns from txt file are printed
            pdf.multi_cell(self.col_width1, self.row_height, txt='{0}'.format(column1), align="L", border=1)
            # sets x and y coordinates adjacent to the previously written cell
            pdf.set_xy(self.l_margin + self.col_width1, pdf.get_y() - self.row_height * 2)
            pdf.multi_cell(self.col_width2, self.row_height * 2, txt='{0}'.format(column2), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1 + self.col_width2, pdf.get_y() - self.row_height * 2)
            pdf.multi_cell(self.col_width3, self.row_height * 2, txt='{0}'.format(column3), align="L", border=1)

        # tests if table contents are longer than table cell for the second column, same structure as for column 1
        elif self.get_string_width(column2) > self.col_width2:
            if pdf.get_y() > (297 - pdf.b_margin - 2 * self.row_height):
                pdf.ln(self.row_height)

            pdf.multi_cell(self.col_width1, self.row_height * 2, txt='{0}'.format(column1), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1, pdf.get_y() - self.row_height * 2)
            pdf.multi_cell(self.col_width2, self.row_height, txt='{0}'.format(column2), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1 + self.col_width2, pdf.get_y() - self.row_height * 2)
            pdf.multi_cell(self.col_width3, self.row_height, txt='{0}'.format(column3), align="L", border=1)

        # tests if table contents are longer than table cell for the third column, same structure as for column 1
        elif self.get_string_width(column3) > self.col_width3:
            if pdf.get_y() > (297 - pdf.b_margin - 2 * self.row_height):
                pdf.ln(self.row_height)

            pdf.multi_cell(self.col_width1, self.row_height * 2, txt='{0}'.format(column1), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1, pdf.get_y() - self.row_height * 2)
            pdf.multi_cell(self.col_width2, self.row_height * 2, txt='{0}'.format(column2), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1 + self.col_width2, pdf.get_y() - self.row_height * 2)
            pdf.multi_cell(self.col_width3, self.row_height, txt='{0}'.format(column3), align="L", border=1)

        # normal case when the contents are not too long
        else:
            pdf.multi_cell(self.col_width1, self.row_height, txt='{0}'.format(column1), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1, pdf.get_y() - self.row_height)
            pdf.multi_cell(self.col_width2, self.row_height, txt='{0}'.format(column2), align="L", border=1)
            pdf.set_xy(self.l_margin + self.col_width1 + self.col_width2, pdf.get_y() - self.row_height)
            pdf.multi_cell(self.col_width3, self.row_height, txt='{0}'.format(column3), align="L", border=1)

        # return full pdf
        return pdf


# initialize variables
full_list = []


# read data while txt file is open
with open('bestsellers2.txt') as fp:
    for line in fp:
        # separates data by tab
        line_list = line.split('\t')
        # add the separated data to the list
        full_list.append(line_list)


# function that adds a space before every capital letter [A-Z] in the data file
def capital_words_spaces(str1):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)


# add spaces to columns for title, author and publisher (column 1, 2 and 3)
for each_item in full_list:
    each_item[0] = (capital_words_spaces(each_item[0]))
    each_item[1] = (capital_words_spaces(each_item[1]))
    each_item[2] = (capital_words_spaces(each_item[2]))


# function to retrieve current time for timestamp in file name of PDF
def filename_timestamp():
    # retrieve current time using the timestamp function
    # apply DOS-compliant time format (YYYYMMDD_HHMMSS) for file name
    get_time = datetime.datetime.today()
    timestamp = datetime.datetime.strftime(get_time, '%Y%m%d_%H%M%S')
    return timestamp


# function to search by title
def search_by_title():
    # initialize variables
    title_list = []
    counter = 0

    # retrieve and store user input for title
    title_input = str(input("Title: "))

    # search function that creates a list of all results
    for item in full_list:
        # re.findall compares lower-letter input for user input and list to find matches
        if re.findall(title_input.lower(), item[0].lower()):
            result = re.findall(title_input.lower(), item[0].lower())
            list_set = set(result)
            unique_list = (list(list_set))
            # append each match to an empty list and increase counter by 1
            for _ in unique_list:
                title_list.append(item)
                counter = counter + 1

    # creating new instance of class PDF
    pdf = PDF()
    # start creating PDF in print_head_pdf function
    pdf = pdf.print_head_pdf(
        search_type='Title',
        search_term=title_input,
        counter=counter,
        sort_type='Title',
        title1='Title',
        title2='Author',
        title3='Date')

    # creates a sorted list of the results, sorted by title
    sorted_title_list = sorted(title_list, key=lambda x: x[0])
    # loop that prints results to the console and creates the contents of the pdf
    for item in sorted_title_list:
        print('{0}, by {1}, {2}'.format(item[0], item[1], item[3]))
        pdf.print_body_pdf(pdf, column1=item[0], column2=item[1], column3=item[3])

    # prints output when there was no match
    if counter == 0:
        print("There is no book with that Title")
    # print number of results
    if counter == 1:
        print(counter, 'result found')
    if counter > 1:
        print(counter, 'results found')

    # save pdf in output folder with current timestamp in file name
    pdf.output('output/bestseller_search_query_{0}.pdf'.format(filename_timestamp()), 'F')


# function to search by author
def search_by_author():
    # initialize counter variable that displays number of results
    counter = 0
    author_list = []
    # ask for author search input
    author_input = input("Author: ")

    # search function that creates a list of all results
    for item in full_list:
        # re.findall compares lower-letter input for user input and list to find matches
        if re.findall(author_input.lower(), item[1].lower()):
            result = re.findall(author_input.lower(), item[1].lower())
            list_set = set(result)
            unique_list = (list(list_set))
            # append each match to an empty list and increase counter by 1
            for _ in unique_list:
                author_list.append(item)
                counter = counter + 1

    # creating new instance of class PDF
    pdf = PDF()
    # start creating PDF in print_head_pdf function
    pdf = pdf.print_head_pdf(
        search_type='Author',
        search_term=author_input,
        counter=counter,
        sort_type='Title',
        title1='Title',
        title2='Author',
        title3='Date')

    # creates a sorted list of the results, sorted by title
    sorted_author_list = sorted(author_list, key=lambda x: x[0])
    # loop that prints results to the console and creates the contents of the pdf
    for item in sorted_author_list:
        print('{0}, by {1}, {2}'.format(item[0], item[1], item[3]))
        pdf.print_body_pdf(pdf, column1=item[0], column2=item[1], column3=item[3])

    # prints output when there was no match
    if counter == 0:
        print("There is no book written by that Author")
    # print number of results
    if counter == 1:
        print(counter, 'result found')
    if counter > 1:
        print(counter, 'results found')

    # save pdf in output folder with current timestamp in file name
    pdf.output('output/bestseller_search_query_{0}.pdf'.format(filename_timestamp()), 'F')


# function to search by a year range
def search_by_year():
    # retrieves current year as an integer variable
    this_year = int(datetime.datetime.strftime(datetime.datetime.today(), '%Y'))

    # input loop for start_year and end_year
    while True:
        try:
            # retrieve and store user input for start and end year
            start_year = int(input("Starting year: "))
            end_year = int(input("Ending year: "))
            # checks that the input is between 1900 and now, and that the start year is earlier than the end year
            if start_year in list(range(1900, this_year)) \
                    and end_year in list(range(1900, this_year)) \
                    and start_year <= end_year:
                break
            # returns a message if the years are not between 1900 and now
            elif start_year not in list(range(1900, this_year)) \
                    or end_year not in list(range(1900, this_year)):
                print("Please only use 4-digit year numbers between 1900 and {0}.".format(this_year))
                continue
            # returns a message if the start year is later than the end year
            elif start_year > end_year:
                print("The start year must be earlier than the end year.")
                continue
        # raise non-integer input
        except ValueError:
            print("Please provide integers only.")

    # initialize variables
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    range_dates = []
    counter = 0
    time_range_list = []

    # create a pretty table using PrettyTable
    table = PrettyTable(['Date', 'Title', 'Author'])
    table.align = "l"

    # transform dates from library to MM/DD/YYYY-format
    for date_item in full_list:
        # convert date column from text file to datetime format
        temp_a = datetime.datetime.strptime(str(date_item[3]), '%m/%d/%Y')
        # convert datetime to string, creates leading zeros for day and month to ensure consistency for search function
        temp_b = datetime.datetime.strftime(temp_a, "%m/%d/%Y")
        date_item[3] = temp_b

    # create a list for the time between user input (i.e. between start date and end date)
    for single_date in date_range(start_date, end_date):
        range_dates.append(single_date.strftime("%m/%d/%Y"))

    # loop that creates a list of all results
    for item in full_list:
        for date in range_dates:
            # append each match to an empty list and increase counter by 1
            if date in item[3]:
                time_range_list.append(item)
                counter = counter + 1

    # creating new instance of class PDF
    pdf = PDF()
    # start creating PDF in print_head_pdf function
    pdf = pdf.print_head_pdf(
        search_type='Year',
        search_term=str(start_year) + ' - ' + str(end_year),
        counter=counter,
        sort_type='Date',
        title1='Title',
        title2='Author',
        title3='Date')

    # creates a sorted list of the results, sorted by the date it reached bestseller
    sorted_time_range_list = sorted(time_range_list, key=lambda x: datetime.datetime.strptime(str(x[3]), '%m/%d/%Y'))
    # loop that creates content for the PrettyTable and creates the contents of the pdf
    for item in sorted_time_range_list:
        table.add_row(['{0}'.format(item[3]), '{0}'.format(item[0]), '{0}'.format(item[1])])
        pdf.print_body_pdf(pdf, column1=item[0], column2=item[1], column3=item[3])

    # prints output if there was no match
    if counter == 0:
        print("There was no book that reached bestseller between {0} and {1}.".format(start_year, end_year))
    # print number of results and PrettyTable if results are found
    if counter == 1:
        print(table)
        print(counter, 'result found')
    if counter > 1:
        print(table)
        print(counter, 'results found')

    # save pdf in output folder with current timestamp in file name
    pdf.output('output/bestseller_search_query_{0}.pdf'.format(filename_timestamp()), 'F')


# function to retrieve all days between start and end date from user input
def date_range(start_date, end_date):
    # each day between the start and end date is included
    # timedelta of plus one for end_date required as the end_date is not included in the range
    for n in range(int((end_date + datetime.timedelta(days=1) - start_date).days)):
        yield start_date + timedelta(n)


# function to search by a specific month and year
def search_by_month():
    # retrieves current year as an integer variable
    this_year = int(datetime.datetime.strftime(datetime.datetime.today(), '%Y'))
    # loop to retrieve and store month and year variable
    while True:
        try:
            # retrieve and store user input for month and year
            month = int(input("Please enter a month (1-12): "))
            year = int(input("Please enter a year: "))
            # break loop only if month is between 1 and 12 and year between 1900 and now
            if month in list(range(1, 13)) and year in list(range(1900, this_year)):
                break
            # allow for re-entering month and year variable in case it is not valid
            elif month not in list(range(1, 13)) and year not in list(range(1900, this_year)):
                print("Please only use integers between 1 and 12 for the month and "
                      "4-digit year numbers between 1900 and {0}.".format(this_year))
                continue
            # allow for re-entering month variable in case it is not between 1 and 12
            elif month not in list(range(1, 13)):
                print("Please only use integers between 1 and 12 for the month.")
                continue
            # allow for re-entering year variable in case it is not between 1900 and now
            elif year not in list(range(1900, this_year)):
                print("Please only use 4-digit year numbers between 1900 and {0}.".format(this_year))
                continue
        # raises non-integer input
        except ValueError:
            print("Please provide integers only.")

    # define start_date as the first day of the month and year from user input
    start_date = datetime.date(year, month, 1)
    # end date for each month
    # monthrange returns the start and end date of each month, its maximum is thus the month end day
    end_date = datetime.date(year, month, max(calendar.monthrange(year, month)))

    # initialize variables
    range_dates = []
    time_point_list = []
    counter = 0

    # create a pretty table using PrettyTable
    table = PrettyTable(['Date', 'Title', 'Author'])
    table.align = "l"

    # transform dates from library to MM/DD/YYYY-format
    for date_item in full_list:
        # convert date column from text file to datetime format
        temp_a = datetime.datetime.strptime(str(date_item[3]), '%m/%d/%Y')
        # convert datetime to string, creates leading zeros for day and month to ensure consistency for search function
        temp_b = datetime.datetime.strftime(temp_a, "%m/%d/%Y")
        date_item[3] = temp_b

    # create a list for the time between user input (i.e. between start date and end date)
    for single_date in date_range(start_date, end_date):
        range_dates.append(single_date.strftime("%m/%d/%Y"))

    # search function that creates a list of all results
    for item in full_list:
        for date in range_dates:
            if date in item[3]:
                time_point_list.append(item)
                counter = counter + 1

    # creating new instance of class PDF
    pdf = PDF()
    # start creating PDF in print_head_pdf function
    pdf = pdf.print_head_pdf(
        search_type='Month & Year',
        search_term=datetime.datetime.strftime(start_date, "%B") + ' ' + datetime.datetime.strftime(start_date, "%Y"),
        counter=counter,
        sort_type='Date',
        title1='Title',
        title2='Author',
        title3='Date')

    # creates a sorted list of the results, sorted by the date it reached bestseller
    sorted_time_range_list = sorted(time_point_list, key=lambda x: datetime.datetime.strptime(str(x[3]), '%m/%d/%Y'))
    # loop that prints results to the console and creates the contents of the pdf
    for item in sorted_time_range_list:
        table.add_row(['{0}'.format(item[3]), '{0}'.format(item[0]), '{0}'.format(item[1])])
        pdf.print_body_pdf(pdf, column1=item[0], column2=item[1], column3=item[3])

    # prints output if there was no match
    if counter == 0:
        print("No book reached bestseller in {0} {1}.".format(start_date.strftime("%B"), end_date.strftime("%Y")))
    # print number of results and PrettyTable if results are found
    elif counter == 1:
        print(table)
        print(counter, 'result found')
    elif counter > 1:
        print(table)
        print(counter, 'results found')

    # save pdf in output folder with current timestamp in file name
    pdf.output('output/bestseller_search_query_{0}.pdf'.format(filename_timestamp()), 'F')


# function to search by publisher
def search_by_publisher():
    # initialize variables
    counter = 0
    publisher_list = []

    # retrieve and store user input for title
    publisher_input = input("Publisher: ")

    # search function that creates a list of all results
    for item in full_list:
        # re.findall compares lower-letter input for user input and list to find matches
        if re.findall(publisher_input.lower(), item[2].lower()):
            result = re.findall(publisher_input.lower(), item[2].lower())
            list_set = set(result)
            unique_list = (list(list_set))
            for _ in unique_list:
                publisher_list.append(item)
                counter = counter + 1

    # creating new instance of class PDF
    pdf = PDF()
    # start creating PDF in print_head_pdf function
    pdf = pdf.print_head_pdf(
        search_type='Publisher',
        search_term=publisher_input,
        counter=counter,
        sort_type='Title',
        title1='Title',
        title2='Author',
        title3='Publisher')

    # creates a sorted list of the results, sorted by title
    sorted_publisher_list = sorted(publisher_list, key=lambda x: x[0])
    # loop that prints results to the console and creates the contents of the pdf
    for item in sorted_publisher_list:
        print('{0}, by {1}, {2}'.format(item[0], item[1], item[2]))
        pdf.print_body_pdf(pdf, column1=item[0], column2=item[1], column3=item[2])

    # prints output when there was no match
    if counter == 0:
        print("There is no book published by that Publisher")
    # print number of results
    if counter == 1:
        print(counter, 'result found')
    if counter > 1:
        print(counter, 'results found')

    # save pdf in output folder with current timestamp in file name
    pdf.output('output/bestseller_search_query_{0}.pdf'.format(filename_timestamp()), 'F')


# loop for user input to select the query to perform
while True:
    try:
        a = input("\nWhat task do you want to perform?\n"
                  " 1: Search for Title\n"
                  " 2: Search for Author\n"
                  " 3: Look up Year Range\n"
                  " 4: Look up Month/Year\n"
                  " 5: Search for Publisher\n")
        # runs the search functions depending on user input and afterwards gets back to the menu ("continue")
        if a == "1":
            search_by_title()
            continue
        elif a == "2":
            search_by_author()
            continue
        elif a == "3":
            search_by_year()
            continue
        elif a == "4":
            search_by_month()
            continue
        elif a == "5":
            search_by_publisher()
            continue
        # exit program by entering "q" or "Q"
        elif a == "q" or a == "Q":
            print("The program will not run anymore")
            quit()
        else:
            print("Please only provide integers from 1 to 5.")
    # raises non-integer input
    except ValueError:
        print("Please enter an integer between 1 and 5.")
