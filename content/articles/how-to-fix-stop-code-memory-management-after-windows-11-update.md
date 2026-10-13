---
title: "Fix the MEMORY_MANAGEMENT Blue Screen After a Windows 11 Update"
slug: how-to-fix-stop-code-memory-management-after-windows-11-update
date: 2026-09-26
categories: ["windows-errors"]
tags: ["memory management", "blue screen", "windows 11 update"]
description: "Fix the MEMORY_MANAGEMENT blue screen after a Windows 11 update: test your RAM, repair system files, and update the drivers behind stop code 0x1A."
thumbnail: "/images/thumbs/how-to-fix-stop-code-memory-management-after-windows-11-update.webp"
faqs:
  - q: "What does the MEMORY_MANAGEMENT stop code mean?"
    a: "Stop code 0x0000001A means Windows' memory manager detected serious corruption — bad page tables, corrupted pool memory, or faulty RAM. After a Windows 11 update, the trigger is usually an incompatible driver or corrupted system files, but genuinely failing RAM is always on the suspect list."
  - q: "Does this error always mean my RAM is broken?"
    a: "No. Drivers cause this crash more often than bad RAM does, especially right after an update. Test the easy things first — update drivers and run SFC — and only suspect the hardware if those do not help or if Windows Memory Diagnostic reports errors."
  - q: "Why did it start right after the Windows update?"
    a: "The update changed the kernel and memory manager behavior, which can expose a driver bug that was previously harmless. It can also corrupt system files if the install was interrupted. Both are fixable without replacing hardware."
  - q: "How long does Windows Memory Diagnostic take?"
    a: "The standard pass takes about 15–30 minutes depending on how much RAM you have. Let it finish completely — interrupting it early can miss errors. Run it when you can leave the laptop alone for a bit."
---

The MEMORY_MANAGEMENT blue screen (stop code 0x0000001A) is Windows' memory manager raising the alarm: something corrupted the structures it uses to track RAM. When it appears right after a Windows 11 update, the update is the trigger but rarely the root cause — it usually exposed a driver that was already misbehaving, or left system files in a bad state.

Do not assume your RAM is dead. Work the list below in order: drivers and system files first, hardware testing second, physical fixes last.

## Why this happens

- **An incompatible driver after the update:** Graphics, storage, and network drivers that have not been updated for the new Windows build corrupt memory manager structures.
- **Corrupted system files:** An interrupted or buggy update leaves damaged kernel files behind, and the memory manager is one of the first things to misbehave.
- **Failing RAM:** Bad memory cells corrupt page tables and pool allocations, producing this exact stop code.
- **Disk errors:** Bad sectors in the pagefile area cause the memory manager to read garbage when paging memory to disk.
- **Overclocked or mismatched RAM:** XMP profiles and mixed RAM sticks create instability that shows up as memory management crashes under load.
- **Third-party antivirus drivers:** Kernel-level security software that has not been updated for the new Windows build can corrupt pool memory.

- **Memory integrity conflicts:** Windows' Memory integrity (HVCI) feature plus an incompatible driver can produce 0x1A. Toggling it off temporarily is a legitimate diagnostic step — see Fix 8.
## How to fix it

Work through these in order — most post-update cases resolve by Fix 4.

### Fix 1: Update graphics, storage, and network drivers

1. Open **Device Manager** (right-click **Start**).
2. Update **Display adapters**, **Storage controllers**, and **Network adapters** — right-click each, choose **Update driver**, but prefer downloading from your laptop maker's support page for the newest versions.
3. For the GPU specifically, get a clean install from [NVIDIA](https://www.nvidia.com/Download/index.aspx), AMD, or [Intel's tool](https://www.intel.com/content/www/us/en/support/detect.html).
4. Restart. Post-update MEMORY_MANAGEMENT crashes are driver-caused more often than not, so this is the highest-value step.

### Fix 2: Run SFC and DISM

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. When it finishes, run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `sfc /scannow` once more to confirm everything is clean.
4. Restart and test for a day. If the update damaged system files, this is the repair — quick, safe, and surprisingly effective.

### Fix 3: Check the disk for errors

1. In **Terminal (Admin)**, run `chkdsk C: /f /r`.
2. Type **Y** when asked to schedule the check, then restart — the scan runs before Windows loads and can take 30+ minutes on large drives.
3. Bad sectors in the pagefile region cause exactly this stop code, and chkdsk maps them out.
4. If chkdsk finds many bad sectors, back up your data promptly — the drive itself may be failing. Disk-related crashes overlap with [page fault errors](/articles/how-to-fix-page-fault-in-nonpaged-area/), which share several of these fixes.

### Fix 4: Run Windows Memory Diagnostic

1. Press **Win + R**, type `mdsched.exe`, and press Enter.
2. Choose **Restart now and check for problems** and let the full test complete.
3. If errors are reported, power off and reseat the RAM modules if your laptop has accessible slots.
4. Retest. Persistent errors mean a failing module — replace it. No errors means your RAM is fine and the cause is software, which narrows the field considerably.

### Fix 5: Reset the pagefile to system-managed

1. Press **Win + R**, type `sysdm.cpl`, go to **Advanced → Performance → Settings → Advanced → Virtual memory → Change**.
2. Tick **Automatically manage paging file size for all drives**.
3. Click **Set**, then **OK**, and restart.
4. A manually-sized or corrupted pagefile can trigger 0x1A. Letting Windows manage it eliminates that variable entirely.

### Fix 6: Disable overclocks and test with default RAM settings

1. Enter the BIOS at boot (**F2**/**Del**/**Esc** depending on brand).
2. Choose **Load Optimized Defaults** — this disables XMP and any CPU overclock.
3. Save and exit, then use the laptop under normal load for a day or two.
4. If the crashes stop, your RAM overclock was not stable with the new Windows build. You can try re-enabling XMP later, but stability beats a few percent of memory bandwidth.

### Fix 7: Uninstall the update or do a repair install

1. If crashes began with a specific update, go to **Settings → Windows Update → Update history → Uninstall updates** and remove it.
2. Pause updates for two weeks to give vendors time to ship fixed drivers.
3. If uninstalling is not an option, do an in-place repair: download Windows 11 from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11), run setup, and choose **Keep personal files and apps**.
4. For broader post-update crash triage, our [general post-update guide](/articles/how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update/) covers the full checklist.

### Fix 8: Test with Memory integrity toggled off

Memory integrity is a worthwhile security feature, but it changes how drivers interact with memory. If an incompatible driver is the problem, this test exposes it quickly.

1. Open **Settings → Privacy & security → Windows Security → Device security → Core isolation details**.
2. Turn **Memory integrity** off and restart when prompted.
3. Use the laptop normally for a day or two. If the 0x1A crashes stop, an incompatible driver was clashing with HVCI.
4. Update every driver (graphics, chipset, network, storage) to the latest versions, then turn Memory integrity back on.
5. If crashes return with it on even after driver updates, leave it off and note which driver version you are on — report the incompatibility to the driver vendor.

## Closing

MEMORY_MANAGEMENT after a Windows 11 update is guilty-until-proven-innocent for your drivers — update them first, repair system files second, test the RAM third, and check the Memory integrity interaction fourth. The physical memory is actually fine in most cases; it is the software managing that memory that went sideways when the update landed. Work the list in order and stop code 0x1A becomes a story you tell about a bad driver week, not an ongoing problem.
