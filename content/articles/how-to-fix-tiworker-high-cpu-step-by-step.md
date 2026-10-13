---
title: "TiWorker.exe High CPU: Fix Windows Modules Installer Worker Step by Step"
slug: how-to-fix-tiworker-high-cpu-step-by-step
date: 2026-09-29
categories: ["performance"]
tags: ["tiworker.exe", "windows modules installer worker", "high cpu", "windows update", "step by step"]
description: "TiWorker.exe pinning your CPU at 100%? This step-by-step guide explains what the Windows Modules Installer Worker is doing and how to get it under control."
thumbnail: "/images/thumbs/how-to-fix-tiworker-high-cpu-step-by-step.webp"
faqs:
  - q: "What is TiWorker.exe and is it safe?"
    a: "TiWorker.exe — the Windows Modules Installer Worker — is a legitimate Windows process that installs updates, enables and disables Windows features, and maintains system components. It lives in the WinSxS servicing stack and is completely safe. High CPU from it means Windows is actively servicing the system; the problem is only when it never finishes, which the steps below address."
  - q: "How long should TiWorker.exe normally run at high CPU?"
    a: "After Patch Tuesday or a feature update, one to three hours of elevated CPU is normal while updates install and the component store is optimized. Give it that window with the laptop plugged in. If it is still hammering the CPU after 24 hours, or if it starts at high CPU on every boot with no updates pending, the servicing stack is stuck and needs repair."
  - q: "Can I just disable TiWorker.exe to stop the high CPU?"
    a: "You should not. TiWorker is part of the trusted installer servicing stack; disabling it breaks Windows Update, feature installation, and system repair. The correct approach is to let it finish its work, or fix whatever is preventing it from finishing — corrupted update caches, a damaged component store, or a stuck update. Disabling servicing creates bigger problems than high CPU."
  - q: "Why does TiWorker.exe use high CPU even when Windows Update says everything is up to date?"
    a: "Because servicing continues after the visible update completes: post-install component cleanup, .NET optimization, and Store app servicing all run through TiWorker. Also, a corrupted update cache can make it retry the same work endlessly while Update reports success. Clearing the SoftwareDistribution cache and running DISM usually breaks that loop."
---

**TiWorker.exe** — the Windows Modules Installer Worker — is Windows doing its own maintenance: installing updates, servicing components, enabling Windows features. When it runs hot, your CPU sits at 50–100%, the fan roars, and the laptop feels broken. Here's the uncomfortable truth most guides skip: TiWorker running hot is usually Windows working correctly. The skill is telling "working" from "stuck" — and this guide is built around exactly that distinction.

You'll learn how long to let it work, how to check what it's actually doing, and the repair sequence that un-sticks it when it genuinely won't finish.

## Why this happens

- **Legitimate post-update servicing:** After Patch Tuesday or a feature update, TiWorker installs components and optimizes the store — hours of real work.
- **Corrupted SoftwareDistribution cache:** Damaged update files make TiWorker retry the same failed work in an endless loop.
- **Damaged component store (WinSxS):** Corruption in the servicing stack itself prevents operations from completing, so TiWorker never stands down.
- **Stuck or partially installed update:** An update that can't finish keeps the worker engaged indefinitely.
- **.NET optimization backlog:** After updates, the .NET native image generator queues heavy compilation work through the servicing stack.
- **Windows feature changes pending:** Enabling/disabling features (Hyper-V, .NET Framework versions) triggers extended TiWorker activity.
- **Insufficient disk space:** Servicing needs working room; a nearly-full C: drive stalls operations mid-flight.
- **Third-party interference:** Overzealous "debloating" tools that damaged servicing components leave TiWorker spinning on broken dependencies.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what it's doing and give it a deadline

Open Task Manager → TiWorker.exe → right-click → Go to details, and check Windows Update (Settings → Windows Update) for pending or recently installed updates. If updates just installed, this is legitimate work: plug in, leave the laptop alone, and give it up to 3 hours. Set a timer. If CPU is still pinned after your deadline — or Update shows nothing pending and TiWorker is hot on every boot — it's stuck, not working. For the broader family of installer-worker issues, see [Windows Modules Installer high CPU](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/).

1. Check Windows Update status: pending, installing, or recently completed?
2. If recent updates: plug in, leave idle, set a 3-hour deadline.
3. If no updates pending and TiWorker is hot → it's stuck.
4. Record your finding; it determines the next step.

### Fix 2: Let pending updates fully complete

If updates are pending or mid-install, the worst thing you can do is interrupt. Go to Settings → Windows Update and let everything download and install, rebooting when asked — repeatedly, until Update reports fully up to date. TiWorker often spikes hardest during the finalization phase. Only after Update is clean and the machine has rebooted twice should you judge whether the problem persists. Interrupting servicing mid-flight is how corrupted states (and stuck workers) are born.

1. Settings → Windows Update → install everything pending.
2. Reboot when prompted; check for more updates; repeat.
3. Continue until Update reports fully up to date after a reboot.
4. Observe TiWorker for an hour of idle time.

### Fix 3: Clear the corrupted update cache

Stop the Windows Update service (admin Terminal: `net stop wuauserv` and `net stop bits`), then rename `C:\Windows\SoftwareDistribution` to `SoftwareDistribution.old`. Restart the services (`net start wuauserv`, `net start bits`). This forces Windows to rebuild its update cache from scratch, breaking the retry loop that keeps TiWorker spinning on damaged files. Check for updates afterward — it will re-scan cleanly. This is the single most effective fix for the "stuck at high CPU with nothing pending" pattern.

1. Admin Terminal: `net stop wuauserv` then `net stop bits`.
2. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old`.
3. `net start wuauserv` and `net start bits`.
4. Check for updates; observe TiWorker behavior.

### Fix 4: Repair the component store with DISM

Admin Terminal, in order: `DISM /Online /Cleanup-Image /ScanHealth` to assess, then `DISM /Online /Cleanup-Image /RestoreHealth` to repair. This fixes the WinSxS component store that TiWorker itself operates on — a damaged store is a classic reason the worker can never finish. Follow with `sfc /scannow` and reboot. The scan takes 15–30 minutes; let it complete uninterrupted. If DISM reports it repaired corruption, there's a good chance your TiWorker problem is solved. Microsoft documents these tools on the [Windows support site](https://support.microsoft.com/en-us/windows).

1. Admin Terminal: `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Reboot when finished.
4. Monitor TiWorker at idle for an hour.

### Fix 5: Free disk space for servicing

Check C: free space — servicing needs room for staging, and under 15–20GB free, operations stall and retry. Run Disk Cleanup as admin with system files (Windows Update Cleanup especially), enable Storage Sense, and move large personal files off C: if needed. After freeing space, trigger a manual update check to let any stalled servicing resume with room to work. This is a mechanical fix for a mechanical problem, and it's frequently the missing piece when DISM alone didn't help. Deeper disk guidance: [Windows Modules Installer high CPU variants](/articles/how-to-fix-windows-modules-installer-high-cpu-step-by-step/).

1. Check C: free space; target 20GB+ free.
2. Disk Cleanup (admin) → Clean up system files.
3. Enable Storage Sense; move large files off C:.
4. Manually check for updates to resume stalled servicing.

### Fix 6: Run the Windows Update troubleshooter

Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run. The troubleshooter resets update components, fixes service registrations, and clears common stuck states automatically. It's less thorough than the manual cache clear, but it catches service-configuration issues the manual steps miss — and it takes two minutes. Run it after the manual repairs as a final sweep, then reboot and check for updates once more.

1. Settings → System → Troubleshoot → Other troubleshooters.
2. Run the Windows Update troubleshooter; apply its fixes.
3. Reboot.
4. Check for updates; observe TiWorker.

### Fix 7: In-place upgrade repair for a broken servicing stack

If TiWorker is still pinned after all of the above, the servicing stack itself is damaged beyond DISM's ability to repair — usually from interrupted updates or aggressive debloating tools. Download Windows 11 media from the [official download page](https://www.microsoft.com/en-us/software-download/windows11), run setup, and keep files and apps. This reinstalls the entire servicing stack cleanly. It's a 1–2 hour process but it resolves TiWorker issues that nothing else touches, because it replaces the worker's own infrastructure.

1. Download official Windows 11 installation media.
2. Run setup → Keep personal files and apps.
3. Complete the in-place upgrade (1–2 hours).
4. Verify TiWorker idles normally afterward.

## Closing

TiWorker high CPU is a patience problem first and a repair problem second: most instances are legitimate servicing that finishes if you let it, and the stuck ones yield to the cache-clear and DISM sequence in that order. The mistake to avoid is treating the worker as the enemy — it's Windows maintaining itself. Fix what's blocking it, give it room to work, and it goes quiet on its own.
