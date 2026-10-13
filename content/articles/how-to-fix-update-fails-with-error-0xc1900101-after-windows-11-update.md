---
title: "Windows Update Fails With Error 0xC1900101? Here's How to Fix It"
slug: how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update
date: 2026-10-10
categories: ["windows-update"]
tags: ["0xc1900101", "update error", "driver conflict", "windows 11", "update rollback"]
description: "Error 0xC1900101 keeps rolling back your Windows 11 update? Decode the extended error code, find the guilty driver, and get the update installed."
thumbnail: "/images/thumbs/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update.webp"
faqs:
  - q: "What does error 0xC1900101 mean?"
    a: "It's Windows' code for 'a driver broke the update.' During installation, Windows migrates your drivers to the new build; if one fails to load in the new environment, the whole update rolls back with 0xC1900101. The extended code after the dash (like 0x30018) identifies which phase failed, narrowing the suspect list considerably."
  - q: "Which drivers most commonly cause 0xC1900101?"
    a: "Storage controller drivers (Intel RST, Samsung NVMe), display drivers, and network drivers top the list, followed by antivirus filter drivers and old peripheral drivers for printers or scanners. The pattern is drivers that hook deep into the kernel — the deeper the hook, the more likely it breaks across a build upgrade."
  - q: "Will updating all my drivers fix 0xC1900101?"
    a: "Often yes, but blindly updating everything can backfire if the newest driver has its own issues. The smarter approach is identifying the specific failing driver from setupact.log or the extended code, then updating or removing just that one. Targeted beats carpet-bombing for this error."
  - q: "Can antivirus cause 0xC1900101?"
    a: "Absolutely — third-party antivirus installs kernel filter drivers that are among the most common 0xC1900101 triggers. Temporarily uninstalling (not just disabling) the antivirus before a feature update resolves a large share of cases. Windows Defender, which is designed for build upgrades, can stay on."
---

0xC1900101 is the error code of a driver mutiny. Everything else about the update was fine — the download verified, the files staged, the installation began — and then one driver refused to make the trip to the new build. Windows, correctly, chose to roll everything back rather than leave you with a system missing a critical driver. The result: hours wasted, the "Undoing changes" screen, and a hex code that looks like line noise.

The good news is that 0xC1900101 is one of the most diagnosable update errors in Windows. The extended code pinpoints the failure phase, the setup logs usually name the offending driver file, and Microsoft's SetupDiag tool automates the whole analysis. This isn't a "try random fixes" error — it's a "find the guilty driver and deal with it" error. Here's the full procedure.

## Why this happens

- **Incompatible storage driver**: Intel RST, RAID, or NVMe drivers that can't initialize under the new build — the single most common cause.
- **Display driver conflict**: Old GPU drivers failing during the second-boot phase when the display stack comes up.
- **Antivirus filter drivers**: Kernel-level security drivers blocking or breaking during migration.
- **Peripheral drivers**: Printer, scanner, or USB device drivers from vendors who never updated them for the new build.
- **BIOS/UEFI too old**: Firmware the new build's driver model doesn't support, cascading into driver failures.
- **Corrupt driver in the DriverStore**: A damaged driver package that fails when Windows tries to migrate it.
- **Insufficient system partition space**: Too little room for the driver migration staging, failing late in the process.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Decode the extended error code

The full error looks like 0xC1900101 - 0x30018. Those last digits are the diagnosis.

1. Find the complete code in **Settings > Windows Update > Update history** (expand the failed update).
2. **0x2000C**: Safe OS phase failure — driver issue during the downlevel phase; check recently installed drivers.
3. **0x30018**: First boot phase — a driver failed as the new build booted; usually storage or chipset.
4. **0x40017**: Second boot phase — failure after the first restart; commonly display or network drivers.
5. **0x50012**: Sysprep/app failure — an application (not driver) blocked the upgrade.
6. Write down your phase — it focuses every step that follows.

### Fix 2: Find the guilty driver in the setup logs

The logs usually name names. Ten minutes here saves hours of guessing.

1. Open File Explorer and navigate to `C:\$Windows.~BT\Sources\Panther\` (enable hidden files if needed).
2. Open `setupact.log` in Notepad and search for "Failed" or "0xC1900101".
3. Look for driver file names near the failure — patterns like `oem42.inf`, `iaStorAC.sys`, or `nvlddmkm.sys`.
4. Also check `setuperr.log` in the same folder — it's the condensed error-only version.
5. Alternatively, run Microsoft's **SetupDiag** tool — it parses these logs automatically and names the failure.
6. Once you have the driver name, you know exactly what to update or remove.

### Fix 3: Update storage drivers first (the top suspect)

If the extended code points at the boot phases (0x30018/0x40017) or the log names a storage driver, this is your fix.

1. Identify your storage controller in **Device Manager** under **Storage controllers** / **IDE ATA/ATAPI controllers**.
2. If you see **Intel Chipset SATA RAID Controller** or similar RST entries, get the latest RST driver from Intel's official support site or your laptop maker.
3. For NVMe drives, check the drive maker's site for NVMe driver updates.
4. Consider switching **RAID to AHCI** in BIOS if you're not actually using RAID — RAID mode needs the RST driver; AHCI uses the inbox Microsoft driver which never causes this error. (Back up first; the switch can prevent booting if done wrong — research your model's procedure.)
5. After updating, retry the Windows update.

### Fix 4: Uninstall third-party antivirus completely

Disabling isn't enough — filter drivers load regardless. For the update attempt, the antivirus must be fully gone.

1. Go to **Settings > Apps > Installed apps** and uninstall your third-party antivirus.
2. Run the vendor's **removal tool** if they offer one (Norton, McAfee, Kaspersky all have them) — these clean up leftover filter drivers.
3. Confirm Windows Defender activates automatically (it will).
4. Disconnect non-essential USB devices too — their drivers are secondary suspects.
5. Run the Windows update now.
6. Reinstall your antivirus after the update succeeds. If 0xC1900101 returns on the next feature update, consider whether that antivirus is worth the recurring pain.

### Fix 5: Clean-boot the update to isolate software conflicts

When logs are inconclusive, a clean boot removes all non-Microsoft drivers and services from the equation.

1. Run `msconfig`, hide all Microsoft services, and **Disable all** on the Services tab.
2. Disable all startup items in Task Manager.
3. In **Device Manager**, temporarily disable non-essential devices (printers, scanners, USB peripherals, virtual adapters).
4. Restart and run the update.
5. If it succeeds, re-enable devices and services in groups to find the culprit — then update or replace that driver permanently.
6. Our [driver rollback guide](/articles/how-to-rollback-driver-update-in-windows-11-24h2/) helps if a specific driver version is the problem.

### Fix 6: Update BIOS and prune the DriverStore

Old firmware plus a cluttered driver store is a potent 0xC1900101 cocktail.

1. Update your BIOS/UEFI from the manufacturer's site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/).
2. Back up drivers (see our [backup guide](/articles/how-to-backup-drivers-before-update-in-windows-11-24h2/)), then run `pnputil /enum-drivers` in elevated Command Prompt.
3. Remove ancient third-party `oem*.inf` drivers for hardware you no longer own (old printers are classic).
4. Run `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow` to repair servicing damage.
5. Ensure 20+ GB free on C: — migration staging needs room.

### Fix 7: Block the bad driver and retry

If one specific driver is identified but no update exists for it, remove it from the migration path.

1. In **Device Manager**, uninstall the offending device, checking **"Attempt to remove the driver"** if offered.
2. Physically disconnect the hardware if it's external.
3. Use Microsoft's "Show or hide updates" tool to block the driver if Windows Update keeps offering it.
4. Run the feature update — without the bad driver in the migration set, it should complete.
5. Afterward, check the hardware vendor for an updated driver, or leave the device on Microsoft's inbox driver.
6. For recurring 0xC1900101 across updates, the pattern usually means one aging device — identifying it once (Fix 2) prevents every future occurrence.

## Closing

0xC1900101 rewards diagnosis and punishes guessing. Decode the extended code, read setupact.log or run SetupDiag, and you'll usually find one driver with its name on the failure. Update it, remove it, or uninstall the antivirus whose filter driver is the real culprit — and the update that rolled back three times will install on the fourth attempt without drama.
