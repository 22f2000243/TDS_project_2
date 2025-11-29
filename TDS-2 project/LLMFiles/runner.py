
import requests
import json

url = "https://tds-llm-analysis.s-anand.net/submit"
payload = {
    "answer": "03d8d9aaf2cd",
    "email": "22f2000243@ds.study.iitm.ac.in",
    "secret": "I_can_do_anything",
    "url": "https://tds-llm-analysis.s-anand.net/demo2-checksum"
}
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
