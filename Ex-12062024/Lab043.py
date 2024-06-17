# write a program that calculates and display given numerical score
# (ex. A, B, C, D or E)
# A > 90
# B > 80 and B < 89
# C > 70 and C < 79
# D > 60 and D < 69
# F > 0 and F < 59

score = int(input("enter the score "))

if score >= 90 and score  <= 100:
    print("Grade is A")
elif score >= 80 and score <= 89:
    print("Grade is B")
elif score >= 70 and score <= 79:
    print("Grade is C")
elif score >= 60 and score <= 69:
    print("Grade is D")
elif score >= 0 and score <= 59:
    print("Grade is F")
else:
    print("Invalid score")