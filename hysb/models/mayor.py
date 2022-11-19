class Mayor:
    def __init__(self, data):
        self.key = data.get('key')
        self.name = data.get('name')
        self.perks = [Perk(perk) for perk in data.get('perks')]
        self.election = Election(data.get('election'))


class Candidates:

    def __init__(self, data):
        self.key = data.get('key')
        self.name = data.get('name')
        self.perks = [Perk(perk) for perk in data.get('perks')]
        self.votes = data.get('votes')


class Perk:
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')


class Election:

    def __init__(self, data):
        self.year = data.get('year')
        self.candidates = [Candidates(can) for can in data.get('candidates')]


