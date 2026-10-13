---
title: "Intel Wi-Fi 6 AX201 Not Working on Windows 11? Here's How to Fix It"
slug: how-to-fix-intel-wifi-6-ax201-not-working-on-windows-11
date: 2026-09-15
categories: ["drivers"]
tags: ["intel ax201", "wifi 6", "windows 11", "wireless driver"]
description: "Intel Wi-Fi 6 AX201 showing Code 10, vanishing after sleep, or dropping constantly on Windows 11? Fix it with the right driver and the settings that matter."
thumbnail: "/images/thumbs/how-to-fix-intel-wifi-6-ax201-not-working-on-windows-11.webp"
faqs:
  - q: "Why is the AX201 so problematic on Windows 11?"
    a: "The AX201 is a CNVi card — part of its logic lives in the Intel chipset rather than on the card itself — which makes it sensitive to chipset driver versions and BIOS support. Windows Update installing a mismatched Wi-Fi or chipset driver breaks the CNVi handshake, producing Code 10 errors or a completely missing adapter. Matched Intel drivers fix it."
  - q: "Should I use Intel's driver or my laptop maker's driver?"
    a: "Either can work, but Intel's own releases via the Driver & Support Assistant are usually newer and well-tested for the AX201. The laptop maker's package is the safer choice if Intel's generic driver misbehaves, since vendors validate against their specific BIOS. Try Intel's first; fall back to the vendor package if problems persist."
  - q: "Why does my AX201 disappear after sleep?"
    a: "That is the classic AX201 power-management failure. Windows 11's power policies suspend the CNVi interface during sleep and the driver cannot reinitialize it on wake. Disabling 'allow the computer to turn off this device' on the adapter and setting the wireless power saving mode to Maximum Performance resolves the wake failure."
  - q: "Can I upgrade the AX201 to an AX210?"
    a: "No — and this trips up many owners. The AX201 uses Intel's proprietary CNVi interface and is not interchangeable with the standard M.2 AX210, which speaks PCIe/USB. An AX210 physically fits the slot but will not work in a CNVi-only socket. The correct upgrade path, if any, is another CNVi card like the AX211, and only if the BIOS supports it."
---

The Intel Wi-Fi 6 AX201 is in millions of laptops, and it has a split personality on Windows 11: rock solid for months, then dead after an update — Code 10 in Device Manager, or the adapter simply gone, or Wi-Fi that evaporates every time the laptop sleeps. The pattern is so consistent that technicians recognize it on sight.

The AX201's quirk is architectural: it is a CNVi card, meaning part of the Wi-Fi logic lives in the Intel chipset, not on the card. That makes it dependent on matched chipset drivers, BIOS support, and precise driver versions in a way standard cards are not. Windows Update's habit of mixing and matching breaks the CNVi handshake. The fix is Intel's own driver stack, installed cleanly, with power management tamed. (For the other common card, see our [MediaTek Wi-Fi guide](/articles/how-to-fix-mediatek-wifi-not-working-in-windows-11-24h2/).)

## Why this happens

- **Mismatched Wi-Fi driver from Windows Update.** The new driver build breaks the CNVi handshake with the chipset.
- **Chipset driver outdated.** The CNVi interface needs a current Intel chipset driver to function.
- **Code 10 after a feature update.** The 24H2 update replaced a working driver with an incompatible one.
- **Power management suspending CNVi.** Sleep/wake cycles kill the adapter when power saving is aggressive.
- **Bluetooth driver mismatch.** The AX201's Bluetooth shares the card; a mismatched BT driver can destabilize Wi-Fi.
- **BIOS lacking CNVi support updates.** Older BIOS versions mishandle the AX201 after OS updates.
- **Antenna or card seating issue.** The M.2 card loosened, breaking the CNVi connection intermittently.
- **Router-side incompatibilities.** Certain Wi-Fi 6 router features trigger AX201 driver bugs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Intel Driver & Support Assistant

Download and run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html). It detects your AX201, chipset, and Bluetooth, and offers the matched driver set Intel validated together. Install everything it recommends — Wi-Fi driver, Bluetooth driver, and chipset INF — then restart. This is the highest-percentage fix for the AX201 because it restores the matched driver set the CNVi architecture requires. Verify in Device Manager that the adapter shows no warning and note the driver version.

### Fix 2: Clean-reinstall the AX201 driver manually

If the Assistant does not resolve it, do a manual clean install. In **Device Manager**, expand **Network adapters**, right-click **Intel Wi-Fi 6 AX201**, choose **Uninstall device**, and check **Attempt to remove the driver for this device**. Restart. Then install the Wi-Fi driver package downloaded from Intel's site (or your laptop maker's site) rather than letting Windows choose. Restart again and test, including a sleep/wake cycle. The manual clean install matters because it purges the mismatched build from the driver store completely. For the general Code 10 error on any Wi-Fi adapter, our [Wi-Fi Code 10 repair guide](/articles/how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2/) covers the error itself in depth.

### Fix 3: Update the Intel chipset driver

The CNVi interface lives partly in the chipset, so the chipset driver is not optional. Download the **Intel Chipset INF** package — from the Driver & Support Assistant or your laptop maker's official support site — and install it, then restart. An outdated chipset driver with a new Wi-Fi driver (or vice versa) is a classic AX201 Code 10 recipe. After updating, recheck Device Manager: both the AX201 and the chipset system devices should be warning-free.

### Fix 4: Disable power management on the adapter

Open the AX201's **Properties > Power Management** in Device Manager and uncheck **Allow the computer to turn off this device to save power**. Then go to **Settings > System > Power & battery**, open the advanced power settings, and set **Wireless Adapter Settings > Power Saving Mode** to **Maximum Performance** on battery and plugged in. The AX201's "dead after sleep" failure is almost always this: the CNVi link suspends and never resumes. Test with a real sleep/wake cycle — close the lid for a minute, reopen, and confirm Wi-Fi reconnects.

### Fix 5: Update Bluetooth and check coexistence

The AX201 is a Wi-Fi/Bluetooth combo card, and the two radios share the hardware. In Device Manager, update the **Intel Wireless Bluetooth** driver to the version matching your Wi-Fi driver (the Driver & Support Assistant handles this as a set). In the Wi-Fi adapter's **Properties > Advanced**, verify **Bluetooth Collaboration** or coexistence settings are at defaults. A mismatched Bluetooth driver can cause Wi-Fi drops under Bluetooth load — the symptom of Wi-Fi dying when you connect Bluetooth headphones points here.

### Fix 6: Adjust advanced Wi-Fi settings for stability

In the adapter's **Properties > Advanced** tab: set **Preferred Band** to match your environment, set **Roaming Aggressiveness** to **3. Medium** if you roam between access points, and try setting **802.11a/b/g Wireless Mode** to **6. 802.11ax** only if your network is Wi-Fi 6 throughout. If drops happen on a specific router, try disabling **802.11ax** mode temporarily to test whether a Wi-Fi 6 handshake bug is the cause. Change one setting at a time and test — shotgun changes make the real cause impossible to identify.

### Fix 7: Update the BIOS and check the hardware

Check the laptop maker's site for a **BIOS update** — CNVi initialization fixes ship in firmware, and vendors specifically addressed AX201 issues in BIOS updates. Flash with the charger connected. If the adapter is still missing or Code 10 across every driver combination, power off, open the laptop (if out of warranty), and reseat the M.2 card, confirming both antenna leads are firmly attached. Remember: the AX201 socket is CNVi — do not "upgrade" to an AX210, which will not work. If reseating fails, the card or the chipset's CNVi logic needs professional diagnosis.

## Closing

The AX201's CNVi architecture makes it fussier than ordinary Wi-Fi cards, but the fix pattern is reliable: matched Intel drivers via the Driver & Support Assistant, current chipset INF, and power management disabled on the adapter. Get those three right and the card is as stable as anything else. Pin the working driver against Windows Update so the next feature update does not restart the cycle.
