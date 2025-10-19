#!/usr/bin/env python3

# VSCO DOWNLOADER
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

import tls_client
import traceback as tb
import json
import re

__version = "2.0.1"
__date = "20251019"

EXAMPLE_URL = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
REQUEST_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:144.0) Gecko/20100101 Firefox/144.0",
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
    "Upgrade-Insecure-Requests": "1",
}


def get_links(vsco_media_url: str, get_video_thumbnails: bool = True):
    s = tls_client.Session(client_identifier="firefox_120")
    response = s.get(vsco_media_url, headers=REQUEST_HEADER)
    if response.status_code != 200:
        raise RuntimeError(f"GET responded with status code {response.status_code}!")
    data = response.content.decode("utf-8")  # pyright: ignore[reportOptionalMemberAccess,reportAttributeAccessIssue]
    data_cleaned_1 = str(data).split("<script>window.__PRELOADED_STATE__ =")[1]
    data_cleaned_2 = str(data_cleaned_1).split("</script>")[0]
    data_cleaned_3 = str(data_cleaned_2).strip()
    data_cleaned_4 = (
        str(data_cleaned_3).replace("undefined", '""').replace("\\x", "\\u00")
    )
    data_cleaned_5 = re.sub(
        r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r"", data_cleaned_4
    )

    media_urls = []
    try:
        json_data = json.loads(data_cleaned_5)
    except Exception as _e:
        print("ERROR: Failed to load json data!")
        tb.print_exc()
        return media_urls

    try:
        medias = json_data["medias"]["byId"]
        for media in medias:
            info = medias[media]["media"]
            if not bool(info["isVideo"]) or get_video_thumbnails:
                media_url = "https://" + str(
                    info["responsiveUrl"].encode().decode("unicode-escape")
                )
                media_urls.append(media_url)
            if bool(info["isVideo"]):
                media_url = "https://" + str(
                    info["videoUrl"].encode().decode("unicode-escape")
                )
                media_urls.append(media_url)
    except Exception as _e:
        print("ERROR: Failed to extract image/video location!")
        tb.print_exc()
        return media_urls

    return media_urls
