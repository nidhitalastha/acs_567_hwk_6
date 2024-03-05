from tabulate import tabulate

class feature_a:
    ''' This class is responsible for collecting the data for the feature A '''

    def __init__(self):
        self.sprint_points = []
        self.average_velocity = 0.0
        self.input()

    def input(self):
        ''' Collect previous sprint point completion data to calculate velocity of the team '''

        print("Collecting data for average velocity of the team")
        no_of_sprints = int(input("Enter the number of previous sprints completed: "))

        for i in range(no_of_sprints):
            ''' Collect sprint points completed in each sprint '''

            sprint_point = int(input("Enter the sprint points completed in sprint " + str(i+1) + ": "))
            self.sprint_points.append(sprint_point)
        print("Data collected successfully")
        self.calculate_velocity()

    def calculate_velocity(self):
        ''' Calculate the average velocity of the team '''

        total_sprint_points = sum(self.sprint_points)
        no_of_sprints = len(self.sprint_points)
        self.average_velocity = total_sprint_points / no_of_sprints
        self.display_output()

    def display_output(self):
        ''' Display the output of the feature A '''
        index = [i for i in range(1, len(self.sprint_points)+1)]
        sprint_details = zip(index, self.sprint_points)
        print(tabulate(sprint_details, headers=["Sprint", "Sprint Points"], tablefmt="grid"))
        print("The average velocity of the team is: ", self.average_velocity)
        
if __name__ == "__main__":
    ''' This is the main function which will be called when the file is executed '''
    ins_a = feature_a()
        
