import pytest
from unittest.mock import AsyncMock, patch
from services.ai import analyze_comments
from models.schemas import AnalysisResult

@pytest.mark.asyncio
@patch("services.ai.client.chat.completions.create")
async def test_analyze_comments_empty(mock_create):
    # Test with empty comments list
    result = await analyze_comments([])
    assert isinstance(result, AnalysisResult)
    assert result.sentiment["positive"] == 0
    assert not result.topics

@pytest.mark.asyncio
@patch("services.ai.client.chat.completions.create")
async def test_analyze_comments_mock(mock_create):
    # Mock OpenAI response
    mock_response = AsyncMock()
    mock_response.choices = [
        AsyncMock(message=AsyncMock(content='{"sentiment": {"positive": 60, "neutral": 30, "negative": 10}, "topics": ["Battery"], "complaints": [], "feature_requests": [], "summary": "Good battery life."}'))
    ]
    mock_create.return_value = mock_response

    result = await analyze_comments(["Great battery!"])
    assert result.sentiment["positive"] == 60
    assert "Battery" in result.topics
    assert result.summary == "Good battery life."
