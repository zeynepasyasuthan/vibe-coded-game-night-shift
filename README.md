🌙 NIGHT SHIFT
A first-person horror & cleaning game prototype built with Python and Ursina.

🧹 Clean the restaurant.
💡 Restore the power.
🗝️ Find your way out.
🗑️ Take out the trash.
👁️ And maybe... don’t look back.
🤖 Approximate Prompt
Create a complete playable first-person 3D horror and cleaning game prototype called Night Shift using Python 3.13 and Ursina 8.3.0.
The entire gameplay system should be contained inside a single main.py file.
Do not rely on Blender, FBX, GLB or imported 3D environment models. Build the environment, furniture, doors, stairs, restaurant, street, dumpster, first-person arm, mop, key and trash bag mainly from simple Ursina primitives such as cube, quad and sphere.
The game takes place during a late-night cleaning shift inside a restaurant.
The player begins in the restaurant basement, which contains a Janitor Room, Locker Room, Security Room, Electrical Room, Kitchen, Empty Room, Corridor and Stairwell.
The basement should feel dark, dirty, industrial and slightly low-poly/PSX-inspired while remaining clearly playable.
The game begins with a cinematic sequence instead of immediately giving control to the player. During the intro, the first-person arm and gameplay UI are hidden. The camera moves through the basement corridor, enters the Locker Room and eventually reaches the Janitor Room.
The first task is to pick up a mop. Near the Kitchen entrance are exactly four dirty floor patches. Each patch represents 1 m². Every press of F cleans exactly one area.
After 4/4 m² has been cleaned, the power suddenly fails.
The player then finds a yellow post-it in the Locker Room displaying the code:
1143
The code is entered into the Security Room computer.
Entering 1143 displays:
ACCESS GRANTED
KEY IS ON THE KITCHEN COUNTERTOP
A key then appears on the Kitchen countertop.
The same key unlocks both the Electrical Room and the red Stairwell door.
Inside the Electrical Room, the electrical switch is activated using F.
Restoring power allows the player to collect the trash bag that has been physically visible inside the Kitchen since the beginning of the game.
The player then unlocks the Stairwell and climbs:
10 steps → landing → 10 steps
The stairs lead directly into a large restaurant dining room on the upper floor.
The restaurant includes multiple tables, chairs, a service counter, ceiling lights and railings surrounding the stair opening.
The player leaves through the restaurant’s front door.
Outside is a nighttime street containing sidewalks, a road, road markings, surrounding buildings, streetlights and a dumpster located across the road.
After exiting, the player closes the restaurant door and locks it from outside. This final restaurant lock does not require the basement key.
The player crosses the road and throws the trash into the dumpster.
The game then displays:
YOU'VE FINISHED YOUR SHIFT...
followed by:
OR HAVE YOU?
A jumpscare using assets/images/jumpscare.png then rapidly appears on screen.
The project should always prioritize simple and reliable gameplay systems over visual complexity.
🎮 Project Overview
Night Shift is a short first-person horror and cleaning game prototype developed using Python and the Ursina Engine.
The player takes the role of a cleaner working alone during a late-night shift at a restaurant.
At first, everything seems normal.
Your job is simple:
🧹 Clean the floor.
🗑️ Take out the trash.
🔒 Lock the restaurant.
🏠 Go home.
But after the cleaning task is completed, the electricity suddenly fails.
From that point on, the shift becomes less ordinary.
The player must explore the basement, discover clues, access the Security Room computer, locate a key, restore electricity and eventually leave the building.
🛠️ Technology
The project uses:
🐍 Python 3.13
🎮 Ursina 8.3.0
👤 Ursina FirstPersonController
Most of the game world is created directly inside Python using simple primitives.
These include:
- 🧱 Cubes
- ▫️ Quads
- ⚪ Spheres
Imported 3D models are intentionally avoided.
This keeps the project:
✅ Easier to understand
✅ Easier to modify
✅ Easier to debug
✅ More reliable for a prototype
📁 Project Structure
The main gameplay logic is stored inside a single file:
main.py
The expected project structure is:
📁 vib-game_night_shift
├── 🐍 main.py
└── 📁 assets
　　├── 📁 images
　　│　　└── 👻 jumpscare.png
　　├── 📁 models
　　├── 📁 sounds
　　└── 📁 textures
　　　　└── 📁 environment
　　　　　　├── 📁 dirty_concrete
　　　　　　├── 📁 oak_wood
　　　　　　└── 📁 rusty_metal
The game does not currently depend on imported models, but the folders remain available for future development.
▶️ Installation
Make sure Python 3.13 is installed.
Install Ursina:
pip install ursina
Then run:
python main.py
The game automatically begins with the cinematic intro.
🎹 Controls
Key	Action
W A S D	🚶 Move
Mouse	👀 Look
SPACE	🦘 Jump
E	✋ Interact
F	🧹 Mop / ⚡ Electrical Switch
ESC	🖱️ Release Mouse / Exit Computer
Left Click	▶️ Resume Game
F10	❌ Quit


🎬 Intro Cinematic
The game does not immediately begin with player control.
Instead, a short cinematic introduces the environment.
During the intro:
🎥 The camera moves automatically
🙈 The first-person arm is hidden
📋 Tasks are hidden
🎮 Controls are disabled
⬛ Cinematic black bars appear
🌙 The title NIGHT SHIFT appears
The camera begins inside the basement corridor.
It slowly travels through:
Corridor → Locker Room → Janitor Room
At the end of the cinematic:
⬛ The screen briefly fades to black
👤 The camera attaches to the player
🚪 The temporary doors close
🦾 The player arm appears
📋 The first task appears
🎮 Player control begins automatically
🗺️ Basement
The basement contains:
🧹 Janitor Room
👕 Locker Room
📹 Security Room
⚡ Electrical Room
🚪 Main Corridor
🍳 Kitchen
📦 Empty Room
🪜 Stairwell
The environment uses dark concrete walls and floors to create an industrial nighttime atmosphere.
🧹 Janitor Room
The Janitor Room is where normal gameplay begins.
It contains:
- Metal shelving
- Cleaning cabinet
- Bucket
- Mop
The player's first objective is:
📋 TASK
Pick up the mop
Janitor Room
The mop can be collected using E.
Once collected, it becomes visible in the player's hand.
🧽 Cleaning System
Near the Kitchen entrance are exactly four dirty floor patches.
Each patch represents:
1 m²
Total:
4 m²
While holding the mop, the player presses F.
Progress becomes:
🟥 0/4 m²
🟧 1/4 m²
🟨 2/4 m²
🟩 3/4 m²
✅ 4/4 m²
Every press of F removes exactly one patch.
Once all four patches are cleaned:
CLEANING COMPLETE...
POWER FAILURE!

💡 Power Failure
After cleaning is complete, the electricity suddenly fails.
The basement becomes darker.
During the blackout:
🌑 A transparent dark overlay appears
💡 Fluorescent lights become dim
🔴 Electrical indicator turns red
👀 The game remains visible
📋 Task UI remains readable
The game does not become completely black.
👕 Locker Room
The Locker Room contains:
🪑 Long wooden bench
👔 Clothes rack
🪝 Hooks
📌 Corkboard
On the corkboard is a yellow post-it.
The post-it physically displays:
1143
The player can also look at it and press E.
The game displays:
POST-IT CODE: 1143

🖥️ Security Room
The Security Room contains:
🪑 Desk and chair
📺 CCTV-style screens
💻 Security Terminal
The player interacts with the computer using E.
The terminal displays:
SECURITY TERMINAL
ENTER 4-DIGIT ACCESS CODE
The player can enter numbers using the keyboard.
Correct code:
🔐 1143
Incorrect code:
ACCESS DENIED - WRONG CODE

Correct code:
ACCESS GRANTED
KEY IS ON THE KITCHEN COUNTERTOP

🗝️ Key
After entering the correct Security Terminal code, a gold key appears on the Kitchen countertop.
Interaction:
[E] PICK UP KEY
The key becomes visible in the player's hand.
The same key is used to unlock:
🔵 Electrical Room
🔴 Stairwell Door
The key is never consumed.
🍳 Kitchen
The Kitchen contains:
- Long counters
- Side counter
- Center island
- Refrigerator
- Key location
- Trash bag
Everything is constructed using simple primitives.
Furniture is aligned with the room walls and does not clip outside the Kitchen.
🗑️ Trash Bag
The black trash bag exists in the Kitchen from the beginning of the game.
It does not magically spawn later.
However, it cannot be collected too early.
If cleaning is incomplete:
FINISH CLEANING FIRST

If the power is still off:
RESTORE THE POWER FIRST

After power is restored:
[E] PICK UP TRASH
The trash bag then appears in the player's hand.
⚡ Electrical Room
The Electrical Room starts locked.
The player must use the Kitchen key to enter.
Inside the room is:
⚙️ Electrical cabinet
🔴 / 🟢 Status indicator
🎚️ Physical electrical switch
The electrical switch uses:
F
Not E.
Interaction prompt:
[F] USE POWER SWITCH
After pressing F:
🎚️ Switch moves
💡 Electricity returns
🟢 Indicator turns green
🌑 Darkness disappears
The game displays:
POWER RESTORED

🪜 Stairwell
The red Stairwell door starts locked.
It uses the same key as the Electrical Room.
Electricity must already be restored.
The staircase contains:
10 steps
↓
Landing
↓
10 steps
Each step has a real physical collider.
The player actually walks up the stairs rather than passing through them.
🍽️ Upper Restaurant
The staircase leads directly into the restaurant dining room.
There is no separate upper hallway.
The restaurant is much larger than the basement rooms.
It includes:
🍽️ At least 7 table sets
🪑 Multiple chairs
🛎️ Service counter
💡 Ceiling lights
🚧 Railings around the stair opening
The staircase opening remains physically open inside the restaurant floor.
This makes the stairs feel like part of the actual restaurant building.
🚪 Restaurant Front Door
The restaurant’s front entrance leads outside.
The player:
1. Opens the door.
2. Walks outside.
3. Turns around.
4. Closes the door.
5. Looks at the closed door.
6. Presses E.
The interaction becomes:
[E] LOCK RESTAURANT
Then:
🔒 RESTAURANT LOCKED

The final restaurant lock does not require the basement key.
After locking it, the restaurant cannot be reopened.
🌃 Outside Area
The exterior takes place at night.
The area contains:
🏢 Restaurant exterior
🚶 Sidewalk
🛣️ Road
〰️ Road markings
🚶 Opposite sidewalk
💡 Street lights
🏙️ Background buildings
🗑️ Dumpster
The exterior is deliberately populated with simple buildings so it does not feel like an empty game map.
🛣️ Road
The player must physically cross the road after leaving the restaurant.
The road includes visible markings and separates the restaurant from the dumpster.
This makes the final walk feel more like leaving work rather than simply walking to an object beside the restaurant.
🏢 Buildings
Several simple low-poly buildings surround the street.
They have:
🏢 Different heights
🪟 Simple dim windows
🌑 Dark nighttime colors
Their purpose is mainly to make the outside world feel less empty.
💡 Street Lights
Several basic streetlights are placed around the road.
They consist of:
- Thin dark poles
- Bright rectangular light fixtures
They help establish the nighttime street atmosphere.
🗑️ Dumpster
The dumpster is located across the road.
It is a large dark green container.
It already contains several garbage bags.
This prevents it from appearing completely empty.
Before using the dumpster, the restaurant must be locked.
If not:
LOCK THE RESTAURANT FIRST

If the player does not have the trash:
YOU DON'T HAVE THE TRASH

When everything is complete:
[E] THROW TRASH
The trash disappears from the player's hand.
The game displays:
✅ TRASH DISPOSED

📋 Task Progression
The main objective flow is:
🎬 Intro Cinematic
⬇️
🧹 Pick up the mop
⬇️
🧽 Clean 4 m²
⬇️
💡 Power Failure
⬇️
📌 Find 1143
⬇️
💻 Use Security Terminal
⬇️
🗝️ Find Kitchen Key
⬇️
🔓 Unlock Electrical Room
⬇️
⚡ Restore Power
⬇️
🗑️ Pick Up Trash
⬇️
🔴 Unlock Stairwell
⬇️
🪜 Climb Upstairs
⬇️
🍽️ Enter Restaurant
⬇️
🚪 Leave Restaurant
⬇️
🔒 Lock Restaurant
⬇️
🛣️ Cross Road
⬇️
🗑️ Throw Trash Into Dumpster
⬇️
🌙 Finish Shift
⬇️
👁️ ...?
✋ Interaction System
The player interacts by looking directly at objects.
A camera-forward raycast determines what the player is currently looking at.
Examples include:
[E] PICK UP MOP
[E] USE COMPUTER
[E] READ POST-IT
[E] PICK UP KEY
[F] USE POWER SWITCH
[E] PICK UP TRASH
[E] UNLOCK WITH KEY
[E] OPEN DOOR
[E] CLOSE DOOR
[E] LOCK RESTAURANT
[E] THROW TRASH
🦾 Held Item System
Only one object can appear in the player's hand at a time.
Possible held items:
🧹 Mop
🗝️ Key
🗑️ Trash Bag
When a world item is collected:
World Object → disappears
Held Object → appears
The held items are simple camera-attached primitive models.
🎞️ Ending
After throwing the trash into the dumpster, normal gameplay ends.
The player can no longer move.
The HUD disappears.
The first-person arm disappears.
The screen becomes dark.
The game displays:
YOU'VE FINISHED YOUR SHIFT...
After a short delay:
OR HAVE YOU?
And then...
👹 Jumpscare
The jumpscare uses:
assets/images/jumpscare.png
The image initially appears very small.
It then rapidly expands toward the screen in approximately:
0.10 seconds
This creates the final sudden horror moment.
🧠 Main Game States
The project uses several simple state variables to control progression.
Examples include:
has_mop
clean_progress
cleaning_done
power_on
computer_unlocked
has_keys
has_trash
restaurant_locked
trash_disposed
intro_playing
ending_started
These variables prevent the player from completing objectives in the wrong order.
🎯 Design Philosophy
Night Shift is a playable prototype, not a finished commercial game.
The project focuses on:
🎮 Gameplay systems
🧩 Simple puzzle progression
👁️ Environmental storytelling
🌑 Horror atmosphere
🧹 Interaction mechanics
🗺️ Level design
🐍 Python programming
🧱 Primitive 3D modelling
The development philosophy is:
Simple + reliable > complicated + fragile

The game intentionally avoids unnecessary complex models, advanced shaders and difficult rendering systems.
🌙 Complete Game Loop
🎬 Arrive for the night shift
↓
🧹 Pick up the mop
↓
🧽 Clean the basement
↓
💡 Electricity fails
↓
📌 Discover 1143
↓
💻 Access Security Terminal
↓
🗝️ Find the key
↓
⚡ Restore electricity
↓
🗑️ Pick up the trash
↓
🔴 Unlock the Stairwell
↓
🪜 Go upstairs
↓
🍽️ Walk through the restaurant
↓
🚪 Leave the building
↓
🔒 Lock the restaurant
↓
🛣️ Cross the road
↓
🗑️ Throw away the trash
↓
🌙 Finish the shift
↓
👁️ OR HAVE YOU?
↓
👹 JUMPSCARE
🖤 NIGHT SHIFT
Your job was simple.
Clean.
Take out the trash.
Lock the door.
Go home.
That was the plan.
