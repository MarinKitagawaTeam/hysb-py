from hysb.models.dungeons import Dungeons
from hysb.models.slayer import Slayer


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