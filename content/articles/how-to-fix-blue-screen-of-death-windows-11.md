---
title: "How to Fix the Blue Screen of Death in Windows 11"
slug: how-to-fix-blue-screen-of-death-windows-11
date: 2026-09-11
categories: ["windows-errors"]
tags: ["blue screen", "bsod", "windows 11"]
description: "Windows 11 blue screen crashing your laptop? Identify the stop code, find the faulty driver or hardware, and fix BSODs step by step."
thumbnail: "/images/thumbs/how-to-fix-blue-screen-of-death-windows-11.webp"
faqs:
  - q: "What causes the blue screen of death on Windows 11?"
    a: "Faulty or incompatible drivers cause the majority of BSODs, followed by failing RAM or storage, overheating, corrupted system files, and occasionally bad Windows updates. The stop code on the blue screen (like DRIVER_POWER_STATE_FAILURE or MEMORY_MANAGEMENT) points to the category — photograph it before the laptop restarts."
  - q: "How do I find out which driver caused my blue screen?"
    a: "Check the minidump: after rebooting, look in C:\\Windows\\Minidump for .dmp files and analyze them with the free BlueScreenView tool or Windows Debugger (WinDbg). The dump names the faulting driver file directly. Event Viewer's System log (filter for BugCheck events) also records the stop code of each crash."
  - q: "Can a blue screen damage my laptop?"
    a: "The crash itself does not damage hardware — it is Windows protecting itself by halting. But the underlying cause can: overheating that triggers BSODs is cooking components, and a failing drive causing crashes may be losing data. Treat recurring BSODs as a warning to diagnose promptly, not as harmless annoyances."
  - q: "Should I reinstall Windows to fix recurring blue screens?"
    a: "Only as a last resort. Most BSODs are fixed by updating or rolling back the specific bad driver, testing RAM, or checking thermals — all faster and less destructive. Reinstall Windows when dumps implicate no clear driver, SFC/DISM repairs fail, and crashes persist across driver versions. Even then, test the hardware first."
---

The blue screen is Windows' way of saying "I found a problem I cannot safely continue through, so I stopped." It looks catastrophic. Usually it is not — most BSODs trace to one bad driver, and the stop code on the screen tells you where to look. The worst thing you can do is ignore recurring blue screens; the second worst is reinstalling Windows before diagnosing.

This guide is the diagnostic order that works: capture the code, identify the driver, fix or replace it, then check hardware. If you already know your stop code names a driver power issue, the focused [driver power state failure fix](/articles/driver-power-state-failure-windows-11-fix/) goes deeper on that one.

## Why This Happens

- **Bad or incompatible drivers.** The top cause by a wide margin — especially graphics, Wi-Fi, and chipset drivers after updates.
- **Failing RAM.** Corrupt memory cells cause random, varied stop codes — the hallmark of hardware memory failure.
- **Failing storage.** A dying SSD/HDD corrupts data mid-read, crashing the kernel.
- **Overheating.** Thermal emergencies halt the system; crashes cluster during gaming or heavy loads.
- **Corrupted system files.** Damaged Windows components crash unpredictably until repaired.
- **Buggy Windows updates.** Occasionally Microsoft ships an update that blue-screens specific hardware combinations.

## How to Fix It

Work through these in order. Do not skip the diagnosis steps — they prevent wasted effort.

### Fix 1: Capture the Stop Code and Crash Dumps

You cannot fix what you have not identified. Gather evidence first.

1. The next time the blue screen appears, photograph it with your phone — note the **stop code** (e.g., MEMORY_MANAGEMENT) and any named file (e.g., nvlddmkm.sys).
2. Let the percentage counter finish; Windows saves a minidump before restarting. Do not force-power-off during it.
3. After reboot, press **Win + X** > **Event Viewer** > **Windows Logs** > **System**. Filter for **BugCheck** events — each records the stop code and parameters of a crash.
4. Check **C:\Windows\Minidump** for .dmp files. Analyze them with the free **BlueScreenView** utility or **WinDbg** from the Microsoft Store — both name the faulting driver.
5. Write down the pattern: same code every time means one driver or component; different codes each crash means RAM or power.
6. If the laptop blue-screens in a loop and never reaches the desktop, [boot into Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/) — dumps and Event Viewer are accessible from there.

### Fix 2: Update or Roll Back the Faulty Driver

The dump named a driver. Now deal with that specific driver.

1. Identify the driver file from the dump (e.g., **nvlddmkm.sys** = NVIDIA graphics, **Netwtw10.sys** = Intel Wi-Fi, **ntoskrnl.exe** = often a driver corrupting kernel memory rather than Windows itself).
2. **Win + X** > **Device Manager**, find the device, right-click > **Properties** > **Driver** tab.
3. If the crashes started after a driver update, click **Roll Back Driver**.
4. Otherwise, update: first try the manufacturer's support site (laptop maker) for the validated version, then the chipmaker (Intel, NVIDIA, AMD) for the newest.
5. For graphics drivers specifically, use **Display Driver Uninstaller (DDU)** in Safe Mode for a truly clean reinstall — standard uninstalls leave remnants that preserve the bug.
6. Driver sources: [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel chips and [NVIDIA's driver page](https://www.nvidia.com/Download/index.aspx) for NVIDIA graphics (AMD users: AMD's driver download page). For specific older versions, search the Microsoft Update Catalog by KB number.

### Fix 3: Test the RAM

Random stop codes across crashes scream memory failure. Test it.

1. Press **Win + R**, type `mdsched.exe`, press Enter, and choose **Restart now and check for problems**.
2. Let Windows Memory Diagnostic complete (15-30 minutes). Any reported errors mean bad RAM.
3. For a deeper test, run **MemTest86** from a bootable USB overnight — it catches errors Windows' quick test misses.
4. If errors appear and you have two RAM sticks, test them one at a time to identify the bad one. Reseat both first — poorly seated RAM causes errors too.
5. Replace faulty RAM with the correct DDR generation and speed for your laptop (check the manual or CPU-Z).
6. Note: on laptops with soldered RAM, a memory failure means motherboard-level repair — get a quote before deciding, and back up data immediately since crashes risk corruption.

### Fix 4: Check the Drive and System Files

Storage and OS corruption are the next layer down.

1. Open elevated Terminal and run `chkdsk C: /f /r`. Agree to run at next restart, then reboot. Bad sectors get mapped out; widespread bad sectors mean replace the drive.
2. Run `sfc /scannow` — repairs corrupted Windows system files. Reboot if it fixed anything.
3. Run `DISM /Online /Cleanup-Image /RestoreHealth` — repairs the component store SFC depends on.
4. Check drive health with **CrystalDiskInfo** (free): look at the overall status and SSD wear percentage. A drive at 5% life remaining is living on borrowed time — clone it now.
5. If the drive is failing, replace it (an SSD upgrade is the single best aging-laptop upgrade anyway) and reinstall Windows from Microsoft's official download page.
6. After any drive replacement, monitor for a week: no crashes confirms the old drive was the cause.

### Fix 5: Rule Out Overheating

Heat-caused BSODs have a distinctive pattern: crashes under load, fine at idle.

1. Install **HWiNFO** and log CPU/GPU temperatures during normal use and during a heavy task.
2. Crashes correlating with 95-100°C readings are thermal. Sustained high temps also degrade everything else over time.
3. Clean the vents with compressed air (short bursts, fans held still). Check that all fans actually spin.
4. Replace dried thermal paste if the laptop is several years old and runs hot — or have a shop do it.
5. Use a cooling pad during heavy workloads as an immediate mitigation while you arrange proper cleaning.
6. Also verify the crashes stop when thermals are controlled. If they do, heat was the cause — and the cleaning just extended your laptop's life, not merely fixed crashes.

### Fix 6: Uninstall Recent Updates and Software

When BSODs start on a specific date, something changed on that date.

1. **Settings** > **Windows Update** > **Update history** > **Uninstall updates**. Remove the most recent quality update and test for a few days.
2. Think about recently installed software: antivirus suites, VPN clients, virtualization tools, and RGB/fan control utilities install kernel drivers — prime BSOD suspects. Uninstall the most recent additions one at a time.
3. Check **Reliability Monitor** (**Win + R** > `perfmon /rel`): it graphs crashes against installs on a timeline, making the correlation visual.
4. If a Windows update is the confirmed cause, pause updates for 2-3 weeks (**Settings** > **Windows Update** > **Pause updates**) while Microsoft ships a fix — they usually do quickly for widespread BSODs.
5. Report it via **Feedback Hub** with the stop code. BSOD reports with dumps attached genuinely influence fix prioritization.
6. Microsoft's official BSOD troubleshooting reference on the [Windows support site](https://support.microsoft.com/en-us/windows) covers additional stop-code-specific steps.

### Fix 7: Reset Windows as the Last Software Resort

When dumps blame nothing consistently and hardware tests pass, the OS itself is suspect.

1. Back up everything important. A reset is reliable but backups are non-negotiable.
2. **Settings** > **System** > **Recovery** > **Reset PC**. Try **Keep my files** first.
3. If crashes persist after a keep-files reset, do **Remove everything** — a fully clean slate eliminates software causes definitively.
4. After reset, install drivers from the laptop manufacturer's site *before* letting Windows Update run free — manufacturer-validated drivers first, newest chipmaker drivers only if problems persist.
5. Add hardware back into the mix gradually (docks, peripherals) — a faulty peripheral driver can be the hidden cause, and gradual reintroduction identifies it.
6. If blue screens survive a clean reset with validated drivers and passing hardware tests, you are looking at an intermittent motherboard fault — professional diagnosis time. Document the stop codes; the technician will want them.

## Closing

Blue screens feel random, but they are among the most diagnosable problems in computing — the system writes down what killed it. Read the dump, fix the named driver, test the hardware the pattern suggests, and most BSODs end within an hour.
