# Cricket Match Simulation

This project is a Python-based cricket match simulation that allows users to simulate a cricket match between two teams. The simulation employs various classes and modules to create an interactive and dynamic cricket match experience.

## Methodology

The project is structured using object-oriented programming principles to achieve modularity, reusability, and maintainability. The methodology of the project involves the following key components:

### 1. Classes and Modules

The project is divided into several classes, each responsible for a specific aspect of the cricket match simulation:

- **Field**: Represents the field conditions, such as field type (dry or wet) and field size (large, medium, small). The `run_scoring_difficulty` method adjusts run scoring based on field conditions.

- **Umpire**: Simulates the umpire's role, including making decisions and tossing the coin to decide which team bats or bowls. The `make_decision` and `toss` methods contribute to the game's randomness and dynamics.

- **Commentator**: Provides commentary on the match events. The `display_event` method outputs commentary for each ball bowled, adding realism to the simulation.

- **Match**: Orchestrates the entire match simulation. It initializes instances of the `Field`, `Umpire`, and `Commentator` classes. The `innings` method simulates a team's innings, and the `run_match` method runs the entire match, including both innings and displaying the result.

### 2. Run Scoring Difficulty

The simulation introduces a run scoring difficulty mechanism based on field conditions. If the field type is "wet" or the field size is "large," the run scoring is adjusted to be harder. This introduces variability and strategy into the simulation, where the outcome of the match can be influenced by the chosen field conditions.
(If you choose "wet" or "large" then the score will reduce by 1 run on every ball!)
### 3. User Interaction

The simulation prompts the user to input field conditions, such as field type (dry or wet) and field size (large, medium, small), before running the match. This user interaction adds an element of control and customization, allowing users to set the stage for the match according to their preferences.

### 4. Randomness and Realism

The project incorporates randomness through dice rolling for ball outcomes and decision-making. This randomness, combined with the adjusted run scoring based on field conditions, creates a realistic and engaging cricket match simulation.

## Getting Started

To run the simulation, execute the provided Python script. Follow the prompts to input the desired field type and field size. The simulation will then proceed to simulate a complete cricket match, displaying commentary and match results.

* Install Python
* Change the directory to the root directory
* Run the following command
```
python criket.py
```
## Match Variables

You can update the following variables to personalize your match:

* _team1_ - the name of the team that will bat first
* _team2_ - the name of the team that will bat second
* _oversPerTeam_ - the number of overs per innings. Set equal to unlimitedOvers if you do not want to play a limited overs match
* _gameRate_ - the number of seconds between each ball. Used to control the speed of the game

## Conclusion

The cricket match simulation project showcases the effective use of object-oriented programming, user interaction, and randomness to create an immersive and dynamic cricket match experience. By following the provided methodology, the project achieves a balance between realism and entertainment, making it an enjoyable tool for cricket enthusiasts and learners alike.
