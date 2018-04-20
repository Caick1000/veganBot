import praw

bot = praw.Reddit(user_agent='niceBot v0.1',
                  client_id='5B7ysU3JrEDvOA',
                  client_secret='mp6ObGVFCb0_1JHhPvsI_WntLlI',
                  username='randomBots-',
                  password='')

subreddit = bot.subreddit('all')

comments = subreddit.stream.comments()

cache = []


for comment in comments:
    text = comment.body
    author = comment.author.name

    if 'Nice.' in text == 'Nice.' and author != 'randomBots-' and comment.id not in cache:
        message = 'Nice.'

        comment.reply(message)
        print(author, '-->', text)
        cache.append(comment.id)

