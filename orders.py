import argparse
import os
import os.path
from typing import Optional

import pandas
from pandas.core.frame import DataFrame
from pandas.errors import EmptyDataError

import calculations
from enums import Mapping

RESULT_FILE_NAME = "result.csv"


def load_frame(path: str) -> Optional[DataFrame]:
    """Loading csv file"""
    if not os.path.isfile(path):
        print("File not found")
        return

    try:
        return pandas.read_csv(path, sep=';', parse_dates=Mapping.get_dates(), infer_datetime_format=True,
                               index_col=Mapping.id.value, decimal=",", usecols=Mapping.get_values())
    except EmptyDataError:
        print("No columns to parse from file")


def save_frame(frame: DataFrame, path: str):
    """Saving csv file"""
    frame.to_csv(path, sep=';')


def main():
    parser = argparse.ArgumentParser(description='Prints statistics and save result csv file')
    parser.add_argument('path', help="CSV file path")
    args = parser.parse_args()

    path = os.path.abspath(args.path)
    path_result_file = os.path.join(os.path.dirname(path), RESULT_FILE_NAME)

    frame = load_frame(path)
    if frame is None:
        return

    sum_profit = calculations.get_sum_profit(frame)
    best_products = calculations.get_best_products(frame, 5)
    worst_products = calculations.get_worst_products(frame, 5)
    average_time = calculations.get_average_time(frame)
    deviation_time = calculations.get_standard_deviation_time(frame)

    save_frame(calculations.get_count_sales_by_products(frame), path_result_file)

    out = f"1. Посчитать общий профит с точностью до цента: \n{sum_profit}  \n\n\n" \
          "2. Найти самые лучшие продукты по продажам, по количеству продаж и по профиту соответственно: \n" \
          f"[{Mapping.sales.value}] \n {best_products[Mapping.sales.value]} \n\n" \
          f"[{Mapping.quantity.value}] \n {best_products[Mapping.quantity.value]} \n\n" \
          f"[{Mapping.profit.value}] \n {best_products[Mapping.profit.value]} \n\n\n" \
          "3. Найти самые худшие продукты по продажам, по количеству продаж и по профиту соответственно: " \
          f"[{Mapping.sales.value}] \n {worst_products[Mapping.sales.value]} \n\n" \
          f"[{Mapping.quantity.value}] \n {worst_products[Mapping.quantity.value]} \n\n" \
          f"[{Mapping.profit.value}] \n {worst_products[Mapping.profit.value]} \n\n\n" \
          f"4. Найти средний срок доставки товара клиенту: \n{average_time} \n\n\n" \
          f"5. Найти стандартное отклонение от среднего срока доставки товара клиенту: \n{deviation_time} \n\n\n" \

    print(out)


if __name__ == "__main__":
    main()
