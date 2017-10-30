from random import choice

class RandomWalk():
    """ a class of RandomWalk"""

    def __init__(self, num_points=5000):
        """initilise attributs"""
        self.num_points = num_points

        #all walks start from 0,0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """calculate all points of walking"""

        #keep walking until reading the length
        while len(self.x_values) < self.num_points:

            #decide directions and distances
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4,10,20])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4,10,20])
            y_step = y_direction * x_distance

            #avoid 0,0
            if x_step == 0 and y_step == 0:
                continue

            #calculate next points
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

