- [Raspberry Pi RGB Xmas Tree Additional Lighting Sequence](#raspberry-pi-rgb-xmas-tree-additional-lighting-sequence)
  - [Pre-requisites](#pre-requisites)
  - [How to run the script](#how-to-run-the-script)
  - [Scripts](#scripts)
    - [single_colour.py](#single_colourpy)
    - [gradient_by_row.py](#gradient_by_rowpy)
    - [gradient_by_row_with_reverse.py](#gradient_by_row_with_reversepy)
    - [random_sparkle.py](#random_sparklepy)
    - [vertical_pattern.py](#vertical_patternpy)
    - [row_by_row.py](#row_by_rowpy)
    - [snake.py](#snakepy)
  - [How to keep your light sequence running indefinitely](#how-to-keep-your-light-sequence-running-indefinitely)
    - [How to stop `long_run.sh`](#how-to-stop-long_runsh)

# Raspberry Pi RGB Xmas Tree Additional Lighting Sequence 

Additional lighting sequence for the Raspberry Pi RBG Xmas tree which can be purchased [here]. They also provide some code and instructions to [start you off]. It does provide a good starting point.

This my attempt at learning how to program the lights and building more lighting sequences.

## Pre-requisites
Before you can run these scripts you will need to install the following modules:
* colorzero
* time
* decimal
* numpy

To install a module e.g. colorzero you need to run the command:

```Python
python3 -m pip install colorzero
```

## How to run the script
Assuming you have gone through the instructions given in Pi Hut's example project you can run the scripts found here by running `python3 <script_name>`. For example,

```
python3 gradient_by_row.py
```

To stop the script just press `ctrl + c` i.e. `ctrl` and `c` together. (All you need to do is just press `c` while `ctrl` is still pressed.)

## Scripts

### single_colour.py
A simple script to test out colours. Some of the formats you can use to represent colours are:

* Colour names `Color(('blue')`
* Hexadecimal value `Color('#fec89a')`
* RGB e.g. `Color((0,255,0))`

### gradient_by_row.py
This lights up the xmas tree each pixel at a time moving up each row. The colour of each pixel forms a gradient between two colours. For example you could start with the first pixel blue and slowly transition each pixel to red at the top. The script contains a list of colour pairs that you can add to or modify. 

After lighting up from bottom to top the lights will pause for one second before switching off and a second colour pair will be picked at random and the light sequence will start again. 

### gradient_by_row_with_reverse.py
This does the same thing as before but once the lights are all lit up it will start turning off the pixels one by one from the top down. When it reaches the bottom a new colour pair will be chosen and the tree will light up again.

By default it picks a pair of colours from a fix list of colours. I've included a few functions that generate colours in different ways:

* generate_random_gradient_by_pair - This function generates a pair of colours from a list of predefined pairs.
* generate_random_gradient_by_hex_pair - Same as before but the colours are not defined in hexadcimal. You can use sites look [coolors] to create gradients and get the hexadecimal values for them.
* random_colour - This function generates a random colour in a RGB tuple format i.e. (255,0,0)

### random_sparkle.py
This is a slight variaion on the `randomsparkles.py` found in the PiHut examples. It still lights up random pixels with random colours. But this script will also turn of pixels at random. So you should never end up with a fully lit tree. There should always be around half of the tree lit with one of them changing to a random colour ever 0.1 seconds. This give it a bit more of a sparkle look. 

You can try modifying how quickly the pixel changes colour as well as how likely a pixel will be turned off.

### vertical_pattern.py
This script turns on the pixels in vertical columns along each blade of the tree. After turning all the pixels for one colour it will then pick another random colour and start change all the pixels vertically and so on so forth.

### row_by_row.py
This lights up the tree row by row. It does this by telling tree which pixel to turn on in a single array. At the moment it lights up in white but could easily be modified to light up in different colours. 

The tree takes a list of 25 tuples which represents RGB. In this instance you can use hexadecimal values.

### snake.py
This is variation on `gradient_by_row.py` that create a string of 4 pixels that travels up the tree. At the moment it only goes up the tree. See if you can make it come back down when it reaches the top.

----

***Note***: On some of the script I've left off the top most pixel (pixel #3) in the script because of personal preference.

***Note 2***: A little mod that may make the tree a bit more visually pleasing is to put a paper cone over the RGB xmas tree. You can use a coffee filter or just cut a circle out of a piece of paper and roll it into a cone. This will help diffuse the light and make it look less pixelated. If you do do this it would also be a good idea to use a brighter setting for LEDs. My quick little hack ended up looking like [this]

***Note 3***: The LEDs on the xmas tree can't represent all colours. (I don't know if it's becuase of the LEDs themselves, the chip that controls the LEDs or something else.) If the colour you enter isn't understood then it will show up white. If you choose a lighter shade of a colour it might also show up as white. I've found that vibrant colours work best. And don't even think about trying brown :) .

---

## How to keep your light sequence running indefinitely

You will notice that once you are not connected to your Raspberry Pi (if you are connected to is using ssh) or close your terminal/IDE (if you are working via Raspberry Pi's UI) that the lighting script will stop working. This is because the `python` process is killed when it's parent process i.e. your terminal or IDE exits. If doesn't mean anything to you, don't worry for now

[long_run.sh] is a little script that let's your lighting script run even when you are not connected to your Raspberry Pi anymore. 

To use this, open `long_run.sh` and replace `<your_script>` with your lighting script. For example if you wanted to run `gradient_by_row.py` on your tree all day long then you would update the code so that it looks like:

```Bash
setsid python3 gradient_by_row.py < /dev/zero &> /dev/null &
```

Basically what this is doing is running `python3` under a new process.

### How to stop `long_run.sh`
If you want to stop the long running script first you will have to find out the process ID that it's running under. To do that run the following command in your terminal:

```Bash
ps aux | grep python3
```
This will show you all process that mention `python3`. In the response there should be a line that looks similar to:

```Bash
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
ubuntu    645044 99.9  0.2  24916 18448 ?        Rs   Dec27 1729:06 python3 gradient_by_row_with_reverse.py
```

I have included the headings from each column but it won't be displayed on your output. (To see the column you can run `ps aux` which will list all process but it will be much harder to find the process we are looking for.)

The process ID is found under the `PID` column in the example it is `645044`. 

Next we are going to run a command to kill this process:

```Bash
kill 645044
```


[here]: https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi
[start you off]: https://github.com/ThePiHut/rgbxmastree
[long_run.sh]: scripts/long_run.sh
[coolors]: https://coolors.co/gradients
[this]: https://photos.app.goo.gl/ASrtkw665mumwcxS7
[single_colour.py]: scripts/single_colour.py
[gradient_by_row.py]: scripts/gradient_by_row.py
[gradient_by_row_with_reverse.py]: scripts/gradient_by_row_with_reverse.py
[random_sparkle.py]: scripts/random_sparkle.py
[vertical_pattern.py]: scripts/vertical_pattern.py
[row_by_row.py]: scripts/row_by_row.py
[snake.py]: scripts/snake.py