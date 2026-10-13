---
title: "How Do I Fix a Printer Not Working on Windows 11?"
slug: how-do-i-fix-printer-not-working-on-windows-11
date: 2026-09-10
categories: ["drivers"]
tags: ["printer not working", "fix printer windows 11", "printer troubleshooting", "print queue stuck"]
description: "Printer not working on Windows 11 and not sure where to start? This plain-English walkthrough takes you from cable checks to driver fixes."
thumbnail: "/images/thumbs/how-do-i-fix-printer-not-working-on-windows-11.webp"
faqs:
  - q: "Where do I even start when my printer stops working?"
    a: "Start with the physical layer: is the printer on, does its display show an error, and is the cable or Wi-Fi connection solid? Then check whether Windows sees it in Settings > Bluetooth & devices > Printers & scanners. Half of all printer problems are connection or 'wrong default printer' issues, not driver problems."
  - q: "What does restarting the print spooler actually do?"
    a: "The Print Spooler is the Windows service that receives your documents and feeds them to the printer. When it stalls, jobs pile up and nothing prints. Restarting it clears the jam — and manually emptying its queue folder removes jobs so corrupted that even a restart cannot clear them."
  - q: "Why does Windows keep picking the wrong printer?"
    a: "Windows 11 has a 'let Windows manage my default printer' option that switches the default to whichever printer you used last, which surprises people with multiple printers. Turn that off in Settings > Bluetooth & devices > Printers & scanners and set your real default manually."
  - q: "When should I reinstall the printer driver?"
    a: "When the printer is connected and visible but prints garbage, only prints test pages, or shows a driver error — or when the problem started right after a Windows update. Download the full driver from the printer maker's site for your exact model rather than using the basic driver Windows offers."
---

If your printer suddenly stopped working on Windows 11, you are not alone — and you do not need to be technical to fix it. Most printer problems come down to a short list of causes: the connection dropped, the print queue jammed, the wrong printer is selected, or the driver broke after an update.

This guide assumes no prior knowledge. Each step tells you exactly where to click and what you should see, starting with the simple physical checks and moving up to the driver fixes. Work through them in order and stop when your test page prints.

## Why this happens

- **Printer not actually connected** — cable loose, Wi-Fi dropped, or printer asleep.
- **Wrong default printer selected**, so jobs go to a printer that is not there.
- **Print queue jammed** with a stuck job blocking everything behind it.
- **Print Spooler service stalled**, freezing all printing.
- **Printer showing 'offline'** while powered on, usually a network address change.
- **Driver broken by a Windows update**, needing a fresh install from the maker.
- **Printer's own error state** — out of paper, low ink, or a paper jam you have not noticed.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the printer itself first

Walk to the printer. Is it powered on? Does its screen show an error like 'paper jam', 'low ink', or 'offline'? Clear any paper jams, make sure paper is loaded, and check ink or toner. Printers stop for their own reasons constantly, and Windows cannot fix a printer that is refusing for hardware reasons. Print a test page from the printer's own menu to confirm the printer itself works.

1. Check the printer's power and display for errors.
2. Clear jams, load paper, and check ink/toner.
3. Print a self-test page from the printer's menu.
4. Only continue if the printer's own test page prints fine.

### Fix 2: Check the connection

For USB printers, unplug the cable from both ends and plug it back in firmly — try a different USB port too. For Wi-Fi printers, check the printer's display for a Wi-Fi icon; if it dropped off the network, reconnect it to your Wi-Fi from the printer's settings menu. A printer Windows cannot reach cannot print, no matter what you do in Windows.

1. Reseat the USB cable or reconnect the printer to Wi-Fi.
2. Try a different USB port for wired printers.
3. Confirm the printer shows as connected on its own display.
4. Check that your laptop is on the same Wi-Fi network.

### Fix 3: Set the correct default printer

Open Settings > Bluetooth & devices > Printers & scanners. If your printer is listed, click it and choose 'Set as default'. Turn off 'Let Windows manage my default printer' so Windows stops switching it behind your back. Then right-click a document and print — or better, print a Windows test page from the printer's properties.

1. Open Settings > Bluetooth & devices > Printers & scanners.
2. Set your printer as the default.
3. Turn off 'Let Windows manage my default printer'.
4. Print a test page from the printer's properties.

### Fix 4: Clear the stuck print queue

Open the print queue by double-clicking the printer icon in the taskbar (or via Printers & scanners > Open print queue). If jobs are stuck, cancel them all. If they refuse to cancel, restart the Print Spooler: press Win + R, type services.msc, find Print Spooler, and restart it. Microsoft walks through queue issues in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open the print queue and cancel all documents.
2. If jobs will not cancel, open services.msc.
3. Restart the Print Spooler service.
4. Try printing again.

### Fix 5: Run the Windows printer troubleshooter

Windows 11 has a built-in troubleshooter that checks the common faults automatically. Go to Settings > System > Troubleshoot > Other troubleshooters and run 'Printer'. It checks the spooler, the driver, and the port, and applies fixes itself. It will not fix everything, but it is free and takes two minutes.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Printer troubleshooter.
3. Apply whatever fixes it recommends.
4. Print a test page afterward.

### Fix 6: Remove and re-add the printer

In Printers & scanners, select your printer and click Remove. Restart your laptop, then click 'Add device' and let Windows find the printer again. For Wi-Fi printers that show 'offline', adding via the printer's current IP address (from its network config page) is more reliable than auto-discovery. The deeper technical version of this process is in our [printer troubleshooting guide](/articles/troubleshoot-printer-not-working-on-windows-11/).

1. Remove the printer from Printers & scanners.
2. Restart the laptop.
3. Click Add device and re-add the printer.
4. Print a test page to confirm.

### Fix 7: Reinstall the printer driver from the maker

Go to the printer maker's website (HP, Canon, Epson, Brother), find your exact model, and download the full driver and software package. Uninstall the old printer software from Settings > Apps first, then run the maker's installer with the printer connected. The maker's full package includes the status monitor and scanning tools that Windows' basic driver lacks.

1. Uninstall the old printer software from Settings > Apps.
2. Download the full driver package from the maker's site.
3. Run the installer with the printer connected and on.
4. Print and scan test pages to verify everything.

## Closing

Printer troubleshooting is really just working a short checklist: the printer's own state, the connection, the default selection, the queue, and the driver. Most people find the problem in the first three steps and never need the driver reinstall. And when a Windows update is the trigger, the maker's fresh driver plus a re-add is the combination that puts things right — keep the maker's support page bookmarked, because printers and updates will meet again. HP owners can also use the [HP-specific printer fixes](/articles/how-to-fix-printer-not-working-on-windows-11-on-hp-laptop/). If you print over Wi-Fi, give the printer a static IP address or a DHCP reservation in your router settings. Printers that change addresses after every router reboot are the number one cause of the mysterious it-worked-yesterday offline problem — a fixed address ends it permanently.
