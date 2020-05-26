from autobet.constants import *
from autobet.util import get_screen_size

import pyautogui
import bisect
import os
import random
import time

class Clicker:
	MOUSE_MOVEMENT_MODE = pyautogui.easeOutQuad

	def get_random_mouse_duration():
		return random.uniform(MOUSE_MOVEMENT_MIN_DURATION_SECONDS,
			MOUSE_MOVEMENT_MAX_DURATION_SECONDS)

	def get_random_delay():
		return random.uniform(MIN_ACTION_DELAY_SECONDS, MAX_ACTION_DELAY_SECONDS)

	def get_random_pixel():
		x, y = get_screen_size()
		rand_x = int(random.random() * x)
		rand_y = int(random.random() * y)
		return rand_x, rand_y

	def get_absolute_path(relative_path):
		dirname = os.path.dirname(__file__)
		return os.path.join(dirname, relative_path)

	def click(x, y, times=1, frac=True):
		if frac:
			x = int(get_screen_size()[0] * x)
			y = int(get_screen_size()[1] * y)
		pyautogui.moveTo(x, y, Clicker.get_random_mouse_duration(), Clicker.MOUSE_MOVEMENT_MODE)
		time.sleep(Clicker.get_random_delay())
		for _ in range(times):
			pyautogui.click()
			time.sleep(Clicker.get_random_delay())
		pyautogui.moveTo(*Clicker.get_random_pixel(), Clicker.get_random_mouse_duration(), Clicker.MOUSE_MOVEMENT_MODE)
		time.sleep(Clicker.get_random_delay())

	def click_img(img_path):
		Clicker.click(*pyautogui.locateCenterOnScreen(img_path, confidence=0.8))

	def click_place_bet_start_screen():
		Clicker.click(START_SCREEN_PLACE_BET_X, START_SCREEN_PLACE_BET_Y)

	def click_bet_again():
		Clicker.click(RESULTS_SCREEN_BET_AGAIN_X, RESULTS_SCREEN_BET_AGAIN_Y)

	def place_bet(position, amount):
		# Click corresponding horse
		Clicker.click(PLACE_BET_SCREEN_BETS_X, PLACE_BET_SCREEN_BETS_YS[position])
		# Click bet amount
		num_clicks = bisect.bisect(BET_AMOUNTS, amount)
		Clicker.click(PLACE_BET_SCREEN_INCREMENT_X, PLACE_BET_SCREEN_INCREMENT_Y, times=num_clicks)
		# Click place bet
		Clicker.click(PLACE_BET_SCREEN_PLACE_BET_X, PLACE_BET_SCREEN_PLACE_BET_Y)


