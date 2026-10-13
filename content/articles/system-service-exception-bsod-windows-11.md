---
title: "System Service Exception BSOD on Windows 11: Repair Guide"
slug: system-service-exception-bsod-windows-11
date: 2026-09-28
categories: ["windows-errors"]
tags: ["system service exception", "windows 11", "bsod repair", "driver"]
description: "Repair guide for SYSTEM_SERVICE_EXCEPTION on Windows 11: update drivers, fix system files, and verify hardware with Windows 11-specific steps."
thumbnail: "/images/thumbs/system-service-exception-bsod-windows-11.webp"
faqs:
  - q: "Why am I getting System Service Exception on Windows 11 specifically?"
    a: "Windows 11's driver model and update cadence expose the usual culprits: GPU drivers (especially after game-ready updates), webcam drivers used by Teams/Zoom, and Wi-Fi drivers during Modern Standby transitions. The stop code is 0x0000003B. Windows 11 also auto-updates drivers more aggressively, so a working driver can be replaced by a buggy one overnight."
  - q: "How do I stop Windows 11 from reinstalling the bad driver?"
    a: "After finding a stable driver version, block the bad one: Settings, Windows Update, Advanced options, turn off 'Receive updates for other Microsoft products' doesn't cover drivers — instead use the 'Show or hide updates' troubleshooter to hide the driver update, or set a Group Policy to exclude drivers from Windows Update. This prevents the exact regression from recurring."
  - q: "Does Windows 11 Safe Mode work the same as Windows 10?"
    a: "Yes, functionally identical — minimal drivers, no third-party software. Access differs slightly: Settings, System, Recovery, Advanced startup, Restart now, then Troubleshoot, Advanced options, Startup Settings. The triple-interrupt method (forcing Automatic Repair) also works unchanged when Windows 11 won't boot."
  - q: "Should I use Windows 11's built-in driver updates or the vendor's?"
    a: "The vendor's, for anything implicated in a crash. Windows Update drivers are convenient but often older or generic; GPU vendors (NVIDIA/AMD/Intel) and laptop OEMs ship tuned, newer versions with crash fixes. Use Windows Update for the OS and vendor installers for graphics, chipset, network, and webcam drivers."
---

SYSTEM_SERVICE_EXCEPTION on Windows 11 (stop code 0x0000003B) follows the same driver-bug script as on Windows 10, but Windows 11 adds its own wrinkles: more aggressive automatic driver updates (a working driver can be swapped for a buggy one overnight), Modern Standby power transitions that stress Wi-Fi and webcam drivers, and game-ready GPU driver churn. This repair guide is Windows 11-specific — the Settings paths, the driver-update behavior, and the recovery flows all match what you'll actually see on screen.

The repair order: identify the faulting driver from the crash, replace it with the right version (newer or older depending on timing), lock in the working version so Windows Update doesn't regress it, then verify system files and hardware. For the fastest fix-order version, see our [best-way guide](/articles/best-way-to-fix-system-service-exception/); for the full diagnostic walkthrough, see our [troubleshooting walkthrough](/articles/system-service-exception-troubleshooting/); for power-transition crashes specifically, see our [driver power state failure guide](/articles/driver-power-state-failure-windows-11-fix/).

## Why this happens

- **GPU driver bugs**: Game-ready and studio driver updates introducing kernel exceptions.
- **Windows Update driver swaps**: The OS replacing a stable vendor driver with a problematic inbox version.
- **Webcam driver faults**: Teams/Zoom-era webcam drivers throwing exceptions during calls.
- **Wi-Fi driver Modern Standby bugs**: Power-transition exceptions on sleep/wake.
- **Antivirus filter drivers**: Kernel hooks faulting after security product updates.
- **Corrupt driver store**: Mixed driver versions from repeated install/rollback cycles.
- **Failing hardware**: RAM or storage corruption faulting innocent drivers.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the driver (Windows 11 paths)

Get the name using Windows 11's tools.

1. Photograph the blue screen's parenthesized `.sys` filename.
2. **Settings** > **Privacy & security** > **Windows Security** > no — for crash history use **Event Viewer** (Windows + X > Event Viewer) > **Windows Logs** > **System** > **BugCheck** events.
3. Analyze `C:\Windows\Minidump` with BlueScreenView for the highlighted faulting driver.
4. Map it: graphics (`nvlddmkm.sys`, `amdkmdag.sys`, `igdkmd64.sys`), network (`Netwtw*.sys`, `rtwlan*.sys`), webcam (`usbvideo.sys` + vendor driver), `dxgmms2.sys` (DirectX graphics subsystem).

### Fix 2: Clean-install the vendor driver

Replace Windows Update's version with the manufacturer's.

1. Download from the vendor: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), Intel DSA, or your laptop OEM's support page (preferred for Wi-Fi/webcam/chipset on laptops).
2. **Device Manager** > uninstall the device with driver removal, then run the vendor installer with **Clean installation**/**Factory reset** checked.
3. If the crash followed a driver update, install the previous known-good version instead of the latest.
4. Restart and test with the original trigger (the game, the video call, the sleep/wake cycle).

### Fix 3: Block the bad driver from reinstalling

Windows 11's auto-updates are the recurrence vector — close it.

1. Once a stable driver version is confirmed, download Microsoft's "Show or hide updates" troubleshooter (wushowhide) and hide the driver update.
2. Alternative: **Group Policy** (`gpedit.msc`) > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Update** > **Manage updates offered from Windows Update** > enable **Do not include drivers with Windows Updates**.
3. Verify the block held after the next Patch Tuesday — check the driver version in **Device Manager** > **Properties** > **Driver**.
4. Revisit the block every few months; vendors do fix these bugs, and eventually the new version is safe.

### Fix 4: Repair Windows 11 system files

Use the built-in repair stack.

1. **Windows + X** > **Terminal (Admin)**: run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`, then SFC again.
3. **Settings** > **Windows Update** > install all pending updates — Windows 11 ships kernel fixes in cumulative updates that resolve exception classes outright.
4. If a specific update caused the crashes, uninstall it (**Update history** > **Uninstall updates**) and pause updates while you stabilize.

### Fix 5: Test in Safe Mode and clean-boot

Confirm third-party involvement the Windows 11 way.

1. **Settings** > **System** > **Recovery** > **Advanced startup** > **Restart now** > **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > **4**.
2. Stable in Safe Mode → third-party driver/software. Then clean-boot: `msconfig` > hide Microsoft services > disable all; **Task Manager** > **Startup** > disable all.
3. Bisect by re-enabling halves until the culprit reappears.
4. Pay special attention to RGB/fan control utilities and VPN clients on Windows 11 — their drivers are disproportionately represented in 0x0000003B dumps.

### Fix 6: Scan for malware and check the disk

Cover the non-driver branches.

1. **Windows Security** > **Virus & threat protection** > **Scan options** > **Microsoft Defender Offline scan**.
2. Elevated terminal: `chkdsk C: /f /r` (schedule at restart) — storage corruption of driver binaries causes repeat exceptions.
3. If crashes name different drivers each time, run `mdsched.exe` (Windows Memory Diagnostic) — then MemTest86 overnight for certainty.
4. Replace failing hardware; no driver fix survives bad RAM.

### Fix 7: In-place upgrade repair

The Windows 11-native last resort that keeps everything.

1. Download the Windows 11 ISO, mount it, run `setup.exe`, choose **Keep personal files and apps**.
2. This reinstalls Windows 11's system files and rebuilds the driver store while preserving data, apps, and settings.
3. Afterward, install laptop-vendor drivers first, test thoroughly, then reintroduce third-party software gradually.
4. If exceptions persist on a clean driver set, it's hardware — run full OEM diagnostics (**F12**/**F2** at boot) and consider professional diagnosis.

## Closing

On Windows 11, SYSTEM_SERVICE_EXCEPTION is usually a driver problem wearing an OS-update disguise — the aggressive auto-update behavior means the "cause" is often a driver that was fine last week. The repair that sticks has three parts: the right driver version, the block that keeps it, and the verification that nothing else is faulting. Skip the blocking step and you'll fix the same crash twice. Do all three, verify for a few days under real workloads, and this stop code becomes a closed case. For the condensed fix order, our [best-way guide](/articles/best-way-to-fix-system-service-exception/) is the quick reference; for power-transition variants, our [power state failure guide](/articles/driver-power-state-failure-windows-11-fix/) covers that branch. It's also worth auditing the software you install going forward: the utilities most often implicated in 0x0000003B dumps — RGB controllers, fan managers, VPN clients with kernel drivers, and "system optimizer" suites — all earn their place by installing kernel-mode components, so every new one is a new roll of the dice. Prefer tools that don't need kernel drivers when a user-mode alternative exists. And when Windows 11's next feature update arrives, give it a week on your machine before assuming stability; the update changes the kernel your drivers run against, and the first days after a feature update are when latent driver exceptions surface. A little patience after updates prevents a lot of blue screens.
