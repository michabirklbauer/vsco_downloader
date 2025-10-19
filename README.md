![vsco_downloader.py](https://github.com/michabirklbauer/vsco_downloader/workflows/vsco_downloader.py/badge.svg)

# VSCO Downloader

A python script to retrieve links for images and videos in full resolution from [VSCO](https://vsco.co/).

## Requirements

- Python (version 3.10 or higher)

## Usage

Examples:

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
- ### Using the web interface:
  A web version is available [here](http://89.58.32.151:8503/).
