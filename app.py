import feature_a
import feature_b

def menu():
    ''' This function displays the menu for the user to choose the feature '''
    print("1. Feature A: Calculate average velocity of the team based on previous sprint points completed")
    print("2. Feature B: Calculate team effort-hour capacity based on team size and working hours per day")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ins_a = feature_a.feature_a()
        sprint_points = ins_a.input()
        average_velocity = ins_a.calculate_velocity(sprint_points)
        ins_a.display_output(sprint_points,average_velocity)
    elif choice == 2:
        ins_b = feature_b.FeatureB()
        sprint_days = ins_b.input_sprint_days()
        no_team_members = ins_b.input_no_team_members()
        team_members_details = ins_b.input_team_members_details(no_team_members)
        team_members_details, team_cap_min, team_cap_max = ins_b.calculate_available_hours(sprint_days,team_members_details)
        ins_b.display_available_hours(sprint_days,team_members_details, team_cap_min, team_cap_max)
    else:
        exit()

if __name__ == "__main__":
    ''' This is the main function which will be called when the file is executed '''
    menu()