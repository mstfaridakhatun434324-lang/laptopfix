---
title: "DRIVER_VERIFIER_IOMANAGER_VIOLATION on Windows 10 — How to Stop It"
slug: how-to-fix-driver-verifier-iomanager-violation-on-windows-10
date: 2026-09-16
categories: ["windows-errors"]
tags: ["windows-10", "driver-verifier", "bsod"]
description: "DRIVER_VERIFIER_IOMANAGER_VIOLATION on Windows 10 means a forgotten Driver Verifier is crashing your PC on purpose. Here is the exact off-switch."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-iomanager-violation-on-windows-10.webp"
faqs:
  - q: "What does DRIVER_VERIFIER_IOMANAGER_VIOLATION mean on Windows 10?"
    a: "Driver Verifier — a built-in Windows driver stress-test tool — is active and caught a driver mishandling I/O requests. Verifier responds to violations by crashing the system deliberately. It is a testing tool, not a protection feature, and it should not be running on a normal-use Windows 10 laptop. Turning it off stops the crashes immediately."
  - q: "How do I open Driver Verifier Manager on Windows 10?"
    a: "Press Win + R, type verifier, and press Enter. Choose 'Delete existing settings' and click Finish, then restart. If the GUI will not open or crashes prevent reaching the desktop, use Safe Mode and run verifier /reset from an admin Command Prompt instead — it does the same thing more reliably."
  - q: "The crashes started after a Windows 10 update. Is the update the cause?"
    a: "Indirectly. The update did not enable Verifier — it was already on, silently. What the update did was change drivers or validation rules so that a driver finally tripped Verifier's I/O checks. That is why the crashes seem to 'start' with the update. Disable Verifier first, then update the flagged driver so the underlying issue is resolved too."
  - q: "Can System Restore fix this instead of messing with Verifier?"
    a: "Yes, and it is often the easier path. Boot into the Recovery Environment, choose Troubleshoot > System Restore, and pick a restore point from before the crashes began. This reverts driver and registry changes — including the Verifier settings that are stressing the driver. Your personal files are untouched, though you may need to reinstall apps added after that point."
---

DRIVER_VERIFIER_IOMANAGER_VIOLATION on Windows 10 has the same punchline as on Windows 11: somebody (or some tool) switched on Driver Verifier, forgot about it, and now it is crashing your laptop on purpose every time a driver mishandles an I/O request. The crashes feel random, but they are anything but — Verifier is doing exactly what it was told to do.

Here is the Windows 10-specific path to turning it off and fixing the driver underneath.

## Why this happens

- **Driver Verifier was enabled and abandoned.** A diagnostic tool, a support session, or a "PC repair" utility turned it on months or years ago.
- **A Windows 10 feature update changed the drivers.** Updates like 22H2 swap or modify drivers, and the new versions trip Verifier's I/O checks.
- **Aging third-party drivers.** Old antivirus, VPN, or disk-utility filter drivers that have not been updated for current Windows 10 builds.
- **Corrupted driver files.** Years of incremental updates leave mismatched `.sys` files that fail I/O validation.
- **A genuinely faulty driver.** Sometimes Verifier is right — a driver really is corrupting I/O request packets, and the crash prevented data loss.
- **Failing storage hardware.** A dying drive or bad RAM can cause I/O errors that Verifier interprets as driver violations.
- **Overclocking or unstable BIOS settings.** Marginal hardware timing causes I/O glitches under Verifier's microscope.

## How to fix it

Work through these in order, using Windows 10's menus.

### Fix 1: Disable Driver Verifier

This stops the crashes. Do it before anything else.

1. Press **Win + R**, type `verifier`, press **Enter** → select **Delete existing settings** → **Finish** → restart the laptop.
2. Command-line alternative (more reliable): right-click **Start** → **Command Prompt (Admin)** → run `verifier /reset` → restart.
3. If crashes block booting: hold **Shift** while clicking **Restart** → **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart** → press **4** for Safe Mode, then run the command from an admin prompt.
4. Verify afterward: run `verifier /query` in an admin Command Prompt. It should report no drivers under verification.
5. Use the laptop for a full day. If the crashes are gone, Verifier was the entire problem.

### Fix 2: Identify the driver Verifier was flagging

Do not just mute the alarm — find out what it was warning about.

1. Confirm crash dumps are enabled: right-click **Start** → **System** → **Advanced system settings** → **Startup and Recovery** → **Settings** → **Small memory dump (256 KB)**.
2. Install WinDbg Preview from the Microsoft Store, open the newest `.dmp` in `C:\Windows\Minidump`, and run `!analyze -v`.
3. Note the `IMAGE_NAME` — search the file name to identify the device it belongs to.
4. If the blue screen named a `.sys` file directly, skip WinDbg and target that driver now.

### Fix 3: Update the flagged driver from the manufacturer

Windows 10's automatic driver updates are part of how this mess started — go to the source instead.

1. Identify your exact laptop model: press **Win + R**, type `msinfo32`, read **System Model**.
2. Visit the manufacturer's support site (Dell, HP, Lenovo, ASUS, Acer), enter the model, and download the latest Windows 10 drivers — especially **chipset**, **storage**, **network**, and **graphics**.
3. For Intel hardware, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the correct drivers automatically.
4. Install chipset first, then the rest, restarting between groups.

### Fix 4: Remove outdated security and utility software

Old kernel-level software is the classic Verifier tripwire on Windows 10.

1. Open **Control Panel** → **Programs** → **Programs and Features** and sort by install date — look at the oldest entries first.
2. Uninstall ancient antivirus products, old VPN clients, and "system optimizer" tools. Use each vendor's dedicated removal tool to clear leftover filter drivers.
3. Make sure Windows Defender is active afterward (**Settings** → **Update & Security** → **Windows Security**).
4. If you reinstall third-party security software, get the current version — vendors fix Verifier-flagged issues in newer releases.

### Fix 5: Clean-reinstall the graphics driver

Graphics drivers are the most common Verifier I/O violators, so give yours a clean slate.

1. Download Display Driver Uninstaller and the latest driver for your GPU.
2. Disconnect from the internet, boot into Safe Mode, run DDU → **Clean and restart**.
3. Install the fresh driver and restart.
4. Microsoft's [Windows support documentation](https://support.microsoft.com/en-us/windows) confirms the standard driver troubleshooting flow if you want the official version.

### Fix 6: Run SFC, DISM, and chkdsk

Repair the files underneath the drivers.

1. Right-click **Start** → **Command Prompt (Admin)**.
2. Run `sfc /scannow` to completion.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` (needs internet).
4. Run `chkdsk C: /f` — type `Y` to schedule it and restart so it runs before Windows loads.
5. After all three, run `sfc /scannow` once more and restart normally.

### Fix 7: Stop Windows 10 from re-breaking drivers, and test hardware

Lock in the fix and rule out hardware.

1. Prevent driver downgrades: **Win + R** → `sysdm.cpl` → **Hardware** → **Device Installation Settings** → **No** → **Save Changes**.
2. Test RAM: **Win + R** → `mdsched.exe` → **Restart now and check for problems**.
3. Check the drive: `wmic diskdrive get status` in an admin prompt — every drive should say **OK**.
4. If hardware passes and crashes stay gone with Verifier off, you are done. If a specific driver keeps misbehaving, roll it back (**Device Manager** → device → **Properties** → **Driver** → **Roll Back Driver**).

## Closing

On Windows 10, DRIVER_VERIFIER_IOMANAGER_VIOLATION is almost always archaeology: some long-forgotten tool enabled Verifier, and a recent update finally gave it something to crash about. The `verifier /reset` command is the whole battle — the driver updates afterward are just good hygiene so the underlying flaw does not cause subtler problems later. And while you are here, lock down Windows 10's automatic driver updates (Fix 7), because that habit is how these driver messes start. For the step-by-step edition, see [DRIVER_VERIFIER_IOMANAGER_VIOLATION step by step](/articles/how-to-fix-driver-verifier-iomanager-violation-step-by-step/); for the sibling stop code, [DRIVER_VERIFIER_DETECTED_VIOLATION on Windows 10](/articles/how-to-fix-driver-verifier-detected-violation-on-windows-10/).
