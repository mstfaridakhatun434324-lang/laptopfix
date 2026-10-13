---
title: "How Do I Fix the Windows 11 Green Screen of Death?"
slug: how-do-i-fix-windows-11-green-screen-of-death
date: 2026-09-20
categories: ["windows-errors"]
tags: ["gsod", "insider-build", "crash-fix"]
description: "Seeing a green crash screen on Windows 11? Here's exactly how to fix the Green Screen of Death, from reading the stop code to leaving the Insider program."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-green-screen-of-death.webp"
faqs:
  - q: "I got a green screen instead of a blue screen. Is my Windows broken?"
    a: "No — the green screen is the normal crash screen on Windows Insider preview builds. It works exactly like the blue screen of death and carries the same stop codes. Seeing green simply tells you the laptop is running a Dev, Beta, or Canary test build of Windows 11 rather than the stable release."
  - q: "How do I check which Insider build I'm on?"
    a: "Press Win + R, type winver, and press Enter. The About Windows dialog shows your version and build number, and if it mentions an Insider channel you are on a preview build. You can also open Settings, go to Windows Update, then Windows Insider Program to see your enrolled channel."
  - q: "Can I fix a GSOD without reinstalling Windows?"
    a: "Yes, in most cases. Updating or rolling back the crashing driver, removing incompatible antivirus or VPN software, and repairing system files with SFC and DISM resolve the majority of GSODs. Reinstalling is only needed if you want to leave the Dev or Canary channel, which cannot be done in place."
  - q: "How long does it take to get back to stable Windows?"
    a: "If you are on the Beta channel, unenrolling takes effect with the next major release and requires no reinstall. From Dev or Canary, a clean install takes one to three hours including backups, driver installation, and Windows Update. Plan it for a time you don't need the laptop."
---
If your Windows 11 laptop just crashed to a green screen, you're probably wondering two things: what just happened, and how to make it stop. Short answer: the green screen of death (GSOD) is the same crash as the blue screen of death, shown in green because your laptop is running a Windows Insider preview build. Longer answer: here's the exact sequence to fix it, starting with the five-minute checks and ending with the nuclear option of leaving the Insider program.

Don't skip the order. Most GSODs are fixed by the first three steps below, and jumping straight to a reinstall wastes an afternoon you didn't need to spend. Grab the stop code from the crash screen first — everything else flows from it.

## Why this happens

- **Preview kernel changes in your Insider build** introduce bugs or stricter checks that stable Windows 11 doesn't have, and your hardware trips one of them.
- **A driver that was fine on stable Windows breaks on the preview build** — graphics, Wi-Fi, and chipset drivers are the most common victims after a new Insider flight.
- **Security or VPN software with kernel-level hooks** that haven't been updated for the Insider build's internals, causing a crash on boot or during network activity.
- **A corrupted update**: Insider flights are big and occasionally land half-applied, leaving system files mismatched.
- **Real hardware problems** — bad RAM or a failing SSD crash Insider builds just like stable ones, and the green color doesn't rule hardware out.
- **Overclocking, undervolting, or "optimizer" utilities** that were stable before but cross new limits in the preview kernel.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Capture the stop code

You can't fix what you haven't identified. The stop code is printed on the green screen itself.

1. If the crash is still on screen, photograph it or write down the all-caps code at the bottom, such as `DRIVER_IRQL_NOT_LESS_OR_EQUAL`.
2. After the reboot, open **Event Viewer** (**Win + X** → **Event Viewer**), go to **Windows Logs** → **System**, and look for **BugCheck** entries that confirm the code and its parameters.
3. Install **WinDbg Preview** from the Microsoft Store, press **Ctrl + D**, open the newest dump in `C:\Windows\Minidump`, and run `!analyze -v`.
4. Note the **IMAGE_NAME** value — that file is the driver you'll target in Fix 2.

Once you have a code, you can also look up code-specific guides — for example, our walkthrough for [general blue screen crashes](/articles/how-to-fix-blue-screen-of-death-windows-11/) uses the same repair playbook.

### Fix 2: Update or roll back the crashing driver

Nine times out of ten, the named driver just needs a different version — newer or older, depending on which direction the Insider flight broke it.

1. Open **Device Manager** (**Win + X** → **Device Manager**) and locate the device behind the crashing driver.
2. Right-click it → **Properties** → **Driver** tab. If **Roll Back Driver** is clickable, use it to return to the pre-flight version.
3. If rollback is greyed out, choose **Uninstall device**, tick **Attempt to remove the driver**, restart, and let Windows install its inbox driver.
4. For GPU-related GSODs, install the newest driver from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html), since GPU vendors patch for Insider builds fastest.

### Fix 3: Boot into Safe Mode and strip out conflicting software

If the laptop GSODs during normal boot, Safe Mode lets you remove the software doing it.

1. Hold **Shift** while clicking **Restart** from the Start menu to reach the recovery environment.
2. Go to **Troubleshoot** → **Advanced options** → **Startup Settings** → **Restart**, then press **4** for Safe Mode.
3. In Safe Mode, open **Settings** → **Apps** → **Installed apps** and uninstall third-party antivirus, VPNs, firewalls, RGB control software, and game overlays.
4. Restart normally. If the GSODs stop, reinstall needed tools one at a time from their latest versions.

Our full Safe Mode walkthrough covers [every way to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode-on-laptop/) if the Shift+Restart path doesn't work for you.

### Fix 4: Repair system files and test memory

A half-applied Insider flight leaves corruption that SFC and DISM were made for.

1. Open **Terminal (Admin)** (**Win + X** → **Terminal (Admin)**).
2. Run `sfc /scannow` and let it complete without closing the window.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**, and let the memory test finish to rule out faulty RAM.

### Fix 5: Install the newest flight or pause updates

Your GSOD might be a known bug in the flight you're on, already fixed in the next one.

1. Go to **Settings** → **Windows Update** and install any newer Insider build available.
2. Check the release notes for your flight on the Windows support site for documented GSOD issues and workarounds.
3. If the crashes began with the current flight, pause updates (**Windows Update** → **Advanced options**) for a few weeks while Microsoft ships fixes.
4. Search Feedback Hub for your stop code — highly upvoted crashes usually get official responses or workarounds quickly.

### Fix 6: Leave the Insider program

If every flight brings new crashes and you need a dependable laptop, the preview builds are the problem, not any single bug.

1. Open **Settings** → **Windows Update** → **Windows Insider Program**.
2. On Beta, select **Stop getting preview builds** — you'll return to stable with the next major release, no reinstall required.
3. On Dev or Canary, back up your files and do a clean install using media from the official Windows 11 download page.
4. After the reinstall, get drivers from your laptop maker's support site rather than letting old Insider-era drivers linger.

### Fix 7: Rule out failing hardware

GSODs that survive a clean stable install are a hardware red flag.

1. Run your laptop's built-in UEFI diagnostics (usually **F2**, **F12**, or **Esc** at boot) and run the full component scan.
2. Check SSD health with the drive maker's tool and look at SMART data for reallocated or pending sectors.
3. If you have two RAM sticks, test with one at a time to isolate a bad module.
4. Replace whatever fails — no software fix survives dying hardware, green screen or blue.

## Closing

Fixing the Windows 11 green screen of death comes down to a simple chain: read the stop code, fix the driver or software behind it, repair any update damage, and — if the Insider builds keep biting — step back to stable Windows. Most people are done by Fix 3. And if you decide preview builds aren't for your daily driver, that's not giving up; it's the most reliable fix on this entire list.
