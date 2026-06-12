grade = int(input("Enter the number of the day (1,2,3,4,5,6,7);"))

match grade:
    case 1:
        print("The day is monday")
    case 2:
        print("The day is Tuesday")
    case 3:
        print("The day is Wednesday")
    case 4:
        print("The day is Thursday")
    case 5:
        print("The day is Friday")
    case 6:
        print("The day is Saturday")
    case 7:
        print("The day is Sunday")
    case _:
        print("Invalid day")