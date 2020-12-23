from nltk import FreqDist
from nltk.draw import dispersion_plot
import pandas as pd
import time
import matplotlib.pyplot as plt

from get_all_comments_pipelines import get_all_hot_comments, get_all_top_comments, get_all_controversial_comments, get_all_gilded_comments, get_all_rising_comments
from plots import plot_freqdist_freq, plot_freqdist_freq_bar

from nltk.text import Text
from wordcloud import WordCloud

subreddit = "nfl"
n_posts = 50

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
plot_freqdist_freq_bar(freq_dist_pos, title="Frequency of top 50 tokens -- Hot  /r/all posts")
#plot_freqdist_freq(freq_dist_pos, 50, title="Frequency of top 50 tokens -- Top 100 /r/WSB posts")


# ------------------------------------------------------------------------------------------------------------------------
# DISPERSION PLOTS
# ------------------------------------------------------------------------------------------------------------------------
# text = Text(all_comments)
# plt.figure(figsize=(16,5))
# topics = ['soccer', 'football', 'arsenal', 'liverpool', 'shit']
# text.dispersion_plot(topics)


# ------------------------------------------------------------------------------------------------------------------------
# WORDCLOUD
# ------------------------------------------------------------------------------------------------------------------------
#texts = Text(all_comments)
# comments = " ".join(comment for comment in texts)
# wordcloud = WordCloud(max_font_size=60, max_words=100, background_color="white").generate(comments)
# plt.figure(figsize=(15,7))
# # plot wordcloud in matplotlib
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.axis("off")
# plt.show()


# ------------------------------------------------------------------------------------------------------------------------
# LDA MODEL
# ------------------------------------------------------------------------------------------------------------------------
from gensim import corpora, models, similarities 
import numpy as np

texts = list(all_comments_duo)
list_texts = [[d] for d in texts]

dictionary = corpora.Dictionary(list_texts)
corpus = [dictionary.doc2bow(text) for text in list_texts]
print(corpus)


# lda model
lda = models.LdaModel(corpus, num_topics=5, 
                            id2word=dictionary, 
                            update_every=5, 
                            chunksize=10000, 
                            passes=100)

# show topics
lda.show_topics()

# top 25 words in each topic
topics_matrix = lda.show_topics(formatted=False, num_words=25)
topics_matrix = np.array(topics_matrix, dtype=object)

topic_words = topics_matrix[:,1]
for i in topic_words:
    print([str(word) for word in i])
    print()


