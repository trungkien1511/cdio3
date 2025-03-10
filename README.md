<<<<<<< HEAD
# cdio3
=======
# Tóm Tắt Văn Bản Sử Dụng Mô Hình VietAI/vit5-base-vietnews-summarization

## Giới thiệu
Đây là một đoạn mã Python sử dụng mô hình **VietAI/vit5-base-vietnews-summarization** từ thư viện **Hugging Face Transformers** để thực hiện tóm tắt văn bản tiếng Việt.

## Cài đặt
Trước khi chạy mã, cần cài đặt thư viện **transformers** và các dependencies cần thiết:
```bash
pip install transformers torch
```

## Hướng dẫn sử dụng

### 1. Import các thư viện cần thiết
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
```

### 2. Tải mô hình và tokenizer
```python
model_name = "VietAI/vit5-base-vietnews-summarization"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
```

### 3. Văn bản cần tóm tắt
Ví dụ văn bản về đồ án tốt nghiệp minh họa sách nghệ thuật truyền thống:
```python
text = """ ĐỒ ÁN TỐT NGHIỆP: MINH HỌA SÁCH VỀ MỘT SỐ LOẠI HÌNH NGHỆ THUẬT TRUYỀN THỐNG VIỆT NAM "TINH HOA ÂM SẮC"
Đây là sách minh họa về một số loại hình nghệ thuật như Cà Trù, Hát Chèo, Tuồng... của tác giả Kim Ngân. Những yếu tố đặc trưng được thể hiện qua nét vẽ đầy màu sắc, bắt mắt, kết hợp chất liệu xà cừ với mong muốn sẽ tạo ra cái nhìn mới mẻ hơn tới độc giả trải nghiệm nhưng vẫn giữ được những đường nét cổ kính đậm tinh thần truyền thống.
Nội dung sách được chia làm ba miền với các gam màu đặc trưng như đỏ tượng trưng cho miền Bắc, xanh lam cho miền Trung và xanh lá cho miền Nam.
Về thông tin sách tác giả đã tổng hợp từ nhiều nguồn khác nhau và biên tập lại để cho ra quyển sách có nội dung phân cấp và dễ nhận ra yếu tố đặc trưng."""
```

### 4. Tiền xử lý văn bản
Mã hóa văn bản đầu vào trước khi đưa vào mô hình:
```python
input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
```

### 5. Sinh bản tóm tắt
Dùng mô hình để sinh bản tóm tắt:
```python
summary_ids = model.generate(input_ids, max_length=100, min_length=20, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
```

### 6. In kết quả tóm tắt
```python
print("Bản tóm tắt:", summary)
```

## Kết luận
- Mô hình **VietAI/vit5-base-vietnews-summarization** có thể giúp tóm tắt văn bản tiếng Việt một cách hiệu quả.
- Có thể điều chỉnh **max_length**, **min_length**, **num_beams** để cải thiện chất lượng tóm tắt.
- Ứng dụng hữu ích trong xử lý văn bản, báo chí, nghiên cứu.

---

Nếu bạn có thắc mắc hoặc cần hỗ trợ, hãy liên hệ qua GitHub hoặc email. 🚀

>>>>>>> cbcf2d6 (Initial commit)
