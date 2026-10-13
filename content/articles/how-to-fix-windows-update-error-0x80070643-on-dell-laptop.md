---
title: "How to Fix Windows Update Error 0x80070643 on a Dell Laptop"
slug: "how-to-fix-windows-update-error-0x80070643-on-dell-laptop"
date: 2026-09-24
categories: ["windows-update"]
tags: ["windows update", "0x80070643", "winre", "kb5034441", "dell laptop"]
description: "Error 0x80070643 on a Dell laptop is usually the WinRE update (KB5034441) failing for lack of recovery partition space. Fix it by resizing WinRE or hiding the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070643-on-dell-laptop.webp"
faqs:
  - q: "What is KB5034441 and why does it keep failing?"
    a: >
      It is a security update for the Windows Recovery Environment that
      requires about 250 MB of free space in the hidden recovery
      partition. Many Dell laptops shipped with smaller recovery
      partitions, so the update fails with 0x80070643 regardless of how
      much free space your C: drive has.
  - q: "Is it safe to hide KB5034441?"
    a: >
      For most home users, yes. Microsoft provides the official
      hide-updates troubleshooter for exactly this situation. Your main
      Windows installation still receives all normal security updates;
      only the recovery environment stays at its current patch level.
      Since WinRE is used rarely — mainly for emergency recovery — running
      a slightly older version carries minimal practical risk for typical
      home use.
  - q: "Will resizing the recovery partition delete my data?"
    a: >
      Not if done correctly — you shrink the OS partition to create free
      space, then recreate a larger recovery partition. Still, back up
      important files first, because any partition operation carries some
      risk if power is lost mid-way. Keep the laptop plugged into AC power
      throughout, and do not interrupt the process. Thousands of users
      have performed this exact Microsoft-documented procedure without
      data loss.
  - q: "Does this error mean my Dell laptop is failing?"
    a: >
      No. This is a servicing and disk-layout issue, not hardware failure.
      Your SSD and motherboard are fine; the update simply needs more room
      in a hidden partition than the factory layout provided. It is one of
      the most widely reported Windows update issues of recent years and
      affects perfectly healthy machines. Fix the partition size or hide
      the update, and the error goes away for good.
---

Error 0x80070643 (ERROR_INSTALL_FAILURE) on Dell laptops is overwhelmingly tied to one specific update: the Windows Recovery Environment servicing update, KB5034441. That update needs roughly 250 MB of free space in the recovery partition to install, and on many Dell machines — particularly those shipped with Windows 10 and later upgraded — the recovery partition was created too small. The update fails at install time with 0x80070643 no matter how many times you retry.

This is a well-documented Microsoft issue, not a quirk of your machine. The recovery partition is hidden from File Explorer, which is why the failure is confusing: your C: drive can have hundreds of gigabytes free while the tiny partition the update actually needs is full. The permanent fix is to shrink the OS partition slightly and extend the recovery partition, then let the update run again.

If you do not use the Windows Recovery Environment, Microsoft also supports simply hiding KB5034441 with the official ‘show or hide updates’ troubleshooter. Both approaches are covered below, starting with diagnosis so you can confirm the recovery partition is the cause. If you are dealing with a related symptom instead, see [the disk-full 0x80070070 error](/articles/how-to-fix-windows-update-error-0x80070070-on-dell-laptop/) and [KB5034441 failing to install on Dell](/articles/how-to-fix-kb5034441-not-installing-on-dell-laptop/).

If the update history page shows KB5034441 failing over and over while every other update installs normally, you have the textbook version of this problem — and the good news is that it is one of the best-documented update failures in recent Windows history. Microsoft has published the exact partition-resize procedure, and the hide-updates troubleshooter gives you a supported way to skip it. Either path takes under an hour, and the steps below walk you through diagnosing first so you pick the right one.

## Why this happens

- **Recovery partition too small** KB5034441 needs ~250 MB free in the WinRE partition; older Dell images allocated less.

- **WinRE partition nearly full** staged files and old recovery images consume the little space it has.

- **Corrupt WinRE image** a damaged winre.wim causes the servicing step to fail outright.

- **BitLocker-encrypted OS volume** encryption complicates the partition resize needed for the real fix.

- **Third-party disk tools moved partitions** resizing utilities can orphan the recovery partition’s free space.

- **Pending restart blocking the installer** a stuck reboot state makes the WinRE update fail its pre-checks.

- **Outdated servicing stack** an old servicing stack update can mis-handle the WinRE payload.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the failing update is KB5034441

Before resizing partitions, verify this is the WinRE update and not a different 0x80070643 failure. This two-minute check decides your whole strategy: the WinRE partition fix only applies to KB5034441, while a .NET failure needs the repair approach in Fix 6.

1. Open Settings > Windows Update > Update history.

2. Look for the failed entry — check whether its KB number is KB5034441.

3. If it is a different KB (often a .NET update), skip to Fix 6.

4. Also note the error code shown next to it to confirm 0x80070643.

### Fix 2: Check the recovery partition size

Seeing the actual free space proves the diagnosis before you touch disk layout. Take a screenshot of Disk Management before changing anything — having the original layout documented makes every later step safer and reversible.

1. Open Command Prompt as administrator and run: reagentc /info to confirm WinRE is enabled.

2. Open Disk Management (right-click Start).

3. Find the Recovery partition — note its total size and layout position.

4. If it is around 500–600 MB with little free, it is the cause.

### Fix 3: Extend the recovery partition (the permanent fix)

Microsoft’s documented fix: shrink the OS partition by 250 MB and give that space to the recovery partition. This is Microsoft’s own documented procedure for the KB5034441 failure, so you are following the official playbook rather than improvising with partitions.

1. If BitLocker is on, suspend it first (manage-bde -protectors -disable C:).

2. In Disk Management, shrink the C: partition by 250–500 MB.

3. Use diskpart to delete the old recovery partition and create a new, larger one in the freed space — follow Microsoft’s KB5034441 guidance step by step.

4. Re-enable the recovery agent with: reagentc /enable.

5. Run: reagentc /info to confirm WinRE is enabled with the new partition.

6. Retry Windows Update — KB5034441 should now install.

### Fix 4: Hide KB5034441 if you do not need WinRE updates

Microsoft officially supports skipping this update on machines where resizing is impractical. You can reverse this any time by running the troubleshooter again and choosing ‘Show hidden updates’ if you later enlarge the recovery partition.

1. Download the ‘Show or hide updates’ troubleshooter (wushowhide.diagcab) from Microsoft support.

2. Run it, click Next, then choose ‘Hide updates’.

3. Select KB5034441 from the list and finish the wizard.

4. Windows Update will stop offering it, and 0x80070643 disappears.

5. Remember WinRE stays at its current patch level — acceptable for most home users.

### Fix 5: Repair a corrupt WinRE image

If the partition has space but the update still fails, the winre.wim itself may be damaged. A healthy reagentc /info report — showing WinRE as enabled with a valid location — is the confirmation that this fix actually worked.

1. Run: reagentc /disable in an elevated Command Prompt.

2. Run: reagentc /enable to rebuild the WinRE configuration.

3. Verify with: reagentc /info.

4. Retry the update from Settings > Windows Update.

### Fix 6: Fix 0x80070643 on non-WinRE updates

The same code also appears on .NET Framework updates, where the cause is usually a corrupt .NET install. The .NET repair tool is a small download from Microsoft that fixes the framework’s installation state without touching your applications or their data.

1. Open Settings > Apps > Installed apps and find Microsoft .NET entries.

2. Use the .NET Framework Repair Tool from Microsoft support.

3. Alternatively, run: DISM /Online /Cleanup-Image /RestoreHealth then sfc /scannow.

4. Restart and retry the update.

### Fix 7: Update Dell firmware and retry

Dell occasionally ships BIOS and storage firmware fixes that affect partition handling during updates. Install Dell’s updates before retrying Windows Update, since a firmware fix can change how the recovery partition behaves during servicing.

1. Go to [Dell’s support site](https://www.dell.com/support) and enter your service tag.

2. Install any pending BIOS, chipset, or storage firmware updates.

3. Restart the laptop.

4. Run Windows Update again and confirm KB5034441 (or the .NET update) installs.

## Closing

For most Dell owners, 0x80070643 is the KB5034441 recovery-partition problem and nothing more. Extending the partition is the proper permanent fix, while hiding the update is the pragmatic shortcut Microsoft itself blesses. Either way, the error should be gone after one focused session. For official guidance, see [Microsoft’s Windows update support hub](https://support.microsoft.com/en-us/windows).
