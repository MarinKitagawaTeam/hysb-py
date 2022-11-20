from hysb.models.dungeons import Dungeons
from hysb.models.slayer import Slayer
from hysb.models.hotm import Hotm


class ProfileResult:

    def __init__(self, data):
        self.success = data.get('success')
        if data.get('profile'):
            self.profile = Profile(data.get('profile'))
        else:
            self.profiles = [Profile(profile) for profile in data.get('profiles')]


class Profile:

    def __init__(self, data):
        self.id = data.get('profile_id')
        self.members = data.get('members')
        self.community_upgrades = data.get('community_upgrades')
        self.cute_name = data.get('cute_name')
        self.banking = data.get('banking')
        self.game_mode = data.get('game_mode')


class Member:

    def __init__(self, data):
        self.pets = [Pets(pet) for pet in data[0]]
        self.fairy_exchanges = data[1]
        self.dungeons = Dungeons(data.get('dungeons'))
        self.slayer = Slayer(data.get('slayer_bosses'))
        # till now not modelled
        self.active_effects = data.get('active_effects')
        self.nether_island_player_data = data.get('nether_island_player_data')
        self.jacob = data.get('jacob2')
        # hell nah I won't model that
        self.stats = data.get('stats')
        self.death_count = data.get('death_count')
        self.harp_quest = data.get('harp_quest')
        self.experimentation = data.get('experimentation')
        self.first_join_hub = data.get('first_join_hub')
        self.personal_bank_upgrade = data.get('personal_bank_upgrade')
        self.bestiary = data.get('bestiary')
        self.tutorial = data.get('tutorial')
        self.perks = data.get('perks')
        self.visited_zones = data.get('visited_zones')
        self.coop_invitation = data.get('coop_invitation')
        self.quests = data.get('quests')
        self.purse = data.get('coin_purse')
        self.autopet = data.get('autopet')
        self.inv_armor = data.get('inv_armor')
        self.accessory_bag_storage = data.get('accessory_bag_storage')
        self.crafted_generators = data.get('crafted_generators')
        self.visited_modes = data.get('visited_modes')
        self.disabled_potion_effects = data.get('disabled_potion_effects')
        self.mining_core = Hotm(data.get('mining_core'))


class Pets:

    def __init__(self, data):
        self.uuid = data[0]
        self.type = data[1]
        self.exp = data[2]
        self.active: bool = data[3]
        self.tier = data[4]
        self.held_item = data[5]
        self.candy_used = data[6]
        self.skin = data[7]