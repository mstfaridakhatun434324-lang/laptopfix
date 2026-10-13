---
title: "Network Adapter Missing? How to Troubleshoot It"
slug: troubleshoot-network-adapter-missing
date: 2026-09-04
categories: ["drivers"]
tags: ["network adapter", "missing", "device manager", "wifi fix"]
description: "Your network adapter vanished from Device Manager? This troubleshooting guide walks you from quick checks to BIOS and clean driver reinstalls."
thumbnail: "/images/thumbs/troubleshoot-network-adapter-missing.webp"
faqs:
  - q: "What is the difference between a missing adapter and a Code 10 error?"
    a: "A missing adapter does not appear in Device Manager at all, which suggests Windows cannot see the hardware — a BIOS setting, a disabled device, or a failed card. A Code 10 error means the adapter is detected but its driver cannot start, which is almost always a driver problem. The two need different fixes, so confirming which one you have is the essential first step."
  - q: "Can a Windows update make my network adapter disappear?"
    a: "Yes, though it is less common than driver corruption. Updates can install an incompatible driver that fails to enumerate the device, or change power policies that keep the adapter powered down. If the disappearance lines up with an update, a driver rollback or a clean install of the manufacturer's driver usually restores it."
  - q: "Should I open my laptop to reseat the Wi-Fi card?"
    a: "Only after software troubleshooting fails and the adapter is also missing from the BIOS. On most modern laptops the Wi-Fi card is an M.2 module that is easy to reseat, but opening the machine may void warranty on some models. Try BIOS checks, power drains, and driver reinstalls first — they resolve the majority of cases without tools."
  - q: "Will a USB Wi-Fi adapter work as a permanent fix?"
    a: "Yes. A USB Wi-Fi dongle bypasses the internal adapter entirely and works reliably as a long-term solution. It is also the fastest way to confirm a hardware failure: if the USB adapter works fine while the internal one stays missing, the internal card or its slot is the problem."
---

When your network adapter disappears from Device Manager entirely — not error-flagged, just gone — the troubleshooting mindset changes. Windows is telling you it cannot see the hardware at all, and that narrows the suspects to a short list: a BIOS setting, a power state problem, a driver that fails to enumerate the device, or genuinely failed hardware. The fix sequence below is ordered to rule these out from easiest to hardest, and most people find their adapter before reaching the hardware steps.

One important distinction first: check whether the adapter is missing under **Network adapters** or missing everywhere including **View > Show hidden devices**. A greyed-out hidden adapter means Windows knows about it but has marked it disconnected — that is a different, usually simpler problem. If you are dealing with an adapter that shows up with an error instead, see our guide on [fixing a Wi-Fi driver Code 10 error](/articles/how-to-fix-wifi-driver-code-10-error/). For adapters that are present but cannot find networks, the [Wi-Fi 5GHz connection guide](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/) is the better next step.

## Why this happens

- **Disabled in BIOS/UEFI.** Many business and consumer laptops have a wireless toggle in the BIOS; a BIOS update or reset can flip it off.
- **Physical wireless switch or Fn key.** Some laptops still have a hardware Wi-Fi switch or an Fn-key toggle that electrically disconnects the radio.
- **Deep power state lockup.** Fast Startup and hibernate can leave the adapter in a low-power state that survives normal reboots, hiding it from enumeration.
- **Corrupted driver preventing enumeration.** A badly corrupted driver can fail so early that Windows never lists the device at all.
- **Airplane mode stuck on.** A stuck airplane mode state can suppress the adapter's appearance in some configurations.
- **Windows Update driver replacement.** An incompatible driver pushed by Windows Update may fail to bring the device up.
- **Failed Wi-Fi card or slot.** The M.2 card itself or its slot can fail, especially after drops, liquid exposure, or years of heat cycling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check for hidden devices and the physical switch

Start with the checks that take thirty seconds.

1. Open Device Manager, click **View > Show hidden devices**, and expand **Network adapters**. A greyed-out adapter means it is known but disconnected — right-click it and choose **Uninstall device**, then restart.
2. Inspect the laptop's edges and keyboard for a physical Wi-Fi switch or an **Fn + F-key** wireless toggle (often F2, F8, or a key with an antenna icon). Flip it and recheck.
3. Open **Settings > Network & internet** and confirm **Airplane mode** is off. If the toggle is stuck, our [airplane mode stuck guide](/articles/how-to-fix-airplane-mode-stuck-on-in-windows-11-24h2/) covers that specific fault.

### Fix 2: Perform a full power drain

This clears the deep power states that survive normal reboots.

1. Shut down the laptop completely (not sleep, not hibernate — full shutdown).
2. Unplug the charger and all USB devices. If the battery is removable, take it out.
3. Hold the power button down for **30 seconds** to drain residual charge from the capacitors.
4. Reconnect power (leave USB devices unplugged for now) and boot. Check Device Manager for the adapter.
5. If it reappears, the culprit was a stuck power state — consider disabling **Fast Startup** in **Control Panel > Power Options > Choose what the power buttons do** to prevent recurrence.

### Fix 3: Verify the wireless is enabled in BIOS

The BIOS can disable the adapter at a level Windows cannot override.

1. Restart and enter the BIOS/UEFI (usually **F2**, **F10**, or **Delete**).
2. Look through **Advanced**, **Security**, or **Device Configuration** for **Wireless**, **WLAN**, or **Wireless LAN** and make sure it is **Enabled**.
3. While there, check for a **Wireless switch** behavior setting and set it to allow OS control if available.
4. Save and exit, then check Device Manager again.

### Fix 4: Scan for hardware changes and reinstall the driver

Force Windows to rediscover the device.

1. In Device Manager, click **Action > Scan for hardware changes** and wait for the scan to finish.
2. If the adapter appears (even with an error), right-click it, choose **Uninstall device**, and check **Attempt to remove the driver for this device**.
3. Restart the laptop and let Windows reinstall. Then immediately install the manufacturer's driver from the laptop maker's support site — for Intel cards, [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) finds the right one automatically.
4. If nothing appears after the scan, the driver store may need a manual purge — continue to Fix 5.

### Fix 5: Reset the network stack and clear the driver store

Corrupted network components can suppress enumeration.

1. Open an elevated Command Prompt (**Win + X > Terminal (Admin)**).
2. Run these commands, pressing Enter after each: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /flushdns`.
3. Open **Settings > Network & internet > Advanced network settings > Network reset** and click **Reset now**. Confirm and let the laptop restart.
4. After the restart, install the manufacturer's Wi-Fi driver manually rather than letting Windows Update choose one.

### Fix 6: Check Windows Update history and roll back

If the disappearance lines up with an update, undo the driver portion of it.

1. Go to **Settings > Windows Update > Update history** and note the date of the most recent driver or quality update.
2. If a driver update matches the timeline, open Device Manager (with hidden devices shown), find the adapter, and use **Roll Back Driver** on the Driver tab.
3. Alternatively, uninstall the most recent quality update from **Update history > Uninstall updates** as a test — you can reinstall it later once the adapter is stable.
4. After recovery, pause driver updates via **Settings > Windows Update > Advanced options** while you install the manufacturer's driver.

### Fix 7: Test with a USB adapter and reseat the internal card

The final step separates hardware failure from everything else.

1. Plug in a USB Wi-Fi adapter. If it works immediately, your Windows network stack is healthy and the internal card or slot is the problem.
2. If the laptop is out of warranty and you are comfortable opening it, remove the back panel, locate the M.2 Wi-Fi card, remove its retaining screw, reseat the card firmly, and reconnect the antenna wires (note which wire goes to MAIN and AUX before disconnecting).
3. If reseating does not help, replacement M.2 Wi-Fi cards are inexpensive — but a USB adapter remains a perfectly valid permanent solution with zero disassembly.

## Closing

A missing network adapter feels like a hardware death sentence, but the power drain and BIOS checks alone recover a surprising number of them — deep sleep states and flipped BIOS toggles are silent and common. Work the sequence in order and note where the adapter reappears, because that tells you the cause: after a power drain it was a stuck state, after a BIOS change it was firmware, after a driver purge it was software. Only when every software step fails and the BIOS cannot see the card either should you reach for the screwdriver.
