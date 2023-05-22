from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():

    import os
    import random
    import getpass
    import time
    import datetime
    from cards import cards, card_values

    play = False
    stucked = False
    score = 0
    dealerScore = 0
    credits = 0
    current_user = ""

    def clear_console():
        time.sleep(2)
        # Clear the console based on the operating system
        if os.name == "nt":  # For Windows
            _ = os.system("cls")
        else:  # For Unix-based systems (Linux, macOS)
            _ = os.system("clear")

    def wfui():
        input("Press Enter to continue")

    def log_login(username):
        with open("logs/logs.txt", "a") as logs:
            pass
        # Get the current time
        current_time = datetime.datetime.now()
        # Convert the current time to a string representation
        current_time_string = current_time.strftime("%Y-%d-%m %H:%M:%S")
        with open("logs/logs.txt", "a") as logs:
            logs.write(username + ", " + current_time_string + " ACTION: Log In"+ "\n")
        
    def log_logout(username):
        with open("logs/logs.txt", "a") as logs:
            pass
        # Get the current time
        current_time = datetime.datetime.now()
        # Convert the current time to a string representation
        current_time_string = current_time.strftime("%Y-%d-%m %H:%M:%S")
        with open("logs/logs.txt", "a") as logs:
            logs.write(username + ", " + current_time_string + " ACTION: Log Out"+ "\n")

    def log_signup(username):
        with open("logs/logs.txt", "a") as logs:
            pass
        # Get the current time
        current_time = datetime.datetime.now()
        # Convert the current time to a string representation
        current_time_string = current_time.strftime("%Y-%d-%m %H:%M:%S")
        with open("logs/logs.txt", "a") as logs:
            logs.write(username + ", " + current_time_string + " ACTION: Sign Up"+ "\n")

    def log_gamestart(username):
        with open("logs/logs.txt", "a") as gameplay:
            pass
        # Get the current time
        current_time = datetime.datetime.now()
        # Convert the current time to a string representation
        current_time_string = current_time.strftime("%Y-%d-%m %H:%M:%S")
        with open("logs/gameplay.txt", "a") as gameplay:
            gameplay.write(username + ", " + current_time_string + " ACTION: Start game"+ "\n")


    def log_gameend(username, score, dealerScore):
        with open("logs/logs.txt", "a") as gameplay:
            pass
        # Get the current time
        current_time = datetime.datetime.now()
        # Convert the current time to a string representation
        current_time_string = current_time.strftime("%Y-%d-%m %H:%M:%S")
        with open("logs/gameplay.txt", "a") as gameplay:
            gameplay.write(username + ", " + current_time_string + " ACTION: Finish game " + "Score: " + str(score) + " and dealer score: " +  str(dealerScore) + "\n")
        
    def create_user(username, password):
        # Create the text file if it doesn't exist.
        with open("users.txt", "a") as f:
            pass

        # Write the username and password to the text file.
        with open("users.txt", "a") as f:
            f.write(username + ":" + password + "\n")

        # Print a message to confirm that the user has been created.
        print("User {} has been created successfully!".format(username))

    def login(username, password):
        # Check if the username and password are in the text file.
        with open("users.txt", "r") as f:
            for line in f:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and password == stored_password:
                    return True

        # If the username and password are not in the text file, return False.
        return False
    def get_credits(username):
        # Load the credits for the specified user from the text file.
        with open("credits.txt", "r") as f:
            for line in f:
                stored_username, stored_credits = line.strip().split(":")
                if username == stored_username:
                    return int(stored_credits)

        # If the user is not found in the text file, return 0 credits.
        return 0

    def update_credits(username, new_credits):
        # Update the credits for the specified user in the text file.
        with open("credits.txt", "r") as f:
            lines = f.readlines()

        with open("credits.txt", "w") as f:
            for line in lines:
                stored_username, stored_credits = line.strip().split(":")
                if username == stored_username:
                    f.write(username + ":" + str(new_credits) + "\n")
                else:
                    f.write(line)


    def signup():
        # Get the username and password from the user.
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password (hidden): ")

        # Write the username and password to the text file.
        with open("users.txt", "a") as f:
            f.write(username + ":" + password + "\n")

        # Print a message to confirm that the user has been signed up.
        print("You have been signed up successfully!")
        log_signup(username)
        clear_console()

    def logout():
        print("You have logged out successfully!")
        clear_console()

    def main():
        loggedIn = False
        global score, dealerScore, credits, current_user

        # Display the login and signup options to the user.
        print("Welcome to Blackjack Online")
        print("*** This demo is in ALPHA development as of 13/05/2023. If you find any bugs, or have suggetions, please email WILKINL ***")
        print("1. Login")
        print("2. Signup")

        # Get the user's choice.
        choice = input("What would you like to do? ")

        # If the user chooses to login, prompt for username and password and check their validity.
        if choice == "1":
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password (hidden): ")
            if login(username, password):
                print("You have logged in successfully!")
                log_login(username)
                clear_console()
                loggedIn = True
                current_user = username
                credits = get_credits(current_user)
            else:
                print("Invalid username or password!")
                clear_console()

        # If the user chooses to signup, create a new account for the user.
        elif choice == "2":
            signup()

        # If the user enters an invalid choice, print an error message.
        else:
            print("Invalid choice!")

        while loggedIn:
            print("Choose an option from the list below:")
            print("NOTE: To save your new credit score, save and exit after every session.")
            print("1. Add credits to your balance")
            print("2. Play Game")
            print("3. View current balance")
            print("4. Save and exit")
            

            option = input("What would you like to do? ")

            if option == "1":
                clear_console()
            def add_credits():
                # my_secret = os.environ['pin_key']
                    pin_credits = getpass.getpass("Please enter administrative PIN: ")
                    if pin_credits == "1234":
                        global credits
                    try:
                        amount = int(input("Enter the amount to add: "))
                        if amount <= 0:
                            print("Invalid amount. Please enter a positive number.")
                            return
                        credits += amount
                        print("Credits added successfully. Your current credits:", credits)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
                    else:
                        print("Please obtain admin PIN before attempting to purchase credits.")

            add_credits()

            elif option == "2":
            clear_console()
            log_gamestart(username)
            print("Your current credits:", credits)
            update_credits(current_user, credits)
            bet = int(input("Enter the bet amount: "))  # Input the bet amount
            if bet > credits:
                    print("Insufficient credits. Please enter a valid bet amount.")
                    continue
            print("******* BLACKJACK *******")
            wfui()

                # Two starting cards for player
            score = 0
            dealerScore = 0
            for i in range(2):
                    lastPlayedCard = random.choice(cards)
                    cards.remove(lastPlayedCard)
                    score += card_values[lastPlayedCard]
                    print("You were dealt:", lastPlayedCard)

            # Print score outside of loop
            print("Your current score is:", score)

                # Check if straight Blackjack win
            if score >= 21:
                    play = False
                    print("Blackjack! You won - congratulations...")
                    log_gameend(username, score, dealerScore)
                    credits += 3 * bet
                    print("Your current credits:", credits)
                    update_credits(current_user, credits)
                    time.sleep(2)
                    clear_console()
                    continue

                # One starting card for dealer THAT'S REVEALED
            dealerlastPlayedCard = random.choice(cards)
            cards.remove(dealerlastPlayedCard)
            dealerScore += card_values[dealerlastPlayedCard]
            print("The dealer was dealt:", dealerlastPlayedCard)
            print("The dealer's single card score is:", dealerScore)

                # Second UNREVEALED card for dealer
            dealerlastPlayedCard = random.choice(cards)
            cards.remove(dealerlastPlayedCard)
            dealerScore += card_values[dealerlastPlayedCard]

                # If dealer score is under 17, pick another card for the dealer, and then check whether the dealer has busted.
            if dealerScore < 17:
                    print("The dealer's score was under 17, so they are picking another card")
                    dealerlastPlayedCard = random.choice(cards)
                    cards.remove(dealerlastPlayedCard)
                    dealerScore += card_values[dealerlastPlayedCard]
                    print("The dealer's third card was hidden.")
                    if dealerScore > 21:
                        print("The dealer busted. You WIN!")
                        log_gameend(username, score, dealerScore)
                        play = False
                        credits += 2 * bet
                        print("Your current credits:", credits)
                        update_credits(current_user, credits)
                        time.sleep(2)
                        clear_console()
                        break

                # Double check if under 21, and wanting to 'stick'
            if score <= 21:
                    play = True
                    stuck = input("Do you want to stick? (y/n): ")

            while play:
                    # In the instance that the player wants to stick
                    if stuck == "y":
                        stucked = True
                    # In the instance that the player wants to play
                    elif stuck == "n":
                        stucked = False
                    # The operation if the player is stuck
                    if stucked:
                        print("You're stuck.")
                        print("Dealer playing")
                        dealerlastPlayedCard = random.choice(cards)
                        cards.remove(dealerlastPlayedCard)
                        dealerScore += card_values[dealerlastPlayedCard]
                        print("The dealer was dealt:", dealerlastPlayedCard)
                        print("The dealer's score is:", dealerScore)
                        if dealerScore > 21:
                            print("The dealer busted. You WIN!")
                            log_gameend(username, score, dealerScore)
                            play = False
                            credits += 2 * bet
                            print("Your current credits:", credits)
                            update_credits(current_user, credits)
                            time.sleep(2)
                            clear_console()
                            break
                        stuck = input("Do you want to stick? (y/n): ")
                    # The operation if the player is playing
                    elif not stucked:
                        lastPlayedCard = random.choice(cards)
                        cards.remove(lastPlayedCard)
                        score += card_values[lastPlayedCard]
                        print("You were dealt:", lastPlayedCard)
                        print("Your current score is:", score)
                        if score > 21:
                            print("Busted! You lose...")
                            log_gameend(username, score, dealerScore)
                            play = False
                            credits -= bet
                            print("Your current credits:", credits)
                            update_credits(current_user, credits)
                            time.sleep(2)
                            clear_console()
                            break

            elif option == "3":
            clear_console()
            print("Your current credits:", credits)
            update_credits(current_user, credits)
            continue

            elif option == "4":
            clear_console()
            logout()
            log_logout(username)
            loggedIn = False
            update_credits(current_user, credits)

            else:
                print("Invalid option. Please try again.")

        print("Goodbye!")
        update_credits(current_user, credits)

if __name__ == "__main__":
    main()
    app.run(host="127.0.0.1", port=8080, debug=True)
