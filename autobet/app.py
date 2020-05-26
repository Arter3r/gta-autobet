from pynput import keyboard
from autobet.clicker import Clicker
from autobet.reader import Reader
from autobet.bettor import Bettor
from autobet.constants import START_STOP_KEY, HORSE_RACE_DURATION_SECONDS
from autobet.util import *

import time

class App:
	def on_press(self, key):
		if key == START_STOP_KEY:
			return False

	def __init__(self):
		self.started = False
		self.odds = []
		self.winnings = []

	def start(self):
		if self.started:
			log("Already started.")
			return self.stop()
		if not check_game_running():
			log("Game is not running.")
			return self.stop()
		if not check_aspect_ratio():
			log("Wrong aspect ratio.")
			return self.stop()
		if not check_betting_screen():
			log("Not on betting screen.")
			return self.stop()
		log('Started.')
		self.started = True
		with keyboard.Listener(on_press=self.on_press) as listener:
			self.main_loop()
			if not listener.running:
				self.stop()

	def stop(self):
		self.started = False
		log('Stopped.')
		self.run()

	def run(self):
		with keyboard.Listener(on_press=self.on_press) as listener:
			listener.join()
		self.start()

	def main_loop(self):
		Clicker.click_place_bet_start_screen()
		odds = Reader.read_odds()
		self.odds.append(odds)
		bet_position, bet_amount = Bettor.bet(odds)
		Clicker.place_bet(bet_position, bet_amount)
		log(f'Placing bet on {bet_position} for {bet_amount}')
		time.sleep(HORSE_RACE_DURATION_SECONDS)
		winning = Reader.read_winning()
		net_won = winning - bet_amount
		log(f'Made ${net_won}')
		self.winnings.append(net_won)
		Clicker.click_bet_again()