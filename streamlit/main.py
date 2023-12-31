import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

add_page_title() # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("welcome.py", "welcome", "🏠"),
        Page("ui.py", "향수찾기", ":books:"),
        Page("bard.py", "카테고리향챗봇", ":books:")
    ]
)