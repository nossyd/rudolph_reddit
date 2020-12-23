import praw
import config

reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     user_agent=config.user_agent)







#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#               CAUTION: TESTING AREA BELOW
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------

# Test api connection by printing top 10 hot submissions to /r/soccer
#for submission in reddit.subreddit("soccer").hot(limit=10):
#    print(submission.title)

# obtaining subreddit
#subreddit = reddit.subreddit("soccer")

# Test obtaining metadata
#comments=[]
#for submission in subreddit.hot(limit=10):
#    submission.comments.replace_more(limit=0)
#    for top_level_comment in submission.comments:
#        comments.append(top_level_comment.body)
    #print(submission.title)
#    print(submission.score)
    #print(submission.id)
#    print(submission.url)
#print("-------------------------------------------------------------------------------------------")
#print("-------------------------------------------------------------------------------------------")
#print(comments)

# obtaining submission instance
#submission = reddit.submission(id="keis8u")

# post title
#print(submission.title)

# redditor who posted
#redditor1 = submission.author
#print(redditor1)
# their karma
#print(redditor1.link_karma)

# comments from post
## this just gathers list of comments by id
#top_level_comments = list(submission.comments) # top level
#print(top_level_comments)


# this actually prints contents of comments & first line solves 'MoreComments" problem
#comments = []
#submission.comments.replace_more(limit=0)
#for top_level_comment in submission.comments:
#    comments.append(top_level_comment.body)
    #print(top_level_comment.body)

#print(comments)

#all_comments = submission.comments.tolist() # all comments
#print(all_comments)