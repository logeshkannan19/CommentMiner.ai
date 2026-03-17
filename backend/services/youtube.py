import re
from typing import List, Optional
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def extract_video_id(url: str) -> str:
    """
    Pulls the unique Video ID from a YouTube URL.
    Supports standard, shortened, and shared URL formats.
    """
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Invalid YouTube URL")

async def get_video_comments(video_id: str, max_results: int = 100) -> List[str]:
    """
    Fetches raw comment text for a video using the YouTube Data API.
    If no API key is set, returns a few mock comments for local testing.
    """
    if not YOUTUBE_API_KEY:
        # Fallback/Mock for testing if no key is provided
        return ["Great product!", "I wish it had better battery life.", "The UI is a bit confusing."]
        
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    
    try:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=max_results,
            textFormat="plainText"
        )
        response = request.execute()
        
        comments = []
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
        return comments
    except Exception as e:
        print(f"Error fetching comments: {e}")
        return []
