import requests

#
# difficult = input("Select the difficulty level of the quiz (easy, medium, hard) : ").lower()
# cate = input("Select the category (entertainment=11, sports=21, science=17, geography=22, history=23, politics=24, celebrities=26) : ").capitalize()
# num = input("How many questions do you want ? : ")

main = "https://opentdb.com/api.php?amount=5"

num="3"
cate="17"
difficult = "easy"

url = f"https://opentdb.com/api.php?amount={num}&category={cate}&difficulty={difficult}"
# print(url)

response = requests.get(url)
# print(response)

final_response = response.json()
# print(type(final_response))
# print(final_response)
respo = final_response.get("results")
# print(respo)
# print(respo[0].get("difficulty"))

# for items in respo:
#     print(items)

score = 0
correct = 0
incorrect = 0

incorrect_ques = {}
incorrect_ans = []

play = True
while play:
    for i in range(int(num)):
        data = respo[i]
        print()
        print(f"{i+1}. {data.get("question")}")
        c = data.get('correct_answer')
        print(f"\ta) {c}")
        bullet = ["b", "c", "d"]
        t = 0
        for y in data.get('incorrect_answers'):
            print(f"\t{bullet[t]}) {y}")
            t += 1
        ans = input("Choose your answer : ")
        if ans.lower() == c.lower():
            score += 1
            correct += 1
        else:
            incorrect_ques[f"{data.get('question')}"] = f"{data.get('correct_answer')}"
            incorrect_ans.append(ans)
            incorrect += 1
    play = False
    print(f"Correct ✅ : {correct}\nIncorrect ❌ : {incorrect}\nTotal Score : {score}")
    for (key,value), incorrect_a in zip(incorrect_ques.items(), incorrect_ans):
        print("-------------------------------------------------------------------------------")
        print(f"Q. {key}")
        print(f"Correct answer : {value}")
        print(f"Your Answer: {incorrect_a}")
    print("-------------------------------------------------------------------------------")



























    # quiz_type = input("Please select the quiz type : ")
    # print(quiz_type)
    # print(final_response.get("difficulty"))





