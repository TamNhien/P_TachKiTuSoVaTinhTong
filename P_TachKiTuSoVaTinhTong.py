string = input("Nhập chuỗi: ")
numbers = [int(char) for char in string if char.isdigit()]
total = sum(numbers)
print("Tổng các ký tự số trong chuỗi là : ", total)

