# Q7 — Design a Mobile Emergency Communication Network

The design uses a three-tier emergency network: mobile responders/vehicles, mesh gateways/command vehicles, and a remote control centre with redundant Home Agents, command servers, AAA and VPN gateway.

AODV is selected inside the mobile mesh because vehicles move at roughly 5–20 m/s, traffic is bursty, and route demand is intermittent. The assignment reports AODV overhead 5–17× lower than DSDV and about 4 percentage points higher delivery at 20 m/s in the simplified simulation.

Reliability target: 99.9% using redundant HA, multi-homing, heartbeat monitoring and store-and-forward.