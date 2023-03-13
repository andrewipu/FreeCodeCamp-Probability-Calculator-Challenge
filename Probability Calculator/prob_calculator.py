import copy
import random
# Consider using the modules imported above.


class Hat:
    #constructor
    def __init__(self, **urn):
        self.urn = urn
        #list comprehension to extract k,v.
        self.contents = [k for k, v in urn.items() for i in range(v)]
        
        

    def draw(self, num_draw):
        #list to store randomly drawn balls
        contents_rand = []

        #loop to randomly sample from hat
        for i in random.sample(self.contents, min(num_draw, len(self.contents))):
            contents_rand.append(i)
        self.contents = self.contents[:-num_draw]
        if num_draw > len(self.contents):
            self.contents = self.contents[:+num_draw]
            return contents_rand
        else:
            return contents_rand





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    #convert expected_balls 
    expected_conv = [k for k, v in expected_balls.items() for i in range(v)]
    experiments_to_divide = num_experiments
    exp_found_count = 0 #to be divided by the # of experiments


    while num_experiments > 0:
        num_experiments -= 1
        #draw
        hat_copy = copy.copy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        found_flags = {k: False for k in expected_balls}
        for ball in drawn_balls:
            if drawn_balls.count(ball) >= expected_conv.count(ball):
                found_flags[ball] = True
        
        if all(found_flags.values()):
            exp_found_count += 1
            
    
    probability = exp_found_count / experiments_to_divide


    return probability
