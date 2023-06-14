# Westbrook Miovision API Request
# Sebago Technics 2023 VT

def Get_Data():

    # Importing Libraries
    from datetime import datetime, timedelta, date
    import requests
    import json
    import csv
    import time
    import os
    
    print("1. Data Request through API\n")
    #start = time.time() #Start time when execution begins
    
    # Set the URL to the API endpoint
    url = "https://api.miovision.com/intersections/7499f7b1-1bb6-43b2-91af-45c8636cdada/tmc" #Westbrook Intersection URL
    
    # Set the API Key
    apiKey = ""
    
    # Prompt the user to input the start date and number of weeks
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    num_weeks = int(input("Enter number of weeks: "))

    # Convert the start date to a datetime object
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    # Calculate the end date based on the number of weeks
    delta = timedelta(weeks=num_weeks)
    end_date = start_date + delta - timedelta(seconds=1)

    # Calculate yesterday's date
    yesterday = date.today() - timedelta(days=1)

    # Create a list of start and end times for each day
    start_times = []
    end_times = []
    delta = timedelta(days=1)

    while start_date <= end_date:
        # Skip dates that are after yesterday
        if start_date.date() > yesterday:
            start_date += delta
            continue

        start_time = start_date.strftime("%Y-%m-%dT%H:%M")
        end_time = (start_date + delta - timedelta(seconds=1)).strftime("%Y-%m-%dT%H:%M")
        start_times.append(start_time)
        end_times.append(end_time)
        start_date += delta
    
    # Set the Headers for the API Request
    headers = {
        "accept": "application/json",
        "Authorization": apiKey,
    }
    
    for i in range(len(start_times)):
        # Set the Parameters for the Time Request
        params = {"endTime": end_times[i], "startTime": start_times[i]}
    
        response = requests.get(url, params=params, headers=headers)
    
        # Parse the JSON data
        data = json.loads(response.content)
    
        # Format the start time into a desired file name format
        start_time = datetime.strptime(params["startTime"], "%Y-%m-%dT%H:%M")
        file_name = start_time.strftime("%Y-%m-%d.csv")
        
        # Check if the file already exists
        if os.path.exists(r"A:\Data Analytics\ME Westbrook\Miovision\Raw Data\Intersection Name\\" + file_name):
            print(file_name + " already exists. Skipping...")
            continue
    
        # Create a CSV file with the desired file name
        with open(r"A:\Data Analytics\ME Westbrook\Miovision\Raw Data\Intersection Name\\" + file_name, "w", newline="") as f:
            writer = csv.writer(f)
    
            # Write the header row
            writer.writerow(["timestamp","class","entrance","exit","qty"])
    
            # Write each row of data to the CSV file
            for row in data:
                writer.writerow([row["timestamp"], row["class"], row["entrance"], row["exit"], row["qty"]])
    
        print(file_name+" created.")
    
    #end = time.time() #End time when the execution ends
    #total = end - start #Total time elapsed for executing a folder
    #total = str(timedelta(seconds=total))
    #print("Total time elapsed:",total,'\nDone.')
    print("Done.\n")
