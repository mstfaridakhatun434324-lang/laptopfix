---
title: "Can You Move Recall Snapshots to Another Drive? Options That Work"
slug: move-recall-snapshots-another-drive
date: 2026-10-22
categories: ["ai-pc"]
tags: ["move recall snapshots", "recall storage location", "windows recall disk", "recall another drive", "copilot plus pc", "windows 11"]
description: "Running out of space for Recall snapshots? Learn whether Windows lets you move them to another drive, plus the proven alternatives that free space safely."
thumbnail: "/images/thumbs/move-recall-snapshots-another-drive.webp"
faqs:
  - q: "Can I officially move Recall snapshots to the D: drive?"
    a: >
      No. Windows provides no supported way to relocate the Recall snapshot store. The supported controls are the storage allocation cap, retention settings, and deleting snapshots you do not need.
  - q: "What happens if my system drive fills up completely?"
    a: >
      Recall pauses snapshot capture to protect the system, and Windows itself becomes unstable. Keep at least 25–50 GB free on the system drive at all times on a Copilot+ PC.
  - q: "Do deleted Recall snapshots free space immediately?"
    a: >
      Yes, once deletion completes. On a large store the cleanup can take several minutes — let it finish before judging free space, and do not reboot mid-delete.
  - q: "Will a bigger allocation make Recall work better?"
    a: >
      A bigger allocation only means longer history, not better capture. If space is tight, a smaller allocation with shorter retention gives you the useful recent history without the disk pressure.
---

Recall's snapshot storage grows relentlessly — every few seconds, another screenshot lands on your system drive. On a 256 GB or 512 GB laptop with a second drive or a roomy D: partition, the obvious question is: can I just move the snapshots somewhere else?

Here is the honest answer up front: Windows does not offer an official way to relocate Recall's snapshot store to another drive. The storage location is fixed by design, tied to the encryption and security model that keeps snapshots private. Anyone promising a registry hack to move it is selling risk — the same kind of risky unofficial tweak that causes [Studio Effects NPU unavailable errors](/articles/studio-effects-npu-unavailable-error/) when NPU driver files get relocated by hand.

This guide covers what you actually can do: shrink what Recall stores, free the system drive properly, and use the supported storage controls. Six fixes that solve the space problem without breaking Recall's security model.

## Why this happens

- **Snapshot store pinned to the system drive:** Recall keeps its encrypted database on the Windows drive by design — encryption keys and access controls assume that location, which is why [storing Recall snapshots on an external drive](/articles/recall-snapshots-external-drive/) is not a supported configuration either.
- **Fixed storage allocation, not a movable folder:** What you can change is how much space Recall may use, not where it uses it. The allocation slider is the official control.
- **Small system drives filling fast:** 256 GB drives can feel the pinch quickly when Recall's allocation plus apps plus OneDrive local copies stack up.
- **Old snapshots never expiring:** If retention is set too generously, months of snapshots accumulate — storage that could simply be aged out.
- **Duplicate data from other features:** Storage Sense, hibernation files, and old Windows installations compete for the same gigabytes Recall wants.
- **Misunderstanding the allocation setting:** Many users do not realize the allocation cap exists, so Recall keeps its default reservation while they hunt for a move option that is not there.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Accept the constraint — then use the allocation control

The supported lever is how much space Recall may use. Set it deliberately instead of leaving the default.

1. Open **Settings > Privacy & security > Recall & snapshots** and find the snapshot storage allocation.
2. Lower the allocation to a value that fits your drive — on 256 GB machines, a modest allocation is the pragmatic choice.
3. Confirm the change; Recall will age out the oldest snapshots to fit the new cap.
4. Monitor free space over the next week to confirm the pressure is gone.

### Fix 2: Delete snapshots you do not need

The fastest way to reclaim space is to throw away history you will never search. Be deliberate, not indiscriminate.

1. Open Recall and delete snapshots from date ranges you know are uninteresting — old work trips, idle weekends.
2. For a full reset, delete all snapshots from Recall settings. The timeline restarts fresh from today.
3. Remember deleted snapshots are unrecoverable — but so is the disk space they were occupying.
4. After deleting, verify free space actually increased in **Settings > System > Storage**.

### Fix 3: Tighten retention so the store stops growing

Retention settings decide how long snapshots live. Shorter retention means a smaller steady-state store.

1. In Recall settings, review the snapshot retention or storage duration options available on your build.
2. Choose the shortest retention you are comfortable with — 30 days is plenty for most people's actual recall needs.
3. Combine this with the allocation cap from Fix 1: retention controls age, allocation controls size.
4. Check back in a month; the store should now plateau instead of growing.

### Fix 4: Free the system drive properly

Recall competes with everything else on C:. Clearing the real hogs gives Recall room without touching its store.

1. Run **Settings > System > Storage > Cleanup recommendations** and remove large unused apps and old downloads.
2. Delete previous Windows installations (Windows.old) if present — often tens of gigabytes.
3. Move personal media libraries to the second drive or external storage; keep the system drive for system data.
4. Peripheral driver issues can compound storage confusion on ARM machines — [Wacom tablet drivers on ARM](/articles/wacom-tablet-driver-arm-windows/) covers keeping those installs clean.

### Fix 5: Exclude high-churn apps from capture

Apps that change constantly — video players, dashboards, games — generate snapshots with little long-term value while consuming the same storage.

1. Open the app exclusion list in Recall settings.
2. Add media players, games, and monitoring dashboards you never need to search later.
3. Fewer captured apps means slower store growth and a more useful timeline.
4. Re-check storage after a week of excluded capture to confirm the growth rate dropped.

### Fix 6: Consider hardware options if software is not enough

When the drive is simply too small for your workflow, no setting fully compensates — but there are legitimate paths.

1. Check whether your laptop's SSD is upgradeable; many Copilot+ laptops allow it, some do not.
2. A clean Windows reinstall with a sensible Recall allocation from day one avoids years of cruft.
3. For driver and firmware-level storage issues, grab updates from [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) matched to your exact model.
4. Never use symbolic-link or registry hacks to relocate the store — they break encryption assumptions and can corrupt the database.

## Closing

You cannot move Recall's snapshots to another drive — that is a deliberate security design, not an oversight. But the space problem is solvable where it counts: cap the allocation, tighten retention, delete dead history, exclude high-churn apps, and clear the real disk hogs. Do that, and the system drive stops feeling small even with Recall running around the clock.
