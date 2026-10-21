import subprocess
import time

network_interface = "wlo1"
mac_address = "00:11:22:33:44:55"  # Replace with the desired MAC address

import time

# MU/TH/UR 6000 CRT Color Palette
GREEN = "\033[38;5;46m"    # Phosphor Terminal Green
AMBER = "\033[38;5;214m"   # Nostromo Warning Amber
RED   = "\033[38;5;196m"   # Containment Breach Red
DIM   = "\033[2m"          # Dimmed CRT scanline look
RESET = "\033[0m"

noise_lines = [
    f"{AMBER}[SYS_CHK]{RESET}   {DIM}Verifying UID=0 root clearance for raw netlink socket...{RESET}",
    f"{GREEN}[L2_PROBE]{RESET}  {DIM}Inspecting 802.3 Ethernet frame header offsets (14-byte L2 PDU)...{RESET}",
    f"{GREEN}[BIT_CHK]{RESET}   {DIM}Validating unicast/locally-administered bit (U/L bit 0x02) in Octet 0...{RESET}",
    f"{RED}[CAM_WARN]{RESET}  {AMBER}Note: Enterprise switches running Sticky Port-Security (802.1X) may err-disable.{RESET}",
    f"{GREEN}[NVRAM]{RESET}     {DIM}Physical factory ROM untouched; mutation strictly confined to volatile RAM.{RESET}",
    f"{GREEN}[CRC_SYNC]{RESET}  {DIM}Recalibrating Frame Check Sequence (FCS) trailer generator...{RESET} {GREEN}[OK]{RESET}",
    f"{AMBER}[FINISHED]{RESET}  {GREEN}Changing MAC address of {AMBER}{network_interface}{GREEN} to {AMBER}{mac_address}{RESET}",
]

print(f"{DIM}--------------------------------------------------------------------------------{RESET}")
for line in noise_lines:
    print(line)
    time.sleep(0.12)
print(f"{DIM}--------------------------------------------------------------------------------{RESET}")

subprocess.call(f"ifconfig {network_interface} down", shell=True)
subprocess.call(f"ifconfig {network_interface} hw ether {mac_address}", shell=True)
subprocess.call(f"ifconfig {network_interface} up", shell=True)
