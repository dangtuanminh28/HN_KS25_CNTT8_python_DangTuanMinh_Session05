'''
Phân tích lỗi 
Vì total_students = 0 đang ở ngoài làm cho biến không bao giờ thay đổi được khi chuyển sang chi nhánh mới
Dò luồng thực thi
- Chi nhánh 1:
    Khởi tạo total_students = 0 
    Người dùng nhập 83 xong hệ thống xử lý vòng lặp với phép tính 0 + 83 = 83
    In ra kết quả 83 học viên(đúng)
- Chi nhánh 2:
    Khi vòng lặp ngoài sang branch = 2, lúc đấy total_students = 83 chưa thay đổi gì
    Người dùng nhập 60 hệ thống cộng dồn 83 + 60 = 143 học viên(sai)
- Chi nhánh 3:
    Khi sang chi nhánh branch = 3, lúc này total_students = 143
    Người dùng nhập 97 và hệ thống xử lý 143 + 97 = 240 học viên(sai)
'''

#Sửa lại
branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lớp học của mỗi chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(f"\n--- CHI NHÁNH {branch} ---")
    
    total_students = 0 
    
    for classroom in range(1, class_count + 1):
        student_count = int(input(f"Nhập số học viên lớp {classroom}: "))
        total_students += student_count
        
    print(f"Chi nhánh {branch}: {total_students} học viên")