## Inspiration

I was inspired to create this project after being faced with many obstacles after taking up interest with creating my own TAS files, or a series of frame-by-frame inputs to be ran on a video game console, allowing inhuman levels of input precision.

## What it does

This tool allows the average person to fill out an Excel spreadsheet with frame-by-frame inputs, and converts them to a hex file that can be ran on an Arduino Uno R3 as a USB controller for the Nintendo Switch.

I was unable to complete my code in the allotted time of the hackathon.  However, I was able to convert a CSV from a spreadsheet to a formatted TAS file, and only ran into problems when the trying to execute the compiled arduino code, which unfortunately would not run.
 
## How I built it

I was able to create my own TAS files thanks to a controller for the Nintendo Switch that has been reverse engineered, allowing for it to be simulated by an Arduino.  With the groundwork laid for this type of project by GitHub user "shinyquagsire23" (among others), the TAS community has a good understanding of how this controller works.  By sorting through his existing projects and the reverse engineered controller, I gained an understanding for how a TAS could be written for the controller and loaded onto an Arduino.  From there, I had to convert a CSV file from an excel spreadsheet to a usable C header file.  Then I adjusted the C code to read the header file I had created.  With this done, the makefile now compiles the hex file and is ready to be loaded onto an Arduino, and executed once plugged into the Nintendo Switch. 

## Challenges I ran into

I had trouble with a lot of the smaller formatting problems that I ran into, but aside from that I had a decent grasp on what I needed to do to reach my goal.  Further, despite my code compiling and  seeming to be unchanged from working builds of the project, the arduino stopped executing correctly and I was unable to resolve this problem.

## Accomplishments that I'm proud of

I'm proud of what I learned, and with what I completed during the event

## What I learned

Even if planning before beginning to code can seem excessive, sometimes it is necessary, and often saves more time than it costs.

## What's next for EZTas Switch Tool

Completing the functional code for the tool
Making my code more efficient in order to fit longer TAS files onto the Arduino.
Allowing for loopable code to run repeated inputs indefinitely.
