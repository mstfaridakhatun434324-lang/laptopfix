---
title: "How to Fix KMODE_EXCEPTION_NOT_HANDLED on a Windows Laptop"
slug: how-to-fix-kmode-exception-not-handled-youtube
date: 2026-09-06
categories: ["windows-errors"]
tags: ["blue screen", "kmode exception", "driver error"]
description: "KMODE_EXCEPTION_NOT_HANDLED blue screen? A kernel-mode driver crashed. Here's how to identify the faulty driver and fix it — Safe Mode to clean installs."
thumbnail: "/images/thumbs/how-to-fix-kmode-exception-not-handled-youtube.webp"
faqs:
  - q: "What does KMODE_EXCEPTION_NOT_HANDLED mean?"
    a: "A driver running in kernel mode (the privileged core of Windows) generated an exception — usually an illegal memory access — that wasn't handled. Windows crashes to protect itself. It's a driver bug in the vast majority of cases, occasionally faulty RAM."
  - q: "Which drivers cause KMODE_EXCEPTION_NOT_HANDLED most often?"
    a: "Network drivers (especially Wi-Fi), graphics drivers, and storage drivers top the list. The blue screen often names the file — common ones include netwtw10.sys (Intel Wi-Fi), nvlddmkm.sys (NVIDIA), and rtwlane.sys (Realtek). Antivirus filter drivers are also frequent offenders."
  - q: "Can overclocking cause this blue screen?"
    a: "Yes. Overclocked CPUs, GPUs, or RAM running XMP profiles can produce kernel exceptions under load that look exactly like driver bugs. If you overclock, return everything to stock speeds as a test before blaming drivers."
  - q: "How do I fix it if I can't boot into Windows?"
    a: "Use Safe Mode — it loads a minimal driver set that usually bypasses the crashing driver. From there, update, roll back, or uninstall the suspect driver. If Safe Mode also crashes, use the recovery environment's Command Prompt and System Restore."
---
KMODE_EXCEPTION_NOT_HANDLED is the kernel-mode cousin of the thread exception crash: a driver operating with full system privileges did something illegal — usually touching memory it shouldn't — and Windows stopped everything to contain it. Like its sibling stop codes, it frequently names the offending driver file on the blue screen itself.

Catch that filename if you can; it shortcuts the whole investigation. Work through these in order otherwise. For the quick-reference variant, see [KMODE exception not handled (best fixes)](/articles/best-way-to-fix-kmode-exception-not-handled/), and for the closely related crash, [IRQL not less or equal on HP](/articles/how-to-fix-irql-not-less-or-equal-on-hp-laptop/).

## Why this happens

- **Faulty network driver:** Wi-Fi and Ethernet drivers are the single most common named culprits.
- **Buggy graphics driver:** Especially after major driver version jumps.
- **Corrupted driver binaries:** Disk damage to an otherwise fine driver.
- **Antivirus filter drivers:** Kernel-level AV operating where mistakes are fatal.
- **Overclocking instability:** CPU/GPU/RAM pushed past stable limits.
- **Faulty RAM:** Bad memory cells corrupting kernel-mode operations.
- **Windows update driver replacement:** An update swapping your working driver for a broken inbox version.
- **VPN and network filter drivers:** Virtual network adapters from VPN clients operate in kernel mode and crash here when outdated — update or reinstall your VPN client if crashes coincide with its use.
- **Corrupted hibernation data:** A damaged hiberfil.sys can throw kernel exceptions on resume; rebuilding it with `powercfg /hibernate off` then `powercfg /hibernate on` rules this out.

## How to fix it

Work through these in order — start with Fix 1 and stop as soon as the blue screens stop appearing.

### Fix 1: Note the faulting driver name

The blue screen is trying to hand you the answer — take it.

1. Photograph the blue screen, noting any **"What failed:"** file name.
2. If it flashes by too fast, [disable automatic restart after blue screens](/articles/how-can-i-disable-automatic-restart-after-bsod/) first.
3. Also note any error code in parentheses after the stop code name — it occasionally narrows things down further.
3. Cross-reference: `netwtw*.sys` = Intel Wi-Fi, `rtwlane.sys`/`rtwlanu.sys` = Realtek Wi-Fi, `nvlddmkm.sys` = NVIDIA, `atikmdag.sys` = AMD, `e1d65x64.sys` = Intel Ethernet.
4. With the name in hand, jump straight to Fix 3's targeted update.

### Fix 2: Boot into Safe Mode with Networking

Gets you a working system while skipping most third-party drivers.

1. Force recovery with the double forced-shutdown method at the Windows logo.
2. **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart** > press **5** (Safe Mode with Networking — you need internet for driver downloads).
3. If stable here, proceed with driver fixes below. If it crashes even in Safe Mode, skip to Fix 6.

### Fix 3: Update or reinstall the suspect driver

Targeted strike on the named driver.

1. In **Device Manager** (**Win + X** > **Device Manager**), locate the device.
2. Right-click > **Uninstall device** — check **Attempt to remove the driver for this device** to wipe the bad version fully.
3. Restart; Windows installs its inbox driver. Test stability.
4. Then install the latest manufacturer driver: your laptop maker's site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) or the Intel Driver & Support Assistant for Intel parts.
5. For Wi-Fi crashes specifically, also update the Bluetooth driver — they often share a package, and the Bluetooth side crashes just as often.
6. After installing, verify in **Device Manager** > device **Properties** > **Driver** that the new version and date are actually in place — failed installs that silently roll back are a real frustration.

### Fix 4: Roll back recent driver updates

When the timeline points at an update, undo it.

1. **Device Manager** > device **Properties** > **Driver** tab > **Roll Back Driver**.
2. Restart, test for a day.
3. Use the show/hide updates troubleshooter to block the bad version.
4. If rollback isn't available (no previous driver stored), uninstall per Fix 3 and install an older version manually from the manufacturer.

### Fix 5: Remove overclocking and reset BIOS to defaults

Eliminates instability masquerading as driver bugs.

1. Enter BIOS/UEFI and load **Optimized Defaults**.
2. Disable **XMP/DOCP** memory profiles and any CPU overclocking.
3. In Windows, reset GPU tuning utilities (Afterburner, AMD Adrenalin, GeForce Experience) to stock.
4. Test under the workload that used to crash (gaming, video calls, large downloads).

### Fix 6: Test RAM and repair system files

Covers the hardware and corruption causes.

1. Run `mdsched.exe` (Extended mode) to test RAM — replace/reseat on errors.
2. Open an **administrator Command Prompt**: run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` (press **Y**, restart, let it finish).
4. Restart and monitor. This combination clears the non-driver causes.

### Fix 7: Temporarily uninstall third-party antivirus

Filter drivers are silent KMODE offenders.

1. Uninstall third-party AV via **Settings** > **Apps** > **Installed apps** (disabling leaves the driver loaded).
2. Confirm **Windows Security** is active and run a full scan.
3. Test for a couple of days. If crashes stop, reinstall the AV fresh — or switch products.
4. If crashes continue, the AV wasn't the cause; reinstall it.

## Closing

KMODE_EXCEPTION_NOT_HANDLED is a kernel driver crash, and the fix is almost always found in the driver layer: identify the faulting file, update or roll it back, and clear out the filter drivers and overclocks that amplify these crashes. The blue screen naming the file is a gift — use it. When it doesn't, the minidump will, and Safe Mode gives you the stable ground to work from. Keep network and graphics drivers current from trusted sources, leave overclocking alone on laptops that already run hot, and this particular blue screen becomes a rare visitor rather than a regular one. If it ever returns, you'll already know the drill: catch the filename first, ask questions later. And keep a restore point from your stable state — rolling back a bad driver in two minutes beats reinstalling it for two hours.
