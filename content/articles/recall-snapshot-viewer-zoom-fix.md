---
title: "How to Fix Recall Snapshot Viewer Zoom Not Working on Your Copilot+ PC"
slug: recall-snapshot-viewer-zoom-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["recall", "snapshot viewer", "zoom", "copilot+ pc", "windows 11", "troubleshooting"]
description: "Fix Recall snapshot viewer zoom not working on your Copilot+ PC with checks for display scaling, graphics drivers, Recall settings, and damaged snapshots."
thumbnail: "/images/thumbs/recall-snapshot-viewer-zoom-fix.webp"
faqs:
  - q: "Why does zoom not work in the Recall snapshot viewer?"
    a: "Zoom usually fails because of a display scaling conflict, an outdated graphics driver, a disabled Recall feature, or a damaged snapshot. Check scaling and the driver first, then verify that Recall is fully enabled and the snapshot itself opens correctly."
  - q: "Does display scaling affect Recall zoom?"
    a: "Yes. Custom scaling above 100 percent, or a scaling change after Recall captured a snapshot, can break pinch and button zoom. Reset scaling to the recommended value, sign out and back in, and test the same snapshot again."
  - q: "Can I zoom a snapshot that is blurry or incomplete?"
    a: "No. Zoom only enlarges what was captured. If the snapshot is blurry, incomplete, or shows a placeholder, recapture the activity and open the new snapshot instead of trying to repair the old one."
  - q: "Will resetting Recall delete my snapshots?"
    a: "Resetting Recall settings does not automatically delete saved snapshots, but clearing snapshot data will. Back up anything important and use the gentler fixes in this guide before you choose any option that deletes data."
---

You open a Recall snapshot to read small text, try to zoom in, and nothing happens. The zoom buttons are greyed out, pinch gestures do nothing, or the view jumps back to full-page size the moment you release it. The snapshot itself may look fine — the viewer just refuses to magnify it.

On a Copilot+ PC, Recall zoom depends on more than the viewer window. It relies on display scaling, the graphics driver, the NPU-backed Recall service, and the integrity of the snapshot file. If any one of those layers is out of step, zoom can fail while the rest of Recall appears to work normally.

This guide walks you through six fixes in order, from quick settings checks to a clean Recall reset. Work through them in sequence and test the same snapshot after each step, so you know exactly which fix restored zoom.

## Why this happens

- **Display scaling conflict:** A custom scaling value, a second monitor with different scaling, or a scaling change since the snapshot was taken can confuse the viewer's zoom calculations.
- **Outdated or generic graphics driver:** Recall renders snapshots through the GPU pipeline, so a generic driver can break zoom, panning, and rendering even when normal windows look fine.
- **Recall paused or partly disabled:** If Recall is paused, snapshots are still listed but the viewer may run in a limited mode where zoom and related controls are unavailable.
- **Corrupted or incomplete snapshot:** An interrupted capture, a disk error, or a failed NPU processing step can leave a snapshot that opens but cannot be zoomed or rendered at higher detail.
- **Touchpad and gesture settings changed:** Disabled pinch-to-zoom, a changed touchpad driver, or a conflicting mouse utility can block gesture zoom while button zoom still works — or block both.
- **Windows display component fault:** A damaged Windows shell or display component, often after a failed update, can break viewer controls across Recall and other apps. Similar viewer and rendering faults appear in [Copilot+ display and NPU problems](/articles/npu-driver-error-code-38-fix/), where a driver fault blocks more than one feature at once.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reset display scaling to the recommended value

Scaling is the fastest check and the most common cause. If your scaling is custom or mismatched across monitors, the viewer cannot calculate zoom levels correctly, so it disables them.

1. Open **Settings > System > Display** and note the current **Scale** value.
2. Set Scale to the value marked **(Recommended)**, usually 100 percent on a laptop panel.
3. If you use an external monitor, set each display to its own recommended scaling rather than forcing one value everywhere.
4. Sign out of Windows and sign back in so every app reloads with the new scaling.
5. Open the same Recall snapshot and test both the zoom buttons and pinch gestures.

### Fix 2: Confirm Recall is fully enabled and not paused

A paused or partly disabled Recall service can leave snapshots visible but functionally limited. This check rules out a policy or settings problem before you touch drivers or data.

1. Open **Settings > Privacy & security > Recall & snapshots** and confirm Recall is turned **On**.
2. Check that snapshot saving is not paused and that filtering has not blocked the app shown in the snapshot.
3. Confirm you have free disk space, since Recall stops processing new snapshots when storage is critically low.
4. Close the Recall viewer completely, reopen it from the timeline, and test zoom on a recent snapshot.
5. If zoom works on new snapshots but not old ones, the older snapshots may be damaged — move to Fix 5 for those specific items.

### Fix 3: Update the graphics driver from your laptop maker

A generic Windows graphics driver is a frequent hidden cause of viewer problems. Your laptop maker's validated driver matches the panel, the NPU, and the Recall pipeline in a way a generic driver does not.

1. Open **Device Manager > Display adapters** and check whether a generic driver is listed instead of your maker's GPU.
2. Note your exact model in **Settings > System > About**, then download the latest graphics driver from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
3. Install the driver as administrator and allow the installer to finish without putting the PC to sleep.
4. Restart the PC, then open Recall and test zoom on the same snapshot.
5. If Windows Update later replaces the driver again, check Microsoft's Windows support pages for how to keep the maker's driver in place.

### Fix 4: Repair touchpad gestures and test button zoom separately

Gesture and button zoom can fail independently, and separating them tells you whether the problem is input or rendering. This step also catches utility software that hijacks pinch gestures.

1. In the Recall viewer, try the on-screen zoom buttons or **Ctrl + Plus** and **Ctrl + Minus** before using any gesture.
2. If button zoom works but pinch does not, open **Settings > Bluetooth & devices > Touchpad** and confirm pinch-to-zoom is enabled.
3. Update or reinstall the touchpad driver from your laptop maker's support page.
4. Temporarily close mouse, gesture, and overlay utilities, then test pinch zoom again.
5. If neither method works, the fault is in rendering or the snapshot itself, not input — continue to the next fix.

### Fix 5: Test a fresh snapshot and clear a damaged one

A single damaged snapshot can make zoom look broken everywhere. Testing a fresh capture separates a viewer fault from bad snapshot data, which need very different fixes.

1. Open an app, do something distinctive, and wait for Recall to capture a new snapshot.
2. Open the new snapshot and test zoom immediately — if it works, the viewer is healthy.
3. For the broken snapshot, note its time and app, then try opening it after a restart to rule out a temporary rendering fault.
4. If it still will not zoom, delete only that snapshot from the Recall timeline rather than clearing all data.
5. Avoid bulk-deleting snapshots to fix one bad item; that removes useful history for no benefit. The same isolate-one-item approach helps when unrelated apps misbehave, as with [WhatsApp on ARM laptops](/articles/whatsapp-desktop-arm-laptop-fix/).

### Fix 6: Reset the Recall viewer and Windows display components

When zoom fails on every snapshot, including fresh ones, reset the feature layer rather than reinstalling Windows. This clears stale viewer state while keeping your snapshots where possible.

1. Close Recall, then open **Settings > System > Troubleshoot > Other troubleshooters** and run the available display and app troubleshooters.
2. In Recall settings, toggle Recall **Off**, restart the PC, then toggle it **On** again.
3. Run Windows Update and install any pending updates, then restart once more.
4. Open Recall, wait for it to finish loading the timeline, and test zoom on both an old and a new snapshot.
5. If zoom still fails everywhere, run **System File Checker** from an elevated terminal and, as a last resort, consider a Windows repair install — a step also worth trying when [Cocreator stops working offline](/articles/cocreator-offline-not-working/) after an update damages shared AI components.

## Closing

Recall zoom usually fails for an ordinary reason — scaling, a generic driver, a paused service, or one damaged snapshot — not because Recall itself is broken. Reset scaling, confirm Recall is fully on, update the maker's graphics driver, and test a fresh snapshot before resetting anything. That order finds the real fault fast and protects your snapshot history.
