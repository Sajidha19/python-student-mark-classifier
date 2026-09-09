# 📊 Python Student Mark Classifier

A simple Python-based console program that evaluates student marks and assigns a performance classification using conditional logic and input validation.

## 📌 Project Overview

The **Student Mark Classifier** is an academic Python project designed to demonstrate basic programming concepts through a practical mark classification system.

The program accepts a student's mark between **0 and 100**, validates the input, and assigns a classification based on the defined grading criteria.

## 🎯 Classification Criteria

| Mark Range | Classification |
| ---------- | -------------- |
| 0–49       | Fail           |
| 50–69      | Credit         |
| 70–100     | Distinction    |

## ✨ Features

* Accepts student marks from **0 to 100**
* Classifies marks as **Fail, Credit, or Distinction**
* Handles decimal marks using `float`
* Validates marks above 100
* Handles non-numeric input using exception handling
* Allows the user to exit by entering a negative value
* Provides clear console output
* Uses a separate function for mark classification

## 🛠️ Technologies Used

* **Python**
* **VS Code / Python IDE**
* **Python Console / Terminal**

## 🧠 Programming Concepts Demonstrated

This project demonstrates:

* Functions
* Variables and data types
* User input
* `if`, `elif`, and `else` statements
* Comparison operators
* `while` loops
* Input validation
* `try-except` exception handling
* Formatted output
* Function return values
* `if __name__ == "__main__":`

## ▶️ How to Run

1. Clone or download this repository.
2. Open the project in any Python-supported development environment.
3. Run the following file:

```text
student_mark_classifier.py
```

4. Enter a mark when prompted.
5. The program will display the corresponding classification.

### Example

```text
=============================================
       MARK CLASSIFICATION SYSTEM
=============================================
Enter a mark between 0 and 100.
Enter a negative value to exit.

Enter mark: 75
Result: Distinction
```

### Invalid Input Example

```text
Enter mark: 120
Invalid mark. Please enter a value from 0 to 100.
```

```text
Enter mark: abc
Invalid input. Please enter a numeric mark.
```

## 🧪 Testing

The program was tested using different types of input to check the classification and validation logic.

| Test Input | Expected Result |
| ---------- | --------------- |
| 35         | Fail            |
| 49         | Fail            |
| 50         | Credit          |
| 65         | Credit          |
| 69         | Credit          |
| 70         | Distinction     |
| 85         | Distinction     |
| 100        | Distinction     |
| 120        | Invalid mark    |
| `abc`      | Invalid input   |
| -1         | Exit program    |



## 📚 Learning Outcome

This project helped develop an understanding of fundamental Python programming concepts, particularly **functions, conditional statements, loops, input validation, and exception handling**.

It also demonstrates how basic programming logic can be applied to a simple real-world academic scenario.

## 🚀 Possible Future Improvements

Future versions could include:

* Supporting multiple students
* Calculating the average mark
* Adding more classification categories
* Generating a summary report
* Storing student results in a file
* Adding a graphical user interface (GUI)

## 👩‍💻 Project Type

**Academic Python Project | First-Year BSc (Hons) Computing**

---

⭐ This project is part of my learning journey in Python programming and software development.
