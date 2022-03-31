import requests
import json
import time

# 1
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

my_dict_from_response = response.text

ser_to_dict_first_response = json.loads(my_dict_from_response)

my_token = ser_to_dict_first_response["token"]


# 2
etalon_status_of_not_ready_Job = "Job is NOT ready"
etalon_status_of_ready_job = "Job is ready"
wait_seconds = ser_to_dict_first_response["seconds"]

response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": my_token})

my_dict_from_response_with_token = response_with_token.text
ser_to_dict_second_response = json.loads(my_dict_from_response_with_token)

job_status = ser_to_dict_second_response["status"]

if job_status == etalon_status_of_not_ready_Job:
    print(
        "The program works correctly - ", job_status,
        "\nJob will be done after", wait_seconds, "seconds"
        )
else:
        print("Something was wrong. Please debug")

# 3

print("Please waiting for", wait_seconds, "seconds")

time.sleep(wait_seconds)
response_with_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": my_token})

my_dict_from_response_with_token_after_sleep = response_with_token.text
ser_to_dict_second_response = json.loads(my_dict_from_response_with_token_after_sleep)

job_status_after_sleep_time = ser_to_dict_second_response["status"]
my_result = ser_to_dict_second_response["result"]

if job_status_after_sleep_time == etalon_status_of_ready_job and my_result is not None:
    print(
        "The program worked correctly - ", job_status_after_sleep_time,
        "\nResult -", my_result
    )
else:
    print("Something was wrong. Please debug")








