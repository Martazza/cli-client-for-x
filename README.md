# CLI Client using Tweepy

A Python-based Twitter client that can automate various actions on X/Twitter, such as posting tweets, uploading photos, liking tweets, and more.

## Features

- Post text tweets
- Post tweets with single or multiple photos
- Show recent tweets from your timeline
- Follow or unfollow users
- Like or retweet tweets
- Reply to tweets
- Search for recent tweets based on a query
- Download media from a tweet
- Send direct messages
- Delete tweets

## Requirements

- Python 3.7+
- Tweepy
- Requests
- Python-dotenv

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/twitter-bot.git
   cd twitter-bot
   ```
2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Set up your `.env` file with your Twitter API credentials:

   ```env
   API_KEY=your_api_key
   API_SECRET_KEY=your_api_secret_key
   BEARER_TOKEN=your_bearer_token
   ACCESS_TOKEN=your_access_token
   ACCESS_TOKEN_SECRET=your_access_token_secret
   ```
5. Run the bot with your desired action:

   ```bash
   python twitter_bot.py --tweet "Hello, world!"
   ```

## Usage

### Command-Line Arguments

- **Post a text tweet:**

  ```bash
  python twitter_bot.py --tweet "Your tweet text here"
  ```
- **Post a tweet with a photo:**

  ```bash
  python twitter_bot.py --tweet-photo "Caption for the photo" path/to/photo.jpg
  ```
- **Post a tweet with multiple photos:**

  ```bash
  python twitter_bot.py --tweet-multiple-photos "Caption for photos" path/to/photo1.jpg path/to/photo2.jpg
  ```
- **Show recent tweets (default is 5):**

  ```bash
  python twitter_bot.py --show-tweets 5
  ```
- **Follow a user:**

  ```bash
  python twitter_bot.py --follow username
  ```
- **Unfollow a user:**

  ```bash
  python twitter_bot.py --unfollow username
  ```
- **Like a tweet by ID:**

  ```bash
  python twitter_bot.py --like TWEET_ID
  ```
- **Retweet a tweet by ID:**

  ```bash
  python twitter_bot.py --retweet TWEET_ID
  ```
- **Reply to a tweet by ID:**

  ```bash
  python twitter_bot.py --reply "Your reply text" TWEET_ID
  ```
- **Search for tweets with a query:**

  ```bash
  python twitter_bot.py --search "your search query"
  ```
- **Download media from a tweet by ID:**

  ```bash
  python twitter_bot.py --download-media TWEET_ID
  ```
- **Send a direct message:**

  ```bash
  python twitter_bot.py --dm USER_ID "Your message text"
  ```
- **Delete a tweet by ID:**

  ```bash
  python twitter_bot.py --delete TWEET_ID
  ```

## Logging

All actions and errors are logged into `twitter_bot.log` for easy debugging and tracking of activities.

## Contributing

Feel free to fork this repository, create a new branch, and submit a pull request for any improvements or features you would like to add.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this bot responsibly and in compliance with Twitter's terms of service. The author is not responsible for any misuse of this tool.
