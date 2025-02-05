import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import json
import streamlit as st
import numpy as np
from datetime import date
from datetime import datetime
today = str(date.today())

#######################
# Page configuration
st.set_page_config(
    page_title="Most In-Demand Data Science Skills",
    page_icon="📊",
    layout="wide")

alt.themes.enable("dark")

#######################
# Load data

path = '/content/drive/MyDrive/Set_Uni_Analytics/'
analytics_name = path + 'analytics' + today + '.csv'
soft_skills_name = path + 'soft_skills' + today + '.csv'
hard_skills_name = path + 'hard_skills' + today + '.csv'

with open(path + 'pie_chart_data.json', "r", encoding="utf-8") as f:
    pie_chart = json.load(f)

with open(path + 'donut_data.json', "r", encoding="utf-8") as f:
    donut_chart = json.load(f)

df_hard = pd.read_csv(hard_skills_name, index_col = False)
df_soft = pd.read_csv(soft_skills_name, index_col = False)
df = pd.read_csv(analytics_name, index_col = False)
length = df.shape[0]

#######################
# Plots
# Donut

def make_donut(input_response, input_text, input_color):
    if input_color == 'blue':
      chart_color = ['#29b5e8', '#155F7A']
    if input_color == 'green':
      chart_color = ['#27AE60', '#12783D']
    if input_color == 'orange':
      chart_color = ['#F39C12', '#875A12']
    if input_color == 'red':
      chart_color = ['#E74C3C', '#781F16']
    
    source = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100-input_response, input_response]
    })
    source_bg = pd.DataFrame({
      "Topic": ['', input_text],
      "% value": [100, 0]
    })
    
    plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          domain=[input_text, ''],
                          range=chart_color),
                      legend=None),
    ).properties(width=130, height=130)
    
    text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
    plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
      theta="% value",
      color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
    ).properties(width=130, height=130)
    return plot_bg + plot + text

# Pie
def make_pie(labels, values):
    # Enable dark theme
    plt.style.use("dark_background")
    # Create figure with dark background
    fig1, ax1 = plt.subplots(figsize=(2.5, 2.5), facecolor="#0e1117")
    # Define colors for contrast
    colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f", "green"]
    # Create pie chart with dark theme adjustments
    wedges, texts, autotexts = ax1.pie(
        values,
        labels=labels,
        autopct='%1.1f%%',
        shadow=True,
        startangle=90,
        colors=colors,
        textprops={"color": "white"})
    # Make sure text labels are readable
    for text in texts + autotexts:
        text.set_color("white")
    # Remove axis background
    ax1.set_facecolor("#0e1117")
    # Keep aspect ratio circular
    ax1.axis("equal")
    st.pyplot(fig1)

#######################
# Dashboard Main Panel
col = st.columns((1.5, 4, 2.5), gap='medium')
with col[0]:
    #Current date info
    current_date = datetime.now().strftime("%B %d, %Y")
    st.markdown(
    f"""
    <div style="
        background-color:#4CAF50;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 24px;
        font-weight: bold;">
        Report for {current_date}
    </div>
    """, unsafe_allow_html=True)

    ed_required = round(donut_chart['Higher_education']/length * 100,1)
    exp_required = round(donut_chart['Just_experience']/length * 100,1)
    both_required = round(donut_chart['Both_required']/length * 100,1)

    donut_chart_higher_ed = make_donut(ed_required, 'Higher education required', 'green')
    donut_chart_exp = make_donut(exp_required, 'Experience required', 'blue')
    donut_chart_higher_exp = make_donut(both_required, 'Education & Experince required', 'orange')

    migrations_col = st.columns((0.2, 1, 0.2))
    with migrations_col[1]:
        st.markdown('#### Edu & Exp')
        st.write('Higher education required')
        st.altair_chart(donut_chart_higher_ed)
        st.write('Experience required')
        st.altair_chart(donut_chart_exp)
        st.write('Education & Experience required')
        st.altair_chart(donut_chart_higher_exp)

with col[1]:
    st.markdown('#### Popularity of Job Titles in the Market')
    # Extract labels and values
    labels = list(pie_chart.keys())
    values = list(pie_chart.values())
    # Generate Pie Chart
    make_pie(labels, values)
    st.markdown('#### Top-20 Most Popular Technologies')
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df_hard["Technologies"][:20], df_hard["Number"][:20], color="indianred")
    # Rotate x-axis labels for readability
    ax.set_xticklabels(df_hard["Technologies"][:20], rotation=45, ha="right")
    # Labels
    ax.set_xlabel("Technologies")
    ax.set_ylabel("Popularity Score")
    ax.set_title("Top-20 Most Popular Technologies")
    plt.show()
    st.pyplot(fig)

with col[2]:
    st.markdown('#### Soft skills')
    st.dataframe(df_soft[:10],
                column_order=("Soft_skills", "Number"),
                hide_index=True,
                width=None,
                column_config={
                  "Soft_skills": st.column_config.TextColumn(
                      "Soft_skills",
                  ),
                  "Number": st.column_config.ProgressColumn(
                      "Number",
                      format="%f",
                      min_value=0,
                      max_value=max(df_soft["Number"]),
                    )}
                )

    with st.expander('About', expanded=True):
        st.write('''Scraped from https://djinni.co/''')