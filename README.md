# MuonTelescope
Code for use and analysis of a muon telescope SP5621 by CAEN.
This project was done during the Ferienakademie 2022 in Sarntal.

To communicate with the telescope via a Raspberry Pi, follow these steps:
1. Connect GND, 5V and the + coincidence pins with the equivalent raspberry pi pins (check wiringPi for reference)
2. Compile the software using "g++ CoinCounter.cpp -o CoinCounter -lwiringPi"
3. Power on the coincidence module
4. Execute the software using "sudo ./CoinCounter"; the program will tell you the needed parameters