from hysb.models import mayor


class ElectionMayorResult:

    def __init__(self, data: dict):
        self.success: bool = data.get('success')
        self.last_updated: int = data.get('lastUpdated')
        self.mayor = mayor.Mayor(data.get('mayor'))
