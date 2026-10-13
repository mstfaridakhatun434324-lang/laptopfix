---
title: "WiFi Completely Disappeared From Your Laptop? Step-by-Step Recovery"
slug: "how-to-fix-wifi-disappeared-from-laptop-step-by-step"
date: "2026-09-28"
categories: ["drivers"]
tags: ["wifi disappeared", "no wifi", "wireless", "network", "drivers"]
description: "No WiFi option anywhere on your laptop? Follow a technician's step-by-step recovery: from quick checks to driver repair and network resets that bring WiFi back."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop-step-by-step.webp"
faqs:
  - q: "What should I do first when WiFi disappears from my laptop?"
    a: "Check airplane mode and your laptop's wireless function key first — they are the fastest fixes. Then open Device Manager with hidden devices shown to see whether the adapter is disabled, hidden, or truly gone. This sixty-second triage tells you whether you are dealing with a switched-off radio, a driver problem, or a deeper system issue, and it directs every step that follows."
  - q: "Why is there no WiFi option in Windows Settings at all?"
    a: "Windows only shows WiFi settings when it detects a working wireless adapter. If the driver failed, the card is disabled in BIOS, or airplane mode is stuck on, Windows hides the entire WiFi section rather than showing an error. Restoring the adapter — via driver reinstall, BIOS enable, or radio toggle — makes the Settings page reappear automatically."
  - q: "Will a network reset bring back missing WiFi?"
    a: "It can, when the cause is corrupted network configuration rather than a missing driver. Network reset reinstalls all adapters and clears every profile, which fixes stack corruption that hides the adapter. But if Device Manager shows no wireless hardware at all, reset alone will not help — you need driver or BIOS-level repair first. Use it as a late step, not the first one."
  - q: "How do I know if my WiFi card is dead?"
    a: "If the adapter is absent from Device Manager even with hidden devices shown, missing in BIOS, and invisible to a Linux live USB, the card has likely failed or worked loose. WiFi cards rarely die suddenly without symptoms — preceding dropouts and disconnects are the usual warning. A USB WiFi adapter is a cheap confirmation test and a practical permanent workaround."
---

The WiFi icon is gone from the taskbar. Settings shows no WiFi section. Device Manager may not even list a wireless adapter. When WiFi disappears completely, the natural reaction is panic — but this problem has one of the most reliable step-by-step recoveries in all of laptop troubleshooting, because the causes form a short, checkable list.

The key insight is that "WiFi disappeared" is a symptom with about seven possible diseases, ranging from a bumped function key to a corrupted driver stack. Work them in order from simplest to deepest, verifying after each step, and you will find the culprit without wasting time on fixes for problems you don't have.

## Why this happens

- **Airplane mode stuck on:** The radio kill persists across reboots and hides all wireless hardware.
- **Wireless function key toggled:** A hardware-level radio switch Windows cannot override.
- **Adapter disabled in Device Manager:** Accidentally disabled, or disabled by a failed driver update.
- **Corrupted wireless driver:** Update damage removes the adapter from the device list.
- **Wireless turned off in BIOS:** Firmware toggle hides the card before Windows boots.
- **Corrupted network stack:** Damaged Winsock/TCP-IP configuration blocks adapter enumeration.
- **Failed or loose WiFi card:** Hardware failure, the least common but real possibility.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode and the hardware wireless switch
Press Windows key + A and verify airplane mode is off — toggle it on and off once to clear a stuck state. Then press your laptop's wireless key (Fn + the tower-icon key, often F2 or F3) and look for an LED change. Some laptops also have a physical side switch. These hardware-level controls override everything in software, and an accidental bump is the number one cause of sudden total WiFi loss. If WiFi returns here, you are done in under a minute.

### Fix 2: Inspect Device Manager with hidden devices shown
Open Device Manager, click View, "Show hidden devices," and expand Network adapters. If your wireless adapter appears greyed out, right-click and enable it. If it shows a warning icon, note the error code — Code 10 and Code 43 point to driver problems. If the adapter is missing entirely, click Action, "Scan for hardware changes." This inspection tells you exactly which of the remaining fixes applies, so don't skip it. For deeper adapter-specific repair, see our guide on the [WiFi adapter not showing up](/articles/how-to-fix-wifi-adapter-not-showing-up-on-windows-11/).

### Fix 3: Reinstall the wireless driver from the manufacturer
On another device, download the WiFi driver for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/). Transfer it via USB. In Device Manager, uninstall the wireless adapter with driver deletion, then install the downloaded driver and reboot. OEM drivers include firmware and regulatory hooks the generic Windows driver lacks. After reinstalling, block automatic driver replacement in Device Installation Settings so Windows Update doesn't undo your work. Our [driver reinstall walkthrough](/articles/how-to-reinstall-wifi-driver-on-windows-11/) details the clean technique.

### Fix 4: Enable wireless in BIOS and disable fast startup
Restart into BIOS/UEFI setup and confirm the WLAN/wireless entry is Enabled. While there, disable Fast Boot if present. Back in Windows, go to Power Options, "Choose what the power buttons do," and uncheck fast startup. Then shut down fully, unplug, hold the power button 30 seconds, and boot. This combination fixes cases where the card is hidden at firmware level or skipped during hybrid boot — particularly common after BIOS or Windows updates.

### Fix 5: Reset the network stack via Command Prompt
Open an elevated Command Prompt and run, in order: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`. Restart the laptop. These commands rebuild the networking components that a corrupted stack uses to hide adapters. If Device Manager showed the adapter but Windows still offered no WiFi, this step frequently closes the gap. Microsoft documents the network repair sequence at Windows support.

### Fix 6: Perform a full network reset
Go to Settings, Network and internet, Advanced network settings, Network reset. Confirm and restart. This reinstalls every network adapter to factory defaults and clears all profiles — the deepest software reset short of reinstalling Windows. You will need to re-enter WiFi passwords afterward, so have them handy. If WiFi appears after the reset, the cause was configuration corruption; if not, you have eliminated software configuration as the cause.

### Fix 7: Test the hardware and use a USB adapter as fallback
Boot a Linux live USB: working WiFi there means your Windows install needs repair; absent WiFi there means hardware trouble. Reseat the WiFi card if your laptop allows access, or simply plug in a USB WiFi adapter — a $15–$25 fix that restores full wireless without opening the machine. If the internal card is dead and the laptop is under warranty, file a claim with the diagnostics you've gathered. For persistent cases, the Microsoft Update Catalog can supply alternate driver versions to try.

## Closing
Total WiFi disappearance looks catastrophic but follows a short checklist: radio switches, Device Manager state, driver reinstall, BIOS enable, stack reset, network reset, hardware test. Each step eliminates one cause, and working them in order means you find the real problem — usually in the first three steps — instead of guessing at all seven. Once WiFi is back, make the fix stick: write down your WiFi passwords somewhere safe, because the network reset you may have used wipes them and the next one will too. Keep the OEM wireless driver installer on a USB stick — the cruel irony of WiFi failures is that you need the internet to download the fix for having no internet. After every Windows feature update, verify the wireless driver version hasn't been swapped; catching it early is a five-minute reinstall versus a full diagnostic session later. If your laptop has a physical wireless switch, develop the habit of checking it first whenever wireless acts up — it remains the number one cause of sudden total loss. And consider the USB WiFi adapter not just as a fallback but as a permanent diagnostic tool: when internal wireless misbehaves, a ten-second plug-in test instantly tells you whether the problem is the card or the OS.
