# Read csv file and split string using string methods
with open('./data/courses.csv', mode='r+') as csv_file:
    for line in csv_file.readlines():
        # row = line.strip().split(',')
        # print(row)
        # print(row[0])
        
        # row = line.strip().split(',')
        # print('ROW: ', row)
        # print(f'{row[0]}\t{row[1]}\t{row[2]}')  # we can format the output

        c_id, c_name, instructor = line.strip().split(',')
        print(f'{c_id}\t{c_name}\t{instructor}')  # we can format the output

# Use the csv module to work with csv file
import csv

with open('./data/courses.csv') as csv_file:
    # print(csv_file.read())
    
    csv_reader = csv.reader(csv_file)
    print(csv_reader) # csv object
    
    for line in csv_reader:
        # print(line)
        print(line[0])
        
        
# Open the CSV file for writing
with open('output.csv', 'w', newline='') as file:
   # Create a CSV writer object
   csv_writer = csv.writer(file)

   # Write rows to the CSV file
   csv_writer.writerow(['Name', 'Age', 'City'])
   csv_writer.writerow(['John', '25', 'New York'])
   csv_writer.writerow(['Alice', '30', 'San Francisco'])

        
