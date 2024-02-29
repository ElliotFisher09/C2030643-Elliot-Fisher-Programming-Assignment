import tkinter as tk
from tkinter import ttk, messagebox
import random
from sympy import Symbol, sin, exp, integrate, diff, pi, sqrt

# Question 1

"""
    Check if n satisfies the condition (n % 6 == 5).



    Returns:
    True if n satisfies the condition, False otherwise.
    Error message if n is out of range (not between 1 and 100).
    """


def question1(n):
    if not (1 <= n <= 100):
        return "Error: Input must be between 1 and 100."
    return (n % 6 == 5)

# Question 2

"""
    Performs a mathematical operation based on the value of x.

    Returns:
    The result of the mathematical operation.
    Error message if the denominator is zero.
    """
def question2(x):
    if (3 * x - 7) == 0:
        return "Error: Denominator cannot be zero."
    else:
        result = ( (x**0.5) + (3 * x**5) ) / (3*x - 7)
        return result

# Question 3

"""
    Performs calculations using SymPy.

    Returns:
    A list containing the result of symbolic calculations.
    Error message if any exception occurs during the calculations.
    """
def question3(a, b, c, d):
    if not all(isinstance(val, (int, float)) for val in [a, b, c, d]):
        return "Error: All inputs must be numbers."

    x = Symbol('x')
    f_x = a * sin(b*x) + c * exp(d*x)

    try:
        f_5 = f_x.subs(x, 5)
        third_derivative = diff(f_x, x, 3)
        integral_result = integrate(f_x, (x, sqrt(6), 2*pi))

        return [f_5, third_derivative, integral_result,]

    except Exception as e:
        return f"Error: {e}"

# Question 4

"""
    A number guessing game using a GUI.

    The game generates a random number between 0 and 100.
    The player has 6 attempts to guess the number correctly.
    """

def question4():
    random_number = random.randint(0, 100)
    attempts_left = 6

    def check_guess():
        nonlocal attempts_left
        try:
            guess = int(txt.get())
            if guess < 0 or guess > 100:
                raise ValueError("Number out of range")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer between 0 and 100.")
            return

        attempts_left -= 1

        if guess == random_number:
            messagebox.showinfo("Congratulations!", "You guessed the correct number!")
            gui.destroy()
        else:
            hint = "Too low." if guess < random_number else "Too high."
            message = f"Your guess {guess} is {hint}. {attempts_left} attempts left."

            if attempts_left > 0:
                messagebox.showinfo("Incorrect Guess", message)
            else:
                messagebox.showinfo("Game Over", f"Sorry, you've reached the maximum number of attempts. The number was {random_number}.")
                gui.destroy()

    gui = tk.Tk()
    gui.title("Guess the Number")
    gui.geometry("300x150")

    ttk.Label(gui, text="Guess a number between 0 and 100:").pack()
    txt = tk.Entry(gui)
    txt.pack()
    ttk.Button(gui, text="Check", command=check_guess).pack()

    gui.mainloop()
    
    

