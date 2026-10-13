---
title: "System Thread Exception Not Handled on Your HP Laptop: Fixed"
slug: how-to-fix-system-thread-exception-not-handled-on-hp-laptop
date: 2026-10-10
categories: ["windows-errors"]
tags: ["bsod", "stop code", "drivers", "hp laptop"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED on your HP laptop? It's a driver crash — here's how to find the bad driver and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-system-thread-exception-not-handled-on-hp-laptop.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "A system thread — code running inside a driver or Windows itself — threw an exception that nothing caught, so Windows crashed to protect itself. On HP laptops this is almost always a buggy or incompatible driver, frequently graphics, network, or storage."
  - q: "The blue screen names a file like atikmdag.sys. What do I do?"
    a: "That filename is the crashed driver, which makes your job easy. Search the filename to identify the device (atikmdag.sys is AMD graphics, nvlddmkm.sys is NVIDIA, netwtw10.sys is Intel Wi-Fi), then update, roll back, or reinstall that specific driver."
  - q: "Is this error caused by a virus?"
    a: "Extremely unlikely. This stop code is a driver or system-level crash, not malware behavior. Don't buy 'PC repair' software that claims otherwise — the fixes here are free and built into Windows."
  - q: "Will fixing this delete my files?"
    a: "No. Driver updates, rollbacks, Safe Mode repairs, and DISM/SFC scans don't touch personal files. Your documents and apps stay exactly where they are through every fix in this guide."
---

`SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` is Windows telling you that a driver crashed so badly nothing could catch it. On HP laptops the usual story is a graphics, Wi-Fi, or storage driver that went bad — often after a Windows update replaced it, or after HP Support Assistant pushed a driver that doesn't agree with your current Windows build. Sometimes the blue screen even names the culprit file, which turns detective work into a straight line.

Here's the fix order, from reading the clue to verifying the cure.

One thing that helps to know up front: this stop code is almost never random. The same driver crashes the same way under the same conditions, which means your crashes probably have a pattern — during gaming, when connecting to Wi-Fi, on wake from sleep, or right after login. Noticing the pattern before you start tells you which driver to suspect even before you read the dump, and it gives you a concrete test ("play for an hour," "sleep and wake three times") to verify each fix actually worked.

## Why this happens

- **Incompatible or buggy driver**: The top cause. A driver throws an unhandled exception when it hits a condition its code doesn't expect — common with graphics drivers after Windows updates and with old network drivers on new builds.
- **Windows Update replaced a working driver**: HP laptops are prone to this because Windows Update pushes generic drivers over HP-validated ones. The generic version can crash where the HP version worked.
- **Corrupted driver files**: Interrupted updates, disk errors, or failed installations leave driver binaries in a half-written state that crashes on load.
- **Conflicting HP utilities**: HP Support Assistant, HP System Event Utility, and Wolf Security components install drivers and services. Version mismatches after updates can destabilize the driver stack.
- **Overheating causing driver timeouts**: A GPU driver waiting on overheated hardware can throw exceptions. Dust-clogged HP cooling is a real contributor on older machines.
- **Failing hardware beneath the driver**: A dying SSD, bad RAM, or a failing GPU produces errors the driver can't handle, and the unhandled exception is how it surfaces.

## How to fix it

Work through these in order.

### Fix 1: Note the driver filename on the blue screen

If the crash names a file, your job gets much easier.

1. The next time it blue-screens, look for text like "What failed: **nvlddmkm.sys**" near the stop code.
2. Write it down or photograph it. Common ones: `nvlddmkm.sys` (NVIDIA graphics), `atikmdag.sys` (AMD graphics), `igdkmd64.sys` (Intel graphics), `netwtw10.sys` / `Netwtw12.sys` (Intel Wi-Fi), `rt640x64.sys` (Realtek network).
3. If no filename appears, check `C:\Windows\Minidump` for the latest dump and analyze it per [how to check minidump files on Windows 11](/articles/how-to-check-minidump-files-on-windows-11/).
4. Knowing the driver lets you target Fix 2 precisely instead of updating everything.

### Fix 2: Update the culprit driver via HP Support Assistant

HP's own driver packages are validated for your model — prefer them.

1. Open **HP Support Assistant** (get it from the [HP support site](https://support.hp.com/us-en) if missing).
2. Run a check for updates and install all driver updates, especially the one matching your culprit (graphics, network, chipset).
3. Restart and use the laptop normally for a day.
4. If HP offers no update for that driver, get it from the chip vendor: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or [Intel](https://www.intel.com/content/www/us/en/support/detect.html).

### Fix 3: Roll back the driver

If the crashes started right after a driver update, undo it.

1. Boot into Safe Mode if normal boot crashes: **Shift + Restart** from the sign-in screen, then **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**, press **4**.
2. Open **Device Manager** (**Win + X**), find the device, right-click > **Properties** > **Driver** tab.
3. Click **Roll Back Driver**, choose a reason, and restart.
4. If the button is grayed out, download the previous driver version from HP or the vendor and install it manually.

### Fix 4: Clean-reinstall the graphics driver

Graphics drivers cause the majority of these crashes, and they deserve a true clean install.

1. In Safe Mode, open **Device Manager**, expand **Display adapters**, right-click your GPU, and choose **Uninstall device**, checking **Attempt to remove the driver for this device**.
2. Restart — Windows will use the basic display adapter.
3. Install the fresh driver from HP Support Assistant or the GPU vendor, choosing the clean-install option during setup.
4. Avoid installing the vendor's extra "experience" utilities if you don't need them — fewer components, fewer crash surfaces.

### Fix 5: Remove conflicting third-party software

Filter drivers and "optimizers" are frequent unhandled-exception sources.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall third-party antivirus, VPN clients, system optimizers, and RGB/peripheral utilities you don't need.
3. Use vendor removal tools where available — leftover kernel drivers survive standard uninstalls.
4. Restart and test.

### Fix 6: Repair system files

Corrupted OS files can make good drivers throw exceptions.

1. Open an elevated **Command Prompt** (**Win + S** > type `cmd` > right-click > **Run as administrator**).
2. Run:

   ```cmd
   DISM /Online /Cleanup-Image /RestoreHealth
   ```

3. Then:

   ```cmd
   sfc /scannow
   ```

4. Restart when both complete.

### Fix 7: Check thermals and hardware health

Rule out heat and failing components.

1. Monitor temperatures with HWMonitor during normal use — sustained 90°C+ on CPU/GPU is a problem.
2. Clean vents with compressed air (laptop off).
3. Run Windows Memory Diagnostic: **Win + R** > `mdsched.exe` > **Restart now and check for problems**.
4. Run HP's built-in hardware diagnostics: restart and press **Esc**, then **F2** for **System Diagnostics**, and run the full component tests.

### Fix 8: Block the bad driver from coming back

Windows Update loves to reinstall the exact driver version you just removed.

1. After a successful rollback or clean install, open **Settings** > **Windows Update** > **Advanced options** > **Optional updates** and uncheck any driver update for the fixed device.
2. If Windows keeps pushing it, use Microsoft's "Show or hide updates" troubleshooter to hide that specific driver update.
3. Revisit in a month or two — vendors do fix bad drivers, and a newer version may be safe to take later.

## Closing

On HP laptops, `SYSTEM_THREAD_EXCEPTION_NOT_HANDLED` is a driver story in the vast majority of cases — read the filename on the blue screen, update or roll back that driver through HP Support Assistant, and the crashes stop. If you'd rather work through the generic version of this error, see the [step-by-step system thread exception fix](/articles/how-to-fix-system-thread-exception-not-handled-step-by-step/), or check [how to fix unexpected kernel mode trap](/articles/how-to-fix-unexpected-kernel-mode-trap-step-by-step/) for a closely related stop code.
