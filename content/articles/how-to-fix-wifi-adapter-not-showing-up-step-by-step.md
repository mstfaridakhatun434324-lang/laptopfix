---
title: "WiFi Adapter Not Showing Up? Step-by-Step Recovery Guide"
slug: how-to-fix-wifi-adapter-not-showing-up-step-by-step
date: 2026-10-13
categories: ["drivers"]
tags: ["wifi", "network adapter", "device manager", "wireless driver", "troubleshooting"]
description: "WiFi adapter not showing up on your laptop? Follow this step-by-step recovery: reveal hidden adapters, fix BIOS toggles, and reinstall wireless drivers."
thumbnail: "/images/thumbs/how-to-fix-wifi-adapter-not-showing-up-step-by-step.webp"
faqs:
  - q: "Why is there no WiFi option in Windows Settings?"
    a: "Windows isn't loading a WiFi adapter — it's disabled, its driver failed, or it's toggled off in BIOS. Check Device Manager with Show hidden devices enabled, verify the BIOS wireless toggle, and reinstall the wireless driver from your laptop manufacturer's support site."
  - q: "My WiFi adapter is grayed out in Device Manager. What does that mean?"
    a: "A grayed-out adapter is not starting — usually a failed driver binding or a disabled state rather than dead hardware. Right-click it and try Enable first. If that fails, uninstall it with the remove driver option checked, scan for hardware changes, and install the wireless driver from your laptop manufacturer's support site."
  - q: "Can a Windows update make the WiFi adapter disappear?"
    a: "Yes, it is a common trigger. The update may install an incompatible wireless driver or disturb a power setting that parks the adapter. Reinstalling the manufacturer's Wireless LAN driver and disabling Fast Startup resolves most post-update disappearances — then block the bad driver version from returning."
  - q: "How can I tell if my WiFi card is physically dead?"
    a: "Boot a Linux live USB and check for the adapter there. If it appears and works in Linux, the hardware is fine and you are dealing with a Windows driver issue. If it is invisible in Linux too — after reseating the card and checking antenna leads — the card has likely failed physically."
---

A WiFi adapter that doesn't show up — no icon in the taskbar, no WiFi section in Settings, nothing under Network adapters — is one of the most disorienting Windows failures because the usual 'reconnect' instincts have nothing to grab onto. But the diagnostic logic is straightforward: either Windows can't see the hardware, or it sees it and can't start it. Everything below determines which, then fixes it.

This guide is brand-neutral and works for Intel, MediaTek, Realtek, and Qualcomm adapters on any Windows 10 or 11 laptop. The steps escalate from 30-second checks to the hardware verdict, and each one tells you explicitly what a positive or negative result means.

Don't skip the order. Step 3's hidden-devices check is the pivot the whole diagnosis turns on.

Keep the two failure families straight as you diagnose: adapter missing (Windows cannot see the hardware — BIOS, toggles, enumeration) versus adapter present but broken (driver errors, Code 10 or 43). The fixes below handle both, but knowing which family you are in determines where to spend your effort.

## Why this happens

- **Adapter disabled:** A disabled adapter vanishes from Settings and the taskbar while remaining in Device Manager.
- **Failed driver hidden from normal view:** Driver failures often show only as grayed entries under Show hidden devices.
- **BIOS/firmware wireless toggle off:** Firmware-level radio switches that OS updates or BIOS resets can flip.
- **Physical wireless switch or Fn toggle:** Hardware kill switches and Fn combos that unload the adapter.
- **Driver replaced by incompatible version:** Windows Update installing a driver the card firmware rejects.
- **Power management deep-sleep:** The adapter parked in a state it can't wake from, invisible to the OS.
- **Corrupted network stack:** Stack corruption hiding adapters from the network UI.
- **Dead or unseated wireless card:** Genuine hardware failure — diagnosed last, never first.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious: switches, keys, and Settings

Thirty seconds that resolve a real share of cases.

1. Look for a physical wireless switch on the laptop's side/front edge and ensure it's on.
2. Press the wireless Fn key (**Fn + F2/F3/F8** varies) and watch for the radio indicator.
3. Open **Settings → Network & internet** — is there a **WiFi** section at all? Missing section = driver/BIOS problem; present-but-off = just toggle it on.
4. Check **Airplane mode** is off (**Win + A**).

### Fix 2: Look in Device Manager — normal and hidden views

The pivot: what does Windows actually see?

1. **Device Manager → Network adapters**: adapter present with warning = driver problem (note the code). Present and healthy = UI/stack problem.
2. **View → Show hidden devices**: grayed-out adapter = failed or disabled binding. Right-click → **Enable**; if that fails, **Uninstall** (check remove driver) → **Action → Scan for hardware changes**.
3. Check **Other devices** for unknown network controllers — the card may be unrecognized rather than missing.
4. Completely absent everywhere = proceed to BIOS checks next.

### Fix 3: Verify BIOS wireless settings

Rule out the firmware kill switch.

1. Reboot into BIOS/UEFI (**F2**, **Del**, **F1**, or **Fn+F2** depending on brand).
2. Find the wireless/WLAN toggle (often under **Security → I/O Port Access**, **Advanced**, or **Configuration**) and set it to **Enabled**.
3. Save, exit, recheck Device Manager.
4. If the adapter appears now, a BIOS reset or update had disabled it.

### Fix 4: Reinstall the wireless driver from the manufacturer

The core software repair for invisible adapters.

1. From your laptop maker's support site, download the **Wireless LAN** driver for your exact model.
2. In Device Manager, uninstall every trace of the adapter (including hidden grayed entries), checking **Attempt to remove the driver**.
3. Reboot, install the manufacturer's package, reboot again.
4. Verify the adapter appears in Network adapters with no warning, then check Settings for the WiFi section.

### Fix 5: Reset the network stack and clear power states

Fix the software layers around the adapter.

1. Elevated Command Prompt: **netsh winsock reset** + **netsh int ip reset**, then reboot.
2. **Settings → Network & internet → Advanced network settings → Network reset** as the GUI alternative.
3. Adapter **Properties → Power Management** → uncheck **Allow the computer to turn off this device**.
4. Turn off **Fast Startup**, do a full shutdown, power on, recheck.

### Fix 6: Try the adapter vendor's driver and older versions

When the manufacturer's package doesn't take.

1. Identify the card exactly (**Hardware Ids** in Device Manager → Details).
2. For Intel: run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html). For MediaTek/Realtek/Qualcomm: the vendor's support download page.
3. If the newest driver fails, try one version older — regressions happen.
4. Block the bad version afterward via **Show or hide updates** so Windows doesn't reinstall it.

### Fix 7: Hardware verdict: reseat, live USB, replace

The final arbiter, in order.

1. If the model allows, reseat the M.2 wireless card and snap both antenna leads firmly on.
2. Boot a Linux live USB: adapter works there = Windows driver problem, keep fighting it in software. Invisible there = hardware.
3. Replacement M.2 2230 WiFi cards are inexpensive and user-replaceable on many models — or use a USB WiFi adapter as the zero-disassembly fix.

### Fix 8: Verify the WLAN AutoConfig service and rebuild Winsock fully

The adapter depends on Windows services and a healthy network stack. When both are verified, missing-adapter cases narrow to drivers or hardware fast.

1. In **services.msc**, ensure **WLAN AutoConfig** is **Running** and set to **Automatic** — the adapter cannot function without it.
2. In an elevated prompt, run **netsh winsock reset catalog**, then **netsh int ipv4 reset** and **netsh int ipv6 reset**, then reboot.
3. Check **Task Manager → Services** for third-party network services (VPNs, firewalls) starting before WLAN AutoConfig and delaying or blocking it.
4. If the adapter appears after disabling a VPN client's service, update or reinstall that client — its filter driver was the blocker.

## Closing

A missing WiFi adapter is a detection story: switches, BIOS toggles, hidden failed bindings, then drivers — in that order. The hidden-devices view is the single most informative check in the sequence; it separates 'Windows sees broken hardware' from 'Windows sees nothing' in one glance. Work it like a flowchart rather than a grab-bag, and the adapter reappears — or the Linux test honestly tells you it's a hardware replacement. If the adapter appears but reports Code 10, follow [Code 10 WiFi repair](/articles/how-to-fix-wifi-driver-code-10-error-on-dell-laptop/). For MediaTek cards specifically, see [MediaTek WiFi not working](/articles/how-to-fix-mediatek-wifi-not-working-on-acer-laptop/).
