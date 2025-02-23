from flask import Flask, request, jsonify
from flask_cors import CORS
import whisper
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {
    "origins": "*",
    "allow_headers": ["Content-Type", "Authorization"],
    "methods": ["GET", "POST", "PUT", "DELETE"]
}})

model = whisper.load_model(os.getenv("WHISPER_BASE_MODEL"))

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['audio']
    file_path = os.path.join("temp", file.filename)
    os.makedirs("temp", exist_ok=True)

    file.save(file_path)

    result = model.transcribe(file_path)
    transcription = result["text"]

    os.remove(file_path)

    return jsonify({
        "transcription": transcription,
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)