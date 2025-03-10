import google.generativeai as genai
import time

# Cấu hình API Key (Không nên để API Key trực tiếp trong code, dùng biến môi trường thay thế)
API_KEY = "AIzaSyC8WB_X1d3RIkIdcLI_Db3KDUSfkEfXKM8"
genai.configure(api_key=API_KEY)

# Chọn mô hình Gemini
model = genai.GenerativeModel("gemini-1.5-pro")

# Nội dung cuộc họp mở rộng
conversation = """
Chủ trì: Chào mọi người, hôm nay chúng ta họp để lên kế hoạch tổ chức sự kiện cuối năm. Ai có ý tưởng gì không?

Lan: Tôi nghĩ chúng ta có thể tổ chức một buổi tiệc ngoài trời, kết hợp với các hoạt động team building để gắn kết mọi người.

Nam: Nghe hay đấy! Nhưng chúng ta cần chọn địa điểm phù hợp. Công viên trung tâm có thể là một lựa chọn tốt.

Mai: Đúng vậy, nhưng cần xin giấy phép nếu tổ chức ở công viên. Chúng ta có thể cân nhắc thuê một địa điểm riêng để dễ quản lý hơn.

Chủ trì: Ý tưởng hay. Vậy chi phí cho địa điểm, thức ăn và các hoạt động dự kiến khoảng bao nhiêu?

Lan: Tôi sẽ lên bảng dự toán chi phí. Nhưng cần quyết định xem chúng ta có tổ chức bữa ăn tự chọn hay thuê dịch vụ catering không?

Nam: Tôi đề xuất thuê dịch vụ catering chuyên nghiệp để đảm bảo chất lượng.

Mai: Đồng ý. Nhưng chúng ta cũng có thể tổ chức một khu vực buffet nhỏ cho những ai muốn tự phục vụ.

Chủ trì: Tuyệt vời! Vậy thời gian dự kiến là khi nào?

Lan: Tôi nghĩ cuối tuần trước Giáng sinh là hợp lý, vì sau đó mọi người sẽ bận về quê hoặc đi du lịch.

Nam: Đồng ý, nhưng chúng ta cần chốt danh sách tham gia sớm để đặt dịch vụ.

Tất cả: Nhất trí!
"""
    
# Yêu cầu AI tóm tắt và đưa ra kế hoạch tổ chức cuộc họp
prompt = f"Tóm tắt cuộc họp sau:\n{conversation}"

# Gửi yêu cầu đến AI
try:
    response = model.generate_content(prompt)
    print("Bản tóm tắt:")
    print(response.text)
except Exception as e:
    if "429" in str(e):
        print("Quota API đã hết! Vui lòng chờ hoặc thử API Key khác.")
    else:
        print(f"⚠️ Đã xảy ra lỗi: {e}")
