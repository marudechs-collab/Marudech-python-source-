def deposit(money):
    balance = money
    print(f"ยอดเงินเริ่มต้น: {balance} บาท")

    try:
        amount = float(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
   
    except ValueError:
        print(f"\nเกิดข้อผิดพลาดกรุณากรอกตัวเลข")
    
    else:
        balance += amount
        print(f"\nฝากเงินสำเร็จ\nยอดเงินคงเหลือ: {balance:.2f} บาท")
   
    finally:
        print("สิ้นสุดรายการฝากเงิน")

deposit(1000)