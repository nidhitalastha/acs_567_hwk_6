import feature_a
import feature_b

def menu():
    ''' This function displays the menu for the user to choose the feature '''
    print("1. Feature A: Calculate average velocity of the team based on previous sprint points completed")
    print("2. Feature B: Calculate team effort-hour capacity based on team size and working hours per day")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ins_a = feature_a.feature_a()
    elif choice == 2:
        ins_b = feature_b.FeatureB()
    else:
        exit()

if __name__ == "__main__":
    ''' This is the main function which will be called when the file is executed '''
    menu()