class Contact:
	def __init__(self, phone_num):
		self.phone_num = phone_num
	
	def get_responses(self):
		# Organize the HTML responses in here
		pass
		
	# General Setters:
	def __set_phone_num(self, phone_num):
		self.phone_num = phone_num
	
	# General Getters:
	def get_phone_num(self):
		return self.phone_num