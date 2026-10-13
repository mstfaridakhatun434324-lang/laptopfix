---
title: "Fix a Printer That Won't Work on an ASUS Laptop in Windows 11"
slug: how-to-fix-printer-not-working-on-windows-11-on-asus-laptop
date: 2026-10-10
categories: ["drivers"]
tags: ["printer not working", "windows 11", "asus laptop", "print spooler", "printer driver"]
description: "Fix printer failures on an ASUS laptop in Windows 11: spooler resets, driver reinstallation, port checks, and network printer diagnosis."
thumbnail: "/images/thumbs/how-to-fix-printer-not-working-on-windows-11-on-asus-laptop.webp"
faqs:
  - q: "Why is my printer not working on Windows 11 after working before?"
    a: "Windows 11 updates frequently break printer drivers, corrupt the print spooler with a jammed job, or change the port assignment out from under the configured printer. The printer hardware is usually innocent — clearing the spooler queue and reinstalling the manufacturer's full driver package resolves the large majority of failures."
  - q: "What does restarting the print spooler fix?"
    a: "The spooler service manages the entire print queue, so one corrupted job wedges it and every job behind it fails. Stopping the Print Spooler service, deleting the stuck files in the spool PRINTERS folder, and restarting the service clears the jam and lets new jobs flow normally again."
  - q: "Should I use the Windows built-in driver or the manufacturer's?"
    a: "Always install the manufacturer's full driver package for complete functionality — scanning, ink-level monitoring, duplex control, and status feedback. Windows' built-in IPP class driver handles basic printing but drops advanced features and is a known source of intermittent failures on multifunction printers."
  - q: "Why does my network printer show offline when it is on?"
    a: "The printer's IP address almost certainly changed via DHCP, so Windows keeps sending jobs to the old, dead address while the printer sits ready on a new one. Assign the printer a static IP or a DHCP reservation in your router, then update the Standard TCP/IP port in printer properties to match."
---

A printer that stops working on an ASUS laptop running Windows 11 usually fails in one of three places: the print spooler jammed on a corrupted job, the driver broke during a Windows update, or the connection path (USB port or network address) changed underneath the configured printer. The printer itself is rarely the problem — prove it by printing a test page from the printer's own control panel. If that works, the fault is entirely in the laptop's software chain.

Printer troubleshooting rewards a strict order: spooler first, then driver, then port/connection. Jumping straight to driver reinstallation while a corrupted job is still jamming the spooler just produces a fresh driver with the same jam. Work the sequence below and note which step restores printing — that tells you the failure class if it recurs.

## Why this happens

- **Print spooler jammed by a corrupted job:** One bad print job wedges the spooler queue and every job behind it fails silently.
- **Printer driver broken by Windows update:** Feature updates replace or corrupt manufacturer drivers, especially for older printer models.
- **Printer IP address changed:** DHCP assigns the network printer a new address; the configured TCP/IP port still points at the old one, showing "offline."
- **Wrong port selected:** USB printers that move between ports, or printers shared through changing configurations, end up bound to a dead port.
- **Print Spooler service stopped or crashing:** The service can be disabled by updates or crash-loop on corrupted spool files.
- **Manufacturer software missing:** Status monitors, ink-level tools, and scan drivers that the full package installs get removed by updates.
- **USB power management cutting the printer:** Windows suspends the USB port the printer uses, breaking the connection mid-job.
- **Windows protected print mode conflicts:** Newer Windows 11 print protections can block older manufacturer drivers until updated.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the jammed spooler queue

1. Open **Services** (Win + R → `services.msc`), find **Print Spooler**, and click **Stop**.
2. Open File Explorer and delete everything in `C:\Windows\System32\spool\PRINTERS` (these are the stuck job files).
3. Back in Services, **Start** the Print Spooler.
4. Try printing again. A single corrupted job is the most common cause of "printer suddenly stopped," and this clears it in two minutes.

### Fix 2: Run the printer troubleshooter and check the default printer

1. Go to **Settings → System → Troubleshoot → Other troubleshooters → Printer → Run**.
2. Go to **Settings → Bluetooth & devices → Printers & scanners** and confirm your printer shows **Default** — Windows sometimes switches the default to a virtual printer (Fax, PDF) after updates.
3. Right-click your printer → **Set as default** if needed.
4. Send a test page: printer properties → **Print Test Page**. Related device-enumeration checks are covered in the [hidden devices guide](/articles/how-to-enable-hidden-devices-in-device-manager-in-windows-11-24h2/) if the printer appears duplicated.

### Fix 3: Reinstall the manufacturer's driver package

1. In **Settings → Bluetooth & devices → Printers & scanners**, select the printer → **Remove**.
2. Download the full driver package from the printer manufacturer's site (HP, Canon, Epson, Brother) for Windows 11 — not the basic driver Windows offers.
3. Disconnect the USB cable (for USB printers) before installing, per the manufacturer's instructions; reconnect only when the installer asks.
4. For network printers, let the installer discover the printer on the network rather than reusing the old port — this also fixes stale IP bindings.
5. Print a test page from the manufacturer's software to confirm full functionality.

### Fix 4: Fix the port for network printers

1. Open printer **Properties → Ports** tab.
2. If the port is a **Standard TCP/IP Port** with an IP address, verify it matches the printer's current IP (print a network config page from the printer's panel).
3. If the IP changed, either update the port to the new IP or — better — set a **DHCP reservation** for the printer in your router so it never changes again.
4. Consider switching to the printer's **hostname** instead of raw IP in the port configuration; hostnames survive DHCP changes.
5. Microsoft documents network printer setup in [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 5: Check USB connection and power management

1. Plug the printer directly into the laptop — not through a hub — and try a different USB port.
2. In **Device Manager → Universal Serial Bus controllers**, right-click each **USB Root Hub → Properties → Power Management** and uncheck **Allow the computer to turn off this device to save power**.
3. Try a different USB cable; printer cables fail more often than people expect.
4. If Device Manager shows the printer with a warning icon, uninstall it there and let Windows redetect it on reconnection.

### Fix 6: Remove ghost printer entries and stale drivers

1. Open **Print Management** (Win + R → `printmanagement.msc`).
2. Under **Custom Filters → All Drivers**, remove driver packages for printers you no longer own.
3. Under **Printers**, delete grayed or duplicate entries for your printer.
4. Reinstall cleanly using Fix 3. Duplicate and ghost printer objects are a classic cause of jobs vanishing into the wrong queue.

### Fix 7: Check Windows protected print mode and firmware

1. Go to **Settings → Bluetooth & devices → Printers & scanners** and check for any **Windows protected print mode** toggle — if your manufacturer driver is blocked, try toggling it off temporarily to test.
2. Update the printer's own firmware from the manufacturer's site; old firmware plus new Windows 11 print stack is a known conflict source.
3. As a final isolation test, print from another device (phone via the manufacturer's app). If that works, the printer and network are fine and the fault is isolated to the ASUS laptop's print stack — repeat Fixes 1–3 carefully.

## Closing

Printer failures on Windows 11 are spooler, driver, or port problems — in that order of likelihood. The same spooler-first discipline applies across brands — for the Lenovo-specific take on this pipeline, see the [Lenovo printer troubleshooting guide](/articles/how-to-fix-printer-not-working-on-windows-11-on-lenovo-laptop/). Clear the spooler queue, reinstall the manufacturer's full driver package, and verify the port points at the printer's real current address. The printer's own test page is your ground truth: if the printer can print by itself, the laptop's software chain is the only thing left to fix, and the steps above rebuild it completely.
