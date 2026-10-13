---
title: "DRIVER_IRQL_NOT_LESS_OR_EQUAL: Blue Screen Fix Guide"
slug: driver-irql-not-less-or-equal-blue-screen-error-fix
date: 2026-09-02
categories: ["windows-errors"]
tags: ["bsod", "drivers", "stop code"]
description: "DRIVER_IRQL_NOT_LESS_OR_EQUAL blue screen? A driver touched memory it shouldn't at a raised IRQL. Here's how to find and fix the bad driver."
thumbnail: "/images/thumbs/driver-irql-not-less-or-equal-blue-screen-error-fix.webp"
faqs:
  - q: "What does DRIVER_IRQL_NOT_LESS_OR_EQUAL mean?"
    a: "A kernel-mode driver tried to access memory at an invalid address while running at a raised interrupt level (IRQL), where page faults aren't allowed. Windows stops the system immediately. It's almost always a buggy, outdated, or corrupted device driver."
  - q: "Which drivers cause this error most often?"
    a: "Network adapters (Wi-Fi and Ethernet), graphics drivers, storage controller drivers, and USB drivers. If the blue screen names a .sys file — like ndis.sys, nvlddmkm.sys, or storport.sys — that file tells you exactly which driver is at fault."
  - q: "Can overclocking cause this stop code?"
    a: "Yes. CPU, RAM, or GPU overclocks make hardware behave unpredictably at high interrupt levels, and this is a classic overclock-instability crash. If you're overclocked, reset to stock speeds before doing anything else — it may fix the problem outright."
  - q: "Is DRIVER_IRQL_NOT_LESS_OR_EQUAL a virus?"
    a: "Rarely. It's a driver bug far more often than malware. That said, rootkits live in kernel mode and can trigger similar crashes, so if the crashes appeared alongside other suspicious behavior, run a full Defender offline scan to be safe."
---

`DRIVER_IRQL_NOT_LESS_OR_EQUAL` (stop code 0xD1) sounds like alphabet soup, but the meaning is practical: a driver tried to touch memory it wasn't allowed to touch, at a moment when Windows couldn't tolerate the mistake. Nine times out of ten, the fix is finding that driver and updating, rolling back, or replacing it.

The blue screen often names the guilty file — something like `ndis.sys` or `rtwlanu.sys`. If you caught that name, you're already halfway to the fix. If not, the steps below include how to dig it out of the crash dump.

## Why this happens

- **Buggy network driver**: Wi-Fi and Ethernet drivers (ndis.sys, rtwlane.sys, Netwtw10.sys) are the top offenders — they run at high IRQL constantly and any bug shows up here.
- **Graphics driver memory bug**: GPU drivers map large memory regions; a bad version can reference freed or invalid addresses.
- **Corrupted driver files**: Partial updates or disk errors corrupt .sys files so they misbehave even though the version looks current.
- **Overclocked CPU, RAM, or GPU**: Unstable overclocks corrupt addresses and timing at high interrupt levels, producing exactly this crash.
- **Faulty RAM**: Bad memory returns garbage addresses to drivers, which then fault when they try to use them.
- **Incompatible driver after Windows update**: A driver written for an older build can violate memory rules the new kernel enforces more strictly.

## How to fix it

Work through these in order — identifying the driver comes first, then fixing it.

### Fix 1: Identify the guilty driver from the crash dump

Guessing wastes time. Get the actual filename first.

1. Install **BlueScreenView** (NirSoft) or **WhoCrashed** — both free and read Windows minidumps.
2. Open `C:\Windows\Minidump` with the tool. Look at the most recent dump's **Caused By Driver** column.
3. Note the filename: `ndis.sys` = network stack, `nvlddmkm.sys` = NVIDIA, `atikmdag.sys` = AMD, `rtwlanu.sys` = Realtek Wi-Fi, `storport.sys` = storage.
4. If the dump names a third-party driver, that driver is your prime suspect — jump to Fix 3 for it specifically.
5. If dumps point at `ntoskrnl.exe` (the kernel itself), the kernel is usually the victim, not the cause — suspect RAM (Fix 6) or a driver corrupting kernel memory.

For more on reading crash dumps and general blue screen triage, see our [blue screen of death guide for Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/).

### Fix 2: Reset any overclocking

If your CPU, RAM (XMP), or GPU is overclocked, stop here first — this is a classic instability crash.

1. Restart and enter BIOS/UEFI (usually **F2**, **Del**, or **F12** during the manufacturer's logo).
2. Load **Optimized Defaults** or **Setup Defaults** — this disables CPU overclocks and XMP profiles.
3. If you use MSI Afterburner, Intel XTU, or Ryzen Master, reset those profiles to stock too.
4. Save, exit, and use the laptop normally for a day. If crashes stop, your overclock was the cause — re-apply it more conservatively if you must.

### Fix 3: Update or reinstall the suspect driver

Once you know the driver, hit it directly.

1. Open **Device Manager** (**Win + X** > **Device Manager**) and find the device matching the .sys file.
2. Right-click it, choose **Update driver** > **Search automatically for drivers**.
3. Whether or not that helps, get the manufacturer's version: [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel Wi-Fi/graphics, [NVIDIA's driver download](https://www.nvidia.com/Download/index.aspx) for GeForce, [AMD's driver page](https://www.amd.com/en/support/download/drivers.html) for Radeon — or your laptop maker's site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)).
4. Install the downloaded driver, choosing **Clean installation** if the installer offers it.
5. Restart and stress-test: browse heavily on Wi-Fi (for network drivers) or run a game/benchmark (for GPU drivers).

### Fix 4: Roll back a recently updated driver

If crashes started after a driver update, the new driver is the prime suspect.

1. In **Device Manager**, right-click the device > **Properties** > **Driver** tab.
2. Click **Roll Back Driver**, pick a reason, and confirm.
3. Restart and test. If roll-back is greyed out, uninstall the device instead: right-click > **Uninstall device**, check **Delete the driver software**, restart, and let Windows install its inbox driver.
4. Block the bad version from reinstalling with the **Show or hide updates** troubleshooter from Microsoft.

### Fix 5: Run Driver Verifier to catch the culprit

When dumps are inconclusive, Driver Verifier stresses drivers until the bad one crashes identifiably. Use with care — it intentionally causes blue screens.

1. Press **Win + R**, type `verifier`, and press Enter.
2. Choose **Create standard settings**, then **Automatically select unsigned drivers** (or select specific suspects).
3. Click **Finish** and restart. Use the laptop normally — Verifier will blue-screen on the misbehaving driver, naming it clearly.
4. After capturing the culprit, boot into Safe Mode, run `verifier` again, and choose **Delete existing settings** to turn it off.
5. Then apply Fix 3 to the identified driver.
6. If Verifier itself causes a boot loop, see our guide on [fixing Driver Verifier IOManager violations](/articles/best-way-to-fix-driver-verifier-iomanager-violation/) — it covers escaping Verifier-induced crashes.

### Fix 6: Test your RAM

Drivers blamed by dumps are sometimes innocent — bad RAM feeds them corrupt addresses.

1. Press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
2. Any error at all means the RAM is bad. For laptops with removable RAM, test sticks individually to isolate the faulty one.
3. For a definitive result, run MemTest86 from USB overnight.
4. Also run `sfc /scannow` from an elevated Command Prompt — corrupted system files can mimic driver crashes.

### Fix 7: Check for malware in kernel mode

Rare, but rootkits operate at the same level as drivers and cause identical crashes.

1. Open **Windows Security** > **Virus & threat protection** > **Scan options**.
2. Run a **Microsoft Defender Offline scan** — it reboots into a clean environment outside Windows.
3. Remove anything found and retest. If your third-party antivirus's kernel drivers are themselves suspect, temporarily uninstall it (not just disable) and test with Defender alone.

If the crashes only began after a Windows update, our [blue screen after Windows 11 update guide](/articles/blue-screen-after-windows-11-update-troubleshooting/) walks through update-specific rollbacks that complement these driver fixes.

## Closing

DRIVER_IRQL_NOT_LESS_OR_EQUAL is Windows telling you, in its own cryptic way, exactly what's wrong: a driver broke the memory rules. Read the dump to name the driver, reset any overclocks, then update or roll back that driver — and test the RAM if the dumps keep blaming the kernel itself. It's methodical work, but it resolves cleanly in the vast majority of cases.
