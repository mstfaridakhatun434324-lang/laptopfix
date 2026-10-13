---
title: "How to Fix a Printer Not Working on Windows 11 (Lenovo Laptop)"
slug: how-to-fix-printer-not-working-on-windows-11-on-lenovo-laptop
date: 2026-09-19
categories: ["drivers"]
tags: ["printer not working", "lenovo laptop", "printer driver", "windows 11"]
description: "Printer not working from your Lenovo laptop on Windows 11? Six fixes from print spooler repair to full driver reinstalls for USB and network printers."
thumbnail: "/images/thumbs/how-to-fix-printer-not-working-on-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "Why did my printer stop working after the Windows 11 24H2 update?"
    a: "The 24H2 upgrade migrates printer drivers, and older printer drivers — especially v3 kernel-mode drivers — often don't survive the migration or get replaced with a basic class driver that lacks your printer's features. Additionally, Microsoft has been tightening restrictions on legacy print components for security. The printer worked before because its proper driver was installed; reinstalling the current Windows 11 driver from the printer maker restores full function."
  - q: "My printer shows as 'Offline' but it's on and connected. What's wrong?"
    a: "'Offline' almost always means a communication or queue problem, not a dead printer. For USB printers, it's usually the port assignment or driver; for network printers, it's the IP address having changed (printers on DHCP get new addresses, breaking the configured port). Uncheck 'Use Printer Offline' in the print queue, then check the port configuration — a printer that pings at a new IP needs its port updated to match."
  - q: "Should I use the driver from Windows Update or the printer maker's site?"
    a: "Use the printer maker's site. Windows Update provides basic class drivers that print but often lack scanning, duplex control, ink-level reporting, and finishing options. The manufacturer's full driver package includes the status monitor and utilities your printer needs. Download it for your exact printer model and Windows 11 — never rely on the inbox driver for a printer you use seriously."
  - q: "The print spooler keeps stopping. Is that a driver problem?"
    a: "Usually yes — a crashing spooler is most often a corrupt print job or a bad printer driver (especially old v3 drivers) taking the spooler down with it. Clear the spooler queue manually, then update or reinstall the printer driver. If the spooler crashes with no printers installed at all, run SFC/DISM to repair system files, because then it's OS corruption rather than a driver."
---

The document is ready, you hit Print, and nothing happens — or the printer shows Offline, or jobs pile up in the queue going nowhere. Printer failures on Windows 11 are rarely about the printer: they're about the driver, the spooler service, and the port configuration between your Lenovo laptop and the printer. The printer itself is usually innocent, sitting there with full ink and a blinking ready light.

On Lenovo laptops specifically, there's an extra wrinkle worth knowing: Lenovo Vantage and Windows Update can both push driver updates that replace your printer's full-featured driver with a basic class driver, silently removing scanning and status features. And 24H2's migration is notorious for orphaning older printer drivers. So we'll work the standard printer stack — queue, spooler, driver, port — with the Lenovo-specific driver management noted where it matters. If Device Manager shows the printer as an unknown device rather than a printer problem per se, the [unknown device guide](/articles/how-to-fix-unknown-device-in-device-manager-in-windows-11-24h2/) helps identify it first.

## Why this happens

- **The 24H2 upgrade orphaned the printer driver.** The old driver didn't migrate, and Windows substituted a basic class driver — or nothing at all.
- **The print spooler is crashed or jammed.** A corrupt print job wedged the spooler, so nothing flows to the printer regardless of driver health.
- **The network printer's IP address changed.** DHCP reassigned the printer's address, but Windows still points the printer port at the old one.
- **"Use Printer Offline" got stuck on.** A transient disconnect flipped the queue to offline mode, and it never flipped back.
- **Lenovo/Windows Update replaced the full driver.** A driver update swapped the manufacturer's feature-complete package for a basic driver missing key functions.
- **The USB port assignment broke.** The printer enumerated on a different USB port after a reboot, but the driver still points at the old port.
- **A v3 legacy driver conflicts with 24H2 hardening.** Microsoft's ongoing restrictions on legacy print drivers can disable or degrade old kernel-mode printer drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the queue and restart the print spooler

Unjam the pipeline before touching drivers.

1. Open **Settings** > **Bluetooth & devices** > **Printers & scanners**, click your printer > **Open print queue**, and cancel all documents.
2. Press **Win + R**, type `services.msc`, find **Print Spooler**, right-click > **Restart**.
3. If jobs won't cancel: stop the spooler service, delete everything in `C:\Windows\System32\spool\PRINTERS`, then start the service again.
4. Send a test page (**Printer properties** > **Print Test Page**). If it prints, the jam was the whole problem.

### Fix 2: Uncheck "Use Printer Offline" and set as default

Fix the queue state flags.

1. In the print queue window, open the **Printer** menu — if **Use Printer Offline** is checked, uncheck it.
2. In **Settings** > **Printers & scanners**, ensure your printer is set as default (or disable **Let Windows manage my default printer**, which switches defaults unpredictably).
3. For USB printers, unplug and replug the USB cable with the printer on — watch for the "device connected" sound.
4. Print a test page again.
5. If the printer shows "Offline" only when the laptop wakes from sleep, USB power management is the trigger — disable USB selective suspend under Control Panel > Power Options > advanced settings so the port stops dropping the printer on wake.

### Fix 3: Reinstall the manufacturer's printer driver

Replace whatever the update left behind with the real driver.

1. In **Settings** > **Printers & scanners**, remove the printer entirely.
2. Go to the printer maker's website (HP, Canon, Brother, Epson) and download the full Windows 11 driver for your exact printer model — not the basic driver.
3. Run the installer with the printer connected (USB) or on the network as the installer directs.
4. Complete the installer's test print. Full-feature drivers restore scanning, ink levels, and finishing options the class driver lacks.

### Fix 4: Fix the port for network printers

Re-point Windows at the printer's current address.

1. Find the printer's current IP: print a network configuration page from the printer's own menu.
2. On the laptop, ping that IP to confirm reachability.
3. **Printer properties** > **Ports** tab > **Configure Port** — update the IP to match, or **Add Port** > **Standard TCP/IP Port** with the new address.
4. Better long-term: give the printer a static IP or DHCP reservation on your router so the address stops changing — this permanently ends the recurring "offline" mystery.

### Fix 5: Update the USB and chipset drivers on the Lenovo

For USB-connected printers that won't stay connected.

1. Open **Lenovo Vantage** > **System Update** and install chipset and USB driver updates.
2. In Device Manager, check **Universal Serial Bus controllers** for warning icons — reinstall any flagged USB hub drivers.
3. Try a different USB port, preferably a direct port rather than a hub; avoid USB hubs for printer testing.
4. If the printer needs an older driver package, the [compatibility mode install guide](/articles/how-to-install-driver-in-compatibility-mode-in-windows-11-24h2/) covers getting legacy printer drivers onto 24H2.

### Fix 6: Repair the print subsystem

When the spooler itself is corrupted.

1. Run the printer troubleshooter: **Settings** > **System** > **Troubleshoot** > **Other troubleshooters** > **Printer** > **Run**.
2. Open **Terminal (Admin)** and run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` — print components are system files too.
3. Check **Windows Update** for the latest cumulative update; Microsoft ships print-spooler fixes in these regularly.
4. As a final measure, remove all printers, stop the spooler, rename `C:\Windows\System32\spool\drivers` to `drivers.old`, restart, and reinstall the printer fresh — this rebuilds the entire driver store for printing. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the built-in printer troubleshooting flow if you need the official reference.

## Closing

Printer problems are stack problems: queue, spooler, driver, port — in that order. Clear the jam, restart the spooler, install the manufacturer's real driver, and fix the port addressing, and the printer that "stopped working" will be working again. And once it's healthy, give a network printer a static IP: it's the single most effective prevention for the mysterious recurring offline printer.
