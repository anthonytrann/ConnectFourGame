# ConnectFourGame

This project is a Connect Four command-line game.

## Project Description
This is a two-player command-line simulation of the well-known board game 'Connect Four'.

It uses principles of Object-Oriented Programming (OOP) and fully developed in Python. Each functionality and method fully tested and implemented, using pytest, following Test Driven Development (TDD) practices.

One of the main challenges faced with the development of this game is the diagonal checks. This was because the most efficent way of doing this would check for connect four for both x's and o's in all the diagonals once in one direction and the other diagonal in the other direction (which the time complexity would be about O(2n)). However, this came more challenging that I thought it to be, so I brute forced it it find all possible combinations, having a lot of nested loops.

Possible changes would definitely be to make the efficiency of the diagonal checks to be much better.
