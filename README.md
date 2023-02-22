## Before you run the tracker

1. Clone the repository recursively:

`git clone --recurse-submodules https://github.com/AD-IQ/object-tracking.git`

If you already cloned and forgot to use `--recurse-submodules` you can run `git submodule update --init`

2. Make sure that you fulfill all the requirements: Python 3.8 or later with all [requirements.txt](https://github.com/AD-IQ/object-tracking/blob/master/requirements.txt) dependencies installed, including torch>=1.7. To install, run:

`pip install -r requirements.txt`

3. Take a sample video, store it in the root folder and change the link.py file.


## Tracking sources

Tracking can be run on most video formats

```bash
$ python track.py
```




## Cite

If you find this project useful in your research, please consider cite:

```latex
@misc{yolov5-DeepSort-2022,
    title={Real-time multi-camera total people count using Unique ID},
    author={Islam Saiful},
    howpublished = {\url{https://github.com/AD-IQ/object-tracking.git}},
    year={2022}
}
```
