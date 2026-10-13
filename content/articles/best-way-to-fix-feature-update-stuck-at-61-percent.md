---
title: "Feature Update Stuck at 61%? Best Way to Push It Through"
slug: best-way-to-fix-feature-update-stuck-at-61-percent
date: 2026-09-23
categories: ["windows-update"]
tags: ["feature update", "stuck at 61", "windows 11", "installation stuck", "upgrade frozen"]
description: "The feature update has been parked at 61% for hours. Here's what that stage means and the best ordered fixes to get it moving again."
thumbnail: "/images/thumbs/best-way-to-fix-feature-update-stuck-at-61-percent.webp"
faqs:
  - q: "What is happening at 61% during a feature update?"
    a: "Around 61%, the installer is in its heaviest phase: applying the new OS image to disk and migrating your drivers into it. This file-copy and driver-handoff stage demands sustained disk throughput for a long stretch. Stalls here usually mean the disk cannot keep up, a driver is hanging during migration, or the staged image is corrupted. A freeze means the current phase has hit something it cannot get past."
  - q: "How long should I wait at 61%?"
    a: "Wait at least three hours with no disk activity before intervening. This phase involves enormous file I/O, and slower laptops can sit at one percentage for a very long time while genuinely working. Check the drive activity light: sustained activity means progress, silence means stuck."
  - q: "Will forcing a shutdown at 61% damage Windows?"
    a: "No. At 61% your previous Windows installation is fully preserved as the rollback target, so a forced shutdown simply triggers the automatic rollback — the designed recovery path for exactly this situation. The installer anticipates interruptions at every phase and handles them safely. The one thing to avoid is interrupting the rollback itself; let it complete undisturbed and you will return to a working desktop."
  - q: "Why does my feature update always stall at the same percentage?"
    a: "A repeatable stall at one percentage indicates a deterministic blocker rather than bad luck: the same hanging driver, the same disk problem, or the same corrupted payload each time. Check the setup error logs after the rollback — they usually name the specific component, turning a mystery into a targeted fix."
---

Sixty-one percent is the feature update's favorite parking spot. The progress bar stops, the spinner spins on, and the laptop sits there for hours doing apparently nothing. Unlike a failed update that at least tells you something, a stall gives you silence — which makes the ordered approach even more important.

At 61%, the installer is in the heavy phase: laying down the new OS image and migrating your drivers into it. A freeze here means that phase hit something it cannot get past. The best fix sequence: confirm the stall, recover via rollback, eliminate the blocker, and reinstall through the strongest path.


Treat the 61% figure as a location, not a measurement: it tells you which phase is stuck, not how close you are to done. That framing changes the response from "wait longer" to "fix the phase." The phase at 61% is image application and driver migration — everything below targets exactly those two operations.
## Why this happens

- **Driver hanging in migration:** A single unmigratable driver stalls the whole phase.
- **Slow or failing storage:** The intense write workload exposes marginal disks.
- **Corrupted staged image:** A damaged payload failing at the same point every attempt.
- **Insufficient disk space:** The image application needs working room.
- **Peripheral conflicts:** External devices confusing the hardware migration.
- **Thermal throttling:** Sustained load overheating a dusty laptop into a crawl.
- **Antivirus interference:** File operations intercepted mid-migration.
- **USB 2.0 installer media:** Slow installation media bottlenecking the image application phase.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the stall with real evidence

1. Give it a full **three hours** from the last percentage movement.
2. Watch the drive activity light for sustained blinking versus total darkness.
3. Feel for heat and listen for fan behavior — a working installer keeps the machine warm and busy.
4. Cold, silent, and dark for an hour means genuinely stuck. Only then intervene.
5. Compare against a known-good baseline: a healthy 61% phase takes 20-60 minutes on an SSD.
6. Beyond three hours with zero activity, you have your answer — proceed to recovery.

### Fix 2: Force shutdown and accept the rollback

1. Hold the power button for **10 seconds** until the machine powers off completely.
2. Disconnect the charger, wait 30 seconds, then power on.
3. Windows will roll back to your previous build automatically — do not interrupt the rollback.
4. Once at the desktop, verify everything works. The rollback is the safety net doing its job. For broader rollback guidance, see our guide on [updates stuck on restarting](/articles/best-way-to-fix-windows-update-stuck-on-restarting/).
5. If rollback offers Safe Mode options, choose normal boot first — Safe Mode is for later diagnosis.
6. Do not attempt the retry immediately; complete Fixes 3-5 first for a genuinely fresh attempt.

### Fix 3: Free space and improve thermals

1. Free **30 GB** on C: — space pressure during image application causes exactly this stall.
2. Clean the vents and run the retry on a hard, flat surface with the charger connected.
3. Consider a cooling stand for the retry; thermal throttling under sustained load mimics a freeze.
4. Disable sleep in power settings so nothing interrupts the long install.
5. Check the SMART status of the drive — the stall may be an early warning of failure.
6. If the drive is healthy but slow, the retry simply needs more patience, not more fixes.

### Fix 4: Update drivers, firmware, and remove blockers

1. Update **chipset, storage, and graphics drivers** from the manufacturer's support site.
2. Install any pending **BIOS/UEFI update**.
3. Temporarily uninstall third-party antivirus, VPN clients, and virtual drive software.
4. Disconnect all peripherals except the charger. The 61% phase migrates hardware state — fewer devices, fewer hang points. For the driver-error family, see our guide on [error 0xc1900101](/articles/how-to-fix-update-fails-with-error-0xc1900101-after-windows-11-update/).
5. Remove SD cards and USB drives — the migration enumerates every storage device.
6. Update the BIOS even if the changelog seems unrelated; firmware fixes are often undocumented.

### Fix 5: Clear the staging and repair the system

1. In an elevated Command Prompt: `net stop wuauserv`, `net stop bits`, empty `C:\Windows\SoftwareDistribution\Download`, restart both services.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow`.
3. Run Disk Cleanup with **Windows Update Cleanup** to purge the failed staging.
4. Restart and confirm the system is healthy before retrying.
5. Verify the staging folders are gone after deletion — permission issues sometimes protect them.
6. Restart after the repairs; the component store changes need a boot to settle.

### Fix 6: Retry through the Installation Assistant

1. Download the **Windows 11 Installation Assistant** from the [official download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run it with peripherals disconnected, antivirus paused, and thermals managed.
3. Its delivery and staging path differs from Windows Update and often clears the stall point.
4. If it stalls at 61% again, the blocker is deterministic — check the logs in Fix 7.
5. Choose the 'upgrade this PC' path in the Assistant, not the media creation path.
6. If the Assistant needs to download, let it finish completely before starting the install phase.

### Fix 7: Read the logs and target the culprit

1. After the rollback, open `C:\$Windows.~BT\Sources\Panther\setuperr.log`.
2. Identify named drivers or failing operations near the end of the log.
3. Update, disable, or uninstall the implicated component.
4. Run `chkdsk C: /f` to rule out disk errors, then retry. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document log locations for deeper analysis.
5. Focus on errors timestamped around the stall — earlier errors may be red herrings.
6. Fix one implicated component at a time; changing five things teaches you nothing.

## Closing

A 61% stall is the installer stuck in its heaviest phase — image application and driver migration under load. Confirm it, roll back, clear space, refresh drivers, cool the machine, and retry through the Assistant. When the stall repeats at the same spot, the logs will name your culprit. Treat the percentage as a phase indicator rather than a progress bar, and the fix becomes obvious. The 61% stall is a phase problem with phase solutions: disk throughput, driver migration, image integrity. Address the phase and the percentage takes care of itself.
