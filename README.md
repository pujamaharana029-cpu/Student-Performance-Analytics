Student Performance Analytics System

1. Project Objective

The objective of this project is to analyze student academic performance using Python, Pandas, and NumPy. The system calculates marks, averages, grades, results, and attendance statistics.

2. Technologies Used

- Python
- Pandas
- NumPy
- CSV for dataset storage
- Visual Studio Code

3. Dataset

The project uses a CSV dataset containing 15 student records with the following information:

- Student ID
- Student Name
- Python marks
- SQL marks
- HTML marks
- CSS marks
- JavaScript marks
- Attendance percentage

4. Key Features

- Loads student records from a CSV file.
- Calculates total and average marks for each student.
- Assigns grades based on average marks.
- Determines pass/fail status based on subject marks.
- Calculates subject-wise average marks.
- Identifies the top three students.
- Calculates the highest, lowest, and overall average subject marks using NumPy.
- Analyzes average attendance and identifies students with attendance below 75%.

5. Grading Rules

- Average >= 90: Grade A
- Average >= 80: Grade B
- Average >= 70: Grade C
- Average >= 60: Grade D
- Average >= 50: Grade E
- Average < 50: Grade F

A student passes when all five subject marks are at least 40.

6. How to Run the Project

1. Install Python.
2. Install the required libraries:
   "pip install pandas numpy"
3. Keep "main.py" and "students.csv" in the same folder.
4. Run:
   "python main.py"

7. Learning Outcomes

This project demonstrates the use of Python functions, loops, conditional statements, Pandas DataFrames, CSV files, and NumPy numerical calculations.

8. Project Files

- "main.py" — Main program and analysis.
- "students.csv" — Student dataset.
- "README.md" — Project documentation.

9. Future Improvements

- Add graphical charts for student performance.
- Allow users to enter new student records.
- Create a graphical user interface.
- Generate downloadable performance reports.