'''
Coachable Take Home - Part 2

For this assignment, you'll be implementing a 2D point class.

As usual, test that your code is working by creating a few basic points 
and running the functions to see if the code works as intended.

You can install the stddraw libraries with the instructions here - https://introcs.cs.princeton.edu/python/code/

'''

class Point:        

	def __init__(self, x, y):      		  # create the Point (x, y) in 2D
	def toString(self):                   # return a reasoanble string representation of the Point.
	def draw(self):                       # Draw point using standard draw
	def drawTo(self, that):               # Draw a line segment between the two points with stddraw.
	def distanceTo(self, that):           # Return Euclidean distance between the two points.



'''
Bonus! (Optional)

Implement a N-dimensional point class.
'''


class ND_Point:        

	def __init__(self, N, coords):        # create the point in N-dimensions. N refers to the dimension and 
										  # coords is a list of coordinates. You should raise an exception 
										  # If the length of coordinates does not match N.

	def toString(self):                   # return a reasonable string representation of the point.
	def distanceTo(self, that):           # return Euclidean distance between the two points. 
										  # This should raise an exception if the points are not the same dimension.