class Album(object):
	def __init__(self, album_data):
		self.album_id = album_data['_id']
		self.artist = album_data['artist']
		self.album_name = album_data['album']
		self.year = album_data['year']

	def __str__(self):
		return '*' + self.album_name + '*' + \
				'\nby ' + self.artist + \
			 	'\nyear: ' + str(self.year)