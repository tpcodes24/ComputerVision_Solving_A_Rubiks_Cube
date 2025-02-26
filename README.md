Rubik's Cube Solver - Python

Overview

This is a Python-based Rubik's Cube color resolver and solver that processes scanned color data to determine a valid cube representation. It utilizes the rubikscolorresolver library to analyze the cube's color scheme and outputs the data in a format suitable for solving.

Features

Accepts Rubik's Cube color data from a JSON file or as a direct JSON string.

Resolves cube colors and translates them into a valid cube representation.

Supports output in JSON format or Kociemba-compatible strict notation.

Error logging for debugging and troubleshooting.

Dependencies

Ensure you have Python 3 installed along with the following dependencies:

pip install rubikscolorresolver

Usage

Running the Solver

python rubiks_solver.py --filename <path_to_json>

OR

python rubiks_solver.py --rgb '<json_string>'

Optional Arguments

-j, --json : Print results in JSON format.

--filename <file> : Provide a JSON file containing Rubik's Cube RGB scan data.

--rgb '<json_string>' : Provide Rubik's Cube RGB scan data as a JSON string.

Example

python rubiks_solver.py --rgb '{"0": [255, 0, 0], "1": [0, 255, 0], "2": [0, 0, 255], ...}'

How It Works

Reads the cube's color data from a file or JSON string.

Parses and converts the scan data into a structured format.

Initializes a RubiksColorSolverGeneric object and processes the cube colors.

Outputs the cube's representation in a structured format.

Error Handling

If no valid input is provided, the script will return:

ERROR: Neither --filename or --rgb was specified

If any parsing or processing error occurs, detailed logs are stored using Python's logging module.

Logging

Logging is enabled for debugging purposes. Logs will be printed in the console using color-coded warnings and errors.

License

This project is licensed under the MIT License.

Contributors

Feel free to contribute by submitting issues and pull requests!

For further improvements or integrations, you may explore extending it with Kociemba’s solver for full Rubik’s Cube solving capabilities.

