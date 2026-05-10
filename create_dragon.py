from PIL import Image

# กำหนดขนาดของภาพพิกเซล (เช่น 16x16 พิกเซล)
size = (16, 16)
# สร้างภาพใหม่พื้นหลังโปร่งใส (RGBA)
img = Image.new("RGBA", size, (0, 0, 0, 0))
pixels = img.load()

# กำหนดสีที่ใช้
RED = (255, 0, 0, 255)
DARK_RED = (150, 0, 0, 255)
BLACK = (0, 0, 0, 255)

# ตัวอย่างการวาดพิกเซลแบบกำหนดจุด (ตัวอย่างร่างโครงมังกรแบบง่าย)
# วาดส่วนหัว
for x in range(5, 10):
    for y in range(3, 7):
        pixels[x, y] = RED

# วาดส่วนตัว
for x in range(4, 11):
    for y in range(7, 12):
        pixels[x, y] = DARK_RED

# วาดปีก
pixels[3, 7] = RED
pixels[2, 6] = RED
pixels[11, 7] = RED
pixels[12, 6] = RED

# ขยายภาพให้ใหญ่ขึ้นเพื่อให้เห็นพิกเซลชัดเจน (จาก 16x16 เป็น 256x256)
img_scaled = img.resize((256, 256), resample=Image.NEAREST)

# บันทึกไฟล์
img_scaled.save("pixel_dragon.png")
print("สร้างภาพมังกรพิกเซลเรียบร้อยแล้ว!")