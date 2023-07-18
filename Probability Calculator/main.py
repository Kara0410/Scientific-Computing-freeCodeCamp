from prob_calculator import Hat


hat = Hat(black=6, red=4, green=3)
print(hat.contents)
hat.draw(amount_of_balls_drawn=12)
print(hat.draw(amount_of_balls_drawn=12))
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)