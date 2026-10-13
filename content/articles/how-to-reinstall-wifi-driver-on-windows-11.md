---
title: "How to Reinstall the WiFi Driver on Windows 11 (Clean Method)"
slug: how-to-reinstall-wifi-driver-on-windows-11
date: "2026-09-01"
categories: ["drivers"]
tags: ["wifi driver reinstall", "wireless adapter", "windows 11", "network driver", "wifi fix"]
description: "Learn how to properly reinstall the WiFi driver on Windows 11 — from a quick Device Manager reinstall to a full clean install of the manufacturer's driver."
thumbnail: "/images/thumbs/how-to-reinstall-wifi-driver-on-windows-11.webp"
faqs:
- q: "Will reinstalling my WiFi driver delete my saved networks?"
  a: "A standard driver reinstall does not delete saved WiFi networks or passwords — those live in Windows' network profiles, not the driver. However, the deeper network reset described in this guide does remove saved networks, so note your passwords first if you go that far. For the basic reinstall steps, your networks and passwords remain untouched."
- q: "How do I download a WiFi driver with no internet access?"
  a: "Use another device — a phone, tablet, or second computer — to visit your laptop manufacturer's support page, download the WiFi driver for your exact model, and transfer it via USB drive. Phone USB tethering is another option: connect your phone with a cable, enable USB tethering, and the laptop gets internet through the phone to download the driver directly."
- q: "Should I let Windows install the WiFi driver automatically?"
  a: "Windows' automatic driver is fine as a temporary measure to get back online, but for a lasting fix install the manufacturer's driver package. Vendor drivers include proper power management, the correct regulatory settings for your region, and companion utilities. The automatic driver is a good fallback while you download the real one, not the final destination."
- q: "How often should I update my WiFi driver?"
  a: "Only when you have a problem or the manufacturer releases a version fixing a known issue — WiFi drivers are not like security patches that need constant updating. If your wireless is stable, leave the driver alone. Updating a working driver introduces risk with little benefit, which is why this guide focuses on reinstalling to fix problems rather than routine updating."
---

Reinstalling a WiFi driver sounds like a single action, but there is a quick way and a right way — and the difference matters. The quick way (uninstall in Device Manager, reboot, let Windows handle it) fixes simple corruption in two minutes. The right way (download the manufacturer's package first, fully remove the old driver, install clean) fixes the stubborn cases the quick way leaves behind: adapters that vanish, connections that drop every few minutes, and speeds that never recover.

Most WiFi problems that survive a router reboot are driver problems. Windows 11 updates replace wireless drivers aggressively, vendor utilities conflict with new builds, and interrupted updates leave half-installed drivers that misbehave in subtle ways. A proper reinstall cuts through all of it by giving Windows a known-good driver to bind to the hardware.

This guide covers the full progression: the fast reinstall, the clean manufacturer reinstall, and the follow-up steps for when the new driver misbehaves. Read the "download first" warning in Fix 2 before you uninstall anything — it will save you from the classic trap of removing your only path to the internet.

## Why this happens

- **Windows Update replaced a working driver**: Newer is not always better; updated wireless drivers regularly introduce drops and disconnects.
- **Corrupted driver files**: Interrupted updates or disk errors damage driver files, causing erratic behavior rather than clean failure.
- **Vendor utility conflicts**: Manufacturer WiFi tools fight Windows 11's native wireless management for control of the adapter.
- **Power management bugs**: Driver-level power saving puts the card to sleep and fails to wake it, looking like a dead adapter.
- **Wrong driver for the card revision**: Similar model numbers ship different wireless chips; a mismatched driver half-works.
- **Leftover settings from the old driver**: Uninstalling without removing driver software leaves stale configuration behind.
- **Hardware actually failing**: Worth ruling out last — a dying card mimics driver issues until tested.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: The quick reinstall via Device Manager

For straightforward corruption — WiFi was fine, then an update or crash broke it — the quick reinstall is enough. Uninstalling the adapter forces Windows to redetect the hardware on reboot and rebuild the driver binding from its driver store. No download needed, two minutes total, and it resolves the simple cases outright.

1. Press Win + X and open Device Manager.
2. Expand "Network adapters," right-click your WiFi adapter, and choose "Uninstall device."
3. Do NOT tick "Attempt to remove the driver" for this quick version — keep the driver files.
4. Restart the laptop (a full restart, not just sleep/wake).
5. After reboot, Windows redetects the adapter and reinstalls the driver — test your connection.

### Fix 2: Download the manufacturer's driver BEFORE uninstalling

This is the step people skip, then regret. If the clean reinstall goes wrong — or if Windows has no driver to fall back on — you need the manufacturer's package ready on disk, because a laptop with no WiFi driver has no WiFi to download it with. Download first, on a working connection, and you are immune to that trap.

1. Find your exact laptop model (sticker on the bottom or System Information).
2. On your manufacturer's support page, locate the Wireless or WiFi driver for Windows 11.
3. Download it to a folder you can find easily, like Downloads or the Desktop.
4. If you have no working connection on the laptop, use a phone or second computer and a USB drive.
5. Confirm the file downloaded completely before touching Device Manager.

### Fix 3: Perform a clean driver install

The clean install removes every trace of the old driver — files, settings, and registry entries — before installing the manufacturer's package onto pristine ground. This is the fix for adapters that appear as [unknown devices](/articles/how-to-fix-unknown-device-in-device-manager/), drivers that reinstall but misbehave identically, and version conflicts between vendor and Microsoft drivers.

1. In Device Manager, right-click the WiFi adapter and choose "Uninstall device."
2. This time TICK "Attempt to remove the driver for this device," then confirm.
3. If the adapter vanishes entirely, click Action, "Scan for hardware changes."
4. Run the manufacturer's installer you downloaded in Fix 2 and restart when prompted.
5. Reconnect to your WiFi network and verify speed and stability over several minutes. [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can supply the correct package automatically for Intel wireless cards.

### Fix 4: Roll back when the new driver is worse

Sometimes the "latest" driver is the problem — you updated hoping for a fix and got new symptoms instead. Windows keeps the previous driver version around specifically for this situation, and rollback restores it in under a minute. Use this whenever trouble started right after a driver update.

1. In Device Manager, right-click the WiFi adapter and choose Properties.
2. Open the Driver tab and click "Roll Back Driver" if the button is active.
3. Pick a reason, confirm, and restart.
4. Test thoroughly — the old driver's stability is the point, not its age.
5. If rollback is grayed out, manually install the older version from the manufacturer's archive.

### Fix 5: Reset the network stack after reinstalling

A fresh driver on top of a corrupted network stack still misbehaves — stuck "identifying," APIPA addresses, or connections that establish but pass no traffic. The stack reset commands rebuild TCP/IP and Winsock to factory state, giving the new driver clean plumbing to work with. Run these after any driver reinstall that did not fully fix things.

1. Open Terminal as administrator (Win + X, Terminal (Admin)).
2. Run `netsh winsock reset` and press Enter.
3. Run `netsh int ip reset` and press Enter.
4. Restart the laptop.
5. Reconnect to WiFi and confirm you receive a proper IP address.

### Fix 6: Stop Windows Update from replacing your driver

Reinstalling is pointless if Windows Update swaps your working manufacturer driver for its own version next Tuesday. This is the most common reason WiFi "breaks again" weeks after a successful fix. Blocking driver delivery through Windows Update — while keeping security updates flowing — makes your repair permanent.

1. Open Settings, Windows Update, Advanced options.
2. Look for driver-update options and disable driver inclusion where available.
3. For a durable block, use Group Policy (gpedit.msc): Computer Configuration, Administrative Templates, Windows Components, Windows Update, Manage updates offered from Windows Update — enable "Do not include drivers with Windows Updates."
4. Get future driver updates from the manufacturer instead. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document these update controls.
5. Recheck after each feature update, which can reset the policy.

### Fix 7: Rule out hardware failure

If no driver — old, new, manufacturer, or Microsoft — makes the adapter work, and it is absent even with hidden devices shown, suspect the card. Confirm with a Linux live USB: no wireless card visible there either means hardware. Most laptop WiFi cards are replaceable M.2 modules, and a USB WiFi adapter is a five-minute workaround that doubles as a permanent fix.

1. Boot a Linux live USB and check for wireless interfaces.
2. If Linux sees the card but Windows does not, the fault is Windows-side — consider a Windows reset.
3. If neither sees it, reseat the M.2 card (one screw, two antenna wires) if comfortable opening the laptop.
4. Alternatively, plug in a USB WiFi adapter and install its driver.
5. If the USB adapter works perfectly, the internal card is dead — replace it or keep using USB.

If your adapter is missing rather than misbehaving, start with the [WiFi adapter not showing up guide](/articles/wifi-adapter-not-showing-up-troubleshooting/) instead. On Windows 10 rather than 11, the companion [Windows 10 WiFi driver reinstall](/articles/how-to-reinstall-wifi-driver-on-windows-10/) covers the same process with that OS's interface differences.

## Closing

WiFi driver problems reward method over haste: download the manufacturer's package before you uninstall anything, remove the old driver completely, install clean, and then stop Windows Update from undoing your work. The quick Device Manager reinstall handles simple corruption; the full clean install handles everything else. Either way, the fix is software — the card itself is guilty last, not first.
