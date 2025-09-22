import sys

# Uttarakhand Quiz Questions
quiz_data = {
    "Beginner": [
        {"q": "What is the capital of Uttarakhand?", "options": ["Dehradun", "Nainital", "Haridwar", "Rishikesh"], "answer": "Dehradun"},
        {"q": "Which flower is the state flower of Uttarakhand?", "options": ["Lotus", "Brahma Kamal", "Rhododendron", "Sunflower"], "answer": "Brahma Kamal"},
        {"q": "Which river originates from Gangotri Glacier?", "options": ["Yamuna", "Ganga", "Saraswati", "Mandakini"], "answer": "Ganga"},
        {"q": "Which tree is the state tree of Uttarakhand?", "options": ["Oak", "Buransh (Rhododendron)", "Deodar", "Pine"], "answer": "Buransh (Rhododendron)"},
        {"q": "Which animal is the state animal of Uttarakhand?", "options": ["Snow Leopard", "Musk Deer", "Tiger", "Elephant"], "answer": "Musk Deer"},
        {"q": "Nainital is famous for which type of natural attraction?", "options": ["Waterfalls", "Lakes", "Mountains", "Caves"], "answer": "Lakes"},
        {"q": "Which is the state bird of Uttarakhand?", "options": ["Monal", "Peacock", "Eagle", "Hornbill"], "answer": "Monal"},
        {"q": "Where is the famous Ganga Aarti performed in Uttarakhand?", "options": ["Rishikesh", "Dehradun", "Nainital", "Haridwar"], "answer": "Haridwar"},
    ],
    "Intermediate": [
        {"q": "In which year was Uttarakhand formed as a separate state?", "options": ["1998", "2000", "2002", "2005"], "answer": "2000"},
        {"q": "Which is the official language of Uttarakhand?", "options": ["Hindi", "Garhwali", "Kumaoni", "English"], "answer": "Hindi"},
        {"q": "Jim Corbett National Park is famous for which animal?", "options": ["Tiger", "Elephant", "Leopard", "Deer"], "answer": "Tiger"},
        {"q": "Which lake is known as the 'Lake District of India'?", "options": ["Bhulla Tal", "Naini Lake", "Sattal", "Nainital"], "answer": "Nainital"},
        {"q": "Valley of Flowers is located in which district?", "options": ["Chamoli", "Almora", "Pithoragarh", "Rudraprayag"], "answer": "Chamoli"},
        {"q": "Which dance form is famous in Kumaon region?", "options": ["Chholiya", "Kathak", "Bhangra", "Garba"], "answer": "Chholiya"},
        {"q": "Tehri Dam is built on which river?", "options": ["Ganga", "Bhagirathi", "Yamuna", "Mandakini"], "answer": "Bhagirathi"},
        {"q": "Which city is known as the 'Yoga Capital of the World'?", "options": ["Haridwar", "Dehradun", "Rishikesh", "Nainital"], "answer": "Rishikesh"},
    ],
    "Hardcore": [
        {"q": "Who was the first Chief Minister of Uttarakhand?", "options": ["N.D. Tiwari", "B.C. Khanduri", "Nityanand Swami", "Harish Rawat"], "answer": "Nityanand Swami"},
        {"q": "Chipko Movement is associated with which district of Uttarakhand?", "options": ["Chamoli", "Almora", "Pauri", "Tehri"], "answer": "Chamoli"},
        {"q": "What is the approximate height of Nanda Devi peak?", "options": ["6,781 m", "7,816 m", "7,434 m", "8,848 m"], "answer": "7,816 m"},
        {"q": "Gaumukh is the source of which river?", "options": ["Alaknanda", "Mandakini", "Bhagirathi", "Ganga"], "answer": "Bhagirathi"},
        {"q": "Who led the famous Chipko Movement?", "options": ["Chandi Prasad Bhatt", "Sundarlal Bahuguna", "Gaura Devi", "All of the above"], "answer": "All of the above"},
        {"q": "Which pass connects Uttarakhand with Tibet?", "options": ["Niti Pass", "Rohtang Pass", "Mana Pass", "Shipki La"], "answer": "Mana Pass"},
        {"q": "Where is the Hemkund Sahib located?", "options": ["Chamoli", "Pithoragarh", "Tehri", "Almora"], "answer": "Chamoli"},
        {"q": "Which famous personality wrote the book 'Our Trees Still Grow in Dehra'?", "options": ["Ruskin Bond", "R.K. Narayan", "Vikram Seth", "Khushwant Singh"], "answer": "Ruskin Bond"},
    ]
}


def run_quiz():
    print("\n Welcome to the Uttarakhand Quiz ")
    score = 0

    for level, questions in quiz_data.items():
        print(f"\n--- {level} Level ---")
        for idx, q in enumerate(questions, 1):
            print(f"\nQ{idx}. {q['q']}")
            for i, opt in enumerate(q['options'], 1):
                print(f"  {i}. {opt}")

            try:
                user_choice = int(input("Your answer (1-4): "))
                if q['options'][user_choice - 1] == q['answer']:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer: {q['answer']}")
            except (ValueError, IndexError):
                print("Invalid input. Skipping question.")

    print("\n Quiz Over!")
    print(f"Your total score: {score}/{sum(len(v) for v in quiz_data.values())}")


if __name__ == "__main__":
    run_quiz()
