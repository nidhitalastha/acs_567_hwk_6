from tabulate import tabulate

class FeatureB:
    """
    Feature B: Sprint Planning
        1. Input the number of Sprint Days
        2. Input the number of Team Members
        3. Input the details of each Team Member

        For each Team Member:
            1. Input the number of days off
            2. Input the number of days committed to Sprint ceremonies
            3. Input the number of hours/day available (min-max)
        
        Calculate the available hours for each Team Member
    """
    def __init__(self):
        sprint_days = self.input_sprint_days()
        no_team_members = self.input_no_team_members()
        team_members_details = self.input_team_members_details(no_team_members)
        team_members_details, team_cap_min, team_cap_max = self.calculate_available_hours(sprint_days,team_members_details)
        self.display_available_hours(sprint_days,team_members_details, team_cap_min, team_cap_max)

    def input_sprint_days(self):
        """
        Input: Number of Sprint Days
        """
        sprint_days = input("Enter the number of Sprint Days: ")
        sprint_days = int(sprint_days)
        return sprint_days

    def input_no_team_members(self):
        """
        Input: Number of Team Members
        """
        no_team_members = input("Enter the number of Team Members: ")
        no_team_members = int(no_team_members)
        return no_team_members

    def input_team_members_details(self, no_team_members):
        """
        Input: Team Member Details
        """
        team_members_details = []
        for i in range(no_team_members):
            member_details = {}
            member_details['name'] = input("Enter the name of Team Member: ")
            
            days_off = input("Enter the number of days off for Team Member: ")
            member_details['days_off'] = int(days_off)

            days_for_scrum_commitment = input("Enter the number of days committed to Sprint ceremonies for Team Member: ")
            member_details['days_for_scrum_commitment'] = int(days_for_scrum_commitment)

            hours_per_day = input("Enter the number of hours/day available for Team Member (e.g. 6-8): ")
            hours_per_day = hours_per_day.split('-')
            member_details['min_hours_per_day'] = int(hours_per_day[0])
            member_details['max_hours_per_day'] = int(hours_per_day[1])

            team_members_details.append(member_details)

        return team_members_details


    def calculate_available_hours(self, sprint_days, team_members_details):
        """
        Calculate the available hours for each Team Member and Team as a whole
        """
        team_min_cap = 0
        team_max_cap = 0
        for member in team_members_details:
            available_days = sprint_days - member['days_off'] - member['days_for_scrum_commitment']
            min_available_hours = member['min_hours_per_day'] * available_days
            max_available_hours = member['max_hours_per_day'] * available_days
            team_min_cap += min_available_hours
            team_max_cap += max_available_hours
            member['available_hours'] = "{}-{}".format(min_available_hours, max_available_hours)

        return (team_members_details,team_min_cap,team_max_cap)


    def display_available_hours(self, sprint_days, team_members_details, team_min_cap, team_max_cap):
        """
        Display the available hours for each Team Member and Team as a whole
        """
        print("Available hours for each Team Member:")
        formatted_team_members_details = []

        for member in team_members_details:
            member_details = {}
            member_details['Name'] = member['name']
            member_details['Days Off (PTO)'] = member['days_off']
            member_details['Days Available'] = sprint_days - member['days_off']
            member_details['Days for Scrum Commitment'] = member['days_for_scrum_commitment']
            member_details['Hours Per Day'] = "{}-{}".format(member['min_hours_per_day'], member['max_hours_per_day'])
            member_details['Total Available Hours'] = member['available_hours']
            formatted_team_members_details.append(member_details)

        formatted_team_members_details.append({"Name":"Team Capacity","Total Available Hours":"{}-{}".format(team_min_cap, team_max_cap)})  
        print(tabulate(formatted_team_members_details, headers='keys', tablefmt='grid', showindex=False))


if __name__ == "__main__":
    feature_b = FeatureB()