a = input("grade obtain in m2:")
b = input("grade obtain in phy:")
c = input("grade obtain in bee:")
d = input("grade obtain in bme:")
e = input("grade obtain in co:")
f = input("grade obtain in cs:")
g = input("grade obtain in exp:")
h = input("grade obtain in club:")
i = input("grade obtain in lphy:")
j = input("grade obtain in lbee:")
k = input("grade obtain in lbme:")

subjects = ["m2", "phy", "bee", "bme", "co", "cs", "exp", "club", "lphy", "lbee", "lbme"]
credits = [4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1]

grade_points = {
    "A++": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
}

total_credit_points = 0
for subject, credit, grade in zip(subjects, credits, [a, b, c, d, e, f, g, h, i, j, k]):
    for g in grade.split():  # Split the input string into characters
        grade_point = grade_points.get(g, 0)  # Handle invalid grades gracefully
        subject_credit_points = credit * grade_point
        total_credit_points += subject_credit_points

sgpa = total_credit_points / sum(credits)

print("SGPA:", sgpa)
