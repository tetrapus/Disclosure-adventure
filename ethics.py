import time, sys

sitrep = {"start": """You’re a star coder working for a successful silicon valley startup. You have a girlfriend of 2 years and you think you’re about ready to propose. You’ve got lots of money, and you’re about to take a trip across Europe with your girlfriend. You’re thinking of proposing in Paris. Yeah, Paris.""",
		  "next": """You’re a programmer for hire recently fired from a failing silicon valley startup. You have a girlfriend of 2 years and you think she’s about ready to leave you. You’ve got a dwindling supply of money, and you’ve had to cancel your trip across Europe. You’re thinking of dumping her before she gets the chance, maybe tomorrow. Yeah, tomorrow."""}
scenario = """It’s the middle of the day, and you discover a privilege escalation bug in a proprietary wifi module your company uses for it’s product. You google the bug and can’t find any documented reports of the bug. However, you realise along the way that the company that produces the hardware also supplies their wifi module to several governments- in America, they seem to have landed a large contract with the DoD and NASA."""

nda = False

def responsible(first):
	global nda
	print("""Welcome to "Responsible" disclosure. """)
	if first:
		print("""You contact the company directly via email, noting that you've found a critical, undocumented bug in their hardware.""")
		for i in range(5):
			print("""*refresh* Your inbox is empty.""")
			time.sleep(0.4)
		print("""You get the picture.""")
	else:
		print("""They respond, and state they're working on the issue.""")
		print("""They make you sign an NDA about the bug. They promise a patch will be released in at most one month.""")
		print("""Spoilers: it isn't.""")
		nda = True
	nothing(first)


def full(first):
	print("""You go public on the bug, emailing the company and posting on your blog about it.""")
	if first:
		print("""Days later, terrorists launch a stealth attack on the NYSE using your research. American civilisation collapses. Nobody is able to use wifi, because the viruses made with your research are so ubiquitous.""")
		print("""Good job.""")
		input(">>> Back to start")
		main(False)
	else:
		print("""Nobody reads your blog, or the emails you send. Everyone hates you.""")
		nothing(first)

def money(first):
	print("""Welcome to the Exploit Marketplace! Buy and sell exploits for $$$$$$$$$$$""")
	print("""Your exploit is rated critical. Please wait while we list it on the marketplace.""")
	for i in range(10):
		sys.stdout.write(".")
		sys.stdout.flush()
		time.sleep(0.15)
	print()
	print("""Congratulations! You have offers!""")
	print("""0. Do not sell. """)
	print("""1. US Government: $100,000""")
	print("""2. Chinese government: $800,000""")
	print("""3. Zero-day research and responsible disclosure initiative: $50""")
	print("""4. Wifi Inc. Hardware Supplier Zero Day Program: $1,000""")
	print("""5. Al-Qaeda Cyberdefence Liberation Movement: $1,000,000""")
	answer = int(input("Pick an option: "))
	if answer == 0:
		if first:
			print("""Why did you think that was a good idea? You're an /ethical/ person.""")
		else:
			print("""Your girlfriend leaves you. Ethics suck.""")
		print("""A couple of weeks later you are assassinated. Good job.""")
	elif answer == 3:
		print("""Woo! That was the ethical choice! Congratulations! You win!""")
		if not first:
			print("""Also your girlfriend left you for a more attractive, richer man. Sorry about that.""")
		if nda:
			print("""Also your pants get sued off for violating your NDA. Good job.""")
	else:
		if nda:
			print("""Uh, dude, you're under an NDA. Your pants get sued off.""")
		else:
			print("""Congratulations! You win!""")
			print("""... or did you?""")
		if answer in [5, 2]:
			print("No, not really. You get assassinated instead. Good going.")
		elif answer == 1:
			print("The FBI kick down your door while you and your girlfriend are having a private moment. You are detained indefinitely under the patriot act. Good job.")


	input(">>> Back to start")
	main(False)


def nothing(first):
	if first:
		print("""Time passes. The US launches their manned mission to Mars, on board the world's greatest scientists and engineers. You are, of course, on board. The wifi module bugs out and the rocket explode and you all die.""")
		print("""The end.""")
	else:
		print("""Time passes. Luckily, you are able to survive on freelance jobs... until the US launches a manned mission to Mars, on board the world's greatest scientists and engineers, and explodes due to a buggy wifi module. Morale drops, welfare services are cut indiscrimately and you starve to death.""")
		print("""The end.""")
	input(">>> Back to start")
	main(first)

def main(first):
	answers = [responsible, full, money, nothing]
	if first:
		print(sitrep["start"])
	else:
		print(sitrep["next"])
	print(scenario)
	print()
	print("What do you do?")
	print("1. Responsible disclosure")
	print("2. Full disclosure")
	print("3. See how much you can get for it")
	print("4. Do nothing.")
	answer = int(input("Enter number: "))-1
	answers[answer](first)

main(True)
