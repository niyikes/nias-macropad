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

<img width="960" alt="final macropad assembled" src="https://github.com/user-attachments/assets/7fde7620-1a69-4aa7-b3e0-34c0ecf64e69" />

<img width="1189" alt="CAD Model" src="https://github.com/user-attachments/assets/3fd4fbd6-ab34-406e-af7c-99f8d61320ff" />

### PCB & Schematics

<table>
<tr>
<td width="50%">
<img width="205" alt="PCB" src="https://github.com/user-attachments/assets/320e209a-ff8f-4d13-a3d3-85ca91b5c41c" />
</td>
<td width="50%">
<img width="301" alt="Schematics" src="https://github.com/user-attachments/assets/9c76f049-2b70-4683-bd14-61efb99ac4fe" />
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
- 3D printed top plate & bottom case
- 4x M3 bolts & heatset inserts
- 4x M3 bolts & heatset inserts
