---
title: "HP Laptop Stuck on 'Undoing Changes'? Fix the Update Rollback Loop"
slug: how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-hp-lapto
date: 2026-10-13
categories: ["windows-update"]
tags: ["undoing changes hp", "hp laptop update failed", "windows update hp", "hp support assistant", "undoing changes"]
description: "HP laptop stuck undoing Windows updates? Use HP Support Assistant, BIOS, and driver fixes to break the rollback loop."
thumbnail: "/images/thumbs/how-to-fix-windows-update-says-undoing-changes-made-to-your-computer-on-hp-lapto.webp"
faqs:
  - q: "Should I update drivers through HP Support Assistant or Windows Update?"
    a: "Use HP Support Assistant (or support.hp.com) for HP-specific drivers — BIOS, chipset, and HP utilities — since HP validates them for your exact model. Windows Update handles Microsoft components. Stale HP drivers are a leading rollback cause, so the HP-validated stack comes first, before retrying any failed update."
  - q: "Can HP BIOS updates fix Windows update rollbacks?"
    a: "Frequently. Windows 11 updates check firmware compatibility, and HP ships BIOS updates that explicitly improve Windows 11 update compatibility. An outdated BIOS can fail those checks silently and trigger the rollback. If your BIOS is a year or more behind, update it (plugged in, no interruptions) before the next update attempt."
  - q: "Why does my HP show a black screen during 'Undoing changes'?"
    a: "Some HP models with certain graphics drivers lose video output during the rollback phase while the rollback continues underneath — the power light and disk activity tell the real story. Wait it out if the drive is active. Only treat it as stuck after two-plus hours with zero disk activity, then force a restart."
  - q: "Does HP Wolf Security or Sure Sense block Windows updates?"
    a: "They can contribute. HP security tools with deep system hooks occasionally interfere with update file operations, similar to third-party antivirus. If rollbacks recur, temporarily disable HP Sure Sense real-time protection as a test, run the update, then re-enable. Keep the tools updated — newer builds fix these conflicts."
---

HP Pavilion, Envy, Spectre, and ProBook owners know this screen well: a Windows update fails and the laptop sits on **"Undoing changes made to your computer"** — sometimes for hours, sometimes in a loop that returns every Patch Tuesday. HP machines carry their own driver and firmware stack, and when that stack is stale, Windows updates cannot migrate it and roll back.

This guide works the HP layer first: HP Support Assistant updates, BIOS compatibility, and HP utility conflicts — then the standard rollback repairs. Generic guides skip the HP specifics; on an HP, the HP specifics are usually the fix.

Find your exact model or product number (bottom sticker or HP Support Assistant → My devices) before downloading anything — HP drivers are model-specific. For the HP-flavored "could not complete" variant, the [HP update-failure guide](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-hp-laptop/) pairs with this one.

## Why this happens

- **Outdated HP-validated drivers:** Chipset, storage, and system drivers older than the Windows build being installed.
- **Old HP BIOS failing compatibility checks:** Firmware predating Windows 11 update requirements.
- **HP Support Assistant / utility conflicts:** Outdated HP utilities colliding with update operations.
- **HP security tool interference:** Sure Sense or Wolf Security hooks blocking update file writes.
- **Corrupted update cache:** Damaged downloads failing integrity checks mid-install.
- **Insufficient disk space:** Tight SSDs on budget HP models hitting the space wall.
- **Failing storage underneath:** A struggling drive making update writes fail and triggering rollback.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update the HP stack with Support Assistant

Open HP Support Assistant → Updates and install everything, then cross-check at [HP support](https://support.hp.com/us-en) with your exact model for anything newer — especially BIOS, chipset, and storage drivers. HP validates these builds for your hardware; generic Windows drivers for HP-specific components are a classic migration failure. Finish the entire HP pass and restart before retrying Windows Update.

1. Open HP Support Assistant → Updates; install all offered items.
2. Verify at support.hp.com with your exact model number.
3. Prioritize BIOS, chipset, storage, and graphics.
4. Restart, then retry the Windows update.

### Fix 2: Update the HP BIOS correctly

Check your BIOS version (msinfo32) against the latest on the HP support page for your model. HP BIOS notes often mention Windows 11 compatibility explicitly. Download the BIOS update, close everything, stay plugged in with a charged battery, and run it — do not interrupt. A current BIOS clears the silent firmware-gate failures that cause rollbacks with no useful error code.

1. Compare your BIOS version against HP latest for your model.
2. Download the BIOS update from HP support.
3. Run it plugged in, charged, with all apps closed.
4. Confirm the new version, then retry the update.

### Fix 3: Clear the cache and repair the servicing stack

Now the Windows layer: run the Update troubleshooter, stop the Windows Update and BITS services, delete `C:\Windows\SoftwareDistribution\Download` contents, restart the services. Then elevated `DISM /Online /Cleanup-Image /RestoreHealth` and `sfc /scannow`. This pair fixes the corrupted-cache and damaged-component-store causes that strike HPs like any other PC.

1. Run the Windows Update troubleshooter.
2. Clear the SoftwareDistribution download cache.
3. Run DISM restore-health and SFC elevated.
4. Restart and retry the update.

### Fix 4: Test without HP security and utility interference

Temporarily disable HP Sure Sense real-time protection and non-essential HP startup utilities, then retry the update. If it succeeds, update the HP security tools and utilities to their latest builds before re-enabling — the conflict is usually fixed in newer versions. Document which component was the blocker; HP utility updates can reintroduce the conflict, and you will want the name.

1. Temporarily disable HP Sure Sense / Wolf real-time protection.
2. Disable non-essential HP startup items.
3. Retry the Windows update in this state.
4. Success: update the HP tools, then re-enable.

### Fix 5: Check the drive underneath the rollback

Repeated rollbacks with no clear software cause deserve a hardware look: check SMART health and Event Viewer for disk errors. On HPs with budget SSDs or aging HDDs, update write failures from a struggling drive trigger rollbacks that no driver update will fix. If the drive shows warnings, back up immediately — the rollback loop is the least of your problems; the drive is.

1. Check SMART data for warnings or reallocated sectors.
2. Search Event Viewer → System for disk errors.
3. Failing drive: back up now and replace it.
4. Healthy drive: continue with software repairs.

### Fix 6: Install the update manually from the catalog

Take the KB number from update history and install it by hand from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/). Manual installation sidesteps the automatic-pipeline timing issues where HP utility schedulers and Windows Update collide. Same-code manual failure means system state is the problem; manual success means the pipeline was.

1. Get the KB number from Update history.
2. Download the .msu from the Update Catalog.
3. Install manually and record the result.
4. Identical failure: move to the repair install.

### Fix 7: In-place upgrade with HP drivers ready

Back up, pre-download the latest HP driver pack for your model, then run the Windows 11 installer (Upgrade → keep files and apps). Install the HP drivers immediately after the repair, before Windows Update runs — so the fresh build never operates on stale HP drivers. This breaks the loop at its root and is the standard final answer for chronic HP rollback cases.

1. Back up personal files.
2. Pre-download the HP driver pack for your exact model.
3. Run the in-place upgrade, keeping files and apps.
4. Install HP drivers first thing post-repair; verify the update.

## Closing

On HP laptops the "Undoing changes" loop usually starts in the HP layer — stale HP drivers, an old BIOS, or a conflicting HP utility — so the fix starts at HP Support Assistant and support.hp.com. Update the HP stack and BIOS, clear the cache, test without interference, check the drive, install manually, and repair in place as the final step. Keep the HP stack current and the loop stays broken. For the general stuck-rollback procedure behind these HP steps, see the [undoing changes stuck in 24H2 guide](/articles/how-to-fix-undoing-changes-made-to-your-computer-stuck-in-windows-11-24h2/).
