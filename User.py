from Post import PostFactory
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class User(Observer):
    boolean_log = True

    def __init__(self, username, password):
        self.posts = set()
        self.username = username
        self.password = password
        self.noty = []
        self.follows = set()

    def follow(self, second_user):
        if self.boolean_log:
            second_user.follows.add(self)
            print(f"{self.username} started following {second_user.username}")

    def unfollow(self, second_user):
        if self.boolean_log:
            second_user.follows.remove(self)
            print(f"{self.username} unfollowed {second_user.username}")

    def publish_post(self, post_type, *args):
        factory = PostFactory(self)
        post = factory.create_post(post_type, *args)
        for follower in self.follows:
            follower.update(f"{self.username} has a new post")
        self.posts.add(post)
        return post

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.follows)}"

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.noty:
            print(notification)

    def update(self, message):
        self.noty.append(message)
