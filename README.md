# my own macropad (kpad)
### 3x3 macropad with an oled screen

this project is a macropad i designed to fill my needs using my pc what it has :

- 3x3 MX switches (programmable)
- oled screen
- 3d case (optional)
- firmaware


## the schematics

<img width="951" height="715" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/0e5b0921-57cd-40a9-8a73-5fb4d9a641c2" />

- using the xiao rp2040 as our microcontroller
- connecting the switches directly using "single pin method"
- using i2c with the oled screen 

## PCB design 

<img width="448" height="445" alt="531800851-49c27150-cd61-4b0f-911c-a4945d69f0c4" src="https://github.com/user-attachments/assets/5285b30a-d52e-4785-8dec-b5b82b96a4e3" />

## 3d case 

<img width="369" height="377" alt="531800389-01e19b98-0800-49fd-bf8c-9a057464779e" src="https://github.com/user-attachments/assets/135328b9-8b14-4285-b117-1d20e7596b09" />
<img width="526" height="395" alt="531776715-4a29475f-67ef-4243-8563-37fa1b546242" src="https://github.com/user-attachments/assets/d5accb28-ef3d-4d4b-b999-1634464262bb" />





bom
-
| Reference | Component | Footprint | Qty | Description | price | link |
|---|---|---|---|---|---|---|
| U1 | Seeed XIAO RP2040 | XIAO-RP2040-DIP | 1 | Main Microcontroller (MCU) | 
| SW1-SW9 | MX Switches | SW_Cherry_MX_1.00u_PCB | 9 | 1.00u Mechanical switches |
| J1 | 0.91" OLED Display | PinHeader_1x04_P2.54mm | 1 | 128x32 I2C OLED Screen |
| J2 | pcb | pcb | 1 | the board (alr bought) |
| J3 | 3d case | case | 1 | the case (alr bought) |


