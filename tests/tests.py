#!/usr/bin/env python3

# VSCO DOWNLOADER - TESTS
# 2021 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

from vsco import get_links

sample_image = "https://vsco.co/emilieristevski/media/561f648001146426743090fa"
sample_video = "https://vsco.co/emmasuz/media/5c61243fbbb29b6617e3d26c"


def test_image1():
    assert len(get_links(sample_image, True)) == 1


def test_image2():
    assert len(get_links(sample_image, False)) == 1


def test_video1():
    assert len(get_links(sample_video, True)) == 2


def test_video2():
    assert len(get_links(sample_video, False)) == 1
