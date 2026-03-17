import pytest
from services.youtube import extract_video_id

def test_extract_video_id_standard():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_shortened():
    url = "https://youtu.be/dQw4w9WgXcQ"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_share():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=share"
    assert extract_video_id(url) == "dQw4w9WgXcQ"

def test_extract_video_id_invalid():
    with pytest.raises(ValueError, match="Invalid YouTube URL"):
        extract_video_id("https://google.com")
