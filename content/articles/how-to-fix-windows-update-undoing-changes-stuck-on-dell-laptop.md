---
title: "Fix Windows Update 'Undoing Changes' Stuck on a Dell Laptop"
slug: how-to-fix-windows-update-undoing-changes-stuck-on-dell-laptop
date: 2026-09-06
categories: ["windows-update"]
tags: ["undoing changes stuck", "dell laptop", "we couldn't complete updates"]
description: "Stuck on 'Undoing changes made to your computer' on your Dell laptop? Learn how long to wait, how to force a safe reboot, and how to stop the loop."
thumbnail: "/images/thumbs/how-to-fix-windows-update-undoing-changes-stuck-on-dell-laptop.webp"
faqs:
  - q: "How long can 'Undoing changes' legitimately take on a Dell laptop?"
    a: "Allow at least 60 to 90 minutes. A rollback reverses everything the failed update did, which on a hard drive can be slow. On an SSD, more than two hours with zero drive activity is the practical definition of stuck. Interrupting a genuine rollback mid-way is far more dangerous than interrupting an install, so err toward patience."
  - q: "Is 'Undoing changes' the same as a boot loop?"
    a: "Not exactly. A rollback screen with spinning dots means Windows is actively reverting changes, while a boot loop restarts the machine repeatedly. If your Dell restarts over and over without ever showing the rollback progress, that is a boot loop and needs the WinRE-based fixes below rather than more waiting."
  - q: "Will I lose my files during the rollback?"
    a: "No. Rolling back an update only reverses system files, drivers, and update packages. Your documents, photos, and installed apps are not touched by the rollback process itself. This is one of the safer failure states Windows Update can land in."
  - q: "Why does this happen every month on my Dell?"
    a: "A recurring rollback points to a persistent blocker: usually an outdated Dell driver, a failing hard drive, or insufficient disk space. Dell's SupportAssist can check driver and hardware health, and fixing the underlying cause once stops the monthly cycle. See the Dell-specific fixes below."
---

"Undoing changes made to your computer" is Windows telling you the update failed and it is now reversing the damage. That is good news wrapped in a stressful package: the system is protecting itself. On Dell laptops, this screen appears most often after cumulative or feature updates that collided with Dell-specific drivers — storage controllers, BIOS-linked firmware, or the Dell SupportAssist components themselves.

The critical mistake people make here is panic-rebooting. A rollback is slower than an install because every change must be undone in reverse order, and on a spinning hard drive 60–90 minutes is completely normal. The second most common mistake is forcing a shutdown and then walking away — a Dell that loses power mid-rollback can fail to boot entirely. This guide gives you the exact decision tree: how long to wait, how to break out safely if it is genuinely stuck, and how to prevent the monthly repeat that so many Dell owners report. The same loop shows up across brands — see the general guide to [troubleshooting the undoing-changes loop](/articles/troubleshoot-we-couldn-t-complete-the-updates-undoing-changes/) for the brand-neutral version.

## Why this happens

- **An update package fails its final checks:** Windows installs the update, then validates the result. If validation fails, it rolls everything back automatically — the screen you are seeing.
- **Dell driver incompatibility:** Intel RST storage drivers, Realtek audio drivers, and Dell-specific system drivers are frequent blockers. The update changes system files the driver cannot work with, validation fails, rollback begins.
- **Corrupted download:** A partially corrupted update package passes the initial checks but fails during application, triggering the automatic reversal.
- **Insufficient disk space for the rollback:** Reversing an update needs working space. A nearly full drive can stall the rollback itself, producing the stuck screen.
- **Failing hard drive:** Bad sectors in the middle of system files cause the install to fail validation. HDD-equipped Dell models (Inspiron, older Vostro) are the usual victims.
- **Third-party antivirus interference:** Kernel-level security suites can modify the same files the update touches, so the final state never matches what the update expected.
- **BIOS/firmware mismatch:** An outdated Dell BIOS paired with a new feature update can fail the hardware abstraction checks, forcing a rollback every time.
- **Interrupted previous install:** A laptop that lost power during an earlier update may have a damaged servicing stack, so every subsequent update fails at the same point.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait it out properly before touching anything

1. Note the time and give the rollback **at least 90 minutes** on a hard drive, **45 minutes** on an SSD.
2. Watch for drive activity: a blinking activity light or audible drive churning means the rollback is progressing — keep waiting.
3. Dell laptops often show no percentage here; that is normal, not a symptom.
4. Only proceed to Fix 2 once you have exceeded these windows with zero activity. Patience resolves a large share of "stuck" rollbacks because they were never actually stuck.

### Fix 2: Force a safe reboot into the Recovery Environment

1. Hold the power button for **10 seconds** until the Dell powers off. Unplug all USB devices except the charger.
2. Power on, and the moment the Dell logo appears, hold power to force off again. Repeat **three times** total.
3. On the fourth boot, Windows Recovery Environment (WinRE) loads with the "Choose an option" screen.
4. Go to **Troubleshoot → Advanced options**. From here you have the full repair toolkit without the rollback blocking you.
5. First try **Startup Repair** — it takes five minutes and fixes boot damage from the interrupted rollback.

### Fix 3: Roll back with System Restore from WinRE

1. In WinRE, go to **Troubleshoot → Advanced options → System Restore**.
2. Choose the restore point timestamped just before the failed update.
3. Complete the wizard and let the laptop reboot. Your personal files survive this; only system state rewinds.
4. If no restore points exist, skip to Fix 4 — and enable System Protection afterward so you have this safety net next time.

### Fix 4: Uninstall the latest quality update from WinRE

1. In WinRE, go to **Troubleshoot → Advanced options → Uninstall Updates**.
2. Select **Uninstall latest quality update** (the monthly cumulative update is the usual culprit).
3. Confirm and wait for the uninstall to complete, then reboot normally.
4. Once booted, immediately pause updates for 7 days: **Settings → Windows Update → Pause updates**. This buys you time to fix the root cause before Windows retries.

### Fix 5: Update Dell drivers and BIOS before retrying

1. Boot normally and open [Dell Support](https://www.dell.com/support) — enter your Service Tag for the exact driver list.
2. Install any **BIOS**, **Intel Rapid Storage Technology**, and **chipset** updates shown. These are the three Dell components most responsible for rollback loops.
3. Alternatively, run the preinstalled **SupportAssist** app and let it scan for driver updates.
4. Also update your third-party antivirus, or temporarily uninstall it before the next update attempt.

### Fix 6: Clear the update cache and repair system files

1. Open an elevated Terminal (right-click Start → Terminal (Admin)).
2. Run `net stop wuauserv` and `net stop bits`, then `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`, then `net start wuauserv` and `net start bits`.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` followed by `sfc /scannow` to repair any damage from the failed install.
4. Restart and check **Settings → Windows Update** for a clean slate.

### Fix 7: Check the drive health and free space

1. Ensure at least **15 GB free** on C: — use Storage Sense or Disk Cleanup with "Windows Update Cleanup" selected.
2. Check drive health: in an elevated Command Prompt run `wmic diskdrive get status` — anything other than "OK" means the drive is failing and no update will ever install cleanly until it is replaced.
3. For deeper detail, Dell's built-in diagnostics (press **F12** at boot → Diagnostics) run a full drive test in about 15 minutes.

## Closing

The "Undoing changes" screen is Windows doing its job — the update failed safely instead of breaking your system. Once you are back in Windows, resist the urge to immediately hit "Check for updates." The update failed for a reason, and retrying blindly starts the loop over. Update your Dell drivers and BIOS first, clear the cache, verify your drive health, and only then retry. Do that, and the monthly rollback ritual ends. If the loop persists across all of this, the in-place repair install via the Media Creation Tool rebuilds the entire servicing stack while keeping your files — the definitive fix for stubborn cases. For updates that fail without reaching the rollback screen at all, the [Windows Update fails-to-install walkthrough](/articles/how-to-fix-windows-update-fails-to-install-in-windows-11-24h2/) covers the complementary repair sequence.
