a = input("grade obtain in m1")
b = input("grade obtain in chem")
c = input("grade obtain in pps")
d = input("grade obtain in iks")
e = input("grade obtain in bee")
g = input("grade obtain in cw")
h = input("grade obtain in yoga")
i = input("grade obtain in lchem")
j = input("grade obtain in lpps")
k = input("grade obtain in lbee")

subjects = ["m1", "chem", "pps", "iks", "bee", "cw", "yoga", "lchem", "lpps", "lbee"]
credits = [4, 3, 3, 2, 2, 2, 2, 1, 1, 1]

grade_points = {
    "A++": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
}

total_credit_points = 0
for subject, credit, grade in zip(subjects, credits, [a, b, c, d, e, g, h, i, j, k]):
    for g in grade.split():  # Split the input string into characters
        grade_point = grade_points.get(g, 0)  # Handle invalid grades gracefully
        subject_credit_points = credit * grade_point
        total_credit_points += subject_credit_points

sgpa = total_credit_points / sum(credits)

print("SGPA:", sgpa)
