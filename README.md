# E-Puck Maze Solver with Line Following

## Overview

This project involves programming an E-Puck robot to navigate a maze, manipulate boxes, and follow a line. The robot utilizes various sensors, including proximity sensors, ground sensors, and cameras, to perceive its environment and make decisions accordingly.

## Features

- **Maze Navigation**: The robot is capable of autonomously navigating through a maze using proximity sensors to detect obstacles and determine the appropriate path.
- **Box Manipulation**: It can interact with boxes placed within the maze, pushing them along the path to clear the way or collecting them for specific tasks.
- **Line Following**: The robot employs ground sensors to track and follow a line, enabling precise movement along designated paths.
- **Color Recognition**: Utilizing cameras, the robot can identify the colors of objects, allowing it to make decisions based on the detected colors.

## Components

- **Sensors**: Proximity sensors, ground sensors, and cameras are used to perceive the robot's surroundings and gather relevant information.
- **Actuators**: Motors control the movement of the robot's wheels, enabling it to navigate and manipulate objects.
- **Control Logic**: The core logic of the robot, including decision-making algorithms, PID controllers for motor control, and object detection routines.

## Operation

1. **Line Following**: The robot starts by following a line using ground sensors until it reaches a designated point.
2. **Color Detection**: Upon reaching the designated point, the robot uses cameras to detect the colors of nearby objects, such as boxes.
3. **Maze Navigation**: Based on the detected colors, the robot decides its path through the maze, avoiding certain boxes and collecting others.
4. **Box Manipulation**: As the robot progresses through the maze, it interacts with boxes using its actuators to clear obstacles or accomplish specific tasks.
5. **End Goal**: The ultimate objective is to successfully navigate the maze, collect required items, and reach the end point.

## Future Enhancements

- **Path Planning**: Implementing advanced path planning algorithms to optimize the robot's navigation through the maze.
- **Object Recognition**: Enhancing object recognition capabilities to identify and classify objects more accurately.
- **Collision Avoidance**: Improving collision avoidance strategies to enable smoother and more efficient movement in complex environments.

## Usage

To replicate and experiment with this project:

1. Set up the E-Puck robot with the required sensors and actuators.
2. Install the necessary dependencies and libraries as specified in the project's documentation.
3. Upload the provided code to the robot's control unit.
4. Calibrate and fine-tune the robot's parameters to suit the specific maze environment.
5. Run the program and observe the robot's behavior as it navigates the maze and completes tasks.

## Credits

This project was developed as part of paractical project of the robotic course at Damascus university


For any inquiries or support, please contact [hayanjaber6@gmail.com].

