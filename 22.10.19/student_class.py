class Student:
    def __init__(self, score=10):
        self.score = score
    
    def add_score(self):
        self.score += 10

    def decrease_score(self):
        self.score -= 10

    def __str__(self):
        return "{}".format(self.score)

def main():
    p = Student()
    print(p)
    p.add_score()
    print(p)

main()