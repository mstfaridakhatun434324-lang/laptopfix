---
title: "How to Troubleshoot the Windows 11 Green Screen of Death"
slug: troubleshoot-windows-11-green-screen-of-death
date: 2026-09-18
categories: ["windows-errors"]
tags: ["gsod", "windows-11", "blue-screen"]
description: "Green Screen of Death on Windows 11? Learn what a GSOD means, how to read the stop code, and the exact troubleshooting steps to stop the crashes."
thumbnail: "/images/thumbs/troubleshoot-windows-11-green-screen-of-death.webp"
faqs:
  - q: "What is the difference between a green screen and a blue screen of death?"
    a: "Functionally, none — both are the same Windows crash screen with a stop code. The green background appears on Windows Insider preview builds instead of blue, so Microsoft can tell crash reports from testers apart from stable-release crashes. If you see green, you are running a Dev, Beta, or Canary build of Windows 11."
  - q: "Does a GSOD mean my laptop hardware is broken?"
    a: "Not necessarily. On Insider builds, GSODs are most often caused by unfinished drivers or preview kernel changes clashing with third-party software. That said, the same checks apply: faulty RAM or a failing SSD can cause GSODs on any build. Work through driver and hardware diagnostics before assuming the preview build is at fault."
  - q: "How do I leave the Insider program to stop getting GSODs?"
    a: "Open Settings, go to Windows Update, then Windows Insider Program, and choose Stop getting preview builds. On Dev or Canary builds you usually cannot roll back without a clean install, so unenrolling takes effect on the next major release. Beta channel users can often switch off previews without reinstalling."
  - q: "Where do I find the stop code from a GSOD?"
    a: "The stop code is shown at the bottom of the green screen itself, in all caps, like MEMORY_MANAGEMENT or DRIVER_IRQL_NOT_LESS_OR_EQUAL. If it flashed by too quickly, open Event Viewer, go to Windows Logs, then System, and look for BugCheck entries — they record the exact stop code and parameters of every crash."
---
A green screen of death looks alarming the first time you see it, but take a breath: it is the exact same crash screen as the familiar blue screen, just wearing a different color. Microsoft paints the crash screen green on Windows Insider preview builds so engineers can instantly tell a tester crash apart from a stable-release crash. Everything you know about reading and fixing blue screens applies here too.

The twist is that Insider builds crash more often by design. You are running unfinished code, and unfinished graphics drivers, preview kernel changes, and half-baked features all raise the odds of a GSOD. So the troubleshooting path has two branches: fix the specific stop code, and decide whether staying on the preview build is worth the instability. Let's handle both.

## Why this happens

- **You are on a Windows Insider build** (Dev, Beta, or Canary), where preview kernel and driver changes introduce crashes that don't exist on stable Windows 11.
- **A third-party driver that worked on stable Windows 11 breaks on the preview kernel** — GPU, Wi-Fi, and audio drivers are the usual suspects after a new Insider flight lands.
- **Antivirus, VPN, or overlay software** with kernel hooks that haven't been updated for the Insider build's changed internals.
- **Overclocked or undervolted hardware** whose margins were fine on stable but trip new, stricter checks in preview builds.
- **Genuine hardware faults** — failing RAM or a dying SSD cause GSODs exactly like they cause blue screens, regardless of build.
- **Corrupted system files** from a failed Insider update that left the component store half-updated.

## How to fix it

Work through these in order, from quickest to most involved.

### Fix 1: Read the stop code and check the dump

Don't treat "green screen" as the diagnosis. The stop code at the bottom of the screen is the actual diagnosis.

1. Next time it crashes, photograph the screen or note the all-caps stop code, e.g. `VIDEO_TDR_FAILURE` or `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED`.
2. After rebooting, press **Win + X** and open **Event Viewer**. Navigate to **Windows Logs** → **System** and filter for **BugCheck** events to confirm the code.
3. For deeper analysis, install **WinDbg Preview** from the Microsoft Store, open the latest `.dmp` in `C:\Windows\Minidump` with **Ctrl + D**, and run `!analyze -v`.
4. Write down the **IMAGE_NAME** — that driver is your prime suspect for Fix 2.

If the code points at a specific driver file, our guide to [fixing blue screens on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the same repair steps in more detail.

### Fix 2: Roll back or update the suspect driver

Insider builds break drivers constantly. The fix is almost always a driver version change in one direction or the other.

1. Open **Device Manager** (**Win + X** → **Device Manager**) and find the device tied to the crashing driver.
2. Right-click it, choose **Properties**, go to the **Driver** tab, and click **Roll Back Driver** if the button is active — this returns you to the version that worked before the Insider flight.
3. If rollback isn't available, choose **Uninstall device** (tick **Attempt to remove the driver**), restart, and let Windows install its inbox driver.
4. For graphics crashes specifically, grab the latest driver directly from [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel's driver tool](https://www.intel.com/content/www/us/en/support/detect.html) — GPU vendors ship Insider-compatible drivers faster than Windows Update does.

### Fix 3: Uninstall kernel-hooking software

Preview kernels change internal structures that third-party drivers hook into. Software that was rock solid on stable Windows 11 can GSOD an Insider build on day one.

1. Open **Settings** → **Apps** → **Installed apps** and remove third-party antivirus, VPN clients, firewall tools, and game overlays one group at a time.
2. Press **Win + R**, type `appwiz.cpl`, and check for old driver packages (printer drivers, phone sync tools) you no longer use — remove them too.
3. Restart after each round of removals and give the laptop a normal day of use before deciding the crash is fixed.
4. Reinstall only the tools you actually need, always the newest version, which is most likely to support your Insider channel.

### Fix 4: Run the standard crash repairs (SFC, DISM, memory test)

Insider updates sometimes land half-applied. These built-in repairs clean up the damage.

1. Open **Terminal (Admin)** (**Win + X** → **Terminal (Admin)**) and run `sfc /scannow`. Wait for it to finish completely.
2. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store.
3. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**, and let the memory test finish — rule out RAM before blaming the preview build.
4. Restart normally afterward. If SFC found and fixed corruption, watch for a few days: one-off corruption after a bad update flight is common and usually doesn't return.

### Fix 5: Update to the newest Insider flight — or pause updates

Sometimes the GSOD is a known bug in your current flight that Microsoft already fixed in the next one.

1. Open **Settings** → **Windows Update** and click **Check for updates**. Install any newer Insider build offered.
2. Read the flight's release notes on the Windows Insider blog for known GSOD issues and their workarounds before installing.
3. If crashes started with the latest flight and you need a stable machine now, go to **Windows Update** → **Advanced options** and pause updates for up to 5 weeks while the next flight matures.
4. Keep an eye on the Feedback Hub for your stop code — upvoted crash reports often get official workarounds within days.

### Fix 6: Switch channels or leave the Insider program

If GSODs keep coming and you need the laptop for real work, the preview build itself is the problem.

1. Go to **Settings** → **Windows Update** → **Windows Insider Program**.
2. On the Beta channel, choose **Stop getting preview builds** to glide back to stable at the next release — no reinstall needed.
3. On Dev or Canary, leaving requires a clean install: back up your files, create Windows 11 media from the official Windows 11 download page, and reinstall.
4. After returning to stable, reinstall drivers from your laptop maker's support site — Insider-era drivers sometimes linger and cause odd issues on stable builds.

This is also the right moment to reconsider whether the machine should have been on Insider builds at all. A daily-driver laptop and preview software are a rough combination.

### Fix 7: Test the hardware

If GSODs survive a channel switch or a clean install, stop blaming software.

1. Run the memory diagnostic (`mdsched.exe`) and your SSD maker's health tool; check SMART status for reallocated sectors.
2. Monitor temperatures with your laptop maker's utility — thermal shutdowns during heavy loads can present as crashes on some firmware.
3. Boot into your BIOS/UEFI diagnostics (usually **F2** or **F12** at the logo, or a dedicated key) and run the full hardware scan.
4. If diagnostics flag the RAM or SSD, replace the part — and note that crashes matching the [WHEA uncorrectable error pattern](/articles/whea-uncorrectable-error-windows-11-fix/) are almost always hardware, on any build color.

## Closing

A green screen of death is just a blue screen on a test build of Windows — same stop codes, same fixes, plus one extra question about whether you should be running preview software on a machine you depend on. Read the stop code, fix the driver or software behind it, and if the crashes keep pace with every new flight, step back to the stable channel. The Insider program is for testing Windows, not for testing your patience.
