from robot import *
from point import *

# takes in user input for robot and treasure position, prints out all the shortest routes in between    
# them and number of routes
def main():

    # try statement to ensure all values inputted are valid else except statement is printed
    try:
        user_input = input("Please enter the x and y positions for both the Robot and the Treasure (separated by spaces): ")
        user_input = user_input.split()
        robot_pos = Point(int(user_input[0]), int(user_input[1]))
        treasure_pos = Point(int(user_input[2]), int(user_input[3]))

        robot = Robot(robot_pos, treasure_pos)
        robot.print_routes()
    except:
        raise ValueError("Please enter proper points as integers separated by spaces!")
