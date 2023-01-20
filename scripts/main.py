
from distutils.command import upload
from turtle import back
import requests
from PIL import Image
import imageio
import hashlib
from io import BytesIO
import json
import base64
from datetime import datetime
import cairosvg
import io
import yaml

with open("config/rapid-api.yml") as file:
    # Load the YAML file
    api_config = yaml.safe_load(file)

# Get the base URL
base_url = api_config["base_url"]

mode_send_cat=["base64","url","byte"]
mode_receive_cat=["base64","url","byte"]
send_mode=mode_send_cat[2]
receive_mode=mode_receive_cat[2]
svg_mode=True
is_local=False
def get_time():
    time_now=str(datetime.now())
    time_now1=time_now[2:10]
    time_now2=time_now[11:13]
    time_now3=time_now[14:16]
    time_now4=time_now[17:21]
    time=time_now1+"_"+time_now2+time_now3+time_now4
    return time
def save_pic(image_string,time):
    pass
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="png")
    img_str = base64.b64encode(buff.getvalue()).decode()
    return img_str
def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    return False

# get the basic api calling info from yaml file
endpoint_url = base_url + api_config["endpoints"]["get_data"]["path"]
headers = api_config["headers"]
body = api_config["endpoints"]["post_data"].get("body", {})
query_params = api_config["endpoints"]["get_data"].get("query_params", {})

