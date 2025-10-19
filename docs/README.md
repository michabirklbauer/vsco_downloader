# VSCO Downloader by Micha Birklbauer

A simple python library to extract raw image and video paths from [VSCO](https://www.vsco.co/) posts.

## Requirements

- Python (version 3.10 or higher)

## Usage

Examples:

- ### Using the python functions:
  ```python
  >>> from vsco import get_links

  >>> sample_image = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
  >>> sample_video = "https://vsco.co/emmasuz/media/5c61243fbbb29b6617e3d26c"

  >>> # downloading an image
  >>> get_links(sample_image)
  ['https://im.vsco.co/1/51a9887c50f8151/561f648001146426743090fa/vsco_101515.jpg']

  >>> # downloading a video
  >>> get_links(sample_video)
  ['https://im.vsco.co/aws-us-west-2/aaf64f/597912/5c61243fbbb29b6617e3d26c/5c61243fbbb29b6617e3d26c.jpg',
   'https://img.vsco.co/aaf64f/597912/5c61243fbbb29b6617e3d26c/5c61243fbbb29b6617e3d26c.mp4']

  >>> # downloading a video but not the thumbnail
  >>> get_links(sample_video, get_video_thumbnails = False)
  ['https://img.vsco.co/aaf64f/597912/5c61243fbbb29b6617e3d26c/5c61243fbbb29b6617e3d26c.mp4']
  ```

## GUI

A web version is available [here](http://89.58.32.151:8503/).

## License

[MIT License](https://github.com/michabirklbauer/vsco_downloader/blob/master/LICENSE.md)

## Download
- ZIP: [DOWNLOAD](https://github.com/michabirklbauer/vsco_downloader/archive/master.zip)
- TAR.GZ: [DOWNLOAD](https://github.com/michabirklbauer/vsco_downloader/archive/master.tar.gz)

## Contact
- Website: [michabirklbauer.github.io](https://michabirklbauer.github.io/)
- Contact: [micha.birklbauer@gmail.com](mailto:micha.birklbauer@gmail.com)
