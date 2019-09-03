import argparse
import os
import re
import instabot
from dotenv import load_dotenv


def get_mentions(comment):
    # https://gist.github.com/technion/5ca01ca420725e17cd3f#gistcomment-2658841
    pattern = re.compile(
        r"@([A-Za-z0-9_.](?:(?:[A-Za-z0-9_.]|(?:\\.(?!\\.))){0,28}(?:[A-Za-z0-9_.]))?)"
    )
    return pattern.findall(comment)


def is_user_exists(bot, user):
    user_id = bot.get_user_id_from_username(user)
    return bool(user_id)


def get_link():
    parser = argparse.ArgumentParser(
        description="Returns users qualified to enter sweepstakes"
    )
    parser.add_argument("URL", help="URL for your Instagram post")
    return parser.parse_args().URL


if __name__ == "__main__":
    load_dotenv()

    bot = instabot.Bot()
    bot.login(username=os.environ["INSTA_LOGIN"], password=os.environ["INSTA_PASS"])

    media_link = get_link()
    media_id = bot.get_media_id_from_link(media_link)
    likers = bot.get_media_likers(media_id)
    author = bot.get_media_info(media_id)[0]["user"]["username"]
    followers = bot.get_user_followers(author)
    comments = bot.get_media_comments_all(media_id)

    qualified_users = []
    for comment in comments:
        user_id = str(comment["user"]["pk"])
        username = comment["user"]["username"]
        if username in qualified_users:
            continue
        mentions = get_mentions(comment["text"])
        mention_verified = any(
            is_user_exists(bot, mention) for mention in mentions if mentions
        )
        if mention_verified and user_id in likers and user_id in followers:
            qualified_users.append(username)

    print(*qualified_users, sep=", ")
