# Connect Four Game

This project is a Connect Four command-line game.

## Project Description
This is a two-player command-line simulation of the well-known board game 'Connect Four'.

It uses principles of Object-Oriented Programming (OOP) and fully developed in Python. Each functionality and method fully tested and implemented, using pytest, following Test Driven Development (TDD) practices.

One of the main challenges faced with the development of this game is the diagonal checks. This was because the most efficent way of doing this would check for connect four for both x's and o's in all the diagonals once in one direction and the other diagonal in the other direction (which the time complexity would be about O(2n)). However, this came more challenging that I thought it to be, so I brute forced it it find all possible combinations, having a lot of nested loops.

Possible changes would definitely be to make the efficiency of the diagonal checks to be much better.

## How to Install and Run `Connect Four` Project
To be able to run the game, all you need is to have python installed.

To run the game:
- First type this in your terminal `export PYTHONPATH=$(pwd)`. 
- Then to run the actual gameplay type `python src/gameplay`.

To run the tests:
- Make sure you are in a virtual environment (venv). To create a venv, type this in your terminal `python -m venv venv`.
- To activate the venv type `source venv/bin/activate`.
- Next install all the requirements needed to test the functionality of the game. Type `pip install -r requirements.txt`.
- To run the tests type `pytest --testdox -vvvrP test/test_connect_four_game.py`.
- After you have finished running the tests make sure you deactivate the venv by typing `deactivate`.

## How to play `Connect Four` 
To place your counter all you need to do is enter the numbers between 0 and 6 insert your counter in the desired position.

Entering other characters should cause a error message to show in the terminal but should not crash the game.

To win your counter must stack next to each other four times in a row. 
The game will end once there is a winner or if the board is full and there is no winner.