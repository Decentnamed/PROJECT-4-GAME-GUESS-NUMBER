

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def enter_number(self, min_number, max_number):
        while True:
            number = int(input(f"Enter number in range {min_number} to {max_number}: "))
            if number not in range(min_number, max_number):
                print("Enter value not in range, try again...\n")
            else:
                break
    
    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score
    
    def add_score(self):
        self.score += 1