#bai tap 4
# import
from pymongo import MongoClient
from datetime import datetime

# buoi1 ket noi den mongodb
client = MongoClient('mongodb://localhost:27017/')
client.drop_database('tiktokABC')
db = client['tiktokABC']# chon csdl tiktok

#buoc 2 : tao cac collections
users_collection = db['users']

videos_collection = db['videos']

#buoc 3 them du lieu ng dung
users_data = [
    { 'user_id': 1, 'username': 'user1', 'full_name': 'Nguyen Van A', 'followers': 1500, 'following': 200 },
    { 'user_id': 2, 'username': 'user2', 'full_name': 'Tran Thi B', 'followers': 2000, 'following': 300 },
    { 'user_id': 3, 'username': 'user3', 'full_name': 'Le Van C', 'followers': 500, 'following': 100 }
]
users_collection.insert_many(users_data)  # Thêm dữ liệu người dùng

videos_data = [
    { 'video_id': 1, 'user_id': 1, 'title': 'Video 1', 'views': 10000, 'likes': 500, 'created_at': datetime(2024, 1, 1) },
    { 'video_id': 2, 'user_id': 2, 'title': 'Video 2', 'views': 20000, 'likes': 1500, 'created_at': datetime(2024, 1, 5) },
    { 'video_id': 3, 'user_id': 3, 'title': 'Video 3', 'views': 5000, 'likes': 200, 'created_at': datetime(2024, 1, 10) }
]
videos_collection.insert_many(videos_data)  # Thêm dữ liệu video

# buoc 5 truy van du lieu
# xem at ca nguoi dung
print("tat ca nguoi dung")
for user in users_collection.find():
    print(user)

# tim vd co luot xem nhieu nhat
most_viewed_video = videos_collection.find().sort('views', -1).limit(1)
print("\nVideo co nhieu luot xem nhat:")
for video in most_viewed_video:
    print(video)
# tim tat ca ideo cua nguoi dun co username la user1
print("\n tat ca video cau nguoi dung 'user1':")
user_videos = videos_collection.find({'user_id': 1})
for video in user_videos:
    print(video)

client.close()

