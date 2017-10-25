import praw
import pdb
import re
import os

# returns an array of each string in posts_replied_to.txt, which is all the post id's previously replied to
def get_posts_array():
    if not os.path.isfile("storage\posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("storage\posts_replied_to.txt", "r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to


# returns an array of each string in comments_replied_to.txt, which is all the comment id's previously replied to
def get_comments_array():
    if not os.path.isfile("storage\comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("storage\comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    return comments_replied_to



# takes an array of strings of post id, wirtes them to the posts_replied_to.txt
def store_posts(posts_replied_to):
    with open("storage\posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


# takes an array of strings of comments id, writes them to the comments_replied_to.txt
def store_comments(comments_replied_to):
    with open("storage\comments_replied_to.txt", "w") as f:
        for comment_id in comments_replied_to:
            f.write(comment_id + "\n")
