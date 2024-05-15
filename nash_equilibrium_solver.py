#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------
# Nash Equilibrium Solver for Finite Two-Person Games
# --------------------------------------------------------------------------------
# Description:
# This script is designed to find the Nash equilibrium in finite two-person games.
# It is developed as part of the coursework for the course "Economics: Micro for Computer Science"
#
# Authors:
# - Sebastian Oes, sebastian.oes@student.unisg.ch
# - Timo Stricker, timo.stricker@student.unisg.ch
#
# University: University of St.Gallen
# Course: Economics: Micro for Computer Science
# --------------------------------------------------------------------------------
import numpy as np

def find_nash_equilibria(A, B):
    """
    Finds the Nash equilibria for two players given their payoff matrices.

    Parameters:
    - A (numpy.ndarray): Payoff matrix for Player 1.
    - B (numpy.ndarray): Payoff matrix for Player 2.

    Returns:
    - equilibria (list of tuples): List of action profiles (i, j) that are Nash equilibria.
    """
    n = A.shape[0]  # Number of strategies for each player
    equilibria = []

    for i in range(n):
        for j in range(n):
            # Check if Player 1's strategy i is a best response to Player 2's strategy j
            player1_best_response = np.all(A[i, j] >= A[:, j])
            # Check if Player 2's strategy j is a best response to Player 1's strategy i
            player2_best_response = np.all(B[i, j] >= B[i, :])

            # If both conditions are satisfied, (i, j) is a Nash equilibrium
            if player1_best_response and player2_best_response:
                equilibria.append((i + 1, j + 1))

    return equilibria

def print_results(equilibria):
    """
    Prints the Nash equilibria found.

    Parameters:
    - equilibria (list of tuples): List of action profiles that are Nash equilibria.
    """
    if equilibria:
        for eq in equilibria:
            print(f"The action profile {eq} is a Nash equilibrium.")
    else:
        print("No pure strategy Nash equilibrium exists.")

def input_matrix(n, player):
    """
    Prompts the user to input a payoff matrix for a given player.

    Parameters:
    - n (int): Dimension of the matrix (number of strategies).
    - player (str): Player identifier (e.g., "Player 1" or "Player 2").

    Returns:
    - matrix (numpy.ndarray): The entered payoff matrix.
    """
    print(f"Enter the payoff matrix for {player}:")
    while True:
        try:
            entries = [input(f"Enter row {i + 1} (space-separated): ").strip().split() for i in range(n)]
            matrix = np.array(entries, dtype=int)
            if matrix.shape != (n, n):
                raise ValueError("Matrix must be square with dimension n x n")
            return matrix
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    """
    Main function to run the Nash Equilibrium Finder program.
    """
    while True:
        # Clear the screen
        print("\033c", end="")
        print("=" * 30)
        print("Welcome to the Nash Equilibrium Finder")
        print("=" * 30)
        print("1. Input matrices")
        print("2. Exit")
        print("-" * 30)
        choice = input("Choose an option (1 or 2): ")

        if choice == '1':
            n = int(input("\nEnter the matrix dimension >= 2: "))
            A = input_matrix(n, "Player 1")
            B = input_matrix(n, "Player 2")
            equilibria = find_nash_equilibria(A, B)
            print_results(equilibria)
            input("\nPress enter to continue...")
        elif choice == '2':
            print("\nExiting program. Thank you for using the Nash Equilibrium Finder!")
            break
        else:
            print("\nInvalid input. Please enter a valid option (1 or 2).")

if __name__ == "__main__":
    main()
