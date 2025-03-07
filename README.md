# Local Transcriber

A Flask-based API service that transcribes audio files using OpenAI's Whisper model locally. This service provides a simple REST API endpoint for audio transcription without requiring external API calls.

## Prerequisites

- Python 3.x
- FFmpeg (required for audio processing)
- Docker (optional, for containerized deployment)

## Installation

### Using Docker (Recommended)

1. Build and run using Docker Compose:
```bash
docker-compose up --build
```

### Manual Setup

1. Install FFmpeg:
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`.

## API Documentation

### Transcribe Audio

Endpoint to transcribe audio files to text.

- **URL**: `/transcribe`
- **Method**: `POST`
- **Content-Type**: `multipart/form-data`
- **Form Parameter**: `audio` (audio file)

#### Example Requests

Using curl:
```bash
curl -X POST \
  http://localhost:5000/transcribe \
  -H 'Content-Type: multipart/form-data' \
  -F 'audio=@path/to/your/audio.mp3'
```

Using JavaScript Fetch:
```javascript
const formData = new FormData();
formData.append('audio', audioFile);

fetch('http://localhost:5000/transcribe', {
  method: 'POST',
  body: formData
})
  .then(response => response.json())
  .then(data => console.log(data));
```

#### Response Format
```json
{
  "transcription": "The transcribed text appears here"
}
```

## Configuration

### Whisper Models

The application uses environment variables for configuration:

- `WHISPER_BASE_MODEL`: Sets the Whisper model to use (default: "base")

Available models (in order of increasing accuracy and resource usage):
- `tiny`: Fastest, lowest accuracy
- `base`: Good balance of speed and accuracy (default if not specified)
- `small`: Better accuracy, slower
- `medium`: High accuracy, requires more resources
- `large`: Best accuracy, highest resource usage

You can set the model in three ways:

1. In docker-compose.yml:
```yaml
environment:
  - WHISPER_BASE_MODEL=base
```

2. Environment variable:
```bash
export WHISPER_BASE_MODEL=small
python app.py
```

3. If not set, the application will default to "base" model

## Error Handling

The API will return appropriate HTTP status codes:
- 200: Successful transcription
- 400: No file uploaded or invalid request
- 500: Server error during transcription

## License

MIT
