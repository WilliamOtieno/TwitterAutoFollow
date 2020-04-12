from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self. password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/")
        time.sleep(5)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typeahead_click')
        time.sleep(5)
        for i in range(1, 10):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements_by_class_name('css-90loao')
            links = [elem.get_attribute('role') for elem in tweets]
            print(links)
            for link in links:
                bot.get('https://twitter.com' + link)
                try:
                    bot.find_element_by_class_name('r-4qtqp9').click()
                    time.sleep(10)
                except Exception as ex:
                    time.sleep(15)


will = TwitterBot('William__Otieno', 'shadowwalker101')
will.login()
will.like_tweets('ArchLinux')