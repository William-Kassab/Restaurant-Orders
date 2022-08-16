from collections import Counter


class TrackOrders:

    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def add_new_order(self, customer, order, day):
        self.data.append({
            'customer': customer,
            'order': order,
            'day': day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        orders = list()

        for order in self.data:
            orders.append(order)

        foods = [
            order['order'] for order in orders if order['customer'] == customer
        ]
        most_ordered = Counter(foods)
        return most_ordered.most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        orders = list()

        for order in self.data:
            orders.append(order)
        foods = set([x['order'] for x in orders])
        joao_orders = set(
            [
                order['order'] for order in orders if order['customer'] == customer
            ]
        )
        never_ordered = foods - joao_orders

        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        orders = list()

        for order in self.data:
            orders.append(order)
        days = set([day['day'] for day in orders])
        joao_days = set(
            [day['day'] for day in orders if day['customer'] == customer]
        )
        never_went = days - joao_days

        return never_went

    def get_busiest_day(self):
        orders = list()

        for order in self.data:
            orders.append(order['day'])

        days = Counter(orders)

        return days.most_common()[0][0]

    def get_least_busy_day(self):
        orders = list()

        for order in self.data:
            orders.append(order['day'])

        days = Counter(orders)

        return days.most_common()[-1][0]
