# News_search_agent

<h3> Objective:</h3>
<p>Create a news search agent using any large language model and a web search/scraping tool of your choice. The agent should be capable of providing the latest news, along with links to relevant articles, based on the user's search query.</p>

<h3>Requirements:</h3>
  
- Use any large language model of your choice.
- Incorporate a web search/scraping tool for obtaining news articles.
- Execute the code in a Jupyter notebook or any IDE of your preference.
- Attach the code file along with screenshots demonstrating the outputs.


<h3>Environment Details:</h3>

- <b>IDE</b>: VS Code, Python environment, terminal output
- <b>Libraries</b>: Streamlit, Serp Api, GoogleSearch, Json (output format)
- <b>Deployment</b>: Streamlit

<h3>Methodology:</h3>
  
- <b>Main code functions</b>: get_news_results() takes a keyword and an optional max_pages parameter. It uses the Serp api library to perform a Google search for news related to the given keyword. The function fetches results and extracts relevant information like title, link, source, date, snippet, and thumbnail. The loop continues until either 10 pages are fetched (default value of max_pages) or until there are no more pages.
- <b>Deployment</b>: The st.json(results) line displays the fetched news results in a JSON format on the web page. When the code is run on Streamlit, it provides a simple web interface where users can input a news keyword, click the "Search" button, and see the related news results displayed on the page.

<h3> Output</h3>
![GitHub Logo](https://github.com/Srijan0519/News_search_agent/blob/main/Screenshots/streamlit%20deployed.jpg)
![GitHub Logo](https://github.com/Srijan0519/News_search_agent/blob/main/Screenshots/terminal%20ss.jpg)

