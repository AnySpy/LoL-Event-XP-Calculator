# ===========================
# Event Mission Calculator
# Code by: Samuel Young
# Created on: 3/24/23
# ===========================

# This code can (and will be) improved upon in the future. It's quite spaghetti-esque right now, but I'll make it better.

print("=============================================================================================================")
print("Welcome to the Event Mission Calculator")
print("=============================================================================================================")
print()

def main():
    # Prints the options for the user
    print("1. Summoner's Rift")
    print("2. ARAM")
    print("3. TFT")
    print("4. Co-op vs. AI")
    print("5. Exit the Program")
    print()
    # Asks the user to input one of the five options
    print("Please input the number corresponding to the gamemode you want.")
    mode = input()

    # If the mode is five, it exits the code.
    if mode != "5":
        if mode == "1":
            print("You have selected: Summoner's Rift")
            print()
            # Requests the number of points until they finish their mission
            print("Please input the number of points required for your mission")
            pts = int(input())

            # Does some math
            Lmins = round(pts/4)
            Wmins = round(pts/6)

            Lgames = round(Lmins/30)
            Wgames = round(Wmins/30)

            # If either are less than one, it just assumes one (Otherwise it prints 0, which is wrong).
            if Lgames < 1:
                Lgames = 1
            if Wgames < 1:
                Wgames = 1                
            
            # Prints the output
            print()
            print("=============================================================================================================")
            print("You would need to play a losing game for {} minutes or a winning game for {} minutes.".format(Lmins, Wmins))
            print("Assuming 30 minutes per game, you'd have to play {} losing games or {} winning games.".format(Lgames, Wgames))
            print("=============================================================================================================")
            print()

            # Asks the user if they'd like to try again
            print("Try again?")
            print("Y/N")
            again = input()

            # If they say yes, it runs the program again. Otherwise, it exits the program
            if again == "Y" or again == "y":
                print()
                main()
            elif again == "N" or again == "n":
                exit()

        # The rest of it is copy-pasted from the first function.
        elif mode == "2":
            print("You have selected: ARAM")
            print()
            print("Please input the number of points required for your mission")
            pts = int(input())

            Lmins = round(pts/4)
            Wmins = round(pts/6)
            
            Lgames = round(Lmins/30)
            Wgames = round(Wmins/30)

            if Lgames < 1:
                Lgames = 1
            if Wgames < 1:
                Wgames = 1  

            print()
            print("=============================================================================================================")
            print("You would need to play a losing game for {} minutes or a winning game for {} minutes.".format(Lmins, Wmins))
            print("Assuming 15 minutes per game, you'd have to play {} losing games or {} winning games.".format((round(Lmins/15)), (round(Wmins/15))))
            print("=============================================================================================================")
            print()

            print("Try again?")
            print("Y/N")
            again = input()

            if again == "Y" or again == "y":
                print()
                main()
            elif again == "N" or again == "n":
                exit()

        elif mode == "3":
            print("You have selected: TFT")
            print()
            print("Please input the number of points required for your mission")
            pts = int(input())

            Lmins = round(pts/3)
            Wmins = round(pts/6)
            
            Lgames = round(Lmins/30)
            Wgames = round(Wmins/30)

            if Lgames < 1:
                Lgames = 1
            if Wgames < 1:
                Wgames = 1  

            print()
            print("=============================================================================================================")
            print("You would need to play a losing game for {} minutes or a winning game for {} minutes.".format(Lmins, Wmins))
            print("Assuming 25 minutes per game, you'd have to play {} losing games or {} winning games.".format((round(Lmins/25)), (round(Wmins/25))))
            print("=============================================================================================================")
            print()

            print("Try again?")
            print("Y/N")
            again = input()

            if again == "Y" or again == "y":
                print()
                main()
            elif again == "N" or again == "n":
                exit()

        elif mode == "4":
            print("You have selected: Co-op vs. AI")
            print()
            print("Please input the number of points required for your mission")
            pts = int(input())

            Lmins = round(pts/1)
            Wmins = round(pts/2)
            
            Lgames = round(Lmins/30)
            Wgames = round(Wmins/30)

            if Lgames < 1:
                Lgames = 1
            if Wgames < 1:
                Wgames = 1  

            print()
            print("=============================================================================================================")
            print("You would need to play a losing game for {} minutes or a winning game for {} minutes.".format(Lmins, Wmins))
            print("Assuming 15 minutes per game, you'd have to play {} losing games or {} winning games.".format((round(Lmins/15)), (round(Wmins/15))))
            print("=============================================================================================================")
            print()

            print("Try again?")
            print("Y/N")
            again = input()

            if again == "Y" or again == "y":
                print()
                main()
            elif again == "N" or again == "n":
                exit()

        # If they enter something that isn't an option (6, aaa, etc.), it prints this error message and then asks them to choose a correct value.
        else:
            print()
            print("=============================================================================================================")
            print("The inputted value does not match a value we have. Please try again.")
            print("=============================================================================================================")
            print()
            main()

main()