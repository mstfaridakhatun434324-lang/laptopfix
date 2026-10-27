---
title: "How to Fix NPU Driver Error Code 38 on Your AI PC"
slug: npu-driver-error-code-38-fix
date: 2026-10-27
categories: ["ai-pc"]
tags: ["npu driver", "error code 38", "device manager", "copilot+ pc", "windows 11", "troubleshooting"]
description: "Fix NPU driver error code 38 on your AI PC with step-by-step driver removal, clean reinstall, BIOS checks, and Windows Update repair for Copilot+ features."
thumbnail: "/images/thumbs/npu-driver-error-code-38-fix.webp"
faqs:
  - q: "What does NPU error code 38 mean?"
    a: "Code 38 means Windows cannot load the NPU driver because a previous instance of the driver is still in memory. It usually appears after a failed update, a driver conflict, or a resume from sleep that left the old driver loaded."
  - q: "Will restarting fix error code 38?"
    a: "Sometimes. A full restart can clear the stuck driver instance. If the error returns after a restart, the driver itself is damaged or conflicting, and you need a clean reinstall rather than another restart."
  - q: "Can Windows Update cause code 38 on the NPU?"
    a: "Yes. Windows Update can install a generic or mismatched NPU driver over your laptop maker's validated driver. Reinstalling the maker's driver and blocking the bad update usually resolves it."
  - q: "Do I need to replace hardware if code 38 persists?"
    a: "Rarely. Code 38 is almost always a software or driver problem. Only consider hardware service if a clean driver reinstall, BIOS update, and Windows repair all fail on the same machine."
---

Device Manager shows your neural processing unit with a yellow warning, and its properties read: "Windows cannot load the device driver for this hardware because a previous instance of the device driver is still in memory. (Code 38)." Copilot+ features such as Recall, Cocreator, and live captions may stop working at the same time, even though the rest of the laptop seems fine.

Code 38 is a driver-state problem, not a dead NPU. Windows believes the old driver is still loaded, so it refuses to load the new one. That stuck state often follows a failed update, a sleep or hibernation resume, or two drivers fighting over the same device.

This guide gives you six fixes in the right order: clear the stuck driver, reinstall cleanly, then check BIOS and Windows Update. Test the NPU in Device Manager after each step before moving on.

## Why this happens

- **Previous driver instance still loaded:** A driver that failed to unload during shutdown, sleep, or an update stays in memory, blocking the replacement driver from loading.
- **Mismatched or generic NPU driver:** Windows Update may install a driver meant for a different NPU model, or a generic package that cannot initialise your specific chip.
- **Interrupted driver update:** A laptop that slept, lost power, or restarted mid-install can leave half-installed driver files that Windows cannot load cleanly.
- **Conflict with chipset or GPU drivers:** The NPU shares platform resources with the chipset and graphics stack, so a broken chipset or GPU driver can prevent the NPU driver from starting.
- **BIOS or firmware out of step:** An old BIOS may not expose the NPU correctly to Windows 11, especially after a major Windows feature update changes what the OS expects.
- **Corrupted driver store:** Damaged files in the Windows driver store can make every reinstall attempt load the same broken package again. A similar stuck-driver pattern can also follow resume problems, as seen with an [NPU missing after hibernation](/articles/npu-not-detected-after-hibernation-fix/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Do a full restart, not a fast shutdown

Fast Startup saves driver state to disk, which can preserve exactly the stuck instance causing code 38. A true restart clears memory and gives the driver a clean load attempt.

1. Close all apps and save your work, then choose **Restart** — do not use Shut down with Fast Startup enabled.
2. After the restart, open **Device Manager > Neural processors** or **System devices** and check the NPU status.
3. If code 38 is gone, open a Copilot+ feature such as live captions to confirm the NPU actually works.
4. If the error remains, hold **Shift** while choosing Shut down for a cold boot, then power on and recheck.
5. A cold boot that clears the error points to a resume or Fast Startup problem — keep Fast Startup off if the error keeps returning after sleep.

### Fix 2: Uninstall the NPU driver and let Windows redetect it

Removing the driver forces Windows to drop the stuck instance and build a fresh device entry. Do this cleanly, with the driver-removal option checked, or the same broken files will reload.

1. In Device Manager, right-click the NPU device and choose **Uninstall device**.
2. Check **Attempt to remove the driver for this device** if the option appears, then confirm.
3. Restart the PC and let Windows redetect the NPU automatically.
4. Check Device Manager again: a clean device entry with no warning means the stuck instance is gone.
5. If Windows reinstalls the same broken driver, note its version and date — you will replace it manually in the next fix.

### Fix 3: Install the laptop maker's validated NPU driver

Your laptop maker's driver package is validated for your exact NPU, BIOS, and Windows build. Generic or Windows Update drivers are the most common source of a recurring code 38.

1. Find your exact model in **Settings > System > About** and your current BIOS version.
2. Download the latest NPU, chipset, and AI engine drivers from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) support.
3. Install the chipset driver first, then the NPU driver, running each installer as administrator.
4. Restart when prompted and check Device Manager for a clean NPU entry with no code.
5. Test a Copilot+ feature to confirm the NPU is working, not merely listed without an error. For chipset-level detection help, Intel's driver detection tool can confirm which platform drivers your machine needs.

### Fix 4: Update the BIOS and platform firmware

An outdated BIOS can present the NPU incorrectly after a Windows update, leaving Windows unable to load any driver for it. Firmware updates are low-risk when done on AC power with no interruptions.

1. Check your BIOS version in **Settings > System > About** or in the BIOS setup screen.
2. Download the BIOS update for your exact model from your laptop maker's support page only.
3. Plug in the charger, close all apps, and run the update without touching the laptop until it restarts itself.
4. After the update, open Device Manager and confirm the NPU appears without a warning.
5. If code 38 returns immediately, the driver — not the BIOS — is still at fault, so return to Fix 3 with a different driver version.

### Fix 5: Clean the driver store and block the bad update

If every reinstall loads the same broken driver, the Windows driver store itself holds the bad package. Cleaning it and blocking that update breaks the loop.

1. In Device Manager, uninstall the NPU driver again with driver removal checked, then restart.
2. Install the maker's driver from Fix 3 before Windows Update runs, so the good driver is in place first.
3. Open **Settings > Windows Update** and check whether it immediately offers a different NPU driver.
4. If it does, check Microsoft's Windows support pages for the supported way to hide or pause that specific driver update.
5. Recheck Device Manager after the next Windows Update cycle to confirm the good driver survived. Driver conflicts like this can also affect unrelated apps, so the same clean-reinstall discipline helps when [Telegram misbehaves on ARM Windows](/articles/telegram-arm-windows-issues-fix/).

### Fix 6: Repair Windows system files and test a clean profile

When code 38 survives every driver fix, Windows itself may be damaged. System repair is slower, but it is the right last step before considering hardware service.

1. Open an elevated terminal and run **System File Checker**, then the DISM image repair commands if it reports damage.
2. Restart and check the NPU in Device Manager before reinstalling any driver.
3. If the error persists, create a fresh local user account and check Device Manager there to rule out profile-level corruption.
4. As a final software step, consider a Windows repair install that keeps your files, then reinstall the maker's NPU driver.
5. If code 38 still appears on a clean Windows install with the maker's driver, contact your laptop maker's support — that pattern points to hardware. Similar persistence checks apply when [Cocreator generative erase fails](/articles/cocreator-generative-erase-not-working/) despite a healthy-looking driver list.

## Closing

Error code 38 means Windows is stuck on an old driver instance, not that your NPU has failed. Restart fully, uninstall with driver removal, install your laptop maker's validated driver, and update the BIOS if the problem returns. That sequence clears the stuck state in most cases, and only a failure on a clean Windows install should push you toward hardware service.
