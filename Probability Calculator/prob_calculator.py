import copy
import random
# Consider using the modules imported above.

class Hat:
    #constructor
    def __init__(self, **urn):
        self.urn = urn
        self.contents = []

        #loop to generate list of individual items for each ball
        for k, v in urn.items():
            i = 0
            while i < v:
                i += 1
                self.contents.append(k)

    def draw(self, num_draw):
        #list to store randomly drawn balls
        contents_rand = []

        #loop to randomly sample from hat
        for i in random.sample(list(self.contents),num_draw):
            contents_rand.append(i)
        self.contents = self.contents[:-num_draw]
        if num_draw > len(self.contents):
            self.contents = self.contents[:+num_draw]
        else:
            return contents_rand





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass