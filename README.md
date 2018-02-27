<h2>Overview:<h2>
<h5>Pop the Bubbles is a game written in Python utilizing Pygame. Use your mouse or trackpad to click on the bubbles and pop them before they reach the top of your screen. Once the bubbles fill your screen, you have lost the game. Each bubble is worth 15 points. You must earn 900 points to win each level. There are three total levels. The bubbles move faster and propagate more frequently in each subsequent level.</h5>

<h2>How to Download Python and Play the Game:<h2>
<h5>Go to this site to download Python: https://www.python.org/downloads/ This Pygame was created using Python version 2.7.13.</h5>

<h5>After you have downloaded Python, either clone or download this repository. Finally, open your terminal in Mac or Command Prompt in Windows, change into this repository file in your terminal, and type: python popthebubbles.py </h5>

<h2>Code Snippets:</h2>

<img src="introscreen.png" alt="Intro screen for Pop the Bubbles game">
<h5>Intro screen</h5>
<br />

<img src="bubbleclass.png" alt="Code for Bubble class">
<h5>Creation of bubble class</h5>
<br />

<img src="collisioncode.png" alt="Code for collision of bubbles">
<h5>Logic for bubble collision. Bubbles will only stop moving if they collide with a stopped bubble, which prevents bubble jams.</h5>
<br />

<img src="maingamelogic.png" alt="Main game logic code">
<h5>Code for main game loop. Game will continue as long as score is under 900 and no stopped bubbles have reached the bottom of the screen. Generates between 1-3 bubbles every three seconds (based on set timer for bubble drop event).</h5>
<br />


<h2>Screenshots:</h2>
<img src="introscreen.png" alt="Intro screen for Pop the Bubbles game">
<h5>Intro screen for the game</h5>
<br />
<img src="gameplay.png" alt="Screenshot during gameplay">
<h5>User must use their mouse or trackpad to pop the bubbles during gameplay</h5>
<br />
<img src="gameoverscreen.png" alt="Screenshot of game ending when bubbles fill the screen">
<h5>The game ends when any stopped bubble reaches the bottom of your screen.</h5>
<br />
