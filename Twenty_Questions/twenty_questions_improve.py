from random import choice

objects = ["elephant", "apple", "star", "guitar", "mountain", "rocket", "piano", "computer"]
object_attributes = {
    "elephant": {"size": "large", "color": "gray", "live": "yes", "animal": "yes"},
    "apple": {"size": "small", "color": "red", "live": "no", "animal": "no"},
    "star": {"size": "large", "color": "white", "live": "no", "animal": "no"},
    "guitar": {"size": "medium", "color": "varied", "live": "no", "animal": "no"},
    "mountain": {"size": "large", "color": "varied", "live": "no", "animal": "no"},
    "rocket": {"size": "large", "color": "white", "live": "no", "animal": "no"},
    "piano": {"size": "large", "color": "black", "live": "no", "animal": "no"},
    "computer": {"size": "medium", "color": "varied", "live": "no", "animal": "no"}
}


game_status = {
    "selected_object" : choice(objects),
    "questions_asked" : 0,
    "win" : False
    }


def display_start_game_messages():
    print("Welcome to 20 Questions!")
    print("Try to guess the object I'm thinking of within 20 questions!")
    print("You can ask questions about size, color, if it's alive, or if it's an animal.")


def validate_guess(guess:str, accepted_guesses:list[str]) -> bool:
    return guess in accepted_guesses


def ask_a_question():
    question = input("Ask a question: ").lower()
    if not validate_guess(question, ["size", "color", "alive", "animal"]):
        print("Sorry, I can't answer that question.")
        return ask_a_question()
    if "size" in question:
        print(f"The object is {object_attributes[game_status["selected_object"]]['size']}.")
    elif "color" in question:
        print(f"The object is {object_attributes[game_status["selected_object"]]['color']}.")
    elif "alive" in question:
        print(f"Is it alive? {object_attributes[game_status["selected_object"]]['live']}.")
    else: 
        print(f"Is it an animal? {object_attributes[game_status["selected_object"]]['animal']}.")
        

def guess_object():
    guess = input("Do you want to guess the object? (yes/no): ").lower()
    if not validate_guess(guess, ["yes", "no"]):
        print("Please enter yes or no")
        return guess_object
    if guess == "yes":
        your_guess = input("What is your guess? ").lower()
        if your_guess == game_status["selected_object"]:
            print("Congratulations! You guessed the correct object!")
            game_status["win"] = True
        else:
            print("Incorrect guess. Try again.")
           

def play_game():
    display_start_game_messages()
    while game_status["questions_asked"] < 20 and not game_status["win"]:
        ask_a_question()
        guess_object()
        game_status["questions_asked"] += 1

    if not game_status["win"]:
        print(f"Sorry, you've used all your questions. The object was: {game_status["selected_object"]}.")


if __name__ == "__main__":
    play_game()
