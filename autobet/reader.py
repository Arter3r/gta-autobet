import difflib

from autobet.constants import *
from autobet.util import log
from PIL import ImageOps, ImageEnhance
from datetime import datetime

import re
import time
import platform
import pytesseract
import pyautogui

if platform.system() == 'Windows':
	pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

class Reader:
	# Assume that if '+' is read, it's always followed by the currency symbol
	WINNING_REGEX = re.compile('^(?:\+.)?(\d+)$')
	OCR_MODEL_INPUT_DIMENSIONS = (int(PLACE_BET_SCREEN_ODDS_WIDTH * SCREEN_WIDTH), int(PLACE_BET_SCREEN_ODDS_HEIGHT * SCREEN_HEIGHT))

	def __init__(self, game_coord):
		self.game_coord = game_coord

	def generate_screenshot_name(self, fmt):
		return f'Screenshot on {time.ctime()}-{datetime.now().microsecond}.{fmt}'\
			.replace(' ','_').replace(':','-')

	def enhance_screenshot(self, img):
		# Invert then enhance contrast
		return ImageEnhance.Contrast(ImageOps.invert(img)).enhance(5)

	def screenshot_names(self):
		left = int(self.game_coord.width * PLACE_BET_SCREEN_NAMES_X) + self.game_coord.left
		top = int(self.game_coord.height * PLACE_BET_SCREEN_NAMES_Y) + self.game_coord.top
		width = int(self.game_coord.width * PLACE_BET_SCREEN_NAMES_WIDTH)
		height = int(self.game_coord.height * PLACE_BET_SCREEN_NAMES_HEIGHT*6)
		raw_imgs = [pyautogui.screenshot(region=(185, 297+121*i, 280, 30)) for i in range(6)]
		enhanced_imgs = [ImageOps.invert(raw_img.point(lambda p: p > 80 and p)) for raw_img in raw_imgs]
		bw_imgs = [enhanced_img.convert('L') for enhanced_img in enhanced_imgs]
		return bw_imgs

	def screenshot_colors(self):
		imgs = [pyautogui.screenshot(region=(185, 297+121*i, 1, 1)) for i in range(6)]
		return imgs

	def parse_winning(self, img):
		ocr_res = pytesseract.image_to_string(img, config='--psm 8 -c tessedit_char_whitelist=+0123456789')

		# Good OCR
		matched = self.WINNING_REGEX.match(ocr_res)
		if matched:
			return int(matched[1])

		# Bad OCR
		return 0

	def read_odds(self):
		racers = self.read_names()
		return [HORSEODDS[HORSENAMES.index(racers[i])] for i in range(len(racers))]

	def read_names(self):
		screenshots = self.screenshot_names()
		names = [difflib.get_close_matches(pytesseract.image_to_string(screenshot, lang='eng', config='--psm 7 --oem 3 --user-words "C:\\Program Files\\Tesseract-OCR\\tessdata\\eng.user-words"'), HORSENAMES, n=1)[0] for screenshot in screenshots]
		print(names)
		return names

	def read_colors(self):
		screenshots = self.screenshot_colors()
		colors = [screenshot.convert("RGB").getpixel((0, 0)) for screenshot in screenshots]
		return colors

	def screenshot_winning(self):
		left = int(self.game_coord.width * RESULTS_SCREEN_WINNING_X) + self.game_coord.left
		top = int(self.game_coord.height * RESULTS_SCREEN_WINNING_Y) + self.game_coord.top
		width = int(self.game_coord.width * RESULTS_SCREEN_WINNING_WIDTH)
		height = int(self.game_coord.height * RESULTS_SCREEN_WINNING_HEIGHT)
		raw_img = pyautogui.screenshot(region=(left, top, width, height))
		return self.enhance_screenshot(raw_img)

	def read_winning(self):
		screenshot = self.screenshot_winning()
		return self.parse_winning(screenshot)

	def screenshot_leaderboard(self):
		#x, y, width, height
		#Middle, left, right (first second third)
		sizes = [(712, 614, 492, 33), (151, 601, 454, 26), (1302, 601, 454, 26)]
		raw_imgs = [pyautogui.screenshot(region=box) for box in sizes]
		enhanced_imgs = [ImageOps.invert(raw_img.point(lambda p: p > 80 and 255)) for raw_img in raw_imgs]
		bw_imgs = [enhanced_img.convert('L') for enhanced_img in enhanced_imgs]
		return bw_imgs

	def read_leaderboard(self):
		screenshots = self.screenshot_leaderboard()
		names = [difflib.get_close_matches(pytesseract.image_to_string(screenshot, lang='eng', config='--psm 7 --oem 3 --user-words "C:\\Program Files\\Tesseract-OCR\\tessdata\\eng.user-words"'), HORSENAMES, n=1)[0] for screenshot in screenshots]
		print(names)
		return names