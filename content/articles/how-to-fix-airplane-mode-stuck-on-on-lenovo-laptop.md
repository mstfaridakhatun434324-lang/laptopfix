---
title: "Airplane Mode Stuck On? Fix It on Your Lenovo Laptop"
slug: how-to-fix-airplane-mode-stuck-on-on-lenovo-laptop
date: 2026-09-22
categories: ["drivers"]
tags: ["airplane mode", "lenovo", "wifi stuck", "fn key"]
description: "Airplane mode stuck on and won't turn off on your Lenovo laptop? Fix it with these 7 repairs — Fn key, radio management, driver reinstalls, and BIOS checks."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-on-lenovo-laptop.webp"
faqs:
  - q: "Why is airplane mode stuck on my Lenovo laptop?"
    a: "The usual causes are the physical wireless switch or Fn + F-key toggle being stuck off, Lenovo's radio management driver holding the radios disabled, a Windows update breaking the WiFi driver so the toggle can't complete, or the airplane mode switch being greyed out by a corrupt network state. On Lenovos specifically, the Energy Management or Vantage radio controls can lock airplane mode on even when Windows shows it as off."
  - q: "Which Fn key turns off airplane mode on Lenovo?"
    a: "On most Lenovo laptops it's Fn + F8 (IdeaPad) or Fn + F5 (ThinkPad) — look for the airplane or radio-tower icon on the function row. If pressing it does nothing, the Lenovo hotkey driver may be missing — reinstall it from Lenovo Vantage or the support site. Note that on some models the key only works when the hotkey driver is installed; without it, use the Windows Settings toggle instead."
  - q: "Can I turn off airplane mode without the Fn key?"
    a: "Yes. Click the network/volume/battery icons in the taskbar to open Quick Settings and click the Airplane mode tile to toggle it. Or go to Settings then Network and internet and toggle Airplane mode there. If both are greyed out or snap back on, the problem is driver-level — work through the fixes below rather than fighting the toggle."
  - q: "Will resetting network settings fix stuck airplane mode?"
    a: "Often, yes. Settings then Network and internet then Advanced network settings then Network reset reinstalls all network adapters and resets networking components to defaults, which clears the corrupt state holding airplane mode on. You'll need to re-enter WiFi passwords afterward. If the reset doesn't help, the cause is likely the radio driver or BIOS setting — see the [general airplane mode guide](/articles/best-way-to-fix-airplane-mode-stuck-on/) for the deeper driver fixes."
---

The airplane mode tile is lit, WiFi and Bluetooth are dead, and every toggle you flip snaps back to on — or is greyed out entirely. On Lenovo laptops, stuck airplane mode has Lenovo-specific wrinkles: the Fn-key radio toggle, the physical wireless switch on some models, and Lenovo's radio management software can each lock the radios off independently of Windows.

This guide is Lenovo-focused: the right Fn keys, the Lenovo drivers that matter, and the BIOS settings ThinkPads and IdeaPads hide wireless controls in. Work in order.

## Why this happens

- **Fn radio toggle or physical switch off:** The hardware-level radio kill that Windows can't override.
- **Lenovo hotkey driver missing:** Without it, the Fn radio key does nothing and Windows can't sync state.
- **Radio Management driver stuck:** Lenovo's power/radio driver holding radios disabled.
- **WiFi driver broken by update:** Airplane mode can't complete its off-transition with a failed WiFi driver.
- **Corrupt network stack state:** The toggle's state machine wedged on.
- **BIOS wireless disabled:** Firmware-level radio disable.
- **Fast Startup caching the stuck state:** The wedged state replayed on every boot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Use the Lenovo radio toggle (Fn key and physical switch)

Lenovo's hardware radio control overrides Windows — check it first.

1. Press **Fn + F8** (IdeaPad) or **Fn + F5** (ThinkPad) — the key with the airplane/radio icon. Watch for an on-screen indicator.
2. Check the laptop's edges and front lip for a **physical wireless switch** — some ThinkPads and older IdeaPads have one; slide it on.
3. If the Fn key does nothing, open **Lenovo Vantage > Device > Power** or device settings and look for wireless radio toggles there.
4. Try the Windows toggle after each hardware attempt: taskbar Quick Settings > **Airplane mode** tile.

If the hardware toggle is off, no Windows setting can bring the radios up — this step resolves a large share of cases. The [airplane mode reference](/articles/how-do-i-fix-airplane-mode-stuck-on/) documents toggle locations across brands.

### Fix 2: Reinstall the Lenovo hotkey driver

A missing hotkey driver breaks the Fn radio key and state sync.

1. Open **Lenovo Vantage** (install it from the Microsoft Store if missing) and check for driver updates — install any **Hotkeys** or **System Interface** updates.
2. Or download the hotkey driver from [Lenovo support](https://support.lenovo.com/us/en/) for your exact model.
3. Uninstall the old hotkey software first (**Settings > Apps**), restart, install fresh, restart again.
4. Test **Fn + F8/F5** — the on-screen display should now appear.

With the hotkey driver working, the Fn toggle and Windows' airplane mode state stay in sync instead of fighting.

### Fix 3: Reinstall the WiFi driver

Airplane mode can't turn off cleanly when the WiFi driver is broken underneath.

1. Press **Win + X**, open **Device Manager**, expand **Network adapters**.
2. Right-click the WiFi adapter and choose **Uninstall device**, ticking **Attempt to remove the driver**.
3. Restart — Windows reinstalls the adapter.
4. Install the WiFi driver from [Lenovo support](https://support.lenovo.com/us/en/) for your model (don't rely on Windows' choice).
5. Try the airplane mode toggle again.

If Device Manager shows the WiFi adapter with a Code 10 or it's missing entirely, fix that first — airplane mode is a symptom. A vanished adapter needs the [missing WiFi adapter guide](/articles/best-way-to-fix-wifi-adapter-not-showing-up/).

### Fix 4: Reset the network stack

Clear the wedged toggle state.

1. Go to **Settings > Network & internet > Advanced network settings > Network reset** and click **Reset now**, then restart.
2. After reboot, open Command Prompt as administrator and run:
   `netsh winsock reset`
   `netsh int ip reset`
3. Restart once more and test the airplane mode toggle.
4. Reconnect to WiFi (you'll need to re-enter passwords).

Network reset reinstalls every network adapter — it's the heavy hammer for corrupt network state, and it's safe.

### Fix 5: Check the Radio Management and power settings

Lenovo's radio/power drivers can hold the radios off.

1. In Device Manager, expand **System devices** and look for **Lenovo Radio Management** or power management entries — update or reinstall them from Lenovo support.
2. In the WiFi adapter's **Properties > Power Management**, untick **Allow the computer to turn off this device to save power**.
3. Set **Settings > System > Power & battery > Power mode** to **Best performance** while testing.
4. In **Lenovo Vantage**, check battery/power settings for any **wireless radio power saving** and disable it.

Radio management fighting Windows' own radio control is a classic Lenovo-specific wedge.

### Fix 6: Disable Fast Startup and cold boot

The stuck state may be cached across boots.

1. **Control Panel > Power Options > Choose what the power buttons do** > **Change settings that are currently unavailable** > untick **Turn on fast startup**.
2. **Shut down** fully (not restart), wait 30 seconds, power on.
3. Immediately test the airplane mode toggle before opening other apps.

If the toggle works after a cold boot but wedges again later, some startup program is re-triggering it — clean boot to find it.

### Fix 7: Check BIOS wireless settings and update BIOS

Firmware can disable radios below Windows' reach.

1. Restart into BIOS (**F1** on most Lenovos, or **Enter** then F1).
2. Look under **Security > I/O Port Access** (ThinkPad) or **Configuration** (IdeaPad) for **Wireless LAN** / **Bluetooth** toggles — set them to **Enabled**.
3. Check your BIOS version (`msinfo32`) against the latest on [Lenovo support](https://support.lenovo.com/us/en/) and update if behind — keep AC connected during the update.
4. After updating, load BIOS defaults, re-enable wireless if needed, save, and boot.

If radios stay off across Windows, Linux live USB, and BIOS-enabled settings, the wireless card itself may have failed — but that's rare compared to the software causes above.

## Closing

Stuck airplane mode on a Lenovo is usually a stack of toggles fighting: the Fn key says off, Windows says on, the radio driver says off. Working from the hardware toggle down through the hotkey driver, WiFi driver, and network reset un-wedges each layer. Once everything agrees, the toggle behaves — and keeping Lenovo Vantage's drivers current keeps it that way.
