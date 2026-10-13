---
title: "How to Check Your Disk for Errors on Windows 10 (3 Reliable Ways)"
slug: how-to-check-disk-for-errors-on-windows-10
date: 2026-10-02
categories: ["performance"]
tags: ["check disk", "chkdsk", "disk errors", "windows 10", "smart"]
description: "Check your disk for errors on Windows 10 with CHKDSK, the drive Properties tool, and SMART health checks — step by step."
thumbnail: "/images/thumbs/how-to-check-disk-for-errors-on-windows-10.webp"
faqs:
  - q: "How do I check my disk for errors on Windows 10?"
    a: "Three reliable methods: (1) Right-click the drive in File Explorer > Properties > Tools > Check — the friendly GUI option. (2) Run `chkdsk C: /f` in an elevated Command Prompt for a thorough file-system check, adding `/r` to also scan for bad sectors. (3) Check SMART health with a free tool like CrystalDiskInfo for the drive's self-reported condition. Use all three for a complete picture."
  - q: "What does chkdsk /f /r actually do?"
    a: "The /f parameter tells CHKDSK to fix logical file-system errors it finds — cross-linked files, lost clusters, directory errors. The /r parameter goes further: it scans the entire disk surface for bad sectors, recovers readable data from them, and marks them so Windows never uses them again. /r implies /f and takes much longer — hours on large HDDs, less on SSDs."
  - q: "Is it safe to run chkdsk on an SSD?"
    a: "Yes, running chkdsk with /f is safe on SSDs — it checks the file system, not the flash cells. Be more cautious with /r on SSDs: a full surface scan causes heavy writes and takes a long time, and SSDs handle bad blocks internally anyway. For SSD health, SMART data (via CrystalDiskInfo) is more informative than a surface scan. Never defragment an SSD, but chkdsk /f is fine."
  - q: "How often should I check my disk for errors?"
    a: "There's no need for scheduled checks on a healthy drive — Windows 10 automatically scans drives at boot when it detects problems (that's the 'scanning and repairing drive' screen). Run a manual check when you see symptoms: frequent freezes, files that won't open, Event Viewer disk errors, or SMART warnings. After any improper shutdown or power loss, a check is good preventive hygiene."
---

Disk errors are sneaky. They start as an occasional freeze, a file that won't open, a program crashing for no reason — and they end, if ignored, with a drive that won't boot. The good news: Windows 10 has excellent built-in tools for finding and fixing disk errors, and checking takes minutes of your time (plus some waiting while the scan runs).

This guide covers the three reliable methods: the graphical Check tool for quick scans, CHKDSK from the command line for thorough repairs, and SMART health monitoring to catch drives that are physically failing. Use them in that order — quick to deep — and you'll know exactly where your disk stands.

## Why this happens

- **Improper shutdowns**: Power loss or forced shutdowns interrupt writes, leaving the file system inconsistent.
- **Aging drive mechanics**: HDDs develop bad sectors over time; SSDs wear their flash cells with writes.
- **Failing hardware**: Dying controllers or degrading NAND produce errors faster than normal aging.
- **Bad cables/connections**: Loose SATA cables or failing USB enclosures cause I/O errors that look like disk errors.
- **Driver issues**: Buggy storage drivers corrupting transfers between Windows and the drive.
- **Malware damage**: Some malware deliberately corrupts file-system structures.
- **Overheating**: Hot drives (especially in cramped laptops) produce transient errors under thermal stress.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Quick check with the drive Properties tool

The fastest, friendliest check — start here.

1. Open **File Explorer** > **This PC**, right-click your system drive (usually C:) > **Properties**.
2. Go to the **Tools** tab and click **Check** under "Error checking."
3. Windows may say "You don't need to scan this drive" — click **Scan drive** anyway for peace of mind.
4. The scan runs in a few minutes on SSDs (longer on HDDs). It reports either "no errors found" or repairs what it finds automatically.
5. Repeat for your other drives (D:, external drives) — errors on a data drive cause the same symptoms as system-drive errors. If the laptop is generally slow too, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) — many of the principles apply to Windows 10 as well.

### Fix 2: Thorough check with CHKDSK

When the quick check isn't enough, CHKDSK goes deeper.

1. Open **Command Prompt as administrator**: search `cmd` in Start, right-click > **Run as administrator**.
2. For a standard repair scan, type `chkdsk C: /f` and press Enter. If it's the system drive, Windows will ask to schedule the scan at next reboot — type **Y** and press Enter, then restart.
3. For a deep scan including bad-sector detection, use `chkdsk C: /r` instead. **Warning**: this takes much longer (30 minutes to several hours) — run it overnight on AC power.
4. After the scan, review the summary: "0 KB in bad sectors" is what you want. Note the counts of repaired errors for your records.
5. To check the detailed results afterward, open **Event Viewer** > **Windows Logs** > **Application**, filter for source **Wininit** — the full CHKDSK log is there.

### Fix 3: Read the drive's SMART health data

CHKDSK fixes file systems; SMART tells you if the hardware itself is dying.

1. Download **CrystalDiskInfo** (free) and run it — it reads every connected drive's SMART data.
2. Check the top-line **Health Status**: **Good** (blue) = healthy; **Caution** (yellow) = degrading, back up now; **Bad** (red) = replace immediately.
3. For HDDs, watch **Reallocated Sectors Count**, **Current Pending Sector Count**, and **Uncorrectable Sector Count** — any raw values above zero are warning signs.
4. For SSDs, check **Percentage Used** / **Media Wearout Indicator** and **Available Spare** — these show how much of the drive's write lifespan is consumed.
5. Also note **Temperature** — consistently above 55–60°C in a laptop shortens drive life; improve cooling if it's hot.

### Fix 4: Fix what CHKDSK can't — bad sectors and corruption

When scans find problems, act on the results.

1. If CHKDSK repaired errors and SMART is **Good**: you're done — the file system is consistent again. Monitor for recurrence over the next weeks.
2. If CHKDSK finds **bad sectors** (`/r` scan): the drive marked them unusable, which is fine in small numbers — but growing bad-sector counts mean the drive is failing. Back up immediately.
3. If CHKDSK **can't complete** or hangs at a certain percentage: that's itself a bad sign — the drive may have unreadable areas. Try the scan from **Windows Recovery** (Shift + Restart > Troubleshoot > Command Prompt) where nothing else accesses the disk.
4. For external drives with errors: try a different USB port and cable first — enclosure/cable issues cause errors that vanish with better connections.
5. If errors keep recurring after repairs, the drive is telling you it's done — clone it to a replacement with a tool like Macrium Reflect Free *before* it fails completely.

### Fix 5: Prevent future disk errors

An ounce of prevention for your storage.

1. Always shut down properly — avoid holding the power button except as a last resort. Enable a UPS if your area has unstable power.
2. Keep **at least 15–20% free space** on every drive — full drives fragment more and give the file system less room for safe operations.
3. Keep storage drivers current: **Device Manager** > **Storage controllers** > update, or get chipset drivers from your vendor ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
4. Run `sfc /scannow` in an elevated Command Prompt periodically — corrupt system files can *cause* symptoms that mimic disk errors.
5. Maintain backups: Windows 10 **File History** (Settings > Update & Security > Backup) for documents, plus periodic full system images. A healthy backup makes any disk problem a minor inconvenience.

### Fix 6: Know when the drive must be replaced

Recognize the point of no return.

1. **Replace immediately** if: SMART status is Bad, bad-sector counts grow between scans, the drive makes clicking/grinding noises (HDD), or CHKDSK can't finish.
2. **Plan replacement soon** if: SMART shows Caution, the drive is over 5 years old with heavy use, or you see occasional Event Viewer disk errors (IDs 7, 11, 51, 154).
3. Before replacing, **back up everything** — clone the drive if it's still readable; copy critical files first if it's marginal.
4. Consider upgrading to an SSD if you're still on an HDD — it's the single biggest performance upgrade for an older Windows 10 laptop, and new drives come with warranties.
5. After replacement, verify with a fresh CrystalDiskInfo reading (should show Good, 100% health) and a clean `chkdsk` pass. Microsoft documents disk tools at Windows support.

## Closing

Checking your disk for errors is straightforward: quick GUI check, thorough CHKDSK, and SMART health reading. Most "mystery" freezes and crashes trace back to something these three reveal. Run the checks when symptoms appear, act on what they find, and keep backups — that's the entire disk-health discipline in one paragraph. For general performance tune-ups alongside disk health, see [speeding up a slow Windows 11 laptop](/articles/how-to-speed-up-windows-11-laptop/).
