# NY Times Bestseller List

## Group Project #2263
This is a group project carried out by students of the University of St.Gallen in fall semester 2020 as part of the following courses:
* 3,793,1.00 - Skills: Programming - Introduction Level
* 7,789,1.00 - Skills: Programming with Advanced Computer Languages

## About
The goal of this Python project is to process the data file that contains the list of bestsellers books that reached number 1 and construct a list of books.
The user will then be able to choose different search functions to get the list of books that meet the choosen criteria.

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
In a first step, all of the relevant libraries were downloaded. Then, a list was created with all of the books in the data file.
Afterwards the data was cleaned to be viewed and understood in a better way. Finally, the 5 main functions for the menu option were defined.

* The first function is the search by the title of the book. The program asks the user for a string input and then returns the subset of books that fulfill the criteria. The search is conducted for case-insensitive substrings of a string.
Each book of the subset will be displayed by alphabetic order in the following way: title, author and date it reached number 1.
If the user chooses an invalid input the program will display an appropriate message.

* The second function is the search by author of the book. The program asks the user a string input and then returns the subset of books that fulfill the criteria. The search is conducted for case-insensitive substrings of a string.
Each book of the subset will be displayed by alphabetic order in the following way: title, author and date it reached number 1.
If the user chooses an invalid input the program will display an appropriate message.

* The third function is the search by year range. The program asks the user for two years, the beginning year and the ending year. The function returns all of the books that reached number 1 between those years.
If the user chooses an invalid input the program will display an appropriate message. 
For the program to work the code associates the the first day of the year to the beginning year and the last day of the year to the ending year.
This way the subset includes all books that reached success between those years.
The code convertes the dates in the library file to python format to make a comparison between the inputed dates and the library dates possible.
The subset of books will be sorted by date and displayed in a tablet format.

* The forth function is the search by a specific month and year. The program asks the user two inputs: a specific month and a specific year.
If the user chooses an invalid input the program will display an appropriate message.
The code convertes the dates in the library file to python format to make a comparison between the inputed dates and the library dates possible.
The subset of books that reached number 1 in that specific month and year will be displayed sorted by date.

* The fifth function is the search by publisher of the book. The program asks the user a string input and then returns the subset of books that fulfill the criteria. The search is conducted for case-insensitive substrings of a string.
Each book of the subset will be displayed by alphabetic order in the following way: title, author and publisher.
If the user chooses an invalid input the program will display an appropriate message.

* After every search, the program will create a pdf file with a list of the subset of books that met the search criteria. The search parameters (search function, search query, search item and number of results) will be displayed on the first page of the PDF.

The loop for the menu function was defined. The user can input "1", "2", "3", "4" and "5" to run the first, second, third, fourth and fifth function respectively.
If the user chooses an invalid input the program will display an appropriate message.
The loop continues to run until the user decides to quit the program by choosing "q" or "Q"



## Sources
* [YouTube Tutorial](http://youtu.be/O4hNpq3Aiig)

* [Data file](https://drive.google.com/drive/folders/1xzpvleKVbRHnPR1SAKtJXcDCxg7K0Yhw)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be
```
``` 
```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Licensing

The code in this project is licensed under the terms of the [MIT license](https://opensource.org/licenses/MIT).
