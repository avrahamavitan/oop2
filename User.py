from Post import PostFactory
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
#All the options a user can do
#Checking in every function that the user is actually connected
class User(Observer):
    is_connected = True

    def __init__(self, username, password):
        self.posts = set()
        self.username = username
        self.password = password
        self.noty = []
        self.follows = set()

    def follow(self, second_user):
        if not self.is_connected:
            raise ValueError("You are not connected to the social network")

        if self not in second_user.follows:
            second_user.follows.add(self)
            print(f"{self.username} started following {second_user.username}")

    def unfollow(self, second_user):
        if not self.is_connected:
            raise ValueError("You are not connected to the social network")
        if self not in second_user.follows:
            raise ValueError(f"You are not following after {second_user.username}")
        second_user.follows.remove(self)
        print(f"{self.username} unfollowed {second_user.username}")

    def publish_post(self, post_type, *args):
        if not self.is_connected:
            ValueError("You are not connected to the social network")

        factory = PostFactory(self)
        post = factory.create_post(post_type, *args)
        self.posts.add(post)
        self.notify_followers()
        return post

    def __str__(self):
        return f"User name: {self.username}, Number of posts: {len(self.posts)}, Number of followers: {len(self.follows)}"

    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.noty:
            print(notification)

    def notify_followers(self):
        for follower in self.follows:
            follower.update(f"{self.username} has a new post")

    def update(self, message):
        self.noty.append(message)
