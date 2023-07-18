import random


class Hat():
    # with this method the infinite amount of arguments are directly
    # a dic
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        keys = self.__dict__.keys()

        self.contents = []

        for key in keys:
            if key == "contents":
                continue
            else:
                amount_of_key = self.__dict__[key]
                self.contents.extend([key for i in range(amount_of_key)])

    def draw(self, amount_of_balls_drawn: int):

        if amount_of_balls_drawn > len(self.contents):
            return self.contents
        else:
            removed_balls = []
            random_chosen_ele = random.sample(self.contents, amount_of_balls_drawn)
            for ele in random_chosen_ele:
                removed_balls.append(ele)
        return removed_balls
