---
title: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Best Way to Fix It"
slug: best-way-to-fix-system-thread-exception-not-handled
date: 2026-10-12
categories: ["windows-errors"]
tags: ["bsod", "stop code", "drivers", "graphics"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED blue screen? A system thread threw an exception nobody caught — usually graphics drivers. Best fix order inside."
thumbnail: "/images/thumbs/best-way-to-fix-system-thread-exception-not-handled.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "A thread running in kernel mode (a system thread, usually inside a driver) generated an exception that no error handler caught. Windows stops the system because an unhandled kernel exception means internal state can't be trusted. Graphics drivers are the most common source."
  - q: "Why do graphics drivers cause this error so often?"
    a: "GPU drivers are the largest, most complex kernel drivers on a typical laptop, with huge amounts of threaded code. More threads plus more complexity equals more chances for an unhandled exception — which is why the crash screen so often names nvlddmkm.sys, dxgkrnl.sys, or atikmdag.sys."
  - q: "Can I fix it without knowing which driver is guilty?"
    a: "You can try the shotgun approach — update graphics, chipset, and other drivers — and it works often enough. But reading the minidump takes five minutes and tells you exactly which driver to target, saving you from updating (and possibly breaking) drivers that were fine."
  - q: "Is SYSTEM_THREAD_EXCEPTION_NOT_HANDLED a hardware problem?"
    a: "Usually not, but overheating GPUs and failing VRAM produce exceptions in graphics drivers that look identical to driver bugs. If driver fixes fail and crashes happen under 3D load, check GPU temperatures and test with the GPU underclocked slightly."
---

`SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` (stop code `0x0000007E`) is the kernel-mode cousin of an uncaught exception: a system thread — code running on behalf of a driver deep in the kernel — hit an error nobody handled, and Windows pulled the plug. In practice, this crash has a favorite author: graphics drivers. The crash screen frequently names `nvlddmkm.sys` (NVIDIA), `dxgkrnl.sys` (DirectX graphics kernel), or `atikmdag.sys` (AMD), which is as close to a signed confession as blue screens get.

But "usually graphics" isn't "always graphics," and blindly reinstalling GPU drivers while the real culprit is a storage driver wastes an afternoon. The best fix order reads the evidence first, then acts on it — graphics drivers get priority, but the dump has the final say.

## Why this happens

- **Buggy graphics drivers**: The top cause by a wide margin. Complex, heavily threaded GPU drivers throw unhandled exceptions from driver bugs, corrupt installs, or version mismatches.
- **Mismatched driver components**: A GPU driver whose user-mode and kernel-mode parts are different versions (from a partial update) throws exceptions at the boundary.
- **Overheating GPU**: Thermal stress causes GPU errors that surface as driver exceptions — crashes only under gaming or 3D load are the tell.
- **Other faulty drivers**: Storage, network, and audio drivers can all throw unhandled system-thread exceptions; the dump distinguishes them.
- **Corrupt system files**: Damage to kernel thread-management components.
- **Failing RAM**: Bad memory corrupts thread stacks, producing exceptions the driver didn't cause.
- **Overclocked GPU or CPU**: Unstable clocks corrupt driver computations under load.

## How to fix it

Work through these in order — identify the thread's owner first, then fix that specific driver.

### Fix 1: Read the minidump to name the driver

Five minutes that saves hours of blind updates.

1. Open the newest `.dmp` in `C:\Windows\Minidump` with WinDbg Preview and run `!analyze -v`.
2. Note the blamed module: `nvlddmkm.sys` = NVIDIA, `atikmdag.sys`/`amdkmdag.sys` = AMD, `igdkmd64.sys` = Intel graphics, `dxgkrnl.sys` = DirectX kernel (points at the GPU driver above it).
3. If it's consistently one driver, that's your target for Fix 2. If it varies, suspect RAM or overheating and jump to Fix 5 after Fix 2.
4. Write down the exact name — targeted fixes beat shotgun updates.

### Fix 2: Clean-install the graphics driver

The highest-probability fix for this stop code.

1. Download the latest driver for your GPU: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) for Intel graphics.
2. During installation, choose **Custom** and tick **Clean install** (NVIDIA) or use Display Driver Uninstaller in Safe Mode for a truly clean slate.
3. Prefer your laptop maker's customized graphics driver if the generic one misbehaves — manufacturer tuning matters on laptops.
4. Restart and stress-test with the workload that used to crash it.

### Fix 3: Update chipset, storage, and remaining drivers

When the dump blames something other than graphics.

1. Open **Device Manager** (**Win + X**) and update **Storage controllers**, **System devices**, and **Network adapters**.
2. Get chipset drivers from your laptop maker's support page — they govern how the GPU talks to the rest of the system.
3. If the dump named an audio or network driver, update exactly that one from the manufacturer.
4. Don't update drivers that the dump never implicated and that are working — "update everything" introduces new variables.

### Fix 4: Repair system files

Corruption in kernel thread handling.

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Restart. If the crashes started after a Windows update, this repairs update damage to the thread infrastructure.

### Fix 5: Check GPU thermals and test RAM

Hardware causes that mimic driver bugs.

1. Monitor GPU temperatures under load with HWMonitor — sustained temps above 90°C on a laptop GPU invite exactly these exceptions.
2. Clean vents with compressed air; repaste if the machine is old and still hot.
3. Run `mdsched.exe` for a RAM check — bad memory corrupts thread stacks identically to driver bugs.
4. If crashes only happen in games, try slightly lowering the GPU clock with the vendor's tuning tool as a diagnostic — stability at lower clocks proves thermal/marginal-silicon causes.

### Fix 6: Update the BIOS

Firmware fixes for GPU initialization and power management.

1. Check your BIOS version with `msinfo32` and compare against your manufacturer's support page.
2. Flash with the charger plugged in. BIOS updates regularly fix the PCIe power-management quirks that trigger graphics-driver exceptions.

### Fix 7: Clean-boot to isolate software conflicts

Overlays and "boosters" inject into graphics threads.

1. Press **Win + R**, type `msconfig`, press Enter. Hide Microsoft services, disable the rest; disable all startup items.
2. Restart and test. Game overlays (Discord, GeForce Experience overlay), screen recorders, and "game booster" utilities inject code into graphics threads and cause unhandled exceptions.
3. Re-enable in halves to find the culprit, then update or remove it.

### Fix 8: Reset Windows

For a driver stack too tangled to repair piecemeal.

1. Back up your files.
2. **Settings** > **System** > **Recovery** > **Reset this PC** > **Keep my files**.
3. After the reset, install the graphics driver from the laptop maker first, then let Windows Update handle the rest.
4. Crashes surviving a reset with clean drivers point at hardware — GPU, VRAM, or motherboard — and need professional diagnostics.
5. For the post-update variant of this crash, see [SYSTEM_THREAD_EXCEPTION_NOT_HANDLED after a Windows 11 update](/articles/how-to-fix-system-thread-exception-not-handled-after-windows-11-update/), and for general methodology, [how to fix the blue screen of death](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Closing

The best way to fix `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` is to let the evidence lead: read the minidump, clean-install the named driver (usually graphics), and only then broaden to thermals, RAM, and clean boots. The stop code's reputation as a "graphics driver crash" is well earned, but the dump is what turns reputation into certainty. Fix the right driver and this particular blue screen doesn't come back.
