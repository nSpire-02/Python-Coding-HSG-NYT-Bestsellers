# NY Times Bestseller List

## Group Project #2263
This is a group project carried out by students of the University of St.Gallen in fall semester 2020 as part of the following courses:
* 3,793,1.00 - Skills: Programming - Introduction Level
* 7,789,1.00 - Skills: Programming with Advanced Computer Languages

## About
The goal of the project is to process the data file that contains the list of bestsellers books that reached number 1 and construct a list of books.
The user will then be able to choose different search functions to get the list of books that meet the choosen criteria.

## Prerequisites
This program works with Python 3.8.2

To run the program the following libraries need to be installed:
* Fpdf

```
pip install fpdf

```

To run the program the following libraries need to be imported:
* Datetime
* Re
* Calendar

```
pip install fpdf
import datetime
import re
import calendar

```

## Instructions
1. Read the menu option the program will display
2. Choose the option you want to perform
3. Input the variables that are asked 
4. Check the final list of books that meet your criteria
5. To quit the program input "q" or "Q"

## Files
Code:
Dataset:

## Description
All of the relevant libraries were downloaded as a first step. A list was created with all of the books in the data file.
Afterwards the data was cleaned to be viewed and understood in a better way. The 4 functions of the menu option were then defined.

* The first function is the search by the title of the book. The program asks the user a string input and then returns the subset of books that fullfil the criteria (the program is not case sensitive).
Each book of the subset will be displayed in the following way: title, author and date it reached number 1.
If the user chooses an invalid input the program will display an appropriate message.

* The second function is the search by author of the book. The program asks the user a string input and then returns the subset of books that fullfil the criteria (the program is not case sensitive).
Each book of the subset will be displayed in the following way: title, author and date it reached number 1.
If the user chooses an invalid input the program will display an appropriate message.

* The third function is the search by year range. The program asks the user for two years, the beginning year and the ending year. The function returns all of the books that reached number 1 between those years.
If the user chooses an invalid input the program will display an appropriate message. 
For the program to work the code associates the the first day of the year to the beginning year and the last day of the year to the ending year.
This way the subset includes all books that reached success between those years.
The code convertes the dates in the library file to python format to make a comparison between the inputed dates and the library dates possible.
The subset of books that will be displayed is sorted by date.

* The forth function is the search by a specific month and year. The program asks the user two inputs: a specific month and a specific year.
If the user chooses an invalid input the program will display an appropriate message.
The code convertes the dates in the library file to python format to make a comparison between the inputed dates and the library dates possible.
The subset of books that reached number 1 in that specific month and year will be displayed

The loop for the menu function was defined. The user can input "1", "2", "3" and "4" to run the first, second, third and fourth function respectively.
If the user chooses an invalid input the program will display an appropriate message.
The loop continues to run until the user decides to quit the program by choosing "q" or "Q"



## Sources
[Tutorial](http://youtu.be/O4hNpq3Aiig)

[Data file](https://drive.google.com/drive/folders/1xzpvleKVbRHnPR1SAKtJXcDCxg7K0Yhw)

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
