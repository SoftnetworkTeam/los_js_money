import re

def convert_db_table_to_lowercase(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # ใช้ regex หา db_table และแปลงค่าด้านในให้เป็นตัวพิมพ์เล็ก
    updated_content = re.sub(
        r"(db_table\s*=\s*['\"])([^'\"]+)(['\"])", 
        lambda match: f"{match.group(1)}{match.group(2).lower()}{match.group(3)}", 
        content
    )

    # บันทึกการเปลี่ยนแปลงกลับไปที่ไฟล์เดิม
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"✅ เปลี่ยนชื่อ db_table ในไฟล์ {file_path} เป็นตัวพิมพ์เล็กเรียบร้อยแล้ว!")

# ระบุพาธไฟล์ที่ต้องการเปลี่ยน
file_paths = [
    "models.py",
    "userauth/models.py",
    "nameList/models.py",
    "theme/models.py",
]
for file_path in file_paths:
    convert_db_table_to_lowercase(file_path)

#วิธีรัน คลิกขวาที่ไฟล์ convert_db_table.py → เลือก Run Python File in Terminal