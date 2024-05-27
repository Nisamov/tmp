import math
import random

def cu(minValue, maxValue):
	temp = None
	def consecutivelyUnique() :
		nonlocal temp
		randomValue = math.floor((random.random() * (maxValue - minValue + 1)) + minValue)
		temp = (consecutivelyUnique() if (randomValue == temp and minValue != maxValue) else randomValue)
		return temp
	return consecutivelyUnique
