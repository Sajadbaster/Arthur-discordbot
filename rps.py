import random

checkWining=[("rock", "scissors"),("paper", "rock"),("scissors", "paper")]
shortcut={
	"r":"rock",
	"p":"paper",
	"s":"scissors"
}

class rps:
	def __init__(self, userInput):
		self.userInput=userInput
		
	def function(self):
		botInput=random.choice(["rock", "paper", "scissors"])
		
		if self.userInput.lower() in shortcut:
			self.userInput=shortcut[self.userInput.lower()]
		
		
		if self.userInput.lower() not in ["rock", "paper", "scissors"]:
			return None
			
		
		if self.userInput.lower()==botInput:
			return "it's a draw",botInput, self.userInput
			
		elif (self.userInput.lower(), botInput) in checkWining:
			return "You won >:(", botInput, self.userInput
			
		else:
			return "I won loser >:)", botInput, self.userInput