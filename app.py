from flask import Flask, render_template, jsonify, request
import scraper
import json
from datetime import datetime
import os

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/scrape', methods=['POST'])
def scrape_news():
    try:
        articles = scraper.scrape_all_sites()
        journalists = set()
        outlets = set()
        for article in articles:
            if article['journalist'] and article['journalist'] != 'Unknown':
                journalists.add(article['journalist'])
            outlets.add(article['outlet'])
        journalist_count = len(journalists)
        outlet_count = len(outlets)
        return jsonify({
            'success': True,
            'articles': articles,
            'stats': {
                'total_articles': len(articles),
                'journalists_found': journalist_count,
                'outlets_covered': outlet_count,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})


@app.route('/api/demo')
def demo_data():
    """Provide demo data if scraping fails"""
    demo_articles = [
        {
            'title': 'Climate Change Summit Concludes with New Agreements',
            'journalist': 'Sarah Chen',
            'outlet': 'BBC News',
            'date': '2025-10-24',
            'url': '#',
            'content_preview': 'World leaders agree on ambitious new climate targets during the international summit...'
        },
        {
            'title': 'Tech Innovation Revolutionizes Healthcare Diagnostics',
            'journalist': 'Mike Johnson',
            'outlet': 'CNN',
            'date': '2025-10-24',
            'url': '#',
            'content_preview': 'AI-powered diagnostic tools show promising results in early disease detection...'
        },
        {
            'title': 'Local Economy Shows Strong Growth in Quarterly Reports',
            'journalist': 'Priya Sharma',
            'outlet': 'Times of India',
            'date': '2025-10-23',
            'url': '#',
            'content_preview': 'Latest economic indicators suggest positive trends in the local market...'
        },
        {
            'title': 'Breakthrough in Renewable Energy Storage Solutions',
            'journalist': 'David Kim',
            'outlet': 'Tech News Daily',
            'date': '2025-10-23',
            'url': '#',
            'content_preview': 'New battery technology promises to solve key challenges in renewable energy...'
        },
        {
            'title': 'Sports Championship Concludes with Historic Victory',
            'journalist': 'Maria Garcia',
            'outlet': 'Sports Network',
            'date': '2025-10-22',
            'url': '#',
            'content_preview': 'Underdog team makes surprising comeback in the final moments of the tournament...'
        }
    ]

    return jsonify({
        'success': True,
        'articles': demo_articles,
        'stats': {
            'total_articles': len(demo_articles),
            'journalists_found': 5,
            'outlets_covered': 5,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        'demo': True
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)