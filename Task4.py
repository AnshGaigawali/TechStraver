import random
def run_quiz(ques):
    score = 0
    random.shuffle(ques)  
    for q in ques:
        print(q['question'])
        options = q['options']
        random.shuffle(options)  
        for i, option in enumerate(options, 1):
            print(str(i) + ". " + option)
        
        user_answer = input("Your answer (enter the option number): ")
        
        while not user_answer.isdigit() or int(user_answer) not in range(1, len(options) + 1):
            print("Invalid input! Please enter a valid option number.")
            user_answer = input("Your answer (enter the option number): ")
        
        user_answer = int(user_answer)
        correct_answer = options.index(q['answer']) + 1
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            print("The correct answer is:", options[correct_answer - 1])
        
        print()  
    
    print("Quiz ended!")
    print("Your score:", score, "out of", len(ques))

ques = [
    {
        'question': 'Which anime series features characters known as "Shinigami" or Death Gods?',
        'options': ['Bleach', 'Death Note', 'Fairy Tail', 'Tokyo Ghoul'],
        'answer': 'Death Note'
    },
    {
        'question': 'Which movie won the Academy Award for Best Picture in 2020?',
        'options': ['Parasite', '1917', 'Joker', 'Once Upon a Time in Hollywood'],
        'answer': 'Parasite'
    },
    {
        'question': 'Who directed the movie "Inception"?',
        'options': ['Christopher Nolan', 'David Fincher', 'Martin Scorsese', 'Quentin Tarantino'],
        'answer': 'Christopher Nolan'
    },
    {
        'question': 'In "My Hero Academia," what is the name of the school where heroes are trained?',
        'options': ['U.A. High School', 'Hero Academy', 'Shinigami Academy', 'Konoha Academy'],
        'answer': 'U.A. High School'
    },
    {
        'question': 'Who is the main character in the anime "Attack on Titan"?',
        'options': ['Eren Yeager', 'Levi Ackerman', 'Mikasa Ackerman', 'Armin Arlert'],
        'answer': 'Eren Yeager'
    },
    {
        'question': 'Who is often referred to as the "King of Bollywood"?',
        'options': ['Shah Rukh Khan', 'Salman Khan', 'Amitabh Bachchan', 'Akshay Kumar'],
        'answer': 'Shah Rukh Khan'
    },
    {
        'question': 'Which Hollywood actor played the lead role in the "Pirates of the Caribbean" series?',
        'options': ['Brad Pitt', 'Johnny Depp', 'Tom Cruise', 'Leonardo DiCaprio'],
        'answer': 'Johnny Depp'
    },
    {
        'question': 'Which football club is known as "The Red Devils"?',
        'options': ['Manchester United', 'Real Madrid', 'FC Barcelona', 'Bayern Munich'],
        'answer': 'Manchester United'  
    },
    {
        'question': 'What is the name of the creature that Luffy aims to become in "One Piece"?',
        'options': ['Pirate King', 'Marine Admiral', 'Yonko', 'King of the Pirates'],
        'answer': 'King of the Pirates'
    },
    {
        'question': 'Who is the main protagonist in the anime "My Hero Academia"?',
        'options': ['Deku', 'Naruto', 'Goku', 'Luffy'],
        'answer': 'Deku'
    }
]

run_quiz(ques)