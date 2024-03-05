class FeatureB:
    """
    Feature B: Sprint Planning
        1. Input the number of Sprint Days
        2. Input the number of Team Members
        3. Input the details of each Team Member
    """
    def __init__(self):
        sprint_days = self.input_sprint_days()
        no_team_members = self.input_no_team_members()
        team_members_details = self.input_team_members_details(no_team_members)
        

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



if __name__ == "__main__":
    feature_b = FeatureB()