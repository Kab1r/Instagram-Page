from instabot import Bot


class Poster:
    def __init__(self, username, password):
        self.bot = Bot()
        self.bot.login(username=username, password=password)

    def post_image(self, image):
        bot.upload_photo(image)
