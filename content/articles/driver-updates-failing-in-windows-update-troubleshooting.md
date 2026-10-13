---
title: "Driver Updates Failing in Windows Update: Full Troubleshooting Walkthrough"
slug: driver-updates-failing-in-windows-update-troubleshooting
date: 2026-10-06
categories: ["windows-update"]
tags: ["driver updates", "troubleshooting", "setupapi log", "error codes", "device manager"]
description: "A diagnostic walkthrough for driver updates that fail in Windows Update: read the real error in logs, match it to the cause, and apply the targeted fix."
thumbnail: "/images/thumbs/driver-updates-failing-in-windows-update-troubleshooting.webp"
faqs:
  - q: "Where do I find the real reason a driver update failed?"
    a: "The two best sources are Device Manager's Events tab for the device, which logs the install attempt and failure, and the setupapi.dev.log file in C:\\Windows\\INF, which records driver installation in fine detail. The generic message in Windows Update history rarely tells the full story."
  - q: "What does error 0x80070103 mean for a driver update?"
    a: "It means Windows Update tried to install a driver that is already installed or older than the current one — usually because the driver was already updated manually. It is harmless. Hiding the update or installing the newer driver manually makes it go away."
  - q: "Why does the same driver update fail with different error codes?"
    a: "Because the failure point moves as you change conditions. A corrupted download gives one code, a signature problem gives another, and a device-in-use lock gives a third. Treat each new code as fresh information pointing at the current blocker, not as the problem getting worse."
  - q: "Can I see driver update failures in Event Viewer?"
    a: "Yes. Look under Windows Logs > System for events from the 'Microsoft-Windows-DeviceSetupManager' and 'Microsoft-Windows-Kernel-PnP' sources around the time of the failure. They record which driver package failed and often include the underlying error code, giving you the precise starting point for diagnosis that the generic Windows Update message never provides."
---

When a driver update fails in Windows Update, the message you see — "failed to install" with a hex code — is the end of a long chain of events, and the real cause is buried earlier in that chain. Effective troubleshooting means reading the chain instead of guessing: find the exact failure in the logs, match it to its cause, and apply the fix that addresses that cause. This walkthrough teaches you that diagnostic process, because once you can read a driver failure, you can fix any of them.

You will need two tools: Device Manager's Events tab for the quick version of the story, and the setupapi.dev.log file for the full version. Keep a notepad handy for error codes — precision matters here, since 0x80070103 and 0x800F0247 point at completely different problems.

## Why this happens

- **Driver already current (0x80070103):** Windows Update offers a driver older than or equal to the installed one, often after you updated manually. Harmless but noisy.
- **Signature or catalog failure:** The driver package's digital signature does not validate on your system, and Windows refuses the install as a protective measure.
- **Hardware ID mismatch:** The offered driver's INF does not cleanly match your device's hardware ID, so Plug and Play rejects the binding.
- **Device in use during install:** The old driver is locked by a running application or its own control utility, and the replacement cannot unload it.
- **Corrupted driver package download:** The downloaded driver files fail hash verification, so the install aborts before it begins.
- **Driver Store conflicts:** Multiple versions of the same driver in the store create staging conflicts that fail the install.
- **Third-party driver blockers:** Some "privacy" and "debloating" tools block all driver changes system-wide, which breaks legitimate updates too.
- **Pending reboot blocking staging:** A previous install left a pending reboot flag, and new driver staging is queued behind it indefinitely.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the failure in Device Manager Events

Get the precise error before doing anything else. The Events tab records each driver install attempt with its outcome.

1. Open **Device Manager** and locate the device whose driver update failed.
2. Right-click it, choose **Properties**, and open the **Events** tab.
3. Read the most recent events top-down: look for "failed" entries and their error codes.
4. Write down the exact code. Common ones: 0x80070103 (already installed), 0x800F0247 (blocked by policy), 0x80070005 (access denied).

### Fix 2: Check setupapi.dev.log for the detailed failure

When the Events tab is vague, the setup log tells you exactly which step failed — signature check, file copy, device binding, or service start.

1. Open `C:\Windows\INF\setupapi.dev.log` in Notepad (it is large — use Find).
2. Search for the device name or the timestamp of the failed attempt.
3. Look for lines containing `!!!` — these mark errors — and read the surrounding context.
4. Typical findings: `signature verification failed` (get the driver from the OEM), `file not found` (corrupted download — clear the cache), or `device is in use` (close the vendor utility and retry).

### Fix 3: Handle the benign 0x80070103 case

If your code is 0x80070103, there is nothing to fix — Windows is offering a driver you already have or have surpassed. Silence it and move on.

1. Confirm in **Device Manager > Driver tab** that your installed version is equal to or newer than the offered one.
2. Run Microsoft's **Show or hide updates** troubleshooter and hide the redundant driver update.
3. Alternatively, exclude drivers from Windows Update via Group Policy so this class of noise stops permanently.

### Fix 4: Close vendor utilities and retry the install

Many driver installs fail because the old driver's control panel or background service holds the device open. A clean retry with those closed often succeeds.

1. Close any vendor control software (NVIDIA Control Panel, Intel Graphics Command Center, Realtek Audio Console, printer utilities).
2. Open **Task Manager > Startup apps** and temporarily disable the vendor's background services, then restart.
3. Go to **Settings > Windows Update** and click **Retry** on the failed driver.
4. If it installs now, re-enable the startup entries afterward.

### Fix 5: Clear pending reboot flags and the update cache

A stuck pending-reboot state or corrupted driver package blocks staging. Clear both.

1. Check for pending reboots: look at `HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\PendingFileRenameOperations` — if an unrelated installer left junk here, reboot first.
2. Open **Terminal (Admin)** and run `net stop wuauserv`, then `net stop bits`.
3. Delete the contents of `C:\Windows\SoftwareDistribution\Download`.
4. Run `net start wuauserv` and `net start bits`, restart, and retry the driver update.

### Fix 6: Install the correct driver manually and stage it properly

When Windows Update's package is wrong for your hardware, bypass it with the OEM driver — the same strategy recommended in [the best-order fix guide](/articles/best-way-to-fix-driver-updates-failing-in-windows-update/) — but do it cleanly.

1. Download the driver from your laptop maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for your exact model.
2. In Device Manager, uninstall the device with **Attempt to remove the driver for this device** ticked.
3. Run `pnputil /enum-drivers`, find stale packages for the device, and remove them with `pnputil /delete-driver oemXX.inf /uninstall`.
4. Install the OEM package, restart, and verify the version on the Driver tab.

### Fix 7: Check for policy or tool-based driver blocks

If driver installs fail with access-denied codes across all devices, something is blocking driver changes system-wide.

1. Run `gpresult /h report.html` in Terminal and open the report — look under Windows Update policies for driver exclusions you did not set.
2. Check for "debloating," privacy, or update-blocker tools you may have run in the past; their registry changes persist after uninstallation.
3. Undo the block: in Group Policy, set **Do not include drivers with Windows Updates** to **Not configured** (unless you want it on deliberately), and remove registry blocks under `HKLM\SOFTWARE\Policies\Microsoft\Windows\DeviceInstall`.
4. For persistent [missing-file style failures](/articles/how-to-fix-windows-update-error-0x80070003-on-windows-11/) affecting drivers specifically, the full SoftwareDistribution and Catroot2 reset is the final pipeline-level fix.

## Closing

Driver update failures reward diagnosis over repetition: read the Events tab, confirm with setupapi.dev.log, and match the error code to its cause instead of clicking retry and hoping. The benign cases (already-installed drivers) just need hiding; the real ones (signature failures, wrong packages, locked devices) need the OEM driver installed cleanly. Learn to read one driver failure properly and every future one becomes a five-minute job instead of a month of nagging red text in Windows Update.
