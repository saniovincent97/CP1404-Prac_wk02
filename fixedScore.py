def main():
    score = float(input("Enter score: "))
    grade = check_marks(score)
    print(grade)


def check_marks(score):
    if score < 0:
        msg = "Invalid score"
    elif score > 100:
        msg = "Invalid score"
    elif score >= 50:
        msg = "Passable"
    elif score > 90:
        msg = "Excellent"
    if score < 50:
        msg = "Bad"
    return msg

main()