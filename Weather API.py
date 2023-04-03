import requests
import csv

# URL of the API endpoint
location=['London','Toronto','Delhi','Tokyo','Mumbai','Rome','Cairo','Moscow','Jakarta','Kolkata']
api_key='c709407055bb0782127685592982bc32'

# Open the CSV file for writing in append mode
with open('weather_data.csv', mode='a', newline='') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Check if the file is empty; if so, write the header row
    if file.tell() == 0:
        writer.writerow(['temp', 'temp_min', 'temp_max', 'name'])

    # Iterate over the list of locations
    for city in location:
        # Construct the URL for the API request
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        # Send a GET request to the API endpoint
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON data
            data = response.json()

            # Extract the necessary data
            temp = data['main']['temp']
            temp_min = data['main']['temp_min']
            temp_max = data['main']['temp_max']
            name = data['name']

            # Write the data to the CSV file
            writer.writerow([temp, temp_min, temp_max, name])

            # Print the data to the console
            # print(f"Temperature: {temp} K")
            # print(f"Minimum temperature: {temp_min} K")
            # print(f"Maximum temperature: {temp_max} K")
            # print(f"City: {name}")
        else:
            print("Error fetching data from the API")
# Open the CSV file for reading
with open('weather_data.csv', mode='r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Initialize variables for the min and max temperatures
    min_temp = float('inf')
    max_temp = float('-inf')

    # Iterate over the rows in the CSV file
    for row in reader:
        # Extract the temperature data
        temp = float(row[0])
        temp_min = float(row[1])
        temp_max = float(row[2])
        location = row[3]

        # Update the min and max temperatures if necessary
        if temp < min_temp:
            min_temp = temp
            min_location = location
        if temp_max > max_temp:
            max_temp = temp_max
            max_location = location

    # Print the min and max temperatures along with location to the console
    print(f"Minimum temperature: {min_temp} K, Location: {min_location}")
    print(f"Maximum temperature: {max_temp} K, Location: {max_location}")
