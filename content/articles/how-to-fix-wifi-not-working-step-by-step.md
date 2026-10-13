---
title: "WiFi Not Working on a Windows Laptop: Step-by-Step Fix Guide"
slug: how-to-fix-wifi-not-working-step-by-step
date: 2026-09-08
categories: ["drivers"]
tags: ["wifi not working", "wireless adapter", "no internet", "windows 11", "step by step"]
description: "WiFi dead on your Windows laptop? Follow this ordered, step-by-step guide to diagnose and fix wireless problems from quick toggles to full driver reinstalls."
thumbnail: "/images/thumbs/how-to-fix-wifi-not-working-step-by-step.webp"
faqs:
  - q: "Why does my laptop say no WiFi networks found when my phone connects fine?"
    a: "When only the laptop fails, the fault is local to the laptop: a disabled adapter, corrupted wireless driver, wrong band selection, or a misconfigured network stack. The router is almost certainly fine since your phone connects. Work through adapter checks and driver fixes before touching the router."
  - q: "Should I restart my router or my laptop first?"
    a: "Restart the laptop first, because most WiFi failures are driver or stack issues on the laptop side. If the laptop still fails after a clean reboot and your phone also cannot connect, then restart the router. Fixing in this order avoids chasing a router problem that does not exist."
  - q: "How do I know if my WiFi adapter is broken hardware?"
    a: "Hardware failure is likely when the adapter is missing from Device Manager even with hidden devices shown, missing from BIOS, and a USB WiFi dongle works perfectly on the same machine. If the adapter appears in Device Manager with a driver loaded, the hardware is almost always fine and software fixes will work."
  - q: "Will resetting network settings delete my files?"
    a: "No. A network reset only removes saved WiFi passwords, VPN profiles, and custom network configurations. Your documents, photos, apps, and Windows settings stay untouched. You will need to re-enter WiFi passwords afterward, so keep them handy somewhere safe before you reset."
---

WiFi failures are maddening because the symptom is identical whether the cause is trivial or serious: no networks, no internet, a globe icon in the taskbar. The trick is to work a strict order — quick checks first, then the network stack, then drivers, and only then suspect hardware. Skipping around wastes time and can make things worse.

This guide is written as a sequence. Do each step fully before moving on. Most people never get past step four. By the time you reach step seven, you will know with certainty whether the problem is software you can fix or hardware you need to replace.

## Why this happens

- **Wireless adapter disabled:** A keyboard shortcut (Fn + a function key) or Windows setting disabled the radio. The icon looks dead but the hardware is fine.
- **Corrupted wireless driver after a Windows update:** The most common cause overall — an update replaces or breaks the WiFi driver, and networks vanish.
- **TCP/IP stack corruption:** The networking subsystem itself is damaged, so the adapter exists but cannot obtain or hold an IP address.
- **Airplane mode stuck on:** Windows believes the radio is off even when you toggle the switch. The setting and the hardware disagree.
- **Wrong WiFi band or channel:** Some older adapters cannot see 5 GHz networks; crowded channels can make networks appear and disappear.
- **Router-side issues:** DHCP exhaustion, MAC filtering, or a hung router process can block one specific device while others work.
- **Power management turning off the adapter:** Windows powers down the wireless card to save battery, and it fails to wake back up.
- **Dead wireless card:** The physical WiFi module fails, especially after drops, spills, or antenna wire damage during disassembly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the physical and software wireless switches

1. Look for a **Fn key combination** (often Fn + F2, F3, or a key with a wireless icon) and press it. Many laptops toggle WiFi this way with no on-screen confirmation.
2. Check for a physical WiFi switch on the laptop's side or front edge — some business laptops still have them.
3. Open **Settings → Network & internet → WiFi** and confirm WiFi is **On**. Also confirm **Airplane mode** is **Off** on the same page.
4. If networks appear now, you were one keypress away from a fix. If you see an [airplane mode stuck-on situation](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/), that needs its own treatment.

### Fix 2: Run the built-in network troubleshooter

1. Go to **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run **Network and Internet**. Let it complete — it resets adapters, flushes DNS, and re-registers the network stack automatically.
3. Restart the laptop when it finishes, even if it claims nothing was wrong. The restart finalizes the repairs it made.

### Fix 3: Reset the TCP/IP stack and flush DNS manually

1. Open **Terminal as Administrator** (right-click Start → Terminal (Admin)).
2. Run these commands one at a time, pressing Enter after each: `netsh winsock reset`, `netsh int ip reset`, `ipconfig /release`, `ipconfig /renew`, `ipconfig /flushdns`.
3. Restart the laptop. This rebuilds the networking subsystem from scratch and fixes the large class of problems where the adapter is present but cannot get online.

### Fix 4: Reinstall the wireless adapter driver

1. Open **Device Manager** → expand **Network adapters**.
2. Right-click your wireless adapter (Intel, Realtek, MediaTek, or Qualcomm) → **Uninstall device**. Check "attempt to remove the driver" if offered.
3. Restart. Windows will reinstall a driver automatically.
4. If Windows installs a broken or generic driver, download the correct one from your laptop maker's support page or the [Intel driver detection tool](https://www.intel.com/content/www/us/en/support/detect.html) and install it manually — the same approach that resolves [missing network adapters](/articles/how-to-fix-network-adapter-missing-after-windows-11-update/).

### Fix 5: Disable power management on the wireless adapter

1. In Device Manager, right-click the wireless adapter → **Properties → Power Management** tab.
2. Uncheck **"Allow the computer to turn off this device to save power."**
3. Go to **Control Panel → Power Options → Change advanced power settings → Wireless Adapter Settings → Power Saving Mode** and set it to **Maximum Performance** on both battery and plugged in.
4. Test after a sleep/wake cycle, since this fix specifically targets adapters that die on resume.

### Fix 6: Forget the network and check the 5 GHz band

1. Go to **Settings → Network & internet → WiFi → Manage known networks**, select your network, and click **Forget**.
2. Reconnect by entering the password fresh. Corrupted saved profiles cause silent connection failures.
3. If your network has separate 2.4 GHz and 5 GHz names, try each one. If the adapter cannot see 5 GHz at all, see this guide for [laptops not connecting to WiFi 5GHz](/articles/how-to-fix-laptop-not-connecting-to-wifi-5ghz-in-windows-11-24h2/).
4. As a last router-side check, restart the router and confirm DHCP is enabled with enough addresses for your devices.

### Fix 7: Use the network reset and test with a USB adapter

1. Go to **Settings → Network & internet → Advanced network settings → Network reset** and click **Reset now**. Restart when prompted.
2. If WiFi still fails, plug in a cheap USB WiFi dongle. If the dongle works, your internal wireless card is a hardware failure — replacement modules cost little, but check warranty first via the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) documentation on hardware diagnostics.
3. If even the dongle fails, the problem is deep in Windows itself, and an in-place upgrade or clean reinstall is the honest next step.

### Fix 8: Isolate router vs laptop with a phone hotspot

1. Enable the **mobile hotspot** on your phone and try connecting the laptop to it.
2. If the laptop connects to the hotspot fine, the laptop's WiFi is healthy and the problem is specific to your router — focus on router settings, not the laptop.
3. If the laptop can't connect to the hotspot either, the problem is definitely on the laptop — return to the driver fixes above.
4. Also check the router for **MAC address filtering**: log into the admin page and make sure your laptop's MAC isn't blocked. Delete and re-add the laptop's entry if filtering is on — stale filter entries silently block previously-working devices.

## Closing

Step-by-step discipline beats guessing. The vast majority of WiFi failures end at Fix 3 or Fix 4 — a corrupted stack or a bad driver. Work the list in order, and you will either fix it or know exactly which part failed.
