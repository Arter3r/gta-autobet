GAME_EXECUTABLE = 'GTA5.exe'
TESSERACT_PATH = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
ASPECT_RATIO = 16/9
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
HORSE_RACE_DURATION_SECONDS = 36
BET_AMOUNTS = [100,200,300,400,500,600,700,800,900,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500,9000,9500,10000]
USERNAME = "USERNAME"

SAFE_CLICK_X_Y = (0.1, 0.1)
MIN_ACTION_DELAY_SECONDS = 0.03
MAX_ACTION_DELAY_SECONDS = 0.05

START_SCREEN_TOP_LEFT_PIXEL_RGB = (20, 0, 46)
START_SCREEN_PLACE_BET_X = 947/1280
START_SCREEN_PLACE_BET_Y = 603/720

PLACE_BET_SCREEN_TOP_LEFT_PIXEL_RGB = (219, 19, 0)
NUM_BETS = 6
PLACE_BET_SCREEN_BETS_X = 214/1280
PLACE_BET_SCREEN_BETS_YS = list(228/720 + i * 80/720 for i in range(NUM_BETS))
PLACE_BET_SCREEN_INCREMENT_X = 1011/1280
PLACE_BET_SCREEN_INCREMENT_Y = 343/720
PLACE_BET_SCREEN_PLACE_BET_X = 854/1280
PLACE_BET_SCREEN_PLACE_BET_Y = 525/720
PLACE_BET_SCREEN_ODDS_X = 119/1280
PLACE_BET_SCREEN_ODDS_WIDTH = 226/1280
PLACE_BET_SCREEN_ODDS_HEIGHT = 32/720
PLACE_BET_SCREEN_ODDS_YS = list(231/720 + i * 80/720 for i in range(NUM_BETS))
PLACE_BET_SCREEN_NAMES_X = 185/1920
PLACE_BET_SCREEN_NAMES_Y = 297/1080
PLACE_BET_SCREEN_NAMES_WIDTH = 532/1920
PLACE_BET_SCREEN_NAMES_HEIGHT = 121/1080

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
MOUSE_MOVEMENT_MIN_DURATION_SECONDS = 0.2
MOUSE_MOVEMENT_MAX_DURATION_SECONDS = 0.3
MOUSE_X_RADIUS = 25/1280
MOUSE_Y_RADIUS = 8/720

HORSENAMES = [name.upper() for name in ['A Tethered End', 'Bad Egg', 'Banana Hammock', 'Better than Nothing', 'Black Rock Rooster', 'Bleet Me Baby', 'Blue Dream', 'Borrowed Sorrow', 'Bouncy Blessed', 'Cancelled Check', "Can't Be Wronger", 'Clapback Charlie', 'Constant Brag', 'Country Stuck', 'Crackers and Please', 'Creepy Dentist', 'Crock Janley', "Dancin' Pole", "Dancin' Shoes", 'Darling Ricki', 'Dead Fam', 'Dead Heat Hattie', 'Dexie Runner', 'Divorced Doctor', 'Doozy Floozy', 'Downtown Renown', 'Dr. Deez Reins', 'Dream Shatterer', 'Drone Warning', 'Drunken Brandee', 'Durban Poison', 'Feed the Trolls', 'Fire Hazards', 'Flipped Wig', 'Friendly Fire', 'Getting Haughty', 'Ghost Dank', 'Glass or Tina', 'Hard Time Done', 'Hell for Weather', "Hennigan's Steed", 'Hippie Crack', 'Hot & Bothered', 'Invade Grenade', "It's a Trap", 'Kraff Running', 'Lead Is out', 'Lit as Truck', 'Lonely Stepbrother', 'Los Santos Savior', "Lover's Speed", 'Measles Smeezles', 'Micro Aggression', 'Minimum Wager', 'Miss Mary John', 'Miss Triggered', 'Mister Redacted', 'Mister Scissors', 'Money to Burn', 'Moon Rocks', 'Mr. Worthwhile', 'Mud Dragon', 'Night-time Mare', 'Northern Lights', 'Nuns Orders', "Ol' Skag", 'Old Ill Will', 'Omens and Ice', 'Pedestrian', 'Pretty as a Pistol', 'Questionable Dignity', 'Reach Around Town', 'Robocall', "Salt 'n' Sauce", 'Salty and Woke', 'Scrawny Nag', 'Sir Scrambled', 'Sizzurp', 'Snatched Your Mama', 'Social Media Warrior', 'Square to Go', 'Study Buddy', 'Stupid Money', 'Sumptin Saucy', 'Sweet Releaf', 'Tax the Poor', 'Tea Ache Sea', 'Tenpenny', 'There She Blows', 'Throwing Shady', 'Thunder Skunk', 'Total Belter', 'Turnt Mood', 'Uptown Rider', 'Wage of Consent', 'Wee Scunner', 'Worth a Kingdom', "Yay Yo Let's Go", 'Yellow Sunshine']]
HORSEODDS = [27, 29, 16, 15, 18, 7, 2, 12, 5, 25, 28, 10, 3, 21, 3, 7, 8, 9, 5, 22, 26, 17, 6, 7, 13, 4, 5, 1, 8, 14, 20, 30, 24, 12, 9, 3, 10, 23, 18, 2, 4, 23, 2, 13, 1, 14, 3, 1, 3, 5, 2, 15, 8, 26, 22, 19, 19, 7, 30, 4, 2, 5, 16, 15, 9, 28, 29, 3, 25, 4, 12, 6, 4, 1, 17, 30, 26, 13, 1, 27, 6, 15, 30, 1, 4, 13, 24, 10, 2, 21, 20, 1, 12, 14, 21, 8, 2, 3, 5]
