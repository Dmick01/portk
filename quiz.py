import random

questions = [
    {
        "question": "Python ใช้คำสั่งใดในการแสดงข้อความ?",
        "choices": ["A. print()", "B. show()", "C. display()", "D. text()"],
        "answer": "A"
    },
    {
        "question": "ข้อใดเป็นชนิดข้อมูลจำนวนเต็มใน Python?",
        "choices": ["A. str", "B. int", "C. float", "D. bool"],
        "answer": "B"
    },
    {
        "question": "คำสั่งใดใช้รับข้อมูลจากผู้ใช้?",
        "choices": ["A. get()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    },
    {
        "question": "ข้อใดใช้สำหรับตรวจสอบเงื่อนไข?",
        "choices": ["A. if", "B. for", "C. import", "D. def"],
        "answer": "A"
    },
    {
        "question": "สัญลักษณ์ใดใช้สำหรับการหารใน Python?",
        "choices": ["A. +", "B. //", "C. /", "D. %"],
        "answer": "C"
    },
    {
        "question": "คำสั่งใดใช้สร้างฟังก์ชัน?",
        "choices": ["A. function", "B. func", "C. def", "D. create"],
        "answer": "C"
    },
    {
        "question": "ข้อใดเป็น Boolean?",
        "choices": ["A. 10", "B. 'Hello'", "C. True", "D. 3.14"],
        "answer": "C"
    },
    {
        "question": "คำสั่งใดใช้วนซ้ำตามจำนวนรอบ?",
        "choices": ["A. if", "B. for", "C. def", "D. input"],
        "answer": "B"
    },
    {
        "question": "ข้อใดใช้เก็บข้อมูลหลายค่าในรูปแบบรายการ?",
        "choices": ["A. list", "B. int", "C. bool", "D. float"],
        "answer": "A"
    },
    {
        "question": "Python มีนามสกุลไฟล์ใด?",
        "choices": ["A. .cpp", "B. .java", "C. .py", "D. .html"],
        "answer": "C"
    }
]


def show_result(score):
    print("\n========== ผลคะแนน ==========")
    print(f"คะแนนของคุณ: {score}/10")

    if score >= 9:
        print("ระดับ: เก่งนี่หว่า 🏆")
    elif score >= 7:
        print("ระดับ: ใช้ได้ ⭐")
    elif score >= 5:
        print("ระดับ: งั้นๆ 👍")
    else:
        print("ระดับ: ไปเรียนมาใหม่ 💪")


def start_quiz():
    score = 0

    # สุ่มลำดับคำถาม
    quiz = questions.copy()
    random.shuffle(quiz)

    print("\n========== เริ่มทำแบบทดสอบ ==========")

    for number, question in enumerate(quiz, 1):
        print(f"\nข้อที่ {number}: {question['question']}")

        for choice in question["choices"]:
            print(choice)

        answer = input("คำตอบของคุณ: ").upper()

        if answer == question["answer"]:
            print("✓ ถูกต้อง!")
            score += 1
        else:
            print(f"✗ ผิด! คำตอบคือ {question['answer']}")

    show_result(score)


while True:
    print("\n==============================")
    print("     COMPUTER QUIZ - PYTHON")
    print("==============================")
    print("1. เริ่ม")
    print("2. ออกจากโปรแกรม")

    menu = input("เลือกเมนู: ")

    if menu == "1":
        start_quiz()

    elif menu == "2":
        print("แต๊งกิ้วที่เล่นเกม!")
        break

    else:
        print("มีแค่นี้เว้ย 1 หรือ 2")
