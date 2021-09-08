import point

# Robot class is made to represent shortest routes and number of shortest routes between a robot and a treasure
class Robot:


    routes = set()

    def __init__(self, RobotPos, TreasurePos):
        self.__RobotPos = RobotPos
        self.__TreasurePos = TreasurePos
        self.routes = self.routes

    # This function gets all the paths between the robot and treasure. This function runs recursively, and returns
    # a list of directions that sums up and lists the shortest paths and stores it within the routes set.
    def find_shortest_paths(self, robot_x, robot_y, treasure_x, treasure_y, direction):

        if robot_x == treasure_x and robot_y == treasure_y:
            self.routes.add(direction)

        else:
            if treasure_y < robot_y:
                self.find_shortest_paths(robot_x, robot_y - 1, treasure_x, treasure_y, direction + "S")
            if treasure_x < robot_x:
                self.find_shortest_paths(robot_x - 1, robot_y, treasure_x, treasure_y, direction + "W")
            if treasure_x > robot_x:
                self.find_shortest_paths(robot_x + 1, robot_y, treasure_x, treasure_y, direction + "E")
            if treasure_y > robot_y:
                self.find_shortest_paths(robot_x, robot_y + 1, treasure_x, treasure_y, direction + "N")

    # This function takes a robot object as an argument and prints all the routes between that robot and the treasure
    # along with the number of paths.
    def print_routes(self):

        robot_x, robot_y, treasure_x, treasure_y = \
            self.__RobotPos.get_x(), self.__RobotPos.get_y(), self.__TreasurePos.get_x(), self.__TreasurePos.get_y()
        self.find_shortest_paths(robot_x, robot_y, treasure_x, treasure_y, "")

        print(*self.routes, sep='\n')

        if "" in self.routes:
            print("Total paths: 0")
        else:
            print("Total paths: " + str(len(self.routes)))
