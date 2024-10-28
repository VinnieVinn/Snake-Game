import pygame

#Text class
class Text():
	def __init__(self, x, y, prompt, font, fontSize, antialias, color, bgColor):
		self.fontSize = fontSize
		self.textFont = font
		self.font = pygame.font.Font(font, fontSize)
		self.x = x
		self.y = y
		self.antialias = antialias
		self.color = color
		self.bgColor = bgColor
		self.prompt = prompt
		self.text = self.font.render(prompt, antialias, color, bgColor)
		self.width, self.height = self.font.size(prompt)
		
		self.rect = self.text.get_rect()
		self.rect.topleft = (x, y)


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

	def set_prompt(self, value):
		self.prompt = value
		self.text = self.font.render(self.prompt, self.antialias, self.color, self.bgColor)

	def set_font_size(self, value):
		self.font = pygame.font.Font(self.textFont, int(value))
		self.text = self.font.render(self.prompt, self.antialias, self.color, self.bgColor)
		self.width, self.height = self.font.size(self.prompt)
		self.rect = self.text.get_rect()

	

	def draw(self, surface):
		#draw button on screen
		surface.blit(self.text, (self.rect.x, self.rect.y))