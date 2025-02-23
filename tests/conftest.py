import pytest
import os
import sys

# Add the parent directory to the path so we can import the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(autouse=True)
def setup_test_env():
    # Store original environment
    original_env = os.environ.copy()

    # Set up test environment variables
    os.environ['WHISPER_BASE_MODEL'] = 'base'

    yield

    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)
