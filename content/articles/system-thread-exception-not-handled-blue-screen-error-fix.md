---
title: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Fixing This Blue Screen Error"
slug: system-thread-exception-not-handled-blue-screen-error-fix
date: 2026-10-07
categories: ["windows-errors"]
tags: ["windows 11", "blue screen", "drivers", "system thread"]
description: "SYSTEM_THREAD_EXCEPTION_NOT_HANDLED keeps crashing your laptop? Learn how to read the dump, find the bad driver, and stop the blue screens."
thumbnail: "/images/thumbs/system-thread-exception-not-handled-blue-screen-error-fix.webp"
faqs:
  - q: "What does SYSTEM_THREAD_EXCEPTION_NOT_HANDLED mean?"
    a: "It means a system thread — a background task run by Windows or a driver — hit an error it didn't know how to handle, so Windows crashed to protect itself. The stop code is 0x1000007E. In practice, the cause is almost always a faulty or incompatible driver, and the crash dump usually names the exact file."
  - q: "Why does the blue screen sometimes show a file name like nvlddmkm.sys?"
    a: "When Windows can identify the driver that was running when the thread crashed, it prints the filename on the blue screen itself. That is a gift — it tells you exactly which driver to update, roll back, or reinstall. nvlddmkm.sys is NVIDIA graphics, igdkmd64.sys is Intel graphics, and rtwlane.sys is Realtek Wi-Fi."
  - q: "Can this error be caused by hardware?"
    a: "Yes, though drivers are more common. Overheating GPUs, failing RAM, and dying hard drives can all produce this stop code. If you've updated every driver and the crashes continue, run a memory diagnostic and check your drive health with CrystalDiskInfo or the manufacturer's tool."
  - q: "Should I update my BIOS to fix this error?"
    a: "Only if your laptop maker's support page lists a BIOS update that mentions stability, crashes, or compatibility with your Windows version. BIOS updates carry a small risk if power is lost mid-flash, so don't update speculatively — rule out drivers first, then consider BIOS as a later step."
---

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: Fixing This Blue Screen Error

There's something uniquely annoying about SYSTEM_THREAD_EXCEPTION_NOT_HANDLED: the name tells you almost nothing, yet the fix is usually straightforward. Translated from engineer-speak, it means a background system task crashed in a way nothing expected — and nine times out of ten, a driver is the reason. The best part? Windows often prints the guilty driver's filename right on the blue screen, handing you the answer.

This guide shows you how to read that clue, track down the driver, and fix it properly — plus what to do when the dump doesn't name anyone. If you're dealing with a different stop code, our main [Windows 11 blue screen fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the general approach.

## Why this happens

- **A driver threw an unhandled exception.** Graphics, Wi-Fi, and audio drivers run system threads constantly; a bug in any of them produces exactly this crash.
- **The driver is incompatible with your Windows build.** Major Windows 11 updates change kernel internals that older drivers weren't written for.
- **Two drivers are fighting.** Antivirus filter drivers and VPN clients that hook the network stack can collide with the Wi-Fi driver's threads.
- **The driver file itself is corrupted.** A bad download or interrupted update can leave a driver half-installed but still loading.
- **Overheating triggers thread failures.** A GPU that overheats can fault mid-operation in ways Windows reports as a thread exception.
- **Failing RAM or storage.** Hardware faults corrupt the data threads work on, producing crashes that mimic driver bugs.

## How to fix it

Work through these in order. The dump file is your best friend here — let it name the suspect before you start changing things.

### Fix 1: Note the filename on the blue screen

Windows often does the detective work for you.

1. The next time the blue screen appears, look below the stop code for text like **"What failed: nvlddmkm.sys"**.
2. Photograph the screen with your phone — you'll want the exact filename.
3. Common translations: `nvlddmkm.sys` = NVIDIA graphics, `igdkmd64.sys` or `igdkmdn64.sys` = Intel graphics, `rtwlanu.sys` / `rtwlane.sys` = Realtek Wi-Fi, `atikmdag.sys` = AMD graphics.
4. Skip straight to Fix 3 with that driver in mind. If no filename is shown, continue with Fix 2.

### Fix 2: Read the minidump with BlueScreenView

When the blue screen doesn't name the driver, the dump file will.

1. Get to a stable state — Safe Mode if necessary — and open `C:\Windows\Minidump` in File Explorer to confirm dumps exist.
2. Run BlueScreenView (portable, no install needed) and look for crashes with stop code `0x1000007E`.
3. The driver highlighted in red in the lower pane is the one that was executing when the thread died.
4. Note its name and move on — you'll now update or replace exactly that driver instead of guessing.

### Fix 3: Update the identified driver from the manufacturer

Generic Windows drivers are fine until they aren't; the maker's tested version is the real fix.

1. Open **Device Manager** (**Win + X > Device Manager**), find the device matching your suspect driver, right-click it, and choose **Update driver > Search automatically for drivers**.
2. If Windows finds nothing new, go to your laptop maker's support site with your exact model number: [Dell Support](https://www.dell.com/support), [HP Support](https://support.hp.com/us-en), or [Lenovo Support](https://support.lenovo.com/us/en/).
3. Download the driver for the suspect device, install it, and reboot.
4. For NVIDIA graphics specifically, a clean install from NVIDIA's official driver download page with the "Perform a clean installation" checkbox resolves most `nvlddmkm.sys` crashes.

### Fix 4: Roll back a recently updated driver

If the crashes started right after a driver update, the new version is the problem.

1. In **Device Manager**, right-click the suspect device and open **Properties**.
2. On the **Driver** tab, click **Roll Back Driver**, choose a reason, and confirm.
3. Reboot and use the laptop for a day. If crashes stop, block that driver from auto-updating: in **Settings > Windows Update > Advanced options**, turn off **Receive updates for other Microsoft products** won't cover drivers — instead use the "Show or hide updates" troubleshooter from Microsoft to hide the bad driver version.
4. Revisit the newer driver in a month or two; vendors usually fix crash bugs quickly.

### Fix 5: Do a clean reinstall of the graphics driver

Graphics drivers are the number one cause of this stop code, and a truly clean reinstall beats an update.

1. Download Display Driver Uninstaller (DDU) and the latest driver for your GPU on another device if yours is unstable.
2. Boot into Safe Mode (see [how to boot Windows 11 in Safe Mode](/articles/how-to-boot-windows-11-in-safe-mode/)).
3. Run DDU, select your GPU brand, and choose **Clean and restart**.
4. After reboot, install the fresh driver you downloaded. Don't let Windows Update install its own copy first — install yours immediately.

### Fix 6: Check temperatures and test your RAM

Rule out the hardware causes before going deeper.

1. Install HWMonitor or check your BIOS hardware monitor for CPU/GPU temperatures under load. Sustained readings above 90°C point to dust-clogged fans or dried thermal paste.
2. Run Windows Memory Diagnostic: press **Win + R**, type `mdsched.exe`, choose **Restart now and check for problems**.
3. After reboot, check **Event Viewer > Windows Logs > System** for the MemoryDiagnostics-Results entry.
4. If the drive is suspect, check its SMART health — the storage angle is covered in our guide to the related [UNEXPECTED_STORE_EXCEPTION error](/articles/unexpected-store-exception-windows-11-fix/).

### Fix 7: Repair system files and consider a BIOS update

The last-resort software fixes before suspecting deeper hardware trouble.

1. Open an elevated **Command Prompt** and run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Check your laptop maker's support page for a BIOS update that mentions stability or Windows 11 compatibility — install it only on AC power with the battery charged.
3. If crashes persist after all of this, test with a spare RAM stick or have the storage drive checked — at this point hardware is the likeliest explanation. Microsoft's Windows support site documents additional advanced recovery options.

## Closing

SYSTEM_THREAD_EXCEPTION_NOT_HANDLED is Windows telling you, in its own awkward way, exactly where to look: at a driver thread that fell over. Read the filename, refresh that driver from the source, and the crashes almost always stop. And if the dump ever names a different driver next time — well, now you know the drill.
