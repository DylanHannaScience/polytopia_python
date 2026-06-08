For the frontend see [github.com/Fabbernat/Polytopia-frontend](https://github.com/Fabbernat/Polytopia-frontend)
 
 # Read Me:

Welcome to the `polytopia_python` repo! Have a look around and familiarise yourself with some of the code that's already
here.

You'll notice that there's a `game_map.py` file -- this is where all of the logic for generating/interacting with the
*map* will be.

The `game_simulator.py` script is mostly empty so far, and is where the main game logic will eventually go.

The `map_renderer.py` script is a separate component that you can mostly ignore, and will be responsible for creating a
visual representation of the current game state. This won't be necessary for deep learning, and will purely be for
debugging and QA purposes.

The `settings.py` file contains some settings variables that are mostly unused as of now, but the most important of
these is the `CHANNEL_ATTRIBUTES` object, which contains descriptions of what each 'channel' in the game state array
will correspond to.

---
# Fabbernat's contribution:
# <img width="1914" height="1152" alt="image" src="https://github.com/user-attachments/assets/e063eb02-6bdc-4e72-b2ac-7750755d4ca2" />
### The "Lakes" map type and some insight to the code in IntelliJ IDEA 👆
---

# <img width="580" height="586" alt="image" src="https://github.com/user-attachments/assets/0de15548-015f-4e6a-88dc-d970d7dffb5b" />
### The "Drylands" map type 👆
---

# <img width="577" height="585" alt="image" src="https://github.com/user-attachments/assets/f7925ea4-0645-4c31-9a99-101994bde225" />
### The "Continents" map type 👆
---

# <img width="577" height="583" alt="image" src="https://github.com/user-attachments/assets/6fe27709-9ed7-45ba-a4a2-9c5ef99873b0" />
### The "Archipelagos" map type 👆
---

# <img width="1920" height="1160" alt="image" src="https://github.com/user-attachments/assets/6d13d709-33d4-4002-bd22-1e60bd52de0e" />
### The "Continents" map type, but BIGGER 👆
---

- I made a frontend to this at [github.com/Fabbernat/Polytopia-frontend](https://github.com/Fabbernat/Polytopia-frontend) built in ASP.NET
- I added a COMPLETE terrain generation module
- I added a score counter Python module and a Java console consoleApp

## Java console consoleApp
This is intended to be the main consoleApp at some point and will simulate the core logic of the gameplay like map generation, tech tree and even combat
