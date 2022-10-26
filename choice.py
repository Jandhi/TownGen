import re
from noise import frandom

class MagicHat:
    def __init__(self, *items) -> None:
        self.total_weight = 0
        self.top_item = None
        self.count = 0

        for item, weight in items:
            self.add_item(item, weight)
    
    def item(self):
        return self.top_item
    
    def add_item(self, item, weight) -> None:
        self.count += 1

        # weights can't be negative
        if weight < 0:
            weight = 0

        if self.total_weight == 0 and weight > 0:
            self.top_item = item
        elif self.total_weight > 0 and frandom(self.total_weight + weight) > self.total_weight:
            self.top_item = item
        
        self.total_weight += weight
        self.count += 1

        return self.top_item