class Bazaar:

    def __init__(self, data):
        self.success = data.get('success')
        self.last_updated = data.get('lastUpdated')
        self.products = [Products(k, v) for k, v in data.get('products').items()]


class Products:

    def __init__(self, name, values):
        self.name = name
        self.id = values.get('product_id')
        self.sell_sum = [Summary(summary) for summary in values.get('sell_summary')]
        self.buy_sum = [Summary(summary) for summary in values.get('buy_summary')]
        self.quick_status = QuickStatus(values.get('quick_status'))


class Summary:

    def __init__(self, data):
        self.amount = data.get('amount')
        self.price_per_unit = data.get('pricePerUnit')
        self.orders = data.get('orders')


class QuickStatus:

    def __init__(self, data):
        self.product_id = data.get('productId')
        self.sell_price = data.get('sellPrice')
        self.sell_volume = data.get('sellVolume')
        self.sell_moving_week = data.get('sellMovingWeek')
        self.sell_orders = data.get('sellOrders')
        self.buy_price = data.get('buyPrice')
        self.buy_volume = data.get('buyVolume')
        self.buy_moving_week = data.get('buyMovingWeek')
        self.buy_orders = data.get('buyOrders')
