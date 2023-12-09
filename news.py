import streamlit as st
import feedparser

def fetch_feed(url):
    feed = feedparser.parse(url)
    return feed

st.title('Newspaper Headlines')

rss_feeds = [
    'http://rss.cnn.com/rss/cnn_topstories.rss',
    'https://archive.nytimes.com/www.nytimes.com/services/xml/rss/index.html',
    'https://www.abc.net.au/news/rural/rss/',
    'https://www.theguardian.com/help/feeds',
    'https://www.wired.com/about/rss_feeds/',
    'https://thediplomat.com/tag/rss/',
    'https://globalnews.ca/feed',
    'https://torontosun.com/feed',
    'https://www.themoscowtimes.com/page/rss',
    'http://blogs.wsj.com/indiarealtime/feed/',
    'https://www.livemint.com/rss',
    'https://timesofindia.indiatimes.com/rss.cms'
]

for rss_feed in rss_feeds:
    feed = fetch_feed(rss_feed)
    st.subheader(f'Headlines from {feed.feed.title}')
    for entry in feed.entries:
        st.write(entry.title)
