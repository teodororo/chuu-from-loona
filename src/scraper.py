import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes_container = []

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('in_reply_to_status_id:1565484244117458947').get_items()):
    if i>100:
        break
    attributes_container.append([tweet.url, tweet.content, tweet.media])
    
tweets_df = pd.DataFrame(attributes_container, columns=["url", "content", "media"])
print(tweets_df.head())