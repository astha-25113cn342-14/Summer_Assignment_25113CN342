# Quiz Application

score = 0

print("Quiz Time!\n")

q1 = input("What is the capital of India? ")
if q1.lower() == "new delhi":
    score += 1

q2 = input("How many days are there in a week? ")
if q2 == "7":
    score += 1

q3 = input("What is 5 + 3? ")
if q3 == "8":
    score += 1

print("\nYour Score:", score, "/3")