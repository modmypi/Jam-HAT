# Jam HAT Sample Code

![Jam Hat Sample Code](jamhat_github.png)

Welcome to the [Jam HAT](https://www.modmypi.com/jam-hat) repo! Here you'll find example code to get you started with the Jam Hat.

## Assembly
For assembly instructions please refer to our [Getting Started Guide](https://www.modmypi.com/blog/getting-started-with-the-jamhat).

## GPIO Zero Class Available
The Jam Hat has been included in version 1.5 of [GPIO Zero](https://github.com/RPi-Distro/python-gpiozero).

Ensure your version of GPIO Zero is up to date by opening a terminal window and typing:

```
sudo apt-get update
sudo apt-get install python3-gpiozero python-gpiozero
```

From there you can add the Jam Hat into your Python script by using.

```
from gpiozero import JamHat

jamhat = JamHat()
```

For more usage please refer to the [Getting Started Guide](https://www.modmypi.com/blog/getting-started-with-the-jamhat) or the [GPIO Zero docs](https://gpiozero.readthedocs.io/en/stable/api_boards.html#jamhat).

## Example Scripts

There are several scripts here to show you what you can do with the Jam Hat.

### button_led_piezo.py
This sample script shows you how to cycle through the leds, each led having a set pitch, then playing the pitch on the buzzer.

### button_piezo.py
This sample script shows you how to make the buzzer buzz with the push of a button.

### buttons.py
This sample script shows you how to use the buttons to create a simple counter.

### led_ants.py
Walk through the LEDs on the board.

### mario.py
Play the Mario Theme tune via the Buzzer. This currently uses RPi.GPIO but will be transferred over into GPIO Zero soon.
