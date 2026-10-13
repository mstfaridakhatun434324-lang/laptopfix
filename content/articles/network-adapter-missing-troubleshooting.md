---
title: "Network Adapter Missing: Full Troubleshooting Walkthrough"
slug: network-adapter-missing-troubleshooting
date: 2026-09-30
categories: ["drivers"]
tags: ["network adapter", "missing adapter", "troubleshooting", "device manager", "no internet"]
description: "Complete troubleshooting for a missing network adapter on Windows laptops: every diagnostic layer from BIOS to hardware replacement."
thumbnail: "/images/thumbs/network-adapter-missing-troubleshooting.webp"
faqs:
  - q: "What should I check first when the network adapter is missing?"
    a: "First, open Device Manager, click View → Show hidden devices, and expand Network adapters. This 30-second check distinguishes a disabled adapter (grayed out, right-click to enable) from a truly missing one. Second, check whether the problem followed a Windows update — if so, driver rollback or reinstallation is the likely fix. These two checks direct everything that follows."
  - q: "Why would a network adapter disappear after sleep or hibernation?"
    a: "Power management is the usual culprit: Windows powers down the network adapter to save battery and it fails to reinitialize on wake. Disabling 'Allow the computer to turn off this device to save power' on the adapter and turning off Fast Startup resolves most sleep-related disappearances. The adapter isn't gone — it's stuck in a low-power state."
  - q: "Can a BIOS update make network adapters disappear?"
    a: "Yes. BIOS updates sometimes reset device toggles to defaults that disable WLAN or LAN, or introduce firmware bugs affecting device enumeration. After any BIOS update, enter setup and verify all network devices are enabled. If adapters vanished immediately after a BIOS update, check the manufacturer's support page for a follow-up fix."
  - q: "When should I give up and replace the hardware?"
    a: "When the adapter is absent from BIOS/UEFI device lists, invisible to a Linux live USB, and unresponsive to reseating (for socketed cards) — at that point every software layer has been eliminated. For soldered adapters, a USB network adapter is the practical replacement. Get a second opinion from the manufacturer's diagnostics before spending money."
---

This is the deep-dive companion to quick-fix guides: a full troubleshooting walkthrough for a missing network adapter that leaves no layer unexamined. Where quick guides give you the most likely fixes first, this one is exhaustive — BIOS, firmware, driver stack, OS services, filter drivers, power states, and hardware, each with its diagnostic test and its repair.

Use it when the quick fixes didn't work, or when you want to understand exactly which layer failed rather than just making the symptom go away. Precision matters here because the wrong "fix" — like reinstalling Windows for a BIOS-disabled adapter — wastes hours.

## Why this happens

- **BIOS device toggles:** WLAN/LAN switches in firmware hide hardware from the OS entirely.
- **Windows Update driver replacement:** New drivers that fail to initialize the hardware, removing it from enumeration.
- **Corrupted network stack:** Winsock and TCP/IP damage suppressing adapter visibility.
- **Fast Startup state caching:** Broken device states preserved across reboots by hybrid shutdown.
- **Filter driver corruption:** VPN and security filter drivers breaking the network device chain.
- **Chipset/platform driver failure:** The underlying bus enumeration broken by bad chipset drivers.
- **Embedded controller issues:** The EC managing radio/power states locking up.
- **Hardware failure:** Dead modules, damaged controllers, or loose connections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Map the failure — what's missing exactly?

1. Open **Device Manager → View → Show hidden devices** and document precisely which adapters are missing: WiFi only, Ethernet only, or both.
2. Check **Settings → Network & internet** — is the entire WiFi section gone, or just disconnected?
3. Note the timeline: did it follow an update, a sleep/wake, a BIOS change, or happen spontaneously?
4. Both missing suggests shared infrastructure (chipset, stack, BIOS); one missing suggests that specific adapter's driver or hardware. This scoping prevents fixing the wrong thing.

### Fix 2: Audit BIOS and firmware settings

1. Enter **BIOS/UEFI** and verify **WLAN**, **Wireless**, **LAN**, **Onboard LAN** are all **Enabled**.
2. Check the BIOS **system information / device list** page — adapters listed here prove hardware visibility at the firmware level.
3. Look for **Deep Sleep**, **PowerShare**, or similar power features that can gate network hardware, and set them to standard values.
4. If you updated BIOS recently, **Load Optimized Defaults**, re-enable network devices manually, and check the maker's site for a newer BIOS addressing enumeration bugs.

### Fix 3: Clear power states completely

1. Disable **Fast Startup** in Power Options.
2. Shut down, unplug AC **and** all USB devices, then hold the power button **60 seconds** — longer than usual, to fully drain the EC.
3. For removable-battery models, take the battery out during this drain.
4. Boot and check Device Manager before Windows has a chance to sleep — catching the adapter in its freshly-enumerated state tells you whether the problem is enumeration or power-state degradation.

### Fix 4: Rebuild the network stack methodically

1. In an admin Terminal, run in order: `netsh winsock reset`, `netsh int ip reset`, `netsh advfirewall reset`, `ipconfig /flushdns`.
2. Run `netcfg -d` to wipe all network device configurations (have drivers ready on USB first).
3. Use **Settings → Network & internet → Advanced network settings → Network reset**.
4. Reboot between major steps, not just at the end — each rebuild needs a fresh enumeration to take effect. This layered rebuild also addresses the [update-triggered variant](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/).

### Fix 5: Purge filter drivers and virtual adapters

1. Uninstall VPN clients, virtual machine network tools, and third-party firewalls temporarily.
2. In Device Manager (hidden devices shown), uninstall all **WAN Miniport** devices and any virtual adapters with warnings.
3. Check **Control Panel → Network Connections** for ghost connections and delete them.
4. Reboot and verify physical adapters return before reinstalling any of the removed software — then reinstall one at a time to identify the offender.

### Fix 6: Reinstall the driver stack bottom-up

1. With drivers prepared on USB (download on another device), install **chipset drivers** first and reboot.
2. Install **Ethernet**, then **wireless**, then **Bluetooth** — rebooting after each.
3. In Device Manager, confirm each adapter's **Properties → Driver** shows the version you installed, not a Windows-substituted one.
4. For Intel wireless cards, cross-reference symptoms with the [AX201-specific guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/) — that card has unique failure modes worth ruling out.

### Fix 7: Verify OS services and system integrity

1. Confirm **WLAN AutoConfig**, **WWAN AutoConfig**, and **Network Connections** services are running and Automatic.
2. Run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` in an admin Terminal.
3. Check **Event Viewer → System** for network-related errors at boot — failed driver loads log here with specific error codes.
4. If SFC finds unfixable corruption, an **in-place upgrade** (Windows installer → keep files and apps) rebuilds the OS without wiping data.

### Fix 8: Prove hardware fault and choose the workaround

1. Boot a **Linux live USB**: adapters visible there = Windows-only problem, keep troubleshooting software. Invisible = hardware or BIOS.
2. Run manufacturer diagnostics (Dell ePSA, Lenovo UEFI diagnostics) — they test network hardware below the OS.
3. For socketed WiFi cards, reseat the M.2 module and antenna wires; for Ethernet, there's no user-serviceable part.
4. Confirmed hardware failure leaves two paths: warranty repair, or USB adapters as permanent workarounds. Document every test — support agents move faster with evidence, and the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) outlines the same escalation path.

## Closing

Thorough troubleshooting is elimination: scope the failure, audit firmware, clear power states, rebuild the stack, purge filters, reinstall bottom-up, verify services, prove hardware. Somewhere in that sequence the adapter reappears — and you'll know exactly why it vanished. Keep notes on which step fixed it and the driver versions involved; network adapter disappearances love to recur after major updates, and a documented fix turns the second occurrence into a five-minute repeat instead of another full investigation. Your future self will thank you — and so will anyone you help with the same problem down the road.
