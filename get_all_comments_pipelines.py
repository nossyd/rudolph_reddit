from api_test import reddit
from nltk import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import re, string
import itertools as it
import string


#------------------------------------------------------------------------------------------------------------------------
#               GET ALL WORDS FCN
#------------------------------------------------------------------------------------------------------------------------
def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


#------------------------------------------------------------------------------------------------------------------------
#               REMOVE TOKEN NOISE FCN
#------------------------------------------------------------------------------------------------------------------------
def remove_noise(comment_tokens, stop_words = ()):
    cleaned_tokens = []

    for token, tag in pos_tag(comment_tokens):
        token = re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|"\
                       "(?:%[0-9a-fA-F][0-9a-fA-F]))+","", token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        token = token.translate(token.maketrans("","", string.punctuation))
        token = re.sub('”','', token)
        token = re.sub(r"(?<!\\)\\n|\n", " ", token)
        token = re.sub("though", "tho", token)
        token = re.sub("hahaha", "haha", token)
        token = re.sub("lmfao", "lmao", token)
        token = re.sub("fuk", "fuck", token)
        token = re.sub("cals", "calls", token)
        token = re.sub("besos", "bezos", token)


        if tag.startswith("NN"):
            pos = "n"
        elif tag.startswith("VB"):
            pos = "v"
        else:
            pos = "a"
    
    lemmatizer = WordNetLemmatizer()
    cleaned_token  = lemmatizer.lemmatize(token, pos)

    if len(cleaned_token) > 0 and cleaned_token not in string.punctuation and cleaned_token.lower() not in stop_words and cleaned_token.isalpha():
            cleaned_tokens.append(cleaned_token.lower())
    return cleaned_tokens


#------------------------------------------------------------------------------------------------------------------------
#               CLEAN COMMENTS
#------------------------------------------------------------------------------------------------------------------------
def clean_comments(comments):

    comments_tokens = [word_tokenize(i) for i in comments]

    stop_words = stopwords.words("english")

    comment_cleaned_tokens_list = []
    for tokens in comments_tokens:
        comment_cleaned_tokens_list.append(remove_noise(tokens, stop_words))
    
    all_type_comments = get_all_words(comment_cleaned_tokens_list)

    return all_type_comments


#------------------------------------------------------------------------------------------------------------------------
#               GATHER HOT POST COMMENTS
#------------------------------------------------------------------------------------------------------------------------

def get_all_hot_comments(subreddit, num_of_posts):
    comments = []
    for submission in reddit.subreddit("{}".format(subreddit)).hot(limit=num_of_posts):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comments.append(comment.body) 

    all_hot_comments = clean_comments(comments)

    return all_hot_comments


#------------------------------------------------------------------------------------------------------------------------
#               GATHER TOP POST COMMENTS
#------------------------------------------------------------------------------------------------------------------------
def get_all_top_comments(subreddit, num_of_posts):
    comments = []
    for submission in reddit.subreddit("{}".format(subreddit)).top(limit=num_of_posts):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comments.append(comment.body)
    
    all_top_comments = clean_comments(comments)

    return all_top_comments


#------------------------------------------------------------------------------------------------------------------------
#               GATHER CONTROVERSIAL POST COMMENTS
#------------------------------------------------------------------------------------------------------------------------
def get_all_controversial_comments(subreddit, num_of_posts):
    comments = []
    for submission in reddit.subreddit("{}".format(subreddit)).controversial(limit=num_of_posts):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comments.append(comment.body)
    
    all_controversial_comments = clean_comments(comments)

    return all_controversial_comments



#------------------------------------------------------------------------------------------------------------------------
#               GATHER GILDED POST COMMENTS
#------------------------------------------------------------------------------------------------------------------------
def get_all_gilded_comments(subreddit, num_of_posts):
    comments = []
    for submission in reddit.subreddit("{}".format(subreddit)).gilded(limit=num_of_posts):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comments.append(comment.body)
    
    all_gilded_comments = clean_comments(comments)

    return all_gilded_comments



#------------------------------------------------------------------------------------------------------------------------
#               GATHER RISING POST COMMENTS
#------------------------------------------------------------------------------------------------------------------------
def get_all_rising_comments(subreddit, num_of_posts):
    comments = []
    for submission in reddit.subreddit("{}".format(subreddit)).rising(limit=num_of_posts):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            comments.append(comment.body)

    all_rising_comments = clean_comments(comments)

    return all_rising_comments