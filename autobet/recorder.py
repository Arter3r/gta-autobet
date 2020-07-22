import csv
from autobet.constants import USERNAME
import pymongo
import time

class Recorder():
    def __init__(self):
        self.username = USERNAME
        self.horses = ["N/A"]
        self.colors = ["N/A"]
        self.odds = ["N/A"]
        self.betID = "N/A"
        self.bet = "N/A"
        self.leaderboard = ["N/A"]
        self.winnings = "N/A"

        self.client = pymongo.MongoClient(
            "[ASK FOR LINK OR COMMENT OUT RECORDER FUNCTIONS]")
        self.db = self.client.RaceData

    def save(self):
        entryData = {
            "Racers": self.horses,
            "Colors": self.colors,
            "Odds": self.odds,
            "Nominee": self.betID,
            "Bet Amount": self.bet,
            "Leaderboard": self.leaderboard,
            "Winnings": self.winnings,
            "Time": time.localtime(time.time()),
            "Published by": self.username
                     }
        self.db.data.insert_one(entryData)