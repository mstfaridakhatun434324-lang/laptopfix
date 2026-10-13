---
title: "Windows Update Error 0x800f0989 on Laptop: How to Fix It"
slug: how-to-fix-windows-update-error-0x800f0989-on-laptop
date: 2026-09-15
categories: ["windows-update"]
tags: ["windows update error 0x800f0989", "cbs_e", "component store corrupted", "update fails to install"]
description: "Error 0x800f0989 is a component servicing failure closely related to 0x800f0988. Repair the store, remove conflicting features, and finish the update."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0989-on-laptop.webp"
faqs:
  - q: "What is the difference between 0x800f0988 and 0x800f0989?"
    a: "Both are Component-Based Servicing failures rooted in component store corruption. In practice they respond to the same repairs, DISM, SFC, and store cleanup. 0x800f0989 appears slightly more often with driver-adjacent and optional-feature updates, while 0x800f0988 is common with .NET and language updates."
  - q: "Can third-party driver updaters cause 0x800f0989?"
    a: "Yes. Driver updater utilities that inject unsigned or mismatched driver packages into the driver store can create servicing conflicts that surface as 0x800f0989 when Windows Update tries to service those components. Uninstall such tools before troubleshooting, then install drivers from the manufacturer directly."
  - q: "Should I delete the WinSxS folder to fix this?"
    a: "Never. The WinSxS folder is the component store itself, and deleting it destroys Windows beyond repair. Use DISM's StartComponentCleanup instead, which safely removes only superseded components while preserving the store's integrity and bookkeeping. Never run cleaners that promise to shrink WinSxS; they cause exactly this damage."
  - q: "How do I check the CBS log for details?"
    a: "Open C:\\Windows\\Logs\\CBS\\CBS.log in a text editor and search for the error code or the word failed near the time of the attempt. The log names the specific package or manifest that failed, which tells you whether a language pack, driver, or feature is the trigger."
---

Error 0x800f0989 is the near-twin of 0x800f0988: another Component-Based Servicing failure, another signal that the component store Windows uses to assemble updates has damage the servicing stack cannot route around. If you have already read about 0x800f0988, the repair playbook will feel familiar — but the triggers skew a little different.

Where 0x800f0988 loves .NET and language updates, 0x800f0989 shows up more often around driver packages, optional features, and cumulative updates that touch servicing-adjacent components. Third-party driver utilities are a disproportionately common trigger here, injecting packages into the driver store that later updates cannot reconcile.

The repair sequence therefore pairs the standard store repairs with a hunt for the conflicting component. Fix the store, remove the offender, and the update completes.

It helps to think of 0x800f0989 as the servicing stack's conflict report: two components both claim the same servicing territory, usually because a third-party tool staged something unofficial. The repairs below evict the squatter, rebuild the damaged records, and let the legitimate update take its rightful place.

## Why this happens

- **Component store corruption.** Damaged WinSxS entries prevent CBS from staging the update, the same root cause as its sibling code.

- **Conflicting driver packages.** Third-party driver updaters can stage mismatched or unsigned drivers that later servicing operations cannot reconcile.

- **Broken optional features.** Half-installed features such as Hyper-V or media packs leave servicing transactions the stack cannot complete.

- **Corrupted update cache.** Damaged payload files in SoftwareDistribution make an otherwise healthy store fail the install.

- **Disk-level corruption.** Bad sectors affecting servicing manifests produce errors that look identical to logical store corruption.

- **Interrupted servicing operations.** Power loss during a previous update can leave the store in a half-transacted state.

- **Damaged servicing stack.** A bad servicing stack update undermines every install that follows it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Fix 1: Run DISM with RestoreHealth

Start with the canonical store repair. DISM compares your component store against known-good sources and replaces damaged files, which resolves the underlying corruption behind most 0x800f0989 failures. When DISM reports that the source files could not be found, mount a Windows ISO and rerun with /Source pointed at the install.wim; the online repair sometimes needs that explicit source on badly damaged stores.

1. Open Terminal as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for full completion.
3. Restart the laptop before moving on.

### Fix 2: Fix 2: Follow up with SFC

Once DISM has repaired the store, SFC verifies the protected system files against it. This two-punch order matters: SFC draws its repair source from the store, so the store must be healthy first. If SFC keeps finding the same unfixable files across runs, note their names; they identify the exact component family, which helps you decide whether an optional feature removal will clear them.

1. In an admin Terminal, run `sfc /scannow`.
2. Wait for the scan to finish and note whether it repaired anything.
3. Restart and retry Windows Update.

### Fix 3: Fix 3: Uninstall third-party driver updater tools

Driver utilities from outside the manufacturer are a hallmark trigger for this code. They stage driver packages Windows servicing cannot verify, and the conflict surfaces exactly here. Check the manufacturer's support page for the driver the updater was managing; installing the official driver directly usually gives you a newer, properly signed package anyway.

1. Open Settings, then Apps, then Installed apps.
2. Uninstall any third-party driver updater or driver booster utilities.
3. Restart, then run DISM once more to let the store settle before retrying the update.

### Fix 4: Fix 4: Remove conflicting optional features

If the CBS log points at a feature package, removing that feature eliminates the conflict at its source. You can reinstall it cleanly after the update succeeds. The CBS log timestamps use a 24-hour clock and can be verbose, so filter by the hour of your last update attempt to land near the relevant failure quickly.

1. Check C:\Windows\Logs\CBS\CBS.log for the failing package name around the error timestamp.
2. Open Settings, then Apps, then Optional features, and remove the implicated feature.
3. Restart and retry the update.

### Fix 5: Fix 5: Clean the component store

Superseded components can harbor the corrupt entries. DISM's cleanup pass removes them safely, shrinking the store and frequently taking the corruption with it. Component cleanup can take a long time on first run, especially on systems that have never had it done; let it finish rather than assuming it has hung.

1. Open Terminal as administrator.
2. Run `DISM /Online /Cleanup-Image /StartComponentCleanup`.
3. Let it finish, restart, and check for updates.

### Fix 6: Fix 6: Reset the update cache

A damaged payload in the download cache can mimic store corruption. Clearing it ensures the next attempt installs pristine files onto your freshly repaired store. Consider this cache reset mandatory rather than optional after a driver-tool removal, since the old payloads were staged against the conflicting driver state.

1. In an admin Terminal, run `net stop wuauserv` and `net stop bits`.
2. Delete everything in C:\Windows\SoftwareDistribution\Download.
3. Run `net start wuauserv` and `net start bits`, then retry.

### Fix 7: Fix 7: Run an in-place upgrade repair

For store damage that resists DISM, reinstalling Windows over itself rebuilds the entire servicing stack while preserving your files and applications. It is the definitive fix for deep corruption. The in-place upgrade takes one to three hours on most laptops; start it when you can leave the machine plugged in and undisturbed, and do not close the lid mid-repair.

1. Get the installer from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run setup.exe from the mounted ISO and choose Keep personal files and apps.
3. After completion, run Windows Update. If you see the sibling code instead, our [0x800f0988 repair guide](/articles/how-to-fix-windows-update-error-0x800f0988-on-laptop/) covers it.

## Closing

Error 0x800f0989 rewards methodical repair: fix the component store with DISM and SFC, evict the conflicting driver tool or feature, and clear the cache before retrying. That sequence resolves nearly every instance on laptops. Its twin, [error 0x800f0988](/articles/how-to-fix-windows-update-error-0x800f0988-on-laptop/), uses the same playbook if you encounter it, and Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) has the official DISM reference. On 24H2 specifically, the [24H2 edition of this repair](/articles/how-to-fix-windows-update-error-0x800f0989-in-windows-11-24h2/) covers the repeat-pattern quirk — last month's staging debris breaking this month's update — in more depth.
