from transformers import MBartForConditionalGeneration, AutoTokenizer

# Tải tokenizer và mô hình BARTpho-syllable
model_name = "vinai/bartpho-syllable"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)

# Văn bản cần tóm tắt
text = """
Công nghệ đã và đang có ảnh hưởng sâu rộng đến nhiều lĩnh vực, trong đó giáo dục không phải là ngoại lệ. Những tiến bộ trong công nghệ thông tin và truyền thông đã thay đổi cách thức học tập và giảng dạy trên toàn cầu, mang lại nhiều lợi ích đáng kể nhưng cũng đặt ra những thách thức lớn.

Trước tiên, công nghệ đã cải thiện đáng kể hiệu quả của quá trình giảng dạy và học tập. Việc sử dụng các công cụ học tập trực tuyến, phần mềm giáo dục và các thiết bị điện tử giúp học sinh và giáo viên có thể tiếp cận kiến thức một cách dễ dàng và linh hoạt hơn. Các lớp học trực tuyến, học qua video và ứng dụng học tập giúp học sinh học mọi lúc, mọi nơi, giảm bớt sự phụ thuộc vào giờ học cố định tại lớp. Điều này đặc biệt quan trọng trong bối cảnh đại dịch COVID-19, khi việc học trực tuyến trở thành phương thức chính để duy trì hoạt động giáo dục.

Bên cạnh đó, công nghệ cũng giúp giáo viên tạo ra các bài giảng sinh động và hấp dẫn hơn. Các phần mềm tương tác, bảng điện tử, và các công cụ truyền thông đa phương tiện như video, hình ảnh, đồ họa không chỉ giúp nội dung bài học trở nên phong phú mà còn kích thích sự sáng tạo và hứng thú học tập của học sinh. Những công nghệ này còn giúp giáo viên dễ dàng theo dõi tiến độ học tập của từng học sinh, từ đó điều chỉnh phương pháp giảng dạy sao cho phù hợp.

Tuy nhiên, mặc dù công nghệ mang lại nhiều cơ hội, nhưng cũng không thiếu những thách thức. Một trong những vấn đề lớn nhất là sự chênh lệch trong khả năng tiếp cận công nghệ giữa các học sinh. Không phải học sinh nào cũng có đủ điều kiện để sở hữu thiết bị học tập hiện đại và kết nối Internet ổn định, điều này dẫn đến tình trạng phân hóa trong giáo dục. Những học sinh thiếu khả năng tiếp cận công nghệ có thể bị bỏ lại phía sau, gây ra bất bình đẳng trong cơ hội học tập.

Thêm vào đó, việc quá lạm dụng công nghệ cũng có thể dẫn đến những tác động tiêu cực đối với sức khỏe học sinh, như mắt mỏi, đau lưng, hay vấn đề về tâm lý. Việc dành quá nhiều thời gian vào các thiết bị điện tử có thể làm giảm khả năng tương tác xã hội của học sinh, khiến họ cảm thấy cô đơn và thiếu động lực.

Tóm lại, công nghệ mang lại rất nhiều cơ hội phát triển cho giáo dục, nhưng cũng đòi hỏi chúng ta phải giải quyết những thách thức liên quan đến việc tiếp cận công nghệ và bảo vệ sức khỏe tâm lý của học sinh. Việc ứng dụng công nghệ trong giáo dục cần được thực hiện một cách cân nhắc và hợp lý để tận dụng tối đa lợi ích mà nó mang lại.
"""

# Tiền xử lý văn bản
input_ids = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)

# Sinh bản tóm tắt
summary_ids = model.generate(
    input_ids,
    max_length=150,  # Độ dài tối đa của bản tóm tắt
    min_length=50,   # Độ dài tối thiểu của bản tóm tắt
    length_penalty=1.0,  # Hệ số phạt độ dài (1.0 nghĩa là không phạt)
    num_beams=4,     # Số lượng beams trong beam search
    early_stopping=True
)

# Giải mã và in ra bản tóm tắt
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Bản tóm tắt:", summary)
