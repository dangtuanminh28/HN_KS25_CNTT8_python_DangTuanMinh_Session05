"""
Input 
    room_count số lượng phòng int(số nguyên) 
    rows số ghế của từng phòng int(số nguyên) 
    seats_per_row số ghế trên mỗi hàng int(số nguyên) 
Output
    Nếu nhập sai ko hợp lệ thông báo lỗi
    Nếu hợp lệ hiển thị sơ đồ chỗ ngồi dưới ký tự *

Giải pháp dùng vòng lặp lồng 3 tầng
    Tầng 1: quản lý thứ tự phòng đáng xét
    Tầng 2: quản lý từng hàng ghế theo chiều dọc
    Tầng 3: quản lý từng hàng ghế theo chiều ngang
Khai báo is_running = True để kiểm tra dữ liệu nếu hợp lệ, khi gặp dữ liệu sai thì cần thêm is_running = False kèm theo break để kết thúc chương trình

Luồng chạy
Bước 1
    Người dùng nhập số lượng phòng (room_count)
    Kiểm tra điều kiện nếu room_count <= 0 báo lỗi và kết thúc lun chương trình
    Nếu room_count > 0 tạo biến is_running = True để chạy trong vòng lặp ở tầng 1
Bước 2
    Nếu is_running = False chương trình ra khỏi vòng lặp và kết thúc chương trình luôn
    Nếu is_running = True bắt đầu tăng chỉ số room và yêu cầu nhập số rows (hàng) và seat_per_row (ghế)
Bước 3
    Nếu rows <= 0 hoặc seats_per_row <= 0 báo dữ liệu không hợp lệ và bỏ qua không lưu kết quả và xét phòng tiếp theo
    Nếu rows > 10 hoặc seats_per_row > 10 báo phòng quá lớn, biến is_running = False và kết thúc chương trình xuống thẳng luồng cuối
    Nếu hợp lệ sang bước 4 vẽ sơ đồ
Bước 4
    Bắt đầu vòng lặp tầng 2 chỉ số i chạy từ (0 -> rows - 1) và mỗi lần i chạy là bắt đầu vòng lặp tầng 3 với chỉ số j chạy từ (0 -> seats_per_row - 1)
    In ra ký tự * và giữ nguyên con trỏ end=""
    Khi vòng lặp j chạy xong thoát ra vòng lặp i rồi xuống dòng mới qua  print(end="\n")
    Khi in đủ số rows sau đó quay lại bước 2
"""
room_count = int(input("Nhập số lượng phòng học cần kiểm tra: "))

if room_count <= 0:
    print("Số lượng phòng học không hợp lệ")
    print("Chương trình kết thúc")
else:
    is_running = True

    for room in range(1, room_count + 1):
        if not is_running:
            break

        print(f"--- NHẬP THÔNG TIN PHÒNG HỌC THỨ {room} ---")
        
        rows = int(input("Nhập số hàng ghế: "))
        seats_per_row = int(input("Nhập số ghế trên mỗi hàng: "))

        if rows <= 0 or seats_per_row <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue

        elif rows > 10 or seats_per_row > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            is_running = False
            break  

        print(f"Sơ đồ chỗ ngồi của Phòng {room}:")

        for i in range(rows):
            for j in range(seats_per_row):
                print("*", end="")
            
            print(end="\n")