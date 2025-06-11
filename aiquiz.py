import openai

openai.api_key = "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"  # o monadikos kwdikos gia na kserei to chatgpt poios zitaei tin pliroforia


questions = [] # lista giati tha exw polles erwtiseis
current_question = 0
asked_questions = set() # apothikeyontai oi monadikes erwtiseis
score = 0

def generate_questions():
    for i in range(10):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages =[
                {"role": "system",
                 "content": "Generate a simple yes/no question in English about"+ quiz_type +", "
                            "suitable for students up to 18 years old, with a clear correct answer. Return the format: "
                            "'Question: <question> | Answer: <yes/no>'. Ensure the question is unique and not in: " + ", ".join(
                     asked_questions) + "."},
                {"role": "user", "content": "Generate a simple yes/no question."}
            ]
        )
        # 'Question: Is sky blue | Answer: yes'
        result = response.choices[0].message["content"].strip() # to strip afairei tuxon kena prin h meta to keimeno thelw
        question, answer = result.split(" | ") # question = "Question: Is sky is blue", answer = "Answer: yes"
        question = question.replace("Question: ", "") # question = "Is sky is blue"
        answer = answer.replace("Answer: ", "").rstrip(".").lower() # answer = "yes"
        if question not in asked_questions:
            asked_questions.add(question)
            return question, answer
    return "Is this a default question?", "yes" # se periptwsi pou laggarei to chatgpt kai den dinei kainouries erwtiseis

def start_quiz():
    global current_question, quiz_type
    print("Let's start the game!")
    quiz_type = input("Choose category: ")
    for i in range(5):
        questions.append(generate_questions())

    while current_question < len(questions): # loop gia na apantisws oles tis erwtiseis pou exw
        question, correct_answer = questions[current_question] # spaw tin pliroforia se 2 variables (erwtisi + apantisi)
        #print("Question: ", question, " Answer: ", correct_answer)
        print("Question", current_question + 1, ":", question)
        user_answer = input("Answer (yes/no): ").strip()
        while user_answer not in ["yes", "no"]: # perimenei mexri na apantiseis yes/no, den dexetai allou eidous apantisi
            user_answer = input("Answer (yes/no): ").strip()
        if user_answer == correct_answer.lower(): # to correct answer tha einai olo me MIKRA grammata
            print("Correct!")
            #score += 1
        else:
            print("Wrong!")

        current_question += 1 # auksanw kata 1 gia na paw stin epomeno erwtoapantisi

    print("you answered"+str(score)+"/"+str(len(questions))+" questions")
    restart = input("do you want to play again?")
    if restart.lower() == "yes":
        restart_quiz()
    else:
        print("Thanks for playing!")

def restart_quiz():
    global score, questions, current_question
    score=0
    questions = []
    current_question= 0
    start_quiz()

if __name__ == "__main__":
    print("Welcome to my AI Generated Quiz!")
    start_quiz()