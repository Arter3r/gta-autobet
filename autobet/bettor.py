class Bettor:
	MIN_BET_AMOUNT = 100
	SMALL_BET_AMOUNT = 1000
	MEDIUM_BET_AMOUNT = 5000
	MAX_BET_AMOUNT = 10000

	def expected_return(odds):
		win_percentages = [1/(1+odd) for odd in odds]
		totalOdds = sum(win_percentages)
		adjusted_win_percentages = [odd/totalOdds for odd in win_percentages]
		someAmount = 1
		expected_value = [-1 + (odds[i]+1)*adjusted_win_percentages[i] for i in range(6)]
		print(win_percentages)
		print(adjusted_win_percentages)
		print(totalOdds)
		print(expected_value)
		return expected_value

	def bet(odds, names):
		EXPECTED_RETURNS = Bettor.expected_return(odds)
		max_expected_value = max(EXPECTED_RETURNS)
		best_horse = odds.index(min(odds))
		if max_expected_value <= 0:
			return (best_horse, Bettor.SMALL_BET_AMOUNT)
		elif max_expected_value < 0.25:
			return (best_horse, Bettor.MEDIUM_BET_AMOUNT)
		else:
			return (best_horse, Bettor.MAX_BET_AMOUNT)
