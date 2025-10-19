#!/usr/bin/env python3

# VSCO DOWNLOADER
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

version = "2.0.0"
date = "20251019"

import tls_client
import traceback as tb
import json
import sys
import os
import re

EXAMPLE_URL = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
REQUEST_HEADER = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "de,en-US;q=0.7,en;q=0.3",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Host": "vsco.co",
    "Pragma": "no-cache",
    "Priority": "u=0, i",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-GPC": "1",
    "TE": "trailers",
    "Upgrade-Insecure-Requests": "1"
}

def download(vsco_media_url, get_video_thumbnails = True, save = False):

    s = tls_client.Session(client_identifier="firefox_120")
    response = s.get(vsco_media_url, headers=REQUEST_HEADER)
    if response.status_code != 200:
        raise RuntimeError(f"GET responded with status code {response.status_code}!")
    data = response.content.decode("utf-8")
    data_cleaned_1 = str(data).split("<script>window.__PRELOADED_STATE__ =")[1]
    data_cleaned_2 = str(data_cleaned_1).split("</script>")[0]
    data_cleaned_3 = str(data_cleaned_2).strip()
    data_cleaned_4 = str(data_cleaned_3).replace("undefined", "\"\"").replace("\\x", "\\u00")
    data_cleaned_5 = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'', data_cleaned_4)

    try:
        json_data = json.loads(data_cleaned_5)
    except Exception as e:
        print("ERROR: Failed to load json data!")
        tb.print_exc()
        return 1

    media_urls = []
    try:
        medias = json_data["medias"]["byId"]
        for media in medias:
            info = medias[media]["media"]
            if not bool(info["isVideo"]) or get_video_thumbnails:
                media_url = "https://" + str(info["responsiveUrl"].encode().decode("unicode-escape"))
#                media_name = str(media) + ".jpg"
#                response = s.get(media_url, headers=REQUEST_HEADER_IMG)
#                if response.status_code >= 200:
#                    warnings.warn(RuntimeWarning(f"GET responded with status code {response.status_code}!"))
#                if save:
#                    with open(media_name, "wb") as f:
#                        f.write(response.content)
                media_urls.append(media_url)
            if bool(info["isVideo"]):
                media_url = "https://" + str(info["videoUrl"].encode().decode("unicode-escape"))
#                media_name = str(media) + ".mp4"
#                response = s.get(media_url, headers=REQUEST_HEADER_IMG)
#                if response.status_code >= 200:
#                    warnings.warn(RuntimeWarning(f"GET responded with status code {response.status_code}!"))
#                if save:
#                    with open(media_name, "wb") as f:
#                        f.write(response.content)
                media_urls.append(media_url)
    except Exception as e:
        print("ERROR: Failed to extract image/video location!")
        tb.print_exc()
        return 1

    return media_urls

"""
def vsco_downloader(option = None, arg = None):

    if option == 1 or option == None:
        link = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
        prompt_str = "Please enter an URL to an VSCO post e. g. " + link + " \n"
        url = input(prompt_str)
        r = download(url)
        if r != 1:
            print("Download successfully!")
            return 0
        else:
            print("ERROR encountered: Download may have failed!")
            return 1

    if option == 2 or option == "url":

        if arg == None:
            print("ERROR: No URL provided. Exiting!")
            return 1

        r = download(arg)
        if r != 1:
            print("Download successfully!")
            return 0
        else:
            print("ERROR encountered: Download may have failed!")
            return 1

    if option == 3 or option == "file":

        if arg == None:
            print("ERROR: No file provided. Exiting!")
            return 1

        with open(arg, "r") as f:
            lines = f.readlines()
            f.close()
        count = int(len(lines))
        counter = 1
        percent = [ \
            "[--------------------]", "[#-------------------]",
            "[##------------------]", "[###-----------------]",
            "[####----------------]", "[#####---------------]",
            "[######--------------]", "[#######-------------]",
            "[########------------]", "[#########-----------]",
            "[##########----------]", "[###########---------]",
            "[############--------]", "[#############-------]",
            "[##############------]", "[###############-----]",
            "[################----]", "[#################---]",
            "[##################--]", "[###################-]",
            "[####################]"]
        r = 0
        for line in lines:
            l = line.lstrip().rstrip()
            r_ = download(l)
            status = counter/count
            status_bar = percent[int(status * 20)]
            status_msg = "Downloaded " + str(line) + "\n" + \
                "Download at " + str(status*100) + "% \n" + \
                status_bar + "\n"
            counter = counter + 1
            print(status_msg)
            if r_ == 1:
                r = 1
        if r == 0:
            print("Downloaded all Posts successfully!")
            return 0
        else:
            print("ERROR encountered: Downloads of one or more posts may have failed!")
            return 1

    if option not in [1, 2, 3, None, "url", "file"]:
        print("ERROR: Unrecognized option. Exiting!")
        return 1

if __name__ == '__main__':
    if len(sys.argv) == 1:
        result = vsco_downloader()
        print(result)
    elif len(sys.argv) == 2:
        if not os.path.isfile(sys.argv[1]):
            result = vsco_downloader("url", sys.argv[1])
            print(result)
        else:
            result = vsco_downloader("file", sys.argv[1])
            print(result)
    else:
        print("Wrong usage! Try running without parameters or read documentation!")
"""
