class Dungeons:
    def __init__(self, data):
        if not data:
            return
        #  We are adding this, to prevent a crash if hypixel adds in 2030 a new dungeon type
        self.catacombs = DungeonType(data.get('dungeon_types').get('catacombs'))
        # Not supported Yet
        # self.master = DungeonType(data.get('dungeon_types').get('master_catacombs'))
        self.classes_xp = Classes(data.get('player_classes'))
        # till now not modelled
        self.dungeon_journal = data.get('dungeon_journal')
        # yep it's dungeons_blah_blah
        self.dungeons_blah_blah = data.get('dungeons_blah_blah')
        self.selected_dungeon_class = data.get('selected_dungeon_class')
        self.daily_runs = DailyRuns(data.get('daily_runs'))
        # till now not modelled
        self.treasures = data.get('treasures')


class DungeonType:

    def __init__(self, data):
        if not data:
            return
        self.times_played = CatacombsFloors(data.get('times_played'))
        self.experience = data.get('experience')
        self.times_completed = CatacombsFloors(data.get('tier_completions'))
        self.fastest_time = CatacombsFloors(data.get('fastest_time'))
        self.best_runs = data.get('best_runs')
        self.best_score = CatacombsFloors(data.get('best_score'))
        self.mobs_killed = CatacombsFloors(data.get('mobs_killed'))
        self.most_mobs_killed = CatacombsFloors(data.get('most_mobs_killed'))
        self.most_damage_mage = CatacombsFloors(data.get('most_damage_mage'))
        self.most_healing = CatacombsFloors(data.get('most_healing'))
        self.watcher_kills = CatacombsFloors(data.get('watcher_kills'))
        self.highest_tier_completed = data.get('highest_tier_completed')
        self.most_damage_tank = data.get('most_damage_tank')
        self.most_damage_healer = data.get('most_damage_healer')
        self.most_damage_archer = data.get('most_damage_archer')
        self.fastest_time_s = CatacombsFloors(data.get('fastest_time_s'))
        self.fastest_time_s_plus = CatacombsFloors(data.get('fastest_time_s_plus'))
        self.most_damage_berserk = CatacombsFloors(data.get('most_damage_berserk'))
        self.milestone_completions = CatacombsFloors(data.get('milestone_completions'))
        self.daily_runs = DailyRuns(data.get('daily_runs'))


class CatacombsFloors:

    def __init__(self, data):
        if not data:
            return
        self.f0 = data.get("0")
        self.f1 = data.get("1")
        self.f2 = data.get("2")
        self.f3 = data.get("3")
        self.f4 = data.get("4")
        self.f5 = data.get("5")
        self.f6 = data.get("6")
        self.f7 = data.get("7")


class Classes:
    def __init__(self, data):
        if not data:
            return
        self.healer = data.get('healer').get('experience')
        self.mage = data.get('mage').get('experience')
        self.tank = data.get('tank').get('experience')
        self.berserk = data.get('berserk').get('experience')
        self.archer = data.get('archer').get('experience')


class DailyRuns:
    def __init__(self, data):
        if not data:
            return
        self.current_day_stamp = data.get('current_day_stamp')
        self.completed_runs = data.get('completed_runs_count')
