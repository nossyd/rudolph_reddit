from nltk import FreqDist
import pandas as pd
import time
import matplotlib.pyplot as plt

from get_all_comments_pipelines import get_all_hot_comments, get_all_top_comments, get_all_controversial_comments, get_all_gilded_comments, get_all_rising_comments
from plots import plot_freqdist_freq, plot_freqdist_freq_bar, freq_for_bar


subreddit = "soccer"
n_posts = 1

start = time.time()
print("------------------------------------------------------------------------------------------------------------------------")
print("Gathering comments")
print("------------------------------------------------------------------------------------------------------------------------")
all_comments = get_all_hot_comments(subreddit, n_posts)
all_comments_duo = get_all_hot_comments(subreddit, n_posts)
print("------------------------------------------------------------------------------------------------------------------------")
print("Obtained comments")
end_comments = time.time()
mins_elapsed_comments = (end_comments - start)
print("time elapsed gathering comments: ", mins_elapsed_comments, " secs")
print("------------------------------------------------------------------------------------------------------------------------")
print(" ")
print("------------------------------------------------------------------------------------------------------------------------")
print("Gathering most common comments")
print("------------------------------------------------------------------------------------------------------------------------")
freq_dist_pos = FreqDist(all_comments)
end_freq_dist = time.time()
mins_elapsed_freq_dist = (end_freq_dist - end_comments)
print("time elapsed calculating frequency of comments: ", mins_elapsed_freq_dist, " secs")
print("------------------------------------------------------------------------------------------------------------------------")
print("Obtained most common comments")
print("------------------------------------------------------------------------------------------------------------------------")
print(freq_dist_pos.most_common(50))


# ------------------------------------------------------------------------------------------------------------------------
# FREQUENCY PLOTS
# ------------------------------------------------------------------------------------------------------------------------
#df = freq_for_bar(freq_dist_pos, max_num=50)
#plot_freqdist_freq_bar(df, title="Frequency of top 50 tokens -- Hot  /r/NBA posts")
#plot_freqdist_freq(freq_dist_pos, 50, title="Frequency of top 50 tokens -- Top 100 /r/WSB posts")



# from nltk.text import Text

# ------------------------------------------------------------------------------------------------------------------------
# DISPERSION PLOTS
# ------------------------------------------------------------------------------------------------------------------------
# from nltk.draw import dispersion_plot

# text = Text(all_comments)
# plt.figure(figsize=(16,5))
# topics = ['soccer', 'football', 'arsenal', 'liverpool', 'shit']
# text.dispersion_plot(topics)


# ------------------------------------------------------------------------------------------------------------------------
# WORDCLOUD
# ------------------------------------------------------------------------------------------------------------------------
#from wordcloud import WordCloud

#texts = Text(all_comments)
# comments = " ".join(comment for comment in texts)
# wordcloud = WordCloud(max_font_size=60, max_words=100, background_color="white").generate(comments)
# plt.figure(figsize=(15,7))
# # plot wordcloud in matplotlib
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()