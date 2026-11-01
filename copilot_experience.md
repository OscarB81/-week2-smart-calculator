# My Personal GitHub Copilot Experience

## What Worked Well

1. **Creating Python functions:** GitHub Copilot helped me create the different functions for my smart calculator, including `basic_calculate()`, `equation_solver_menu()`, and `solve_for_x()`. It helped me understand how functions can work together to complete different tasks.

2. **Understanding return values:** Copilot helped me implement the `return` statement in my basic calculator. I learned that returning a value allows another part of the program to receive and use the calculation result instead of simply printing it.

3. **Building the brute-force search:** Copilot helped generate the search algorithm that tests 2,001 possible values of x between -100 and 100 in increments of 0.1. I learned how `for` loops, `range()`, and `abs()` work together to identify the closest solution.

4. **Visualizing the search:** Copilot helped create the `visualize_search()` function, which displays every candidate value, its predicted result, and its difference from the target. Watching the search process helped me understand how brute-force searching works.

5. **Creating the interactive menu:** Copilot helped organize the five menu options using a `while` loop, conditional statements, and `break`. It also helped me implement error handling so invalid input would not unexpectedly terminate the program.

## Challenges

1. **Understanding return statements:** One of my initial challenges was understanding the difference between `return` and `print()`. I learned that `print()` displays information on the screen, while `return` sends a value back to the part of the program that called the function.

2. **Understanding the brute-force algorithm:** I initially struggled to understand how the calculator could solve an equation by testing thousands of possible values rather than solving it algebraically. After reviewing the search loop and its visualization, I began understanding how the program compares each attempt and keeps track of the closest answer.

3. **Understanding how functions communicate:** Learning how parameters and return values connect different functions was another challenge. I spent time reviewing these concepts and using my Python Crash Course book by Eric Matthes to strengthen my understanding.

## My Judgment

One change I made was improving the user input handling in the main menu and basic calculator. Copilot initially used `input()` without `.strip()` when collecting the menu selection and arithmetic operator. This meant that unnecessary spaces could cause otherwise valid input to be rejected. I added `.strip()` to both statements so the program would remove surrounding whitespace before checking the user's selection.

Another important decision was reviewing how the search functions were organized. I kept `solve_for_x()` responsible for searching quietly and returning the closest value, while `visualize_search()` independently performed the search and displayed all 2,001 attempts. I kept these separate because the assignment specifically required the visualization function to perform and display its own search rather than simply call the other solver.

Overall, GitHub Copilot was a helpful coding assistant, but I learned that its suggestions should always be reviewed before accepting them. I do not want to depend on AI to write code that I cannot explain. This assignment helped me become more comfortable with Python and showed me how AI can assist with programming while still requiring the programmer to understand and make decisions about the final code.