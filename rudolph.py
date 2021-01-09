import streamlit as st
import altair as alt
from get_all_comments_pipelines import get_all_hot_comments, get_all_top_comments, get_all_controversial_comments, get_all_gilded_comments, get_all_rising_comments
from plots import plot_freqdist_freq, plot_freqdist_freq_bar, freq_for_bar
from sandbox import freq_dist_pos

df = freq_for_bar(freq_dist_pos, max_num=50)
df.sort_values(by=['Frequency'], ascending=False)
df.reset_index()
max_domain = df['Frequency'].max()

st.title("What Is Reddit Saying?")

st.markdown("""
This app performs NLP on comments of posts from the popular website, Reddit.com then displays the most used tokens.
* **Python libraries:** pandas, streamlit, numpy, altair, praw
* **Data source:** [Reddit.com](https://www.Reddit.com/).
""")
col1, col2 = st.beta_columns((1.5,1))
col1.write(alt.Chart(df).mark_bar().encode(
    x=alt.X('Frequency',axis=alt.Axis(format='%')),
    y=alt.Y('Words', sort='-x'),
    color=alt.Color('Frequency', scale=alt.Scale(scheme='purples', domain=[0, max_domain]))
)
.properties(
    width=750,
    height=1500
).configure_axis(
    labelFontSize=13,
    titleFontSize=15
))
col2.table(df)