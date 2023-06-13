import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import time
import subprocess
from PIL import Image
import urllib.request
from pytesseract import pytesseract

query = "from:ChipotleTweets -filter:replies until:2023-06-09 since:2023-06-06"
#query = "from:harrisonchui02 -filter:replies until:2023-06-09 since:2023-06-06"

def runQuery(query,seen_urls):
    tweets = []
    limit = 5000
    mode_param = sntwitter.TwitterSearchScraperMode.TOP
    scraped_tweets = list(sntwitter.TwitterSearchScraper(query, mode = mode_param, maxEmptyPages=1).get_items())

    for tweet in scraped_tweets:
        try:
            if tweet.media and (tweet.media[0].fullUrl not in seen_urls):
              tweets.append(tweet.media[0].fullUrl)
              seen_urls.add(tweet.media[0].fullUrl)
        except sntwitter.ScraperException as e:
            print(f"An error occurred: {str(e)}")
            continue

        if len(tweets) == limit:
            break
    #print(tweets[-1])
    return tweets,seen_urls

def extract_codes(content):
    pattern = r'Text ((\w|[$%])+) to 888222'
    codes = []
    
    for string in content:
        urllib.request.urlretrieve(string,"temp.jpg")
        image = Image.open("temp.jpg")
        text = pytesseract.image_to_string(image)
        match = re.search(pattern, text)
        if match:
            code = match.group(1)
            codes.append(code)
    
    return codes

# print(extract_codes(runQuery(query)))

def send_message(phone_number, message):
    # Construct the AppleScript code with the provided phone number and message
    applescript_code = f'''
    set phone_number to "{phone_number}"
    set message_text to "{message}"

    tell application "Messages"
        set targetService to 1st service whose service type = SMS
        set theBuddy to buddy phone_number of targetService
        send message_text to theBuddy
    end tell
    '''

    # Execute the AppleScript code using osascript
    subprocess.run(['osascript', '-e', applescript_code])

master_codes = set(['BONUSFREEPOINTER%$$Z', 'FREETHREESYN35', 'FREETHREES7QXE', 'FREETHREESH4C8', 'FREETHREESJQGA', 'FREETHREESTZ8F', 'FREETHREESQ7%P', 'FREETHREES9E85', 'FREETHREESXK%2', 'FREETHREESR_FJ', 'FREETHREESMHQZ', 'FREETHREESP_TW', 'FREETHREESX3AV', 'FREETHREESPHAW', 'FREETHREES4WUQ', 'FREETHREESH%QS', 'FREETHREESG329', 'FREETHREESJ88H'])  # Master list of codes

def getBurrito(interval,phone):
    seen_urls = set()
    while True:
        q,s = runQuery(query,seen_urls)
        seen_urls = s
        codes = extract_codes(q)
        for code in codes:
            if code not in master_codes:
                print("new Code :" + code)
                #pyautogui.write(code+'\n')
                send_message(phone,code)
                time.sleep(.2)
                master_codes.add(code)

        time.sleep(interval)

def main():
    #time.sleep(5)
    getBurrito(.1,"888222")
    #runQuery(query)
    #print(type(q[0][0]))
    
# print(runQuery(query, set()))
main()