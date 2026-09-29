NIGHT SHIFT
Approximate Prompt
Create a complete playable first-person 3D horror and cleaning game prototype called “Night Shift” using Python 3.13 and Ursina 8.3.0. The entire gameplay system should be contained in one complete main.py file. Do not rely on imported 3D models, Blender, FBX or GLB files. Build the environment, furniture, doors, stairs, first-person arm, mop, key, trash bag, electrical panel, restaurant, street and dumpster mainly from simple Ursina primitives such as cubes, quads and spheres.
The game takes place during a late-night cleaning shift inside a restaurant. The player begins in the restaurant basement, which contains a Janitor Room, Locker Room, Security Room, Electrical Room, Kitchen, Empty Room, corridor and stairwell. The basement should have a dark, dirty, industrial and slightly low-poly horror atmosphere while still remaining clearly visible and playable.
The game begins with a short cinematic introduction instead of immediately giving control to the player. During this sequence, the first-person arm and gameplay UI are hidden. The camera slowly moves through the basement corridor, enters the Locker Room and then moves into the Janitor Room. Cinematic black bars and the title “NIGHT SHIFT” are displayed. At the end of the sequence, the screen briefly fades to black, the camera attaches to the FirstPersonController, the first-person arm appears and gameplay begins automatically inside the Janitor Room.
The first task is to pick up a mop. Once collected, the mop becomes visible in the player’s hand. Near the Kitchen entrance there are exactly four dirty floor areas, each representing one square metre. The player must stand near the cleaning area and press F once for every square metre. Each press removes one dirty patch and updates the cleaning progress from 1/4 to 4/4.
After the fourth area is cleaned, the mop disappears from the player’s hand and the electricity suddenly fails. The basement becomes noticeably darker using a semi-transparent black overlay while remaining visible enough to navigate. The fluorescent lights become dim and the Electrical Room indicator becomes red.
The player then explores the Locker Room, where a yellow square post-it on a corkboard physically displays the number 1143. The player can also interact with the note to display “POST-IT CODE: 1143”.
The player then enters the Security Room and interacts with a computer. The Security Terminal allows the player to type a four-digit code. The correct code is 1143. Entering the correct code displays “ACCESS GRANTED” and informs the player that the key is located on the Kitchen countertop.
A gold key then appears on the Kitchen countertop. When collected, the key becomes visible in the player’s hand. The same key is used to unlock both the Electrical Room and the red Stairwell door, and the key is never consumed.
Inside the Electrical Room is a physical electrical switch. The switch is activated with F rather than E. Pressing F while looking at the switch restores the electricity, removes the blackout overlay, restores the lights and changes the Electrical Room indicator back to green.
A large black trash bag is physically present inside the Kitchen from the beginning of the game. It can be seen during the earlier objectives but cannot be collected until cleaning is complete and the power has been restored. Once the player is allowed to collect it, the trash bag disappears from the Kitchen and appears in the player’s hand.
The player then unlocks the red Stairwell door using the same key. Behind the door is a physical staircase consisting of ten steps, a landing and another ten steps. Every stair has a real collider so the player can walk and stand on the staircase correctly.
The staircase leads directly into the upper restaurant. It does not lead into a separate hallway. The upper restaurant is much larger than the basement rooms and contains a large dining area, at least seven table-and-chair groups, a service counter, ceiling lights and railings around the open staircase. The restaurant floor is built around the stair opening so the staircase remains physically open.
The player walks through the restaurant and exits through the main front door. Outside the restaurant is a nighttime street environment containing a sidewalk, road, road markings, another sidewalk, streetlights, surrounding buildings and a dumpster positioned across the road.
After leaving the restaurant, the player turns around and closes the front door. While standing outside and looking at the closed door, pressing E locks the restaurant permanently. This final restaurant lock does not require the key.
The player then crosses the road while carrying the trash bag. The dumpster already contains several pieces of garbage so it does not appear empty. Once the restaurant has been locked, the player can interact with the dumpster and throw the trash bag away.
After disposing of the trash, the gameplay UI disappears and player movement is disabled. The screen darkens and displays “YOU’VE FINISHED YOUR SHIFT...”. After a short delay, the text changes to “OR HAVE YOU?”. The game then displays a sudden jumpscare using the image stored at assets/images/jumpscare.png.
The project should prioritize simple and reliable gameplay systems over visual complexity. If there is a choice between a visually impressive but fragile implementation and a simple reliable implementation using primitives, the simpler solution should be preferred.
Project Overview
Night Shift is a short first-person horror and cleaning game prototype developed using Python and the Ursina game engine.
The player takes the role of a cleaner working alone during a late-night shift at a restaurant. What initially appears to be an ordinary cleaning job gradually turns into a strange and unsettling night.
The gameplay combines simple cleaning mechanics, first-person exploration, environmental clues, basic puzzle solving and a short horror storyline.
The main goal of the project is not photorealistic graphics. Instead, the game focuses on creating a complete gameplay loop using simple 3D geometry and understandable Python code.
Technology
Night Shift is developed with Python 3.13 and Ursina 8.3.0.
The game uses Ursina’s FirstPersonController for player movement.
Most of the environment is created directly inside Python using simple shapes such as cubes, quads and spheres. External 3D models are intentionally avoided so the project remains easier to understand, edit and debug.
Environment textures are used for materials such as concrete, wood and rusty metal.
Project Structure
The main gameplay logic is stored inside a single main.py file.
The assets folder contains the additional files used by the project. The images folder contains the jumpscare image. The textures folder contains the concrete, wood and metal textures used throughout the map. Models and sounds folders can remain available for future development even though the current version does not depend on imported 3D models.
The expected project structure is:
vib-game_night_shift
main.py
assets/images/jumpscare.png
assets/models
assets/sounds
assets/textures/environment/dirty_concrete
assets/textures/environment/oak_wood
assets/textures/environment/rusty_metal
Installation and Running
Python 3.13 should be installed on the computer.
Ursina can be installed using the command:
pip install ursina
After Ursina is installed and the project assets are placed in the correct folders, the game can be started by running main.py.
When the game starts, the cinematic introduction begins automatically. The player does not need to click to begin the game after the cinematic ends.
Controls
W, A, S and D are used for movement. The mouse controls the camera. Space is used to jump.
E is the main interaction key. It is used to pick up objects, open and close doors, interact with the Security computer, read the post-it, collect the key, collect the trash and use the dumpster.
F is used for special actions. It is used to mop the dirty floor and operate the electrical switch.
Escape releases the mouse during normal gameplay and closes the Security Terminal while the computer is being used.
After pressing Escape during normal gameplay, clicking the left mouse button resumes the game.
F10 exits the application.
Gameplay
The game begins with a cinematic camera sequence through the restaurant basement. The camera moves through the corridor, passes through the Locker Room and finishes inside the Janitor Room.
After the cinematic, the player receives the first objective: pick up the mop.
The mop is located inside the Janitor Room. When the player collects it, the mop becomes visible in the first-person view.
The next objective is to clean four square metres of dirty floor located near the Kitchen entrance. The dirty area is divided into four individual patches. Each press of F cleans one patch, meaning the player must press F four times to complete the task.
Once all four patches have been cleaned, the electricity suddenly fails.
The player must then investigate the basement.
Inside the Locker Room is a yellow post-it attached to a corkboard. The post-it displays the code 1143.
The player uses this code on the Security Room computer.
After entering 1143 into the Security Terminal, the computer informs the player that a key has been placed on the Kitchen countertop.
The player collects the key and uses it to unlock the Electrical Room.
Inside the Electrical Room, the player activates the electrical switch using F. This restores electricity to the restaurant.
The next objective is to take out the trash. A large black trash bag has been visible in the Kitchen since the beginning of the game. After the power has been restored, the player can finally collect it.
The player then uses the same key to unlock the red Stairwell door.
The staircase consists of ten steps, a landing and another ten steps. It leads directly into the upper restaurant dining room.
The player walks through the restaurant and exits through the main entrance.
After going outside, the player closes the restaurant door and locks the restaurant from the outside.
The player then crosses the road and approaches the dumpster on the opposite sidewalk.
Once the trash is thrown into the dumpster, the shift is apparently finished and the ending sequence begins.
Basement
The basement contains the Janitor Room, Locker Room, Security Room, Electrical Room, Kitchen, Empty Room, corridor and Stairwell.
The environment uses dark concrete walls and floors with a simple industrial appearance.
The rooms are connected through a fixed layout. The Janitor Room connects to the Locker Room. The Locker Room, Security Room, Electrical Room, Kitchen and Empty Room connect to the main corridor. The corridor also connects to the Stairwell.
The level intentionally avoids unnecessary extra doors so the floor plan remains easy to understand.
Janitor Room
The Janitor Room is the starting location for gameplay.
It contains basic cleaning equipment such as shelving, a cabinet, bucket and mop.
The mop is the player’s first interactive item.
Cleaning System
The cleaning area contains exactly four dirty floor patches.
Each patch represents one square metre.
The mop must be held before the cleaning action can be performed.
The player must also be close enough to the dirty area.
Every press of F cleans exactly one patch.
Cleaning progress is displayed as 1/4, 2/4, 3/4 and finally 4/4.
Completing the cleaning task triggers the power failure.
Locker Room
The Locker Room contains a long bench, clothes rack, hooks and corkboard.
The important object in this room is the yellow post-it.
The post-it visibly displays the number 1143.
This is the access code used for the Security Room computer.
Security Room
The Security Room contains a desk, chair, CCTV screens and the Security Terminal computer.
The player interacts with the computer using E.
The computer allows four-digit numeric input.
The correct access code is 1143.
Entering the correct code reveals the location of the key.
Kitchen
The Kitchen contains long countertops, a side counter, center island and refrigerator.
The key appears on one of the Kitchen countertops after the correct Security Terminal code has been entered.
The trash bag is also located inside the Kitchen.
Unlike the key, the trash bag is visible from the beginning of the game.
However, it cannot be collected until the cleaning objective has been completed and the electricity has been restored.
Electrical Room
The Electrical Room begins locked.
The player must use the key obtained from the Kitchen to enter.
Inside the room is a metal electrical panel, status indicator and electrical switch.
The electrical switch is activated using F.
After activation, the restaurant’s electricity is restored.
Power Failure
The power failure occurs immediately after the player finishes cleaning the four dirty floor sections.
During the blackout, the environment becomes darker but does not become completely black.
A transparent dark overlay is used to reduce visibility while keeping the game playable.
The basement fluorescent lights become dim and the electrical indicator changes to red.
After the player restores power, the darkness disappears and the electrical indicator becomes green.
Stairwell
The Stairwell is accessed through the red locked door.
The red door requires the same key used for the Electrical Room.
The electricity must also be restored before the door can be opened.
The staircase contains two flights of ten steps separated by a landing.
The stairs use real collision geometry so the player physically walks up them.
Upper Restaurant
The staircase ends directly inside the restaurant dining room.
The restaurant is intentionally much larger than the basement rooms.
The staircase opening remains visible in the floor and is surrounded by railings.
The restaurant contains multiple wooden tables and chairs, ceiling lights and a service counter.
The player walks through the dining area to reach the main entrance.
Restaurant Front Door
The restaurant front door leads directly outside.
The player opens the door, leaves the restaurant and then turns around.
The door must first be closed.
Once the player is outside and looking at the closed door, pressing E permanently locks the restaurant.
This final lock does not require the basement key.
Exterior
The exterior is a simple nighttime street environment.
The restaurant opens onto a sidewalk.
Beyond the sidewalk is a road with visible road markings.
Another sidewalk is located across the road.
Several simple buildings and streetlights are placed around the scene so the environment does not appear empty.
The dumpster is positioned on the opposite side of the road.
Dumpster
The dumpster is a large dark green container constructed from simple geometry.
Several garbage objects are already inside it so it does not appear empty.
The player cannot complete the dumpster objective until the restaurant has been locked.
Once the restaurant is secured and the player is carrying the trash bag, pressing E while looking at the dumpster disposes of the trash.
Task System
The game displays the current objective in a task panel in the upper-left corner.
The objectives follow the storyline in sequence.
The player begins by picking up the mop, then cleans four square metres of floor, investigates the power failure, discovers the code 1143, uses the Security computer, collects the Kitchen key, unlocks the Electrical Room, restores electricity, collects the trash, unlocks the Stairwell, enters the restaurant, leaves the building, locks the restaurant and finally throws the trash into the dumpster.
The task panel disappears during the intro cinematic and ending sequence.
Interaction System
The game uses a camera-forward raycast to detect interactive objects.
The player must look toward an object and remain within a short interaction distance.
Context-sensitive prompts appear near the bottom of the screen.
Examples include “[E] PICK UP MOP”, “[E] USE COMPUTER”, “[E] READ POST-IT”, “[E] PICK UP KEY”, “[F] USE POWER SWITCH”, “[E] PICK UP TRASH”, “[E] OPEN DOOR”, “[E] CLOSE DOOR”, “[E] LOCK RESTAURANT” and “[E] THROW TRASH”.
Held Item System
The player can visually hold the mop, key or trash bag.
Only one held object is displayed at a time.
When an object is collected, its world version disappears and a simplified first-person version becomes visible in front of the camera.
The objects are constructed from simple primitives rather than imported models.
Intro Cinematic
The game begins with a short cinematic sequence lasting approximately seven to nine seconds.
The first-person arm and interface are hidden during this sequence.
The camera starts in the basement corridor and slowly moves toward the Locker Room.
It then enters the Locker Room and continues into the Janitor Room.
The screen briefly fades to black at the end of the sequence.
Normal first-person control then begins automatically.
Ending
After the player throws the trash into the dumpster, movement is disabled and the gameplay interface disappears.
The screen becomes dark.
The message “YOU’VE FINISHED YOUR SHIFT...” appears.
After a short delay it changes to “OR HAVE YOU?”.
The final jumpscare is then triggered.
Jumpscare
The jumpscare uses the image located at:
assets/images/jumpscare.png
The image first appears relatively small and then rapidly expands toward the player.
The scaling animation lasts only around 0.10 seconds, making the jumpscare sudden and unexpected.
Design Philosophy
Night Shift is designed as a playable game prototype rather than a finished commercial production.
The main focus is on creating a complete gameplay loop, first-person interaction system, simple environmental storytelling and basic horror atmosphere.
The project intentionally prioritizes reliability and understandable code over graphical complexity.
Simple geometry is used whenever possible so the project remains easy to edit and develop further.
The complete gameplay loop is: arrive for the night shift, collect the mop, clean the basement, experience the power failure, discover the 1143 code, access the Security Terminal, obtain the key, restore electricity, collect the trash, unlock the Stairwell, enter the upper restaurant, leave through the front door, lock the restaurant, cross the road, throw the trash into the dumpster and encounter the final horror sequence.
