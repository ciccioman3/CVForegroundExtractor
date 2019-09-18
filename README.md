# CVForegroundExtractor
This Python script extracts foreground from an image with white (or almost white) background using computer vision (OpenCV).


## Getting Started

This script uses [Mathematical morphology](https://en.wikipedia.org/wiki/Mathematical_morphology) to generate from an image with white-like background an output image of the extracted foreground in PNG with transparency. This allows to have an outimage with less image noise caused by white pixels in the expected foreground.

### Prerequisites

You need Python and [OpenCV](https://pypi.org/project/opencv-python/) that can be installed as follows:

```
pip install opencv-python
```

### Usage

You can run the Python script as it follows

```
python ForegroundExtractor.py input_image.png
```

The parameter (in the example "input_image.png") is the input image path that is going to be processed. The output image will be saved in the same folder and the file will be named "RES_input_image.png".

## Contributing

Every contributior is welcome. Please submitt pull requests with detailed comments/infos.


## Authors

* **Francesco Calabrese** - *Initial work* - [Ciccioman3](https://github.com/ciccioman3)

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details
