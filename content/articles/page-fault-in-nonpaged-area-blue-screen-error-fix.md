---
title: "PAGE_FAULT_IN_NONPAGED_AREA: How to Fix This Blue Screen"
slug: page-fault-in-nonpaged-area-blue-screen-error-fix
date: 2026-09-18
categories: ["windows-errors"]
tags: ["blue screen", "memory", "windows 11"]
description: "Seeing PAGE_FAULT_IN_NONPAGED_AREA on a blue screen? This guide explains what it means and walks you through memory, driver, and disk fixes."
thumbnail: "/images/thumbs/page-fault-in-nonpaged-area-blue-screen-error-fix.webp"
faqs:
  - q: "What does PAGE_FAULT_IN_NONPAGED_AREA actually mean?"
    a: "It means a driver or system process tried to read memory that was marked as unavailable — either the data was never there, or the page it pointed to got corrupted. In practice, it points to faulty RAM, a bad driver, or disk/file-system corruption in about that order of likelihood."
  - q: "Is this error caused by bad RAM?"
    a: "Often, yes — failing RAM is the single most common cause. But drivers (especially storage and antivirus filter drivers) and corrupted page files cause it too. Run Windows Memory Diagnostic first since it's free and quick; replace RAM only if the test confirms errors."
  - q: "Can a recent Windows update trigger this blue screen?"
    a: "Absolutely. Updates frequently change driver behavior or expose latent hardware faults. If the crashes started right after an update, roll back the update or update the implicated driver. Check the minidump file name on the blue screen — it often names the faulty driver."
  - q: "Should I worry about data loss from this error?"
    a: "The error itself doesn't delete files, but repeated crashes can corrupt open files and the file system. Back up your important data before running memory tests and disk repairs, then run chkdsk to verify file-system integrity."
---
PAGE_FAULT_IN_NONPAGED_AREA (stop code 0x00000050) is one of the more common blue screens on Windows laptops, and it has a reputation for being scary. Don't worry — the name sounds worse than the problem usually is. It simply means something tried to use a chunk of memory that wasn't available, and Windows stopped everything rather than risk corruption.

The three usual suspects are bad RAM, a misbehaving driver, and disk corruption. This guide helps you identify which one is yours and fix it, starting with the easy checks. If you're seeing other stop codes too, our [general blue screen repair guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the universal approach.

## Why this happens

- **Failing or incompatible RAM.** Bad memory cells return garbage when read, triggering the fault.
- **Faulty device drivers.** Storage, display, and antivirus filter drivers are the most common software culprits.
- **Corrupted page file.** If `pagefile.sys` is damaged, memory paging goes wrong.
- **Disk errors or bad sectors.** Corruption in the paging area on disk produces the same symptom as bad RAM.
- **Overclocked or misconfigured memory.** Wrong RAM timings in BIOS/UEFI cause intermittent faults.
- **Antivirus filter drivers.** Third-party security software hooks deep into memory management.
- **Recent Windows update.** Updates can destabilize previously working drivers or expose weak hardware.

## How to fix it

Work through these in order — note the driver file name on the blue screen if one is shown.

### Fix 1: Boot into Safe Mode and note the details

Before fixing, gather evidence.

1. Boot into Safe Mode using the forced-restart method: hold the power button during boot 2-3 times until **Automatic Repair** appears, then **Advanced options > Troubleshoot > Advanced options > Startup Settings > Restart** and press **4**.
2. In Safe Mode, open **Event Viewer** (**Win + X > Event Viewer**).
3. Go to **Windows Logs > System** and look for **BugCheck** entries around the crash time — they record the stop code and sometimes the driver.
4. Also check `C:\Windows\Minidump` for `.dmp` files; note the date of the newest one.
5. If the blue screen named a file (like `ntfs.sys` or a driver name), write it down — it tells you exactly where to focus. A crash naming [NTFS.SYS points at storage](/articles/how-to-fix-ntfs-sys-blue-screen-on-lenovo-laptop/), not memory.
6. If Safe Mode itself crashes, skip to Fix 4 — that's a strong hint at hardware.

### Fix 2: Run Windows Memory Diagnostic

Free, built in, and catches most bad RAM.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. The laptop reboots into the memory test. Let the standard pass complete — about 10-20 minutes.
4. After Windows boots, open **Event Viewer > Windows Logs > System** and filter for source **MemoryDiagnostics-Results** to read the outcome.
5. If errors are found, you have bad RAM. Power off, reseat the memory modules (if accessible), and retest.
6. If errors persist, replace the faulty stick. On laptops with soldered RAM, this means a service visit — back up your data first.

### Fix 3: Update or roll back drivers

If memory tests clean, the driver layer is next.

1. Open **Device Manager** (**Win + X > Device Manager**).
2. Look for any device with a yellow warning triangle — update those first via **Update driver > Search automatically for drivers**.
3. Pay special attention to **Display adapters**, **Storage controllers**, and **Network adapters**.
4. If the crashes started after a driver update, right-click the device, open **Properties > Driver**, and use **Roll Back Driver**.
5. For the most reliable drivers, download from your laptop maker's support site rather than relying on Windows Update. Intel users can also run the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
6. Restart and use the laptop normally for a day — intermittent faults need time to show themselves.

### Fix 4: Check the disk for errors

Bad sectors in the paging area mimic bad RAM.

1. Open an elevated terminal: right-click **Start > Terminal (Admin)**.
2. Run a read-only check first:
   `chkdsk C:`
3. If it reports errors, schedule a full repair:
   `chkdsk C: /f /r`
4. Type **Y** when asked to schedule at next restart, then reboot. The scan can take an hour or more on large drives — let it finish.
5. After the scan, check drive health with your manufacturer's SSD tool or CrystalDiskInfo (from its official site).
6. If the drive shows reallocated sectors or a failing SMART status, clone it to a new SSD promptly — no software fix repairs dying storage.

### Fix 5: Disable the page file, then re-enable it

This rebuilds a potentially corrupted `pagefile.sys`.

1. Press **Win + R**, type `sysdm.cpl`, and press **Enter**.
2. Go to the **Advanced** tab and click **Settings** under Performance.
3. Switch to the **Advanced** tab in Performance Options and click **Change** under Virtual memory.
4. Uncheck **Automatically manage paging file size for all drives**.
5. Select **No paging file**, click **Set**, then **OK**, and restart.
6. After rebooting, go back and re-check **Automatically manage paging file size for all drives**, click **Set**, and restart again. Windows creates a fresh page file.

### Fix 6: Temporarily remove third-party antivirus

Filter drivers from security suites are a known trigger.

1. Open **Settings > Apps > Installed apps** and uninstall your third-party antivirus (note your license key first).
2. Restart — Windows Defender activates automatically, so you're still protected.
3. Use the laptop for a day or two. If the blue screens stop, the antivirus driver was the cause.
4. Reinstall the latest version of your antivirus from the vendor's official site — newer builds often fix the conflict.
5. If crashes continue without third-party antivirus installed, the cause is elsewhere; proceed to Fix 7.
6. Never run without any antivirus — Defender is a fine fallback, but don't leave the machine unprotected.

### Fix 7: Repair system files and update Windows

The final software sweep before suspecting hardware.

1. Open an elevated terminal and run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
2. When that completes, run:
   `sfc /scannow`
3. Restart, then go to **Settings > Windows Update** and install all pending updates. Microsoft documents known crash fixes on [support.microsoft.com](https://support.microsoft.com/en-us/windows) — check whether your stop code has a known patch.
4. Also install optional driver updates from **Windows Update > Advanced options > Optional updates**.
5. If crashes persist after clean memory, clean disk, fresh drivers, and repaired system files, you're likely looking at a motherboard or soldered-RAM hardware fault — time for professional service with your minidump files in hand.

## Closing

PAGE_FAULT_IN_NONPAGED_AREA almost always comes down to memory, drivers, or disk — and the order above tests them from most to least likely. Don't skip the memory test just because your RAM is new; even fresh modules fail. And always note the driver file name on the blue screen when one appears — that single detail can cut your troubleshooting time in half.
