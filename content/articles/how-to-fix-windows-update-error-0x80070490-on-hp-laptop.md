---
title: "How to Fix Windows Update Error 0x80070490 on an HP Laptop"
slug: how-to-fix-windows-update-error-0x80070490-on-hp-laptop
date: 2026-09-26
categories: ["windows-update"]
tags: ["windows update", "0x80070490", "hp laptop", "windows 11"]
description: "Error 0x80070490 on your HP laptop means Windows Update hit an 'element not found' snag. Here is an HP-focused fix sequence, from Support Assistant to component-store repair."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070490 mean on an HP laptop?"
    a: "It is the ERROR_NOT_FOUND code: Windows Update expected a file, registry entry, or package element to exist and it did not. On HP laptops the trigger is often a half-installed HP driver update, a corrupted component store, or a failed feature update. The fixes walk from HP's own tools through Microsoft's system repair utilities, so you cover both the HP-specific and the general causes."
  - q: "Can HP Support Assistant fix Windows Update errors?"
    a: "Sometimes. HP Support Assistant updates HP drivers, BIOS, and firmware through its own channel, which can clear a driver update that Windows Update keeps failing on. It does not repair the Windows component store, though. Treat it as a useful first pass: let it install pending HP updates, restart, and then retry Windows Update before moving to heavier repairs."
  - q: "Should I update the BIOS on my HP laptop to fix this?"
    a: "Only if a BIOS update is pending and directly relevant — a failing BIOS update package can leave residue that confuses Windows Update. Use HP Support Assistant or the official [HP support site](https://support.hp.com/us-en) to check, keep the charger connected during any BIOS flash, and never interrupt it. Do not flash the BIOS speculatively if none is pending; it adds risk without benefit."
  - q: "Will a Windows reset delete my files?"
    a: "A reset that keeps your files preserves your personal data but removes installed programs and HP utilities, which you would reinstall afterward. Use it only after every other fix has failed, back up anything irreplaceable first, and prefer the cloud-download option so the reset itself uses fresh Windows files rather than a possibly damaged local image."
---

Error 0x80070490 is the "element not found" of Windows Update: somewhere in the install chain, Windows reached for a file or package element that simply wasn't there. On HP laptops the pattern is familiar — a driver update (often a Realtek audio, Intel graphics, or HP firmware package) fails halfway, and every subsequent update attempt trips over the wreckage with the same code.

The fix path is a little different on HP hardware because there are two update channels fighting for the same drivers: Microsoft's and HP's. When they disagree — HP pushes a driver through Support Assistant while Windows Update tries the same one — the result is exactly this kind of phantom failure. Start with the HP-specific checks, then move to the standard Windows repair stack.

From a technician's bench perspective, this is a routine repair rather than a crisis. The error code is precise about what's wrong — a referenced element is absent — which narrows the search enormously compared to vaguer update failures. None of the fixes below risk your files: they repair metadata, refresh the component store, and reinstall packages, all non-destructive operations. The only step that touches your data at all is the optional reset near the end, and it is clearly marked as a last resort.

## Why this happens

- **A half-installed driver update.** The most common cause: a driver package registered as "installing" but missing its payload, so every retry finds the expected element gone.
- **Conflict between HP Support Assistant and Windows Update.** Both channels can offer the same driver; installing one while the other is mid-flight corrupts the update metadata.
- **Component store corruption.** Damage in the WinSxS store leaves update manifests pointing at files that no longer exist.
- **A failed or interrupted feature update.** Power loss or a forced shutdown during a big update leaves package elements in limbo.
- **Corrupted SoftwareDistribution cache.** Stale or partial download metadata makes Windows believe a package is present when it isn't.
- **Pending BIOS or firmware updates in a bad state.** HP firmware packages that stalled can block the whole queue behind them.
- **Third-party driver updaters.** External tools that yank drivers outside Windows Update create exactly the missing-element scenario 0x80070490 reports.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which update is failing

A targeted fix starts with knowing the exact package.

1. Open **Settings > Windows Update > Update history** and find the entry that failed with 0x80070490; note its KB number and whether it's a driver, quality, or feature update.
2. If it's a driver update, open **Device Manager**, find that device, and check whether it currently works — a working device with a failed update entry points at metadata, not hardware.
3. If it's a feature update, note the target version; you'll need it if a manual install becomes necessary later.

### Fix 2: Let HP Support Assistant finish its queue first

Clear the HP channel before touching Microsoft's, so the two stop colliding.

1. Open **HP Support Assistant** (search for it in the Start menu; install it from the [HP support site](https://support.hp.com/us-en) if it's missing).
2. Run a full check and install every pending HP driver, BIOS, and firmware update it offers — keep the laptop plugged in throughout.
3. Restart when prompted, even if HP says it's optional.
4. Go to **Settings > Windows Update** and retry. If the failing driver was HP's, this often clears the error by itself.

### Fix 3: Run the Windows Update troubleshooter

Microsoft's troubleshooter is good at resetting the metadata that produces "element not found."

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow every prompt, including the offer to apply automatic fixes.
3. Restart the laptop and check for updates again. This resolves the error when the cause is purely stale metadata.

### Fix 4: Repair the component store with SFC and DISM

Missing elements usually live in the component store, so repair it directly.

1. Open Command Prompt as administrator and run `sfc /scannow`; let it finish and restart.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` in the same elevated prompt — this re-downloads clean copies of damaged store files from Windows Update.
3. Run `sfc /scannow` once more after DISM completes to confirm everything is clean.
4. Retry the update. DISM is also the right tool when the sibling walkthrough for [fixing 0x80070490 step by step](/articles/how-to-fix-windows-update-error-0x80070490-step-by-step/) is needed on a non-HP machine.

### Fix 5: Reset the Windows Update components

If the store is healthy but the cache still references phantom packages, wipe the cache.

1. In an administrator Command Prompt, run `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Check for updates — Windows rebuilds fresh metadata, and the phantom failure entry disappears.

### Fix 6: Install the failing update manually

When automatic installation keeps tripping on the same package, bypass the broken chain.

1. Look up the KB number you noted in Fix 1 at the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) and download the package matching your architecture (x64 for almost all HP laptops).
2. Double-click the downloaded `.msu` file and let the standalone installer run.
3. If it's a driver, consider hiding it instead: install the correct driver directly from HP, then use Microsoft's "show or hide updates" troubleshooter to hide the failing driver entry so Windows Update stops retrying it.

### Fix 7: Reinstall the specific driver from HP's site

When one HP driver package is the corrupted element, replace it at the source rather than fighting the metadata.

1. In Device Manager, identify the device tied to the failing driver update you noted in Fix 1.
2. Go to the [HP support site](https://support.hp.com/us-en), enter your exact model, and download that specific driver.
3. In Device Manager, right-click the device and choose **Uninstall device**; install the freshly downloaded HP driver afterward.
4. Use Microsoft's "show or hide updates" troubleshooter to hide the failing Windows Update driver entry so the bad metadata stops resurfacing, then run a final update check.

## Closing

On HP laptops, 0x80070490 is usually a tug-of-war between HP's and Microsoft's update channels or a driver package left half-installed, and working through the HP queue first clears most cases. For the generic, non-HP version of the same error, see the [step-by-step 0x80070490 guide](/articles/how-to-fix-windows-update-error-0x80070490-step-by-step/), and if your error code is different — especially the service-disabled [0x80070422](/articles/how-to-fix-windows-update-error-0x80070422-step-by-step/) — match the code to its own guide rather than forcing these fixes.
