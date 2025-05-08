#Import Library of Choice
import random

#Read questions from the saved file
def load_questions_from_file(filename="quiz_questions.txt"):
    questions = []
    try:
        with open(filename, "r") as file:
            content = file.read().strip().split("---n")
            for block in content:
                lines = block.strip().split("\n")
                if len(lines)>= 6:
                    question_text = lines [0].replace("Question: ", "")
                    choices = {
                        'a': lines [1][3].strip(),
                        'b': lines [2][3].strip(),
                        'c': lines [3][3].strip(),
                        'd': lines [4][3].strip()
                    }
                    correct_choice= lines[5].replace("The correct answer is: ", "").strip()
                    questions.append({
                        "question": question_text,
                        "options": choices,
                        "answer": correct_choice
                    })
        return questions
    except FileNotFoundError:
        print("No quiz questions found. Make sure to run the quz_maker_game before running the program.")    
#Ask a question to the user and check the answer

#Run the quiz game