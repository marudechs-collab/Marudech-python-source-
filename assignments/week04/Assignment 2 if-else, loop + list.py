scores = []

for i in range(1, 6):
    score = float(input(f"Enter score of student {i}: "))
    scores.append(score)

for score in scores:
    
    if score >=50:
        print(f"score {score} -> PASS ")

    else:
        print(f"score {score} -> fail")