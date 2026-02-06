import requests
import sys

# ==========================================
# ส่วนตั้งค่า (Config)
# ==========================================
# 1. ลิงก์ประตูทางเข้า AI (อาจารย์เตรียมไว้ให้แล้ว)
API_URL = "https://classroom-ai-service-940908397399.asia-southeast1.run.app/chat"

# 2. กุญแจเข้าใช้งาน (ให้นักเรียนเปลี่ยนตรงนี้เป็น Key ที่ได้รับแจก)
MY_API_KEY = "ให้เอารหัสของตัวเองมาใส่" 
# ==========================================

def chat_loop():
    print(f"\n--- 🤖 ยินดีต้อนรับสู่ AI Classroom ---")
    print(f"🔑 กำลังเชื่อมต่อด้วย Key: {MY_API_KEY}")
    print("พิมพ์ 'exit' เพื่อจบการทำงาน\n")

    while True:
        try:
            user_input = input("🗣️  คุณถาม: ")
            
            if user_input.strip().lower() in ['exit', 'quit', 'ออก']:
                print("👋 บ๊ายบายครับ!")
                break
            
            if not user_input.strip():
                continue

            # เตรียมข้อมูลส่งไปหา Server
            headers = {"x-api-key": MY_API_KEY}
            payload = {"message": user_input}

            print("⏳ กำลังรอคำตอบจาก Gemini...")
            
            # ยิง Request ไปหา Cloud Run
            response = requests.post(API_URL, json=payload, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print(f"🤖 AI ตอบ ({data['student_id']}):\n{data['reply']}")
            elif response.status_code == 401:
                print("❌ Error: กุญแจผิด! หรือยังไม่ได้จ่ายค่าบริการ")
            else:
                print(f"⚠️ Error ({response.status_code}): {response.text}")

            print("-" * 40)

        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาด: {e}")

if __name__ == "__main__":
    chat_loop()
