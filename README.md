# MI424WR Revision 1 Router Vulnerability Analysis

## Introduction

This project was inspired by my interest for hardware hacking but my lack of electrical engineering knowledge. I have been seeing Electrical and Computer Engineering graduate programs, but I am unable to apply to them because I am not in an electrical engineering undergraduate program (I'm in computer science). I looked at the number of courses in an elecrical engineering degree and I saw that it would take a year or two, so I decided to start learning on my own. Topics like wireless communication, embedded systems, and control systems interest me, so I am going to explore all of them and how to perform vulnerability research on those systems.

The learning approach I took during this project was finding what I wanted to do, then finding how to do that and looking things up when I didn't understand. In this way, I was easily able to see how the base knowledge was useful to more complex topics (unlike school, where it often takes a while to realize the benefits of knowledge from previous courses).

## Disassembling the Router and Analyzing the PCB

After some initial learning about different circuit parts and serial communication protocols, I started looking for any old target I had laying around. This happened to be a router, but there are many other electronics that this process can be applied to.

I knew to look for the UART debugger first because I learned that it is often the easiest way to get a shell on the device and dump firmware. Lucklily, I could see a header through gaps in the router casing, which I suspected was UART.

![UART header pins peeking through the gap](./images/router_shell.jpg)

This was confirmed when I opened up to see the PCB. On the top left of the board, the full 6 pin header can be seen.

![Front of the PCB](./images/pcb_front.jpg)