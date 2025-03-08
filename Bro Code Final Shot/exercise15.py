import requests

def play_game():
    play = True
    while play:

        difficult = input("Awesome! Can you please select the difficulty level of the quiz (easy, medium, hard) : ").lower()
        cate = input("Nice! Now select the category (entertainment=11, sports=21, science=17, geography=22, history=23, politics=24, celebrities=26) : ").capitalize()
        num = input("Great! Now how many questions do you want me to ask you ? : ")

        # num = "3"
        # cate = "17"
        # difficult = "easy"

        url = f"https://opentdb.com/api.php?amount={num}&category={cate}&difficulty={difficult}"

        response = requests.get(url)

        final_response = response.json()
        respo = final_response.get("results")
        score = 0
        correct = 0
        incorrect = 0
        incorrect_ques = {}
        incorrect_ans = []
        print()
        print("**************** GK Game ********************** ")
        print()
        for i in range(int(num)):
            data = respo[i]
            print(f"{i+1}. {data.get("question")}")
            c = data.get('correct_answer')
            print(f"\ta) {c}")
            bullet = ["b", "c", "d"]
            t = 0
            for y in data.get('incorrect_answers'):
                print(f"\t{bullet[t]}) {y}")
                t += 1
            ans = input("Choose your answer : ")
            print()
            if ans.lower() == c.lower():
                score += 10
                correct += 1
            else:
                incorrect_ques[f"{data.get('question')}"] = f"{data.get('correct_answer')}"
                incorrect_ans.append(ans)
                incorrect += 1
        print()
        print("**************** Result :  **********************")
        print()
        print(f"Correct ✅ : {correct}\nIncorrect ❌ : {incorrect}\nTotal Score : {score} out of {int(num)*10}")
        print()
        print("-------------------------------------------------------------------------------")
        print()
        for (key,value), incorrect_a in zip(incorrect_ques.items(), incorrect_ans):
            print(f"Q. {key}")
            print(f"Correct answer : {value}")
            print(f"Your Answer: {incorrect_a}")
        print()
        print("-------------------------------------------------------------------------------")
        print()
        play_again = input("Do you wanna start again ? : ").lower()
        while play_again not in ["yes", "y", "no", "n", "sure"]:
            play_again = input("Enter valid input you fool 😤 Do you wanna start again ? : ")
        play = True if play_again in ["Y", "yes", "sure"] else print("Ok! Play again next time!")


if __name__ == "__main__":
    inp = input("Hey! Do you want to test your brain ? 🫵 I mean wanna play Quiz ? 🤔 : ").lower()
    while inp not in ["yes", "y", "no", "n", "sure", "no"]:
        inp = input("Enter valid input you fool 😤 : ")
    play_game() if inp in ["y", "yes", "sure"] else print("Fine! Come back Later Looser 😆 ")


