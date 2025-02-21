# quiz game

questions = ("What is the capital city of Nepal?",
             "What is the Scientific name of Human beings?",
             "How many continents are there ?",
             "What is the smallest country in the world?",
             "In which country was Gautam Buddha Born?")

options = (("A. Lalitpur", "B. Jhapa", "C. Illam", "D. Kathmandu"),
           ("A. Rana Tigrina", "B. Homo Sapiens", "C. Humano Beingo", "D. Being Human"),
           ("A. 6", "B. 9", "C. 77", "D. 7"),
           ("A. Vatican City", "B. Nepal", "C. Bhutan", "D. Russia"),
           ("A. Nepal", "B. India", "C. China", "D. Thailand"))

answers = ("D", "B", "D", "A", "A")
guesses = []
score = 0
question_number = 0
an = 0

neg = input("Do you want Negative Marking ? [Y/N] : ")
print("Thanks for confirming!")
for question in questions:
    print("*****************************")
    print(question)
    for option in options[question_number]:
        print(option)
    question_number+=1
    user_ans = input("Choose the correct option among A, B, C & D : ")
    if user_ans.upper() == answers[an]:
        print("Yes! Correct answer!")
        score = score +1
        print("Your current score is {}".format(score))
    else:
        print("Incorrect answer!")
        if neg.lower() == 'y':
            score-=1
        print("Your current score is {}".format(score))
    an+=1

print(f"Your final Quiz score is : {score}")

