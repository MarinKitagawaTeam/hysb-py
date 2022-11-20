class Hotm:

    def __init__(self, data):
        if not data:
            return

        self.nodes = data.get('nodes')
        self.received_free_tier = data.get('received_free_tier')
        self.tokens = data.get('tokens')
        self.mithril_powder = data.get('powder_mithril')
        self.mithril_powder_total = data.get('powder_mithril_total')
        self.tokens_spent = data.get('tokens_spent')
        self.experience = data.get('experience')
        self.mithril_powder_spent = data.get('powder_spent_mithril')
        self.retroactive_tier2_token = data.get('retroactive_tier2_token')
        self.crystals = Crystals(data.get('crystals'))
        self.selected_pickaxe_ability = data.get('selected_pickaxe_ability')
        self.greater_mines_last_access = data.get('greater_mines_last_access')
        self.biomes = data.get('biomes')
        self.gemstone_powder = data.get('powder_gemstone')
        self.gemstone_powder_total = data.get('powder_gemstone_total')


class Crystals:

    def __init__(self, data):
        if not data:
            return

        self.jade = CrystalsData(data.get('jade_crystal'))
        self.amber = CrystalsData(data.get('amber_crystal'))
        self.amethyst = CrystalsData(data.get('amethyst_crystal'))
        self.sapphire = CrystalsData(data.get('sapphire_crystal'))
        self.topaz = CrystalsData(data.get('topaz_crystal'))
        self.jasper = CrystalsData(data.get('jasper_crystal'))
        self.ruby = CrystalsData(data.get('ruby_crystal'))


class CrystalsData:

    def __init__(self, data):
        if not data:
            return

        self.state = data.get('state')
        self.total_found = data.get('total_found')
        self.total_placed = data.get('total_placed')