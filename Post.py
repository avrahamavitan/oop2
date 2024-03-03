from PIL import Image


class PostFactory:

    def __init__(self, user):
        self.Likes = set()
        self.Comments = set()
        self.name = user.username
        self.password = user.password
        self.user_owner = user
#Classification for the three post types
    def create_post(self, post_type, *args):
        if post_type == "Text":
            return TextPost(*args, self.user_owner)
        elif post_type == "Image":
            return ImagePost(*args, self.user_owner)
        elif post_type == "Sale":
            return SalePost(*args, self.user_owner)

    def like(self, scend_user):
        if not self.user_owner.is_connected:
            raise ValueError("You are not connected to the social network")
        if scend_user.username != self.name:
            self.Likes.add(scend_user)
            self.user_owner.noty.append(f"{scend_user.username} liked your post")
            print(f"notification to {self.name}: {scend_user.username} liked your post")

    def comment(self, scend_user, text):
        if not self.user_owner.is_connected:
            raise ValueError("You are not connected to the social network")
        if scend_user.username != self.name:
            self.Comments.add(scend_user)
            self.user_owner.noty.append(f"{scend_user.username} commented on your post")
            print(f"notification to {self.name}: {scend_user.username} commented on your post: {text}")


class TextPost(PostFactory):
    def __init__(self, text, user):
        super().__init__(user)
        self.text = text
        print(self.__str__())

    def __str__(self):
        return f'{self.name} published a post:\n"{self.text}"\n'


class ImagePost(PostFactory):
    def __init__(self, image_path, user):
        super().__init__(user)
        self.image_path = image_path
        print(self.__str__())


    def display(self):
        if not self.user_owner.is_connected:
            raise ValueError("You are not connected to the social network")
        image = Image.open(f"{self.image_path}")
        image.show()
        print("Shows picture")

    def __str__(self):
        return f"{self.name} posted a picture\n"


class SalePost(PostFactory):
    def __init__(self, product_description, price, location, user):
        super().__init__(user)
        self.product_description = product_description
        self.price = price
        self.location = location
        self.available = True
        print(self.__str__())

    def __str__(self):
        if self.available:
            return (
                f"{self.name} posted a product for sale:\nFor sale! {self.product_description}, price: {self.price}, "
                f"pickup from: {self.location}\n")
        else:
            return (
                f"{self.name} posted a product for sale:\nSold! {self.product_description}, price: {self.price}, "
                f"pickup "
                f"from: {self.location}\n")

    def discount(self, count, password):
        if not self.user_owner.is_connected:
            raise ValueError("You are not connected to the social network")
        if self.password == password:
            self.price = self.price - self.price * 1 / count
            print(f"Discount on {self.name} product! the new price is: {self.price}")

    def sold(self, password):
        if not self.user_owner.is_connected:
            raise ValueError("You are not connected to the social network")
        if self.password == password:
            self.available = False
            print(f"{self.name}'s product is sold")
