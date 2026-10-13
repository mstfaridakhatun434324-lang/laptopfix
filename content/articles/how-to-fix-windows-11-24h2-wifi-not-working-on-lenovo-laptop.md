---
title: "How to Fix Wi-Fi Not Working After the Windows 11 24H2 Update on Lenovo"
slug: how-to-fix-windows-11-24h2-wifi-not-working-on-lenovo-laptop
date: 2026-10-11
categories: ["windows-update"]
tags: ["lenovo wifi not working 24h2", "windows 11 24h2 wifi fix", "intel ax201 driver", "wifi disappeared after update"]
description: "Lenovo laptop lost Wi-Fi after the 24H2 update? Fix the driver mismatch with Lenovo's 24H2 Wi-Fi driver, stack resets, and power-management tweaks."
thumbnail: "/images/thumbs/how-to-fix-windows-11-24h2-wifi-not-working-on-lenovo-laptop.webp"
faqs:
  - q: "Why did Wi-Fi break only after the 24H2 update?"
    a: "Because 24H2 changed network driver validation and power management. Drivers that worked on 23H2 can fail to load or misbehave under the new rules. It is a software mismatch, not hardware failure, which is why a driver update — not a new laptop — is the fix."
  - q: "Should I use Lenovo's driver or Intel's driver?"
    a: "Start with Lenovo's. It is validated for your exact model's BIOS and power management. Use Intel's Driver & Support Assistant only if Lenovo's driver does not fix it or Lenovo has not published a 24H2-specific version yet. Avoid Windows Update's offered driver until you confirm its version is the fixed one."
  - q: "Why does Windows Update keep reinstalling the broken driver?"
    a: "Windows Update's driver ranking does not always prefer the newest version, and Lenovo's fixed driver may not be in Microsoft's catalog yet. Use optional-updates deselection or the show/hide updates tool to block the bad version, and set Lenovo Vantage driver updates to manual."
  - q: "Can a BIOS update really fix Wi-Fi?"
    a: "Yes. The BIOS controls radio power states, and Lenovo has released BIOS updates specifically addressing wireless behavior under Windows 11 24H2. If driver fixes stall, an outdated BIOS is the next most likely culprit, particularly for sleep/wake Wi-Fi drops."
---

Wi-Fi dying right after the Windows 11 24H2 update is a well-documented pattern on Lenovo laptops, and it is almost never the router's fault. Version 24H2 ships with a reworked network stack and new driver enforcement, and the Wi-Fi drivers that worked fine on 23H2 — especially Intel AX201/AX211 and some Realtek and MediaTek parts — can fail to bind to the new stack. The symptom varies: no networks visible, connected-but-no-internet, or the adapter vanishing from Device Manager entirely. [Intel AX201 Wi-Fi problems on Lenovo laptops](/articles/how-to-fix-intel-wifi-6-ax201-not-working-on-lenovo-laptop/)

Lenovo-specific wrinkle: Lenovo Vantage and Windows Update sometimes install different Wi-Fi driver versions on top of each other, leaving the adapter in a conflicted state. The fixes below start with the quick adapter resets, then move to driver surgery, which is where most 24H2 Wi-Fi cases are actually resolved.

## Why this happens

- **Incompatible Wi-Fi driver carried over.** The 23H2-era driver fails 24H2's stricter driver validation and will not bind to the adapter. Check the driver date in Device Manager — anything from before mid-2024 is suspect on 24H2.
- **Windows Update reinstalling the broken driver.** The fixed driver exists, but Windows Update keeps offering the old broken version. Compare the offered version against Lenovo's site; Windows Update is often behind.
- **Lenovo Vantage vs Windows Update conflict.** Two updaters installing different Wi-Fi driver versions leaves the adapter conflicted. Set Vantage driver updates to manual while diagnosing to stop the version tug-of-war.
- **Power management regression.** 24H2 can re-enable aggressive adapter power saving that drops the connection. The Power Management tab setting reverts on some driver updates; recheck it after each install.
- **Corrupted network stack.** The upgrade damages Winsock or the TCP/IP stack configuration. netsh int ip reset and netsh winsock reset rebuild these from defaults.
- **Airplane mode stuck on.** The feature update can leave the radio soft-blocked with no visible indicator. The Settings toggle and the Fn key can disagree; check both.
- **Fast Startup driver handoff bug.** The hybrid shutdown state confuses the Wi-Fi driver on the next boot. Uncheck fast startup in Power Options to test this theory in one reboot.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check airplane mode and the radio switch

Rule out the trivial causes first — 24H2 is known to leave radios soft-blocked after upgrading. Identify your exact adapter first in Device Manager under Network adapters — Intel AX201, AX211, Realtek 8852, and MediaTek MT7922 each have different fixed driver versions.

1. Press the Fn + F8 (or your model's wireless key) to toggle the radio.
2. Open Settings > Network & internet and confirm Airplane mode is off.
3. Click the Wi-Fi toggle off and back on.
4. If networks appear, you are done — the radio was simply blocked.
5. On ThinkPads, also check the BIOS Security > I/O Port Access settings for the wireless radio.
6. Confirm the adapter now appears in Device Manager without any warning icon.

### Fix 2: Run the network troubleshooter

The built-in network troubleshooter resets the common stack pieces automatically. Lenovo's support site lists drivers per machine-type-model (MTM), so enter your serial number rather than guessing the model family.

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Run the 'Network and Internet' troubleshooter.
3. Apply all recommended fixes and restart.
4. Test the connection before moving on.
5. If it reports the adapter has a driver problem, continue to the driver steps.
6. Connect to your network and run a sustained test: stream video for ten minutes to prove stability, not just association.

### Fix 3: Reset the network stack

When the driver is fine but nothing connects, the stack itself is usually corrupt. [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-after-windows-11-update/) The 24H2 network changes are documented in Microsoft's release health notes; checking them tells you whether your symptom is a known issue with a scheduled fix.

1. Open Command Prompt as administrator.
2. Run these in order: netsh winsock reset, then netsh int ip reset.
3. Then run: ipconfig /release, ipconfig /renew, ipconfig /flushdns.
4. Restart the laptop.
5. This rebuilds Winsock and TCP/IP from defaults without touching your files.
6. Check the driver version on the Driver tab and confirm it matches the fixed version you intended to install.

### Fix 4: Install Lenovo's 24H2 Wi-Fi driver

This is the fix that resolves most cases: Lenovo's updated driver built for 24H2. If the adapter shows a yellow warning with code 10 or 43, the driver failed to start — a driver problem, not a router problem.

1. Go to [Lenovo's support site](https://support.lenovo.com/us/en/) and enter your exact model or serial number.
2. Download the Wi-Fi driver listed for Windows 11 24H2 (Intel, Realtek, or MediaTek — match your adapter).
3. In Device Manager, right-click the Wi-Fi adapter and choose Uninstall device, ticking 'delete the driver software'.
4. Install the downloaded Lenovo driver and restart.
5. Verify in Device Manager that the new driver version is active.
6. Restart twice and confirm Wi-Fi connects automatically both times, ruling out a Fast Startup resume flakiness.

### Fix 5: Stop Windows Update from downgrading the driver

Windows Update sometimes replaces Lenovo's fixed driver with the older broken one. Test with your phone's hotspot to separate laptop-side breakage from router-side quirks before spending an hour on drivers.

1. After installing Lenovo's driver, open Device Manager > Wi-Fi adapter > Properties > Driver and note the version.
2. Go to Settings > Windows Update > Advanced options > Optional updates and uncheck any Wi-Fi driver offered there.
3. Consider the 'Show or hide updates' troubleshooter to block the bad driver version.
4. In Lenovo Vantage, set driver updates to manual so it does not fight you either.
5. Recheck the driver version after the next Patch Tuesday.
6. Test sleep/wake cycles specifically, since 24H2 power-management regressions often strike on resume.

### Fix 6: Disable adapter power saving

24H2's power management can put the adapter to sleep and never wake it properly. Lenovo Vantage has a Wi-Fi security and driver section that sometimes offers a different driver version than the support website.

1. Open Device Manager, right-click the Wi-Fi adapter, and open Properties.
2. On the Power Management tab, uncheck 'Allow the computer to turn off this device to save power'.
3. On the Advanced tab, set power-saving or sleep-related properties to Maximum Performance.
4. In Settings > System > Power & battery, set the power mode to Best performance while testing.
5. Restart and confirm the connection stays stable.
6. Run Windows Update afterward and decline any Wi-Fi driver it offers that is older than your working version.

### Fix 7: Disable Fast Startup

The hybrid shutdown state can hand the Wi-Fi driver a confused device on boot. Note the driver version before and after each change (Device Manager > Driver tab) so you can tell whether an update actually replaced it.

1. Open Control Panel > Power Options > 'Choose what the power buttons do'.
2. Click 'Change settings that are currently unavailable'.
3. Uncheck 'Turn on fast startup' and save changes.
4. Shut down fully (not restart), then power on.
5. Test Wi-Fi across several cold boots.
6. If you use a VPN, reconnect it and confirm the tunnel works over the repaired Wi-Fi.

## Closing

Wi-Fi breaking the moment 24H2 lands is a driver mismatch, full stop — and driver mismatches are fixable without touching your data. Lenovo's 24H2-specific driver resolves most cases; the stack reset and power-management fixes cover the rest. If a different symptom appeared after your update, [Wi-Fi 6 issues in Windows 11 24H2](/articles/how-to-fix-wifi-6-not-working-on-laptop-in-windows-11-24h2/) may match it better.
