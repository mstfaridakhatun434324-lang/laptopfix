---
title: "Fixing the SYSTEM_SERVICE_EXCEPTION Blue Screen on Windows 11"
slug: how-to-fix-system-service-exception-youtube
date: 2026-09-09
categories: ["windows-errors"]
tags: ["blue screen", "system service exception", "stop code 0x3b", "driver crash", "windows 11"]
description: "SYSTEM_SERVICE_EXCEPTION (0x3B) blue screens ruining your day? Identify the faulty driver and fix this common crash in 7 proven steps."
thumbnail: "/images/thumbs/how-to-fix-system-service-exception-youtube.webp"
faqs:
  - q: "What does SYSTEM_SERVICE_EXCEPTION mean?"
    a: "It's stop code 0x0000003B. A system service — usually a driver running in kernel mode — threw an exception while executing privileged code. In plain English: a driver tried to do something illegal at the deepest level of Windows, and the system crashed to contain it. The named .sys file on the blue screen tells you which driver."
  - q: "Which drivers cause SYSTEM_SERVICE_EXCEPTION most often?"
    a: "Graphics drivers (nvlddmkm.sys, atikmdag.sys), network drivers, and antivirus filter drivers top the list. The pattern matters: crashes during gaming point at the GPU driver, crashes on Wi-Fi connect point at the network driver."
  - q: "Can Windows updates cause this error?"
    a: "Yes — a Windows update can install a new driver version that's buggy, or change kernel behavior that an old third-party driver can't handle. If crashes started right after an update, roll back the driver or uninstall the update first. See our [update-specific SYSTEM_SERVICE_EXCEPTION guide](/articles/how-to-fix-system-service-exception-after-windows-11-update/)."
  - q: "Is my hardware failing?"
    a: "Usually not. This stop code is overwhelmingly driver-related. Only suspect hardware if crashes blame different drivers every time, which points to RAM or the storage drive corrupting driver code as it loads."
---

SYSTEM_SERVICE_EXCEPTION (0x3B) is one of the most common blue screens on Windows 11, and it's also one of the most fixable. The name means a privileged system routine — almost always a driver — hit an error it couldn't handle. Because the blue screen usually names the offending `.sys` file, you often get the answer handed to you right on the crash screen.

The trick is reading that clue correctly and then working the driver layer methodically instead of reinstalling Windows in a panic.

## Why this happens

- **Corrupt or incompatible device driver.** The named `.sys` file on the crash screen is guilty until proven innocent — graphics and network drivers lead the pack.
- **Driver updated automatically by Windows Update.** A fresh-but-buggy driver lands silently, and crashes start the next day with no obvious trigger.
- **Antivirus or security filter drivers.** Kernel-level security software throws exceptions when its hooks conflict with system updates.
- **Corrupted system files.** Damage to the kernel or service executables makes legitimate calls fail.
- **Faulty RAM corrupting loaded drivers.** Random bit flips in driver code produce exceptions in drivers that are actually fine.
- **Overclocking instability.** Marginal CPU or RAM overclocks corrupt kernel data structures under load.

## How to fix it

Work through these in order — start with Fix 1 and stop when the crashes stop.

### Fix 1: Read the crash screen and note the .sys file

The blue screen is giving you a diagnosis — capture it.

1. The next time it crashes, look for a filename near the bottom, like `nvlddmkm.sys` or `Netwtw10.sys`.
2. Take a phone photo if it disappears too fast to read.
3. Search your memory: does the filename suggest graphics (nv, amd, igdkmd), network (netw, rt640x64), or storage (stornvme, iaStor)?
4. That category becomes your prime suspect for Fix 2.
5. If no filename appears, check `C:\Windows\Minidump` with BlueScreenView to extract it from the dump.

### Fix 2: Update or roll back the named driver

Most 0x3B crashes end here.

1. Open **Device Manager** (**Windows + X**, then select it).
2. Locate the device matching the suspect driver and open **Properties > Driver**.
3. If crashes began after a recent change, click **Roll Back Driver** and restart.
4. Otherwise click **Update driver > Search automatically for drivers**.
5. For graphics crashes, do a full clean reinstall from [NVIDIA](https://www.nvidia.com/Download/index.aspx) or [AMD](https://www.amd.com/en/support/download/drivers.html) — uninstall the old driver first, then install fresh.
6. For network crashes, grab the latest driver from your laptop maker's support page rather than relying on Windows Update's version.

If you'd rather see the full driver-focused methodology, our [SYSTEM_SERVICE_EXCEPTION on Windows 11 deep dive](/articles/system-service-exception-windows-11-fix/) covers the same ground with extra detail.

### Fix 3: Remove third-party antivirus and filter drivers

Security software lives at exactly the level where 0x3B occurs.

1. Open **Settings > Apps > Installed apps** and uninstall any third-party antivirus, "PC optimizer," or firewall suite.
2. Restart — Windows Defender enables itself automatically, so you're protected.
3. Test for a day or two of normal use.
4. If stability returns, the removed product's driver was the cause; only reinstall it after confirming a newer version exists.
5. Also uninstall VPN clients temporarily if crashes coincide with connecting or disconnecting.

### Fix 4: Run SFC and DISM to repair system files

Rule out corruption in Windows' own service code.

1. Open **Terminal (Admin)** from the **Start** right-click menu.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for it to reach 100%.
3. Then run `sfc /scannow` and let it complete.
4. Restart the laptop even if no corruption was reported.
5. Retest under the conditions that previously triggered the crash.

### Fix 5: Test memory and reset overclocks

Cover the hardware suspects that mimic driver bugs.

1. Press **Windows + R**, type `mdsched.exe`, and run the memory diagnostic.
2. Check results afterward in **Event Viewer > Windows Logs > System** under **MemoryDiagnostics-Results**.
3. Enter BIOS/UEFI and disable XMP/EXPO profiles plus any CPU overclock or undervolt.
4. Select **Load Optimized Defaults**, save, and exit.
5. If crashes stop at stock settings, the overclock was corrupting kernel operations.

### Fix 6: Perform a clean boot to isolate software conflicts

Find out whether a background program is triggering the driver.

1. Press **Windows + R**, type `msconfig`, and press Enter.
2. On the **Services** tab, tick **Hide all Microsoft services**, then click **Disable all**.
3. Open **Task Manager > Startup apps** and disable everything.
4. Restart — Windows now boots with minimal third-party software.
5. If crashes stop, re-enable items in halves until the culprit returns, then update or remove it.

### Fix 7: Update BIOS/UEFI and reset Windows as a last resort

When everything software-side checks out, refresh the firmware and OS.

1. Visit your manufacturer's support page and install the latest BIOS/UEFI — firmware updates frequently fix driver-hardware interaction bugs.
2. Keep the charger connected and never interrupt a firmware flash.
3. If crashes persist, go to **Settings > System > Recovery > Reset PC** and choose **Keep my files**.
4. After the reset, install drivers one at a time from the manufacturer's page, testing between each.
5. Microsoft's [Windows troubleshooting hub](https://support.microsoft.com/en-us/windows) offers guided recovery if the reset stalls.

### Fix 8: Scan for rootkits and boot-level malware

Kernel-hooking malware throws the same exceptions as a buggy driver, so rule it out before closing the case.

1. Go to **Windows Security > Virus & threat protection > Scan options** and run a **Microsoft Defender Offline scan** — it reboots into a clean environment outside Windows.
2. Follow up with a second-opinion on-demand scan from a reputable free scanner (Malwarebytes Free works well for this).
3. Quarantine anything found and restart normally afterward.
4. Once clean, re-run `sfc /scannow` in **Terminal (Admin)** — malware frequently damages system files, and you want those repaired after removal.
5. If both scans are clean and crashes persist, the driver stack is fully exonerated and a Windows reset is the reasonable next step.

## Closing

SYSTEM_SERVICE_EXCEPTION rewards methodical driver work: read the `.sys` name, fix that driver, and clear out the filter drivers that love to cause it. Skip the temptation to reinstall Windows first — nine times out of ten, the answer is a single misbehaving driver, and this list finds it without wiping your setup. If the exception appeared right after a Windows 11 update, the [post-update System Service Exception guide](/articles/how-to-fix-system-service-exception-after-windows-11-update/) covers the update-specific driver regressions.
