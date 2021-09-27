from Question import Question


quiz=[
    "What is our National animal?\n(a)Bengal Tiger\n(b)Lion\n(c)Leopard\n\n",
    "What is color of Sun?\n(a)Yellow\n(b)Reddish Yellow\n(c)Blue\n\n"
    ]
questions=[
    Question(quiz[0], 'a'),
    Question(quiz[1], 'b')
    ]


quiz2=[
       "Who is the father of modern science?\n(a)Albert Einstein\n(b)Issac Newton\n(c)Nikola Tesla\n\n",
       "What is our national fruit?\n(a)Mango\n(b)Banana\n(c)Grapes\n\n"
       ]
quesQuiz2=[
    Question(quiz2[0],'a'),
    Question(quiz2[1],'a')
    ]

def run_test(questions):
    score=0
    for question in questions:
        answer=input(question.togive)
        if answer==question.answer:
            score+=1
    print("Your score is "+ str(score)+"/"+str(len(questions))+"correct")
    for question in questions:
                print("The correct answers are "+ question.answer)
    
def run_test(quesQuiz2):
    score=0
    for question in quesQuiz2:
        answer=input(question.togive)
        if answer==question.answer:
            score+=1
    print("Your score is "+ str(score)+"/"+str(len(quesQuiz2))+"correct")
    for question in quesQuiz2:
        print("The correct answers are "+ question.answer)

#run_test(questions)


run_test(quesQuiz2)