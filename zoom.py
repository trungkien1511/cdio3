from flask import Flask, render_template, redirect, url_for, request
import os
import subprocess

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"

@app.route("/")
def index():
    return redirect(url_for("login_meeting"))

@app.route("/login") 
def login_meeting():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/pre_meeting/<room_id>")
def pre_meeting(room_id):
    return render_template("pre_meeting.html", room_id=room_id)

@app.route("/meeting/<room_id>")
def meeting(room_id):
    return render_template("meeting.html", room_id=room_id)

@app.route("/create_meeting")
def create_meeting():
    import random
    room_id = str(random.randint(1000, 9999))  # Tạo RoomID ngẫu nhiên
    return redirect(url_for("pre_meeting", room_id=room_id))

# Đường dẫn đến thư mục uploads
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    if "audio" not in request.files:
        return "Không có file được gửi lên!", 400

    file = request.files["audio"]
    if file.filename == "":
        return "Không có file được chọn!", 400

    # Lưu file gốc (.webm)
    webm_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(webm_path)

    # Chuyển đổi sang .wav bằng ffmpeg với đường dẫn tuyệt đối
    ffmpeg_path = r"C:\Users\Trung Kien\OneDrive\Downloads\ffmpeg-2025-03-06-git-696ea1c223-full_build\bin\ffmpeg.exe"
    wav_filename = file.filename.replace(".webm", ".wav")
    wav_path = os.path.join(app.config["UPLOAD_FOLDER"], wav_filename)
    subprocess.run([
        ffmpeg_path, "-i", webm_path, "-ar", "16000", "-ac", "1", wav_path
    ], check=True)

    # Xóa file .webm nếu không cần
    os.remove(webm_path)

    return "File đã được chuyển đổi và lưu thành công dưới dạng .wav!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
