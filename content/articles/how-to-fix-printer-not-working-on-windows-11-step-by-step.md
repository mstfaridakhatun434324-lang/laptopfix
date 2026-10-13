---
title: "Printer Not Working on Windows 11: Step-by-Step Repair"
slug: how-to-fix-printer-not-working-on-windows-11-step-by-step
date: 2026-09-14
categories: ["drivers"]
tags: ["printer not working", "windows 11 printer fix", "print spooler repair"]
description: "Printer not working on Windows 11? Follow this step-by-step repair — spooler resets, driver reinstalls, offline fixes, and network printer setup."
thumbnail: "/images/thumbs/how-to-fix-printer-not-working-on-windows-11-step-by-step.webp"
faqs:
  - q: "What should I check first when my printer stops working?"
    a: "Check the print queue for stuck jobs, confirm the correct default printer is set, and make sure the printer is not paused or offline in Windows. These three checks take two minutes and resolve a large share of printer failures before any driver work is needed."
  - q: "Why does my printer keep showing as offline?"
    a: "Offline status means Windows lost communication with the printer. For network printers the usual cause is a changed IP address; for USB printers it is often a power-saving port or bad cable. Unchecking Use Printer Offline and re-adding the printer with its current address fixes most cases."
  - q: "Do I need the manufacturer's software or just the driver?"
    a: "The driver is what makes printing work; the manufacturer's software adds scanning utilities, ink monitoring, and maintenance tools. For troubleshooting, install the full driver package — it includes both. You can skip the extra utilities later if you prefer a minimal setup."
  - q: "Can Windows Update break my printer?"
    a: "Yes. Windows Update sometimes replaces a working manufacturer driver with a generic one that loses features or breaks entirely. If printing died right after an update, reinstall the manufacturer's driver and consider hiding that specific driver update. You can also use the show/hide updates troubleshooter to block just that one driver update while allowing everything else through."
---

Printers fail in ways that all look identical from the user's chair: you hit Print, nothing happens, and the queue fills with jobs going nowhere. But underneath, "printer not working" splits into distinct problems — a jammed spooler, the wrong default printer, an offline flag, a broken driver, or a lost network connection — each with its own fix. Guessing wastes time; diagnosing in order does not.

This step-by-step guide walks the full printer repair path on Windows 11, from the two-minute checks through complete driver reinstallation and network-printer surgery. Follow it top to bottom and test after each fix.

## Why this happens

- **Jammed print spooler:** A corrupted job blocks the queue indefinitely.
- **Wrong default printer:** Jobs route to a virtual printer instead of the physical device.
- **Printer flagged offline or paused:** Windows-side flags stop all output while the printer sits ready.
- **Broken or replaced driver:** Updates swap the manufacturer driver for a generic one that fails.
- **Network printer IP changed:** DHCP gives the printer a new address; Windows keeps printing to the old one.
- **USB power saving:** Selective suspend drops the USB printer connection mid-job or between jobs.
- **Firewall blocking network printing:** Security software blocks the ports network printers use.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Inspect the queue and set the right default

Start with the two-minute triage.

1. Open **Settings > Bluetooth & devices > Printers & scanners** and click your printer, then **Open print queue**.
2. If jobs are stuck, cancel them all. In the queue window's **Printer** menu, uncheck **Pause Printing** and **Use Printer Offline**.
3. Back in printer settings, turn off **Let Windows manage my default printer**, then set your physical printer as default.
4. Print a test page (**Printer properties > Print Test Page**).

A clear queue, correct default, and no offline flag resolve the simplest — and most common — failures immediately.

### Fix 2: Restart the print spooler and clear its files

For queues that jam repeatedly, reset the spooler itself.

1. Press **Win + R**, type `services.msc`, and stop the **Print Spooler** service.
2. Delete all files in `C:\Windows\System32\spool\PRINTERS`.
3. Start the Print Spooler service again.
4. Print a test page.

If the same document jams the spooler every time, the file is corrupt — print it from a PDF export or recreate it. Persistent spooler crashes across all documents point to a driver problem (Fix 4).

### Fix 3: Remove and re-add the printer

A fresh device association clears corrupted printer configuration.

1. In **Printers & scanners**, select the printer and click **Remove**.
2. Restart the laptop.
3. Click **Add device** and let Windows rediscover it. For network printers that do not appear, click **Manually add** and add by IP address or hostname.
4. Print a test page.

For network printers, get the current IP from the printer's own menu (network configuration page) — do not trust the address Windows remembers. Assigning a static IP or a DHCP reservation on your router stops the address from changing again. Our [HP-focused printer guide](/articles/how-to-fix-printer-not-working-on-windows-11-on-hp-laptop/) covers brand-specific driver steps if you have an HP.

### Fix 4: Reinstall the manufacturer's full driver package

The definitive fix for driver-level breakage.

1. Disconnect USB printers. Uninstall all printer software for the model in **Settings > Apps > Installed apps**.
2. Download the **Full Feature Software and Drivers** package for Windows 11 from the manufacturer's support site ([HP Support](https://support.hp.com/us-en) for HP models).
3. Run the installer, reconnecting the printer only when prompted.
4. Complete setup and print a test page plus a scan test for all-in-ones.

Connecting the printer only when the installer asks prevents Windows from claiming it first with a generic driver — the step most people skip and most often matters.

### Fix 5: Fix the network printer connection

Network printers have failure modes USB printers never see.

1. Ping the printer's IP address from Command Prompt (`ping 192.168.x.x`) to confirm it is reachable.
2. If unreachable, power-cycle the printer and check it rejoined Wi-Fi (print a network config page).
3. In Windows, remove the printer and re-add it using the current IP address.
4. Temporarily disable third-party firewall software to test whether it blocks printing ports; if so, add an exception for the printer's IP.

Also check that the laptop and printer are on the same network band — some printers only use 2.4 GHz while laptops prefer 5 GHz, and certain routers isolate the bands from each other.

### Fix 6: Stabilize USB printer connections

For USB printers that work intermittently or vanish:

1. Try a different USB port, preferably one directly on the laptop rather than a hub.
2. Swap the USB cable — printer cables fail more often than printers do.
3. Disable **USB selective suspend** in Power Options advanced settings.
4. In Device Manager, uncheck power-saving on **USB Root Hub** entries.

Intermittent USB printers are a power-or-cable problem far more often than a driver problem. If other [USB devices also misbehave](/articles/best-way-to-fix-usb-ports-not-working/), fix the USB subsystem itself.

### Fix 7: Use built-in drivers and block bad updates

Fallbacks and prevention for the long term.

1. If the manufacturer offers no Windows 11 driver, use Windows' inbox drivers: remove the printer, re-add it, and let Windows install its built-in driver. For network printers, the Microsoft IPP Class Driver works with most modern models.
2. After a working driver is installed, hide problematic driver updates with the show/hide updates troubleshooter so Windows Update does not replace it.
3. Keep a note of the working driver version — it saves hours if the problem ever recurs.

Microsoft documents printer troubleshooting on the [Windows support site](https://support.microsoft.com/en-us/windows) as well. With the driver locked in and the network address stabilized, printer problems on Windows 11 rarely return.

## Closing

"Printer not working" on Windows 11 is a diagnosis-first problem: clear the queue and verify the default, reset the spooler, re-add the printer with its current address, and reinstall the manufacturer's driver package. Worked in that order, these steps resolve the jammed, offline, and driver-broken variants alike — and the prevention steps at the end keep the printer working.
