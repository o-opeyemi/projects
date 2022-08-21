import random
# Hat class to choose from
class Hat:
    def __init__(self, contents = [], **balls):
        self.balls = balls
        self.contents = contents
        for i in list(self.balls.keys()):
            temp_contents = ""
            temp_contents += (i + " ") * self.balls[i]
            for temp in temp_contents.split(" "):
                if temp == "":
                    pass
                else:
                    self.contents.append(temp)
    
    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        else:
            selected = []
            for i in range(number_of_balls):
                choice = random.choice(self.contents)
                self.contents.remove(choice)
                selected.append(choice)
            return selected

    def draw_with_replacement(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        else:
            selected = []
            for i in range(number_of_balls):
                choice = random.choice(self.contents)
                selected.append(choice)
            return selected

# Experimental process
def experiment(hat = Hat(), expected_balls ={}, num_balls_draw = 0, num_experiments = 0):
    balls = hat.contents
    prob = 0
    for exp in range(num_experiments):
        balls_drawn = hat.draw_with_replacement(num_balls_draw)
        temp_content_list = []
        for i in list(expected_balls.keys()):
            temp_contents = ""
            temp_contents += (i + " ") * expected_balls[i]
            for temp in temp_contents.split(" "):
                if temp == "":
                    pass
                else:
                    temp_content_list.append(temp)
        print(temp_content_list, balls_drawn)
        subset = set(temp_content_list).issubset(balls_drawn)
        if subset == True:
            prob += 1
        else:
            pass
    return prob/num_experiments