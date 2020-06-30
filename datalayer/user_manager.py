from pymongo import MongoClient

class UserManager(object):
	def __init__(self):
		client = MongoClient("mongodb+srv://admin:admin@albums-mspmg.mongodb.net/<dbname>?retryWrites=true&w=majority")	
		app_db = client.app_data
		
		self.user_collection = app_db.Users

	def create_user(self, user):
		self.user_collection.insert_one({
				'user_id': user.user_id,
				'first_name': user.first_name,
				'last_name': user.last_name,
				'albums_recommended': []
			})

	def check_user_exists(self, user):
		res = self.user_collection.find_one({
				'user_id': user.user_id,
			})
		return res is not None

	def get_user_albums(self, user):
		res = self.user_collection.find_one({
				'user_id': user.user_id
			})
		albums = res['albums_recommended']
		return albums

	def clear_history(self, user):
		self.user_collection.find_and_modify(
				query={'user_id': user.user_id},
				update={"$set": {'albums_recommended': []}}
			)

	def add_album(self, user, album, user_albums):
		new_albums = user_albums + [album.album_id]
		user = self.user_collection.find_and_modify(
				query={'user_id': user.user_id},
				update={"$set": {'albums_recommended': new_albums}}
			)
