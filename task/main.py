from time import perf_counter_ns
from datetime import datetime, timedelta

expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
}

def time_measurement(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter_ns()
        result = func(*args, **kwargs)
        end_time = perf_counter_ns()
        execution_time_ns = (end_time - start_time)
        print(f"Execution time: {execution_time_ns} ns")
        return result
    return wrapper

def get_first_sunday(year_and_month):
    year, month = map(int, year_and_month.split("-"))
    first_day = datetime(year, month, 1)
    days_until_sunday = (6 - first_day.weekday()) % 7
    first_sunday_date = first_day + timedelta(days=days_until_sunday)
    return first_sunday_date

def find_median(sorted_combined_expenses):
    n = len(sorted_combined_expenses)

    if n % 2 == 1:
        return sorted_combined_expenses[n // 2]
    else:
        mid1 = sorted_combined_expenses[n // 2 - 1]
        mid2 = sorted_combined_expenses[n // 2]
        return (mid1 + mid2) / 2

def solution():
    """
    Main optimizations provided:
    1. Check the date of first sunday of each month
    2. Sort the days in months (in order to reduce iterations)
    3. Prohibits days until first sunday is encountered
    4. Extending "combined_expenses" list is Big O(k) operation, where
       k is the length of the list being added at the end of existing one
    5. List of all expenses thorough the year is then sorted
    6. Median of the sorted list is found
    
    Sorting used: built-in function sorted(), which is, under the hood,
    The "Timsort" algorithm. Timsort is a hybrid sorting algorithm derived
    from merge sort and insertion sort.
    """
    individual_expenses_names = ["food", "fuel"]
    combined_expenses = []
    for year_and_month, days in expenses.items():
        first_sunday_date = get_first_sunday(year_and_month=year_and_month)

        for day in sorted(days):
            if int(day) <= first_sunday_date.day:
                for i in individual_expenses_names:
                    combined_expenses.extend(days[day].get(i, []))
    if combined_expenses:
        sorted_combined_expenses = sorted(combined_expenses)
        return find_median(sorted_combined_expenses)
    else:
        return None

@time_measurement
def main():
    ans = solution()
    print(f"Median: {ans}")

if __name__ == "__main__":
    main()