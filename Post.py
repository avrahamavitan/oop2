from PIL import Image


class PostFactory:

    def __init__(self, user):
        self.Likes = set()
        self.Comments = set()
        self.owner = user.username
        self.password = user.password
        self.user1 = user

    def create_post(self, post_type, *args):

        if post_type == "Text":
            return TextPost(*args, self.user1)
        elif post_type == "Image":
            return ImagePost(*args, self.user1)
        elif post_type == "Sale":
            return SalePost(*args, self.user1)

    def like(self, scend_user):
        if scend_user.username != self.owner:
            self.Likes.add(scend_user)
            self.user1.noty.append(f"{scend_user.username} liked your post")
            # self.noty.append(f"{scend_user.username} liked your post")
            print(f"notification to {self.owner}: {scend_user.username} liked your post")

    def comment(self, scend_user, text):
        self.Comments.add(scend_user)
        self.user1.noty.append(f"{scend_user.username} commented on your post")
        print(f"notification to {self.owner}: {scend_user.username} commented on your post: {text}")


class TextPost(PostFactory):
    def __init__(self, text, user):
        super().__init__(user)
        self.text = text
        print(self.__str__())

    def __str__(self):
        return f'{self.owner} published a post:\n"{self.text}"\n'


class ImagePost(PostFactory):
    def __init__(self, image_path, user):
        super().__init__(user)
        self.image_path = image_path
        print(self.__str__())


    def display(self):
        image = Image.open(f"{self.image_path}")
        image.show()
        print("Shows picture")

    def __str__(self):
        return f"{self.owner} posted a picture\n"


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
                f"{self.owner} posted a product for sale:\nFor sale! {self.product_description}, price: {self.price}, "
                f"pickup from: {self.location}\n")
        else:
            return (
                f"{self.owner} posted a product for sale:\nSold! {self.product_description}, price: {self.price}, "
                f"pickup "
                f"from: {self.location}\n")

    def discount(self, count, password):
        if self.password == password:
            self.price = self.price - self.price * 1 / count
            print(f"Discount on {self.owner} product! the new price is: {self.price}")

    def sold(self, password):
        if self.password == password:
            self.available = False
            print(f"{self.owner}'s product is sold")
