#!/usr/bin/env python3

# VSCO DOWNLOADER - TESTS
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

from vsco_downloader import *

sample_image = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
sample_video = "https://vsco.co/emmasuz/media/5c61243fbbb29b6617e3d26c"

def test_image_download1():
    assert download(sample_image, True) != 1

def test_image_download2():
    assert download(sample_image, False) != 1

def test_image_download3():
    assert len(download(sample_image, True)) == 1

def test_image_download4():
    assert len(download(sample_image, False)) == 1

def test_video_download1():
    assert download(sample_video, True) != 1

def test_video_download2():
    assert download(sample_video, False) != 1

def test_video_download3():
    assert len(download(sample_video, True)) == 2

def test_video_download4():
    assert len(download(sample_video, False)) == 1

def test_downloader_1():
    assert vsco_downloader(2, sample_image) == 0

def test_downloader_2():
    assert vsco_downloader(2, sample_video) == 0

def test_downloader_3():
    assert vsco_downloader("url", sample_image) == 0

def test_downloader_4():
    assert vsco_downloader("url", sample_video) == 0

def test_downloader_5():
    assert vsco_downloader(3, "../links.txt") == 0

def test_downloader_6():
    assert vsco_downloader("file", "../links.txt") == 0
