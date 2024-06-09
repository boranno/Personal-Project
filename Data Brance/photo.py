import requests
import base64

url = "http://software.diu.edu.bd:8006/profileUpdate/photograph"

# Add any necessary headers
headers = {
    "accesstoken": "2db4bd8e-0f98-11ef-a067-054decbc0481",  # Make sure to replace this with your access token
    "Referer": "http://studentportal.diu.edu.bd/",
    "Origin": "http://studentportal.diu.edu.bd"
}

# Make the GET request
response = requests.get(url, headers=headers)
print(response.content)

# Check if the request was successful (status code 200)
base64_data =response.content
# Decode the Base64 data
image_data = base64.b64decode(base64_data)

# Save the decoded data as an image file
with open("photoborrannobase.jpg", "wb") as f:
    f.write(image_data)

print("Photo downloaded successfully.")