import praw
import pdb
import re
import os
from utils import *


def fix_bing_references(subreddit, num):
    num_posts_replied_to = 0
    num_comments_replied_to = 0

    posts_replied_to = get_posts_array()
    comments_replied_to = get_comments_array()

    print("comedy test\n")
    for submission in subreddit.new(limit=num):
        if submission.id not in posts_replied_to:
            if re.search("bing", submission.selftext, re.IGNORECASE):
                response = "> bing\n\n"
                response += "google\*"
                submission.reply(response)
                posts_replied_to.append(submission.id)
                num_posts_replied_to += 1
        print(submission.title)
        print(submission.selftext)
        print(submission.author)
        print(submission.score)
        print("---------------------------------------\n")

        for top_level_comment in submission.comments:
            if submission.id not in comments_replied_to:
                if re.search("bing", top_level_comment.body, re.IGNORECASE):
                    response = "> bing\n\n"
                    response += "google\*"
                    submission.reply(response)
                    comments_replied_to.append(top_level_comment.id)
                    num_comments_replied_to += 1

    print("replied to ", num_posts_replied_to, " posts\n")
    print("replied to ", num_comments_replied_to, " comments\n")
    store_posts(posts_replied_to)
    store_comments(comments_replied_to)
