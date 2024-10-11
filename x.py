import tweepy
import logging
import argparse
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API credentials
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

# Configure logging
logging.basicConfig(filename='twitter_bot.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Authenticate using tweepy.Client for API v2
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)
auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

# Function to delete a tweet
def delete_tweet(tweet_id):
    try:
        client.delete_tweet(tweet_id)
        logging.info(f"Deleted tweet ID: {tweet_id}")
        print(f"Deleted tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error deleting tweet {tweet_id}: {e}")
        print(f"Error deleting tweet {tweet_id}: {e}")


# Function to post a text tweet
def tweet_text(text):
    try:
        response = client.create_tweet(text=text)
        tweet_id = response.data.get('id')
        logging.info(f"Text tweet posted successfully! Tweet ID: {tweet_id}")
        print(f"Text tweet posted successfully! Tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error posting text tweet: {e}")
        print(f"Error posting text tweet: {e}")

# Function to post a tweet with a single photo
def tweet_with_photo(text, image_path):
    try:
        # Use API v1.1 for media upload
        media = api.media_upload(image_path)
        media_id = media.media_id
        response = client.create_tweet(text=text, media_ids=[media_id])
        tweet_id = response.data.get('id')
        logging.info(f"Tweet with photo posted successfully! Tweet ID: {tweet_id}")
        print(f"Tweet with photo posted successfully! Tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error posting tweet with photo: {e}")
        print(f"Error posting tweet with photo: {e}")

# Function to post a tweet with multiple photos
def tweet_with_multiple_photos(text, image_paths):
    try:
        media_ids = [api.media_upload(image_path).media_id for image_path in image_paths]
        response = client.create_tweet(text=text, media_ids=media_ids)
        tweet_id = response.data.get('id')
        logging.info(f"Tweet with multiple photos posted successfully! Tweet ID: {tweet_id}")
        print(f"Tweet with multiple photos posted successfully! Tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error posting tweet with multiple photos: {e}")
        print(f"Error posting tweet with multiple photos: {e}")

# Function to show recent tweets
def show_recent_tweets(count=5):
    try:
        user_id = client.get_me().data.id
        response = client.get_users_tweets(id=user_id, max_results=count)
        logging.info(f"Displaying {count} recent tweets:")
        for tweet in response.data:
            print(f"{tweet.created_at} - {tweet.text}\n")
    except tweepy.TweepyException as e:
        logging.error(f"Error retrieving recent tweets: {e}")
        print(f"Error retrieving recent tweets: {e}")

# Function to follow a user
def follow_user(username):
    try:
        user = client.get_user(username=username)
        client.follow_user(user.data.id)
        logging.info(f"Followed user: {username}")
        print(f"Followed user: {username}")
    except tweepy.TweepyException as e:
        logging.error(f"Error following user {username}: {e}")
        print(f"Error following user {username}: {e}")

# Function to unfollow a user
def unfollow_user(username):
    try:
        user = client.get_user(username=username)
        client.unfollow_user(user.data.id)
        logging.info(f"Unfollowed user: {username}")
        print(f"Unfollowed user: {username}")
    except tweepy.TweepyException as e:
        logging.error(f"Error unfollowing user {username}: {e}")
        print(f"Error unfollowing user {username}: {e}")

# Function to like a tweet
def like_tweet(tweet_id):
    try:
        client.like(tweet_id)
        logging.info(f"Liked tweet ID: {tweet_id}")
        print(f"Liked tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error liking tweet {tweet_id}: {e}")
        print(f"Error liking tweet {tweet_id}: {e}")

# Function to retweet a tweet
def retweet_tweet(tweet_id):
    try:
        client.retweet(tweet_id)
        logging.info(f"Retweeted tweet ID: {tweet_id}")
        print(f"Retweeted tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error retweeting tweet {tweet_id}: {e}")
        print(f"Error retweeting tweet {tweet_id}: {e}")

# Function to reply to a tweet
def reply_to_tweet(text, tweet_id):
    try:
        client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
        logging.info(f"Replied to tweet ID: {tweet_id}")
        print(f"Replied to tweet ID: {tweet_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error replying to tweet {tweet_id}: {e}")
        print(f"Error replying to tweet {tweet_id}: {e}")

# Function to search for tweets
def search_tweets(query, count=5):
    try:
        response = client.search_recent_tweets(query=query, max_results=count)
        logging.info(f"Searching for tweets with query: {query}")
        for tweet in response.data:
            print(f"{tweet.author_id}: {tweet.text}")
    except tweepy.TweepyException as e:
        logging.error(f"Error searching tweets: {e}")
        print(f"Error searching tweets: {e}")

# Function to download media from a tweet
def download_media_from_tweet(tweet_id, save_dir='downloads'):
    try:
        tweet = client.get_tweet(id=tweet_id, expansions='attachments.media_keys', media_fields='url')
        if 'media' in tweet.includes:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            for media in tweet.includes['media']:
                media_url = media['url']
                filename = os.path.join(save_dir, media_url.split("/")[-1])
                response = requests.get(media_url)
                with open(filename, 'wb') as file:
                    file.write(response.content)
                logging.info(f"Downloaded media from tweet ID {tweet_id} to {filename}")
                print(f"Downloaded media to {filename}")
        else:
            print("No media found in the specified tweet.")
    except tweepy.TweepyException as e:
        logging.error(f"Error downloading media from tweet {tweet_id}: {e}")
        print(f"Error downloading media from tweet {tweet_id}: {e}")

# Function to send a direct message
def send_direct_message(user_id, text):
    try:
        client.send_direct_message(recipient_id=user_id, text=text)
        logging.info(f"Sent direct message to user ID: {user_id}")
        print(f"Sent direct message to user ID: {user_id}")
    except tweepy.TweepyException as e:
        logging.error(f"Error sending direct message to user {user_id}: {e}")
        print(f"Error sending direct message to user {user_id}: {e}")

# Main function to parse command-line arguments and execute appropriate actions
def main():
    parser = argparse.ArgumentParser(description='Twitter Bot using Tweepy')
    parser.add_argument('--tweet', type=str, help='Post a text tweet')
    parser.add_argument('--tweet-photo', type=str, nargs=2, metavar=('TEXT', 'IMAGE_PATH'), help='Post a tweet with a photo')
    parser.add_argument('--tweet-multiple-photos', type=str, nargs='+', metavar=('TEXT', 'IMAGE_PATH'), help='Post a tweet with multiple photos')
    parser.add_argument('--show-tweets', type=int, metavar='COUNT', help='Show recent tweets')
    parser.add_argument('--follow', type=str, metavar='USERNAME', help='Follow a user')
    parser.add_argument('--unfollow', type=str, metavar='USERNAME', help='Unfollow a user')
    parser.add_argument('--like', type=str, metavar='TWEET_ID', help='Like a tweet by ID')
    parser.add_argument('--retweet', type=str, metavar='TWEET_ID', help='Retweet a tweet by ID')
    parser.add_argument('--reply', type=str, nargs=2, metavar=('TEXT', 'TWEET_ID'), help='Reply to a tweet by ID')
    parser.add_argument('--search', type=str, metavar='QUERY', help='Search for tweets with a query')
    parser.add_argument('--download-media', type=str, metavar='TWEET_ID', help='Download media from a tweet')
    parser.add_argument('--dm', type=str, nargs=2, metavar=('USER_ID', 'TEXT'), help='Send a direct message to a user')
    parser.add_argument('--delete', type=str, metavar='TWEET_ID', help='Delete a tweet by ID')

    args = parser.parse_args()

    if args.tweet:
        tweet_text(args.tweet)
    elif args.tweet_photo:
        tweet_with_photo(args.tweet_photo[0], args.tweet_photo[1])
    elif args.tweet_multiple_photos:
        tweet_with_multiple_photos(args.tweet_multiple_photos[0], args.tweet_multiple_photos[1:])
    elif args.show_tweets:
        show_recent_tweets(args.show_tweets)
    elif args.follow:
        follow_user(args.follow)
    elif args.unfollow:
        unfollow_user(args.unfollow)
    elif args.like:
        like_tweet(args.like)
    elif args.retweet:
        retweet_tweet(args.retweet)
    elif args.reply:
        reply_to_tweet(args.reply[0], args.reply[1])
    elif args.search:
        search_tweets(args.search)
    elif args.download_media:
        download_media_from_tweet(args.download_media)
    elif args.dm:
        send_direct_message(args.dm[0], args.dm[1])
    elif args.delete:
        delete_tweet(args.delete)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
