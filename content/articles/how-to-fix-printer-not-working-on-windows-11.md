---
title: "Printer Not Working on Windows 11? How to Fix It"
slug: how-to-fix-printer-not-working-on-windows-11
date: 2026-09-01
categories: ["drivers"]
tags: ["printer not working windows 11", "printer offline fix", "can't print windows 11", "printer driver windows 11", "print spooler fix"]
description: "Printer not responding, stuck offline, or print jobs vanishing on Windows 11? Fix it with spooler resets, driver reinstalls, and connection checks."
thumbnail: "/images/thumbs/how-to-fix-printer-not-working-on-windows-11.webp"
faqs:
  - q: "Why does my printer show as offline in Windows 11 when it's on?"
    a: "The 'offline' status usually means Windows lost communication with the printer, not that the printer is off. Check that the printer is on the same WiFi network as the laptop — printers often hop to a different band or lose WiFi while appearing connected. Then open Settings > Bluetooth & devices > Printers & scanners, select the printer, and turn off 'Use printer offline' if it's enabled. Restarting the print spooler service also clears stale offline states."
  - q: "How do I restart the print spooler in Windows 11?"
    a: "Press Win + R, type services.msc, and press Enter. Find Print Spooler in the list, right-click it, and choose Restart. If print jobs are stuck, stop the spooler first, delete the files in C:\\Windows\\System32\\spool\\PRINTERS, then start it again — this clears the jammed queue completely. The spooler is the background service managing all print jobs, and restarting it resolves a huge share of mysterious printer failures."
  - q: "Should I use the manufacturer's driver or the Windows built-in one?"
    a: "For full functionality — scanning, ink levels, advanced paper handling — install the manufacturer's driver package from their support site. Windows 11's built-in IPP-based drivers handle basic printing well and are more reliable for simple print-only needs, especially over the network. If the manufacturer's full suite is causing problems, try removing it and letting Windows use its inbox IPP driver as a diagnostic step."
  - q: "Why do my print jobs disappear without printing?"
    a: "Jobs that vanish usually hit a crashed print spooler or a driver rendering failure. Restart the spooler and clear the queue as described above, then try printing a Windows test page (printer properties > Print Test Page). If the test page works but your document doesn't, the problem is in the application's print path — try printing to PDF first to confirm the app can render, then try a different application."
---

Printer problems on Windows 11 cluster into a few recognizable patterns: the printer shows offline, print jobs pile up and never print, jobs vanish silently, or the printer isn't found at all. Each pattern points at a different layer — connectivity, the print spooler, or the driver — and this guide is organized to match symptom to layer so you're not reinstalling drivers for a WiFi problem.

Note whether your printer connects via WiFi, USB, or Ethernet, since the first checks differ. The spooler and driver fixes apply to all connection types.

Windows 11 changed the printing landscape in one important way: it strongly prefers IPP (Internet Printing Protocol) with driverless or inbox drivers, and it is more aggressive than Windows 10 about replacing manufacturer driver suites. That is good for reliability — the inbox IPP path is simpler and breaks less — but it means manufacturer utilities for ink levels and maintenance may stop working after updates even while basic printing is fine. When diagnosing, separate "can it print a test page" (core function, usually fixable) from "do the manufacturer's extras work" (often a casualty of driver modernization, and rarely worth fighting). Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the built-in printer troubleshooting flow as a complement to this guide.

## Why this happens

- **Printer and laptop on different networks** — the printer hopped WiFi bands or joined a guest network.
- **Print spooler crashed or jammed** with a stuck job blocking the queue.
- **Corrupted printer driver**, especially after Windows 11 feature updates.
- **"Use printer offline" mode** accidentally enabled.
- **IPP vs. manufacturer driver conflicts** after switching driver types.
- **Firewall blocking** printer discovery and communication ports.
- **USB port or cable issues** for directly connected printers.
- **Printer firmware needing an update** for Windows 11 compatibility.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the connection layer first

Match the check to your connection type.

1. **WiFi printers:** confirm the printer and laptop are on the same network and band. Print a network configuration page from the printer's panel to see its IP address, then ping it from the laptop.
2. **USB printers:** try a different USB port and cable. Check Device Manager for the printer entry — a missing entry means the USB layer isn't enumerating it.
3. **Ethernet printers:** check the link lights on the printer's port and confirm the IP is in the same subnet as the laptop.
4. Power-cycle the printer (unplug 30 seconds) — printers' network stacks lock up like any embedded device.

### Fix 2: Clear "offline" status and restart the spooler

The highest-yield Windows-side fix.

1. Go to **Settings > Bluetooth & devices > Printers & scanners**, select your printer, and make sure **Use printer offline** is not enabled.
2. Press **Win + R**, type `services.msc`, find **Print Spooler**, right-click > **Restart**.
3. If jobs are stuck: stop the spooler, delete everything in `C:\Windows\System32\spool\PRINTERS`, start the spooler again.
4. Send a test print. A cleared queue plus fresh spooler resolves most "nothing prints" cases.

### Fix 3: Run the printer troubleshooter

Quick automated pass.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters** and run the **Printer** troubleshooter.
2. Apply its recommendations — it commonly fixes spooler states and port configurations.
3. Restart the laptop afterward regardless of what it reports.

### Fix 4: Remove and re-add the printer

Clears corrupted printer configurations and port assignments.

1. In **Printers & scanners**, select the printer and click **Remove**.
2. Restart the laptop (clears cached driver associations).
3. Click **Add device** and let Windows rediscover it. For network printers, use **Manually add** > **Add a printer using IP address** with the IP from the printer's network page if auto-discovery fails.
4. Print a test page immediately to confirm the fresh configuration works.

### Fix 5: Reinstall the printer driver properly

When re-adding isn't enough, the driver itself is corrupt.

1. Remove the printer (Fix 4), then open **Print Management** (search for it in Start) or **Settings > Printers > Print server properties > Drivers tab**.
2. Remove the old driver package completely.
3. Download the latest driver from the manufacturer's support site (HP, Canon, Epson, Brother) for Windows 11 — or let Windows install its IPP inbox driver for a minimal, reliable setup.
4. Re-add the printer and test. If the manufacturer's suite causes trouble, the inbox IPP driver is a solid fallback for basic printing.

### Fix 6: Check firewall and network discovery

For printers found intermittently or not at all.

1. Go to **Settings > Network & internet** and confirm your network profile is **Private**, not Public — Public blocks printer discovery.
2. In **Windows Security > Firewall**, ensure **File and Printer Sharing** is allowed for the Private profile.
3. Temporarily disable third-party firewalls to test — they frequently block the ports printers use.
4. On the printer, ensure protocols like **mDNS/Bonjour** and **WS-Discovery** are enabled if the options exist.

### Fix 7: Update printer firmware

The last resort for compatibility issues.

1. Check the manufacturer's support site for firmware updates for your exact printer model.
2. Apply via the printer's embedded web server (browse to its IP address) or USB, following the manufacturer's instructions.
3. Firmware updates fix Windows 11 protocol compatibility and network stack bugs that no driver change can address.

For HP-specific printer issues, see [how to fix printers on HP laptops](/articles/how-to-fix-printer-not-working-on-windows-11-on-hp-laptop/).

## Closing

Printer troubleshooting is layer isolation: connection, spooler, driver, in that order. The spooler restart plus queue clear is the single most effective Windows-side action — it looks too simple for the number of cases it fixes. When in doubt, the remove-and-re-add with a fresh driver beats hours of tweaking a corrupted configuration. And if the printer works but your laptop's own USB ports are flaky, our [USB port guide](/articles/how-to-fix-usb-ports-not-working-on-hp-laptop/) addresses the connection layer from the laptop side. One last habit: after any Windows 11 feature update, print a test page before you actually need the printer — updates are the most common trigger for spooler and driver regressions, and discovering the problem during a calm test beats discovering it five minutes before a deadline.
