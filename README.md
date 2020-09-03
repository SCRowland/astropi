# Astro Pi Experiments

Some code written to play with Raspberry pi with sense hat installed. I have called mine `astropi` on my local network, so all following commands refer to it by that name.

## Deployment

`scp -r code astropi:/home/pi`

## Installation

Install sense-hat libraries to the system:

`sudo apt-get install sense-hat`

## Running the code

`python3 code/hello_astro.py`