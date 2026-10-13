---
title: "How to Fix Windows Update Error 0x800F0922 Step by Step"
slug: how-to-fix-windows-update-error-0x800f0922-step-by-step
date: 2026-09-29
categories: ["windows-update"]
tags: ["windows update", "0x800f0922", "winre", "windows 11"]
description: "Error 0x800F0922 means an installer inside the update package failed. This step-by-step guide covers the recovery-partition check, .NET repair, and manual install."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0922-step-by-step.webp"
faqs:
  - q: "What is the most common cause of error 0x800F0922?"
    a: "A recovery partition with too little free space. The Windows Recovery Environment update needs roughly 250 MB of free space on the hidden recovery partition, and many factory partition layouts fall short. When the installer cannot fit the WinRE payload, it aborts the whole package and Windows reports 0x800F0922. Checking partition space first saves hours of misdirected repairs."
  - q: "Does 0x800F0922 mean my .NET Framework is broken?"
    a: "Not necessarily, but it is the second most common cause. The code means one of the package's internal installers failed, and the .NET installer is a frequent offender when the recovery partition is fine. The toggling repair in Fix 3 reinstalls .NET cleanly and resolves this variant. If both the partition and .NET check out, move on to antivirus and component-store checks."
  - q: "Can Secure Boot really block a Windows update?"
    a: "Rarely, but it happens. Some updates include boot-environment files that must satisfy Secure Boot policy; on certain firmware revisions the check fails and the installer aborts with 0x800F0922. This is uncommon on mainstream laptops with current firmware. Only investigate Secure Boot after the partition, .NET, antivirus, and component-store causes are ruled out."
  - q: "Will extending the recovery partition erase my data?"
    a: "Extending the partition into adjacent free space does not touch your files, but any partition operation carries some risk, so back up first. The procedure shrinks the Windows partition slightly and gives that space to the recovery partition. Never delete the recovery partition itself — the goal is more room for it, not its removal."
---

Error 0x800F0922 means CBS_E_INSTALLERS_FAILED: Windows Update assembled the package correctly, but one of the installers inside it — usually the Windows Recovery Environment updater or the .NET Framework installer — failed to do its job. The update aborts, and you're left with a code that says nothing about which installer broke.

The good news is that this error has a short list of usual suspects, and the most common one is checkable in two minutes. The sequence below is ordered by likelihood: verify the recovery partition space first, then repair .NET, then rule out antivirus and store corruption, and finally install the package by hand.

Keep in mind that the failed update never actually installed anything — 0x800F0922 is Windows declining to proceed, not Windows breaking something mid-install. That means there's no wreckage to clean up and no risk of making things worse with these repairs. Test the update after each fix so you know exactly which step resolved it, which also tells you what to watch for next time.

## Why this happens

- **Too little free space on the recovery partition.** The WinRE update needs about 250 MB free; factory layouts often leave much less, and the installer aborts.
- **A failing .NET Framework installer.** Damaged .NET payloads inside a cumulative update drag the whole package down with them.
- **Third-party antivirus intercepting the installer.** Security hooks on the .NET or WinRE installer cause silent failures.
- **Secure Boot policy conflicts.** Rare firmware-level clashes with the update's boot files abort the install.
- **Component store corruption.** Broken installer manifests produce install attempts that cannot succeed.
- **A nearly-full system drive.** The installer needs working space on C: beyond the recovery partition's needs.
- **Residue from an interrupted update.** A half-applied package leaves the installer state machine confused.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure the recovery partition's free space

Two minutes here determines everything that follows.

1. Open an administrator Command Prompt and run `reagentc /info` to find the disk and partition hosting Windows RE.
2. Launch `diskpart`, then `list disk`, `select disk 0`, `list partition`, and `select partition N` for the recovery partition; run `detail partition`.
3. If free space is comfortably above 250 MB, the partition is innocent — skip to Fix 3. If it's tight, proceed to Fix 2.
4. Also glance at C:'s free space in File Explorer while you're at it; under 10 GB free on the system drive causes its own installer failures.

### Fix 2: Give the recovery partition more room

This is the permanent fix for the most common variant.

1. Back up your important files — partition edits are safe when done right, but backups are cheap insurance.
2. Open `diskmgmt.msc`, right-click the Windows (C:) partition, choose **Shrink Volume**, and shrink by roughly 500 MB.
3. In `diskpart`, select the recovery partition and run `extend` to absorb the adjacent free space. If the layout won't allow a direct extend, Microsoft's documented approach is to disable WinRE, delete and recreate the partition larger, then re-enable it.
4. Run `reagentc /enable` to verify WinRE works, then retry Windows Update.

### Fix 3: Reinstall the .NET Framework cleanly

The second most likely broken installer gets a fresh start.

1. Open **Control Panel > Programs > Turn Windows features on or off**.
2. Uncheck **.NET Framework 3.5** and **.NET Framework 4.8 Advanced Services**, click OK, and restart the laptop.
3. Return to the same dialog, re-check both, and let Windows fetch clean copies.
4. Retry the failing update; a repaired .NET installer lets the package complete normally.

### Fix 4: Pause third-party antivirus during the install

Installer interception is invisible until you test for it.

1. Temporarily turn off real-time protection in your third-party antivirus (Windows Security steps in automatically).
2. Immediately retry the failing update while protection is paused.
3. Re-enable protection afterward regardless of the outcome.
4. If the update went through, create an exclusion for the update installer or disable the vendor's installer-shielding feature before future updates.

### Fix 5: Repair the component store

When installers fail for no visible reason, their manifests may be damaged.

1. Run `DISM /Online /Cleanup-Image /RestoreHealth` in an administrator Command Prompt and wait for completion.
2. Run `sfc /scannow` afterward and restart.
3. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents these tools in detail if you want the background.
4. Retry the update; a healthy store gives the installers valid instructions to follow.

### Fix 6: Install the package manually

If the automatic path keeps failing on one package, use the standalone installer.

1. Copy the failing KB number from **Settings > Windows Update > Update history**.
2. Download the x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run it and let the simpler standalone path complete the install.
4. Confirm success in Update history, then run a normal check for updates to make sure the queue is clear.

### Fix 7: Perform an in-place upgrade as the final repair

If the partition is roomy, .NET is clean, and the package still fails, rebuild the whole servicing stack with an in-place upgrade.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it by double-clicking.
2. Run `setup.exe`, accept the license terms, and choose **Keep personal files and apps** on the "Choose what to keep" screen.
3. Let the upgrade run its course — 30 to 90 minutes, several restarts, laptop plugged in, no interruptions.
4. After signing in, check for updates; the fresh servicing stack installs the previously failing package without the installer abort.

## Closing

Error 0x800F0922 rewards diagnosis over brute force: the recovery-partition check takes minutes and resolves the most common case outright. For HP-specific angles like Support Assistant conflicts, see the [HP laptop version of this guide](/articles/how-to-fix-windows-update-error-0x800f0922-on-hp-laptop/), and if your code is the component-store [0x80073712](/articles/how-to-fix-windows-update-error-0x80073712-step-by-step/) rather than an installer failure, that guide's DISM-centered sequence is the right one.
