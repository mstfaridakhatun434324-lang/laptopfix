---
title: "Fix Windows Update Error 0x80070057 on Windows 10: The Parameter Is Incorrect"
slug: how-to-fix-windows-update-error-0x80070057-on-windows-10
date: 2026-10-11
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x80070057", "parameter incorrect", "troubleshooting"]
description: "Error 0x80070057 on Windows 10 blocks updates with 'the parameter is incorrect.' Fix it with these Windows 10-specific steps, from locale check to repair install."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070057-on-windows-10.webp"
faqs:
  - q: "What causes 0x80070057 on Windows 10?"
    a: "The error means the update engine received invalid parameters. On Windows 10 the classic triggers are a wrong decimal symbol in Region settings, corrupted update metadata in the SoftwareDistribution cache, a damaged component store, or a full System Reserved partition blocking boot-file updates."
  - q: "Why is the decimal symbol relevant to Windows Update?"
    a: "Some update components parse version numbers expecting a period as the decimal separator. In regions where the comma is standard, the parser misreads the values and the update fails with 0x80070057. Setting the decimal symbol to a period in Region settings fixes it instantly when this is the cause."
  - q: "Can I fix 0x80070057 without losing my files?"
    a: "Yes — every fix in this guide preserves your files, including the in-place upgrade repair install, which explicitly keeps personal files and applications. Only a clean install would remove data, and that is not needed for this error. Backing up important files beforehand is still wise, as with any system repair."
  - q: "The error appears during a Windows 10 feature update. Is that normal?"
    a: "Yes. Feature updates pass far more parameters than monthly patches — driver migration lists, component manifests, boot configuration data — so parameter corruption shows up most often there. Fix the underlying data corruption with the steps in this guide and the feature update will usually proceed normally on the next attempt."
---

Windows 10's version of error 0x80070057 carries the same meaning as on Windows 11: "the parameter is incorrect." Somewhere in the update process, corrupted data — a bad manifest, a wrong registry value, a misparsed version number — got handed to a component that rejected it. On Windows 10 this error has a long and well-documented history, including one famously odd cause (your decimal symbol) that still catches people today.

The repairs themselves are the standard Windows 10 toolkit, navigated through Windows 10's Settings and Control Panel. Work through them in order, and check for updates after each major step. Start with the quick locale check — it takes thirty seconds and resolves more cases than its absurdity suggests.

## Why this happens

- **Wrong decimal symbol:** Region settings using a comma as the decimal separator break version-number parsing in update components — the classic 0x80070057 trigger.
- **Corrupted update metadata:** Damaged manifests in the SoftwareDistribution cache describe the update with invalid parameters.
- **Damaged component store:** WinSxS corruption produces wrong baseline data, so computed update parameters fail validation.
- **Full System Reserved partition:** Boot-file updates fail when this small partition has no free space, surfacing as 0x80070057.
- **Corrupted Windows Update registry keys:** Bad values under the update hives feed invalid parameters to the engine.
- **Antivirus interference:** Security software hooking update APIs can corrupt parameters as they pass through.
- **Damaged system files:** Corrupted protected files loaded by the update engine cause parameter validation failures.
- **Stuck pending operations:** Leftover pending.xml entries from a failed update feed stale parameters into the next attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the decimal symbol is a period

Do this first. It is the fastest fix on the list and a genuinely common cause on Windows 10 systems using non-US regional formats.

1. Open **Control Panel > Clock, Language, and Region > Region** (or **Change date, time, or number formats**).
2. Click **Additional settings** and confirm **Decimal symbol** is `.` (a period, not a comma).
3. Change it if needed, click OK, and restart the laptop.
4. Check for updates via **Settings > Update & Security > Windows Update**.

### Fix 2: Run the Windows Update troubleshooter

Windows 10's troubleshooter resets components and repairs metadata paths.

1. Go to **Settings > Update & Security > Troubleshoot > Additional troubleshooters**.
2. Select **Windows Update** and click **Run the troubleshooter**.
3. Apply every recommended fix, restart, and retry.

### Fix 3: Reset the SoftwareDistribution and Catroot2 folders

Rebuild the cache to eliminate corrupted metadata and manifests.

1. Right-click Start and open **Command Prompt (Admin)**.
2. Run: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart and check for updates.

### Fix 4: Run DISM and SFC

Repair the component store baseline and protected system files.

1. In **Command Prompt (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. When it finishes, run `sfc /scannow`.
3. Restart and retry the update. This is the same repair sequence used for [missing-file update errors](/articles/how-to-fix-windows-update-error-0x80070002-on-windows-11/), which overlap with this error's causes.

### Fix 5: Clear space on the System Reserved partition

A full System Reserved partition is a notorious 0x80070057 source on Windows 10, especially on older machines upgraded through multiple versions.

1. Open **Disk Management** (right-click the Start button).
2. Locate the **System Reserved** partition — it needs roughly 15 MB or more free.
3. If full: right-click it, assign a drive letter, open it in Explorer, navigate to the Fonts folder under the boot directory, and remove non-essential language font files.
4. Remove the drive letter, restart, and retry the update.

### Fix 6: Pause third-party antivirus during the update

Rule out security software corrupting update parameters in transit.

1. Temporarily disable real-time protection in your antivirus.
2. Immediately run Windows Update and let the pending update install.
3. Re-enable protection right after the restart.
4. If the update succeeded with protection off, configure permanent Windows Update exclusions.

### Fix 7: Run an in-place upgrade repair install

When registry or servicing-stack corruption resists every targeted fix, reinstall Windows 10 over itself while keeping everything. Mount a Windows 10 ISO (from the [Microsoft software download page](https://www.microsoft.com/en-us/software-download/windows11) family of official downloads — choose the Windows 10 media), run setup.exe, and select **Keep personal files and apps**. The hour-long process replaces all servicing components. Afterward, check for updates; with a fresh servicing stack, the parameter errors are gone. For ongoing update health, the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) covers current best practices.

The decimal-symbol quirk deserves a fuller explanation because it is so easy to dismiss. Some update components format and parse version strings using the system's regional settings rather than a fixed format. In locales where the comma is the decimal separator — much of Europe and South America — a version like 10.0.22631 can be misread, and the resulting parameter fails validation with 0x80070057. Changing the symbol to a period does not alter how your other applications display numbers in any meaningful way for most users, and it instantly unblocks the parser. If you prefer to keep the comma for daily use, you can change it back after the update completes — though many technicians simply leave the period in place permanently to avoid repeat encounters. For the Windows 11 variant of this error, including the System Reserved partition cleanup, see our [Windows 11 0x80070057 guide](/articles/how-to-fix-windows-update-error-0x80070057-on-windows-11/). Either way, verify the setting survived major updates, since feature updates occasionally reset regional customizations.

## Closing

On Windows 10, 0x80070057 is usually one of three things: the decimal symbol, corrupted update metadata, or a full System Reserved partition — in roughly that order of likelihood. Check the locale setting first, reset the cache, repair with DISM and SFC, and clear the reserved partition. The error's cryptic wording hides very fixable causes, and the in-place upgrade stands ready as the final backstop for the stubborn cases.
