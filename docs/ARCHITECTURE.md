# How CommentMiner Works

CommentMiner is built with a simple goal: turn thousands of messy comments into clear, high-level product intelligence. Here's a look under the hood.

## The Logic Flow

The system operates as a linear pipeline, moving from raw URL to analyzed insight:

1.  **Input & Validation**: The user provides a YouTube URL. Our backend validates the format and pulls the unique `Video ID`.
2.  **Extraction**: Using the official YouTube Data API v3, we pull the most recent comment threads. We focus on top-level comments to capture the most significant user feedback.
3.  **The AI Layer**: This is where the magic happens. We feed the cleaned comments into OpenAI's `gpt-4o-mini`. We use a highly specific system prompt to force the AI to think like a product manager—categorizing sentiment, identifying specific feature requests, and spotting recurring bugs.
4.  **Presentation**: The resulting structured JSON is sent back to our frontend, where we visualize the data using a clean, minimal dashboard to help you make decisions faster.

## The Tech Stack

We chose these tools for their reliability and developer experience:

-   **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python). It’s fast, type-safe, and perfect for handling asynchronous AI calls.
-   **Frontend**: Vanilla HTML/CSS/JS. No bloated frameworks here—just clean, modern code that loads instantly.
-   **Intelligence**: [OpenAI GPT-4o-mini](https://openai.com/). High intelligence with low latency.
-   **Data Source**: [YouTube Data API](https://developers.google.com/youtube/v3). The source of truth for all public feedback.
