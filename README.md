# ChipTweet-Bot

Chipotle is running an promotion during the NBA finals: every time a 3-pointer is made, Chipotle tweets a code for a free Burrito. This bot is specifically designed to retrieve those promotional codes from Chipotle's tweets during NBA finals games **WITHOUT** using any external API that cost money. It sends the codes to your phone as a text message (SMS) using  `AppleScript` and the `subprocess` module. The bot utilizes various technologies, including `snscrape`, `pandas`, `re`, and `subprocess`.

## Usage

1. Clone the repository:
2. Navigate to the project directory:
3. Modify the notebook to include the date of the event in the query field and any customization you desire for code extraction and text message sending.
4. Run the bot:

## Customization

You can customize the bot by modifying the `chipTweetV2.ipynb` file according to your preferences:

- Can be done for any twitter promo since modifying the query field with the desired useredname and date range
- Adjust the code extraction logic by modifying the regular expressions or string manipulation in the `extract_promo_code()` function.
- Customize the text message sending by editing the `send_text_message()` function in the `py_imessage` library.

## Requirements

- `snscrape`: A library for scraping tweets from Twitter.
- `pandas`: A library for data manipulation and analysis.
- `re`: The regular expression module for pattern matching and extraction.
- `subprocess`: A module to run system commands and interact with the terminal.
- `AppleScript`: A scripting language used for automation and control on macOS.

Please note that the bot's efficiency in retrieving promo codes depends on various factors, including network connectivity, and the frequency of tweets made by Chipotle during NBA finals games.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and enhance the bot based on your requirements and enjoy your free meals from Chipotle!

Let me know if you need any further assistance or clarification.

