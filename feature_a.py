from tabulate import tabulate

class feature_a:
    ''' This class is responsible for collecting the data for the feature A '''
    def input(self):
        ''' Collect previous sprint point completion data to calculate velocity of the team '''

        print("Collecting data for average velocity of the team")
        no_of_sprints = int(input("Enter the number of previous sprints completed: "))
        sprint_points = []
        for i in range(no_of_sprints):
            ''' Collect sprint points completed in each sprint '''

            sprint_point = int(input("Enter the sprint points completed in sprint " + str(i+1) + ": "))
            sprint_points.append(sprint_point)
        print("Data collected successfully")
        return sprint_points

    def calculate_velocity(self,sprint_points):
        ''' Calculate the average velocity of the team '''
        if len(sprint_points) == 0:
            return 0
        total_sprint_points = sum(sprint_points)
        no_of_sprints = len(sprint_points)
        average_velocity = total_sprint_points / no_of_sprints
        return average_velocity 

    def display_output(self,sprint_points,average_velocity):
        ''' Display the output of the feature A '''
        index = [i for i in range(1, len(sprint_points)+1)]
        sprint_details = zip(index, sprint_points)
        print(tabulate(sprint_details, headers=["Sprint", "Sprint Points"], tablefmt="grid"))
        print("The average velocity of the team is: ", average_velocity)

if __name__ == "__main__":
    ''' This is the main function which will be called when the file is executed '''
    ins_a = feature_a()
    sprint_points = ins_a.input()
    average_velocity = ins_a.calculate_velocity(sprint_points)
    ins_a.display_output(sprint_points,average_velocity)

        