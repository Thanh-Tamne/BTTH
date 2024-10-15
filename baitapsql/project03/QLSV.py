from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("600x800")

# Kết nối tới db
conn = sqlite3.connect('QLSV.db')
c = conn.cursor()

# # Tạo bảng nếu chưa tồn tại
# c.execute('''
#     CREATE TABLE IF NOT EXISTS QLSV (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name TEXT,
#         last_name TEXT,
#         idclass TEXT,
#         year TEXT,
#         AVG INTEGER
#     )
# ''')
# conn.commit()

def them():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('QLSV.db')
    c = conn.cursor()
    # Lấy dữ liệu đã nhập
    name_value = f_name.get()
    lastName_value = l_name.get()
    idclass_value = idclass.get()
    year_value = year.get()
    AVG_value = AVG.get()
    # Thực hiện câu lệnh để thêm
    c.execute('''
        INSERT INTO QLSV (first_name, last_name, idclass, year, AVG)
        VALUES (:first_name, :last_name, :idclass, :year, :AVG)
    ''', {
        'first_name': name_value,
        'last_name': lastName_value,
        'idclass': idclass_value,
        'year': year_value,
        'AVG': AVG_value,
    })
    conn.commit()
    conn.close()

    # Reset form
    f_name.delete(0, END)
    l_name.delete(0, END)
    idclass.delete(0, END)
    year.delete(0, END)
    AVG.delete(0, END)

    # Hiển thị lại dữ liệu
    truy_van()

def xoa():
    conn = sqlite3.connect('QLSV.db')
    c = conn.cursor()
    c.execute('''DELETE FROM QLSV WHERE id=:id''', {'id': delete_box.get()})
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
    # Hiển thị thông báo
    messagebox.showinfo("Thông báo", "Đã xóa!")
    # Hiển thị lại dữ liệu
    truy_van()

def truy_van():
    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect('QLSV.db')
    c = conn.cursor()
    c.execute("SELECT * FROM QLSV")
    records = c.fetchall()

    for r in records:
        tree.insert("", END, values=(r[0], r[1], r[2], r[3], r[4], r[5]))

    conn.close()

def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")

    conn = sqlite3.connect('QLSV.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM QLSV WHERE id=:id", {'id': record_id})
    records = c.fetchall()

    global f_name_editor, l_name_editor, idclass_editor, year_editor, AVG_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    idclass_editor = Entry(editor, width=30)
    idclass_editor.grid(row=2, column=1)
    year_editor = Entry(editor, width=30)
    year_editor.grid(row=3, column=1)
    AVG_editor = Entry(editor, width=30)
    AVG_editor.grid(row=4, column=1)

    f_name_label = Label(editor, text="Họ")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Tên")
    l_name_label.grid(row=1, column=0)
    idclass_label = Label(editor, text="Mã lớp")
    idclass_label.grid(row=2, column=0)
    year_label = Label(editor, text="Năm nhập học")
    year_label.grid(row=3, column=0)
    AVG_label = Label(editor, text="Điểm trung bình")
    AVG_label.grid(row=4, column=0)

    for record in records:
        f_name_editor.insert(0, record[1])
        l_name_editor.insert(0, record[2])
        idclass_editor.insert(0, record[3])
        year_editor.insert(0, record[4])
        AVG_editor.insert(0, record[5])
    edit_btn = Button(editor, text="Lưu bản ghi", command=lambda: cap_nhat(record_id))
    edit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def cap_nhat(record_id):
    conn = sqlite3.connect('QLSV.db')
    c = conn.cursor()

    c.execute("""UPDATE QLSV SET
            first_name = :first,
            last_name = :last,
            idclass = :idclass,
            year = :year,
            AVG = :AVG
            WHERE id = :id""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'idclass': idclass_editor.get(),
                  'year': year_editor.get(),
                  'AVG': AVG_editor.get(),
                  'id': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()
    truy_van()

# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
id = Entry(input_frame, width=30)
id.grid(row=0, column=1)
f_name = Entry(input_frame, width=30)
f_name.grid(row=1, column=1, padx=20, pady=(10, 0))
l_name = Entry(input_frame, width=30)
l_name.grid(row=2, column=1)
idclass = Entry(input_frame, width=30)
idclass.grid(row=3, column=1)
year = Entry(input_frame, width=30)
year.grid(row=4, column=1)
AVG = Entry(input_frame, width=30)
AVG.grid(row=5, column=1)

# Các nhãn
id_label = Label(input_frame, text="Mã sinh viên")
id_label.grid(row=0, column=0, pady=(10, 0))
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=1, column=0, pady=(10, 0))
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=2, column=0)
idclass_label = Label(input_frame, text="Mã lớp")
idclass_label.grid(row=3, column=0)
year_label = Label(input_frame, text="Năm học")
year_label.grid(row=4, column=0)
AVG_label = Label(input_frame, text="Điểm trung bình")
AVG_label.grid(row=5, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn ID")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("Mã sinh viên", "Họ", "Tên", "Mã lớp", "Năm nhập học","Điểm trung bình")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
for column in columns:
    tree.column(column, anchor=CENTER) # This will center text in rows
    tree.heading(column, text=column)
tree.pack()

# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()