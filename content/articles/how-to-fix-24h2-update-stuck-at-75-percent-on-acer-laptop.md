---
title: "Fix 24H2 Update Stuck at 75% on an Acer Laptop"
slug: how-to-fix-24h2-update-stuck-at-75-percent-on-acer-laptop
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows 11 24h2", "update stuck", "acer laptop", "windows update"]
description: "24H2 frozen at 75% on your Acer laptop? That's the driver-migration phase stalling. Here are 7 fixes to unstick it without losing your data."
thumbnail: "/images/thumbs/how-to-fix-24h2-update-stuck-at-75-percent-on-acer-laptop.webp"
faqs:
  - q: "Is it safe to force restart when 24H2 is stuck at 75% on my Acer?"
    a: "One controlled restart is safe once you have confirmed a true stall — no disk activity for over an hour. Windows is designed to roll back a failed feature update automatically, and your files are preserved. The danger is in repeated force-restarts during the same rollback, which can corrupt the boot configuration. Restart once, then let the rollback finish undisturbed."
  - q: "How can I tell if 75% is really stuck or just slow?"
    a: "Watch the storage activity light and listen for drive sounds for a full hour. The driver-migration phase at 75% legitimately takes a long time on slower Acer hardware — 60 to 90 minutes of apparent stillness with active disk I/O is normal. It is only a true stall when the percentage never moves and the disk shows zero activity for over an hour."
  - q: "Why does the 24H2 update always stop at exactly 75%?"
    a: "Because 75% maps to the driver migration and boot-configuration phase of the feature update. The installer is validating and migrating every driver on the system — and on Acer laptops, the Realtek audio, Intel storage, and Acer Care Center drivers are frequent sticking points. One driver that cannot migrate parks the entire installer at that percentage until it is resolved or rolled back."
  - q: "My Acer rolled back to the old Windows version. Is my data safe?"
    a: "Yes. A rollback restores the previous Windows build while leaving your personal files, installed programs, and settings intact — that is the entire purpose of the undoing-changes process. Verify by checking that your documents and apps are present after the rollback completes. Then use the preparation steps below before attempting 24H2 again."
---

Watching the Windows 11 24H2 update freeze at 75 percent on an Acer laptop is a special kind of suspense: the progress bar climbed steadily for an hour, and now it has not moved for two more. No error, no blue screen — just 75%, indefinitely. This stall is so consistent across Acer's Aspire, Swift, and Nitro lines that it has a known anatomy, and once you understand the anatomy, the fix is straightforward.

Seventy-five percent is not arbitrary. Feature update progress maps to phases, and the three-quarter mark is where the installer migrates drivers and rewrites the boot configuration. Acer laptops carry Realtek audio drivers, Intel storage drivers, and Acer Care Center hooks that all must be validated and migrated in this phase. When one of them is corrupted, outdated, or actively resisting, the installer does not skip it — it waits. The screen looks frozen, but the installer is parked, not crashed, which is why the recovery below works.

## Why this happens

- **A corrupted Acer driver blocks migration.** Damaged Realtek audio, Intel RST, or chipset drivers cannot be migrated, halting the installer.
- **Acer Care Center interference.** Acer's utility services can lock driver files the installer needs to replace.
- **Insufficient free disk space.** The staging phase needs ~20 GB; below that, the driver phase starves at 75%.
- **Third-party antivirus blocking.** Real-time protection intercepting the driver's file replacement operations.
- **Damaged update payload.** A corrupted download means the installer cannot assemble the driver set it is trying to migrate.
- **Outdated BIOS.** Older Acer firmware can conflict with 24H2's driver signing and power behavior.
- **Corrupted component store.** WinSxS damage from a previous interrupted update breaks the image assembly.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall before acting

Interrupting a healthy install is the one thing that turns a slow update into a broken one. Confirm first.

1. Wait at least 90 minutes at 75% — driver migration is legitimately slow on Acer's budget hardware.
2. Check the storage LED for blinking or listen for drive activity. Activity means progress; leave it alone.
3. Press **Ctrl + Alt + Delete** once — a responding screen means Windows is alive underneath.
4. Only with no disk activity for a full hour and an unresponsive screen is it a true stall. Then unplug all USB devices (docks and external drives cause redetection hangs) and wait 30 more minutes before moving to Fix 2.

### Fix 2: Roll back safely with one restart

A single controlled restart triggers Windows' automatic rollback, which restores your previous build with files intact.

1. Hold the power button 10 seconds until the Acer shuts off, wait 30 seconds, then power on.
2. Windows should begin "Undoing changes made to your computer" — allow 30 to 60 minutes without interrupting it.
3. Once back on the desktop, verify your files and apps are present, then open **Settings > System > Storage** and confirm 20 GB free on C:.
4. If the rollback itself hangs, our guide to the [undoing changes loop](/articles/best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer/) covers recovery from the recovery environment.

### Fix 3: Update Acer drivers from the official source

Stale Acer drivers are the top cause of the 75% stall. Bring them current before the next attempt.

1. Go to Acer's support site, enter your serial number or model, and download the latest **chipset**, **Intel RST / storage**, **Realtek audio**, and **BIOS** packages for Windows 11.
2. Install them one at a time with restarts between; install BIOS last with the charger plugged in.
3. Open Device Manager and confirm no yellow warning icons remain.
4. For the full safe order, see our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) — and keep Acer Care Center itself updated, since outdated versions lock driver files.

### Fix 4: Pause Acer Care Center and antivirus

Acer's utilities and third-party antivirus both interfere with driver migration at 75%.

1. In `services.msc`, temporarily stop **Acer Care Center** services and set them to Manual.
2. If you run third-party antivirus, pause its real-time protection for the install window.
3. Retry the 24H2 update from **Settings > Windows Update** with both paused.
4. Re-enable everything after the update completes. Consider whether the third-party AV earns its keep — Windows Security avoids an entire class of these conflicts.

### Fix 5: Clear the update cache and verify the payload

A damaged download poisons every retry. Force a clean one.

1. Open Command Prompt as administrator.
2. Run: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run: `net start wuauserv`, `net start bits`, `net start cryptsvc`. Then check for updates — 24H2 downloads fresh.

### Fix 6: Repair the component store

WinSxS damage breaks the image assembly behind the driver phase. Repair it directly.

1. In an administrator Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth` (15–30 minutes).
2. Follow with `sfc /scannow` to 100%.
3. Restart and retry the 24H2 update.
4. If DISM fails with a source error, our guide to [running DISM RestoreHealth](/articles/how-to-run-dism-restore-health-on-windows-11/) shows how to point DISM at a Windows ISO.

### Fix 7: Install 24H2 via the Installation Assistant or ISO

If Settings-based updates keep stalling at 75%, take the alternative path — it migrates drivers through more robust code.

1. Download the Installation Assistant from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11) and run it as administrator with USB devices unplugged.
2. If the assistant also stalls, download the Windows 11 ISO from the same page, mount it, and run `setup.exe`, choosing **Keep personal files and apps**.
3. Allow 60–120 minutes with several automatic restarts; do not use the laptop during the install.
4. After 24H2 lands, install the follow-up cumulative updates from **Settings > Windows Update**.

## Closing

A 24H2 stall at 75% on an Acer laptop is a driver-migration problem wearing a frozen-progress-bar disguise — and it yields to preparation, not force. Confirm the stall, roll back once, update Acer's drivers, clear the cache, and retry through the assistant or ISO if needed. The same discipline prevents the sibling stall where updates hang during download instead of install — see our guide to updates [stuck downloading on Windows 11](/articles/how-to-fix-windows-update-stuck-downloading-on-windows-11/); and if a future update fails with an explicit code, our [0x80070005 guide for Acer](/articles/how-to-fix-windows-update-error-0x80070005-on-acer-laptop/) shows the code-specific approach.
