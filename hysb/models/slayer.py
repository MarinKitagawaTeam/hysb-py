class Slayer:

    def __init__(self, data):
        if not data:
            return
        self.zombie = SlayerData(data.get('zombie'))
        self.spider = SlayerData(data.get('spider'))
        self.wolf = SlayerData(data.get('wolf'))
        self.enderman = SlayerData(data.get('enderman'))
        self.blaze = SlayerData(data.get('blaze'))


class SlayerData:

    def __init__(self, data):
        if not data:
            return
        self.claimed_levels = Levels(data.get('claimed_levels'))
        self.boss_kills_tier_0 = data.get('boss_kills_tier_0')
        self.boss_kills_tier_1 = data.get('boss_kills_tier_1')
        self.boss_kills_tier_2 = data.get('boss_kills_tier_2')
        self.boss_kills_tier_3 = data.get('boss_kills_tier_3')
        self.boss_kills_tier_4 = data.get('boss_kills_tier_4')
        self.boss_kills_tier_5 = data.get('boss_kills_tier_5')
        self.xp = data.get('xp')


class Levels:

    def __init__(self, data):
        if not data:
            return
        self.level_1 = data.get('level_1')
        self.level_2 = data.get('level_2')
        self.level_3 = data.get('level_3')
        self.level_4 = data.get('level_4')
        self.level_5 = data.get('level_5')
        self.level_6 = data.get('level_6')