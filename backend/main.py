from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.schemas import VideoAnalysisRequest, VideoAnalysisResponse
from services.youtube import extract_video_id, get_video_comments
from services.ai import analyze_comments

app = FastAPI(title="CommentMiner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "CommentMiner API is running"}

@app.post("/analyze", response_model=VideoAnalysisResponse)
async def analyze_video(request: VideoAnalysisRequest):
    try:
        video_id = extract_video_id(request.url)
        comments = await get_video_comments(video_id)
        
        if not comments:
            raise HTTPException(status_code=404, detail="No comments found for this video")
            
        insights = await analyze_comments(comments)
        
        return VideoAnalysisResponse(
            video_id=video_id,
            insights=insights
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
