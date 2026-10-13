---
title: "How to Fix the Driver Overran Stack Buffer Error on Windows 11"
slug: how-to-fix-driver-overran-stack-buffer-on-windows-11
date: 2026-09-26
categories: ["windows-errors"]
tags: ["driver-overran-stack-buffer", "windows-11", "blue-screen"]
description: "Driver Overran Stack Buffer crashing Windows 11? Identify the faulty driver from the crash dump and replace it with these steps."
thumbnail: "/images/thumbs/how-to-fix-driver-overran-stack-buffer-on-windows-11.webp"
faqs:
  - q: "How is this error different on Windows 11 versus Windows 10?"
    a: "The stop code and cause are identical — a driver overflowing its memory buffer. What's different is the driver landscape: Windows 11's stricter driver signing and updated stacks mean older Windows 10-era drivers are more likely to misbehave. Drivers written for Windows 10 but never updated for 11 are prime suspects."
  - q: "Can Windows 11's memory integrity feature cause this?"
    a: "Memory integrity (HVCI) doesn't cause buffer overruns, but it can expose them — a driver with a latent overflow bug that ran fine on Windows 10 may crash under 11's stricter enforcement. If the crashes started after enabling memory integrity, update the named driver rather than disabling the protection."
  - q: "The dump names ntoskrnl.exe. Is Windows itself broken?"
    a: "Almost never. Ntoskrnl.exe is the Windows kernel, and it appears in dumps because it's where the crash was detected — not where it was caused. The real culprit is the third-party driver that corrupted memory before the kernel noticed. Look past ntoskrnl to the other named modules."
  - q: "Should I update all my drivers at once to fix this?"
    a: "No — update the suspect first, test, then move on. Updating everything simultaneously makes it impossible to know what fixed the problem, and a bad new driver can introduce a second issue. Work through graphics, network, and storage drivers one at a time."
---
Driver Overran Stack Buffer (stop code 0xF7) on Windows 11 means exactly what it says: a driver wrote past the end of its allocated memory, Windows caught the violation, and shut everything down. It's a security-flavored crash — the same class of bug that attackers exploit — so Windows treats it seriously and halts immediately rather than risking further damage.

On Windows 11 this error disproportionately involves drivers carried over from Windows 10 installs or pushed by Windows Update without proper 11 testing. The detective work is the same as ever: find the driver, replace it. Keep notes as you go — which driver you replaced, when, and whether the crashes changed — because this kind of methodical tracking is what separates a quick fix from weeks of random reinstalls.

For the Windows 10 version of this guide see [Driver Overran Stack Buffer on Windows 10](/articles/how-to-fix-driver-overran-stack-buffer-on-windows-10/), and for crashes that began after an update, [the after-update variant](/articles/how-to-fix-driver-overran-stack-buffer-after-windows-11-update/) applies.

## Why this happens

- **Outdated Windows 10-era drivers.** Drivers never properly updated for Windows 11's driver model are the top cause.
- **Buggy new driver versions.** A fresh graphics or network driver with a buffer-handling regression.
- **Old peripheral drivers.** USB Wi-Fi adapters, printers, and docks with ancient drivers.
- **Corrupted driver files.** Bad updates or disk errors damaging previously good drivers.
- **Conflicting drivers.** Manufacturer utilities fighting Windows' built-in drivers for the same hardware.
- **Memory integrity exposing latent bugs.** HVCI's stricter enforcement surfaces overflows that older Windows tolerated silently.

## How to fix it

Work through these in order — identify, then replace.

### Fix 1: Identify the driver from the crash dump

Don't guess; read the dump.

1. Verify dumps are on: **Win + R** > `sysdm.cpl` > **Advanced** > **Startup and Recovery Settings** > **Small memory dump** selected.
2. After the next crash, open `C:\Windows\Minidump` and find the newest `.dmp`.
3. Install **WinDbg Preview** from the Microsoft Store, open the dump, run `!analyze -v`.
4. Read the **IMAGE_NAME / MODULE_NAME** line — that's your culprit (examples: `nvlddmkm.sys`, `Netwtw10.sys`, `rtwlanu.sys`).
5. Ignore `ntoskrnl.exe` if it's the only name — it's the detector, not the cause; look at the stack for the driver that called into it.

### Fix 2: Update the identified driver properly

Replace the bad driver with a clean, current version.

1. Download the latest driver from the vendor: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) — or your laptop maker's support page.
2. In **Device Manager**, right-click the device, choose **Uninstall device**, and tick **Attempt to remove the driver for this device**.
3. Restart, then install the downloaded driver fresh.
4. Test with the workload that triggered crashes.

### Fix 3: Update the other high-risk drivers

If the dump was inconclusive, work the usual suspects in order.

1. **Display adapters** — graphics drivers handle the largest buffers in the system.
2. **Network adapters** — Wi-Fi drivers are the second most common trigger, especially on resume from sleep.
3. **Storage controllers** — update the Intel RST/VMD or AMD storage driver.
4. Do them one at a time with a restart and test period between each.

### Fix 4: Check USB peripherals and their drivers

Don't overlook external devices.

1. Unplug all non-essential USB devices and test for a day.
2. If crashes stop, reconnect devices one at a time to find the trigger.
3. For the culprit device, download its newest driver from the manufacturer's site — or replace the device if no updated driver exists.
4. USB Wi-Fi adapters with 2018-era drivers are repeat offenders here.

### Fix 5: Run SFC and DISM

Repair driver and system files damaged by bad updates.

1. Right-click **Start > Terminal (Admin)**.
2. Run: `sfc /scannow`
3. Then: `DISM /Online /Cleanup-Image /RestoreHealth`
4. Restart and retest.

### Fix 6: Review memory integrity and virtualization settings

Windows 11's security features interact with drivers in ways 10's didn't.

1. Go to **Settings > Privacy & security > Windows Security > Device security > Core isolation**.
2. Note whether **Memory integrity** is on. Don't turn it off permanently — but if crashes started the day you enabled it, the named driver needs updating to be HVCI-compatible.
3. Check for very old drivers incompatible with HVCI: in **Windows Security > Device security > Core isolation**, look for the incompatible-driver list and update or remove those drivers.

### Fix 7: Disable Fast Startup

Stale driver states loaded by Fast Startup can trigger this on boot or wake. This is a quick test that rules out an entire class of resume-related driver bugs.

1. Open **Control Panel > Power Options > Choose what the power buttons do**.
2. Click **Change settings that are currently unavailable**.
3. Uncheck **Turn on fast startup** and save.
4. Shut down fully, then cold-boot and test.

### Fix 8: Use Driver Verifier carefully as a last resort

Only when the dump keeps naming nothing useful.

1. Create a restore point first: **Win + R** > `sysdm.cpl` > **System Protection** tab > **Create**.
2. Run `verifier.exe`, choose **Create custom settings**, enable **Special pool** and **Force IRQL checking**.
3. Select **driver names from a list** and tick only your non-Microsoft suspects.
4. Restart — Verifier crashes the system the moment a chosen driver misbehaves, naming it in the dump.
5. Afterwards, run `verifier /reset` and restart. Never leave it enabled.
6. Microsoft's official reference is documented in its Windows support hub.

## Closing

On Windows 11, Driver Overran Stack Buffer is usually an outdated or buggy driver that the stricter 11 driver model finally caught. Read the dump, replace the named driver with a clean current version, and work the other suspects one at a time. Resist the urge to update everything at once — methodical, one-driver-at-a-time testing is what actually ends these crashes, and it leaves you knowing exactly what fixed the problem if it ever comes back.
