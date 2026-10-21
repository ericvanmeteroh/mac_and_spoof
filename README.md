# TERMINAL: INKSTRIDER_SYS_01 // SPECIMEN_01: IFCONFIG
> **OPERATOR:** E. VanMeter (` SECTOR_OH `)  
> **CLASSIFICATION:** CompTIA A+ (220-1201) // MAC Address Spoof Phantom
> **STATUS:** `[ ONLINE // VERIFIED ]`

---

## [01] INITIAL LOG // SPECIMEN INTAKE
**Symptom / Inquiry:**  
Decive MAC address identified by built in utility (`ifconfig`) and return is validated. Device address listed under (`wlo1`) interface. Will validate by cracking the chassis. To navigate checkpoints a phantom is required to provide stealth switches. Targeting (`wlo1`) which identifies wireless network, ```ifconfig wlo1 down```, disable interface to allow modifications. Next, designating a new sequence manually, ```ifconfig wlo1 hw ether 00:11:22:33:44:55```. MAC addresses contain 12 character in sequence followed by colons, xx:xx:xx:xx:xx:xx. To establish connection of (`wlo1`) finish with ```ifconfig wlo1 up```. Important to note, wlo applies to wireless networks, utilize eth if hardwired to system. Verify system integrity by running ifconfig.

## [02] SYNAPTIC WIRING // CORE ARCHITECTURE
* **Substrate:** Arch Linux (Omarchy) / Python 3.12
* **Internals Probed:** 
  * `SUBPROCESS`: Process allow execution of system commands withing defined script. 

<!-- 
## [03] FIELD CHRONICLE // COMMIT TRANSMISSION LOG
* `[BOOT]` — Specimen intake complete. Base script initialized on workbench.
* `[SPLICE]` — 
* `[CAUTERIZE]` — Contained
* `[SEALED]` — System verification passed. Output locked to phosphor-green terminal HUD.

## [04] SYSTEM VERIFICATION // END LOG
To execute this stealth maneuver on your own terminal:
```bash
git clone [https://github.com/ericvanemteroh/mac_and_spoof.git](https://github.com/ericvanmeteroh/mac_and_spoof.git)
cd ../001_mac_shift
python3 001_mac_shift.py -->