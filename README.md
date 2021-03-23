# e-paper-photos

E-paper photos rotations etc.


## Setup

Follow the steps in the
[Waveshare wiki](www.waveshare.com/wiki/7.5inch_e-Paper_HAT) to install the
Python libraries for the 7.5 inch V2 e-paper display.


## Configuration

Copy `config.json.example` and add values appropriate to you:

| Name | Type | Description |
|------|------|-------------|
| `fff` | String | bar |


## Show an image

```shell
python3 show_image.py $imagePath [-f]
```

* `-f` - Widen to full-screen.

When run on a platform other than Raspberry Pi (i.e: not ARM) the display image
is written to `./render.png` instead, which is useful for quickly testing
changes.
