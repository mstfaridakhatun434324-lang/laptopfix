---
title: "How to Fix Windows Update Error 0x800F0922 on an HP Laptop"
slug: how-to-fix-windows-update-error-0x800f0922-on-hp-laptop
date: 2026-09-28
categories: ["windows-update"]
tags: ["windows update", "0x800f0922", "hp laptop", "windows 11"]
description: "Error 0x800F0922 blocking updates on your HP laptop? It's usually the recovery partition, .NET, or Secure Boot. This HP-focused guide walks you through every fix."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0922-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x800F0922 mean on an HP laptop?"
    a: "It means CBS_E_INSTALLERS_FAILED: a component installer — most often the .NET Framework or the Windows Recovery Environment update — could not complete its work. On HP laptops the classic trigger is a recovery partition that is too small for the WinRE update to install into. The fixes below start with the small-partition check because it is the single most common cause on HP hardware."
  - q: "Why does HP's recovery partition cause this error?"
    a: "Some updates need to patch the Windows Recovery Environment, which lives on a small hidden partition. If that partition lacks roughly 250 MB of free space, the update installer aborts and Windows reports 0x800F0922. HP's factory partition layout is sometimes tight, so HP laptops hit this more often than average. Shrinking the main partition and extending the recovery one usually resolves it permanently."
  - q: "Is it safe to resize the recovery partition?"
    a: "Yes, if you follow the steps carefully and back up first. You shrink the Windows partition by a few hundred megabytes and give that space to the recovery partition using Disk Management or diskpart. Do not delete the recovery partition — only extend it. If you are uncomfortable with diskpart, HP support or a technician can do it, and the remaining fixes may clear the error without touching partitions."
  - q: "Can I skip the update that keeps failing?"
    a: "You can hide a specific failing update temporarily, but the WinRE security update behind most 0x800F0922 cases patches the recovery environment itself, so skipping it leaves a real gap. Better to fix the underlying partition or installer problem once; then the update installs cleanly and future updates stop tripping over the same failure."
---

Error 0x800F0922 translates to CBS_E_INSTALLERS_FAILED — one of the installers inside an update package gave up partway through. On HP laptops, this error has a famous trigger: the hidden Windows Recovery Environment partition is too small, so the WinRE security update (the KB5034441 family) has nowhere to install and the whole package aborts. It can also come from .NET Framework installers or Secure Boot conflicts, but the partition story is the one to check first.

Because this error is so often about disk layout rather than broken files, the fix order matters. Don't start with DISM — start by confirming whether the recovery partition is the bottleneck, then work through the installer-level repairs.

A word of reassurance: 0x800F0922 is a refused installation, not a destructive one. The failed update never modified your system, so there is nothing half-installed to clean up and no damage to undo. Every fix below is non-destructive — measuring partitions, reinstalling .NET, pausing antivirus, repairing the store — and the partition extension in Fix 2 is the only step that touches disk layout, with a backup reminder built in.

## Why this happens

- **The recovery partition is too small.** The WinRE update needs around 250 MB of free space on the recovery partition; HP factory layouts sometimes leave far less.
- **A .NET Framework installer fails inside the package.** Corrupted .NET payloads abort the cumulative update that carries them.
- **Secure Boot policy conflicts.** On some HP firmware revisions, the update's boot files clash with Secure Boot settings and the installer bails out.
- **Third-party antivirus hooks the installer.** Security software intercepting the .NET or WinRE installer can cause it to fail silently.
- **Corrupted component store.** Damaged installer metadata makes Windows attempt the install with broken instructions.
- **Insufficient free space on the system drive.** Even outside the recovery partition, a nearly-full C: drive can starve the installer of working space.
- **A previously interrupted update.** A half-applied package leaves the installer state machine confused on the next attempt.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the recovery partition's free space

This diagnosis decides the whole repair path.

1. Open Command Prompt as administrator and run `reagentc /info` — note the disk and partition numbers of the Windows RE location.
2. Run `diskpart`, then `list disk`, `select disk 0` (use the right disk number), `list partition`, and `select partition N` for the recovery partition.
3. Run `detail partition` and check its size and free space. If free space is well under 250 MB, the partition is your problem — continue to Fix 2. If it's generous, skip to Fix 3.

### Fix 2: Extend the recovery partition

Give the WinRE update the room it needs.

1. Back up important files first — partition work is low-risk but not zero-risk.
2. Open **Disk Management** (`diskmgmt.msc`), right-click the C: partition, and choose **Shrink Volume**; shrink by about 500 MB.
3. In `diskpart`, select the recovery partition and run `extend` (this works when the unallocated space sits directly after it; you may need to delete and recreate the recovery partition following Microsoft's documented sequence if it doesn't).
4. Run `reagentc /enable` to confirm the recovery environment still works, then retry Windows Update.

### Fix 3: Repair the .NET Framework installation

If the partition is fine, the .NET installer inside the package is the next suspect.

1. Open **Control Panel > Programs > Programs and Features > Turn Windows features on or off**.
2. Uncheck **.NET Framework 3.5** and **.NET Framework 4.8 Advanced Services**, click OK, and restart.
3. Re-open the same dialog, re-check both features, and let Windows reinstall them cleanly.
4. Retry the update. If .NET was the broken installer, the package now completes. HP-specific .NET tooling can also be refreshed via the [HP support site](https://support.hp.com/us-en) if you prefer HP's channel.

### Fix 4: Disable third-party antivirus temporarily

Security software hooking installers is a classic 0x800F0922 accomplice.

1. Temporarily disable real-time protection in your third-party antivirus (keep Windows Defender's status in mind — Windows enables its own protection automatically).
2. Retry the failing update immediately while protection is paused.
3. Re-enable your antivirus right after the test, pass or fail.
4. If the update succeeded, add an exclusion for the Windows Update process or switch that vendor's "installer protection" feature off before future update runs.

### Fix 5: Run DISM and SFC to repair installer metadata

Corrupted manifests make installers fail even when the disk layout is fine.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` and let it finish.
2. Follow with `sfc /scannow` and restart.
3. If you want background on these tools, Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents the recommended order.
4. Retry the update. If it still fails with the same code, the failure is almost certainly the partition (Fix 2) or a specific package needing manual install.

### Fix 6: Install the update manually from the Catalog

Bypass the automatic installer path for the stubborn package.

1. Find the failing KB number in **Settings > Windows Update > Update history**.
2. Download the matching x64 package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the `.msu` and let the standalone installer complete; it uses a simpler path that often succeeds where the orchestrated install failed.
4. Restart and confirm in Update history that the KB now shows as installed.

### Fix 7: Run Microsoft's .NET Framework Repair Tool

When the .NET toggle in Fix 3 doesn't fully clear the installer failure, use Microsoft's dedicated repair utility.

1. Download the **Microsoft .NET Framework Repair Tool** from Microsoft's website and run it as administrator.
2. Let it detect and repair .NET installation problems automatically, applying every recommended fix.
3. Restart the laptop when the tool finishes, even if it says no problems were found — it also re-registers installer components.
4. Retry the failing Windows update; with .NET's installer stack repaired by its own tool, the package's internal installer completes.

## Closing

On HP laptops, 0x800F0922 is the recovery-partition error far more often than a true system corruption, so the partition check in Fix 1 saves the most time. For the non-HP walkthrough of the same code, see the [step-by-step 0x800F0922 guide](/articles/how-to-fix-windows-update-error-0x800f0922-step-by-step/), and if your failure is the "element not found" [0x80070490](/articles/how-to-fix-windows-update-error-0x80070490-on-hp-laptop/) instead, that guide's metadata repairs are the right starting point.
