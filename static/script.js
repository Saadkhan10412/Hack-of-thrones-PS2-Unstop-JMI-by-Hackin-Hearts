function showLoading(show){
    const loading = document.getElementById('loading');
    loading.style.display = show ? 'block':'none';
}

function showMessage(message, type='info'){
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML=`<div class="${type==='error'?'error':'demo-notice'}">${message}</div>`;
}

function clearMessages(){ document.getElementById('messages').innerHTML=''; }

async function scrapeNews(){
    clearMessages();
    showLoading(true);

    try{
        const response = await fetch('/api/scrape', { method:'POST', headers:{ 'Content-Type':'application/json' } });
        const data = await response.json();
        displayResults(data);
    } catch(error){
        showMessage('Error scraping news: '+error.message,'error');
    } finally{ showLoading(false); }
}

function displayResults(data){
    const resultsDiv = document.getElementById('results');
    const statsDiv = document.getElementById('stats');

    if(!data.success){ showMessage('Error: '+data.error,'error'); return; }

    // Stats
    if(data.stats){
        statsDiv.style.display='flex';
        statsDiv.innerHTML=`
            <div class="stat-card"><span class="stat-number">${data.stats.total_articles}</span><span class="stat-label">Articles</span></div>
            <div class="stat-card"><span class="stat-number">${data.stats.journalists_found}</span><span class="stat-label">Journalists</span></div>
            <div class="stat-card"><span class="stat-number">${data.stats.outlets_covered}</span><span class="stat-label">Outlets</span></div>
            <div class="stat-card"><span class="stat-number">${data.stats.timestamp.split(' ')[0]}</span><span class="stat-label">Last Updated</span></div>
        `;
    }

    // Articles
    if(data.articles && data.articles.length>0){
        resultsDiv.style.opacity=0;
        resultsDiv.innerHTML = data.articles.map(article=>`
            <div class="article-card">
                <div class="article-title">${article.title}</div>
                <div class="article-meta">
                    <span class="journalist">👤 ${article.journalist}</span>
                    <span class="outlet">🏢 ${article.outlet}</span>
                    <span class="date">📅 ${article.date}</span>
                </div>
                <div class="content-preview">${article.content_preview}</div>
                ${article.url!=='#'?`<a href="${article.url}" target="_blank" class="article-link">Read full article →</a>`:''}
            </div>
        `).join('');
        setTimeout(()=>{ resultsDiv.style.opacity=1; }, 50);
    } else { resultsDiv.innerHTML='<p>No articles found.</p>'; }
}
