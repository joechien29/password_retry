# password 3 times Error

password = "a123456"
input_password = input("請輸入密碼 (最多輸入3次密碼): ")
i = 3
while input_password != password:
    if i == 1:
        print("輸入錯誤次數超過3次，將自動離開程式")
        break
    i = i - 1
    print("密碼錯誤，還有", i, "次機會")
    input_password = input("請輸入密碼: ")

if input_password == password:
	print("登入成功")