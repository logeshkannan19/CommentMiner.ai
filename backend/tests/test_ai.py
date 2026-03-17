import pytest
from unittest.mock import AsyncMock, patch
from services.ai import analyze_comments
from models.schemas import AnalysisResult

@pytest.mark.asyncio
@patch("services.ai.get_ai_client")
async def test_analyze_comments_empty(mock_get_client, mock_create):
    # Setup mock
    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client
    mock_client.chat.completions.create = mock_create
    
    # Test with empty comments list
    result = await analyze_comments([])
    assert isinstance(result, AnalysisResult)
    assert result.sentiment["positive"] == 0
    assert not result.topics

@pytest.mark.asyncio
@patch("services.ai.get_ai_client")
async def test_analyze_comments_mock(mock_get_client, mock_create):
    # Setup mock
    mock_client = AsyncMock()
    mock_get_client.return_value = mock_client
    mock_client.chat.completions.create = mock_create
    
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
