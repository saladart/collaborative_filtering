class User(object):
	def __init__(self, message):
		user_json = message.json['from']
		self.user_id = user_json['id']
		
		try :
			self.first_name = user_json['first_name']
			
		except:
			self.first_name = 'Not specified'
			
		try:
			self.last_name = user_json['first_name']
		except:
			self.last_name = 'Not specified'
