'''
python3 nearest_insertion.py < tsp10.txt
'''
from multiprocessing import dummy
from os import P_ALL
from unittest import skip
from pointHW import Point
import sys
import math
import stddraw


class Node:
    def __init__(self, point):
        self.point = point
        self.next = None

class Tour:   
    def __init__(self):                           # create an empty tour
        self.head = Node(None)  
        self.count = 0
    
    def insertFront(self, p): 
       new_node = Node(p)
       new_node.next = self.head.next   #takes the next pointer from the head node, and makes the new node's next pointer point to the thing that comes next
       self.head.next = new_node
       self.count += 1
       print(self.count)
       
    def insertAt(self, insertion_point, new_node):
        curr_node = self.head
        position = 0
        while curr_node:
            if position == insertion_point:
                new_node.next = curr_node.next
                curr_node.next = new_node
                break
            else:
                position += 1
                curr_node = curr_node.next  
        self.count += 1
        print(self.count)

    def insertNearest(self, p):          # insert p using nearest neighbor heuristic            
        if self.count == 0:
            self.insertFront(p)
        
        else:
            new_node = Node(p)
            curr_node = self.head.next
            currentDistance = curr_node.point.distanceTo(p)
            min = currentDistance
            while curr_node.next:
                if (min > curr_node.next.point.distanceTo(p)):
                    min = curr_node.next.point.distanceTo(p)
                curr_node = curr_node.next
                if curr_node.next is None:
                    break
            curr_node = self.head.next
            insertion_point = 0
            while curr_node:
                if curr_node.point.distanceTo(p) == min:
                    self.insertAt(insertion_point, new_node)
                    break
                else:
                    insertion_point += 1
                    curr_node = curr_node.next

    def insertSmallest(self, p):     
        if self.count == 0:
            self.insertFront(p)

        if self.count == 1:
            new_node = Node(p)
            self.insertAt(1, new_node)
                
        else:
            new_node = Node(p)
            curr_node = self.head.next 
            min = curr_node.point.distanceTo(p) + curr_node.next.point.distanceTo(p) - curr_node.point.distanceTo(curr_node.next.point)
            while curr_node.next:
                if curr_node.next.next:
                    if min > (curr_node.next.point.distanceTo(p) + curr_node.next.next.point.distanceTo(p) - curr_node.next.point.distanceTo(curr_node.next.next.point)):
                        min = (curr_node.next.point.distanceTo(p) + curr_node.next.next.point.distanceTo(p) - curr_node.next.point.distanceTo(curr_node.next.next.point))
                else:
                    if min > (curr_node.next.point.distanceTo(p) + self.head.next.point.distanceTo(p) - curr_node.next.point.distanceTo(self.head.next.point)):
                        min = (curr_node.next.point.distanceTo(p) + self.head.next.point.distanceTo(p) - curr_node.next.point.distanceTo(self.head.next.point))                    
                curr_node = curr_node.next

            curr_node = self.head.next
            insertion_point = 1
            while curr_node:
                if curr_node.next:
                    if curr_node.point.distanceTo(p) + curr_node.next.point.distanceTo(p) - curr_node.point.distanceTo(curr_node.next.point) == min:
                        self.insertAt(insertion_point, new_node)
                        break
                    else:
                        insertion_point += 1
                        curr_node = curr_node.next
           
    def draw(self):      
        curr_node = self.head.next    
        while curr_node:  
            if curr_node.next:                             # draw the tour to standard draw
                curr_node.point.draw()
                curr_node.point.drawTo(curr_node.next.point)
                print(curr_node.point._x0)
                curr_node = curr_node.next
            else: 
                curr_node.point.drawTo(self.head.next.point)
                break
            

    def size(self):                                         # number of points on tour
        return self.count
    
    def distance(self):                                     # return the total distance of the tour
        curr_node = self.head.next
        totalDistance = 0
        while curr_node.next:
            totalDistance += curr_node.point.distanceTo(curr_node.next.point)  
            curr_node = curr_node.next        
            if curr_node.next.next is None:
                totalDistance += curr_node.point.distanceTo(self.head.next.point)
                print ("total distance is")
                print(totalDistance)
                break

    