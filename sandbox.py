
# from nltk.text import Text
# from plots import plot_freqdist_freq, plot_freqdist_freq_bar, freq_for_bar

# ------------------------------------------------------------------------------------------------------------------------
# DISPERSION PLOTS
# ------------------------------------------------------------------------------------------------------------------------
# from nltk.draw import dispersion_plot

# all comments is in rudolph.py
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



# ------------------------------------------------------------------------------------------------------------------------
# FREQUENCY PLOTS
# ------------------------------------------------------------------------------------------------------------------------
#df = freq_for_bar(freq_dist_pos, max_num=50)
#plot_freqdist_freq_bar(df, title="Frequency of top 50 tokens -- Hot  /r/NBA posts")
#plot_freqdist_freq(freq_dist_pos, 50, title="Frequency of top 50 tokens -- Top 100 /r/WSB posts")