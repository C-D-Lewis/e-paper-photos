# e-paper-photos

Show photos from various sources on a Waveshare e-paper 7.5in v2 display.

When run on a platform other than Raspberry Pi (i.e: not ARM) the display image
is written to `./render.png` instead, which is useful for quickly testing
changes.


## Setup

Follow the steps in the
[Waveshare wiki](www.waveshare.com/wiki/7.5inch_e-Paper_HAT) to install the
Python libraries for the 7.5 inch V2 e-paper display.


## Configuration

Copy `config.json.example` and add values appropriate to you:

| Name | Type | Description |
|------|------|-------------|
| `mode` | String | Mode - see below. |
| `args` | Object | Mode arguments - see below |


## Modes

### `single`

Show a single image. Arguments:

| Name | Type | Description |
|------|------|-------------|
| `path` | String | Path to the single image to show. |
| `full_width` | Boolean | Set to "true" to fit to screen width |

