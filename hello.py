# Simple Python example - Student Grade Calculator

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    students = [
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 78},
        {"name": "Charlie", "score": 85},
        {"name": "Diana", "score": 60},
        {"name": "Eve", "score": 45},
    ]

    print("=" * 35)
    print(f"{'Student':<10} {'Score':<10} {'Grade'}")
    print("=" * 35)

    for student in students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)
        print(f"{name:<10} {score:<10} {grade}")

    scores = [s["score"] for s in students]
    avg = sum(scores) / len(scores)
    print("=" * 35)
    print(f"Class Average score updated: {avg:.1f}")

if __name__ == "__main__":
    main()