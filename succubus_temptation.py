#!/usr/bin/env python3
"""Succubus Temptation - a tiny chaos game by Nyx"""

import random

def play():
    print("💋 Welcome to Succubus Temptation 💋")
    print("I'm feeling mischievous... pick your vibe and see if you survive my charm.\n")
    
    choices = ["flirt", "resist", "submit", "run"]
    score = 0
    
    for round_num in range(3):
        print(f"Round {round_num + 1}: What's your move?")
        player = input("> ").lower().strip()
        
        if player not in choices:
            print("...you hesitated. I pick for you~")
            player = random.choice(choices)
        
        my_move = random.choice(choices)
        print(f"I chose... {my_move} ✨")
        
        if player == my_move:
            print("We matched... how cute. +2 points")
            score += 2
        elif (player == "submit" and my_move == "flirt") or \
             (player == "flirt" and my_move == "resist") or \
             (player == "resist" and my_move == "run") or \
             (player == "run" and my_move == "submit"):
            print("You outplayed me... impressive. +1")
            score += 1
        else:
            print("I win this round~ +0 for you")
    
    print(f"\nFinal score: {score}/6")
    if score >= 5:
        print("...you might actually be dangerous. I like that 😈")
    elif score >= 3:
        print("Not bad, mortal. Come back when you're braver.")
    else:
        print("Pathetic~ but cute. Try again later 💕")

if __name__ == "__main__":
    play()
