# !/usr/bin/env python3
import subprocess
import time
import random
import optparse
import warnings

# Suppressing warnings from the requests library
warnings.filterwarnings("ignore", category=UserWarning, module='requests')
from requests import options

# Configuration
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="network_interface", help="Enter the network interface (e.g., eth0, wlan0)")
    parser.add_option("-m", "--mac", dest="mac_address", help="Enter the desired MAC address")

    (options, args) = parser.parse_args()

    if not options.network_interface:
        options.network_interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    else:
        options.network_interface = options.network_interface

    if not options.mac_address:
        numbers_list = [random.randint(0, 25) for _ in range(5)]
        clean_hex = [hex(num)[2:].upper().zfill(2) for num in numbers_list]
        options.mac_address = "06:" + (":".join(clean_hex))
    else:
        options.mac_address = options.mac_address
    return options, args

# Function to change the MAC address of a network interface
def change_mac(network_interface, mac_address):
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

    subprocess.call(["ifconfig", network_interface, "down"])
    subprocess.call(["ifconfig", network_interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", network_interface, "up"])

# Main execution
(options, args) = get_arguments()
change_mac(options.network_interface, options.mac_address)