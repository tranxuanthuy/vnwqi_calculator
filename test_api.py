import requests

url = "http://127.0.0.1:8000/calculate_vnwqi_csv"
files = {'file': open('data/dss1.csv', 'rb')}

response = requests.post(url, files=files)

if response.status_code == 200:
    with open('data/wqi_results_from_api.csv', 'wb') as f:
        f.write(response.content)
    print("File CSV kết quả đã được lưu.")
else:
    print(f"Lỗi: {response.status_code} - {response.text}")