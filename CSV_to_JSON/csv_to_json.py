import csv
import json

# Open and read the CSV file
with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # Convert CSV data into a list of dictionaries
    data = list(csv_reader)

# Write the data into a JSON file
with open("students.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON.")
print("Output file: students.json")
