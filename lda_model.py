# ------------------------------------------------------------------------------------------------------------------------
# LDA MODEL
# ------------------------------------------------------------------------------------------------------------------------
from gensim import corpora, models, similarities
from get_all_comments_pipelines import get_all_hot_comments, get_all_top_comments, get_all_controversial_comments, get_all_gilded_comments, get_all_rising_comments
from sandbox import subreddit, n_posts
import numpy as np

all_comments_duo = get_all_hot_comments(subreddit, n_posts)

texts = list(all_comments_duo)
list_texts = [[d] for d in texts]

dictionary = corpora.Dictionary(list_texts)
corpus = [dictionary.doc2bow(text) for text in list_texts]
print(corpus)

# lda model
num_topics = 5
update_every = 5
chunksize = 10000
passes = 100
lda = models.LdaModel(corpus, num_topics=num_topics, 
                            id2word=dictionary, 
                            update_every=update_every, 
                            chunksize=chunksize, 
                            passes=passes)

# show topics
lda.show_topics()

# top N words in each topic
num_words = 25
topics_matrix = lda.show_topics(formatted=False, num_words=num_words)
topics_matrix = np.array(topics_matrix, dtype=object)

topic_words = topics_matrix[:,1]
for i in topic_words:
    print([str(word) for word in i])
    print()