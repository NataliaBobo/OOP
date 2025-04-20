class SecretStash:
    def __init__(self):
        self.__chocolates = 50  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left")

stash = SecretStash()
stash.take_chocolate()