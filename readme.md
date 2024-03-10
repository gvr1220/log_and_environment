# Gettring Ready for Production: Devops, Cloud Computing, Environment Variables, Logging, and Continuous Integration

## Introduction

In this unit, we are adding three new features to our program that will start to prepare your program for use in a production environment.  

You will add the following features:

1.  GitHub Actions to run your tests on GitHub automaticly, which is your first steps toward having an understanding of Deveops.  Make sure that when you push to master, it runs the tests and try to find where it outputs the test results on GitHub.  

2.  Environmnent variables = Environment variables are also important because they are how you provide input to your program.  You use them to store passwords, api keys, etc... It's important to understand how to use them because they are your goto solution for providing input to your program, when you don't want to, or can't ask a user to provide the information.  You need to use Environment variables for API keys or other secure information because if you let an API key appear on GitHub, it will be banned within minutes.  You must create a .env file and put your key there and add the .env file to the .gitignore, so that when you put secret information in your local development environment that it isn't accidently posted to GitHub. Right now we don't have anything secret, so you can just add a key / value pair to identify your local development environment.  Check out my sample .env file [here](.sample.env) 

3.  Logging - Logging is how your program outputs information to external systems and is important for tracking application usage, security, and development, since you can use logging to output data like a print statement; however, as we start working with data in the following units, you will need a more effective way of viewing data in variables.

## Project Enhancements from Assignment 5

Incorporate the functionalities discussed in the lecture videos to your previous assignment. In your program a

## Required Viewing

1. Instructor Video Unit Overview - [here](https://youtu.be/hucp1naTcEY) - Note all the code is on the main branch I ended up making a new repo after I recorded the video.

2. Focus on Logging - [here](https://www.youtube.com/watch?v=pxuXaaT1u3k)

3. Focus on Environment Variables - [here](https://www.youtube.com/watch?v=8dlQ_nDE7dQ)

4. Introduction to DevOps - [here](https://www.youtube.com/watch?v=Xrgk023l4lI)

### Submission Requirements

1. Add a GitHub action to your project by copying my .github folder and the python-app.yml file that is in there and then click on the actions tab on your repository to see that when you push to the main branch that all your tests are run.

2.  Add the .env file and refer to the 
=======
# Project: Command Pattern and Plugins Homework 5

## Introduction

This project focuses on the development of an interactive command-line application that operates continuously, transitioning from a single-execution script to a fully functional application. Through this assignment, you will explore the command pattern, learn how to dynamically load commands using a simple plugin architecture, and understand the appropriate use of exceptions versus conditional statements to manage invalid data inputs. This unit lays the foundational skills for application development, preparing you for the midterm project, which requires a thorough explanation of your program's architecture, design patterns, and functionality.

## Project Enhancements from Assignment 4

Incorporate the functionalities discussed in the lecture videos to your previous assignment. This includes transforming your calculator program into an interactive application using the command pattern and REPL (Read, Evaluate, Print, Loop) principles.

### Submission Requirements

1. **Initial Setup:**
   - Watch the lecture on the main/command branch, which covers REPL and the command pattern. [Instructor Video: Command Pattern Lecture](https://youtu.be/3DVUN091T5g). Integrate these concepts with your existing program to add four basic commands: add, subtract, multiply, and divide, making your calculator interactive.

2. **(Bonus) Implement a Menu Command:**
   - Create a menu command that displays available commands from the command dictionary at the application's start and when the user types "menu." This is a self-guided challenge to deepen your understanding of dynamic command integration.

3. **Testing and Code Coverage:**
   - With the calculator commands integrated, update and expand your tests to achieve 100% test coverage, ensuring your program's functionality is fully verified.

4. **Plugin Architecture:**
   - View the lecture on implementing plugins [Instructor Video: Plugins Lecture](https://youtu.be/c2PmjazGW2w). Learn to refactor your program to automatically load plugins, facilitating easy command additions without manual updates.

5. **(Bonus) Explore Multiprocessing Capabilities:**
   - Investigate adding multiprocessing features to enable commands/plugins to run on separate cores. This enhancement is a forward-looking feature that prepares your application for future scalability and performance improvements.
>>>>>>> origin/main

## Grading Rubric (Total: 100 Points)

- **Testing (50 Points):**
  - Comprehensive test coverage near 100% average coverage: 50 Points

- **Functionality (50 Points):**
  - Implementation of command pattern and REPL: 10 Points
  - Interactive calculator commands (add, subtract, multiply, divide): 20 Points
  - Successful plugin architecture integration for dynamic command loading: 20 
Ensure that the functionality aligns with the requirements and demonstrates the effective use of the command pattern and plugin architecture as outlined in the instructor videos.

## Recommended Viewing
<<<<<<< HEAD
=======

To complement the project work, the following videos are highly recommended:

1. [Python Loop Performance](https://www.youtube.com/watch?v=Qgevy75co8c) - Insights into loop efficiency.
2. [Habits of The Good Programmer](https://www.youtube.com/watch?v=q1qKv5TBaOA&t=2s) - Design patterns and best practices.
3. [Global Interpreter Lock and Multicore Issues in Python](https://www.youtube.com/watch?v=m4zDBk0zAUY) - Python concurrency explained by its inventor.
4. [Design Patterns Explained](https://www.youtube.com/watch?v=tv-_1er1mWI) - General programming design patterns.
5. [5 Patterns in Python](https://www.youtube.com/watch?v=YMAwgRwjEOQ) - Applying patterns in Python.

## Project Setup

1. Clone the repository.
2. CD into the project folder.
3. Create and activate the virtual environment (VE).
4. Install the required libraries.

## Testing Commands

- Run all tests with `pytest`.
- To test a specific file, use `pytest tests/test_main.py`.
- For linting and coverage, `pytest --pylint --cov` commands can be used separately.

## Installed Libraries

1. [Pytest](https://docs.pytest.org/en/8.0.x/)
2. [Faker](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)

## Adding a Library

1. Ensure you're in the correct VE; if unsure, run "deactivate".
2. Activate the VE.
3. Update the requirements file with `pip freeze > requirements.txt`.
>>>>>>> origin/main

