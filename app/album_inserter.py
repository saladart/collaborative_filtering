from pymongo import MongoClient
import os

client = MongoClient(os.getenv('MONGOKEY'))	
app_db = client.app_data

# collections
albums_collection = app_db.Albums

albums = open("./albums.txt", "r")
for line in albums.readlines():
	line = line.replace("•", " ")
	artist, album_name, year = line.split(" - ")
	albums_collection.insert_one({
			"artist": artist.strip(),
			"album": album_name.strip(),
			"year": int(year)
		})
	