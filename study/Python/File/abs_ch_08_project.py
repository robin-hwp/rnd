'''
Project: Generating Random Quiz Files
프로젝트 : 랜덤 퀴즈 파일 발생

Say you’re a geography teacher with 35 students in your class 
and you want to give a pop quiz on US state capitals. 
당신은 35명의 학생을 가르치는 지리 교사이고 미국 수도에 관한 퀴즈를 내고 싶어 합니다.

Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. 
아아, 당신반 중에 약간 안좋은 애들이 있고, 학생들이 부정행위를 하지 않는다는 확신이 없습니다.

You’d like to randomize the order of questions so that each quiz is unique, 
making it impossible for anyone to crib answers from anyone else. 
다른 사람으로 부터 답안지를 베껴서 만드는 것이 불가능하도록 각각의 문제가 유일하도록 순서를 무작위로 만들고 싶습니다.

Of course, doing this by hand would be a lengthy and boring affair. 
물론 손으로 이것을 하는 것은 길고 지루한 일 일것입니다.

Fortunately, you know some Python.
다행히 당신은 약간의 파이썬을 알고 있습니다.


Here is what the program does:
프로그램에서 할일

Creates 35 different quizzes.
35개의 다른 퀴즈들을 만든다.

Creates 50 multiple-choice questions for each quiz, in random order.
무작위 순서로 50개의 다중 선택 퀴즈를 만든다.

Provides the correct answer and three random wrong answers for each question, in random order.
무작위 순서로 각 문제마다 하나의 정답과 3개의 오답을 제공한다.

Writes the quizzes to 35 text files.
35개의 택스트 파일에 퀴즈를 쓴다.

Writes the answer keys to 35 text files.
35개의 텍스트 파일에 답안지를 쓴다.

This means the code will need to do the following:
이것은 코드가 아래에 나오는 것들을 해야할 필요가 있다는 것을 의미한다.

Store the states and their capitals in a dictionary.
사전에 주와 주의 수도를 저장하라.

Call open(), write(), and close() for the quiz and answer key text files.
문제지와 답지 파일을 위해서 open(), write()와 close()를 호출한다.

Use random.shuffle() to randomize the order of the questions and multiple-choice options.
다중 선택 옵션과 문제의 무작위 순서를 위해서 random.shuffle()을 사용한다.

'''
'''
# Step 1: Store the Quiz Data in a Dictionary
# 1단계 : 사전에 퀴즈 데이터를 저장

# The first step is to create a skeleton script and fill it with your quiz data. 
# 첫번째 단계는 뼈대 스크립트를 생성하고 거기에 퀴즈 데이터를 채우는 일이다.
# Create a file named randomQuizGenerator.py, and make it look like the following:
# 파일이름은 randomQuizGenerator.py로 생성하고 아래첨 만들어라


#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
'''

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt'%(quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt'%(quizNum+1), 'w')
    
    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
        answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
