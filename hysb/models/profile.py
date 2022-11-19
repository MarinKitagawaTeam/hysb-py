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