import random

running = True
times = 0
too_big = "Too high!"
too_low = "Too low!"
tip = "Guess the number:"
number = random.randint(0, 100)

while running:
	times = times + 1
	guess = raw_input(tip)
	guess_int = int(guess)
	if number > guess_int:
		print too_low
	if number < guess_int:
		print too_big
	if number == guess_int:
		print "You got it for", times, "times!"
		running = False
