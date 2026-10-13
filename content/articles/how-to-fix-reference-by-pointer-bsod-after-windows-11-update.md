---
title: "REFERENCE_BY_POINTER Blue Screen After a Windows 11 Update: How to Fix It"
slug: how-to-fix-reference-by-pointer-bsod-after-windows-11-update
date: 2026-09-05
categories: ["windows-errors"]
tags: ["windows-11", "bsod", "reference-by-pointer"]
description: "REFERENCE_BY_POINTER blue screen after a Windows 11 update? This stop code points at drivers or RAM — here are 7 fixes in the right order."
thumbnail: "/images/thumbs/how-to-fix-reference-by-pointer-bsod-after-windows-11-update.webp"
faqs:
  - q: "What causes REFERENCE_BY_POINTER?"
    a: "It means a driver tried to use an object reference count incorrectly — typically releasing the same memory twice or mishandling an I/O request packet. In practice, after a Windows 11 update, the triggers are a graphics or network driver that is incompatible with the new build, faulty RAM corrupting reference counts, or Driver Verifier catching a genuinely buggy driver."
  - q: "Is REFERENCE_BY_POINTER a hardware or software problem?"
    a: "Usually software. The vast majority of cases I see are driver-related, especially graphics drivers updated (or broken) by a Windows update. Hardware enters the picture when the crashes survive a clean driver reinstall — then RAM is the next suspect, followed by the SSD. Work the software fixes first; they resolve most cases without spending a cent."
  - q: "The blue screen names a .sys file. What do I do with that?"
    a: "That file name is gold — it identifies the exact driver. Google the file name to find which device it belongs to (nvlddmkm.sys is NVIDIA, netwtw10.sys is Intel Wi-Fi, for example), then update, roll back, or clean-reinstall that specific driver. If no file is named, start with the graphics driver anyway, since it is the most common offender."
  - q: "Does booting into Safe Mode help diagnose REFERENCE_BY_POINTER?"
    a: "Yes, and it is the fastest isolation test. Hold Shift while clicking Restart, go to Troubleshoot > Startup Settings, and boot into Safe Mode. If the crashes stop there, a third-party driver is the cause — usually graphics, audio, or network. Update or roll back those drivers one at a time in normal mode until you find the one that triggers the blue screen."
---

REFERENCE_BY_POINTER is one of those stop codes that sounds like it was written for programmers, not people. Translated: a driver on your laptop mishandled a piece of memory, and Windows crashed rather than let the corruption spread. When it starts right after a Windows 11 update, the update almost certainly disturbed a driver that was previously getting away with sloppy behavior.

The good news is the fix path is well-trodden. Here is how I work through it.

## Why this happens

- **An incompatible graphics driver.** The update changed kernel interfaces the old GPU driver was relying on. NVIDIA's `nvlddmkm.sys` is the single most-named file in these dumps.
- **A broken network or Wi-Fi driver.** Intel and Realtek wireless drivers are frequent offenders after feature updates.
- **Faulty RAM.** Bad memory corrupts the reference counts the kernel maintains, producing this exact stop code with no driver to blame.
- **Driver Verifier catching a real bug.** If Verifier is enabled, it will crash on reference-count mistakes that would otherwise pass silently.
- **Corrupted driver files.** Partial updates leave mismatched driver binaries that misbehave in subtle ways.
- **Overclocking or unstable undervolting.** Pushing CPU/GPU beyond stable limits corrupts in-flight data, including kernel reference counts.
- **Antivirus filter drivers.** Kernel-level security hooks that have not been updated for the new Windows build.

## How to fix it

Work through these in order. If crashes prevent booting, do the early steps from Safe Mode (**Shift** + **Restart** → **Troubleshoot** → **Advanced options** → **Startup Settings**).

### Fix 1: Identify the named driver on the blue screen

Do not skip the diagnosis — it saves you from updating everything blindly.

1. The next time the blue screen appears, look below the stop code for a file name in parentheses and photograph it with your phone.
2. Common mappings: `nvlddmkm.sys` = NVIDIA graphics, `igdkmdnd64.sys` = Intel graphics, `atikmdag.sys` = AMD graphics, `netwtw10.sys`/`Netwtw10.sys` = Intel Wi-Fi, `rtkvhd64.sys` = Realtek audio.
3. If no file is shown, assume the graphics driver and proceed — it is the cause in the majority of post-update cases.
4. Boot into Safe Mode to perform the driver work safely, since the crashing driver is dormant there.

### Fix 2: Clean-reinstall the graphics driver

A regular update leaves old files behind. A clean reinstall does not.

1. Download Display Driver Uninstaller and the latest driver for your GPU from the [NVIDIA driver download page](https://www.nvidia.com/Download/index.aspx) or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) (AMD owners: use AMD's official driver support page), depending on your hardware.
2. Disconnect from the internet to stop Windows Update from interfering.
3. Boot into Safe Mode, run DDU, select your GPU brand, and click **Clean and restart**.
4. Install the freshly downloaded driver, reconnect to the internet, and restart once more.
5. Use the laptop for a day before declaring victory — reference-count bugs can be intermittent.

### Fix 3: Update network and chipset drivers

If the dump named a network driver, or the graphics reinstall did not help, these are next.

1. Open **Device Manager** (**Win + X** → **Device Manager**).
2. Expand **Network adapters**, right-click your Wi-Fi adapter → **Update driver** → **Search automatically for drivers**.
3. Do the same under **System devices** for chipset entries, or better: get the full chipset package from your laptop manufacturer's support site.
4. Restart and test. Network-driver reference bugs often show up during sleep/wake or heavy downloads, so test those scenarios specifically.

### Fix 4: Check whether Driver Verifier is running

Verifier turns silent driver bugs into crashes — useful for debugging, terrible for daily use.

1. Open **Terminal (Admin)** and run `verifier /query`.
2. If it reports drivers under verification, run `verifier /reset` and restart.
3. If the crashes stop, Verifier was amplifying a minor driver flaw into a blue screen. Update that driver (per Fix 2/3) so the underlying flaw is gone too.
4. Never leave Verifier enabled on a daily-use laptop. Microsoft documents it as a testing tool in their [Windows support resources](https://support.microsoft.com/en-us/windows).

### Fix 5: Run SFC and DISM

Corrupted system files can corrupt the kernel structures drivers interact with.

1. In **Terminal (Admin)**, run `sfc /scannow` to completion.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth` (requires internet).
3. Run `sfc /scannow` again to confirm, then restart.
4. If you cannot boot normally, run these from the recovery command prompt: boot to **Troubleshoot** → **Advanced options** → **Command Prompt** and use `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows`.

### Fix 6: Test your RAM

When no driver is clearly at fault, memory is the next suspect — this stop code is a classic RAM symptom.

1. Press **Win + R**, type `mdsched.exe`, press **Enter**, and choose **Restart now and check for problems**.
2. Let the test finish. Any errors mean bad RAM, full stop — no driver update will fix that.
3. Reseat the modules and retest; if errors follow a specific stick, replace it.
4. Also revert any RAM overclocking/XMP profiles in the BIOS to stock speeds and retest — unstable memory timings cause exactly this crash.

### Fix 7: Uninstall the recent update and pause updates

If the crashes started within days of a specific update and nothing else helps, the update itself is the trigger.

1. Go to **Settings** → **Windows Update** → **Update history** → **Uninstall updates** and remove the most recent cumulative update.
2. Restart and test stability for 48 hours.
3. Use **Pause updates** to hold off reinstalling for a week or two while the driver vendor or Microsoft ships a fix.
4. Check the update's KB article for known issues — Microsoft sometimes acknowledges driver conflicts and offers a targeted fix.

## Closing

REFERENCE_BY_POINTER after a Windows 11 update is a driver detective story, and the blue screen usually hands you the first clue in the form of a `.sys` file name. Clean-reinstall that driver, verify Verifier is off, and test the RAM if the crashes persist — that sequence resolves the overwhelming majority of cases. Do not let anyone talk you into a full Windows reinstall before you have done the DDU clean-reinstall; it is faster and fixes the actual problem. For its close cousin involving bad memory addresses, see [DRIVER_IRQL_NOT_LESS_OR_EQUAL after a Windows 11 update](/articles/how-to-fix-driver-irql-not-less-or-equal-after-windows-11-update/), and for general crash recovery, [how to fix the blue screen of death on Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/).
