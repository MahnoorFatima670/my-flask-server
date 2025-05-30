from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from fer import FER
import cv2
import os
from moviepy.editor import VideoFileClip

app = Flask(__name__)

# Enable CORS for the Flask app
CORS(app)

detector = FER()

@app.route('/')
def home():
    return jsonify({"message": "Emotion Monitoring Backend is running!"})

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    if 'video' not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    file = request.files['video']
    
    # Use a temporary file path to store the uploaded video
    video_path = os.path.join(os.getcwd(), "uploaded_video.mp4")
    file.save(video_path)

    if not os.path.exists(video_path):
        return jsonify({"error": "File not found after upload"}), 400

    try:
        clip = VideoFileClip(video_path)
    except Exception as e:
        return jsonify({"error": f"Error loading video: {str(e)}"}), 500

    emotions = []
    frame_count = 0

    # Process frames of the video (limit to first 10 frames for demo)
    for frame in clip.iter_frames(fps=1, dtype="uint8"):
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        detected_emotions = detector.detect_emotions(img)
        
        if detected_emotions:
            # Extract emotions from the detected data
            emotions.append(detected_emotions[0]['emotions'])

        frame_count += 1
        if frame_count >= 10:
            break

    if not emotions:
        return jsonify({"message": "No emotions detected"}), 200

    # Ensure the emotions are serialized correctly
    return jsonify({"emotions": emotions})

# Ensure Flask is running on 0.0.0.0 so it's accessible from other devices
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)










































