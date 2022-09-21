class Transition:

    def __init__(self, name, id):
        self.id = id  # id of transition
        self.value = name  # name
        self.pre = [] # connected "before" trans
        self.post = [] # connected "after" trans