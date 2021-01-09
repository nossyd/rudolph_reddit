import streamlit as st
import altair as alt
from get_all_comments_pipelines import get_all_hot_comments, get_all_top_comments, get_all_controversial_comments, get_all_gilded_comments, get_all_rising_comments
from plots import plot_freqdist_freq, plot_freqdist_freq_bar, freq_for_bar
from nltk import FreqDist
from get_subreddits_pipeline import subreddit_list

#------------------------------------------------------------------------------------------------------------------------
#               LAYOUT
#------------------------------------------------------------------------------------------------------------------------

st.set_page_config(layout="wide")
st.title("What Is Reddit Saying?")
st.markdown("""
This app performs NLP on comments of posts from the popular website, Reddit.com then displays the most used tokens.
* **Python libraries:** pandas, streamlit, numpy, altair, praw, nltk
* **Data source:** [Reddit.com](https://www.Reddit.com/).
""")

st.sidebar.header('Filters')
list_comment_type = ["Hot","Top","Controversial","Gilded","Rising"]
comment_type = st.sidebar.selectbox('Type of Comments', list_comment_type)
subreddit = st.sidebar.selectbox('Subreddit', subreddit_list)
n_posts = st.sidebar.slider("Number of Posts", 0, 100, 15)
n_tokens = st.sidebar.slider("Number of Tokens", 0, 100, 50)


#------------------------------------------------------------------------------------------------------------------------
#               DATA
#------------------------------------------------------------------------------------------------------------------------

@st.cache
def load_data(subreddit_filter, n_posts, n_tokens=50, comment_type=comment_type):
    if comment_type == "Hot":
        all_comments = get_all_hot_comments(subreddit, n_posts)
    
    if comment_type == "Top":
        all_comments = get_all_top_comments(subreddit, n_posts)    

    if comment_type == "Controversial":
        all_comments = get_all_controversial_comments(subreddit, n_posts)

    if comment_type == "Gilded":
        all_comments = get_all_gilded_comments(subreddit, n_posts)

    else:
        all_comments = get_all_rising_comments(subreddit, n_posts)

    freq_dist_pos = FreqDist(all_comments)
    df = freq_for_bar(freq_dist_pos, max_num=n_tokens)
    df.sort_values(by=['Frequency'], ascending=False)
    df.reset_index()
    max_domain = df['Frequency'].max()
    return df, max_domain

df, max_domain = load_data(subreddit_filter,n_posts,n_tokens)



#------------------------------------------------------------------------------------------------------------------------
#               VIZS
#------------------------------------------------------------------------------------------------------------------------

col1, col2 = st.beta_columns((1,1))
col1.write(alt.Chart(df).mark_bar().encode(
    x=alt.X('Frequency',axis=alt.Axis(format='%')),
    y=alt.Y('Words', sort='-x'),
    color=alt.Color('Frequency', scale=alt.Scale(scheme='purples', domain=[0, max_domain]))
)
.properties(
    width=500,
    height=1500
).configure_axis(
    labelFontSize=13,
    titleFontSize=15
))
col2.table(df)