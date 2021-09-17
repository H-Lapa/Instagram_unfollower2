from instapy import InstaPy
import random

session = InstaPy(username = 'enter_username', password = 'enterpassword', headless_browser = False)

session.login()

session.unfollow_users(amount = 1, nonFollowers = True, unfollow_after = 0, sleep_delay = random.randint(4, 7) * 100 )

session.end()
