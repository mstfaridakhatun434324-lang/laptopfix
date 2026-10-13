---
title: "Fix Windows Modules Installer High CPU"
slug: "how-to-fix-windows-modules-installer-high-cpu"
date: 2026-09-21
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "trustedinstaller", "high cpu", "windows update"]
description: "Windows Modules Installer (TiWorker.exe) stuck at high CPU? Repair the servicing stack with DISM, SFC, and update-component resets — safe methods only."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu.webp"
faqs:
  - q: "What is Windows Modules Installer?"
    a: "Windows Modules Installer is the system service (TrustedInstaller) responsible for installing Windows updates, adding or removing optional features, and maintaining the component store. Its worker process, TiWorker.exe, does the actual CPU-heavy work of processing component changes. It is a core part of Windows — not bloatware, not a virus — and disabling it breaks updates, feature changes, and eventually the system repair tools that depend on the servicing stack."
  - q: "Why does Windows Modules Installer run at 100% CPU?"
    a: "It runs hot when it has a large backlog of servicing work, such as a feature update or a big cumulative update, which is normal for 20 to 60 minutes. Sustained 100 percent CPU for hours means something is wrong: usually a corrupted component store, a stuck update queue, or a driver conflict failing the installation silently. The fixes in this guide address each of those root causes rather than just killing the process."
  - q: "Can I disable Windows Modules Installer to stop the CPU usage?"
    a: "Technically you can set the service to Disabled, but you should not. Doing so blocks all Windows updates, prevents adding Windows features, and can break SFC and DISM repairs that rely on the servicing stack. Within weeks the laptop falls behind on security patches. Every legitimate fix — letting updates finish, repairing the store, resetting components — resolves the CPU issue without sacrificing updates."
  - q: "How do I know if the high CPU is normal or a problem?"
    a: "Check Settings > Windows Update. If an update is actively installing and TiWorker calms down within about an hour, that was normal servicing work — leave it alone. If no update is progressing, the same update keeps failing, or TiWorker returns to high CPU after every reboot for days, the servicing stack is stuck and needs repair. Duration plus lack of progress is the diagnostic that separates normal from broken."
---
Windows Modules Installer — the TrustedInstaller service and its worker TiWorker.exe — is Windows' own maintenance crew. It installs updates, manages optional features, and keeps the component store consistent. Normally it works in brief bursts you never notice. When it breaks, though, it can pin your CPU at 80–100 percent for hours, across reboots, with nothing ever finishing.

Killing the process feels satisfying and accomplishes nothing: the servicing queue is still there, so Windows just launches TiWorker again. The loop means the underlying work cannot complete — a corrupted component store, a wedged update queue, or a conflicting driver — and the fix is to unblock the work, not to shoot the worker.

This guide repairs the servicing stack from the gentlest method to the strongest: verify normal activity, run the troubleshooter, repair with DISM and SFC, reset the update components, and check drivers and disk. If TiWorker specifically is your symptom on a Lenovo machine, our [TiWorker guide](/articles/how-to-fix-tiworker-high-cpu-on-lenovo-laptop/) covers the Lenovo-specific angles.

## Why this happens

- **Legitimate update installation:** feature updates genuinely need 20–60 minutes of heavy servicing work — patience, not repair, is the fix.

- **Corrupted component store:** damaged WinSxS metadata makes every servicing operation fail and retry forever.

- **Wedged update queue:** a failed cumulative update leaves the queue in a state TiWorker cannot move past.

- **Driver conflicts:** storage or chipset drivers that fail during the update keep the whole servicing transaction from committing.

- **Interrupted servicing:** a forced shutdown during an update corrupts in-flight component operations.

- **Antivirus interference:** real-time scanners locking system files can make TiWorker's file operations fail repeatedly.

- **Insufficient free space:** servicing needs gigabytes of scratch space on C:; without it, operations abort and retry.

- **Corrupted system files:** damaged protected files that SFC would normally repair can themselves stall servicing.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it is real work before repairing

The most common mistake is “repairing” a system that was simply installing an update. Ten minutes of checking saves you from unnecessary surgery and from interrupting work that was nearly done.

1. Open Settings > Windows Update and look for an update showing as Downloading or Installing.
2. If one is active, plug in the laptop, prevent sleep, and give it up to 90 minutes.
3. In Task Manager's Details tab, verify TiWorker.exe runs from C:\Windows\WinSxS (right-click > Open file location).
4. Note the start time: if CPU drops on its own within the hour, it was normal servicing.
5. Only continue if high CPU persists for hours with zero update progress.

### Fix 2: Run the Windows Update troubleshooter

The troubleshooter re-registers servicing components and clears stuck jobs — the lightest repair that resolves a surprising number of loops. Microsoft documents the current troubleshooter flow on its [Windows support site](https://support.microsoft.com/en-us/windows).

1. Go to Settings > System > Troubleshoot > Other troubleshooters.
2. Run the Windows Update troubleshooter and apply all suggested fixes.
3. Restart the laptop when it finishes.
4. Check for updates once more and let any found updates attempt a clean install.
5. Monitor TiWorker for 30 minutes to see whether it now completes and exits.

### Fix 3: Repair with DISM, then SFC

DISM repairs the component store that the servicing stack runs on; SFC then repairs protected system files using that store. Run in this order, they fix the majority of corrupted-servicing cases without touching your files or apps.

1. Open Command Prompt as administrator.
2. Run DISM /Online /Cleanup-Image /RestoreHealth and wait for it to finish (10–30 minutes).
3. Do not shut down or close the window mid-operation.
4. When DISM succeeds, immediately run sfc /scannow in the same window.
5. Restart afterward and verify TiWorker stays quiet at idle.

### Fix 4: Reset the update components

If the queue itself is corrupt, no amount of store repair helps until the broken queue is discarded. Renaming the SoftwareDistribution and catroot2 folders forces Windows to rebuild both from scratch on the next update check.

1. Open an elevated Command Prompt.
2. Run net stop wuauserv, net stop cryptSvc, net stop bits, and net stop msiserver.
3. Run ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
4. Run ren C:\Windows\System32\catroot2 catroot2.old.
5. Run net start wuauserv, net start cryptSvc, net start bits, net start msiserver, then restart and check for updates.

### Fix 5: Install the update manually from the Catalog

Sometimes the automatic pipeline is the problem, not the update. Downloading the failing cumulative update as a standalone package from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and installing it directly bypasses the stuck queue entirely.

1. In Settings > Windows Update > Update history, note the KB number of the failing update.
2. Search that KB number on the Microsoft Update Catalog site.
3. Download the package matching your architecture (x64 for most laptops).
4. Run the .msu file and let it install, then restart when prompted.
5. Check Task Manager afterward: with the backlog cleared, TiWorker should stand down.

### Fix 6: Update storage and chipset drivers

Servicing transactions commit through your storage driver; a buggy one can fail the commit silently and leave TiWorker retrying forever. Fresh chipset and storage drivers from the laptop vendor eliminate this whole class of failure.

1. Download the latest chipset and storage (IRST/RST or NVMe) drivers for your exact model from the vendor's support site.
2. Install the chipset driver first, restart, then the storage driver.
3. For Intel platforms, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) can detect missing updates automatically.
4. Run Windows Update again and let the previously stuck update attempt a clean pass.
5. If TiWorker completes this time, the driver was the blocker all along.

### Fix 7: Free space and verify drive health

Servicing is disk-intensive: it stages gigabytes of files and needs room to maneuver. A nearly full or failing drive turns every servicing operation into timeouts and retries that look exactly like a software loop.

1. Ensure at least 15–20 GB free on C: via Settings > System > Storage; use Cleanup recommendations aggressively.
2. Delete the Windows.old folder from a previous upgrade if it is still sitting there.
3. Run chkdsk C: /scan from an elevated prompt to check file-system integrity.
4. Check SMART health with CrystalDiskInfo or your SSD vendor's tool — replace on any warning.
5. With space and health confirmed, give Windows Update one final clean attempt.

## Closing

Windows Modules Installer at high CPU is a symptom with a short list of causes: real update work, a corrupted store, a wedged queue, or a driver blocking the commit. Diagnose with the update history, repair with DISM and SFC, reset the components if the queue is broken, and keep drivers current. Followed in order, these steps end the TiWorker loop on nearly every machine — no clean install, no registry hacks, no disabled updates. For the update-specific branch of this problem, see our [post-update servicing guide](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/) as well.
