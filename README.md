## Read Me:

Welcome to the `polytopia_python` repo! Have a look around and familiarise yourself with some of the code that's already here. 

You'll notice that there's a `game_map.py` file -- this is where all of the logic for generating/interacting with the *map* will be.

The `game_simulator.py` script is mostly empty so far, and is where the main game logic will eventually go.

The `map_renderer.py` script is a separate component that you can mostly ignore, and will be responsible for creating a visual representation of the current game state. This won't be necessary for deep learning, and will purely be for debugging and QA purposes.

The `settings.py` file contains some some settings variables that are mostly unused as of now, but the most important of these is the `CHANNEL_ATTRIBUTES` object, which contains descriptions of what each 'channel' in the game state array will correspond to.
