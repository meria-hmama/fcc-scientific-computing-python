import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            for _ in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn = self.contents[:]  
            self.contents.clear()
            return drawn
        drawn = []
        for _ in range(num_balls):
            idx = random.randrange(len(self.contents))
            ball = self.contents.pop(idx)
            drawn.append(ball)
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        ok = True
        for color, needed in expected_balls.items():
            if drawn_counts.get(color, 0) < needed:
                ok = False
                break
        if ok:
            success_count = success_count+1
    return success_count / num_experiments