# Task 1
import json

score = 0

# Functions prototype
def checkAnswer(enteredAnswer, correctAnswer):
    global score  
    if enteredAnswer.lower() == correctAnswer.lower():
        score += 1  # Increase score for a correct answer
        return "correct"
    else:
        score -= 1  # Decrease score for a wrong answer
        return "wrong"
  
  
# Reading file   
with open('data.json', 'r') as file:
    data = json.load(file)
# to make sure that the data was read correctlly
# print(data) 



numOfquestions = 0
#Part1: Sport Questions
print("Sport Questions:")
for q_key, q_value in data['quiz']['sport'].items():
    print(f"Question: {q_value['question']}\n")
    
    print("Options:")
    for option in q_value['options']:
        print(f"{option}")
    print()  # Adds a newline for separation
    
    userAnswer = input("Please, Enter the correct choice: ")
    result = checkAnswer(userAnswer, q_value['answer'])
    print(f"Your answer is {result}\n")
    print()  # Adds an extra newline for separation
    numOfquestions+=1
    
    
    
# Part2: Math Questions
print("Math Questions:")
for q_key, q_value in data['quiz']['maths'].items():
    print(f"Question: {q_value['question']}\n")
    
    print("Options:")
    for option in q_value['options']:
        print(f"{option}")
    print()
    
    userAnswer = input("Please, Enter the correct choice: ")
    result = checkAnswer(userAnswer, q_value['answer'])
    print(f"Your answer is {result}\n")
    print()  
    numOfquestions+=1
    


#Present the final answer  
if score < 0:
    score = 0
    print(f"Your final score = {score}/{numOfquestions}  ")
else:
    print(f"Your final score = {score}/{numOfquestions}  ")
# print(f"number of q = {numOfquestions}")
