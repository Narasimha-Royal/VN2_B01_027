class Details:
    def intro(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')


obj = Details()


obj.intro()

obj.intro('Charan')