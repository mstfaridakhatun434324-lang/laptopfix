---
title: "How to Fix the Bad Pool Header BSOD on Windows 10"
slug: how-to-fix-bad-pool-header-on-windows-10
date: 2026-09-09
categories: ["windows-errors"]
tags: ["bad pool header", "bsod", "windows 10", "blue screen"]
description: "Getting the BAD_POOL_HEADER blue screen on Windows 10? This guide explains why it happens and walks through proven fixes, from driver updates to RAM testing."
thumbnail: "/images/thumbs/how-to-fix-bad-pool-header-on-windows-10.webp"
faqs:
  - q: "What does the Bad Pool Header blue screen mean?"
    a: "It means Windows' memory manager caught a process making an invalid request to the memory pool — usually because a driver freed or accessed memory incorrectly. The system stops itself with stop code 0x00000019 to prevent data corruption. In most cases a faulty driver, bad RAM, or a damaged update is responsible."
  - q: "Can a bad driver really cause the Bad Pool Header error?"
    a: "Yes, and it is the single most common cause. Third-party drivers — especially antivirus, storage controller, and network drivers — can mishandle memory allocation requests. The crash often starts right after a driver update or new hardware install, which makes the culprit easy to identify if you remember what changed recently."
  - q: "Will I lose my files fixing this blue screen?"
    a: "No. None of the standard Bad Pool Header fixes touch your personal files. Updating drivers, running memory diagnostics, repairing system files, and rolling back updates all preserve your data. Only a full clean install would remove files, and that is a last resort after every other fix has been attempted."
  - q: "How do I know if bad RAM is causing it?"
    a: "Run Windows Memory Diagnostic by pressing Windows + R, typing mdsched.exe, and choosing to restart and check now. If it reports hardware errors, reseat your RAM sticks one at a time and retest. Two or more sticks failing the same test almost always means at least one stick needs replacing."
---

The BAD_POOL_HEADER blue screen is one of Windows 10's more cryptic stop codes — it points at memory management, but the real culprit is usually a driver behaving badly. Stop code 0x00000019 means Windows caught a process submitting an invalid request to the memory pool, and it shut everything down rather than risk corrupting your data. Scary to look at, but very fixable.

Here's the practical reality: in the majority of cases, this crash traces back to a third-party driver — often antivirus software, a storage controller, or a network adapter driver that got updated recently. The second most common cause is failing RAM. Both are diagnosable with built-in Windows tools, and neither requires a reinstall. Work through the fixes below in order, and note what changed on your PC right before the crashes started — that timing is usually the biggest clue. For a broader overview of blue screen diagnostics, our [blue screen of death guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the general approach.

## Why this happens

- **Faulty third-party drivers**: Drivers that mishandle memory allocation or free the same memory twice trigger the pool check that produces this stop code.
- **Antivirus filter drivers**: Security software installs deep kernel drivers; when these misbehave after an update, pool corruption follows.
- **Failing RAM**: Bad memory cells return wrong data during pool operations, which the memory manager flags as an invalid request.
- **Corrupt Windows update**: An interrupted or buggy update can damage kernel components involved in memory management.
- **Disk errors**: Bad sectors in the page file area or system files can surface as pool header violations.
- **Overclocked memory**: RAM running beyond its rated speed with unstable timings produces exactly this class of error.
- **Malware**: Rootkits that hook kernel memory functions can corrupt pool headers as a side effect.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Boot into Safe Mode and note the timing

Before changing anything, establish whether the crash is driver-related.

1. Force Windows into recovery by interrupting boot three times (hold the power button during the Windows logo), then choose **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** and press **4** for Safe Mode.
2. If Windows runs fine in Safe Mode for a while, a third-party driver or startup program is almost certainly the cause — continue to Fix 2.
3. If it crashes in Safe Mode too, the problem is more likely hardware or core system files — prioritize Fix 5 and Fix 6.
4. While here, open **Settings** > **Windows Update** > **Update history** and note any driver or system updates from just before the crashes began.

### Fix 2: Uninstall or roll back the suspect driver

The timing of the crashes usually identifies the guilty driver.

1. In Safe Mode or normal Windows, press **Windows + X** and open **Device Manager**.
2. Expand the category of the device you most recently updated (display adapters, network adapters, and storage controllers are the usual suspects).
3. Right-click the device, choose **Properties** > **Driver** tab > **Roll Back Driver** if the option is available.
4. If rollback isn't offered, choose **Uninstall device**, tick **Attempt to remove the driver for this device** if shown, restart, and let Windows install its inbox driver.
5. Test for a day before reinstalling anything from the manufacturer — if the crashes stop, you've found your culprit.

### Fix 3: Remove third-party antivirus temporarily

Antivirus kernel drivers are a classic Bad Pool Header trigger.

1. If you have third-party antivirus installed, uninstall it completely — use the vendor's removal tool rather than just the Control Panel entry, since filter drivers linger otherwise.
2. Windows Defender activates automatically and is perfectly adequate protection during testing.
3. Use the PC normally for a day or two. If the crashes stop, reinstall the latest version of your antivirus (vendors patch these bugs quickly) or switch products.
4. Never run the PC without any antivirus for longer than the test period — check [Microsoft's security guidance](https://support.microsoft.com/en-us/windows) if you're unsure about Defender's coverage.

### Fix 4: Run Windows Memory Diagnostic

Rule out bad RAM before spending time on software.

1. Press **Windows + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems**. The test runs before Windows loads.
3. Let the standard test complete (about 15–30 minutes). If it reports hardware problems, continue.
4. Power down, unplug, and reseat each RAM stick — remove dust from the slots, press sticks firmly until the clips lock.
5. If you have two sticks, test with one at a time to isolate the bad one. A stick that fails on its own needs replacing.

### Fix 5: Run SFC and DISM to repair system files

Corrupted kernel files can produce the same stop code.

1. Open **Command Prompt as administrator** (right-click Start > **Terminal (Admin)** or **Command Prompt (Admin)**).
2. Run `sfc /scannow` and wait for it to finish — this checks and repairs protected system files.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store SFC draws from.
4. Restart and test. If SFC reports it couldn't fix everything, run DISM first and then SFC again — order matters because SFC relies on the store DISM repairs.

### Fix 6: Check the disk with chkdsk

Storage problems feeding bad data into memory operations can masquerade as pool corruption.

1. Open an administrator Command Prompt.
2. Run `chkdsk C: /f /r` and confirm the prompt to schedule it at next restart by typing **Y**.
3. Restart and let the full scan complete — it can take an hour or more on large drives.
4. If chkdsk reports bad sectors, back up important files promptly; bad sectors tend to spread, and a dying drive causes ever-more-frequent crashes.
5. On a laptop, the manufacturer's diagnostics (usually **F12** at boot) can run a deeper drive test.

### Fix 7: Update Windows and reset overclocks

Finish by stabilizing the software environment.

1. Go to **Settings** > **Windows Update** and install all pending updates, including optional driver updates — Microsoft regularly patches the kernel components involved in pool management. Use the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) if a specific fix KB is mentioned in a crash dump.
2. If you've overclocked RAM via XMP or manual timings, enter the BIOS/UEFI (usually **F2** or **Del** at boot) and restore memory settings to defaults — unstable memory timings are a textbook Bad Pool Header cause.
3. Also disable any RAM "turbo" or aggressive timing profiles your laptop vendor's utility may have enabled.
4. After changes, monitor for several days. If a specific driver keeps reinstalling itself through Windows Update and crashing, use the "Show or hide updates" troubleshooter to block that driver version.

## Closing

The Bad Pool Header error looks intimidating, but its causes are narrow and well understood: a bad driver in most cases, failing RAM in many of the rest. The diagnostic sequence that works is to test in Safe Mode, roll back whatever changed recently, verify the memory, and repair system files — in that order. Resist the urge to reinstall Windows first; a clean install with the same faulty driver or the same dying RAM stick brings the crash right back. Fix the actual cause, and this particular blue screen stays gone. If you're seeing a different pool-related stop code, our [special pool corruption guide](/articles/how-to-fix-special-pool-detected-memory-corruption-on-windows-10/) covers its close cousin.
