from pandas.core.frame import DataFrame

from orders.enums import Mapping


def get_sum_profit(frame: DataFrame) -> float:
    return frame[Mapping.profit.value].sum()


def get_count_sales_by_products(frame: DataFrame) -> DataFrame:
    fr = frame.groupby([Mapping.product_id.value, Mapping.product_name.value]).agg(
        {Mapping.profit.value: ['sum'], Mapping.sales.value: ['sum'], Mapping.quantity.value: ['sum']})
    fr.columns = [Mapping.profit.value, Mapping.sales.value, Mapping.quantity.value]
    return fr


def get_best_products(frame: DataFrame, count: int) -> dict:
    fr = get_count_sales_by_products(frame)
    return {
        Mapping.sales.value: fr.sort_values(Mapping.sales.value, ascending=False)[Mapping.sales.value][:count],
        Mapping.quantity.value: fr.sort_values(Mapping.quantity.value, ascending=False)[Mapping.quantity.value][:count],
        Mapping.profit.value: fr.sort_values(Mapping.profit.value, ascending=False)[Mapping.profit.value][:count]
    }


def get_worst_products(frame: DataFrame, count: int) -> dict:
    fr = get_count_sales_by_products(frame)
    return {
        Mapping.sales.value: fr.sort_values(Mapping.sales.value)[Mapping.sales.value][:count],
        Mapping.quantity.value: fr.sort_values(Mapping.quantity.value)[Mapping.quantity.value][:count],
        Mapping.profit.value: fr.sort_values(Mapping.profit.value)[Mapping.profit.value][:count]
    }


def get_average_time(frame: DataFrame) -> str:
    frame['average_time'] = frame[Mapping.end_date.value] - frame[Mapping.start_date.value]
    return frame['average_time'].mean()


def get_standard_deviation_time(frame: DataFrame) -> str:
    frame['average_time'] = frame[Mapping.end_date.value] - frame[Mapping.start_date.value]
    return frame['average_time'].std(ddof=1)
