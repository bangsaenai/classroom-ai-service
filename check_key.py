import requests

API_KEY = "xxx"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

print(f"กำลังตรวจสอบเมนูของ Key: {API_KEY[:10]}...")
response = requests.get(url)

if response.status_code == 200:
    print("✅ สำเร็จ! รายชื่อโมเดลที่ใช้ได้:")
    data = response.json()
    if 'models' in data:
        for m in data['models']:
            print(f"- {m['name']}")
    else:
        print("⚠️ ไม่พบโมเดลใดๆ (รายการว่างเปล่า)")
else:
    print(f"❌ เกิดข้อผิดพลาด (Code {response.status_code}):")
    print(response.text)
