---
title: "IRQL_NOT_LESS_OR_EQUAL After a Windows 11 Update? Here's How to Fix It"
slug: how-to-fix-irql-not-less-or-equal-after-windows-11-update
date: 2026-10-04
categories: ["windows-errors"]
tags: ["windows 11", "blue screen", "irql", "windows update"]
description: "Hit with IRQL_NOT_LESS_OR_EQUAL right after a Windows 11 update? This guide shows you how to find the bad driver and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-irql-not-less-or-equal-after-windows-11-update.webp"
faqs:
  - q: "What does IRQL_NOT_LESS_OR_EQUAL actually mean?"
    a: "It means a driver or system process tried to access a memory address it had no permission to touch, at an interrupt level that forbids it. Windows stops everything with a blue screen rather than risk corrupting data. The root cause is almost always a buggy, outdated, or incompatible driver — very often one that a Windows update just replaced."
  - q: "Why did this start right after a Windows 11 update?"
    a: "Windows Update frequently ships new driver versions alongside system patches. If the new driver has a bug, or if it conflicts with older software on your laptop — antivirus filters, VPN clients, RGB utilities — the first reboot after the update can start throwing IRQL crashes. Rolling back that specific driver usually ends the crashes immediately."
  - q: "Is IRQL_NOT_LESS_OR_EQUAL a sign my RAM is failing?"
    a: "Sometimes, but drivers are far more likely. Memory faults are worth ruling out with Windows Memory Diagnostic, especially if crashes are random and no single driver shows up in the dump files. If the diagnostic reports hardware errors, the RAM stick itself — or a reseat — is the fix."
  - q: "How do I find which driver caused the crash?"
    a: "Open the minidump files in C:\\Windows\\Minidump with BlueScreenView. It highlights the faulting driver in red on each crash entry. Match that driver name to a device in Device Manager, then update, roll back, or reinstall it. Event Viewer under Windows Logs > System also logs each crash as Event ID 1001."
---

IRQL_NOT_LESS_OR_EQUAL After a Windows 11 Update? Here's How to Fix It

Of all the blue screens Windows 11 can throw at you, IRQL_NOT_LESS_OR_EQUAL is one of the most common — and one of the most fixable. The name is intimidating, but the translation is simple: a driver tried to touch memory it wasn't allowed to touch, and Windows pulled the emergency brake. When it starts happening right after a Windows update, the culprit is almost always a driver that update delivered.

Before you do anything drastic, take a breath: this error rarely means your hardware is dying. It usually means one driver and the new update aren't getting along. Work through the steps below and you will most likely have it sorted within the hour. If you're seeing a different stop code instead, our main [blue screen of death fix guide for Windows 11](/articles/how-to-fix-blue-screen-of-death-windows-11/) covers the general approach.

## Why this happens

- **A new driver arrived with the update.** Windows Update bundles driver updates with system patches, and the fresh driver may contain a bug or a conflict with your specific hardware revision.
- **An old third-party driver clashes with the new kernel.** Antivirus filter drivers, VPN clients, and motherboard utilities hook deep into the system; a kernel change can break their assumptions.
- **The driver was only half-installed.** If the update rebooted mid-install or the download was corrupted, you can end up with mismatched driver files.
- **Overclocking or XMP memory profiles.** Aggressive RAM timings can cause the exact memory-access violations this stop code describes.
- **Failing RAM.** Less common, but a genuinely bad memory module produces IRQL crashes that look identical to driver crashes.
- **Corrupted system files.** If the update damaged kernel components, drivers that were fine before can start faulting.

## How to fix it

Work through these in order, testing your laptop after each change. Start with the driver the update touched — that is the most likely suspect.

### Fix 1: Roll back the driver Windows Update just installed

If the crashes began within a day or two of the update, undoing the driver change is the fastest fix.

1. Open **Device Manager** (**Win + X**, then **Device Manager**).
2. Expand the likely categories — **Display adapters**, **Network adapters**, and **Sound, video and game controllers** are the usual suspects.
3. Right-click each recently updated device, choose **Properties**, and open the **Driver** tab.
4. If **Roll Back Driver** is clickable, click it, pick a reason, and confirm. Repeat for other devices updated on the same day.
5. Check **Settings > Windows Update > Update history > Driver updates** to see exactly which drivers the update delivered.

### Fix 2: Identify the faulting driver from the crash dump

Rather than guessing, let the dump file point at the culprit.

1. On a stable moment (or from Safe Mode), open **File Explorer** and confirm files exist in `C:\Windows\Minidump`.
2. Download and run BlueScreenView — it needs no installation and reads the dumps automatically.
3. Look at the top pane: each crash row shows the stop code `0x0000000A` and, in red, the driver blamed for the crash.
4. Google the driver filename plus your laptop model to identify the device, then move to Fix 3 for that specific device.

### Fix 3: Update the faulty driver from the manufacturer

A roll-back helps when the new driver is broken; a fresh manufacturer driver helps when the old one is incompatible.

1. In **Device Manager**, right-click the faulty device and choose **Update driver > Search automatically for drivers**.
2. If Windows says you already have the best driver, go to the source: laptop makers publish tested drivers on their support pages. Dell owners should check [Dell Support](https://www.dell.com/support), HP owners [HP Support](https://support.hp.com/us-en), and Lenovo owners [Lenovo Support](https://support.lenovo.com/us/en/) — enter your serial number for the exact driver list.
3. Download the driver for your exact model, install it, and reboot.
4. Intel Wi-Fi/Bluetooth users can also use Intel's Driver & Support Assistant tool to catch the latest wireless driver updates.

### Fix 4: Uninstall the problematic Windows update

If a specific KB update clearly lines up with the start of the crashes, removing it is reasonable while you wait for a fixed version.

1. Go to **Settings > Windows Update > Update history**.
2. Scroll down and click **Uninstall updates**.
3. Find the most recent update (note its KB number), select it, and click **Uninstall**.
4. Restart, then pause updates for a week or two: **Settings > Windows Update > Pause updates**.
5. Revisit the update later — Microsoft often re-releases fixed drivers within a few weeks. Related driver-level crashes like [driver power state failure](/articles/driver-power-state-failure-windows-11-fix/) respond to the same rollback technique.

### Fix 5: Run Windows Memory Diagnostic

Rule out bad RAM before you spend hours chasing drivers.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems**.
3. Let the test complete — it takes 10 to 30 minutes depending on your RAM size.
4. After reboot, open **Event Viewer**, go to **Windows Logs > System**, and filter for **MemoryDiagnostics-Results** to read the outcome.
5. If errors are reported, power off, reseat the RAM modules (on laptops with removable panels), and retest. Persistent errors mean the stick needs replacing.

### Fix 6: Disable XMP and reset BIOS to defaults

Overclocked memory is a classic IRQL trigger that a Windows update can expose.

1. Restart and enter BIOS/UEFI (usually **F2**, **Del**, or **F10** during the logo screen — check your maker's splash screen).
2. Find the memory settings and disable **XMP**, **EXPO**, or any memory overclock profile.
3. Choose **Load Optimized Defaults** or **Reset to Default** in the BIOS menus.
4. Save and exit. If the crashes stop, your RAM timings were marginal — leave XMP off or try a milder profile.

### Fix 7: Repair system files with SFC and DISM

Corrupted kernel files can make innocent drivers crash.

1. Open an elevated **Command Prompt** (**Win + S**, type `cmd`, right-click, **Run as administrator**).
2. Run `sfc /scannow` and wait for it to finish.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store SFC draws from.
4. Restart and use the laptop normally for a while to confirm the crashes are gone. Microsoft's own Windows support pages document these repair tools in more depth.

## Closing

IRQL_NOT_LESS_OR_EQUAL looks scary on screen, but it is one of the most routine blue screens a technician sees — and after an update, the fix is usually a single driver rollback away. Identify the driver, roll it back or refresh it from your laptop maker's site, and keep your memory in the clear with a quick diagnostic. Your laptop should be back to crashing only when you forget to save your work.
