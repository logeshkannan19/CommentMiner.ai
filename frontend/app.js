document.getElementById('analyze-btn').addEventListener('click', async () => {
    const url = document.getElementById('video-url').value;
    if (!url) return alert('Please paste a YouTube URL');

    const btn = document.getElementById('analyze-btn');
    btn.textContent = 'Analyzing...';
    btn.disabled = true;

    try {
        const response = await fetch('http://localhost:8000/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url })
        });

        if (!response.ok) throw new Error('Analysis failed');

        const data = await response.json();
        displayResults(data.insights);
    } catch (err) {
        alert('Error connecting to backend API');
    } finally {
        btn.textContent = 'Analyze';
        btn.disabled = false;
    }
});

function displayResults(insights) {
    document.getElementById('results').classList.remove('hidden');
    document.getElementById('ai-summary').textContent = insights.summary;
    
    const topicList = document.getElementById('topic-list');
    topicList.innerHTML = '';
    insights.topics.forEach(topic => {
        const li = document.createElement('li');
        li.textContent = topic;
        topicList.appendChild(li);
    });

    // Update sentiment bar
    const bars = document.querySelector('.sentiment-bar');
    bars.querySelector('.positive').style.width = `${insights.sentiment.positive}%`;
    bars.querySelector('.neutral').style.width = `${insights.sentiment.neutral}%`;
    bars.querySelector('.negative').style.width = `${insights.sentiment.negative}%`;
}
