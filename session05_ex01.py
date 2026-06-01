'''
Vì khi đặt month ngoài vòng lặp và branch trong vòng lặp, đầu ra sẽ bị xếp ở các vị trí khó nhìn theo thời gian, khiến cho người ngoài khó nhìn
Vòng lặp ngoài nên duyệt theo chi nhánh:
-> Vì vòng lặp ngoài giữ cố định cho tiêu đề nhóm khi vòng ngoài chọn chi nhánh 1, vòng lặp bên trong sẽ lặp cho đến khi xong mới đến chi nhánh 2
Vòng lặp ngoài nên duyệt theo tháng:
-> Vì vòng lặp trong có chứa dòng thời gian khi đó hệ thống chạy từ tháng 1 đến 3 để lấy dữ liệu và in ra kết quả doanh thu
'''

# Sửa lại
branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3
result = ""

for branch in range(1, branch_count + 1):
    result += f"--- CHI NHÁNH {branch} ---\n"
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu Chi nhánh {branch}, Tháng {month}: "))
        result += f"Chi nhánh {branch} ,tháng {month}: {revenue} triệu đồng\n"
    
print(result)