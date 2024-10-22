#bai tap 5
from pymongo import MongoClient
from datetime import datetime

# ket noi den moongodb
client = MongoClient('mongodb://localhost:27017/')

client.drop_database = ('data')
db = client['data']# chon csdl
client.drop_database= ('data')
collections = db.list_collection_names()
for collection_name in collections:
    db.drop_collection(collection_name)
    print(f"Collection {collection_name} dropped.")
# tao cac collections
users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']

# tao ca collections
users_data = [
    { 'user_id': 1, 'name': "Nguyen Van A", 'email': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'email': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'email': "c@gmail.com", 'age': 22 }
]
users_collection.insert_many(users_data)  # Thêm dữ liệu người dùng
# Tạo bộ sưu tập bài đăng
posts_data = [
    { 'post_id': 1, 'user_id': 1,'content': "Hôm nay thật đẹp trời!", 'created_at': datetime(2024,10,1) },
    { 'post_id': 2, 'user_id': 2, 'content': "Mình vừa xem một bộ phim hay!", 'created_at': datetime(2024,10,2) },
    { 'post_id': 3, 'user_id': 1, 'content': "Chúc mọi người một ngày tốt lành!", 'created_at': datetime(2024,10,3) }
]
posts_collection.insert_many(posts_data)  # Thêm dữ liệu người dùng
# Tạo bộ sưu tập bình luận
comments_data = [
    { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024,10,1) },
    { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024,10,2) },
    { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024,10,3) }
]
comments_collection.insert_many(users_data)  # Thêm dữ liệu người dùng

# xem tat ca nguoi dung
print("tat ca nguoi dung ")
for user in users_collection.find():
    print(user)
# Xem tất cả bài đăng của người dùng với user_id = 1
print("\n xem tat ca bai dang cua nguoi dun 'user = 1':")
user_baidang = users_collection.find({'user_id': 1 })
for baidang in user_baidang:
    print(baidang)
#Xem tất cả bình luận cho bài đăng với post_id = 1
print("\n xem tat ca binh luan cua bai 'post_id = 1 ' ")
posts_baidang = posts_collection.find({'posts_id': 1 })
for baidang in posts_baidang:
    print(baidang)
# Truy vấn người dùng có độ tuổi trên 25
print("\n nguoi dung co do tuoi tren 25")
user_tuoi = users_collection.find({'age': {"$gt": 25}})
for tuoi in user_tuoi:
    print(tuoi)
# Truy vấn tất cả bài đăng được tạo trong tháng 10

print("\n cac bai dang trong thang 10")
posts_baidang = posts_collection.find({ 'created_at': { '$gte': datetime(2024,10,1), '$lt': datetime(2024,11,1) } })
for baidang in posts_baidang:
    print(baidang)
# Bước 6: Cập Nhật và Xóa Dữ Liệu
# // Cập nhật nội dung bài đăng của người dùng với post_id = 1
print("\n cap nhat noi dung bai dang cua nguoi dung post_id = 1 ")
posts_capnhat = posts_collection.update_one({ 'post_id': 1 }, { '$set': { 'content': "Hôm nay thời tiết thật đẹp!" } })

# // Xóa bình luận với comment_id = 2
# db.comments.deleteOne({ comment_id: 2 })
print("\n da xoa binh luan ")
comments_xoa = comments_collection.delete_one({'comment_id': 2 })

print("tat ca nguoi dung")
for user in users_collection.find():
    print(user)
print("tat ca nguoi dung")
for post in posts_collection.find():
    print(post)
print("tat ca nguoi dung")
for comment in comments_collection.find():
    print(comment)
# dong ket noi
client.close()
