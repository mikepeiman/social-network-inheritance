from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        pass

    def set_user(self, user=None):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        pass

    def __str__(self):
        pass


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        pass

    def __str__(self):
        pass


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        pass

    def __str__(self):
        pass
