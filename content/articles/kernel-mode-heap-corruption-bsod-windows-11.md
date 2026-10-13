---
title: "KERNEL_MODE_HEAP_CORRUPTION BSOD on Windows 11: How to Fix It"
slug: kernel-mode-heap-corruption-bsod-windows-11
date: 2026-09-04
categories: ["windows-errors"]
tags: ["KERNEL_MODE_HEAP_CORRUPTION", "driver errors", "BSOD fixes"]
description: "Fix KERNEL_MODE_HEAP_CORRUPTION BSOD on Windows 11: update graphics drivers, test RAM, repair system files, and stop heap corruption crashes."
thumbnail: "/images/thumbs/kernel-mode-heap-corruption-bsod-windows-11.webp"
faqs:
  - q: "What does KERNEL_MODE_HEAP_CORRUPTION mean?"
    a: "It means Windows detected corruption in the kernel's heap — the memory pool drivers use for dynamic allocation. Stop code 0x13A fires when a driver writes outside its heap allocation or frees memory incorrectly. Graphics drivers are the most common offenders, followed by faulty RAM and corrupted system files."
  - q: "Which driver usually causes this error?"
    a: "Graphics drivers lead the pack: NVIDIA's nvlddmkm.sys, AMD's atikmdag.sys, and Intel's graphics drivers all allocate heavily from the kernel heap. If crashes happen during gaming, video playback, or GPU-accelerated work, the GPU driver is suspect number one. A clean driver reinstall with DDU fixes most cases."
  - q: "Can bad RAM cause KERNEL_MODE_HEAP_CORRUPTION?"
    a: "Yes — faulty RAM corrupts heap contents just as readily as buggy drivers do. If driver reinstalls don't help, or if every crash dump blames a different component, test your memory with Windows Memory Diagnostic or MemTest86. Heap corruption from hardware looks identical to heap corruption from software in the dump."
  - q: "Is this error related to overclocking?"
    a: "Frequently. Overclocked GPUs (even factory overclocks on some gaming laptops) and unstable VRAM produce heap corruption under load. If you've used MSI Afterburner or similar tools, reset to stock clocks as a diagnostic step. Factory-overclocked cards that degrade over time can also start throwing this error years into their life."
---

KERNEL_MODE_HEAP_CORRUPTION (stop code `0x13A`) is Windows catching a driver red-handed: something wrote outside its allocated heap memory or freed the same block twice, and the kernel's heap integrity checks caught it. On Windows 11 laptops, the graphics driver is guilty more often than not — especially under gaming or video workloads.

The diagnostic approach mirrors other heap-adjacent crashes like [win32kfull.sys BSODs](/articles/how-to-fix-win32kfull-sys-bsod-on-windows-11/): graphics driver first, RAM second, system files third. The heap is where drivers do their most delicate work, so corruption there points squarely at driver quality. Work the list in order and you'll find the corruptor.

## Why this happens

- Buggy or corrupt graphics drivers corrupting kernel heap allocations.
- Factory or manual GPU overclocks destabilizing VRAM under load.
- Faulty system RAM corrupting heap contents.
- Third-party antivirus or virtualization drivers mishandling heap memory.
- Corrupted Windows system files damaging heap management code.
- A Windows update exposing latent heap bugs in older drivers.
- Corrupted page file feeding damaged heap data back into the kernel on resume from hibernation.

## How to fix it

Work through these in order — graphics first, since it's the top cause.

### Fix 1: Cleanly reinstall the graphics driver with DDU

Heap corruption from GPU drivers is the number-one cause — give the driver a truly clean slate.

1. Download **Display Driver Uninstaller (DDU)** and the latest driver for your GPU.
2. Disconnect from the internet so Windows can't interfere mid-process.
3. Boot into **Safe Mode** and run DDU: **Clean and restart**.
4. Install the fresh driver from [NVIDIA's official download page](https://www.nvidia.com/Download/index.aspx) or your GPU vendor's site.
5. Test with the exact workload that crashed before — games, renders, or video calls.

### Fix 2: Reset GPU clocks to stock

Overclocks — including ones you didn't set — are a classic heap-corruption trigger.

1. Open **MSI Afterburner** or your GPU tuning tool and click **Reset**.
2. Better: uninstall the tuning tool so its profile can't reapply at boot.
3. Check your laptop maker's control software (Armoury Crate, Legion Toolkit, OMEN Hub) for GPU overclock modes and disable them.
4. Some "performance" modes are mild factory overclocks — test in **Balanced** mode.
5. Retest under load; stability at stock clocks confirms the overclock was guilty.

### Fix 3: Test the system RAM

Heap corruption from bad RAM is indistinguishable from driver-caused corruption — test to tell them apart.

1. Press **Win + R**, type `mdsched.exe`, and run **Windows Memory Diagnostic**.
2. Check results in **Event Viewer > Windows Logs > System** (**MemoryDiagnostics-Results**).
3. For a definitive answer, run **MemTest86** from USB for 4 full passes.
4. Reseat modules before replacing; test sticks individually.
5. Replace any failing stick — heap errors from hardware never fix themselves.

### Fix 4: Remove heap-abusing third-party drivers

Antivirus filters and virtualization drivers allocate from the same kernel heap.

1. Uninstall third-party antivirus via **Settings > Apps > Installed apps**.
2. Temporarily disable virtualization software (VMware, VirtualBox) and Hyper-V if installed.
3. Restart — Windows Security covers protection in the meantime.
4. Test for several days; stability here is a definitive diagnosis.
5. Reinstall only current versions, one product at a time.

### Fix 5: Repair system files

Corrupted heap-management code in Windows itself can trigger false corruption reports.

1. Open an elevated Command Prompt.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Then run `sfc /scannow` and restart.
4. Run `chkdsk C: /f` to rule out file-system damage.
5. Microsoft documents these tools on its [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 6: Read the dump for the corrupting driver

When general fixes miss, the dump's stack trace points at the heap abuser.

1. Open the latest `.dmp` in `C:\Windows\Minidump` with **WinDbg Preview**.
2. Run `!analyze -v` and examine the **STACK_TEXT** for third-party drivers.
3. Heap corruption dumps often implicate the allocator victim rather than the corruptor — look one or two frames deeper.
4. Update or remove whatever third-party driver the stack implicates.
5. If only Microsoft modules appear, lean harder on the RAM and GPU-overclock angles.

### Fix 7: Check thermals and power delivery

Heat and unstable power cause the bit-flips that heap checks catch.

1. Monitor GPU and CPU temperatures with **HWiNFO64** under load.
2. Clean vents and fans; replace dried thermal paste on older laptops.
3. Use the original charger — underpowered adapters cause GPU memory errors.
4. Test plugged in with the **Best performance** power plan.
5. If a specific temperature threshold always precedes crashes, cooling is your fix.

### Fix 8: Roll back the triggering update

When crashes begin after a Windows or driver update, the update exposed or introduced the heap bug.

1. Open **Settings > Windows Update > Update history > Uninstall updates**.
2. Remove the most recent update and restart.
3. Alternatively, roll back the GPU driver in **Device Manager > Display adapters > Properties > Driver**.
4. Block the bad version with the **Show or Hide Updates** troubleshooter.
5. Our [NTFS.sys BSOD guide](/articles/how-to-fix-ntfs-sys-blue-screen-in-windows-11-24h2/) covers similar update-rollback tactics for driver-triggered crashes.

## Closing

KERNEL_MODE_HEAP_CORRUPTION is the kernel catching someone writing where they shouldn't: usually the graphics driver, sometimes the RAM, occasionally a third-party filter. Clean-reinstall the GPU driver, reset the clocks, test the memory, and the heap stays intact. The dump confirms the suspect when the obvious fixes don't — use it before assuming the worst, because the worst is rarely what's happening. Heap corruption sounds exotic, but the fix is usually as mundane as a driver reinstall — which is good news for everyone. Don't let the intimidating name push you toward drastic measures; the methodical path in this guide resolves nearly every case without touching your files or settings — a far better outcome than a blind reinstall would ever give you anyway, guaranteed. Work the list patiently, trust what the dump tells you, and the crashes will stop for good.
