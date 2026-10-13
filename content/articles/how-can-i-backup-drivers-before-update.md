---
title: "Back Up Your Drivers Before Updating Windows"
slug: how-can-i-backup-drivers-before-update
date: 2026-09-13
categories: ["drivers"]
tags: ["backup drivers", "driver backup", "windows update safety", "dism"]
description: "Back up your working drivers before any Windows update: built-in tools and simple methods to restore them if an update breaks something."
thumbnail: "/images/thumbs/how-can-i-backup-drivers-before-update.webp"
faqs:
  - q: "Why should I back up drivers before a Windows update?"
    a: "Windows updates frequently replace working manufacturer drivers with generic or incompatible versions, breaking Wi-Fi, audio, or graphics. A driver backup lets you restore the exact working versions in minutes instead of hunting down downloads — especially valuable when the broken driver is your network adapter and you're offline."
  - q: "What's the easiest built-in way to back up drivers?"
    a: "The DISM command: open an elevated Command Prompt and run dism /online /export-driver /destination:C:\\DriverBackup. It copies all third-party drivers into one folder. To restore, point Device Manager's 'Browse my computer for drivers' at that folder, or use pnputil to reinstall them all at once."
  - q: "How much space does a driver backup need?"
    a: "Usually between a few hundred megabytes and 2GB, depending on how many devices and how large the graphics and printer drivers are. A USB stick or a folder on a secondary drive is plenty. The backup is small enough to keep multiple dated copies, which is worth doing before major feature updates."
  - q: "Do I need third-party software to back up drivers?"
    a: "No. Windows' built-in DISM export and PowerShell cmdlets handle driver backup completely, and System Restore points capture driver state too. Third-party backup tools add little and some bundle unwanted software. Stick with the built-in tools — they're free, reliable, and already on your machine."
---

Every experienced technician has a story about a Windows update that replaced a working driver with a broken one — and the fix taking ten times longer because nobody saved the working version first. Driver backup is the five-minute insurance policy that turns those disasters into minor annoyances. This guide shows the built-in methods; no third-party tools needed.

The principle is simple: before any major update, export your third-party drivers to a folder you can reach even if the network breaks. Then if an update mangles your Wi-Fi, audio, or graphics, you restore the exact working driver in minutes. Do this before feature updates especially — they're the ones that swap drivers most aggressively.

## Why this happens

- **Updates replace working drivers:** Feature updates install generic drivers over tuned manufacturer packages.
- **Network drivers break first:** The cruelest failures kill the Wi-Fi you need to download the fix.
- **No rollback available:** Sometimes Windows doesn't keep the old driver for rollback.
- **Maker sites reorganize:** Old driver versions vanish from support pages over time.
- **Clean installs need drivers:** A fresh Windows install needs every driver re-found.
- **Corruption happens:** Driver files degrade; a known-good copy is the fastest repair.
- **Multiple machines:** One backup can serve identical laptop models.
- **Peace of mind:** Five minutes of prevention beats hours of cure.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Export drivers with DISM (the core method)

Open an elevated Command Prompt (search cmd, right-click, Run as administrator). Create a destination folder, then run: `dism /online /export-driver /destination:C:\DriverBackup`. DISM copies every third-party driver package into that folder, organized by published name. It takes a few minutes. Verify the folder has content — you should see dozens of .inf files with their driver packages. Copy this folder to a USB drive or secondary partition so it survives even if Windows needs reinstalling. This single command is 90% of driver backup.

1. Open an elevated Command Prompt.
2. Create the destination folder (e.g., C:\DriverBackup).
3. Run `dism /online /export-driver /destination:C:\DriverBackup`.
4. Verify .inf files and driver folders were exported.
5. Copy the folder to external storage.

### Fix 2: Back up with PowerShell for automation

For a scriptable version, open elevated PowerShell and run: `Export-WindowsDriver -Online -Destination C:\DriverBackup`. It does the same job as DISM through a cmdlet you can schedule. Save it as a .ps1 script and run it before every Patch Tuesday, or create a scheduled task that exports monthly to a dated folder. Pair this with our [safe driver update guide](/articles/how-can-i-update-drivers-on-windows-11/) — backup before, update after, and you have a complete safety workflow.

1. Open elevated PowerShell.
2. Run `Export-WindowsDriver -Online -Destination C:\DriverBackup`.
3. Save the command as a reusable .ps1 script.
4. Schedule monthly exports to dated folders.
5. Keep at least two historical copies.

### Fix 3: Create a System Restore point as well

Driver exports save the files; a restore point saves the whole system state including driver registrations. Search "Create a restore point," select the system drive, click Create, and name it with the date and reason ("Before 24H2 update"). Restore points capture registry state that a file backup doesn't, so the two methods complement each other. Verify restore points are enabled — on some systems protection is off by default, which makes this step silently do nothing.

1. Search "Create a restore point" and open it.
2. Confirm protection is enabled on the system drive.
3. Click Create and name it descriptively.
4. Wait for completion confirmation.
5. Note the restore point name and date.

### Fix 4: Document your working driver versions

Open Device Manager and record the driver version and date for critical devices: display adapter, network adapters, audio, and chipset (Device Properties, Driver tab). Save this in a text file inside your backup folder. After an update, comparing versions instantly reveals which driver Windows replaced — no guessing. This documentation turns "something broke after the update" into "the Wi-Fi driver went from 22.1 to 23.4," which is a directly actionable fact. [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) explains Device Manager's driver details.

1. Open each critical device's Driver tab in Device Manager.
2. Record version, date, and provider for each.
3. Save the list in the backup folder as drivers.txt.
4. Include Wi-Fi, graphics, audio, chipset, Bluetooth.
5. Compare after updates to spot replacements.

### Fix 5: Restore a single driver from backup

When an update breaks one device, you don't need to restore everything. In Device Manager, right-click the broken device, choose Update driver, "Browse my computer for drivers," and point it at your backup folder with "Include subfolders" ticked. Windows will find the matching exported driver and install it. This surgical restore takes two minutes and leaves everything else untouched — far better than rolling back the entire update for one bad driver.

1. Right-click the broken device in Device Manager.
2. Choose Update driver, Browse my computer.
3. Point at the backup folder with subfolders included.
4. Let Windows install the matching exported driver.
5. Reboot and verify the device works.

### Fix 6: Bulk-restore with pnputil

If several drivers broke at once, restore them all: open an elevated Command Prompt, navigate to the backup folder, and run `pnputil /add-driver *.inf /subdirs /install`. This reinstalls every exported driver package. It's the fastest path after a feature update mangles multiple devices. Reboot afterward and check Device Manager for remaining warnings. Keep the backup folder organized by date so you always restore the right generation — restoring ancient drivers over newer working ones creates its own problems.

1. Open an elevated Command Prompt in the backup folder.
2. Run `pnputil /add-driver *.inf /subdirs /install`.
3. Wait for all packages to install.
4. Reboot the laptop.
5. Check Device Manager for remaining issues.

### Fix 7: Block the bad driver from returning

Restoring is only half the battle — Windows Update will cheerfully reinstall the broken driver again. After restoring, block it: on Pro, use `gpedit.msc` to enable "Do not include drivers with Windows Updates"; on any edition, use the "Show or hide updates" troubleshooter to hide the specific driver update. Verify after the next update cycle that your restored versions survived. Then make driver backup a habit — monthly exports plus pre-feature-update exports mean you're never more than a few minutes from recovery. See [stopping driver replacements](/articles/how-to-fix-wifi-driver-code-10-error-in-windows-11-24h2/) for related protection.

1. Block driver updates via Group Policy or the troubleshooter.
2. Hide the specific offending driver update.
3. Verify versions survive the next update cycle.
4. Schedule monthly driver exports.
5. Always export before feature updates.

## Closing

Driver backup is the cheapest insurance in Windows maintenance: one DISM command, a restore point, and a version list, done in under ten minutes. The next time an update breaks your Wi-Fi or audio, you'll restore the working driver before you've finished your coffee — instead of spending the evening hunting downloads on your phone. Make it a habit, not a rescue operation.
