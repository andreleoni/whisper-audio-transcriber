import pytest
import os
from app import app, get_model_name
import io
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_model_name_with_env():
    with patch.dict(os.environ, {'WHISPER_BASE_MODEL': 'small'}):
        assert get_model_name() == 'small'

def test_get_model_name_without_env():
    with patch.dict(os.environ, clear=True):
        assert get_model_name() == 'base'

def test_transcribe_success(client):
    # Create a mock audio file
    data = {}
    data['audio'] = (io.BytesIO(b"mock audio content"), 'test.mp3')

    response = client.post('/transcribe',
                         data=data,
                         content_type='multipart/form-data')

    assert response.status_code == 200
    assert 'transcription' in response.json

def test_transcribe_no_file(client):
    response = client.post('/transcribe',
                         data={},
                         content_type='multipart/form-data')

    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'No file uploaded'

def test_transcribe_empty_file(client):
    data = {}
    data['audio'] = (io.BytesIO(b""), 'empty.mp3')

    response = client.post('/transcribe',
                         data=data,
                         content_type='multipart/form-data')

    assert response.status_code == 400
