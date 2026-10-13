---
title: "WiFi Disappeared From Your Laptop? Complete Troubleshooting Guide"
slug: wifi-disappeared-from-laptop-troubleshooting
date: 2026-10-04
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi option", "wireless adapter", "windows 11", "wifi driver"]
description: "WiFi icon gone and no wireless option on your laptop? Troubleshoot missing WiFi adapters, from airplane mode checks to driver reinstalls."
thumbnail: "/images/thumbs/wifi-disappeared-from-laptop-troubleshooting.webp"
faqs:
  - q: "Why did the WiFi option completely disappear from my laptop?"
    a: "The most common cause is the wireless adapter driver failing or being removed — often after a Windows update — so Windows no longer sees any WiFi hardware. Other causes include airplane mode stuck on, the adapter disabled in Device Manager or BIOS, or a failed WiFi card. If the adapter is missing from Device Manager entirely, suspect driver or hardware; if it's present but disabled, it's usually a quick toggle fix."
  - q: "How do I get the WiFi icon back on Windows 11?"
    a: "First check Settings → Network & internet and look for a WiFi toggle — if the whole WiFi section is missing, open Device Manager and check Network adapters for your wireless card. Re-enable it if disabled, or reinstall its driver if it shows a warning. Restarting the WLAN AutoConfig service and running the network troubleshooter resolves many cases where the icon vanished but hardware is fine."
  - q: "Can airplane mode make WiFi disappear permanently?"
    a: "Airplane mode itself is just a toggle, but on some laptops a stuck airplane-mode state (or a broken function-key toggle) keeps the radio off even when the UI says otherwise. Try the physical WiFi switch or Fn-key combo on your laptop, toggle airplane mode on and off in Settings, and check Device Manager to confirm the adapter isn't software-disabled."
  - q: "What if my WiFi adapter is not in Device Manager at all?"
    a: "First enable 'Show hidden devices' in Device Manager's View menu — the adapter may be present but ghosted. If it's truly absent, check BIOS/UEFI to confirm the wireless card is enabled, then try a full power drain (shutdown, unplug, hold power 30 seconds). Persistent absence across all of this usually means the WiFi card has failed or worked loose — on many laptops it's a replaceable M.2 module."
---

One day the WiFi icon is there; the next, it's gone — no WiFi section in Settings, no available networks, just an Ethernet option staring back at you. A missing WiFi adapter is different from a WiFi connection problem: Windows isn't failing to connect, it's failing to see the hardware at all. That distinction shapes the entire troubleshooting path.
The causes split cleanly into three buckets: something turned the radio off (airplane mode, function keys, BIOS), the driver broke (Windows Update's favorite trick), or the hardware itself gave up. This guide checks them in that order — cheapest fix first. If your WiFi vanished specifically after an update, our [no-WiFi-option guide](/articles/wifi-disappeared-windows-11-no-wifi-option/) targets that scenario directly.
Before you start, note your laptop's exact model and WiFi card brand (Intel, MediaTek, Realtek, Qualcomm) — you'll find it on a sticker or in Device Manager if the adapter still appears. That detail matters because Intel and MediaTek cards have famously different failure modes, covered in our [Intel AX201 fixes](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) and the broader [WiFi adapter troubleshooting](/articles/how-to-fix-wifi-adapter-not-showing-up-in-windows-11-24h2/) guide.

## Why this happens

- **Airplane mode or hardware radio switch engaged.** A function-key toggle or physical switch kills the radio while Windows shows no WiFi section at all.
- **Wireless adapter disabled in Device Manager.** Power management or a glitch disables the device; disabled adapters vanish from Settings.
- **Driver corrupted by Windows Update.** The single most common cause — an update replaces or breaks the WiFi driver.
- **WLAN AutoConfig service stopped.** Without this service running, Windows can't manage wireless connections even with a healthy adapter.
- **Adapter disabled in BIOS/UEFI.** A BIOS reset or update can flip the wireless card off at the firmware level.
- **Failed WiFi card hardware.** M.2 WiFi modules do die, especially after heat stress or liquid exposure.
- **Loose antenna or card connection.** A card that worked loose loses both WiFi and Bluetooth simultaneously (they usually share the module).
- **Corrupted network stack.** Rare, but Winsock corruption can hide adapters from the Settings UI while Device Manager looks normal.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode and hardware radio switches

The embarrassingly common fix — rule it out in sixty seconds before doing anything drastic.

1. Open Settings → Network & internet and check whether Airplane mode is on; toggle it off and wait 30 seconds.
2. Look for a physical WiFi switch on the laptop's sides or front edge — some business laptops still have them.
3. Try the function-key combo (usually Fn + F2/F3 or a key with a radio-tower icon) to toggle the wireless radio.
4. Check the system tray: if you see an airplane icon, the radio is off regardless of what Settings claims.
5. If the toggle seems stuck, restart the laptop — a hung radio state often clears on reboot.

### Fix 2: Verify the adapter in Device Manager

This tells you which bucket you're in: disabled adapter (easy), driver error (medium), or missing hardware (hard).

1. Open Device Manager (Windows + X) → expand 'Network adapters.'
2. If your WiFi adapter appears with a down arrow, right-click → Enable device.
3. If it shows a yellow warning icon, right-click → Properties and read the Device status error code.
4. Click View → 'Show hidden devices' — a grayed-out adapter means Windows sees it but can't start it.
5. If no wireless adapter appears at all, even hidden, skip to Fix 6 (BIOS/power drain) — the hardware isn't enumerating.

### Fix 3: Restart WLAN AutoConfig and related services

These services are the bridge between the adapter and the Settings UI; when they stall, WiFi vanishes from view.

1. Press Windows + R, type services.msc, and press Enter.
2. Find 'WLAN AutoConfig,' right-click → Restart, and set Startup type to Automatic.
3. Do the same for 'WWAN AutoConfig' if present.
4. Open Settings → Network & internet and check whether the WiFi section reappears within a minute.
5. If the service refuses to start, note the error — it often points at the underlying driver problem.

### Fix 4: Reinstall the WiFi adapter driver

The highest-success fix for update-broken WiFi: strip the bad driver and install the correct one.

1. In Device Manager, right-click the WiFi adapter → Uninstall device, checking 'Attempt to remove the driver for this device.'
2. Restart the laptop — Windows will attempt to reinstall a driver on boot.
3. If WiFi returns with a generic driver, download the proper driver for your exact model from the maker's support site (Dell, HP, Lenovo).
4. Install the manufacturer's driver package, which often includes the Bluetooth driver for the combo card too.
5. If you have no internet at all, download the driver on another device and transfer it via USB — or use your phone's USB tethering as a temporary connection.

### Fix 5: Run the network troubleshooter and reset the stack

Windows' built-in tools handle the stack-corruption cases that manual driver work misses.

1. Open Settings → System → Troubleshoot → Other troubleshooters → run 'Network and Internet.'
2. Follow its prompts — it can re-enable adapters and restart services automatically.
3. If that fails, open Command Prompt as administrator and run: netsh winsock reset, then netsh int ip reset.
4. Reboot and check for the WiFi section.
5. As a last software resort, use Settings → Network & internet → Advanced → Network reset, which reinstalls all adapters fresh.

### Fix 6: Check BIOS and perform a full power drain

When the adapter is invisible even as a hidden device, the problem is below Windows — firmware or hardware.

1. Restart into BIOS/UEFI (usually F2, F12, or Del during boot) and look for Wireless/WLAN settings — ensure they're Enabled.
2. While there, check whether the BIOS lists the WiFi card in its device inventory at all.
3. Shut down completely, unplug everything, and hold the power button for 30 seconds to drain residual charge.
4. Power on and recheck Device Manager — a card that reappeappears after a drain was wedged, not dead.
5. If the card is enabled in BIOS but never appears in Windows, the M.2 module has likely failed; check Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) for hardware diagnostics, then consider a replacement card.

### Fix 7: Replace or work around a dead WiFi card

Hardware failure isn't the end — M.2 WiFi cards are cheap and often user-replaceable, and USB adapters are instant.

1. Confirm the diagnosis: adapter absent in BIOS device list and Device Manager across reboots and power drains.
2. For an immediate fix, plug in a USB WiFi adapter — Windows usually installs its driver automatically.
3. For a permanent fix, buy a compatible M.2 WiFi card (Intel AX210 is a popular, broadly compatible upgrade).
4. Follow a disassembly guide for your exact model; on many laptops the card sits under a bottom-panel hatch with one screw.
5. If you're not comfortable opening the laptop, a repair shop typically charges modest labor for this ten-minute job.

## Closing

A vanished WiFi adapter feels catastrophic but is usually a toggle, a service, or a driver away from recovery. Work from the radio switch inward — airplane mode, Device Manager, services, driver, BIOS — and you'll find the layer where your WiFi went missing.
