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
play = True
while play:
    for i in range(int(num)):
        data = respo[i]
        print(data)
        ans = input(f"Q. {data.get("question")} : ")
        if ans.lower() == data.get("correct_answer").lower():
            print("Correct!!!")
            score += 1
        else:
            print("Nah! It's Wrong")
    play = False



























    # quiz_type = input("Please select the quiz type : ")
    # print(quiz_type)
    # print(final_response.get("difficulty"))





