import stdio
import stddraw
from tour import Tour
from pointHW import Point


if __name__ == "__main__":
	# get dimensions
	width = stdio.readInt();
	height = stdio.readInt();
	border = 20;
	stddraw.setCanvasSize(width, height + border);
	stddraw.setXscale(0, width);
	stddraw.setYscale(-border, height);

	# run smallest insertion heuristic
	tour = Tour();
	
	while not stdio.isEmpty():
		x = stdio.readFloat();
		y = stdio.readFloat();
		p = Point(x, y);
		tour.insertSmallest(p);
		
		
	
	# draw to standard draw 
	tour.draw();
	stddraw.show();
	
	
	
	# prtour to standard output


        
	stdout.println(tour);
	stdout.printf("Tour length = %.4f\n", tour.length());
	stdout.printf("Number of points = %d\n", tour.size());

	
