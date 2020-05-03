"""
Disclaimer: This script is just for educational purpose
"""
import random
from selenium import webdriver
from time import sleep, time

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options


class TinderBot:
    """ Tinder bot class with all the methods"""
    def __init__(self):
        """Method to initialize chrome webdriver with settings"""
        chrome_options = Options()

        # This will create a new profile in your chrome browser
        chrome_options.add_argument(
            "--user-data-dir=C:\\Users\\username\\AppData\\Local\\Google Selenium\\Chrome\\User Data"
        )
        chrome_options.add_argument(
            "--profile-directory=Default"
        )

        # Changing the user agent so that tinder.com doesn't know
        # that this is an automated script running using selenium
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.'
            '4044.113 Safari/537.36'
        )
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

        self.driver = webdriver.Chrome(
            executable_path="chromedriver.exe",  # Path to your chrome driver
            chrome_options=chrome_options
        )

    def start(self):
        """Method to start the bot"""
        self.driver.get('https://tinder.com')
        sleep(5)

    def swipe_right(self):
        """Method to swipe right on the current profile"""
        btn_like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        btn_like.click()

    def swipe_left(self):
        """Method to swipe left of the current profile"""
        btn_dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        btn_dislike.click()

    def rand_sleep(self):
        """
        Method to sleep randomly between 1 to 3 seconds (float)
        This randomness prevents our bot from getting detected by tinder
        :return:
        """
        sleep_sec = random.uniform(1, 3)
        print('Sleeping for {} seconds'.format(str(sleep_sec)))
        sleep(sleep_sec)

    def auto_swipe(self):
        """Method to start swiping"""
        likes, dislikes = 0, 0  # Count of swipes
        filename = time()
        while True:
            self.rand_sleep()
            try:
                rand = random.random()
                if rand < .80:  # Probability of swiping right on a profile
                    self.swipe_right()
                    likes += 1
                    print('Swiped Right, Count {}'.format(likes))
                else:
                    self.swipe_left()
                    dislikes += 1
                    print('Swiped Left, Count {}'.format(dislikes))
                # Writing the counts to a file
                with open(str(filename).split('.')[0] + '.txt', 'w+') as stats:
                    stats.writelines('Swiped Right. Count {} \n'.format(likes))
                    stats.writelines('Swiped Left Count {}'.format(dislikes))
            except ElementClickInterceptedException as e:
                # Handling if any unexpected popup occurs on screen
                # Refreshing the page and restarting the bot
                self.driver.refresh()
                sleep(5)
                self.auto_swipe()
            except Exception as e:
                print(str(e))
                return -1


tinder_bot = TinderBot()
tinder_bot.start()
tinder_bot.auto_swipe()
