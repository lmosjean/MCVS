
Modular Computational Vision System v0.2

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
This is a computer vision system with the overall objective of integrating it with external MCUs such as STM32 and Arduino, as well as functioning on single-board computers.

Currently, the system is running on a PC with a webcam but can be adapted for single-board computers like Raspberry Pi or Orange Pi. It interprets gestures made with the right hand, counts the number of fingers shown, and uses this value to send commands to a microcontroller.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
It utilizes the Firmata protocol for serial communication with the MCU. 

To enable Bluetooth functionality, the 'Standard Firmata' sketch was modded to match the baud rate of the HC-05 bluetooth module(9600), it's perfectly possible to use an serial adapter like CH340 tho. 

Using this protocol enables remote commands to be sent to the microcontroller without the need to update the Arduino code for each new implementation, giving space for the creativity in the PC processing side. 

The ports can be used both as outputs and inputs. For example, you can control motors from the PC or read sensors and send the aquired data to your server for processing. 

_______________________________________________________________________________________________________________________________________________________________________
Future Implementations:

1. Object recognition
2. Face tracking (follow me)
3. MQTT + ESP32 protocol integration
4. Integration with MySQL for data storage
5. Safety locks in case of connection loss
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Hardware used:

- Arduino Pro Mini 5v
- Bluetooth Module (Baud Rate: 9600)
- L293 Motor Driver + Custom PCB
- LM7805 Voltage Regulator
- Mechanical components and toy car motors
- 2200mAh Li-Ion battery

Hardware developed for this project is currently in testing and will be made available soon.

- PCI Driver L293 (H-Bridge)
- PCI Arduino Standalone 

The PCBs were designed using Proteus 8.5 software and prototyped using CNC laser technology. You can find the detailed process here: [LINK]
_______________________________________________________________________________________________________________________________________________________________________

