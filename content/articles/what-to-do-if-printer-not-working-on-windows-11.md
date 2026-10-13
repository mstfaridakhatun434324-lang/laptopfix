---
title: "What to Do If Your Printer Is Not Working on Windows 11"
slug: what-to-do-if-printer-not-working-on-windows-11
date: 2026-09-09
categories: ["drivers"]
tags: ["printer not working", "windows 11", "printer troubleshooting", "print spooler", "printer driver"]
description: "Printer not working on Windows 11? This guide covers offline printers, stuck print queues, spooler errors, and driver problems with eight ordered fixes that actually work."
thumbnail: "/images/thumbs/what-to-do-if-printer-not-working-on-windows-11.webp"
faqs:
  - q: "Why does my printer always show offline on Windows 11?"
    a: "The most common reason is that your router gave the printer a new IP address via DHCP while Windows still points the printer port at the old address. Update the port IP in Printer properties, then reserve a static IP for the printer in the router so it cannot happen again. Less common causes include the printer being in deep sleep, the 'Use Printer Offline' option being ticked, or a firewall blocking communication."
  - q: "How do I clear a print job that is stuck and will not delete?"
    a: "Stop the Print Spooler service in services.msc, delete all files in C:\\Windows\\System32\\spool\\PRINTERS, then start the spooler again. This removes the corrupted job files directly, which the normal 'Cancel' button cannot always do. If jobs immediately get stuck again, the printer driver is likely corrupt and needs a clean reinstall."
  - q: "Should I use the Windows built-in driver or the manufacturer's driver?"
    a: "Use the manufacturer's Windows 11 driver package. Windows' built-in class drivers cover basic printing but often lack duplex, tray selection, ink-level reporting, and scanning integration. The exception is very old printers whose makers never released Windows 11 drivers — there, the built-in driver or a universal PCL/PostScript driver is the only option, with reduced features."
  - q: "Why did my printer stop working after upgrading to Windows 10 to 11?"
    a: "Windows 11 enforces stricter driver signing and deprecated parts of the legacy v3 print driver model, so older drivers that worked on Windows 10 can fail silently or crash the spooler. The fix is a clean install of the manufacturer's current Windows 11 driver. If the maker offers no Windows 11 driver for an old model, try their universal driver or Windows' built-in IPP driver before replacing the printer."
---

A printer that refuses to work on Windows 11 usually fails in one of a few familiar ways: it shows as offline even though it is on, jobs pile up in the queue and never print, the spooler service crashes, or Windows simply cannot find the printer on the network. USB printers, Wi-Fi printers, and shared network printers each have their own failure modes, but the diagnostic order is the same.

Windows 11 changed enough of the printing stack — stricter driver signing, the move away from legacy v3 drivers, and PrintNightmare-era security hardening — that printers which worked perfectly on Windows 10 can misbehave after an upgrade. Add a router that reassigned the printer's IP address, and you have the single most common cause of 'offline' network printers.

Start with the physical basics before touching software: power, cables, paper, and ink. Then work through the fixes below in order. If your printer connects over USB and Windows does not see it at all, our [USB device troubleshooting guide](/articles/how-to-fix-usb-device-not-recognized-after-windows-11-update/) pairs well with this one, and Lenovo owners have a [brand-specific printer guide](/articles/how-to-fix-printer-not-working-on-windows-11-on-lenovo-laptop/) for OEM driver quirks.

## Why this happens

- **Printer showing offline due to IP address change** — DHCP reassigned the printer's IP, but the Windows printer port still points at the old address — the number-one cause of 'offline' Wi-Fi printers.
- **Print spooler service crashed or stuck** — The spooler (spoolsv.exe) manages the queue; when it hangs, every job stalls and the printer appears broken.
- **Corrupted printer driver after Windows 11 upgrade** — Legacy v3 drivers and unsigned drivers that worked on Windows 10 are blocked or unstable on Windows 11.
- **Stuck or corrupted job blocking the queue** — A single malformed print job can jam the entire queue so nothing behind it prints.
- **USB connection or cable problem** — Failing USB cables, unpowered hubs, and USB selective-suspend power saving silently drop USB printers.
- **Firewall blocking network printer discovery** — Windows Firewall or third-party security software can block the ports printers use for discovery and job delivery.
- **Wrong default printer or paused printing** — Printing paused at the queue level, or jobs sent to a stale copy of the printer (e.g., 'Printer (Copy 1)'), never reach the hardware.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the printer troubleshooter

Windows 11's built-in printer troubleshooter clears stuck queues, restarts the spooler, and re-detects the printer. It is quick and fixes a surprising share of simple failures.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Click **Run** next to Printer and follow the prompts.
3. Apply any recommended fix, then send a test page.
4. If it finds nothing, continue — the troubleshooter misses driver and IP-port problems.

### Fix 2: Check the physical basics

Roughly a third of 'not working' printers are out of paper, out of ink, jammed, or in an error state nobody noticed. Two minutes here saves an hour of driver surgery.

1. Confirm the printer is powered on and shows no error lights or messages on its display.
2. Check paper, ink/toner levels, and clear any paper jam — open every access door, not just the obvious one.
3. For USB printers, plug directly into the PC (no hub) and try a different cable and port.
4. For Wi-Fi printers, confirm the printer is connected to the same network as the PC — print a network configuration page from the printer's menu.

### Fix 3: Restart the Print Spooler and clear the queue

A jammed spooler is the classic 'jobs stuck at 0%' failure. Restarting the service and clearing its cache resolves it.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find **Print Spooler**, right-click it, and choose **Stop**.
3. Open File Explorer and navigate to `C:\Windows\System32\spool\PRINTERS` — delete every file inside (these are the stuck jobs).
4. Back in Services, right-click Print Spooler and choose **Start**.
5. Send a fresh test page.

### Fix 4: Set the printer online and as default

Windows sometimes leaves a printer in offline or paused state after an error, and jobs sent to a duplicate printer entry go nowhere.

1. Open Settings > Bluetooth & devices > Printers & scanners.
2. Click your printer, then open the print queue.
3. In the queue window, open the Printer menu and uncheck **Use Printer Offline** and **Pause Printing** if either is ticked.
4. Back in Settings, click **Set as default**. Remove any duplicate '(Copy 1)' entries you do not use.

### Fix 5: Fix the printer port for network printers

If your Wi-Fi printer shows offline but prints its network page fine, the port IP is almost certainly stale. Updating it takes a minute.

1. On the printer's network configuration page, note its current IP address (e.g., 192.168.1.42).
2. In Settings > Printers & scanners, click your printer > Printer properties > **Ports** tab.
3. Select the existing Standard TCP/IP port and click **Configure Port**.
4. Replace the old IP with the current one from the printer's page and click OK.
5. To prevent recurrence, reserve a static IP for the printer in your router's DHCP settings.

### Fix 6: Reinstall the printer driver from the manufacturer

When the driver is the problem — spooler crashes, garbled output, or features missing — only a clean reinstall of the manufacturer's Windows 11 driver fixes it. Get it from the printer maker's official site; Microsoft's [printer support pages](https://support.microsoft.com/en-us/windows) explain the built-in options.

1. In Settings > Printers & scanners, select the printer and click **Remove**.
2. Open Device Manager, show hidden devices, and remove any lingering printer entries under Print queues.
3. Download the latest Windows 11 driver package from your printer manufacturer's official support site.
4. Run the installer with the printer connected (USB) or on the network (Wi-Fi) as the installer directs.
5. Print a test page and confirm all features (duplex, color) work.

### Fix 7: Temporarily test with the firewall off

If a network printer is discovered but jobs never arrive, the firewall may be blocking the print ports. This test isolates that in seconds.

1. Open Windows Security > Firewall & network protection.
2. Temporarily turn off the firewall for your active network profile.
3. Try printing. If it works, turn the firewall back on immediately.
4. Then add a proper exception: allow your printer's app through the firewall, or allow inbound TCP ports 9100 and 515 for the printer's IP only — never leave the firewall off.

## Closing

Printer problems on Windows 11 reward a calm, ordered approach: physical check, spooler reset, queue and default settings, port IP for network printers, and a clean driver reinstall as the heavy fix. The vast majority of cases resolve by Fix 5, and assigning the printer a static IP in your router prevents the most common recurrence — the mysterious 'offline' printer that worked yesterday.
