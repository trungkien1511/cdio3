from flask import Flask, render_template, redirect, url_for, request
import os

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

# Route để xử lý upload file
@app.route("/upload", methods=["POST"])
def upload_file():
    if "audio" not in request.files:
        return "Không có file được gửi lên!", 400

    file = request.files["audio"]
    if file.filename == "":
        return "Không có file được chọn!", 400

    # Lưu file vào thư mục uploads
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)
    return "File đã được lưu thành công!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
