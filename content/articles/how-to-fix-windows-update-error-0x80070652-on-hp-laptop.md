---
title: "How to Fix Windows Update Error 0x80070652 on an HP Laptop"
slug: how-to-fix-windows-update-error-0x80070652-on-hp-laptop
date: 2026-09-05
categories: ["windows-update"]
tags: ["windows update", "0x80070652", "hp laptop", "windows 11"]
description: "Error 0x80070652 on your HP laptop means another installation is already running. This HP-focused guide clears the stuck installer and finishes your updates."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070652-on-hp-laptop.webp"
faqs:
  - q: "What does error 0x80070652 mean on an HP laptop?"
    a: "It is ERROR_INSTALL_ALREADY_RUNNING: Windows' installer engine believes another installation is in progress and refuses to start a second one. Sometimes that's true — HP Support Assistant installing a driver while Windows Update runs — and sometimes it's a phantom: a previous install crashed without releasing the engine. The fixes distinguish the real collision from the stuck one and clear whichever it is."
  - q: "Is it safe to end the Windows Installer process?"
    a: "Ending a genuinely stuck msiexec.exe is safe and is a standard troubleshooting step. If an installation was actually progressing, the worst outcome is that specific install needs to be rerun. The key is to end it once, restart, and retry — not to repeatedly kill installer processes, which can leave the engine in a confused state that produces exactly this error."
  - q: "Why do HP laptops get this error more often?"
    a: "Because HP laptops run two installer pipelines at once: Windows Update's and HP Support Assistant's. When both try to install drivers simultaneously, the Windows Installer engine serializes them — one must wait — and if either side stalls, the other reports 0x80070652. Staggering the two channels, HP first then Windows, prevents the collision pattern almost entirely."
  - q: "How long should I wait before assuming the installer is stuck?"
    a: "Give a visibly progressing install at least 30–60 minutes, especially for large drivers, BIOS updates, or feature updates — they have long silent phases. Only treat it as stuck when there's no disk activity, no progress change, and no installer window for an extended period. Prematurely killing a working installer creates the very stuck state you're trying to fix."
---

Error 0x80070652 is the installer engine's traffic cop: ERROR_INSTALL_ALREADY_RUNNING. Windows allows only one MSI-based installation at a time, so when a second one starts, the engine waves it off with this code. Sometimes the first install is real and you just need patience; sometimes it's a ghost — a crashed install that never released the engine — and you need to clear it.

HP laptops are prime territory for this error because they run two installation pipelines concurrently: Windows Update and HP Support Assistant. Both install drivers, both use the installer engine, and when they overlap, one of them gets the 0x80070652 wave-off. The repair sequence below first determines whether the blocking install is real or phantom, then clears it appropriately. A final piece of practical advice for HP owners: resist running HP Support Assistant and Windows Update at the same time even when both show pending items begging for attention. It feels efficient to parallelize, but the single-installer rule makes it the opposite — the two queues collide, one fails with 0x80070652, and you spend longer untangling the collision than sequential updating would ever have taken. HP first, Windows second, always.

## Why this happens

- **HP Support Assistant installing while Windows Update runs.** The classic HP collision — two pipelines, one installer engine.
- **A crashed installer never released the engine.** The phantom case: msiexec died without cleaning up its lock.
- **A genuinely long install in progress.** Large drivers and BIOS updates have silent phases that look stuck but aren't.
- **Pending reboot from a previous install.** The engine waiting on a restart that never happened.
- **Stuck Windows Installer service.** The service itself wedged, reporting "busy" forever.
- **Corrupted installer metadata.** The engine's record of what's running doesn't match reality.
- **Background Microsoft Store updates.** Store app updates using the installer engine concurrently.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether an install is genuinely running

Don't kill what might be working — verify first.

1. Open Task Manager's **Processes** tab and look for **Windows Installer** or `msiexec.exe` entries with CPU or disk activity.
2. Check for visible installer windows, HP Support Assistant progress, or Microsoft Store update activity.
3. If something is genuinely progressing, wait — give it 30–60 minutes, especially for drivers or firmware.
4. Only proceed to the stuck-installer fixes if there's no activity, no progress, and no window for an extended period.

### Fix 2: Restart to let pending installs complete

A reboot is the cleanest way to drain the installer queue.

1. Save your work and do a full **Restart** — many "stuck" installs are actually waiting on the reboot phase.
2. After rebooting, wait five minutes for startup tasks to settle before touching updates.
3. Go to **Settings > Windows Update** and retry the failed update.
4. If 0x80070652 is gone, the previous install simply needed its reboot to release the engine.

### Fix 3: End the stuck installer process

For the confirmed phantom, terminate it cleanly.

1. Open Task Manager's **Details** tab and find `msiexec.exe` with no activity.
2. Right-click it and choose **End task** — once, then stop killing things.
3. Also check for `setup.exe` or `TrustedInstaller.exe` orphans from the same failed session.
4. Restart the laptop and retry the update with the engine lock released.

### Fix 4: Stagger HP and Windows updates

Prevent the HP-specific collision pattern permanently.

1. Open **HP Support Assistant** and install all pending HP drivers and firmware first, restarting as prompted.
2. Only after HP's queue is fully clear, run **Settings > Windows Update > Check for updates**.
3. Make this ordering a habit: HP channel first, Microsoft channel second, never simultaneously.
4. HP's drivers remain available directly from the [HP support site](https://support.hp.com/us-en) if you prefer manual control over Support Assistant's scheduling.

### Fix 5: Clean boot to isolate a third-party blocker

Some program may be re-triggering the phantom on every boot.

1. Run `msconfig`; on the **Services** tab, check **Hide all Microsoft services** and click **Disable all**.
2. Disable all **Startup apps** in Task Manager, then restart.
3. Retry the update in the clean state — success proves third-party interference.
4. Re-enable in halves to identify the program that keeps wedging the installer, then update or remove it.

### Fix 6: Reset the Windows Installer service and update components

Rebuild the engine's state when it reports busy forever.

1. In an administrator Command Prompt, run `msiexec /unregister` followed by `msiexec /regserver` to re-register the engine.
2. Reset the update cache: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, then `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`, then `net start wuauserv`, `net start bits`, `net start cryptsvc`.
3. Restart the laptop to let the re-registered engine initialize cleanly.
4. Retry the update; the engine no longer believes a phantom install is running.

### Fix 7: Run the troubleshooter and install manually

Cover the remaining cases with automated repair plus a direct install.

1. Run the **Windows Update** troubleshooter at **Settings > System > Troubleshoot > Other troubleshooters** and apply its fixes.
2. Note the failing KB from Update history and download its x64 `.msu` from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Run the standalone installer with other installers quiet — no Support Assistant activity concurrently.
4. Confirm success in Update history. Microsoft's official [Windows Update support hub](https://support.microsoft.com/en-us/windows) documents installer-engine conflicts for further background.

## Closing

Error 0x80070652 is the installer engine refusing a second concurrent job, and on HP laptops the fix is usually about sequencing HP's and Microsoft's pipelines rather than repairing anything. For the generic walkthrough, see the [step-by-step 0x80070652 guide](/articles/how-to-fix-windows-update-error-0x80070652-step-by-step/), and if your installer fails outright rather than reporting a conflict, the [0x80070643 guide for HP laptops](/articles/how-to-fix-windows-update-error-0x80070643-on-hp-laptop/) covers that adjacent failure.
