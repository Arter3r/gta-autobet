from pynput import keyboard

GAME_EXECUTABLE = 'GTA5.exe'
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ASPECT_RATIO = 16/9
START_STOP_KEY = keyboard.Key.f8
HORSE_RACE_DURATION_SECONDS = 36
BET_AMOUNTS = [100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]

SAFE_CLICK_X_Y = (0.1, 0.1)
MOUSE_MOVEMENT_MIN_DURATION_SECONDS = 0.2
MOUSE_MOVEMENT_MAX_DURATION_SECONDS = 0.3
MIN_ACTION_DELAY_SECONDS = 0.08
MAX_ACTION_DELAY_SECONDS = 0.1
# Mouse moves to within specified radius of target
MOUSE_X_RADIUS = 25/1280
MOUSE_Y_RADIUS = 8/720

START_SCREEN_TOP_LEFT_PIXEL_RGB = (20, 0, 46)
START_SCREEN_PLACE_BET_X = 947/1280
START_SCREEN_PLACE_BET_Y = 603/720

NUM_BETS = 6
PLACE_BET_SCREEN_BETS_X = 214/1280
PLACE_BET_SCREEN_BETS_YS = list(228/720 + i * 80/720 for i in range(NUM_BETS))
PLACE_BET_SCREEN_INCREMENT_X = 1011/1280
PLACE_BET_SCREEN_INCREMENT_Y = 343/720
PLACE_BET_SCREEN_PLACE_BET_X = 854/1280
PLACE_BET_SCREEN_PLACE_BET_Y = 525/720
PLACE_BET_SCREEN_ODDS_X = 119/1280
PLACE_BET_SCREEN_ODDS_WIDTH = 39/1280
PLACE_BET_SCREEN_ODDS_HEIGHT = 30/720
PLACE_BET_SCREEN_ODDS_YS = list(231/720 + i * 80/720 for i in range(NUM_BETS))

RESULTS_SCREEN_TOP_LEFT_PIXEL_RGB = (219, 19, 0)
RESULTS_SCREEN_BET_AGAIN_X = 636/1280
RESULTS_SCREEN_BET_AGAIN_Y = 659/720
RESULTS_SCREEN_WINNING_X = 564/1280
RESULTS_SCREEN_WINNING_Y = 535/720
RESULTS_SCREEN_WINNING_WIDTH = 237/1280
RESULTS_SCREEN_WINNING_HEIGHT = 38/720

# Unused for now
PLACE_BET_SCREEN_BETS_TOP_LEFT_X = 34/1280
PLACE_BET_SCREEN_BETS_TOP_LEFT_Y = 183/720
PLACE_BET_SCREEN_BETS_WIDTH = 381/1280
PLACE_BET_SCREEN_BETS_HEIGHT = 483/720
