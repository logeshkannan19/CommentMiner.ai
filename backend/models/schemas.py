from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class SentimentScore(BaseModel):
    positive: float = Field(..., ge=0, le=100)
    neutral: float = Field(..., ge=0, le=100)
    negative: float = Field(..., ge=0, le=100)

class AnalysisResult(BaseModel):
    sentiment: Dict[str, float]
    topics: List[str]
    complaints: List[str]
    feature_requests: List[str]
    summary: str
    processed_at: datetime = Field(default_factory=datetime.utcnow)

class CommentData(BaseModel):
    text: str
    author: str
    timestamp: datetime
    likes: int

class VideoAnalysisRequest(BaseModel):
    url: str

class VideoAnalysisResponse(BaseModel):
    video_id: str
    title: Optional[str] = None
    insights: AnalysisResult
