## Python Tinder Bot

**Disclaimer**: This script is just for educational purpose

This python script will save your time by auto swiping in your tinder account and will 
save the stats in a file.

#### Setup:
* Download chromedriver, save it in the script folder or anywhere and update the path on line 35
* Install selenium in your venv with the command pip install selenium

#### Running the Bot
* Run the `tinder_bot.py` in debugging mode and pause the debugger once the page loads
* Manually login to your tinder account (You have to do this only the first time)
* Restart the script and the auto_swiping should work

Now, every time you run the script, your tinder will already be logged in.

**Important**: 
* The script just does the auto swiping. You have to do the first login manually.
* Once the chrome windows open, you should not resize it. You can minimize it.
* It is possible that the `xpath` of the elements might have changed, so you will have to
update it in the script. You can find the XPath of like and dislike button from developer
options in chrome.