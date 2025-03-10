function loginWithToken() {
    const token = prompt("Nhập User Token:");
    if (token) {
        fetch("/authenticate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ token: token })
        })
        .then(response => response.json())
        .then(data => {
            if (data.token) {
                window.location.href = "/home";
            } else {
                alert("Đăng nhập thất bại!");
            }
        })
        .catch(error => console.error("Lỗi:", error));
    }
}
