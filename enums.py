from enum import Enum
from typing import List


class Mapping(Enum):
    id = 'Row ID'
    product_id = 'Product ID'
    product_name = 'Product Name'
    sales = 'Sales'
    quantity = 'Quantity'
    profit = 'Profit'
    start_date = 'Order Date'
    end_date = 'Ship Date'

    @classmethod
    def get_values(cls) -> List[str]:
        return [item.value for item in cls]

    @classmethod
    def get_dates(cls) -> List[str]:
        return [cls.start_date.value, cls.end_date.value]
