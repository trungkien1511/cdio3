import google.generativeai as genai
import time

# Thay YOUR_API_KEY bằng API Key của bạn
API_KEY = "AIzaSyC8WB_X1d3RIkIdcLI_Db3KDUSfkEfXKM8"
genai.configure(api_key=API_KEY)

# Chọn mô hình Gemini (ví dụ: gemini-1.5-pro)
model = genai.GenerativeModel("gemini-1.5-pro")

# Vòng lặp để nhập nhiều lần
while True:
    # Nhập câu hỏi từ người dùng
    user_input = input("Nhập câu hỏi của bạn (hoặc 'thoát' để dừng): ")
    
    # Kiểm tra nếu người dùng muốn thoát
    if user_input.lower() == "thoát":
        print("Tạm biệt!")
        break
    
    # Gửi yêu cầu đến API với đầu vào từ người dùng
    try:
        response = model.generate_content(user_input)
        print("Trả lời:", response.text)
        time.sleep(2)  # Chờ 2 giây trước khi cho phép yêu cầu tiếp theo
    except Exception as e:
            if "429" in str(e): 
                print("Quota đã hết! Vui lòng chờ đến khi quota được làm mới (thường sau 24 giờ) hoặc thử API Key khác.")
            else:
                print(f"Đã xảy ra lỗi khác: {e}")
    time.sleep(1)  # Độ trễ để tránh spam   