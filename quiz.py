
questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "Carl and the Passions changed band name to what",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "How many rings on the Olympic flag",
                       "Who wrote the Opera Madam Butterfly",
                       "What is the largest state in the USA",
                       "In Greek mythology who killed the Gorgon",
                       "Which countries men use the most deodorant",
                       "In which country was Auschwitz",
                
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A.Ottmar Annett", "B.Clara Raphaela", "C.Beach Boys", "D.Arpi Trudi"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                    ("A. 5", "B. 7", "C. 2", "D. 9"),
                    ("A. Rosario", "B. Morena", "C. Atanasio", "D. Puccini"),
                    ("A. Alabama", "B. Alaska", "C.  Arizona", "D. Florida"),
                    ("A. Apiram", "B. Terams", "C.  Perseus", "D. Flopmid"),
                    ("A. Russia", "B. Usa", "C.  Morocco", "D. Japan"),
                    ("A. Russia", "B. Saudi Arabia", "C.  Piro", "D. Poland"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "C", "A", "A", "A","D", "B", "C", "D","D", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")

