import praw
import os
import re

# Importing the file.py
import arrays_database


def authenticate():
    print('Authenticating...\n')
    redditBot = praw.Reddit(user_agent='veganBot v1.0',
                            client_id='Qp8x9ezydpD64w',
                            client_secret='GTe4JmTN7gsilAanfevx92ItlyA',
                            username='veganBot-',
                            password='recipesAreLife')
    print('Authenticated as {}\n'.format(redditBot.user.me()))
    return redditBot


# The file to store the comments IDs, so we don't have duplicates
commentID_path = 'commentID.txt'


def run_veganBot(redditBot):
    # Concat the arrays of phrases on the arrays_database.py
    for i in range(0, len(arrays_database.complementPhrases)):

        for x in range(0, len(arrays_database.veganPhrases)):

            for comment in redditBot.subreddit('test').comments():

                text = comment.body
                match = re.findall(arrays_database.complementPhrases[i] + arrays_database.veganPhrases[x], text)
                author = comment.author.name

                # If we find a comment with the phrase we want, get the comment ID
                if match:

                    print('Vegan phrase found in comment with comment ID: ' + comment.id)
                    vegan_comment = match[0]
                    print('{} wrote: '.format(author))
                    print(vegan_comment)

                    if not os.path.exists(commentID_path):
                        open(commentID_path, 'w').close()
                    file_obj_r = open(commentID_path, 'r')

                    # If the comment ID is not in the file, reply to the comment
                    # else, restart function.
                    if comment.id not in file_obj_r.read().splitlines():
                        print('Link is unique...posting recipe\n')
                        comment.reply('--------TEST-------')

                        file_obj_r.close()

                        file_obj_w = open(commentID_path, 'a+')
                        file_obj_w.write(comment.id + '\n')
                        file_obj_w.close()
                    else:
                        print('Already visited link...no reply needed\n')


def main():
    reddit = authenticate()
    while True:
        run_veganBot(reddit)


if __name__ == '__main__':
    main()

