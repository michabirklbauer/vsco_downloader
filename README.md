![vsco_downloader.py](https://github.com/michabirklbauer/vsco_downloader/workflows/vsco_downloader.py/badge.svg)

# VSCO Downloader

A python script to download images and videos in full resolution from [VSCO](https://vsco.co/).

## Requirements
- Python (version 3.7 or higher)

## Features
- Download a single image or video by running the script and providing the link as input.
- Download a single image or video by passing the link as a parameter to the script.
- Download multiple images or videos by passing a filelist to the script (as parameter).

## Usage

Examples:

- ### Download a single image:
  ```shell
  python vsco_downloader.py
  Please enter an URL to an VSCO post e. g. https://vsco.co/emilieristevski/media/561f648001146426743090fa
  https://vsco.co/emilieristevski/media/561f648001146426743090fa
  ```
- ### Download a single image using parameters:
  ```shell
  python vsco_downloader.py https://vsco.co/emilieristevski/media/561f648001146426743090fa
  ```
- ### Download multiple image using a filelist (e.g. links.txt):
  ```shell
  python vsco_downloader.py links.txt
  ```
- ### Using the python functions:
  ```python
  from vsco_downloader import download

  sample_image = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
  sample_video = "https://vsco.co/emmasuz/media/5c61243fbbb29b6617e3d26c"

  # downloading an image
  download(sample_image)

  # downloading a video
  download(sample_video)

  # downloading a video but not the thumbnail
  download(sample_video, get_video_thumbnails = False)
  ```
- ### Using the web interface
  A web version is available [here](http://89.58.32.151:8503/).
