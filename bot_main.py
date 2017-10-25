import praw
import pdb
import re
import os
from utils import *
from responses import *

reddit = praw.Reddit(user_agent='GoogleFixBot',
                     client_id='Vwg_x0jsrQ9rOw',
                     client_secret='2dqhoZf4GDR3ji0B_tnzuVZbsk4',
                     username='FuckBingBot',
                     password='Yourface1234')

subreddit = reddit.subreddit('moviebottestingarena')

fix_bing_references(subreddit, 1)
