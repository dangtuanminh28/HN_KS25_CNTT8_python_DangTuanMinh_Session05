

num_employee = int(input("Nhập số lượng nhân viên: "))
for count in range (num_employee) :    
    name_employee = input(f"Nhập tên nhân viên: ")
    day = int(input("Nhập số ngày làm: "))

    if day != 0:
        print(f"{name_employee}: {"*" * day}") 

    if day < 0 or day > 22 :
        print("Dữ liệu không hợp lệ") 
        continue
    elif day == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
    elif day >= 18:
        print("Làm việc chăm chỉ") 
    elif day < 10 :
        print("Làm việc ít")
    else :
        print("Làm việc bình thường")

    count += 1
