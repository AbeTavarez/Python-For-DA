import requests

# url = "https://jsonplaceholder.typicode.com/users/1"

# req = requests.get(url)

# json text
# print(req.text)

# python dictionary
# user_dict = req.json()

# user_dict["level"] = 1
# print(user_dict["level"])

# =======================
import json

with open('./data/data.json') as json_file:
#Deserialize data from the file into Python dictionary object.
  data = json.load(json_file)
  data['isPresent'] = True
  
  print(data)

# ===================================
# Your object (e.g., a dictionary)
my_object = {
    "name": 'John',
    "age": 30,
    "city": "New York"
}

# Convert to JSON
json_string = json.dumps(my_object)

print(json_string)


# ========================
data = {'courses':[]}

data[ 'courses'].append({
'Course Id': 'CSIPLO1',
'Course Name': 'Introduction to Java',
'Instructor': 'Marcial Cordon'
})

data[ 'courses'].append({
'Course Id': 'CSIPLO2',
'Course Name': 'Introduction to Python',
'Instructor': 'Young Wook Baek'
})

with open('courses.json', 'w') as json_file:
  json.dump(data, json_file)
  
  
# =====================
unicodeData= {
    "string1": "明彦",
    "string2": u"\u00f8",
    'String3': 'école'
}

print("\nunicode Data is ", unicodeData)

encodedUnicode = json.dumps(unicodeData, ensure_ascii=False) # use dump() method to write it in file

print("JSON character encoding by setting ensure_ascii=False", encodedUnicode)
print("Decoding JSON", json.loads(encodedUnicode))

