from transition import Transition


class PetriNet:
    # places consist of a name
    P = []
    # transitions (consist transition object)
    T = []
    # flow relation (consist of a source and a destination place ID's)
    F = []
    # marking (consist of place ID's)
    M = []

    def __init__(self):
        self.F = []
        self.T = []
        self.P = []
        self.M = []

    def add_place(self, name):
        self.P.append(name)
        return self

    def add_transition(self, name, id):
        # create transition
        t = Transition(name, id)

        # add transition to list and dic
        self.T.append(t)

        return self

    def add_edge(self, source, target):
        # if id (source, target) is under 0 it is the id of a transition
        if target < 0:
            for transition in self.T:
                if transition.id == target:
                    transition.pre.append(source)

        if source < 0:
            for transition in self.T:
                if transition.id == source:
                    transition.post.append(target)

        return self

    def get_tokens(self, place):
        return len(list(filter(lambda token: token == place, self.M)))

    def is_enabled(self, transition_id):
        # find transition
        tran = self.find_transition(transition_id)

        if tran is None:
            print("Transition was not found")
            return self

        token_count = len(list(filter(lambda pre_place: pre_place in self.M, tran.pre)))

        return token_count == len(tran.pre)

    # add a token
    def add_marking(self, place):
        # add token
        self.M.append(place)
        return self

    def fire_transition(self, transition_id):
        # find transition
        tran = self.find_transition(transition_id)

        if tran is None:
            print("Transition was not found")
            return self

        # move marking/token from pre-place to post-place
        for pre in tran.pre:
            self.M.remove(pre)
        for post in tran.post:
            self.M.append(post)

        return self

    def find_transition(self, transition_id):
        return next((x for x in self.T if x.id == transition_id), None)