---
title: "Bluetooth Disappeared From Device Manager: How to Fix It on Windows Laptops"
slug: "how-do-i-fix-bluetooth-disappeared-from-device-manager"
date: "2026-09-09"
categories: ["drivers"]
tags: ["bluetooth missing", "device manager", "windows 11", "bluetooth driver", "wireless card"]
description: "Bluetooth vanished from Device Manager? Learn how to bring it back with Bluetooth Support Service checks, driver reinstalls, power management fixes, and hardware diagnostics."
thumbnail: "/images/thumbs/how-do-i-fix-bluetooth-disappeared-from-device-manager.webp"
faqs:
  - q: "Why is Bluetooth completely missing from Device Manager?"
    a: "The Bluetooth enumerator depends on the wireless combo card's driver. When that driver crashes, is disabled, or gets replaced by a bad Windows Update, the entire Bluetooth node can vanish instead of showing an error. It can also disappear if the Bluetooth Support Service is stopped, if USB selective suspend cuts power to the radio, or if the card is disabled in BIOS. Restoring the driver and service usually brings it back."
  - q: "Can a Windows update remove Bluetooth from my laptop?"
    a: "Yes. Windows Update sometimes installs an incompatible Bluetooth or wireless driver, or a major feature update fails to migrate the existing Bluetooth stack properly. The result is a missing Bluetooth category in Device Manager. Rolling back the driver, reinstalling the manufacturer's Bluetooth driver, or running the Windows Bluetooth troubleshooter typically reverses this within a few minutes."
  - q: "How do I check if Bluetooth is disabled in BIOS?"
    a: "Restart your laptop and press the BIOS key (F2, F10, or Del depending on the brand) to enter firmware setup. Look under Advanced, Devices, or Wireless settings for a Bluetooth or wireless radio toggle. If it is disabled, enable it, save, and exit. Many modern laptops combine this with the Wi-Fi toggle, so check for a general wireless device setting if Bluetooth is not listed separately."
  - q: "Is missing Bluetooth ever a hardware failure?"
    a: "It can be. If Bluetooth never appears in Device Manager even with hidden devices shown, survives a clean driver reinstall, and the Wi-Fi side of the same combo card also fails, the card or its USB interface may be dead. On laptops with socketed M.2 wireless cards, reseating or replacing the card is a cheap fix. Soldered cards require board-level repair or a USB Bluetooth dongle as a workaround."
---

Bluetooth disappearing from Device Manager is one of the more confusing laptop problems because there is no error message — the whole Bluetooth category simply stops existing. Your headphones, mouse, and earbuds vanish from Settings, the Bluetooth toggle disappears, and nothing in the usual troubleshooters seems to know the radio was ever there. It feels like hardware failure, but in most cases it is a driver or service problem that takes about fifteen minutes to fix.

Bluetooth on laptops almost always shares a physical card with Wi-Fi (an Intel, MediaTek, Realtek, or Qualcomm combo module). That means Bluetooth and Wi-Fi problems are cousins: a wireless driver crash often takes both down together. If your Wi-Fi is also misbehaving, start by fixing the wireless side — our guide on [fixing Wi-Fi that disappeared from Windows 11](/articles/how-to-fix-wifi-disappeared-from-laptop-on-windows-11/) covers the same card from the networking angle.

## Why this happens

- **Wireless combo driver crash:** The Bluetooth stack is enumerated by the Wi-Fi card's driver; when that driver fails, the Bluetooth node vanishes instead of showing an error.
- **Bad driver from Windows Update:** An automatic update can install a generic Bluetooth driver that does not match your combo card's firmware.
- **Bluetooth Support Service stopped:** If this Windows service is disabled or stuck, Bluetooth hardware will not be listed anywhere.
- **Radio disabled in BIOS or by a function key:** Many laptops let you kill the wireless radios at firmware level, hiding Bluetooth from the OS entirely.
- **USB selective suspend:** Bluetooth often rides the internal USB bus, and aggressive power saving can suspend it into invisibility.
- **Corrupted Bluetooth pairing database:** A damaged device pairing store can crash the Bluetooth enumerator during startup.
- **Fast Startup locking device state:** The hibernation snapshot can preserve a broken Bluetooth state across reboots.
- **Failed or loose wireless card:** A dead combo card removes both Wi-Fi and Bluetooth in one stroke.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Bluetooth troubleshooter and check Settings

Start with the least invasive checks — sometimes Bluetooth is only hidden at the UI level.

1. Open Settings > System > Troubleshoot > Other troubleshooters and run the Bluetooth troubleshooter.
2. Check Settings > Bluetooth & devices — if the page says Bluetooth is turned off, toggle it on.
3. Look for a physical wireless switch or function key (often F12 or an antenna icon) and make sure the radio is on.
4. If Bluetooth is still absent everywhere, move on to Device Manager.

### Fix 2: Reveal hidden devices in Device Manager

Bluetooth may be present but hidden because Windows considers it disconnected.

1. Press Win + X and open Device Manager.
2. Click View > Show hidden devices.
3. Look for a Bluetooth category, plus entries under Network adapters and Universal Serial Bus controllers related to your wireless card.
4. If you find a greyed-out Bluetooth device, right-click it and choose Enable device.
5. If a Bluetooth device shows a yellow warning, double-click it and note the error code on the General tab.
6. For anything flagged, right-click and choose Scan for hardware changes to force re-enumeration.

### Fix 3: Restart the Bluetooth Support Service

Without this service running, Windows will not list Bluetooth hardware at all.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find "Bluetooth Support Service" in the list.
3. Double-click it, set Startup type to Automatic, and click Start if it is stopped.
4. Also check "Bluetooth Audio Gateway Service" and "Bluetooth User Support Service" on newer builds.
5. Click OK, then restart the laptop and check Device Manager again.
6. If the service refuses to start, note the error — it usually points at the underlying driver problem covered below.

### Fix 4: Reinstall the wireless and Bluetooth drivers

Since Bluetooth rides on the combo card, reinstalling the Wi-Fi driver often restores Bluetooth too.

1. In Device Manager, expand Network adapters and note your wireless card model (Intel, MediaTek, Realtek, or Qualcomm).
2. Right-click it, choose Uninstall device, and tick "Attempt to remove the driver for this device".
3. Also uninstall any Bluetooth entries if they exist, using the same driver-removal option.
4. Restart the laptop — Windows should redetect the card and reinstall its inbox drivers.
5. If Bluetooth returns but behaves oddly, download the full driver package from your laptop maker's support site.
6. For persistent [Bluetooth problems on Windows 11](/articles/bluetooth-not-working-on-windows-11-laptop-fix/), installing the manufacturer's chipset and Bluetooth stack together works best.

### Fix 5: Disable USB selective suspend and device power saving

Bluetooth radios on the internal USB bus are vulnerable to power-management shutdowns.

1. Open Control Panel > Power Options > Change plan settings > Change advanced power settings.
2. Expand USB settings > USB selective suspend setting and set it to Disabled for both battery and plugged-in.
3. In Device Manager, open each USB Root Hub's Properties > Power Management tab and uncheck "Allow the computer to turn off this device to save power".
4. Do the same for the wireless adapter under Network adapters.
5. Restart and verify Bluetooth stays visible after the laptop sleeps and wakes.

### Fix 6: Clear the pairing cache and reset the Bluetooth stack

A corrupted pairing database can crash Bluetooth enumeration at every boot.

1. Open Settings > Bluetooth & devices > Devices and remove every paired device.
2. Press Win + R, type `services.msc`, and stop the Bluetooth Support Service temporarily.
3. Open File Explorer and navigate to `C:\Windows\System32\config\systemprofile\AppData\Local\Microsoft\Windows\` — if a Bluetooth-related cache exists there, back it up and delete it.
4. Alternatively, open an elevated Command Prompt and run `netsh winsock reset`, then restart.
5. After rebooting, re-pair one device and confirm the Bluetooth category remains stable in Device Manager.

### Fix 7: Disable Fast Startup and check the BIOS

Fast Startup can lock in a broken radio state, and the BIOS can hide the radio entirely.

1. Go to Control Panel > Power Options > Choose what the power buttons do, click "Change settings that are currently unavailable", and uncheck "Turn on fast startup".
2. Shut down fully, wait 30 seconds, and power on.
3. If Bluetooth is still missing, restart into the BIOS (F2, F10, or Del at boot).
4. Look for wireless device settings and confirm Bluetooth — or the combined wireless radio — is enabled.
5. Load BIOS defaults if you are unsure, save, exit, and check Device Manager again.

### Fix 8: Test the hardware with a live USB or a dongle

If nothing software-side works, determine whether the card itself is dead.

1. Boot from a Linux live USB (Ubuntu works well) and check whether Bluetooth appears there.
2. If it appears in Linux but not Windows, the hardware is fine — reinstall Windows' Bluetooth stack or consider a clean OS install.
3. If it is missing in Linux too, the combo card has likely failed.
4. As a quick workaround, plug in a cheap USB Bluetooth dongle — it installs its own driver and bypasses the internal card.
5. For a permanent fix on socketed M.2 cards, reseat or replace the wireless module; Microsoft's official guidance on [Bluetooth in Windows](https://support.microsoft.com/en-us/windows) covers the software side in more depth.

## Closing

Bluetooth disappearing from Device Manager is alarming but rarely fatal — the service, driver, and power-management fixes above resolve it in the overwhelming majority of cases. If you do land on a hardware failure, a USB Bluetooth dongle is a perfectly good permanent workaround for a few dollars. And once Bluetooth is stable again, keep your wireless drivers updated from the manufacturer's site rather than relying on Windows Update alone, since driver mismatches are the single most common trigger.
