---
title: "How to Fix DRIVER_VERIFIER_DETECTED_VIOLATION in Windows 11"
slug: how-to-fix-driver-verifier-detected-violation
date: 2026-09-21
categories: ["windows-errors"]
tags: ["bsod", "driver-verifier", "drivers"]
description: "Stuck in a DRIVER_VERIFIER_DETECTED_VIOLATION blue screen loop? Learn how to disable Driver Verifier, find the bad driver, and boot normally again."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-detected-violation.webp"
faqs:
  - q: "What is Driver Verifier and why is it crashing my laptop?"
    a: "Driver Verifier is a built-in Windows testing tool that stress-tests drivers for bugs. It is off by default — it usually gets turned on by a troubleshooting guide, a developer tool, or malware. Once enabled, it deliberately crashes the system with DRIVER_VERIFIER_DETECTED_VIOLATION the moment a driver misbehaves, which can trap you in a boot loop."
  - q: "How do I turn off Driver Verifier if Windows won't boot?"
    a: "Boot into Safe Mode or the Windows Recovery Environment, open Command Prompt, and run verifier /reset. This disables all Verifier checks immediately. Restart normally afterward. If Safe Mode also crashes, use installation media to reach the recovery Command Prompt and run the same command there."
  - q: "Will disabling Driver Verifier delete anything?"
    a: "No. The verifier /reset command only clears Verifier's settings and stops the stress-testing. It doesn't uninstall drivers, delete files, or change your data. Your laptop simply goes back to running drivers normally instead of under Verifier's microscope."
  - q: "Should I ever turn Driver Verifier back on?"
    a: "Only if you are deliberately debugging a driver problem and you know which driver you are testing. For everyday use it should stay off — it slows the system and turns minor driver quirks into full blue screens. If a guide told you to enable it, disable it as soon as your testing is done."
---
DRIVER_VERIFIER_DETECTED_VIOLATION is a special kind of blue screen: it usually means someone — a troubleshooting guide, a piece of software, or sometimes malware — switched on Windows' Driver Verifier, a built-in tool that stress-tests drivers until they break. Verifier did its job and caught a misbehaving driver, but now it crashes your laptop on every boot, and you can't get in to turn it off. Frustrating, but very fixable.

The plan is simple: disable Verifier from outside normal Windows, boot back in, then find and fix the actual bad driver Verifier was complaining about. You don't need to reinstall anything, and your files are safe the whole time.

## Why this happens

- **Driver Verifier was enabled manually** — often by following an online guide that said to run `verifier.exe`, or by a driver-development tool — and left running.
- **A genuinely buggy driver** (often Wi-Fi, Bluetooth, or storage) that trips Verifier's checks the moment Windows loads it.
- **An outdated or mismatched driver version** that worked fine normally but can't survive Verifier's stricter validation.
- **Corrupted driver files** from a failed update, which Verifier flags immediately on load.
- **Third-party "driver updater" tools** that enable Verifier-like stress settings or install poorly tested driver builds.
- **Malware or a bad system tweak** that modified driver loading behavior and gets caught by the checks.
- **A driver that only fails under Verifier's stress conditions** — timing-sensitive bugs that never appear in normal use but crash instantly under Verifier's checks.
- **Leftover Verifier settings from a previous troubleshooting session** months ago, reactivated by a driver update that changed the driver's load order.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Disable Driver Verifier from Safe Mode

This is the fix that breaks the loop, and it's the one step you can't skip — nothing else works until Verifier stops crashing the boot process. Everything else comes after it.

1. Force the recovery environment: power the laptop on, and as soon as the Windows logo appears, hold the power button to force it off. Repeat three times — on the fourth boot, Windows opens **Automatic Repair**.
2. Go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**, then press **4** for Safe Mode.
3. Once in Safe Mode, press **Win + R**, type `verifier.exe`, and press Enter. In the Driver Verifier Manager, select **Delete existing settings** and click **Finish**.
4. Alternatively, open **Terminal (Admin)** and run `verifier /reset`. Restart normally — the loop should be gone.

### Fix 2: Disable Verifier from the recovery Command Prompt

If even Safe Mode crashes, run the same reset from outside Windows entirely.

1. Boot from Windows 11 installation media (USB) and choose **Repair your computer** instead of Install.
2. Go to **Troubleshoot** → **Advanced options** → **Command Prompt**.
3. Type `verifier /reset` and press Enter. You should see a confirmation that Verifier settings were cleared.
4. Type `exit`, remove the USB, and choose **Continue** to boot into Windows normally.

For more on reaching these recovery tools, see our guide to [booting Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/).

### Fix 3: Identify the driver Verifier flagged

Verifier crashed for a reason — find out which driver it caught so you can fix the real problem.

1. After booting normally, install **WinDbg Preview** from the Microsoft Store.
2. Press **Ctrl + D** in WinDbg and open the latest dump from `C:\Windows\Minidump`, then run `!analyze -v`.
3. Look for the **Probably caused by** line and the **IMAGE_NAME** — that's the driver Verifier caught red-handed.
4. Write the name down. Common offenders include old Realtek, Killer Networking, and third-party storage filter drivers.

### Fix 4: Reinstall the offending driver cleanly

Don't just update over the top — remove the bad driver completely first.

1. Open **Device Manager** (**Win + X** → **Device Manager**) and find the device.
2. Right-click → **Uninstall device**, and tick **Attempt to remove the driver for this device** so the bad files are actually deleted.
3. Restart the laptop and let Windows install its inbox driver.
4. Then install the latest stable driver from your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — matched to your exact model and serial number.

### Fix 5: Check for the specific Verifier variant on your system

DRIVER_VERIFIER_DETECTED_VIOLATION has a sibling, the I/O Manager variant, with its own quirks. If your dump names `verifier.sys` alongside an I/O-related driver, compare notes with our guide to the [Driver Verifier I/O Manager violation on Windows 11](/articles/how-to-fix-driver-verifier-detected-violation-on-windows-11/) to make sure you're chasing the right driver class.

### Fix 6: Run SFC and DISM to repair driver store damage

Corrupted system driver files can keep tripping checks even after you reinstall the named driver.

1. Open **Terminal (Admin)** and run `sfc /scannow`. Wait for the full scan.
2. Follow it with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart and use the laptop normally for a day. If no blue screen appears, the store repair finished the job.
4. If crashes persist, run the two commands once more — DISM sometimes needs a second pass after SFC fixes files.

### Fix 7: Scan for malware and remove driver updater tools

If you never enabled Verifier yourself, something else did — and you want to know what.

1. Run a full scan with **Windows Security** (**Settings** → **Privacy & security** → **Windows Security** → **Virus & threat protection** → **Scan options** → **Full scan**).
2. Uninstall any third-party "driver updater" or "PC optimizer" tools — they install questionable driver builds and sometimes toggle Verifier themselves.
3. Check **Task Scheduler** (**taskschd.msc**) for unfamiliar tasks that run at boot and disable anything you don't recognize.
4. Confirm Verifier stays off: run `verifier /query` in an admin terminal — it should report no drivers being verified.

## Closing

DRIVER_VERIFIER_DETECTED_VIOLATION looks like a disaster when it loops on boot, but it's really just a testing tool that was left switched on. Reset it from Safe Mode or the recovery prompt, identify the driver it caught, replace that driver properly, and leave Verifier off for good. Your laptop goes back to running drivers the normal way — quietly, in the background, without crashing to prove a point.
