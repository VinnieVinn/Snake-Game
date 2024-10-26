import pygame

#button class
class Button():
	def __init__(self, x, y, image, scale):
		self.width = image.get_width()
		self.height = image.get_height()
		self.x = x
		self.y = y
		self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False


	def get_width(self):
		return self.width
	
	def get_height(self):
		return self.height
	
	def set_x(self, value):
		self.x = value
		self.rect.topleft = (self.x, self.y) 

	def set_y(self, value):
		self.y = value
		self.rect.topleft = (self.x, self.y) 


	def flip_img_x(self):
		self.image = pygame.transform.flip(self.image, True, False).convert_alpha()
		self.rect = self.image.get_rect()

	def draw(self, surface):
		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))


	def pressed(self):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		return action