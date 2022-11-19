class Collections:

    def __init__(self, data: dict):
        self.success: bool = data.get(0)
        self.last_updated: int = data.get(1)
        self.version: str = data.get(2)
        self.collections: dict = data.get(3)
        print(self.collections)
