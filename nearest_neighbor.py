# Isaac Lino - SID 860869360
# Nearest Neighbor - Fall 2016
# CS141 Inter to Data structure and Algorithms

import math
import sys
import time
import operator

#----------------------------------------------------------------------------
def read_points_from_file():
    
    # create an empty array of points
    points = []
    
    # number of arguments pass from script (this case is only one from file)
    file = str(sys.argv[1])
    
    # open and store file info using "r" <- read only mode
    read_file = open(file, "r")
    
    # loop the entire string and store points in two rows
    for index in read_file:
        
        # split string in two sets of points and append to array of points
        set = index.split()
        x_y_points = (float(set[0]), float(set[1]))
        points.append(x_y_points);
    
    # close file
    read_file.close()

    return points;
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
def find_smallest(sort_y_points, distance_d, median):
    
    new_points = []
        
    # check and delete points that are outside array
    for i in range(0, len(sort_y_points)):
            
        current_point = sort_y_points[i][0]
                
        if not((current_point > (median + distance_d)) or (current_point < (median - distance_d))):
            new_points.append(sort_y_points[i])
    
    
    # loop to check for smallest distance for the rest of points
    for i in range(0, len(new_points)):
        j = 1
        
        while(((i + j) < len(new_points)) and (j < 10)):
            
            # distance between 2 points sqare_root[ (Xi - Xj)^2 + (Yi - Yj)^2 ]
            X = new_points[i][0] - new_points[i+j][0]
            Y = new_points[i][1] - new_points[i+j][1]
            sum = pow(X,2) + pow(Y,2)
            distance = math.sqrt(sum)
            
            # check for smallest / closest neighbor pair of points
            if (distance < distance_d):
                distance = distance_d
            
            j += j
                            
    return distance_d
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
def closest_pair(points):
    
    if len(points) == 1 or len(points) == 2 or len(points) == 3:
        return brute_force_algorithm(points)
        
    if len(points) % 3 == 0:
        value_1 = closest_pair(points[:int((len(points)/2)+1)])
        value_2 = closest_pair(points[int((len(points)/2)):])
        distance_d =  min(value_1, value_2)
        
    else:
        value_1 = closest_pair(points[:int(((len(points)-1)/2)+1)])
        value_2 = closest_pair(points[int(((len(points)-1)/2)):])
        distance_d =  min(value_1, value_2)
    
    if len(points) % 3 == 0:
        median = (len(points)/2) + 1

    else:
        median = points[int((len(points) + 1)/2)][0]

    #set[1] contains y points and sort points by y
    #using keyword lambda to save memory(build in iteration/sort function)
    sort_y_points = sorted(points, key = lambda coordinate: coordinate[1])
        
    return find_smallest(sort_y_points, distance_d, median)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
def divde_and_conquer_algorithm(plane_points):
    
    #set[0] contains x points and sort points by x
    #using keyword lambda to save memory(build in iteration/sort function)
    sort_x_points = sorted(plane_points, key = lambda set: set[0])
    
    
    return closest_pair(sort_x_points)
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
def brute_force_algorithm(plane_points):
    
    # brute force version of the algorithm which will compare all
    # pairs of points to find the closest pair.
    closest_neighbor = float
    
    # due to nested for loop, running time is O(n^2)
    for i in range(0,len(plane_points)):
        
        for j in range((i+1),len(plane_points)):
            
            # distance between 2 points sqare_root[ (Xi - Xj)^2 + (Yi - Yj)^2 ]
            X = plane_points[i][0] - plane_points[j][0]
            Y = plane_points[i][1] - plane_points[j][1]
            sum = pow(X,2) + pow(Y,2)
            distance = math.sqrt(sum)
            
            # check for smallest / closest neighbor pair of points
            if distance < closest_neighbor:
                closest_neighbor = distance
    
    return closest_neighbor
#----------------------------------------------------------------------------

def main():

# getting all of the points from the file
    plane_points = read_points_from_file()

#start and stop time for divide and conquer algorithm
    start = time.time()
    closest_neighbor_divde_and_conquer_algorithm = divde_and_conquer_algorithm(plane_points)
    stop = time.time()
    divide_and_conquer_algorithm_time = stop - start

# start and stop time for brute force algorithm
    start = time.time()
    closest_neighbor_Brute_Force = brute_force_algorithm(plane_points)
    stop = time.time()
    brute_force_algorithm_time = stop - start

#writing results to the file
    file  = str(sys.argv[1])
    file = open(file[:len(file)-4] + "_distance.txt", "w")
    file.write("\n- DIVIDE AND CONQUER ALGORITHM -\n")
    file.write("Time (secs): ")
    file.write(str(divide_and_conquer_algorithm_time))
    file.write("\nDistance of closest pair distance: ")
    file.write(str(closest_neighbor_divde_and_conquer_algorithm))
    file.write("\n\n- BRUTE FORCE ALGORITHM - \n")
    file.write("Time (secs): ")
    file.write(str(brute_force_algorithm_time))
    file.write("\nDistance of closest pair distance: ")
    file.write(str(closest_neighbor_Brute_Force))
    file.close()

#print results to console
    print "\n"
    print "DIVIDE AND CONQUER ALGORITHM"
    print "Time (secs): ", divide_and_conquer_algorithm_time
    print "Distance of closest pair distance: ", closest_neighbor_divde_and_conquer_algorithm
    print "\n"
    print "BRUTE FORCE ALGORITHM"
    print "Time (secs): ", brute_force_algorithm_time
    print "Distance of closest pair distance: ", closest_neighbor_Brute_Force
    print "\n"

main()





