import copy
from collections import Counter
import random

class Hat():
    # with this method the infinite amount of arguments are directly
    # a dic
    def __init__(self, **balls):
        balls = dict(balls)
        self.contents = []

        for color in balls:
            self.contents.extend([color for i in range(balls[color])])

    def draw(self, amount_of_balls_drawn: int):

        if amount_of_balls_drawn > len(self.contents):
            return self.contents
        else:
            removed_balls = []
            random_chosen_ele = random.sample(self.contents, amount_of_balls_drawn)
            contents = self.contents
            for ele in random_chosen_ele:
                removed_balls.append(ele)
                contents.remove(ele)
        return removed_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    experiments = []
    for i in range(num_experiments):
        hat_exp = copy.deepcopy(hat)
        result = hat_exp.draw(num_balls_drawn)
        result = dict(Counter(ball for ball in result))
        experiments.append(result)

    failed = []
    for ball in list(expected_balls.keys()):
        for r in experiments:
            if not (ball in list(r.keys())):
                failed.append(r)

    experiments = [r for r in experiments if r not in failed]

    failed = []
    for ball in list(expected_balls.keys()):
        for r in experiments:
            if int(expected_balls[ball]) > int(r[ball]):
                failed.append(r)

    experiments = [r for r in experiments if r not in failed]

    return len(experiments) / num_experiments
