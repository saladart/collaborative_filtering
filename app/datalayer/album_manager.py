from pymongo import MongoClient
from datalayer.entities.album import Album


class AlbumManager(object):
	def __init__(self):
		client = MongoClient("mongodb+srv://admin:admin@albums-mspmg.mongodb.net/<dbname>?retryWrites=true&w=majority")	
		app_db = client.app_data
		
		self.albums_collection = app_db.Albums

	def get_random_album(self, user_albums):
		res = self.albums_collection.aggregate([
				{'$match': 
					{'_id': {'$nin': user_albums}}
				},
				{'$sample': 
					{'size': 1}
				}
			])
		album = Album(list(res)[0])
		return album
