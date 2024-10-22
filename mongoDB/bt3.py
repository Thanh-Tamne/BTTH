#bai tap 6
from pymongo import MongoClient
from datetime import datetime

# ket noi den moongodb
client = MongoClient('mongodb://localhost:27017/')
client.drop_database = ('file1')
db = client['file1']# chon csdl
collections = db.list_collection_names()
for collection_name in collections:
    db.drop_collection(collection_name)
    print(f"Collection {collection_name} dropped.")
# tao cac collections
file_collection = db['file']

# tao cac collections
file_data = [
    { 'file_id': 1, 'name': "Report.pdf", 'size': 2048, 'owner': "Nguyen Van A", 'created_at': datetime(2024,1,10), 'shared': False },
    { 'file_id': 2, 'name': "Presentation.pptx", 'size': 5120, 'owner': "Tran Thi B", 'created_at': datetime(2024,1,15), 'shared': True },
    { 'file_id': 3, 'name': "Image.png", 'size': 1024, 'owner': "Le Van C", 'created_at': datetime(2024,1,20), 'shared': False },
    { 'file_id': 4, 'name': "Spreadsheet.xlsx", 'size': 3072, 'owner': "Pham Van D", 'created_at': datetime(2024,1,25), 'shared': True },
    { 'file_id': 5, 'name': "Notes.txt", 'size': 512, 'owner': "Nguyen Thi E", 'created_at': datetime(2024,1,30), 'shared': False }
]
file_collection.insert_many(file_data) # them du lieu nguoi dung

# Xem tất cả tệp trong bộ sưu tập 'files
print("\nxem tat ca trong bo suu tam file ")
for file in file_collection.find():
    print()

# Tìm tệp có kích thước lớn hơn 2000KB
print("\ntep co kich thuoc lon hon 2000KB")
file_kichthuoc = file_collection.find({'size' : {'$gte' : 2000}})
for kichthuoc in file_kichthuoc :
    print(kichthuoc)

#Đếm tổng số tệp
print("\nDem tong so tep", file_collection.count_documents({}))

#Tìm tất cả tệp được chia sẻ
print("\ntat ca tep duoc chia se")
file_all = file_collection.find({'shared': True})
for all in file_all:
    print(all)

#Thống kê số lượng tệp theo chủ sở hữu
# db.files.aggregate([
#     { $group: { _id: "$owner", count: { $sum: 1 } } }
# ])
print('\nThong ke so luong tep theo chu so huu')
file_tep = file_collection.aggregate([{ '$group' : { '_id' : "$owner" , 'count': { '$sum' : 1 } }}])
for tep in file_tep :
    print(tep)

#Cập nhật và xóa thông tin tệp
#Cập nhật trạng thái chia sẻ của tệp với file_id = 1 thành true
print('\ncap nhat trang thai chia se cua tep voi file_id = 1 thanh True ')
file_capnhat = file_collection.update_one({'file_id': 1 }, { '$set': { 'shared': True }})
#Xóa tệp với file_id = 3
print("\n da xoa binh luan ")
file_xoa = file_collection.delete_one({'file_id': 3 })
#Kiểm tra lại tất cả tệp trong bộ sưu tập
print('\nKiem tra lai tat ca tep trong bo suu tap ')
for file in file_collection.find():
    print(file)

#Câu hỏi 1: Tìm tất cả tệp của người dùng có tên là "Nguyen Van A".
# db.files.find({ owner: "Nguyen Van A" })
print("\nNguoi dung co ten 'Nguyen Van A'")
file_ten = file_collection.find({"owner": 'Nguyen Van A' })
for ten in file_ten :
    print(ten)
#Câu hỏi 2: Tìm tệp lớn nhất trong bộ sưu tập.
# db.files.find().sort({ size: -1 }).limit(1)
print('\n Tep lon nhat trong bo suu tap')
file_lonnhat = file_collection.find().sort({'size' : -1}).limit(1)
for lonnhat in file_lonnhat:
    print(lonnhat)
# // Câu hỏi 3: Tìm số lượng tệp có kích thước nhỏ hơn 1000KB.
# db.files.countDocuments({ size: { $lt: 1000 } })
print('\nSo luong tep co kich thuoc nho hon 1000KB')
file_soluong = file_collection.count_documents({'size' :{'$lt':1000}})
print(file_soluong)
# // Câu hỏi 4: Tìm tất cả tệp được tạo trong tháng 1 năm 2024.
# db.files.find({
#     created_at: {
#         $gte: new Date("2024-01-01"),
#         $lt: new Date("2024-02-01")
#     }
# })
print("\nTất cả tệp được tạo trong tháng 1 năm 2024")
files_thang1 = file_collection.find({
    'created_at': {
        '$gte': datetime(2024, 1, 1),
        '$lt': datetime(2024, 2, 1)
    }
})
for file in files_thang1:
    print(file)
# // Câu hỏi 5: Cập nhật tên tệp với `file_id` là 4 thành "New Spreadsheet.xlsx".
# db.files.updateOne({ file_id: 4 }, { $set: { name: "New Spreadsheet.xlsx" } })
print('\nCập nhật tên tệp với file_id = 4 thành "New Spreadsheet.xlsx"')
file_collection.update_one({'file_id': 4}, { '$set': { 'name': "New Spreadsheet.xlsx" }})

# // Câu hỏi 6: Xóa tất cả tệp có kích thước nhỏ hơn 1000KB.
# db.files.deleteMany({ size: { $lt: 1000 } })
print('\nXóa tất cả tệp có kích thước nhỏ hơn 1000KB')
file_collection.delete_many({'size': {'$lt': 1000}})
