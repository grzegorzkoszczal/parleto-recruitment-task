import json
from datetime import datetime, timedelta
from test_case import expenses, year


def get_current_month():
    for month in expenses.items():
        print(month)

get_current_month()

def sort_days_in_month(month):
    sorted_month = sorted(month.items())
    return sorted_month


def is_within_first_sunday():
    for year_month_key in expenses:
        year, month = map(int, year_month_key.split("-"))
        print(year, month)

        first_day = datetime(year, month, 1)
        print(first_day)
        days_until_sunday = (6 - first_day.weekday()) % 7  # 6 is Sunday in weekday()
        first_sunday_date = first_day + timedelta(days=days_until_sunday)
        print(first_sunday_date)

def get_month_range():
    for month, days in year.items():
        print(month)
        # days = year.get(month, None)
        print(days.keys())
        is_within_first_sunday(month, days.keys())
        # for day, data in days.items():
        #     print(day)
        #     print(data)

        # parsed_month = datetime.strptime(month, "%Y-%m")
        # print(parsed_month)
        # day_of_week = parsed_month.strftime("%A")
        # print(day_of_week)
    # for month in expenses.items():
    #     print(f"Month? {month}")
    #     for day in expenses.get(month[0], None):
    #         print(f"Day? {day}")

    # parsed_date = datetime.strptime(date, "%Y-%m-%d")
    # print(type(parsed_date))
    # print(parsed_date)

    # day_of_week = parsed_date.strftime("%A")
    # print(type(day_of_week))
    # print(day_of_week)

    # get_first_sunday = ""

def find_median(sorted_tmp_bills):
    n = len(sorted_tmp_bills)

    if n % 2 == 1:
        return sorted_tmp_bills[n // 2]
    else:
        mid1 = sorted_tmp_bills[n // 2 - 1]
        mid2 = sorted_tmp_bills[n // 2]
        return (mid1 + mid2) / 2

def solution1():
    """
    Brute-force solution
    
    TODO:
    1. Get each month, such as "2023-01", "2023-03" etc.
    """
    for month, days in expenses.items():
        for day, bills in days.items():
            date = f"{month}-{day}"
            print(date)
            tmp_bills = []
            for bill in bills.values():
                for v in bill:
                    tmp_bills.append(v)
            print(tmp_bills)
            sorted_tmp_bills = sorted(tmp_bills)
            print(sorted_tmp_bills)
            median = find_median(sorted_tmp_bills)
            print(median)


    result = None
    pass
    return result

def solution2(expenses):
    """
    Optimized solution
    """
    result = None
    pass
    return result

def main():
    return solution1()

if __name__ == "__main__":
    main()