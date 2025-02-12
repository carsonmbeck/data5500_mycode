
import requests
import json
from datetime import datetime

def convert_date(date_int):
   
    #tihs Converts an integer date in the format YYYYMMDD (e.g. 20210504) to a datetime object.

    date_str = str(date_int)
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:])
    return datetime(year, month, day)

def format_date(date_int):
   
    #Formats the integerr date into a human-readable string as Month Day Year.
    
    dt = convert_date(date_int)
    return dt.strftime("%B %d, %Y")

def main():
    # Set state code and full state name
    state_code = "pa"
    state_name = "Pennsylvania"

    # Build the API URL for the given state
    url = f"https://api.covidtracking.com/v1/states/{state_code}/daily.json"

    # Try to retrieve the data from the API
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad status codes
    except requests.RequestException as e:
        print("Error accessing the API:", e)
        return

    # Try to parse the JSON data returned by the API
    try:
        data = response.json()
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return

    # Save the JSON data to a file named "<state_code>.json"
    try:
        with open(f"{state_code}.json", "w") as json_file:
            json.dump(data, json_file, indent=2)
    except IOError as e:
        print("Error writing JSON file:", e)
        return

    # Initialize variables for analysis
    positive_increases = []     # List to store daily positive case increases
    highest_increase = -1       # Highest daily increase observed
    date_highest = None         # Date corresponding to the highest daily increase
    most_recent_zero_date = None  # Most recent date with zero new cases

    # Dictionary to store aggregated monthly totals.
   
    monthly_totals = {}

    # Loop through each day's data in the JSON list
    for entry in data:
        # Ensure the entry contains 'positiveIncrease' data
        if "positiveIncrease" in entry and entry["positiveIncrease"] is not None:
            increase = entry["positiveIncrease"]
            positive_increases.append(increase)

            # Check if this day has the highest increase so far
            if increase > highest_increase:
                highest_increase = increase
                date_highest = entry["date"]

            # If the day's increase is 0, check if it is more recent than the current record
            if increase == 0:
                if (most_recent_zero_date is None) or (entry["date"] > most_recent_zero_date):
                    most_recent_zero_date = entry["date"]

            # Aggregate monthly totals
            date_obj = convert_date(entry["date"])
            year = date_obj.year
            month = date_obj.month
            key = (year, month)
            monthly_totals[key] = monthly_totals.get(key, 0) + increase

    # Calculate the average daily positive case increase
    if positive_increases:
        average_increase = sum(positive_increases) / len(positive_increases)
    else:
        average_increase = 0

    # Identify the month/year with the highest and lowest total new cases
    if monthly_totals:
        highest_month_year = max(monthly_totals, key=lambda k: monthly_totals[k])
        lowest_month_year = min(monthly_totals, key=lambda k: monthly_totals[k])
    else:
        highest_month_year = (None, None)
        lowest_month_year = (None, None)

    # Format the dates for display. If no data is found, use "N/A".
    highest_date_str = format_date(date_highest) if date_highest else "N/A"
    most_recent_zero_date_str = format_date(most_recent_zero_date) if most_recent_zero_date else "N/A"
    if highest_month_year[0] is not None:
        highest_month_year_str = datetime(highest_month_year[0], highest_month_year[1], 1).strftime("%B %Y")
    else:
        highest_month_year_str = "N/A"
    if lowest_month_year[0] is not None:
        lowest_month_year_str = datetime(lowest_month_year[0], lowest_month_year[1], 1).strftime("%B %Y")
    else:
        lowest_month_year_str = "N/A"

    # Output the statistics to the console
    print("Covid confirmed cases statistics")
    print("State name:", state_name)
    print("Average number of new daily confirmed cases for the entire state dataset:",
          round(average_increase, 2))
    print("Date with the highest new number of covid cases:", highest_date_str)
    print("Most recent date with no new covid cases:", most_recent_zero_date_str)
    print("Month and Year, with the highest new number of covid cases:", highest_month_year_str)
    print("Month and Year, with the lowest new number of covid cases:", lowest_month_year_str)

if __name__ == "__main__":
    main()
