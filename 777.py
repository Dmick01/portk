import math #เรียกใช้ฟังก์ชันคณิตศาสตร์ เช่น sin() cos()
from turtle import* #เรียกเครื่องมือวาดรูป Turtle ทั้งหมดมาใช้ได้เลย

def hearta(k): #ค่ามุมที่เปลี่ยนไปเรื่อยๆ
    return 15 * math.sin(k)**3 #หมายถึง ยกกำลัง 3
def heartb(k):
    return 12 * math.cos(k)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k) #อันนี้เป็นสูตรคณิตศาสตร์สำหรับ “ครึ่งบน-ล่างของหัวใจ”ใช้ cos() หลายตัวรวมกันเพื่อให้เส้นออกมาเป็นรูปหัวใจ
speed(0)
bgcolor("black")
for i in range(6000):  #คือตัวแปรนับรอบ
    goto(hearta(i)*20, heartb(i)*20) #เอาค่าจากฟังก์ชันหัวใจแกน X มาคูณ 20 เพื่อขยายรูป
    color("red")
done()    
