# app.py
import streamlit as st
from serpapi import GoogleSearch
import json

def get_news_results(keyword, max_pages=10):
    params = {
        "api_key": "f9186e8664a543ac319b4cbdeb0e991229ee7a90988f0b1328b02d81624489c3",
        "engine": "google",
        "q": keyword,
        "location": "Austin, Texas, United States",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
        "tbm": "nws"
    }

    search = GoogleSearch(params)
    pages = search.pagination()
    news_results_list = []

    for page_num, page in enumerate(pages, start=1):
        for news_result in page["news_results"]:
            news_results_list.append({
                "position": news_result["position"],
                "Title": news_result["title"],
                "link": news_result["link"],
                "source": news_result["source"],
                "date_published": news_result["date"],
                "snippet": news_result["snippet"],
                "thumbnail": news_result["thumbnail"]
            })

        if page_num >= max_pages:
            break

    return news_results_list

st.title("News Search App")

# Get user input for the news keyword
keyword = st.text_input("Enter a news keyword:")

if st.button("Search"):
    if keyword:
        st.text(f"Searching for news related to: {keyword}")
        
        # Fetch news results
        results = get_news_results(keyword)

        # Display results
        st.json(results)
    else:
        st.warning("Please enter a news keyword.")
