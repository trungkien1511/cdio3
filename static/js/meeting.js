let localStream;
let mediaRecorder;
let recordedChunks = [];

async function startMeeting() {
    localStream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    document.getElementById("localVideo").srcObject = localStream;
}

function toggleCamera() {
    let videoTrack = localStream.getVideoTracks()[0];
    videoTrack.enabled = !videoTrack.enabled;
}

function toggleMic() {
    let audioTrack = localStream.getAudioTracks()[0];
    audioTrack.enabled = !audioTrack.enabled;
}

function startRecording() {
    recordedChunks = [];
    mediaRecorder = new MediaRecorder(localStream);
    mediaRecorder.ondataavailable = (event) => recordedChunks.push(event.data);
    mediaRecorder.start();
    alert("Bắt đầu ghi âm cuộc họp!");
}

function stopRecording() {
    mediaRecorder.stop();
    mediaRecorder.onstop = () => {
        let blob = new Blob(recordedChunks, { type: "audio/wav" });
        let url = URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "recording.wav";
        a.click();
        alert("Đã lưu file ghi âm!");
    };
}

function shareScreen() {
    navigator.mediaDevices.getDisplayMedia({ video: true }).then((screenStream) => {
        let screenTrack = screenStream.getVideoTracks()[0];
        let sender = localStream.getVideoTracks()[0];
        sender.replaceTrack(screenTrack);
    });
}

function copyURL() {
    navigator.clipboard.writeText(window.location.href);
    alert("Đã sao chép URL phòng họp!");
}

function endMeeting() {
    window.location.href = "/home";
}

startMeeting();
