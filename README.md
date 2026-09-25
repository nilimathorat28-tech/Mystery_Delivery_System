# Mystery_Delivery_System
Python based logistics delivery simulator that assigns packages to the nearest delivery agent and generates a delivery performance report.

## Project Description
This project simulates one day of delivery operations. It assigns each package to the nearest delivery agent based on the distance between the agent and the warehouse.

The program calculates the total distance traveled by each agent and identifies the most efficient agent.

## Features
-Read and parse JSON data.

-Calculate Euclidean distance.

-Assign packages to the nearest delivery agent.

-Calculate total delivery distance.

-Calculate average distance per delivery.

-Identify the most efficient agent.

-Generate a delivery report in JSON format.

-Supports multiple test cases.

## Technologies Used
-Python 3.10

-JSON

-Math module

## Project Structure
'''
Mystery_Delivery_System/
│
├── Mystery_Delivery_System.py
│
├── test_cases/
│   ├── base_case.json
│   ├── test_case_1.json
│   ├── test_case_2.json
│   ├── test_case_3.json
│   ├── test_case_4.json
│   ├── test_case_5.json
│   ├── test_case_6.json
│   ├── test_case_7.json
│   ├── test_case_8.json
│   ├── test_case_9.json
│   └── test_case_10.json
│
└── report.json
'''
## How It Works
1.The program reads the JSON input file.
2.It reads the warehouse, agent, and package information.
3.It calculates the Euclidean distance between each agent and warehouse.
4.Each package is assigned to the nearest agent.
5.The program calculates the distance from the warehouse to the destination.
6.It calculates the total distance traveled by each agent.
7.It calculates the average distance per delivery.
8.It identifies the most efficient agent.
9.The final report is saved as report.json.

## How to Run
Open Mystery_Delivery_System.py using Python 3.10 and run the program.

To run a particular test case, change the file path in the program.

Example:
'''python
file_path = "test_cases/test_case_1.json"
'''
For the base case:
'''python
file_path = "test_cases/base_case.json"
'''

## Output
The program displays the delivery report in the console and saves the final result in:
'''text
report.json
'''

## Assignment
This project was created as part of a Python programming assignment focused on JSON parsing, distance calculation, package assignment, simulation, and report generation.

