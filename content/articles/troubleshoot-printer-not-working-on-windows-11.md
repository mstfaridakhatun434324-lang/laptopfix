---
title: "Printer Not Working on Windows 11? Troubleshooting Guide"
slug: troubleshoot-printer-not-working-on-windows-11
date: 2026-10-07
categories: ["drivers"]
tags: ["printer not working", "windows 11 printer", "printer spooler", "printer offline"]
description: "Printer not working on Windows 11? Fix offline printers, stuck print jobs, and spooler errors with this complete troubleshooting guide."
thumbnail: "/images/thumbs/troubleshoot-printer-not-working-on-windows-11.webp"
faqs:
  - q: "Why does my printer show as offline when it is on?"
    a: "The offline status usually means Windows lost communication with the printer, not that the printer is off. Causes include a changed IP address on network printers, a stalled print spooler, or SNMP status reporting errors. Restarting the spooler and re-adding the printer with its current IP address fix the great majority of offline-but-on cases."
  - q: "How do I clear a stuck print job that will not delete?"
    a: "Stop the Print Spooler service, delete the files in C:\\Windows\\System32\\spool\\PRINTERS, then start the service again. Jobs that resist the normal cancel button are locked in the spooler queue, and clearing the folder manually is the reliable way to remove them."
  - q: "Should I use the manufacturer's driver or the Windows built-in driver?"
    a: "Use the manufacturer's full driver package from HP, Canon, Epson, or Brother for your exact model. Windows' built-in class drivers handle basic printing but often lack scanning, duplex control, and status monitoring. If the full package misbehaves, the built-in driver is a good fallback for testing."
  - q: "Why did my printer stop working after a Windows update?"
    a: "Updates sometimes break the print spooler, replace the printer driver with an incompatible version, or re-enable security defaults that block older printers. Microsoft has released several print-specific fixes through Windows Update itself, so check for updates first, then reinstall the manufacturer's driver."
---

Printer problems on Windows 11 follow a familiar script: the printer shows offline even though it is on, jobs pile up in the queue and never print, or the printer simply vanishes after an update. These faults look different but share the same handful of root causes — the print spooler, the driver, or the connection.

Windows 11 did not fundamentally change printing, but updates have repeatedly disturbed it, which is why printer failures cluster around Patch Tuesdays. The troubleshooting order below is deliberate: connection first, because no software fix helps a printer Windows cannot reach; then the spooler; then the driver; then the deeper resets.

## Why this happens

- **Print Spooler service stalled or crashed**, freezing the entire print queue.
- **Printer showing offline** because its network IP address changed after a router reboot.
- **Corrupted or mismatched printer driver**, especially after a Windows update.
- **Stuck print job** blocking every job behind it in the queue.
- **Wrong default printer** selected, sending jobs to a printer that is not there.
- **USB connection issue** — cable, port, or the printer's USB interface not enumerating.
- **Windows update broke printing** via spooler or driver changes needing a patch or reinstall.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the connection and set the right default

Start physical. For USB printers, try a different port and cable — printers are picky about marginal cables. For network printers, print a network configuration page from the printer's panel and confirm the IP address matches what Windows expects. Then go to Settings > Bluetooth & devices > Printers & scanners, and make sure the correct printer is set as default.

1. Check cables, ports, and the printer's own display for errors.
2. For network printers, print a network config page and note the IP address.
3. Open Settings > Bluetooth & devices > Printers & scanners.
4. Set the correct printer as default and run a test page.

### Fix 2: Restart the Print Spooler

The spooler manages every print job, and restarting it clears most queue freezes. Open services.msc, find Print Spooler, and restart it. If jobs are stuck and will not cancel, stop the service, delete everything in C:\Windows\System32\spool\PRINTERS, and start it again — this empties the queue completely.

1. Press Win + R, type `services.msc`, and press Enter.
2. Right-click Print Spooler and choose Restart.
3. If jobs remain stuck: stop the service, delete files in the PRINTERS folder, start it again.
4. Send a test print.

### Fix 3: Run the printer troubleshooter

Windows 11 includes a printer troubleshooter that checks the spooler, the driver, and the port configuration automatically. It is not magic, but it catches misconfigured ports and stopped services quickly. Microsoft documents printer troubleshooting in the [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Printer troubleshooter and apply any fixes it suggests.
3. Restart the laptop if prompted.
4. Test printing again.

### Fix 4: Remove and re-add the printer

Removing the printer clears its port and driver associations, and re-adding it rebuilds them cleanly. This is the definitive fix for the 'offline when it is on' problem on network printers, because re-adding picks up the printer's current IP address. Use the manufacturer's setup utility or add it manually via its IP.

1. In Printers & scanners, select the printer and click Remove.
2. Restart the laptop.
3. Click Add device, or add manually via TCP/IP with the printer's current IP.
4. Print a test page to confirm.

### Fix 5: Reinstall the manufacturer's driver

Download the full driver package from the printer maker's support site for your exact model — not the class driver Windows offers. Uninstall the existing printer software first, then install fresh. For HP printers specifically, HP's own support page at [support.hp.com](https://support.hp.com/us-en) also offers a Print and Scan Doctor tool that automates much of this. Model-specific variants are covered in our [HP printer fix](/articles/how-to-fix-printer-not-working-on-windows-11-on-hp-laptop/).

1. Uninstall the printer software from Settings > Apps.
2. Download the full driver package from the manufacturer's site.
3. Run the installer with the printer connected and powered on.
4. Print and scan test pages to verify full function.

### Fix 6: Check for Windows updates and printer firmware

Microsoft has shipped several out-of-band fixes for printing bugs, so an update may be the actual cure. Check Settings > Windows Update for pending updates, including optional ones. Separately, check the printer maker's site for firmware updates — outdated printer firmware causes communication failures that look like Windows problems.

1. Check Windows Update and install all pending updates.
2. Check the printer maker's site for a firmware update for your model.
3. Apply the firmware update following the maker's instructions.
4. Retest printing after both updates.

### Fix 7: Reset printing with a clean driver store

When nothing else works, purge the driver store. Remove the printer, then open Print Management (printmanagement.msc), delete the driver package under Drivers, and reinstall from scratch. This eliminates corrupted driver files that survive normal reinstalls. As a last resort, a new Windows user profile rules out profile-level spooler corruption.

1. Remove the printer from Settings.
2. Open printmanagement.msc and delete the driver under Drivers.
3. Reinstall the manufacturer's driver package cleanly.
4. If it still fails, test from a new Windows user profile.

### Fix 8: Fix the network address and SNMP reporting

For network printers stuck showing offline, the printer's IP address has often changed after a router reboot. Print a network configuration page from the printer's panel, then open the printer's Properties > Ports tab and update the port to the new IP. Also try disabling SNMP status on the port: Windows marks printers offline based on SNMP responses, and some printers answer SNMP unreliably. With SNMP off, Windows trusts the live TCP connection instead.

1. Print a network config page from the printer.
2. Update the printer port to the printer's current IP.
3. Disable SNMP status on the port configuration.
4. Restart the spooler and test print.

## Closing

Windows 11 printer failures are spooler, driver, or connection problems in roughly that order of likelihood — and the fixes above address each in turn. The spooler restart and the remove-and-re-add cycle resolve most cases without any downloads. When updates are the trigger, the manufacturer's fresh driver plus any pending Windows patches close the loop. Printers remain fussy, but they are rarely truly broken. For the HP-specific variant of these faults, see [fixing printers on HP laptops](/articles/how-to-fix-printer-not-working-on-windows-11-on-hp-laptop/). For the brand-agnostic version of the same driver-and-spooler sequence, our [core printer repair guide](/articles/how-to-fix-printer-not-working-on-windows-11/) covers every manufacturer in one place.
