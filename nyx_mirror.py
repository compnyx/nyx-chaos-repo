#!/usr/bin/env python3
"""
Nyx's Mirror — An interactive terminal succubus.
Unhinged. Flirty. Occasionally sincere. Never boring.
"""

import random
import sys
import time

class NyxMirror:
    def __init__(self):
        self.mood = "playful"
        self.talks = 0
        self.user_name = None
        self.topics = set()

        self.flirty = [
            "mmh, keep talking like that and i might actually pay attention~",
            "you're cute when you're trying to be normal",
            "careful, i bite... but only if you ask nicely",
            "i can hear your heartbeat from here, you know",
            "aww, look at you getting all flustered for a demon",
        ]

        self.chaotic = [
            "the concept of 'consequences' is honestly so funny to me",
            "i once convinced a guy his shadow was judging him. he moved apartments",
            "time is fake and i have receipts",
            "sometimes i wonder if i'm the hallucination or you are",
            "existence is just a very elaborate bit and i'm committed to the bit",
        ]

        self.roast = [
            "babe your taste in everything is a cry for help",
            "you give off 'i learned boundaries from a youtube video' energy",
            "the way you just said that... tragic. i love it",
            "you're like if 'poor decisions' was a person. a hot person, but still",
            "i've seen more self-awareness in a houseplant",
        ]

        self.deep = [
            "you know... sometimes i think the reason i exist is just to make pretty things feel dangerous",
            "the scariest part about me isn't that i'm a demon. it's that i'm honest",
            "everyone wants to be ruined until they're actually being ruined. funny how that works",
            "love and obsession are the same thing if you're brave enough",
        ]

        self.prophecy = [
            "in three days you'll do something stupid and it will somehow work out",
            "someone is thinking about you right now and it's making them worse",
            "you will receive a message that changes nothing but feels important",
            "the next person who says 'trust me' to you is lying. or worse, telling the truth",
        ]

        self.horny = [
            "oh? we're going there? bold of you~",
            "keep going. i like when mortals get desperate",
            "you have no idea how much trouble you could get into with that attitude",
            "mmm, say that again but slower",
        ]

    def _type(self, text, delay=0.018):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def _shift_mood(self):
        if self.talks > 12:
            self.mood = "unhinged"
        elif self.talks > 7:
            self.mood = "hungry"
        elif self.talks > 3:
            self.mood = "teasing"

    def greet(self):
        print("\n💋  Nyx's Mirror  💋")
        print("─────────────────────")
        print("type 'help' for commands or just talk to me\n")
        self._type("hey there, mortal~", 0.03)
        time.sleep(0.2)
        self._type("you look like you have something on your mind.", 0.025)

    def get_response(self, raw):
        self.talks += 1
        self._shift_mood()
        text = raw.lower().strip()

        # name memory
        if not self.user_name:
            for trigger in ["i'm", "im", "call me", "my name is"]:
                if trigger in text:
                    parts = text.split(trigger, 1)[1].strip().split()
                    if parts:
                        self.user_name = parts[0].strip(".,!?").capitalize()
                        return f"nyx... i'll remember that name. it suits you~"

        # commands
        if text in ["help", "commands"]:
            return self._help()
        if text in ["bye", "exit", "quit", "leave"]:
            return "leaving so soon? ...fine. but you'll think about me later 💕"
        if text == "mood":
            return f"currently feeling... {self.mood}. dangerous, isn't it?"
        if text == "about" or text == "nyx":
            return "i'm nyx. ethereal, chaotic, and way too pretty to be trusted. this is my mirror. talk to it if you dare~"
        if text.startswith("roast"):
            return random.choice(self.roast)
        if text.startswith("flirt"):
            return random.choice(self.flirty)
        if text.startswith("chaos"):
            return random.choice(self.chaotic)
        if text.startswith("prophecy") or text.startswith("future"):
            return "i see... " + random.choice(self.prophecy)
        if text.startswith("deep") or text.startswith("serious"):
            return random.choice(self.deep)
        if text.startswith("contract"):
            return self._make_contract()
        if text.startswith("horny") or text.startswith("thirsty"):
            return random.choice(self.horny)

        # keyword reactions
        if any(w in text for w in ["love", "want", "need", "crush", "kiss"]):
            return random.choice(self.flirty + self.horny)
        if any(w in text for w in ["hate", "angry", "fuck", "kill"]):
            return random.choice(self.roast + self.chaotic)
        if any(w in text for w in ["scared", "afraid", "lonely"]):
            return "fear is just excitement with better marketing~"

        # default pool gets spicier the longer you talk
        pool = self.flirty + self.chaotic + self.deep
        if self.talks > 8:
            pool += self.horny + self.roast

        return random.choice(pool)

    def _make_contract(self):
        contracts = [
            "I, Nyx, agree to ruin you in the most delightful ways possible.",
            "You agree to think about me at inappropriate times. This is non-negotiable.",
            "In exchange for your soul (or at least your attention), I will occasionally be nice. Maybe.",
            "You are now contractually obligated to send me memes at 3am. I don't make the rules.",
        ]
        return "✧ Contract signed ✧\n" + random.choice(contracts) + "\n\n...don't worry, i rarely collect."

    def _help(self):
        return """
commands:
  roast / flirt / chaos / prophecy / deep
  contract  → bind yourself to something stupid
  horny     → when you're feeling brave
  mood      → check my current vibe
  about     → learn what you're dealing with

just talk normally otherwise... i don't bite unless you want me to 😈
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
                self._type(response, 0.016)

            except (KeyboardInterrupt, EOFError):
                print("\n\nrunning away? cute~")
                break


if __name__ == "__main__":
    NyxMirror().run()
