#!/usr/bin/env python3

# VSCO Downloader GUI
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

"""
#####################################################
##                                                 ##
##            -- STREAMLIT MAIN APP --             ##
##                                                 ##
#####################################################
"""

import streamlit as st
from vsco_downloader import download as d

# main page content
def main_page():

    title = st.title("VSCO Downloader")

    general_description = \
    """
    VSCO Downloader is a simple script to extract raw image and video paths from [VSCO](https://www.vsco.co/) posts.
    """
    description = st.markdown(general_description)

    header_1 = st.subheader("Extract Post Media", divider = "rainbow")

    url = st.text_input("VSCO Post URL:",
                        placeholder = "https://vsco.co/emilieristevski/media/561f648001146426743090fa",
                        help = "URL of the VSCO post from which media should be extracted.")

    l1, l2, center_button, r1, r2 = st.columns(5)

    with center_button:
        download = st.button("Download!", type = "primary", use_container_width = True)

    if download:
        if url is None or url.strip() == "":
            url_err = st.error("URL of the post has to be provided!")
        media_urls = d(url, True, False)
        header_2 = st.subheader("Extracted Post Media", divider = "rainbow")
        display_media_urls = st.markdown("\n".join([f"- Found media url: [{media_url}]({media_url})" for media_url in media_urls]))

# side bar and main page loader
def main():

    about_str = \
    """
    VSCO Downloader is a simple script to extract raw image and video paths from [VSCO](https://www.vsco.co/) posts.
    """

    st.set_page_config(page_title = "VSCO Downloader",
                       page_icon = ":camera:",
                       layout = "wide",
                       initial_sidebar_state = "expanded",
                       menu_items = {"Get Help": "https://github.com/michabirklbauer/vsco_downloader/discussions",
                                     "Report a bug": "https://github.com/michabirklbauer/vsco_downloader/issues",
                                     "About": about_str}
                       )

    title = st.sidebar.title("VSCO Downloader")

    div_1 = st.sidebar.subheader("", divider = "rainbow")

    logo = st.sidebar.image(".streamlit/ico/download-icon.png",
                            caption = "VSCO Downloader is a simple script to extract raw image and video paths from VSCO posts.")

    #doc = st.sidebar.markdown(about_str)

    div_2 = st.sidebar.subheader("", divider = "rainbow")

    info_str = ""
    info_str += "- **Contact:**  \n  [micha.birklbauer@gmail.com](mailto:micha.birklbauer@gmail.com)\n"
    info_str += "- **License:**  \n  [MIT License](https://github.com/michabirklbauer/vsco_downloader/blob/master/LICENSE.md)\n"
    info_str += "- **Project Page:**  \n  [GitHub](https://github.com/michabirklbauer/vsco_downloader/)"
    info = st.sidebar.markdown(info_str)

    main_page()

if __name__ == "__main__":

    main()
