

import requests

# Update this URL to your actual local IP (since Flask is running on your laptop)
url = "http://127.0.0.1:5000/detect_emotion"
                               #  url = 'http://192.168.0.100:5000/detect_emotion'  
files = {'video': open(r'C:\Users\hp\OneDrive\Desktop\emotion-monitoring-backend\test_video.mp4', 'rb')}

response = requests.post(url, files=files)

if response.status_code == 200:
    print("Response received:")
    print(response.json())
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response content:", response.text)
