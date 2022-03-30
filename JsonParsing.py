#Ex5: Парсинг JSON
import json

json_text = {
    "messages":
    [
        {"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},
        {"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}
    ]
}

ser_to_json = json.dumps(json_text)
ser_to_obj = json.loads(ser_to_json)

key = 'messages'

# To print a specific key
print(ser_to_obj[key][1])