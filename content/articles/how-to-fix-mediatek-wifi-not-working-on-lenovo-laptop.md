---
title: "How to Fix MediaTek Wi-Fi Not Working on a Lenovo Laptop"
slug: "how-to-fix-mediatek-wifi-not-working-on-lenovo-laptop"
date: "2026-09-18"
categories: ["drivers"]
tags: ["mediatek wifi", "lenovo laptop", "wireless driver", "windows 11", "wifi not working"]
description: "MediaTek Wi-Fi dead on your Lenovo laptop? Fix it with the correct Lenovo driver package, power management tweaks, BIOS settings, and network stack resets."
thumbnail: "/images/thumbs/how-to-fix-mediatek-wifi-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why does my Lenovo laptop use a MediaTek Wi-Fi card instead of Intel?"
    a: "Lenovo ships MediaTek (MT7921/MT7922, Wi-Fi 6/6E) cards in many IdeaPad, ThinkPad, and Legion models as a cost-effective alternative to Intel. They work well with the correct driver but are more sensitive to driver mismatches than Intel cards. Always use Lenovo's driver package for your exact model rather than a generic MediaTek driver, since Lenovo tunes power management and antenna behavior per chassis."
  - q: "My MediaTek Wi-Fi works but randomly disconnects. Is that a driver issue?"
    a: "Usually yes. Random disconnects on MediaTek cards are most often caused by Windows power management turning the adapter off, an outdated driver with poor roaming behavior, or the 802.11 mode being set incorrectly. Update to Lenovo's latest wireless driver, disable power saving on the adapter, and set the preferred band to match your router. These three steps fix the vast majority of MediaTek disconnect issues."
  - q: "Should I replace my MediaTek card with an Intel AX210?"
    a: "It is a popular upgrade and the Intel AX210 is inexpensive, but check two things first: some Lenovo laptops whitelist wireless cards in the BIOS and will refuse to boot with an unapproved card, and opening the laptop may affect warranty. Try the driver fixes in this guide first — most MediaTek problems are software, and a working card you already own beats a hardware swap."
  - q: "Does Lenovo Vantage help with Wi-Fi driver problems?"
    a: "Yes. Lenovo Vantage (or the newer Lenovo Legion/ThinkPad system update tools) automatically detects your model and installs the correct wireless driver, which avoids the mismatch problems that come from manual downloads. Run a system update check in Vantage first — it often resolves MediaTek Wi-Fi issues with one click, including the matching Bluetooth driver for the combo card."
---

MediaTek Wi-Fi cards — the MT7921 (Wi-Fi 6) and MT7922 (Wi-Fi 6E) — appear in a huge number of Lenovo laptops, and they have a reputation for being fussy about drivers. The symptoms are familiar: no networks found, random disconnects, the adapter vanishing from Device Manager, or Code 10 errors after a Windows update. The hardware itself is solid; the problems are almost always driver mismatches, power management, or configuration. This guide walks through the fixes in the order a technician would try them.

Start by noting your exact symptom, because MediaTek issues split into two families: the adapter is missing or erroring (driver problem), or it works but disconnects constantly (power/roaming problem). Both are covered below.

## Why this happens

- **Generic driver replacing Lenovo's tuned package:** Windows Update installs a plain MediaTek driver that lacks Lenovo's power and antenna tuning.
- **Power management shutting the card down:** MediaTek cards are particularly sensitive to Windows' adapter power-saving, causing disconnects and disappearances.
- **Outdated driver with roaming bugs:** Older MediaTek drivers handle band-steering and roaming poorly, dropping connections on mesh networks.
- **Bluetooth coexistence conflict:** The combo card's Bluetooth side can interfere with Wi-Fi on certain driver versions.
- **Wrong 802.11 mode or band setting:** Forcing settings the card or router does not support produces unstable connections.
- **Corrupted driver after feature update:** Major Windows updates sometimes migrate the MediaTek driver badly, leaving a Code 10 device.
- **Fast Startup locking radio state:** The hibernation snapshot can preserve a broken wireless state across reboots.
- **BIOS wireless toggle or hardware fault:** The card disabled in firmware, or rarely, a failing module.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Device Manager and note the exact state

Your next steps depend entirely on what Device Manager shows.

1. Press Win + X, open Device Manager, and expand Network adapters.
2. Look for "MediaTek Wi-Fi 6 MT7921" or "MT7922" — note whether it is present, missing, or flagged with a warning.
3. If missing, click View > Show hidden devices and check for a greyed-out entry.
4. Double-click the adapter, check the Driver tab, and note the driver version and date — drivers older than a year are prime suspects.
5. If Wi-Fi is broadly broken rather than MediaTek-specific, our [general Wi-Fi disappeared guide](/articles/how-to-fix-wifi-disappeared-from-laptop-on-windows-11/) covers the OS-level side.

### Fix 2: Run Lenovo Vantage system update

The easiest correct driver comes from Lenovo itself.

1. Open Lenovo Vantage (install it from the Microsoft Store if missing).
2. Go to Device > System Update and click "Check for Updates".
3. Install any wireless, Bluetooth, or chipset driver updates it offers — these are matched to your exact model.
4. Restart when prompted, even if Vantage does not insist; driver changes need the reboot.
5. Test Wi-Fi thoroughly, including a sleep-wake cycle, before declaring victory.
6. Lenovo documents driver support officially at [Lenovo Support](https://support.lenovo.com/us/en/) if you prefer manual downloads.

### Fix 3: Clean-reinstall the MediaTek driver

When Vantage does not help or you need to purge a corrupt driver, do it manually.

1. Download the latest wireless driver for your exact Lenovo model from Lenovo's support site (use another device if you have no internet).
2. In Device Manager, right-click the MediaTek adapter, choose Uninstall device, and tick "Attempt to remove the driver for this device".
3. Restart the laptop — Windows will install a basic driver on boot.
4. Run the Lenovo driver installer you downloaded, choosing a clean install if offered.
5. Restart again and verify the driver version in Device Manager matches the package you installed.
6. Test both 2.4 GHz and 5 GHz networks if your router offers both.

### Fix 4: Disable power management on the adapter

This single setting fixes most MediaTek random-disconnect complaints.

1. In Device Manager, right-click the MediaTek adapter and choose Properties.
2. On the Power Management tab, uncheck "Allow the computer to turn off this device to save power".
3. Go to the Advanced tab and find "Power Saving Mode" or similar — set it to Maximum Performance.
4. Open Control Panel > Power Options > Change advanced power settings > Wireless Adapter Settings > Power Saving Mode and set Maximum Performance for both battery and plugged-in.
5. Restart and use the laptop normally for a day — disconnect issues often take hours to resurface, so give it time.
6. If disconnects persist only on battery, your power plan is still throttling the card.

### Fix 5: Tune the Advanced adapter settings

MediaTek's default advanced settings do not suit every network.

1. In the adapter's Properties > Advanced tab, find "Preferred Band" and set it to match your router's stronger band (usually 5 GHz for speed, 2.4 GHz for range).
2. Set "Roaming Aggressiveness" to a middle value (3) — too aggressive causes drops on mesh networks, too passive causes sticky connections.
3. If you see "802.11a/b/g Wireless Mode", leave it on auto unless your router is very old.
4. Disable "Bluetooth Collaboration" or coexistence settings temporarily as a test — if Wi-Fi stabilizes, the combo card's Bluetooth side was interfering.
5. Click OK and test for several hours; change one setting at a time so you know what helped.

### Fix 6: Reset the network stack and disable Fast Startup

Clear the OS-level networking state that survives driver changes.

1. Open Command Prompt as administrator and run `netsh winsock reset` and `netsh int ip reset`.
2. Go to Control Panel > Power Options > Choose what the power buttons do, click "Change settings that are currently unavailable", and uncheck "Turn on fast startup".
3. Shut down completely, wait 30 seconds, and power on fresh.
4. Reconnect to your Wi-Fi network — you will need to re-enter the password since the reset clears saved networks.
5. Microsoft's [Windows networking support](https://support.microsoft.com/en-us/windows) documents these reset commands officially.

### Fix 7: Check BIOS settings and update the BIOS

Firmware controls the card's power states and enumeration.

1. Restart into the BIOS (F2 or the Novo button on most Lenovos) and confirm the wireless device is enabled.
2. Check Lenovo's support site for a BIOS update newer than yours — wireless stability fixes appear in BIOS changelogs regularly.
3. Install the BIOS update on AC power without interruption.
4. After updating, load BIOS defaults to clear stale device configuration, then re-enable anything you had customized.
5. Boot into Windows and re-verify the driver version, since BIOS updates can change how the card enumerates.

### Fix 8: Test the hardware and consider the Intel swap

If software is exhausted, verify the card itself.

1. Boot an Ubuntu live USB — MediaTek cards have good Linux support — and test Wi-Fi there.
2. Working in Linux but broken in Windows means a Windows driver problem; consider a repair install.
3. Broken in both means hardware: reseat the M.2 card and antenna leads if your warranty allows.
4. Before buying an Intel AX210 replacement, verify your Lenovo model does not enforce a wireless whitelist (check forums for your exact model).
5. A USB Wi-Fi adapter is the zero-risk workaround if you do not want to open the laptop — compare with [adapter detection issues](/articles/how-to-fix-wifi-adapter-not-showing-up-on-acer-laptop/) for the same diagnostic logic on other brands.

## Closing

MediaTek Wi-Fi on Lenovo laptops rewards one habit above all: get the driver from Lenovo, not from Windows Update and not from generic MediaTek packages. Pair that with power management disabled on the adapter and you will eliminate the overwhelming majority of MediaTek wireless problems. The hardware is capable — it just needs the right software steering it.
