# Q2 — Mobile IP and Mobility Management

Mobile IP keeps the home address stable while the node moves. The MN obtains a care-of address, registers it with the Home Agent, and packets destined to the home address are tunnelled to the CoA.

The worked example uses MN 130.10.5.20, HA 130.10.5.1, FA/CoA 192.168.40.1 and CN 200.50.60.7. IP-in-IP adds a 20-byte outer header.