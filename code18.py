from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io

import plotly.express as px
with st.echo("below"):
    from st_pages import Page, add_page_title, show_pages

    show_pages(
        [
            Page("code13.py", "Home", "🏠"),
            Page("code12.py", "2023 내신 파헤치기", ":books:"),
            Page("code15.py", "고민 상담소", "📖"),
            Page("code16.py", "동아리", "✏️"),
            Page("code17.py", "백석고 실체", "🧰"),
        ]
    )

