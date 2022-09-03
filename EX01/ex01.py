from EX01.transition import Transition


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
        token_count = 0
        for tran in self.T:
            if tran.id == transition_id:
                for pre in tran.pre:
                    if pre in self.M:
                        token_count += 1

                return token_count == len(tran.pre)

    # add a token
    def add_marking(self, place):
        # add token
        self.M.append(place)
        return self

    def fire_transition(self, transition_id):
        # find transition
        tran = next((x for x in self.T if x.id == transition_id), None)

        if tran is None:
            print("Transition was not found")
            return self

        # move marking/token from pre-place to post-place
        for pre in tran.pre:
            self.M.remove(pre)
        for post in tran.post:
            self.M.append(post)

        return self
