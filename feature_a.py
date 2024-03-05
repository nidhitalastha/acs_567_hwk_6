class feature_a:
    ''' This class is responsible for collecting the data for the feature A '''

    def __init__(self):
        self.sprint_points = []

    def input(self):
        ''' Collect previous sprint point completion data to calculate velocity of the team '''

        print("Collecting data for average velocity of the team")
        no_of_sprints = int(input("Enter the number of previous sprints completed: "))

        for i in range(no_of_sprints):
            ''' Collect sprint points completed in each sprint '''

            sprint_point = int(input("Enter the sprint points completed in sprint " + str(i+1) + ": "))
            self.sprint_points.append(sprint_point)
        print("Data collected successfully")
        
if __name__ == "__main__":
    ''' This is the main function which will be called when the file is executed '''
    ins_a = feature_a()
    ins_a.input()
        
