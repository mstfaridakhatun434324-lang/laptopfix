---
title: "NPU Driver Error Code 39 Fix on Windows 11: Driver Is Missing or Corrupted"
slug: npu-driver-error-code-39-fix
date: 2026-10-22
categories: ["ai-pc"]
tags: ["npu","windows-11","device-manager","error-code-39","troubleshooting","ai-pc"]
description: "Code 39 in Device Manager means your NPU driver is missing or corrupt. Follow this step-by-step Windows 11 guide to restore your AI PC's neural processor."
thumbnail: "/images/thumbs/npu-driver-error-code-39-fix.webp"
faqs:
  - q: "What does Code 39 mean on an NPU in Device Manager?"
    a: >
      Code 39 means Windows cannot load the device driver because it is
      missing or corrupted. For an NPU, this usually follows a failed
      Windows Update, an incomplete OEM driver install, or a corrupted
      driver store. The neural processor hardware is almost always fine;
      only the software stack needs repair.
  - q: "Can Code 39 be caused by a hardware failure?"
    a: >
      Rarely. Code 39 is specifically a driver-loading failure, not a
      hardware fault. If the NPU shows a different code, such as Code 43
      or Code 10, the story may differ. But Code 39 alone points to
      corrupted, missing, or blocked driver files, which software fixes
      can resolve.
  - q: "Will reinstalling Windows fix NPU Code 39?"
    a: >
      Usually not necessary. A clean NPU driver install from your laptop
      maker's support page or Windows Update resolves Code 39 in most
      cases. Reinstalling Windows is a last resort after driver cleanup,
      System File Checker, and a BIOS reset have all been tried.
  - q: "Why does Code 39 return after I fix it?"
    a: >
      The most common cause is Windows Update pushing an older or
      conflicting NPU driver over your working one. Pausing driver
      updates or using the "prevent this driver" policy after a successful
      manual install usually stops the cycle.
---

You open Device Manager to figure out why Copilot+ features went quiet, and there it is: a yellow warning triangle on your neural processing unit. Open its properties and Windows tells you it "cannot load the device driver" with error Code 39, meaning the driver is missing or corrupted. The good news is that this is almost never a dead chip. The NPU itself — whether Intel AI Boost, AMD Ryzen AI, or Qualcomm Hexagon — is a separate silicon block that does not fail from a bad driver file.

The frustration is real, though, because Code 39 tends to appear right after a Windows Update or an OEM driver refresh. One moment Recall snapshots are saving and Studio Effects are smoothing your webcam; the next, Device Manager reports the driver cannot load and every AI workload silently falls back to the CPU or fails outright. If you have seen the closely related [Code 43 stop error on your NPU](/articles/npu-driver-error-code-43/) or the [device-cannot-start Code 10](/articles/npu-error-code-10-device-cannot-start/), you know the drill: Windows can see the hardware, but the software handshake is broken. Fixing that handshake is exactly what this guide does.

Work through the fixes below in order, starting with the gentle repairs and ending with the deep clean. Also bookmark our guide on [manually installing the Intel NPU driver from INF files](/articles/manually-install-intel-npu-driver-inf/) in case you need a fully offline driver install later. And while your NPU is down, you may notice side effects elsewhere — for example, [Click to Do losing its Translate text option](/articles/click-to-do-translate-text-missing/) or the [Studio Effects blur strength slider misbehaving](/articles/studio-effects-blur-strength-adjustment/) — both of which depend on the NPU driver loading cleanly, so fix Code 39 first and recheck them after.

## Why this happens

- **Corrupted driver store entry:** The NPU driver package in Windows' DriverStore got damaged during an update, so the service cannot load the .sys and .inf files it needs.
- **Failed Windows Update:** A cumulative or driver update was interrupted mid-install, leaving a half-written NPU driver that Windows refuses to load.
- **Conflicting driver versions:** An OEM driver and a Windows Update driver both claim the same device, and the resulting mix of binaries is inconsistent.
- **Deleted or quarantined files:** Overzealous cleanup tools or antivirus quarantines sometimes remove NPU driver components, triggering Code 39 on next boot.
- **Corrupted system files:** Damaged system components that the NPU driver depends on (like the driver framework runtime) can make a healthy driver fail to load.
- **Stale registry references:** Old driver registration data points at files that no longer exist after a version change, confusing the driver loader.
- **Disabled driver signature or test mode:** Rare on laptops, but booting with driver signature enforcement off (or with leftover test-signing state) can block the NPU driver from loading.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Restart and run the hardware troubleshooter

Before touching drivers, rule out a transient load failure. Code 39 can occasionally appear when the driver fails to load once due to a race at startup, and a clean reboot resolves it.

1. Save your work and restart the laptop — use Restart, not Shut down, so Fast Startup does not skip the clean boot path.
2. Open Device Manager (right-click Start, then Device Manager) and expand the NPU entry, usually under "Neural processors" or "System devices".
3. Right-click the NPU and choose "Scan for hardware changes" to force Windows to re-attempt driver loading.
4. If the error persists, open Settings > System > Troubleshoot > Other troubleshooters and run "Hardware and Devices" if available.
5. Check the device's Properties > General tab again to see whether the Code 39 message changed or cleared.

### Fix 2: Uninstall the device and let Windows reinstall

The quickest genuine fix is a clean reinstall of the driver from the driver store. This clears stale registration and lets Windows pick a consistent driver package.

1. In Device Manager, right-click the NPU with the Code 39 warning and choose "Uninstall device".
2. In the confirmation dialog, check "Attempt to remove the driver for this device" if the option appears.
3. Click Uninstall, then restart the laptop immediately — do not skip the reboot.
4. After signing back in, wait two to three minutes for Windows to detect the NPU and reinstall the driver automatically.
5. Return to Device Manager and confirm the yellow triangle is gone and the device status reads "This device is working properly".

### Fix 3: Install the OEM NPU driver from your laptop maker

Generic Windows drivers sometimes lack the exact firmware pairing your laptop needs. The OEM package is the safest match, and [Microsoft's own guidance](https://support.microsoft.com/en-us/windows) recommends getting hardware drivers from the device manufacturer when Windows' own fail.

1. Find your exact laptop model on the support site: [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
2. Search for your model and open its drivers page; filter by your Windows 11 build if the site offers it.
3. Download the NPU / AI Boost / Ryzen AI driver package (it may be listed under Chipset or Neural Processor).
4. Run the installer as administrator and follow the prompts, then restart when it finishes.
5. Verify in Device Manager that the NPU shows no error and check the Driver tab for the new version and date.

### Fix 4: Update through Windows Update and the Update Catalog

If the OEM package is unavailable or outdated, Microsoft's driver pipeline is the next best source. Some NPU drivers ship only through Windows Update or the standalone catalog.

1. Open Settings > Windows Update and click "Check for updates"; install everything offered, including optional driver updates.
2. If nothing relevant appears, visit [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for your NPU name plus "driver".
3. Download the newest package matching your architecture (ARM64 for Snapdragon, x64 for Intel/AMD) and Windows 11.
4. Install the downloaded package, restart, and recheck Device Manager for Code 39.
5. If Code 39 persists, note the driver version Windows reports — you may need it for the deeper cleanup in Fix 6.

### Fix 5: Run SFC and DISM to repair system files

When driver files keep failing to load even after a fresh install, the underlying system files may be damaged. System File Checker and DISM repair the Windows image that drivers depend on.

1. Open Terminal as administrator (right-click Start > Terminal (Admin)).
2. Run `sfc /scannow` and wait for it to finish — this can take 10 to 20 minutes.
3. If SFC reports it could not fix everything, run `DISM /Online /Cleanup-Image /RestoreHealth` next.
4. Restart the laptop after both tools complete, even if no errors were reported.
5. Reopen Device Manager and check whether the NPU now loads without Code 39.

### Fix 6: Clean out old driver packages with pnputil

Stubborn Code 39 cases are often caused by a corrupted driver still registered in the DriverStore. Removing every NPU driver package and starting from zero clears the conflict.

1. Open Terminal as administrator and run `pnputil /enum-drivers | findstr /i "npu"` to list installed NPU driver packages.
2. Note each published name (like oem42.inf) tied to your NPU vendor — Intel, AMD, or Qualcomm.
3. For each one, run `pnputil /delete-driver oemXX.inf /uninstall /force`, replacing oemXX.inf with the real name.
4. Restart, then install the OEM driver package from Fix 3 (do not let Windows pick first).
5. Confirm the NPU loads cleanly, then run Windows Update to make sure nothing immediately overwrites your working driver.

## Closing

Code 39 looks alarming in Device Manager, but it is a software problem with a software solution: remove the broken driver registration, install a clean OEM or Microsoft driver package, and repair the system files underneath if needed. Most laptops are back to full AI acceleration within half an hour of starting Fix 2. Once the NPU is healthy again, the features that depend on it — Recall, Studio Effects, [Click to Do's Translate text](/articles/click-to-do-translate-text-missing/), and [Studio Effects blur strength control](/articles/studio-effects-blur-strength-adjustment/) — should recover on their own. If Code 39 keeps returning after Windows Update, pause driver updates for a few weeks so your working driver stays put.
