# NY Times Bestseller List

## Group Project #2263
This is a group project carried out by students of the University of St.Gallen in fall semester 2020 as part of the following courses:
* 3,793,1.00 - Skills: Programming - Introduction Level
* 7,789,1.00 - Skills: Programming with Advanced Computer Languages

## About
The goal of this Python project is to process a data file that contains the bestsellers books that reached number 1 according to the New York Times. A list of all books is created for which the user can select different search functions to get the subset of books that match the selected criteria.

## Prerequisites
This program was tested with Python 3.8.2 and 3.9.0. 

In order to run the program, the packages FPDF and Prettytable first need to be installed using the following commands:

```
pip install fpdf
pip install prettytable
```
FPDF is a library for PDF document generation under Python, ported from PHP. 
Prettytable is a simple Python library for easily displaying tabular data in a visually appealing ASCII table format.

## Instructions
1. Open the main.py Python project and run it
2. Read the menu option the program will display
3. Choose the option you want to perform
4. Input the variables that are asked 
5. Inspect the final list of books that meet your criteria either in the console or through the generated PDF file
6. To quit the program input "q" or "Q" in the menu


## Description
In a first step, all of the relevant libraries were downloaded. A list was then created with all books in the data file.
Afterwards the list was cleaned to be processed and displayed in a more comprehensive manner. Subsequently, further functions were implemented to generate a PDF file of all search results. Finally, the following 5 main functions for the menu option were defined:

* The first function is the search by the title of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. The search is conducted for case-insensitive substrings of a string.
All books from the subset will be displayed in alphabetical order with the following information: title, author and date it reached number 1. For every search, the program will create a PDF file with a list of the search parameters and the subset of books that met the search criteria.
If the user selects an invalid input, the program will display an appropriate message.

* The second function is the search by the author of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. The search is conducted for case-insensitive substrings of a string.
All books from the subset will be displayed in alphabetical order with the following information: title, author and date it reached number 1. For every search, the program will create a PDF file with a list of the search parameters and the subset of books that met the search criteria.
If the user selects an invalid input, the program will display an appropriate error message.

* The third function is the search for books that reached bestseller within a certain year range. The program asks the user for two years, the beginning year and the ending year, and then returns all books that reached number 1 in this timeframe.
If the user selects an invalid input, the program will display an appropriate error message. 
For the program to work the code associates the the first day of the year to the beginning year and the last day of the year to the ending year.
This way the subset includes all books that reached success between those years.
The code converts the dates in the library file to a common date format to allow for a comparison between the input dates and the library dates.
The subset of books will be displayed in a table format sorted by date. For every search, the program will create a PDF file with a list of the search parameters and the subset of books that met the search criteria.

* The forth function is the search by a specific month and year. The program asks the user for two inputs, a specific month and a specific year.
If the user selects an invalid input, the program will display an appropriate error message.
The code converts the dates in the library file to a common date format to allow for a comparison between the input dates and the library dates.
The subset of books that reached number 1 in that specific month and year will then be displayed sorted by date. For every search, the program will create a PDF file with a list of the search parameters and the subset of books that met the search criteria.

* The fifth function is the search by the publisher of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. The search is conducted for case-insensitive substrings of a string.
All books from the subset will be displayed in alphabetical order with the following information: title, author and publisher. For every search, the program will create a PDF file with a list of the search parameters and the subset of books that met the search criteria.
If the user selects an invalid input, the program will display an appropriate error message.

Finally, the loop for the menu function was defined. The user can input "1", "2", "3", "4" or "5" to run the first, second, third, fourth or fifth function, respectively.
If the user selects an invalid input, the program will display an appropriate error message.
The loop continues to run until the user decides to quit the program by entering "q" or "Q".

## Sample output
### Search for a title
```
What task do you want to perform?
 1: Search for Title
 2: Search for Author
 3: Look up Year Range
 4: Look up Month/Year
 5: Search for Publisher
1
Title: priv
Private, by James Patterson, 07/18/2010
Private Berlin, by James Pattersonand Mark Sullivan, 02/10/2013
Private Games, by James Pattersonand Mark Sullivan, 03/04/2012
Private Parts, by Howard Stern, 10/24/1993
Private:#1 Suspect, by James Pattersonand Maxine Paetro, 01/22/2012
See Here,Private Hargrove, by Marion Hargrove, 08/18/1942
6 result(s) found
```
PDF output: [Search for a title](https://github.com/nSpire-02/Python-Coding-HSG-NYT-Bestsellers/blob/main/output/bestseller_search_query_20201217_022043.pdf)

### Search for an author
```
What task do you want to perform?
 1: Search for Title
 2: Search for Author
 3: Look up Year Range
 4: Look up Month/Year
 5: Search for Publisher
2
Author: trump
Trump:Survivingatthe Top, by Donald Trump, 09/09/1990
Trump:The Artofthe Deal, by Donald Trump, 01/17/1988
2 result(s) found
```
PDF output: [Search for an author](https://github.com/nSpire-02/Python-Coding-HSG-NYT-Bestsellers/blob/main/output/bestseller_search_query_20201217_021644.pdf)

### Search for a year range
```
What task do you want to perform?
 1: Search for Title
 2: Search for Author
 3: Look up Year Range
 4: Look up Month/Year
 5: Search for Publisher
3
Starting year: 1964
Ending year: 1965
+------------+--------------------------------+------------------------+
| Date       | Title                          | Author                 |
+------------+--------------------------------+------------------------+
| 02/23/1964 | The Spy Who Cameinfromthe Cold | Johnle Carre           |
| 03/22/1964 | Four Days                      | U PI/American Heritage |
| 06/14/1964 | A Moveable Feast               | Ernest Hemingway       |
| 10/04/1964 | The Rectorof Justin            | Louis Auchincloss      |
| 10/25/1964 | Herzog                         | Saul Bellow            |
| 10/25/1964 | Reminiscences                  | Douglas Mac Arthur     |
| 12/20/1964 | Markings                       | Dag Hammarskjold       |
| 05/16/1965 | Upthe Down Staircase           | Bel Kaufman            |
| 07/11/1965 | The Source                     | James Michener         |
| 08/01/1965 | The Makingofthe President-1964 | Theodore H.White       |
| 10/31/1965 | Kennedy                        | Theodore Sorensen      |
+------------+--------------------------------+------------------------+
11 result(s) found
```
PDF output: [Search for a year range](https://github.com/nSpire-02/Python-Coding-HSG-NYT-Bestsellers/blob/main/output/bestseller_search_query_20201217_023851.pdf)

### Search for a specific month and year
```
What task do you want to perform?
 1: Search for Title
 2: Search for Author
 3: Look up Year Range
 4: Look up Month/Year
 5: Search for Publisher
4
Please enter a month (1-12): 3
Please enter a year: 2010
Fantasy In Death, by J.D.Robb, 03/14/2010
House Rules, by Jodi Picoult, 03/21/2010
No Apology, by Mitt Romney, 03/21/2010
Chelsea Chelsea Bang Bang, by Chelsea Handler, 03/28/2010
4 result(s) found
```
PDF output: [Search for a specific month and year](https://github.com/nSpire-02/Python-Coding-HSG-NYT-Bestsellers/blob/main/output/bestseller_search_query_20201217_024103.pdf)

### Search for a publisher
```
What task do you want to perform?
 1: Search for Title
 2: Search for Author
 3: Look up Year Range
 4: Look up Month/Year
 5: Search for Publisher
5
Publisher: Press
Against All Enemies, by Richard A.Clarke, Free Press
Arthritisand Common Sense, by Dale Alexander, Witkower Press
Embracedbythe Light, by Betty J.Eadie, Gold Leaf Press
Fiasco, by Thomas E.Ricks, The Penguin Press
First Among Equals, by Jeffrey Archer, Linden Press
In Defenseof Food, by Michael Pollan, Penguin Press
Losing It, by Valerie Bertinelli, Free Press
The Ageof Turbulence, by Alan Greenspan, Penguin Press
The Deathof Outrage, by William J.Bennett, Free Press
The Fire Next Time, by James Baldwin, Dial Press
The New English Bible, by Oxford University Press(Editor), Oxford University Press
The Prodigal Daughter, by Jeffrey Archer, Linden Press
The Sea Around Us, by Rachel Carson, Oxford University Press
13 result(s) found
```
PDF output: [Search for a publisher](https://github.com/nSpire-02/Python-Coding-HSG-NYT-Bestsellers/blob/main/output/bestseller_search_query_20201217_024309.pdf)

## Sources
* [YouTube Tutorial](http://youtu.be/O4hNpq3Aiig)

* [Data file](https://drive.google.com/drive/folders/1xzpvleKVbRHnPR1SAKtJXcDCxg7K0Yhw)

## Licensing

The code in this project is licensed under the terms of the [MIT license](https://opensource.org/licenses/MIT).
