from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:admin@albums-mspmg.mongodb.net/<dbname>?retryWrites=true&w=majority")	
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
	