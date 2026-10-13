---
title: "Troubleshoot WiFi That Disappeared From a Laptop"
slug: troubleshoot-wifi-disappeared-from-laptop
date: 2026-10-12
categories: ["drivers"]
tags: ["wifi disappeared", "wireless adapter missing", "windows 11", "driver", "troubleshooting"]
description: "WiFi gone from your laptop entirely? Troubleshoot the missing adapter — radio switches, driver failures, BIOS toggles, and hardware tests."
thumbnail: "/images/thumbs/troubleshoot-wifi-disappeared-from-laptop.webp"
faqs:
  - q: "What should I check first when WiFi disappears?"
    a: "Check airplane mode, any physical WiFi switch, and the Fn-key wireless toggle before anything else. These hardware-level switches can make the adapter vanish from Device Manager entirely, and no driver fix will help while the radio is switched off at the hardware level."
  - q: "Why is my wireless adapter missing from Device Manager?"
    a: "Either the driver failed so badly Windows can't enumerate the device, the adapter is disabled in BIOS, or the card itself has failed. Check View > Show hidden devices first, then the BIOS wireless toggle, then test with a Linux live USB to separate software from hardware failure."
  - q: "Can a Windows update make WiFi disappear?"
    a: "Yes. Major Windows updates occasionally drop the wireless driver during migration or install an incompatible replacement that fails to initialize the card. When WiFi vanishes the morning after an update, a driver reinstall from the manufacturer's support site is the standard fix."
  - q: "How do I tell a dead WiFi card from a driver problem?"
    a: "Boot a Linux live USB. Linux uses completely different drivers, so if WiFi works there, your card is alive and Windows is the problem. If Linux also finds no wireless hardware, the card has failed or come unseated — check the M.2 connection or replace the card."
---

When WiFi disappears from a laptop — no icon, no network list, no WiFi section in Settings — the operating system has lost sight of the wireless hardware. This is a different beast from a broken connection: there's nothing to connect with. Troubleshooting it means working downward through the layers that can hide an adapter: hardware switches, BIOS toggles, driver failures, and finally the card itself.

Each layer has a definitive test, so you'll always know whether to keep going or stop.

One more thing worth knowing before you start: a disappeared adapter is one of the few WiFi problems where the order of checks genuinely matters. Toggling a hardware switch takes five seconds and instantly rules out an entire category, while reinstalling drivers takes twenty minutes and accomplishes nothing if the radio is switched off in BIOS. Technicians always clear the physical and firmware layers first for exactly this reason — it prevents the classic trap of performing an impressive driver surgery on a laptop whose WiFi was simply turned off. Keep a phone or second device nearby too, since you'll need internet access to download drivers if the laptop's own wireless is down.

## Why this happens

- **Hardware radio switch off:** Physical switches and Fn-key toggles electrically disable the radio, hiding the adapter.
- **Airplane mode wedged on:** A stuck airplane state suppresses the adapter across reboots.
- **Driver failed to initialize:** Incompatible or corrupted drivers leave the card unenumerated.
- **BIOS wireless toggle disabled:** Firmware-level disable removes the hardware from the OS completely.
- **Windows Update dropped the driver:** Feature updates occasionally lose the wireless driver package.
- **Power management parked the card:** Deep sleep states the adapter never wakes from.
- **Corrupted device enumeration:** Damaged registry entries block Windows from listing the adapter.
- **Dead or unseated wireless card:** Hardware failure or a loose M.2 connection after drops or servicing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check every radio switch

1. Toggle **Airplane mode** off in Quick Settings (**Windows + A**), then on and off once more.
2. Inspect the laptop's edges for a **physical wireless switch** and flip it to on.
3. Press the **Fn-key wireless toggle** (often Fn+F2) and watch for an on-screen indicator.
4. Restart after toggling — radio states sometimes need a reboot to propagate to Device Manager.

### Fix 2: Look for the adapter in Device Manager

1. Open **Device Manager** and expand **Network adapters**.
2. Click **View → Show hidden devices** — a greyed-out wireless adapter means the driver sees hardware it can't initialize.
3. Check **Other devices** for **Network Controller** with a warning — that's your card with a dead driver.
4. Complete absence (even hidden) points to BIOS disable or hardware failure — note which case you have.

### Fix 3: Force hardware re-detection

1. In Device Manager, click **Action → Scan for hardware changes**.
2. If the adapter appears briefly then vanishes, the driver is crashing on load.
3. Try **Action → Add legacy hardware** only as a diagnostic — it rarely fixes modern wireless cards but reveals enumeration issues.
4. Move to driver repair if the scan finds the card at all.

### Fix 4: Reinstall the wireless driver cleanly

1. If the adapter is visible, **Uninstall device** with driver deletion checked, then restart.
2. If it's invisible, download the manufacturer's wireless driver using another device and transfer via USB.
3. Install the OEM package and restart, then check for the WiFi option in Settings.
4. Get drivers from [Dell support](https://www.dell.com/support), [HP support](https://support.hp.com/us-en), or [Lenovo support](https://support.lenovo.com/us/en/) for your exact model. The Windows 11-specific walkthrough is in our [vanished WiFi guide](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/).

### Fix 5: Verify the BIOS wireless setting

1. Enter **BIOS/UEFI setup** and locate the **WLAN/Wireless** toggle under Security or Devices.
2. Ensure it's **Enabled** — this single setting overrides everything in Windows.
3. While there, check for a **wireless power** or **radio** option on some business models.
4. Save, exit, and recheck Device Manager — a BIOS-disabled card appears for no driver on earth. If you recently updated the BIOS, also check the update's release notes — some versions document wireless defaults changing, which confirms you're dealing with a settings reset rather than a failure.

### Fix 6: Cold boot with Fast Startup off

1. Disable **Fast Startup** in Power Options.
2. Shut down completely, disconnect the charger, and hold the power button for 15 seconds to drain residual power.
3. Power on and check for the adapter.
4. This full power cycle resets the embedded controller's device state, which warm reboots preserve.

### Fix 7: Reset the network stack

1. In an admin Terminal, run:
   `netsh winsock reset`
   `netsh int ip reset`
   `ipconfig /flushdns`
2. Then use **Settings → Network → Advanced → Network reset**.
3. Restart and look for WiFi.
4. This repairs corrupted enumeration data that can hide a present-but-confused adapter. If the icon is missing but the adapter works, see [WiFi option missing](/articles/wifi-disappeared-windows-11-no-wifi-option/).

### Fix 8: Prove hardware vs. software

1. Boot a **Linux live USB** and check for wireless — working WiFi in Linux exonerates the card completely.
2. If comfortable opening the laptop, reseat the **M.2 wireless card** and its antenna wires per the service manual.
3. Check Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) for wireless known issues.
4. No WiFi in Linux either means a failed card — replacements are cheap on socketed models, or use a USB WiFi adapter as a stopgap.

## Closing

Disappeared WiFi is a visibility problem, and visibility has layers: switches, BIOS, driver, enumeration, hardware. Test each layer with its definitive check — the toggle, the BIOS setting, the driver reinstall, the Linux boot — and you'll find the exact layer that's hiding your adapter. Most of the time it's the driver, and it's back within the hour. And once it's back, take thirty seconds to note what fixed it; if the same update breaks it again next month, you'll know exactly where to go instead of starting from scratch.
