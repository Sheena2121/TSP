'''
Coachable Take Home - Part 3

For this assignment, you'll be implementing a Tour.

As usual, test that your code is working by creating a few basic inputs 
and running the functions to see if the code works as intended.

We recommend writing a main method to test out simple inputs as a sanity check. 
You'll know the code works when you run on the example inputs and get a Tour drawn
just like in the read me.

You can install the stddraw libraries with the instructions here - https://introcs.cs.princeton.edu/python/code/

python3 nearest_insertion.py < tsp10.txt

'''


'''
SS Note: the tour should loop through the data, and choose the point following the given heuristic.

'''

from multiprocessing import dummy
from pointHW import Point
import sys
import math
import stddraw



class Node:
    def __init__(self, point):
        self.point = point
        self.next_node = None



class Tour:
    
        
    def __init__(self):                           # create an empty tour
        self.head = Node(None)  
        self.tail = Node(None)
        self.head.next_node = self.tail  
        self.tail.next_node = self.head

    

    def insertFront(self, p):
        
       
        '''
        if self.head.point is None:             #if the value of the head node point is none (aka no nodes)
            self.head = new_node;               # store new_node in the head
            self.tail = new_node;               # store new_node as the tail
            new_node.next_node = self.head;     # make the new_node's next pointer, point to the head
        else:
            temp = self.head;                   # if not empty, store the old head in temp
            new_node.next_node = temp;          # put the new node in front of temp (aka in front of the old head)
            self.head = new_node;               # store new node in the head    
            self.tail.next_node = self.head;    # point the tail's next pointer back to the head
'''
        
        dummy_head = Node(None)
        new_node = Node(p);
        dummy_head = self.head
        temp = dummy_head.next_node    
        new_node.next_node = temp;     
        dummy_head.next_node = new_node;
             
        self.tail.next_node = self.head; 
        
        curr = self.head;  
        if self.head is None:  
            return;  
        else:  
           # print(curr.next_node.point._x0),
            while(curr.next_node != self.head):
                print(curr.next_node.point._x0)
                curr = curr.next_node;  
                  
            print("\n");
    
            
    def insertNearest(self, p):                   # insert p using nearest neighbor heuristic            
        new_node = Node(p)

    
        if self.head.point == None:            
            self.head = new_node
            self.tail = new_node
            new_node.next_node = self.head;
        
        # handle non-empty list case
        if self.tail != None:


            # define the first node                                         #traverse the list
            curr_node = self.head
                
            # find shortest distance
            currentDistance = curr_node.point.distanceTo(p)
            print(currentDistance)
            print(curr_node.next_node.point.distanceTo(p))
            min = currentDistance
            while curr_node.next_node:
                print(curr_node.next_node.point.distanceTo(p))
                if (min > curr_node.next_node.point.distanceTo(p)):
                    min = curr_node.next_node.point.distanceTo(p)
                    print("the new min is...")
                    print(min)
                
                #reassign the next node
                curr_node = curr_node.next_node
                
                if curr_node == self.head:
                    break
            
            print("smallest distance")
            print(min)

            
            curr_node = self.head
            while curr_node.next_node:
                if curr_node.point.distanceTo(p) == min:
                    print(curr_node.point._x0)
                    new_node.next_node = curr_node.next_node
                    curr_node.next_node = new_node
                    break
                else:
                    curr_node = curr_node.next_node
            

            curr = self.head;                               #print x coordinate of points in the tour
            if self.head is None:  
                print("The list is empty");  
                return;  
            else:
                print(curr.point._x0),
                while(curr.next_node != self.head):
                    curr = curr.next_node;  
                    print(curr.point._x0),  
                print("\n"); 
        

    def draw(self):
        curr_node = self.head                                   # draw the tour to standard draw
        while curr_node is not None:
            curr_node.point.draw()
            curr_node.point.drawTo(curr_node.next_node.point)
            print("hi from line 126!")
            curr_node = curr_node.next_node
            if curr_node == self.head:
                print("hi from line 129")
                break


    def size(self):                                         # number of points on tour
        curr_node = self.head
        count = 0
        while True:
            print("hi from line 135!")
            count += 1
            print("hi from line 171!")
            curr_node = curr_node.next_node
            if curr_node is self.head:
                print("hi from line 141")
                break      
        return count
    
    def distance(self):                                     # return the total distance of the tour
        curr_node = self.head
        totalDistance = 0
        while curr_node.next_node:
            print(curr_node.point.distanceTo(curr_node.next_node.point))
            totalDistance += curr_node.point.distanceTo(curr_node.next_node.point)     
            curr_node = curr_node.next_node        
            if curr_node == self.head:
                print("hi from line 179")
                print ("total distance is")
                print(totalDistance)
                break




    def insertSmallest(self, p):
        new_node = Node(p)                       
        # adds the node to the list if it is empty.
        if self.head.point == None:            
            self.head = new_node
            
            self.tail = new_node
            new_node.next_node = self.head;
            return
        
        # handle non-empty list case
        if self.tail != None:


            # define the first node                                         #traverse the list
            curr_node = self.head
                
            # find shortest distance
            currentDistance = curr_node.point.distanceTo(p)
            print("distance from current node to P:")
            print(currentDistance)
            print("distance from NEXT node to P:")
            print(curr_node.next_node.point.distanceTo(p))
            min = currentDistance + curr_node.next_node.point.distanceTo(p)
            print ("initial min is")
            print(min)
            
            while curr_node.next_node:
                
                if (min > curr_node.next_node.point.distanceTo(p) + curr_node.next_node.next_node.point.distanceTo(p)):
                    min = curr_node.next_node.point.distanceTo(p) + curr_node.next_node.next_node.point.distanceTo(p)
                    print("the new min is...")
                    print(min)
                
                #reassign the next node
               
                curr_node = curr_node.next_node
                
                if curr_node == self.head:
                    break
            
            print("smallest distance")
            print(min)

            
            curr_node = self.head
            while curr_node.next_node:
                if curr_node.point.distanceTo(p) + curr_node.next_node.point.distanceTo(p) == min:
                    print(curr_node.point._x0)
                    new_node.next_node = curr_node.next_node
                    curr_node.next_node = new_node
                    print("the point has been inserted!!")
                    break
                else:
                    curr_node = curr_node.next_node

            curr = self.head;                               #print x coordinate of points in the tour
            if self.head is None:  
                print("The list is empty");  
                return;  
            else:
                print(curr.point._x0),
                while(curr.next_node != self.head):
                    curr = curr.next_node;  
                    print(curr.point._x0),  
                print("\n"); 

        

