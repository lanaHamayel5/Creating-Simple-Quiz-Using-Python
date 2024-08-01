# Task 1: Simple Quiz implementaion
import json
 
values = [4, 1, 1, 1, 3, 4, 1]
 
score = 0
index = 0
 
# Functions prototype
def check_answer(entered_answer, correct_answer):
    global score,index
   
    # print(f"index = {index}")
    if int(entered_answer) == values[index]:        
        score += 1  # Increase score for a correct answer
        index+=1
        return "correct"
       
    else:
        index+=1
        return "wrong"
   
 
def get_valid_choice():
    while True:
        try:
            user_answer = int(input("Please, Enter the correct choice (1, 2, 3, 4): "))
            if user_answer in [1, 2, 3, 4]:
                return user_answer
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")
           
               
def main():  
    global score  
    # Reading file  
    with open('data.json', 'r') as file:
        data = json.load(file)
    # to make sure that the data was read correctlly
    # print(data)
 
    j=1
    questions_count = 0
    #Part1: Sport Questions
    print("Sport Questions:")
    for q_key, q_value in data['quiz']['sport'].items():
        print(f"Question: {q_value['question']}\n")
       
        print("Options:")
        for option in q_value['options']:
            print(f"{j})  {option}")
            j+=1
        j=1
        print()  # Adds a newline for separation
       
        choice = get_valid_choice()
       
        result = check_answer(choice, q_value['answer'])
        print(f"Your answer is {result}\n")
        print()  # Adds an extra newline for separation
        questions_count+=1
       
       
       
    # Part2: Math Questions
    print("Math Questions:")
    for q_key, q_value in data['quiz']['maths'].items():
        print(f"Question: {q_value['question']}\n")
       
        print("Options:")
        for option in q_value['options']:
            print(f"{j}) {option}")
            j+=1
        j=1
        print()
       
        choice = get_valid_choice()
       
        result = check_answer(choice, q_value['answer'])
        print(f"Your answer is {result}\n")
        print()  
        questions_count+=1
   
    #Present the final answer  
    print(f"Your final score = {score}/{questions_count}  ")
 
if __name__ == "__main__":
    main()