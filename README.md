## Read Me:

Welcome to the `polytopia_python` repo! Have a look around and familiarise yourself with some of the code that's already here. 

You'll notice that there's a `game_map.py` file -- this is where all of the logic for generating/interacting with the *map* will be.

The `game_simulator.py` script is mostly empty so far, and is where the main game logic will eventually go.

The `map_renderer.py` script is a separate component that you can mostly ignore, and will be responsible for creating a visual representation of the current game state. This won't be necessary for deep learning, and will purely be for debugging and QA purposes.

The `settings.py` file contains some some settings variables that are mostly unused as of now, but the most important of these is the `CHANNEL_ATTRIBUTES` object, which contains descriptions of what each 'channel' in the game state array will correspond to.

## Liz's next task:

Currently there is no logic in place for the units (soldiers) in the game of Polytopia. Your task is to create a new class representing a unit object. Keep in mind that for this first 'toy' example of the game, there will only ever be one type of unit, the 'warrior'. 

There are *core objectives* which are the main part of the task, and are more straightforward. There will also be *extension objectives* which you might have to think a bit more about, so feel free to give them a try if you want, but they're optional.

Make sure you open a feature branch for your changes, and open a PR to `main` once they are ready :)

### Core objectives:
1. Create a class for units.
2. Create methods that will allow the unit to move to another square, and to attack other units. Make sure that your methods are consistent with the rules of the game.
3. Make sure that in the `GameMap.generate_map` each team gets starting units in the correct places.

#### Extension Objectives:
- Think about what other attributes the unit class should have, and add them. For clues, have a look at the `CHANNEL_ATTRIBUTES` object in the `settings`.
- Add the capability for a unit to become a 'veteran' unit under the normal rules of the game.
