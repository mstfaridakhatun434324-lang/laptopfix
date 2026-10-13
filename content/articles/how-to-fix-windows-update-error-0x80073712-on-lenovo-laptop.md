---
title: "How to Fix Windows Update Error 0x80073712 on a Lenovo Laptop"
slug: "how-to-fix-windows-update-error-0x80073712-on-lenovo-laptop"
date: 2026-10-03
categories: ["windows-update"]
tags: ["error 0x80073712", "windows update", "lenovo laptop", "component store", "windows 11"]
description: "Error 0x80073712 on a Lenovo laptop signals a corrupted Windows component store. Seven fixes, from the DISM store repair to a full in-place upgrade."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80073712-on-lenovo-laptop.webp"
faqs:
  - q: "What does error 0x80073712 mean?"
    a: "It is shorthand for ERROR_SXS_COMPONENT_STORE_CORRUPT: the WinSxS repository that supplies every update with its system components has damaged entries. Updates assemble their changes from this repository, so when its catalog or stored payloads are broken, installation cannot continue. Typical triggers are interrupted feature updates, deteriorating drives, over-aggressive cleaners, and long-accumulated servicing wear."
  - q: "Will DISM definitely fix 0x80073712?"
    a: "Usually, yes — RestoreHealth exists precisely to rebuild damaged stores by comparing them with healthy online sources. It fails only when the corruption runs extraordinarily deep or the underlying disk is physically failing. If DISM cannot finish the repair, check the disk with chkdsk first, then escalate to an in-place upgrade, which reconstructs the store completely."
  - q: "Can I just delete the WinSxS folder?"
    a: "Absolutely not. WinSxS is the component store itself, and removing it destroys Windows' ability to update or repair anything, leaving reinstallation as the only escape. Use DISM's sanctioned cleanup instead: DISM /Online /Cleanup-Image /StartComponentCleanup prunes superseded components without harming the store's structure. Cleaners that meddle with WinSxS are a leading cause of this error."
  - q: "How do I prevent component store corruption?"
    a: "Let updates finish without interruption, keep the charger attached during installs, and stay away from aggressive system cleaners that touch WinSxS. Run an occasional chkdsk to catch disk trouble early, and install updates regularly instead of letting a massive backlog pile up. These habits keep the store's catalog and payloads consistent for years."
---

Every Windows update is assembled from the component store — the WinSxS library of system parts sitting underneath the visible operating system. Error 0x80073712, officially ERROR_SXS_COMPONENT_STORE_CORRUPT, tells you that library's catalog is damaged: manifests disagree with payloads, and the installer refuses to build on a foundation it cannot trust. On Lenovo laptops, the usual wrecking balls are a feature update interrupted mid-migration, a drive developing bad sectors, or a cleaning tool that deleted pieces it did not understand.

This is not a download problem, so hammering "retry" in Windows Update will not heal it — the breakage lives one layer deeper than the delivery pipeline. The [0x80070643 installation-failure walkthrough](/articles/how-to-fix-windows-update-error-0x80070643-on-lenovo-laptop/) handles updates that fail for unrelated reasons, but 0x80073712 means the store itself is the patient.

The sequence below climbs in intensity, starting with Microsoft's dedicated store-repair tool and ending with a full in-place rebuild. DISM's RestoreHealth was designed for exactly this damage and clears the majority of cases — give it the patience its long scan demands before moving down the list.

## Why this happens

- **A feature update interrupted mid-flight:** Losing power or crashing halfway through a version upgrade can strand the store between old and new layouts, with its index pointing at components that no longer exist.
- **A drive going bad underneath it:** Bad sectors landing in the WinSxS region silently chew up manifests and payloads. Nothing complains until an update reaches for the damaged part.
- **Overzealous cleaning utilities:** Tools promising to free disk space sometimes delete supposedly redundant WinSxS components that the servicing stack still references, fracturing the store's integrity.
- **Malware sabotage:** Some infections deliberately damage system components and their backup copies to resist removal, leaving the store's catalog in ruins.
- **Sloppy driver packages:** Driver installers that write into the driver store incorrectly can corrupt the component metadata sitting adjacent to them.
- **Power loss during servicing:** When the servicing stack is mid-transaction and the machine dies, half-committed changes leave the store internally inconsistent.
- **Years of accumulated drift:** Each update layers on top of the last, and tiny inconsistencies compound over time until they cross the line into outright failure.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Repair the store with DISM

For 0x80073712, DISM belongs first in line — no other tool understands the component store's internals the way it does. While SFC guards individual files, DISM's RestoreHealth audits the whole WinSxS catalog against healthy online sources and rebuilds whatever fails to match, which is precisely the damage this error reports. Microsoft documents this repair path in the [official Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open up an elevated Command Prompt.
2. Launch DISM /Online /Cleanup-Image /RestoreHealth from the elevated prompt and give it the full run — budget 15 to 30 minutes.
3. After it finishes, follow up with sfc /scannow to catch any lingering file damage.
4. Restart the laptop and check for updates again.

### Fix 2: Sweep protected files with SFC

Once DISM has straightened the store's catalog, SFC sweeps the individual protected files it governs. The checker compares every guarded system file against its known-good twin and replaces the casualties — a pass that removes an entire family of install failures that catalog-level repair does not cover.

1. Open Command Prompt or Terminal with admin rights.
2. Type sfc /scannow and press Enter, then let the scan complete.
3. Restart the laptop if the tool reports that it replaced anything.
4. Try the update installation again after the reboot.

### Fix 3: Wipe and rebuild the update working folders

The updater keeps its own working papers — download caches and pending-operation state — and those can be just as damaged as the store. The cure is demolition: stop the four update services, rename both folders out of the way, and Windows rebuilds them empty — pristine permissions, zero leftover operations, nothing stale for the installer to stumble on.

1. Launch a Command Prompt with elevation — right-click Start and pick Terminal (Admin).
2. Halt the services by running net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
3. Tag both folders with new names: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Bring the four services back with net start, then check for updates again.

### Fix 4: Hunt for bad sectors with chkdsk

If the store keeps corrupting, suspect the ground it is built on. Bad sectors can shred component payloads as they are written, and the damage looks identical to mysterious store corruption. A full disk scan finds the defective regions and shifts data away from them, cutting the corruption off at its source.

1. Open a Command Prompt with admin rights.
2. Run chkdsk C: /f /r and approve the scan for the next restart.
3. Reboot and let the scan run to completion — large drives can take an hour.
4. Retry the update once the disk check reports clean.

### Fix 5: Install the package yourself from the Update Catalog

Even with a repaired store, the automatic delivery path can stay wedged. Downloading the failing update as a standalone .msu skips that whole pipeline and installs it directly — a detour that often succeeds where the automated route keeps stalling.

1. In Settings, Windows Update, then Update history, note the KB number of the failing update.
2. Look up that KB on the Microsoft Update Catalog site and open its page.
3. Download the x64 build matching your Windows 11 edition.
4. Run the .msu file, follow the installer through, and restart when it asks.

### Fix 6: Give the built-in troubleshooter a turn

The Windows Update troubleshooter will not rebuild a damaged store, but it clears the surrounding rubble: stuck services, wedged pending operations, misconfigured settings. It is a two-minute automated pass that fixes a surprising share of update failures without touching a command line.

1. Open Settings, head to System, and click Troubleshoot.
2. Open Other troubleshooters and locate Windows Update.
3. Click Run, wait for the scan, and apply every repair it offers.
4. Reboot, then head back to Windows Update and retry the install.

### Fix 7: Rebuild Windows around your files with an in-place upgrade

When every targeted repair has failed, stop repairing and start rebuilding. An in-place upgrade reinstalls Windows over itself while preserving your files and apps, replacing all system files, services, and update machinery with pristine copies — the store included. It is the definitive answer to corruption that nothing else could reach. Back up first anyway: safe is not the same as risk-free. The [official Windows 11 download](https://www.microsoft.com/en-us/software-download/windows11) page hosts the media creation tool you need.

1. Download the media creation tool for Windows 11 from Microsoft's download page.
2. Launch it, choose Upgrade this PC now, and keep personal files and apps.
3. Let setup run its course — expect several restarts along the way.
4. When setup finishes, run Windows Update to collect anything newer than the repair image.

## Closing

Store corruption sounds catastrophic, but DISM was purpose-built for it and succeeds far more often than it fails — run it patiently, verify with SFC, and escalate only if the damage outruns both. And when the next failure turns out to be a busy-installer collision instead of corruption, the [0x80070652 installer-conflict guide](/articles/how-to-fix-windows-update-error-0x80070652-on-lenovo-laptop/) takes over.
