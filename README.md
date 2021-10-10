# Welcome

A smol and ez to use tool to convert images from different formats to `.ico` format. Yeah i was bored so made it.
Don't use it seriously, i jus made it for personal use and dunno if i will improve it or not.
It can be used from Command Line and Also one can use it through code too.

# Installation:

### PIP

`pip install git+https://github.com/mooncell07/icon-caster.git`


# CLI Instructions:

(which i copied from CLI)

### Usage:

`cast [-h] [-F FILEPATH] [-T TARGETPATH] [-S IMAGESIZE [IMAGESIZE ...]] [-V]`

Takes any image format and converts it to .ico format.

### Arguments:
```
  -h, --help            show this help message and exit
  -F FILEPATH, --filepath FILEPATH
                        Absolute file path to the image.
  -T TARGETPATH, --targetpath TARGETPATH
                        Absolute location where the processed image should be saved. (Must end with .ico)
  -S IMAGESIZE [IMAGESIZE ...], --imagesize IMAGESIZE [IMAGESIZE ...]
                        Size of processed image. Pass 2 dimensions.
  -V, --view            Whether to show the generated icon or no.
```

### Examples:

`cast -F ./flower.png -T ./flower.ico -V`

`cast -F ./flower.png -T ./flower.ico -S 255 255 -V`

# Direct Use:

### Example:

```py
from icon_caster import cast

args = cast.Args(
    filepath="./flower.png",
    targetpath="./flower.ico",
    imagesize=None,
    view=True,
)

caster = cast.Caster(args)
caster.generate()

```

- Here, passing `targetpath` is necessary.
- `imagesize` must be a list of two integers.

-------------