# nias-macropad

this hackpad features 6 keys, a rotary encoder and an OLED display, and uses KMK firmware.

this is my first hardware project and it was SO MUCH FUN i literally couldn't stop and speedran the whole thing in two days. like i'm talking morning to night completely locked in.

would do it again 10/10

fusion 360 was really annoying to figure out. measuring everything to fit together properly took FOREVER.

making the PCB was actually fun though. routing traces felt like playing a game haha.

the hackclub slack was REALLY helpful even though I was just lurking the entire time :D

i think i'm also going to paint the top case later!

## Specifications:
- XIAO RP2040 brain
- 128x32 OLED Display
- 1 EC11 Rotary encoder
- 6 keys

<img width="900" alt="very final macropad assmb p" src="https://github.com/user-attachments/assets/8048de74-1ea1-462a-a4fd-13990753d4e0" />


<img width="900" alt="Screenshot 2026-01-17 135416" src="https://github.com/user-attachments/assets/054d8211-1fe8-4fbe-8825-12e7862a369c" />

### PCB & Schematics

<table>
<tr>
<td width="50%">
<img width="500" alt="PCB" src="https://github.com/user-attachments/assets/63c823c0-f0c7-4d97-90a0-f11ec93f7674" />
</td>
<td width="50%">
<img width="500" alt="Schematics" src="https://github.com/user-attachments/assets/bd6d6d42-e560-4a53-875f-182bb0bf2481" />
</td>
</tr>
<tr>
<td align="center"><b>PCB</b></td>
<td align="center"><b>Schematics</b></td>
</tr>
</table>

## Firmware:
The whole thing runs on KMK firmware.

The rotary encoder is a volume knob, press it to pause/play.

The 6 keys are mapped to everyday shortcuts:
- Ctrl+Z (Undo)
- Ctrl+Y (Redo)
- Ctrl+C (Copy)
- Ctrl+V (Paste)
- Alt+Tab (Switch windows)
- Ctrl+Tab (Switch tabs)

I don't know what to make the OLED display just yet, so it has some random text for now.

I'm planning on making the entire thing more interesting later...

## BOM:
- 1x Seeed XIAO RP2040 (Microcontroller)
- 6x Cherry MX switches
- 6x Compatible Keycaps
- 1x EC11 Rotary encoder with push button
- 1x Rotary encoder knob
- 1x SSD1306 OLED display (128x32, I2C)
- 1x Custom PCB
- 3D printed top plate & bottom case (preferred color: pastel blue, or any other pastel color) 
- 4x M3 bolts & heatset inserts
- 4x M3 bolts & heatset inserts
