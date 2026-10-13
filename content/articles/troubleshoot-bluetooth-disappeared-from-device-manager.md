---
title: "Troubleshooting Bluetooth That Disappeared From Device Manager"
slug: "troubleshoot-bluetooth-disappeared-from-device-manager"
date: "2026-09-13"
categories: ["drivers"]
tags: ["bluetooth missing", "device manager troubleshooting", "windows 11", "bluetooth radio", "driver diagnostics"]
description: "A diagnostic walkthrough for Bluetooth missing from Device Manager: isolate whether it's a service failure, driver crash, BIOS toggle, or dead hardware before you fix it."
thumbnail: "/images/thumbs/troubleshoot-bluetooth-disappeared-from-device-manager.webp"
faqs:
  - q: "What is the first thing to check when Bluetooth vanishes from Device Manager?"
    a: "Enable hidden devices in Device Manager first. Bluetooth often still exists as a greyed-out entry, which tells you the hardware is detected but disabled or driverless, a very different problem from a card that is electrically dead. If nothing appears even as hidden, check the Bluetooth Support Service and the BIOS wireless toggle next. This thirty-second check shapes every step that follows."
  - q: "Why do Wi-Fi and Bluetooth disappear at the same time?"
    a: "Laptop Wi-Fi and Bluetooth share one physical combo card and often one driver package. When the wireless driver crashes, Windows can lose the Bluetooth enumerator along with it, so both vanish together. Fixing the Wi-Fi driver frequently restores Bluetooth automatically. If only Bluetooth is missing while Wi-Fi works, the Bluetooth-specific driver or the Bluetooth Support Service is the more likely culprit."
  - q: "Can airplane mode hide Bluetooth from Device Manager?"
    a: "Airplane mode disables the radio but should not remove Bluetooth from Device Manager; the category normally stays visible with the device present. If toggling airplane mode off does not restore Bluetooth, and the category is genuinely gone from Device Manager, you are dealing with a driver, service, or hardware issue rather than a simple radio toggle."
  - q: "When should I suspect the Bluetooth hardware is dead?"
    a: "Suspect hardware only after software is exhausted: Bluetooth is absent with hidden devices shown, the Bluetooth Support Service will not start, the card is enabled in BIOS, the wireless driver has been cleanly reinstalled, and a Linux live USB also shows no Bluetooth radio. If Wi-Fi on the same combo card also fails everywhere, the card itself is the prime suspect and reseating or replacing it is the fix."
---

When Bluetooth disappears from Device Manager, the instinct is to start reinstalling things at random. A better approach is to diagnose first: the symptom looks identical whether the cause is a stopped service, a crashed driver, a BIOS toggle, or a dead card — but the fixes are completely different. This guide is built as a diagnostic walkthrough. Each section tells you what to check, what the result means, and which repair follows from it, so you fix the actual problem instead of guessing.

Bluetooth on Windows laptops is enumerated through the wireless combo card's driver stack, which is why it can vanish without a trace instead of showing a helpful error. Work through the checks in order; each one narrows the field.

## Why this happens

- **Bluetooth Support Service failure:** The service that exposes Bluetooth hardware to Windows stops or is disabled, so the category never appears.
- **Combo wireless driver crash:** The Wi-Fi card's driver enumerates Bluetooth; when it crashes, the Bluetooth node disappears with it.
- **Driver replaced by Windows Update:** A generic Bluetooth driver that does not match the card's firmware breaks enumeration silently.
- **Radio disabled in BIOS:** The firmware-level wireless toggle hides the Bluetooth radio from the operating system completely.
- **Airplane mode or function-key toggle:** The radio is switched off at a low level, though this usually leaves Device Manager entries visible.
- **USB power management:** Bluetooth often rides the internal USB bus, and selective suspend can power the radio into invisibility.
- **Corrupted device metadata cache:** Windows caches device enumeration data; a corrupted cache can persist a missing Bluetooth state across boots.
- **Dead combo card:** Electrical failure of the wireless module removes Bluetooth and usually Wi-Fi in one stroke.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the disappearance and check hidden devices

Establish the baseline before changing anything.

1. Press Win + X, open Device Manager, and confirm there is no Bluetooth category at all.
2. Click View > Show hidden devices and scan for greyed-out Bluetooth entries or unknown devices.
3. Open Settings > Bluetooth & devices — note whether the page shows a toggle, an error, or nothing Bluetooth-related.
4. Check the taskbar and Action Center for any Bluetooth icon.
5. Write down what you find: hidden-but-present means a driver or disabled-device problem; totally-absent points toward services, BIOS, or hardware.

### Fix 2: Check the Bluetooth Support Service

A stopped service is the most common benign cause, and the fastest to rule out.

1. Press Win + R, type `services.msc`, and press Enter.
2. Locate "Bluetooth Support Service" — note whether it is Running, Stopped, or missing.
3. Double-click it, set Startup type to Automatic, and click Start.
4. If it starts successfully, reopen Device Manager and look for the Bluetooth category.
5. If it fails to start, record the exact error message — "Error 1079" points to a logon account problem, while driver-related errors point to the next fix.
6. Also verify the "Bluetooth User Support Service" exists and is set to Manual on Windows 11.

### Fix 3: Diagnose the wireless combo driver

Because Bluetooth depends on the combo card, interrogate the Wi-Fi side next.

1. In Device Manager, expand Network adapters and check your wireless card's status.
2. If the Wi-Fi adapter also has a warning or is missing, treat this as a wireless driver problem first — our [Wi-Fi disappeared guide](/articles/how-to-fix-wifi-disappeared-from-laptop-on-windows-11/) covers that path.
3. If Wi-Fi works fine but Bluetooth is gone, the Bluetooth-specific driver component is the suspect.
4. Check Windows Update history for any driver update dated around when Bluetooth vanished.
5. Download the full wireless plus Bluetooth driver package from your laptop maker's site as your repair ammunition.

### Fix 4: Reinstall the Bluetooth and wireless drivers

With the diagnosis pointing at drivers, do a clean reinstall.

1. In Device Manager with hidden devices shown, uninstall every Bluetooth entry, ticking "Attempt to remove the driver for this device".
2. Uninstall the wireless adapter the same way, also removing its driver.
3. Restart the laptop and let Windows redetect the hardware.
4. If Bluetooth returns, install the manufacturer's driver package over the inbox driver for stability.
5. Verify both Wi-Fi and Bluetooth work, then test a sleep-wake cycle — driver issues often resurface after sleep.
6. For general [Bluetooth failures on Windows 11](/articles/bluetooth-not-working-on-windows-11-laptop-fix/) beyond the missing-device case, the same reinstall sequence applies.

### Fix 5: Rule out BIOS and function-key toggles

If no driver work helps, confirm the radio is actually enabled at the firmware level.

1. Press the wireless function key (often F12 with an antenna icon) and watch for any indicator change.
2. Turn airplane mode on, wait ten seconds, turn it off, and recheck Device Manager.
3. Restart into the BIOS setup and look for wireless, Bluetooth, or WLAN/BT toggles.
4. Enable anything Bluetooth-related, load setup defaults if the options are confusing, and save.
5. Boot into Windows and check whether the Bluetooth category has returned.
6. Microsoft's [official Bluetooth guidance](https://support.microsoft.com/en-us/windows) also documents the expected Settings behavior when the radio is available.

### Fix 6: Disable USB selective suspend and reset power state

Bluetooth's internal USB connection makes it vulnerable to power management.

1. Open Control Panel > Power Options > Change advanced power settings.
2. Set USB selective suspend to Disabled for both battery and plugged-in states.
3. In Device Manager, open each USB Root Hub's Power Management tab and uncheck power-saving.
4. Shut the laptop down fully (not restart), unplug it for 30 seconds to drain residual power, then boot fresh.
5. This full power drain clears radio states that survive warm reboots — recheck Device Manager after boot.

### Fix 7: Clear the device metadata cache and run system repair

A corrupted enumeration cache can keep Bluetooth hidden even with healthy drivers.

1. Open an elevated Command Prompt and run `pnputil /enum-devices /connected` to see what Windows believes is present.
2. Run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` to repair system files.
3. In Device Manager, choose Action > Scan for hardware changes after the repairs complete.
4. If Bluetooth appears but immediately vanishes, create a new local user account and check there — a corrupted user profile can break the Bluetooth UI layer.
5. Intel's [Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also refresh the wireless and Bluetooth stack on Intel-based laptops.

### Fix 8: Confirm or rule out hardware failure

Only now, with software exhausted, test the hardware directly.

1. Boot an Ubuntu live USB and check its Bluetooth settings for your adapter.
2. Bluetooth present in Linux but absent in Windows means a Windows-side problem — consider a repair install.
3. Absent in both means the combo card has likely failed electrically.
4. If your laptop has a socketed M.2 wireless card, reseat it and check the antenna leads (verify warranty implications first).
5. A USB Bluetooth dongle is a reliable permanent workaround if board-level repair is not worthwhile.

## Closing

The diagnostic order matters: hidden-device check, service status, wireless driver health, BIOS toggles, power state, system integrity, and only then hardware. Most Bluetooth disappearances resolve at step two or four — a stopped service or a crashed combo driver — so resist the urge to assume the worst. And once Bluetooth is back, keep the manufacturer's wireless driver installed so Windows Update cannot quietly break the stack again.
