# SQITK3073_Assignment1
Technical Manual Report

INTRODUCTION
This tax calculator program is developed in Python to assist Malaysian taxpayers in computing their annual income tax based on current tax rates and allowable reliefs. The application allows users login, calculate tax payable and store data for recordkeeping.

OBJECTIVE
-To create a simple command-line application that calculats tax payble
-To allow data saving and reading via a CSV file
-To provide a clear and interactive user interface

BACKGROUND
Malaysian taxpayers often struggle with understanding how tax rates and reliefs affect their payable tax. This tool helps users calculate tax and keep records efficiently using basic Python and CSV data mangement. The tax slab is based on LHDN published rates.

SETUP INSTRUCTION AND MANUAL
Requirements:
Python
pandas library
Manual:
1.Download the project from GitHub
2.Navigate into the project folder
3.Install pandas if not already installed:
  pip install pandas
4.Run the program by typing 'python main.py' in cmd
5.Enter IC number and password
6.Enter annual income
7.Enter your tax relief, the program will list the tax relief
8.The program will show your tax payable and save it CSV file

BASIC OPEERATIONS
Login: Use IC number and password of the user
Enter income and tax relief: Input your annual incomee and total tax relief
Tax payable calculation: Based on chargeable income
Data storage: Saved data in a CSV file named tax_data.csv
View Records: View previous data shown in a table

TROUBLESHOOTING AND FAQs
CSV file not saving
-Ensure Python has write access to the folder
Login fails
-Check 12 digits IC number and password is last 4 digits
pandas not gound
-Run pip install pandas, to install pandas

REFERENCES
-Lembaga Hasil Dalam Negeri Malaysia (LHDN)
-draw.io for flowchart creation

LINK TO GITHUB SOURCE CODE
