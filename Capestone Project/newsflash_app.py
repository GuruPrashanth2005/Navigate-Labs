import streamlit as st
import requests
from bs4 import BeautifulSoup
import datetime
import re

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="NewsFlash – Live Headlines",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── News Sources ──────────────────────────────────────────────────────────────
NEWS_SOURCES = {
    "🌍 BBC World News":    {"url": "https://feeds.bbci.co.uk/news/rss.xml",                         "category": "World"},
    "💻 BBC Technology":    {"url": "https://feeds.bbci.co.uk/news/technology/rss.xml",              "category": "Technology"},
    "💰 BBC Business":      {"url": "https://feeds.bbci.co.uk/news/business/rss.xml",                "category": "Business"},
    "🔬 BBC Science":       {"url": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml", "category": "Science"},
    "⚽ BBC Sport":         {"url": "https://feeds.bbci.co.uk/sport/rss.xml",                        "category": "Sports"},
    "🏥 BBC Health":        {"url": "https://feeds.bbci.co.uk/news/health/rss.xml",                  "category": "Health"},
    "🎭 BBC Entertainment": {"url": "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",  "category": "Entertainment"},
}

HEADERS = {"User-Agent": "Mozilla/5.0"}

# ── Helpers ───────────────────────────────────────────────────────────────────
def clean_text(text):
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:250] + "…" if len(text) > 250 else text

def fetch_rss(url, max_items=10):
    articles = []
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        # Use html.parser instead of xml — no lxml needed!
        soup = BeautifulSoup(r.content, "html.parser")
        items = soup.find_all("item")[:max_items]
        for item in items:
            title_tag = item.find("title")
            link_tag  = item.find("link")
            title  = clean_text(title_tag.get_text() if title_tag else "")
            link   = link_tag.get_text().strip() if link_tag else "#"
            summary = ""
            for tag in ["description", "summary"]:
                node = item.find(tag)
                if node and node.get_text().strip():
                    summary = clean_text(node.get_text())
                    break
            date_node = item.find("pubdate") or item.find("published")
            date = date_node.get_text().strip()[:25] if date_node else ""
            if title:
                articles.append({"title": title, "link": link, "summary": summary, "date": date})
    except Exception:
        pass
    return articles

def search_articles(articles, query):
    q = query.lower()
    return [a for a in articles if q in a["title"].lower() or q in a["summary"].lower()]

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📰 NewsFlash")
    st.caption("Real-time headline scraper — no API key needed")
    st.divider()

    selected_sources = st.multiselect(
        "📡 News Sources",
        list(NEWS_SOURCES.keys()),
        default=["🌍 BBC World News", "💻 BBC Technology", "💰 BBC Business"],
    )

    max_per_source = st.slider("Headlines per source", 3, 15, 6)
    search_query   = st.text_input("🔍 Search", placeholder="e.g. AI, economy, health…")

    st.divider()
    st.button("🔄 Refresh Headlines", use_container_width=True)
    st.divider()
    st.caption(f"🕐 {datetime.datetime.now().strftime('%d %b %Y, %H:%M')}")
    st.caption("Sources: BBC RSS Feeds")

# ── Fetch ─────────────────────────────────────────────────────────────────────
if not selected_sources:
    st.warning("👈 Select at least one source from the sidebar.")
    st.stop()

all_articles  = []
source_counts = {}

with st.spinner("📡 Fetching live headlines…"):
    for src_name in selected_sources:
        src  = NEWS_SOURCES[src_name]
        arts = fetch_rss(src["url"], max_items=max_per_source)
        for a in arts:
            a["source"]   = src_name
            a["category"] = src["category"]
        all_articles.extend(arts)
        source_counts[src_name] = len(arts)

filtered = search_articles(all_articles, search_query) if search_query else all_articles

# ── Header ────────────────────────────────────────────────────────────────────
st.title("📰 NewsFlash")
st.subheader("Live Headlines Dashboard")
st.divider()

# ── Metrics ───────────────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
m1.metric("📄 Total Headlines", len(filtered))
m2.metric("📡 Sources Active",  len(selected_sources))
m3.metric("🗂️ Categories",     len(set(a["category"] for a in filtered)))
m4.metric("🕐 Last Updated",   datetime.datetime.now().strftime("%H:%M"))
st.divider()

if not filtered:
    st.info(f"No headlines found for **'{search_query}'**. Try a different keyword or refresh.")
    st.stop()

# ── Top Story ─────────────────────────────────────────────────────────────────
st.subheader("⭐ Top Story")
top = filtered[0]
with st.container(border=True):
    st.markdown(f"### [{top['title']}]({top['link']})")
    if top["summary"]:
        st.write(top["summary"])
    c1, c2 = st.columns(2)
    c1.caption(f"📰 {top['source']}")
    c2.caption(f"🕐 {top['date'] or 'Just now'}")
    st.link_button("Read Full Story →", top["link"], use_container_width=True)

st.divider()

# ── Category Tabs ─────────────────────────────────────────────────────────────
categories = sorted(set(a["category"] for a in filtered))
tabs = st.tabs(["📋 All"] + categories)

def render_articles(articles):
    if not articles:
        st.info("No articles in this category.")
        return
    for i in range(0, len(articles), 2):
        col1, col2 = st.columns(2)
        for col, article in zip([col1, col2], articles[i:i+2]):
            with col:
                with st.container(border=True):
                    st.markdown(f"**[{article['title']}]({article['link']})**")
                    if article["summary"]:
                        st.caption(article["summary"][:150] + "…" if len(article["summary"]) > 150 else article["summary"])
                    st.caption(f"📰 {article['source']}  ·  🏷️ {article['category']}  ·  🕐 {article['date'][:20] if article['date'] else 'Recent'}")
                    st.link_button("Read →", article["link"], use_container_width=True)

with tabs[0]:
    render_articles(filtered[1:])

for tab, cat in zip(tabs[1:], categories):
    with tab:
        render_articles([a for a in filtered if a["category"] == cat])

st.divider()

# ── Source Breakdown ──────────────────────────────────────────────────────────
st.subheader("📊 Source Breakdown")
cols = st.columns(len(selected_sources))
for col, src_name in zip(cols, selected_sources):
    col.metric(src_name, source_counts.get(src_name, 0), "articles")

st.divider()
st.caption("📰 NewsFlash Capstone Project · Built with Python & Streamlit · BBC RSS Feeds · No API Key Required")