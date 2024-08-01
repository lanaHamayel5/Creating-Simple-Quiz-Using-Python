# Task 1: Simple Quiz implementaion
import json
 
score = 0

# Functions prototype
def check_answer(entered_answer, correct_answer):
    """Checks if user answers are correct or not and updates the score.
    Args:
        entered_answer (int): The user's answer.
        correct_answer (int): the correct answer.
        
    Returns:
        str: 'correct' if the answer is correct, otherwise 'wrong
    """ 
    global score

    if int(entered_answer) == correct_answer:        
        score += 1  # Increase score for a correct answer
        return "correct"
       
    else:
        return "wrong"
   
 
def get_valid_choice():
    
    """Ask user to enter a valid choice between 1 and 4
    
    Returns:
        int: The valid choice entered by the user.   
    """
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
    """Main function to run the simple quiz program.
       Reads questions from JSON file, presents them to user, checks answers,
       and updates score. Prints final score at the end.
    """
    global score  
    # Reading file  
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    num_of_options=1
    questions_count = 0
   
    for question_type in data['quiz'].keys():
        print(f"{question_type.capitalize()} Questions:")
        for q_value in data['quiz'][question_type].values():
            print(f"Question: {q_value['question']}\n")
            
            print("Options:")
            for option in q_value['options']:
                print(f"{num_of_options})  {option}")
                num_of_options+=1
            num_of_options=1
            print()  # Adds a newline for separation
            
            choice = get_valid_choice()
            
                
            for i in q_value['options']:
                if q_value['answer'] == i:
                    print((q_value['options'].index(q_value['answer']))+1)
                        
            result = check_answer(choice, (q_value['options'].index(q_value['answer']))+1)
            print(f"Your answer is {result}\n")
            print()  # Adds an extra newline for separation
            questions_count+=1
        
    #Present the final answer  
    print(f"Your final score = {score}/{questions_count}  ")
 
if __name__ == "__main__":
    main()
    