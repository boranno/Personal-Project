import requests
import os

def download_image(url, save_path):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open a new file in binary write mode
        with open(save_path, 'wb') as file:
            # Write the content of the response to the file
            file.write(response.content)
        print("Image downloaded successfully!")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# Example usage
image_url = "https://avatars.githubusercontent.com/u/48504390?v=4"
save_location = "imageBoranno.jpg"
download_image(image_url, save_location)
