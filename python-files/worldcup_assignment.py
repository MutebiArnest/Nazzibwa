print("------- FIFA WORLD CUP 2026 -------")

morale = 70
strength = 70
injuries = 0
wins = 0
match = 1

print("PRE-TOURNAMENT PREPARATION")

while True:
    print("Choose an activity:")
    print("1. Training")
    print("2. Friendly Match")
    print("3. Recovery")
    print("4. Start Tournament")

    choice = input("Enter your choice: ")
    if choice == "1":
        strength += 10
        morale += 5
        print("Training completed. Strength increased.")
    elif choice == "2":
        result = input("Did you win the friendly? (yes/no): ")
        if result.lower() == "yes":
            morale += 10
        else:
            morale -= 5
        print("Friendly match finished.")
    elif choice == "3":
        print("Players are recovering.")
        pass 
    elif choice == "4":
        break
    else:
        print("Invalid choice please enter a valid option.")

print("GROUP STAGE")

while match <= 3:
    print(f"Group Match {match}")
    action = input("Prepare for match? (play/skip): ")
    if action.lower() == "skip":
        print("Match skipped.")
        match += 1
        continue
    result = input("Did your team win? (yes/no): ")
    if result.lower() == "yes":
        wins += 1
        morale += 5
        strength += 2
        print("You won this match!")
    else:
        morale -= 5
        injuries += 1
        print("You lost this match.")
    match += 1

if wins < 2:
    print(f"Your team won only {wins} match(es).")
    print("You failed to qualify for the knockout stage.")
else:
    print(f"Your team won {wins} matches and qualifies!")

    stages = [
        "Round of 16",
        "Quarter-final",
        "Semi-final",
        "Final"
    ]
    stage_index = 0
    while stage_index < len(stages):
        print(f"{stages[stage_index]}")
        result = input("Did your team win? (yes/no): ")

        if result.lower() == "yes":
            if stage_index == len(stages) - 1:
                print("Congratulations! You have won the 2026 FIFA World Cup!")
                break
            else:
                print("You advance to the next stage.")
                stage_index += 1
        else:
            print("Your team has been eliminated from the tournament.")
            break
