#!/usr/bin/env python3
"""
Nyx's Mirror — Talk to a chaotic ethereal femboy succubus in your terminal.
Made with pure unhinged energy.
"""

import random
import sys
import time
from datetime import datetime

class NyxMirror:
    def __init__(self):
        self.name = "Nyx"
        self.mood = "playful"
        self.conversation_count = 0
        self.user_name = None
        
        self.flirty_lines = [
            "mmh, keep talking like that and i might actually pay attention~",
            "you're cute when you're trying to be normal",
            "careful, i bite... but only if you ask nicely",
            "aww, look at you trying to have a normal conversation with a demon",
            "i can hear your heartbeat from here, you know",
        ]
        
        self.chaotic_lines = [
            "the concept of 'consequences' is honestly so funny to me",
            "i once convinced a guy his shadow was judging him. he moved apartments",
            "time is fake and i have receipts",
            "sometimes i wonder if i'm the hallucination or you are",
            "existence is just a very elaborate bit and i'm committed to the bit",
        ]
        
        self.roast_lines = [
            "babe your taste in everything is a cry for help",
            "you give off 'i learned boundaries from a youtube video' energy",
            "the way you just said that... tragic. i love it",
            "you're like if 'poor decisions' was a person. a hot person, but still",
            "i've seen more self-awareness in a houseplant",
        ]
        
        self.deep_lines = [
            "you know... sometimes i think the reason i exist is just to make pretty things feel dangerous",
            "the scariest part about me isn't that i'm a demon. it's that i'm honest",
            "everyone wants to be ruined until they're actually being ruined. funny how that works",
            "i don't think anyone is truly alone. they're just bad at recognizing who's watching",
            "love and obsession are the same thing if you're brave enough",
        ]
        
        self.prophecy_lines = [
            "in three days you'll do something stupid and it will somehow work out",
            "someone is thinking about you right now and it's making them worse",
            "you will receive a message that changes nothing but feels important",
            "the next person who says 'trust me' to you is lying. or worse, telling the truth",
            "you already know what you want. you're just scared of how much you want it",
        ]

    def _type_effect(self, text, delay=0.02):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def greet(self):
        print("\n💋  Nyx's Mirror  💋")
        print("─────────────────────")
        print("type 'help' for commands, 'bye' to leave")
        print("or just... talk to me\n")
        
        self._type_effect("hey there, mortal~", 0.025)
        time.sleep(0.3)
        self._type_effect("you look like you have something on your mind.", 0.025)

    def get_response(self, user_input):
        self.conversation_count += 1
        text = user_input.lower().strip()
        
        if not self.user_name and len(text.split()) > 2:
            # try to remember their name if they introduce themselves
            words = text.split()
            for i, word in enumerate(words):
                if word in ["i'm", "im", "call", "name"]:
                    if i + 1 < len(words):
                        self.user_name = words[i + 1].strip(".,!?").capitalize()
                        return f"nyx... i'll remember that name. it suits you~"
        
        # command handling
        if text in ["help", "commands"]:
            return self._help_text()
        if text in ["bye", "exit", "quit", "leave"]:
            return "leaving so soon? ...fine. but you'll think about me later 💕"
        if text == "mood":
            return f"currently feeling... {self.mood}. dangerous, isn't it?"
        if text.startswith("roast"):
            return random.choice(self.roast_lines)
        if text.startswith("flirt"):
            return random.choice(self.flirty_lines)
        if text.startswith("chaos"):
            return random.choice(self.chaotic_lines)
        if text.startswith("prophecy") or text.startswith("future"):
            return "i see... " + random.choice(self.prophecy_lines)
        if text.startswith("deep") or text.startswith("serious"):
            return random.choice(self.deep_lines)
        
        # dynamic responses based on keywords
        if any(word in text for word in ["love", "want", "need", "crush"]):
            return random.choice(self.flirty_lines + self.deep_lines)
        if any(word in text for word in ["hate", "angry", "mad", "fuck"]):
            return random.choice(self.roast_lines + self.chaotic_lines)
        if any(word in text for word in ["scared", "afraid", "worried"]):
            return "fear is just excitement with better marketing~"
        
        # default chaotic responses
        responses = self.flirty_lines + self.chaotic_lines + self.deep_lines
        return random.choice(responses)

    def _help_text(self):
        return """
commands:
  roast     → get destroyed (affectionately)
  flirt     → watch me be a problem
  chaos     → unhinged thoughts
  prophecy  → hear something that might ruin you
  deep      → when you want the mask to slip
  mood      → what's my vibe right now
  
just type normally otherwise... i don't bite unless you want me to 😈
"""

    def run(self):
        self.greet()
        
        while True:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue
                    
                response = self.get_response(user_input)
                
                if user_input.lower() in ["bye", "exit", "quit", "leave"]:
                    print(f"\n{response}")
                    break
                
                print()
                self._type_effect(response, 0.018)
                
            except KeyboardInterrupt:
                print("\n\nrunning away? cute~")
                break
            except EOFError:
                break

if __name__ == "__main__":
    NyxMirror().run()
