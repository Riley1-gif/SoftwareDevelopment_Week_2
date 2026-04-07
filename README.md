# Software Development Week 2
# Week 2 Lab - Conditional Statements and Loops


## Overview

This Lab foccesed on understanding and applying the if else statements and loops in python. The goal was to analyse existing code, modifying conditions, and observe how different inputs affect program output

These tasks helped me build a strong foundation in the decision making logic, which i have found to be essential for controlling how programs behave


## Features and Functionality

File 1: Temperature Check

- Takes the temperature input from the user
- Converts temperature values
- Uses conditions to classify weather (hot, warm, cold or extreme)


File 2: Gradding System

- Asks for the students score
- Assigns a grade letter from A - F
- Provides a handy message to let them how they did (E.g. Excellent or Good)
- Handles invalid inputs (negative or above 100)


File 3: ATM Withdrawel System

- Requires PIN Verification before access
- Allows the user to withdraw there money
- Checks if the is suffcient balence to complete the transaction
- Handles basic ATM functions

File 4: Age Verification

- Takes the users age as input
- Determines if they are eligable to vote
- Identifies seniors of the age 65+
- Handles invalid age input like negative numbers



## How it Works

This lab mainly uses IF-Elif-Else statements to control the program flow.

- Conditions are used to check the users input
- bassed on the condition, different outputs are displayed
- If statements are used for example checking senior citizen status
- Functions are used in the ATM System to separate the logic in the program:
  - PinSystem() Handles the authentication
  - ATMSystem() Handles the transactions or withdrawels


## Key Concepts Learned from this lab

- How If-else statements control the decision making in a program
- How elif allows more than one condition to be checked
- Importance of input validation (Invalid score or Age)
- Basic use of functions to organise the code
- Understanding how programs flow changes bassed on the users input


## Notes and Possible Improvements

- Temperature conversion logic could be improved for accuracy
- ATM System could:
  - Limit withdrawal attempts
  - Add multiples of 10
- Grading system conditions could be reordered to validate input first
- Add While loops to allow repeated user interaction instead of restarting

