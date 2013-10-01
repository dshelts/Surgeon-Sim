#classes file 
#Andrew Shelton

#-----BALL CLASS----------------------------------------------------------
class Ball():
	def __init__(self, image, size=(50, 50), pos=(0, 0), bounds=(350, 350)):
		self.image = image

		self.x, self.y = pos
		self.width, self.height = size
		self.xBound, self.yBound = bounds

		self.vX = 0
		self.vY = 0

		self.state = 0 # 0 = Falling, 1 = Rising

	def move(self):
		self.x += self.vX
		self.y += self.vY

		self.update()

		return (self.x, self.y)

	def update(self):
		if self.y > self.yBound:
			self.y = self.yBound
			if self.state == 0:
				self.state = 1
			else:
				self.state = 0

			self.vY = -self.vY

		if self.x > self.xBound or self.x < 0:
			self.x = self.xBound

		self.vY += .05 # Gravity
		self.vX *= .9 # Friction

	def surrounds(self, pointer_pos):
		x, y = pointer_pos
		if x < (self.x + self.width) and x > (self.x) and y < (self.y + self.height) and y > (self.y):
			return True
#-----BALL CLASS END------------------------------------------------------


#-----HAND CLASS----------------------------------------------------------
class Hand():
	def __init__(self, image, size=(50, 50), pos=(0, 0), bounds=(350,350)):
		
		self.image = image
		self.hx, self.hy = pos
		self.width, self.height = size
		self.xBound, self.yBound = bounds

		self.vhx = 0
		self.vhx = 0

	def move(self):
		hx+=vhx
		hy+=vhy

		#self.update()

		return(self.x, self.y)

	def openToClose(self):
		
		if not self.ball.surrounds((scaledX, scaledY)):
			self.screen.blit(openHand_image, (scaledX, scaledY))
		else:
			self.screen.blit(closedHand_image, (scaledX, scaledY))

	#def update

	def surrounds(self, pointer_pos):
		x, y = pointer_pos
		if x < (self.hx + self.width) and x > (self.hx) and y < (self.hy + self.height) and y > (self.hy):
			return True

#-----HAND CLASS END------------------------------------------------------