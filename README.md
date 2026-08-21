# TapPad
TapPad speeds up annoying tasks. You can use the keys to assign custom macros on your device or use the rotary switch to control media. It has a customizable 0.91 inch OLED status display and a LED indicator.
<img width="1920" height="782" alt="Schematic" src="imgs/tap pad.png" />

# PCB Design 
The PCB was made on Kicad. It connects all 5 switches, rotory encoder switch, LED and the OLED display, to the Seeduino board. 
Schematic and PCB layout is as follows - 
<img width="1920" height="782" alt="Schematic" src="imgs/Schematic.png" />
<img width="1920" height="782" alt="PCB" src="imgs/tap pad pcb.png" />

# Case design 
Case designed on fusion for the pcb having 5 switches, one rotary encoder, an OLED display and the LED indicator with a USB-C port on the right side. It assembles via 4 magnets flushed inside the corners of the base and lid. 
It has grooves and extruded covers to fit the OLED display, rotary encoder and seeeduino USB-C. 
Triangular designs have been engraved along with a extruding "Tap Pad!" text to give it a unique design.  
<img width="1920" height="782" alt="Tap Pad Case" src="imgs/tap pad case.png" />

# Firmware
The firmware is made via QMK. It assigns the function keys from F13 to F17 to the 5 switches and lets you control media and volume through the rotary encoder. 
[OLED Display Control](https://github.com/Yash-Takhtani/TapPad/blob/main/Update%20display.py) can be used to set text on the display.

# Bill of Materials
Hackpad kit -
- 1x unsoldered Seeed XIAO RP2040
- 5x MX style switches
- 1x EC11 Rotary encoder
- 1x 0.91 inch OLED display
- 5x white blank DSA keycaps
- 1x SK6812 MINI-E LEDs

To be purchased with the grant - 
- PCB (from external PCB manufacturer like JLCPCB)
- 3D printed case and rotary cap from Printing Legion

Parts sourced myself -
- 4x 3mm x 1.5mm magnets
- 3x Short male pin headers (to match the compact spacing for OLED and Seeduino in case)

# Next Steps
After assembling the TapPad, I will be building a custom GUI software through which you can easily assign macros and setup display or LED, making it more purposeful.
