class School:
    
    def __init__(self, name):
        self.name = name
        self.roster = {}
        
    def add_student(self, fullname, grade):
        if grade in self.roster:
            self.roster[grade].append(fullname)
        else:
            self.roster[grade] = [fullname]

    def grade(self, grade):
           return self.roster[grade]
        
    def sort_roster(self):
            sorted_roster = self.roster
            for key in sorted_roster:
                sorted_roster[key].sort()
            return sorted_roster