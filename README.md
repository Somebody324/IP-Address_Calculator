# IP CIDR/VLSM Calculator

This Python script calculates subnet information for multiple networks based on a user-defined base network address and the required number of hosts for each network.

## Description
The script allows the user to specify:
- A base network address with a subnet mask (e.g., `192.168.100.0/24`).
- The number of subnets they wish to create.
- The required number of hosts for each subnet.

It then calculates the appropriate subnet mask (CIDR notation) for each network and outputs the following details:
- Subnet Mask (CIDR)
- Subnet Mask (Dotted Decimal Notation)
- Network Address
- Broadcast Address
- Host Range (First and Last Usable IP)

## How It Works
1. The user inputs the base network address, including the subnet mask (e.g., `192.168.100.0/24`).
2. The user specifies the number of networks to create.
3. For each network, the user inputs the required number of hosts.
4. The script calculates the smallest possible subnet size to accommodate the hosts using CIDR notation.
5. It outputs detailed information for each generated subnet.
