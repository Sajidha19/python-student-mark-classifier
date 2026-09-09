# Mark Classification System
# Academic Python Project
# Classifies marks into Fail, Credit, or Distinction.


def classify_mark(mark):
    """
    Classify a mark according to the grading criteria.

    0–49   : Fail
    50–69  : Credit
    70–100 : Distinction
    """

    if mark < 50:
        return "Fail"
    elif mark < 70:
        return "Credit"
    else:
        return "Distinction"


def main():
    """Run the mark classification program."""

    print("=" * 45)
    print("       MARK CLASSIFICATION SYSTEM")
    print("=" * 45)
    print("Enter a mark between 0 and 100.")
    print("Enter a negative value to exit.")
    print()

    while True:
        try:
            mark = float(input("Enter mark: "))

            # Exit condition
            if mark < 0:
                print("\nThanks. See you next time!")
                break

            # Validate mark range
            if mark > 100:
                print("Invalid mark. Please enter a value from 0 to 100.\n")
                continue

            # Classify and display result
            result = classify_mark(mark)
            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid input. Please enter a numeric mark.\n")


if __name__ == "__main__":
    main()