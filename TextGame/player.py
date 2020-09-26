import sys
import os
import discord
import asyncio

client = discord.Client()

class Player:
    def __init__(self):
        #self.name = client.get_user(0);
        self.maxhp = 200;
        self.starthp = 100;
        self.maxstam = 200;
        self.startstam = 100;
        self.inventory = 20;
        self.hr = 1;
        self.sharpn = 1;
        self.attack = 70;
        self.stats = "HR = 1" \
                     "Attack = 70" \
                     "Defense = 20" \
                     "Affinity = 0%" \
                     "Sharpness = Yellow" \
                     "Element = none" \
                     "Money = 1500z" \
                     "Fire Resistance = -3" \
                     "Water Resistance = 3" \
                     "Ice Resistance = 3" \
                     "Dragon = -10" \
                     "Thunder Resistance = -5" \


