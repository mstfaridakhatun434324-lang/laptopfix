---
title: "How to Fix Windows Update Error 0x80070652 Step by Step"
slug: how-to-fix-windows-update-error-0x80070652-step-by-step
date: 2026-09-06
categories: ["windows-update"]
tags: ["windows update", "0x80070652", "installer busy", "windows 11"]
description: "Error 0x80070652 means another installation is already running. Follow this step-by-step guide to tell real installs from stuck ones and clear the blockage."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-step-by-step.webp"
faqs:
  - q: "What does Windows Update error 0x80070652 mean?"
    a: "It is ERROR_INSTALL_ALREADY_RUNNING: the Windows Installer engine allows only one MSI-based installation at a time, and it believes one is already in progress. The blockage is either genuine — another install truly running — or phantom, where a crashed installer never released the engine. The repair sequence first distinguishes the two, because a real install needs patience while a phantom needs termination."
  - q: "How can I tell if the other install is real or stuck?"
    a: "Open Task Manager and look at the Windows Installer (msiexec.exe) process: CPU activity, disk activity, and a progressing installer window mean it's real — wait 30 to 60 minutes. No activity, no window, and no progress change over an extended period means it's stuck. When in doubt, a single restart resolves the ambiguity: genuine installs resume or complete, phantoms usually clear."
  - q: "Why does Windows only allow one installer at a time?"
    a: "The Windows Installer engine serializes installations to protect shared components. Two installers writing to the same shared libraries, registry keys, or component store simultaneously could corrupt all of them. The single-install rule is a safety design, not a limitation — and 0x80070652 is the engine enforcing it, which is why the fix is clearing the first install rather than forcing the second."
  - q: "Can Microsoft Store updates trigger this error?"
    a: "Yes. Store app updates can use the installer engine, and a Store update running in the background while Windows Update tries an MSI-based update produces exactly this collision. If the error appears at random times, check the Microsoft Store's Downloads section for in-progress updates. Pausing Store updates during Windows Update runs eliminates this quieter variant of the conflict."
---

Error 0x80070652 is the installer engine enforcing its one-at-a-time rule: ERROR_INSTALL_ALREADY_RUNNING. Windows' MSI engine serializes installations to protect shared components — two installers writing the same libraries simultaneously would be a corruption disaster — so when a second install starts while the engine thinks one is running, it gets turned away with this code.

The critical question is whether the first install is real or a ghost. A real one — a driver, a Store app, a pending reboot-phase — just needs time or a restart. A ghost is a crashed installer that died without unlocking the engine, and no amount of waiting clears it. The sequence below tells the two apart first, because patience fixes one and termination fixes the other, and applying the wrong remedy wastes your time. There's also a middle case worth recognizing: an install that is real but progressing absurdly slowly — a large driver crawling on a slow disk, for instance. Task Manager shows faint activity, so it's not a clean phantom, but hours pass with no visible progress. For those, the restart in Fix 2 is still the right move: a healthy installer resumes gracefully after reboot, while a truly wedged one reveals itself by failing to resume, converting ambiguity into a clear diagnosis.

## Why this happens

- **A genuine concurrent installation.** Another MSI install truly running — the engine is correctly refusing the second.
- **A crashed installer holding the lock.** The phantom: msiexec died without releasing the engine.
- **Microsoft Store updates in the background.** Store app installs colliding with Windows Update.
- **A pending reboot.** The engine waiting on a restart from a previous install's final phase.
- **A wedged Windows Installer service.** The service stuck reporting "busy" with nothing running.
- **Corrupted engine state.** The installer database disagreeing with reality about what's in flight.
- **Manufacturer update tools.** OEM utilities running their own installs concurrently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify what's actually running

Look before you terminate — a working install deserves patience.

1. Open Task Manager (**Ctrl + Shift + Esc**) and check the **Processes** tab for **Windows Installer** entries.
2. Note CPU and disk activity: active numbers plus a visible installer window mean a real install — give it 30–60 minutes.
3. Check the Microsoft Store's download queue and any manufacturer update tool for concurrent activity.
4. Only treat the blockage as a phantom when there's no activity, no window, and no progress over an extended stretch.

### Fix 2: Restart to drain the installer queue

The single most effective step for both real and phantom cases.

1. Save everything and perform a full **Restart** from the Start menu.
2. Many "already running" states are installs waiting on their reboot phase — the restart completes them and releases the engine.
3. After reboot, wait a few minutes for startup activity to settle.
4. Retry **Settings > Windows Update > Check for updates**; the engine is usually free now.

### Fix 3: Terminate the confirmed stuck installer

For the verified phantom, end it once and cleanly.

1. In Task Manager's **Details** tab, locate the idle `msiexec.exe`.
2. Right-click and choose **End task** — a single termination, not a repeated killing spree.
3. Look for sibling orphans (`setup.exe`, `TrustedInstaller.exe`) from the same failed session and end those too.
4. Restart and retry the update with the phantom lock gone.

### Fix 4: Pause competing install sources

Stop the collisions from recurring.

1. Pause Microsoft Store updates during Windows Update runs (Store > Downloads > Pause).
2. If your manufacturer ships an update utility, don't run it simultaneously with Windows Update — sequence them instead.
3. Schedule Windows updates for times when you're not installing other software.
4. This habit eliminates the most common genuine-collision pattern entirely.

### Fix 5: Clean boot to find a repeat offender

If the phantom returns on every boot, something keeps wedging the engine.

1. Run `msconfig`; hide Microsoft services and **Disable all** others; disable all **Startup apps** in Task Manager.
2. Restart into the clean state and retry the update.
3. Success indicts a third-party program — re-enable in halves, retesting, until the error returns.
4. Update, reconfigure, or remove the offending program; installer-wedging utilities aren't worth keeping.

### Fix 6: Re-register the installer engine and reset update state

Rebuild the engine's bookkeeping when it insists it's busy forever.

1. In an administrator Command Prompt: `msiexec /unregister` then `msiexec /regserver`.
2. Reset the update cache: stop `wuauserv`, `bits`, `cryptsvc`; rename `SoftwareDistribution` and `catroot2` with `.old` suffixes; restart the services.
3. Restart the laptop so the re-registered engine initializes cleanly.
4. Retry the update; the engine's record of "running" installs now matches reality.

### Fix 7: Troubleshoot and install the package manually

The final combination for stubborn cases.

1. Run the **Windows Update** troubleshooter from **Settings > System > Troubleshoot > Other troubleshooters**.
2. Get the failing KB's x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the standalone installer with all other install sources quiet.
4. Verify in Update history. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents these engine-serialization scenarios for deeper study.

### Fix 8: Perform an in-place upgrade as the final repair

When the installer engine stays wedged through every targeted fix, rebuild it with Windows itself.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11) and mount it with a double-click.
2. Run `setup.exe`, accept the license terms, and choose **Keep personal files and apps** on the "Choose what to keep" screen.
3. Let the 30–90 minute upgrade run with the charger connected and no interruptions; the installer engine is replaced wholesale.
4. After signing in, run **Settings > Windows Update > Check for updates** — the fresh engine serializes installs correctly and the phantom "already running" state is gone.

## Closing

Error 0x80070652 is the installer engine's one-at-a-time rule doing its job — your task is just determining whether the first install is real or a ghost, and acting accordingly. For HP-specific dual-pipeline collisions, see the [HP laptop version](/articles/how-to-fix-windows-update-error-0x80070652-on-hp-laptop/), and if an installer fails outright rather than reporting a conflict, the [0x80070643 step-by-step guide](/articles/how-to-fix-windows-update-error-0x80070643-step-by-step/) is the right next read.
