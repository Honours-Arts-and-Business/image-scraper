from selenium import webdriver
import os
import requests
import io

from PIL import Image

PATH = os.getcwd() + '\\chromedriver.exe'
DOWNLOAD_PATH = os.getcwd() + '\\data'
print(PATH)


wd = webdriver.Chrome(PATH)

image_url = 'https://www.akc.org/wp-content/uploads/2017/11/Chihuahua-standing-in-three-quarter-view.jpg'


def download_image(download_path, url, filename):
    try:
        image_content = requests.get(url).content
        image_file = io.BytesIO(image_content)
        image = Image.open(image_file)
        file_path = download_path + filename

        with open(file_path, 'wb') as f:
            image.save(f, 'JPEG')

        print("SUCCESS")
    except Exception as e:
        print("FAILED")


download_image(DOWNLOAD_PATH, image_url, "\\chihuahua.jpg")
