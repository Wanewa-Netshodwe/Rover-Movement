# Rover Movement Simulation

This Python program simulates the movement of a rover according to instructions from a text file. The rover can move and turn based on specific commands, and if enabled, it can display its path graphically using the `turtle` library. The program also includes obstacle collision detection in graphical mode.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Arguments](#arguments)
- [Instruction File Format](#instruction-file-format)
- [Graphical Mode](#graphical-mode)
- [Example](#example)
- [License](#license)

## Installation

Ensure you have Python installed on your system. You will also need the `turtle` library (standard with Python) and may use `argparse` for command-line arguments.

```bash
# Clone this repository
git clone https://github.com/your-username/rover-movement-simulation.git
cd rover-movement-simulation
```
## Usage
Run the program with a path to an instruction file. Optionally, use the --graphical flag to enable graphical representation.

```bash
python rover_movement.py <filepath> [--graphical]
```
# Arguments
- filepath: Path to the instruction file containing rover commands.
- --graphical: (Optional) Flag to enable graphical representation using the turtle library.
- Instruction File Format
- The instruction file should include commands in the following format, with each line specifying an action, value, unit, and direction:

```plaintext
[action] [value] [unit] [direction]
```
# Supported Commands
- Move - Moves the rover in a specific direction by a specified value.
- Units: meters
- Directions: forward, backward
- Turn - Turns the rover by a specified angle.

- Units: degrees
- Directions: clockwise, counterclockwise
## Example Instructions
```plaintext

move 10 meters forward
turn 90 degrees clockwise
move 5 meters backward
turn 45 degrees counterclockwise
```
# Graphical Mode
In graphical mode, the rover's movements are visually represented, with obstacles displayed as circles. The rover avoids or signals a collision when encountering obstacles.

Obstacle Detection: Obstacles are randomly placed on the screen. If the rover moves within 25 pixels of an obstacle, the obstacle changes color and shape to indicate a collision.
# Example
To run the rover with graphical mode enabled:

```bash

python rover_movement.py instructions.txt --graphical
```
