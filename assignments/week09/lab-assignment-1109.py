units = int(input("กรอกค่าไฟ:"))
cost = 0

def calculate_electricity_cost(uint):
    if units > 200:
        cost = 125.0 + 150.0 + 350.0 +((units-200) * 4.00) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00บาท")
        print("101-200 หน่วย: 350")
        print(f"201-{units} หน่วย: {(units - 200) * 4.00}บาท")
        print("ค่าบริการ : 25.00 บาท")
        print("รวมค่าไฟฟ้าทั้งสิ้น:", cost,"บาท")

    elif units > 100:
        cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print(f"51-{units} หน่วย: {(units - 50) * 3.00} บาท")
        print("ค่าบริการ : 25.00 บาท")
        print("รวมค่าไฟฟ้าทั้งสิ้น:", cost,"บาท")

    elif units > 50:
        cost = 125.0 + ((units - 50) * 3.00) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print("51 - {units} หน่วย: {(unit - 50) * 3.00} บาท")
        print("ค่าบริการ : 25.00 บาท")
        print("รวมค่าไฟฟ้าทั้งสิ้น:", cost,"บาท")

    elif units >= 0:
        cost = units * 2.50 + 25
        print(f"{units} หน่วย: {(units) * 2.50} บาท")
        print("ค่าบริการ : 25.00 บาท")
        print("รวมค่าไฟฟ้าทั้งสิ้น:", cost,"บาท")

    else:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")

while(0<1):
    print("===== โปรแกรมคำนวณค่าไฟ =====")
    print("1.คำนวณค่าไฟ")
    print("2.ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")

    if choice == "2":
        break
    else:
        print("เลือกเมนูให้ถูกต้อง")