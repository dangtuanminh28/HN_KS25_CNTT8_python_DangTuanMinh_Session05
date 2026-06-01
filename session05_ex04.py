'''
Input
    branch_count số lượng chi nhánh quản lý int(số nguyên)
    student_count số lượng học sinh int(số nguyên)
Output
    Thông báo yêu cầu nhập lại nếu số học sinh < 0
    Thông báo bỏ qua kiểm tra nếu số học viên = 0
    Khi dữ liệu hợp lệ hiển thị phân loại trạng thái lớp học

Đề xuất giải pháp: cấu trúc vòng lặp lồng nhau phân tầng
    Tầng 1 biến branch chạy từ (1 -> branch_count)
    Tầng 2 biến classroom chạy từ (1 -> 2)
    Tầng while kiểm soát quá trình nhập bằng biến is_done sẽ chạy liên tục khi người dùng nhập sai dữ liệu nếu điều kiện hợp lệ sẽ break khỏi vòng lặp
    Dùng end="\n" để xử lý khoảng trống dòng giữa các nhánh
Giải pháp
    Nên khai báo biến is_done 
    Nếu người dùng nhập < 0 vòng lặp while not is_done sẽ chạy liên tục cho đến khi người dùng nhập hợp lệ do is_done = False nên vòng lặp sẽ vẫn giữ nguyên False
    Nếu nhập > 0 thì biến is_done = True và thoát khỏi vòng lặp while
    Nếu nhập = 0 điều kiện if sẽ thông báo hcoj sinh vắng và không so sánh điều kiện

Mô tả luồng chạy:
Bước 1: Yêu cầu người dùng nhập số lượng chi nhánh (branch_count)
Bước 2: Bắt đầu vòng lặp tầng 1 biến branch chạy từ (1 -> branch_count), in ra thứ tự chi nhánh
Bước 3: Vòng lặp tầng 2 biến classroom chạy từ (1 -> 2)
Bước 4: Biến is_done = False khai báo và trong vòng lặp while yêu cầu người dùng nhập số lượng học viên (student_count)
Điều kiện:
    Nếu student_count < 0 báo lỗi và quay lại vòng lặp while nhập lại
    Nếu student_count >= 0 biến is_done = True và vòng lặp while not is_done sẽ nhận và tự kết thúc vòng lặp và xuống tiếp
Bước 5:
Điều kiện:
    Nếu student_count == 0 in thông báo lớp vắng
    Nếu student_count >= 20 in thông báo lớp ổn định
    Nếu 0 < student_count < 20 in thông báo lớp cần được nhắc nhở
Bước 6:
    Sau khi in kết quả xong, hệ thống sẽ quay lại vòng lặp ban đầu và sang chi nhánh tiếp theo cho đến khi đủ số lượng chi nhánh (branch_count) từ người dùng nhập
'''


branch_count = int(input("Nhập số lượng chi nhánh: "))

for branch in range(1, branch_count + 1):
    print(end="\n")
    print(f"Chi nhánh {branch}:")
    
    for classroom in range(1, 3):
        is_done = False
        
        while not is_done:
            student_count = int(input(f"  Nhập số học viên đi học của lớp {classroom}: "))
            if student_count < 0:
                print("  Số học viên không hợp lệ. Vui lòng nhập lại.")
            else:
                is_done = True
        if student_count == 0:
            print("  Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
        elif student_count >= 20:
            print(f"  Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
        else:
            print(f"  Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi")