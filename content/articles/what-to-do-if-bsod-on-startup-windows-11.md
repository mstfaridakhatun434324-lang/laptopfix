---
title: "Blue Screen on Startup in Windows 11: What to Do First"
slug: what-to-do-if-bsod-on-startup-windows-11
date: 2026-10-06
categories: ["windows-errors"]
tags: ["bsod on startup", "windows 11", "boot", "blue screen"]
description: "Blue screen every time Windows 11 starts? Don't panic — work through this ordered guide: Safe Mode, driver rollback, and boot repair."
thumbnail: "/images/thumbs/what-to-do-if-bsod-on-startup-windows-11.webp"
faqs:
  - q: "My laptop blue-screens before I can log in — how do I fix anything?"
    a: "Use the Windows Recovery Environment: interrupt boot three times by holding the power button, and Windows will offer recovery options automatically. From there you can reach Safe Mode, System Restore, the command prompt, and Startup Repair without ever logging into Windows."
  - q: "Is a startup blue screen worse than a random one?"
    a: "It's more disruptive but often easier to diagnose — the cause is something that loads at boot: a driver, a startup service, a recent update, or boot file corruption. That narrows the suspect list considerably compared to random crashes. Use that narrow suspect list to your advantage."
  - q: "Should I try System Restore first?"
    a: "If a restore point exists from before the crashes started, yes — it's the fastest fix for update- or driver-caused startup crashes. It doesn't touch personal files. Check it early, but don't rely on it if the cause is disk corruption or failing hardware."
  - q: "What if Safe Mode also blue-screens?"
    a: "That points below the driver level: corrupted system files, boot configuration damage, disk problems, or hardware failure. Move to the boot repair and hardware checks in the later fixes — Safe Mode crashing rules out third-party drivers as the cause."
---

A blue screen on every startup is uniquely stressful because it locks you out of the normal toolbox — you can't just open Device Manager when Windows won't stay up. But startup crashes are also unusually *diagnosable*: the cause is, by definition, something that loads during boot. That narrows the field to drivers, startup services, recent updates, boot file corruption, or hardware that fails when initialized. The strategy is to peel back the layers — Safe Mode first, then rollback, then repair.

The first decision is how you get into the recovery environment. If Windows shows the "Automatic Repair" screen on its own, you're already there. If it just loops through blue screens, force WinRE: power the laptop on, and the moment the manufacturer's logo appears, hold the power button until it shuts off. Do that three times; on the fourth boot, Windows enters recovery automatically. From there, every fix below is reachable. For the specific case where Automatic Repair itself fails with a log file, see our [SrtTrail.txt repair guide](/articles/how-to-fix-srttrail-txt-blue-screen-error/), and for the related config-corruption crash, [BAD_SYSTEM_CONFIG_INFO fixes](/articles/how-to-fix-bad-system-config-info-reddit/).

## Why this happens

- **A bad driver loading at boot**: Graphics, storage, or network drivers that crash during initialization produce a blue screen before the desktop appears.
- **A recent Windows update**: Cumulative or feature updates can install an incompatible driver or corrupt the boot chain.
- **Corrupted boot configuration (BCD)**: Damage to the boot files stops Windows mid-startup with a crash rather than a clean error.
- **Failing storage**: A drive with bad sectors in the boot or system areas crashes Windows as it tries to read them during startup.
- **New hardware or peripheral**: A newly connected device with a bad driver, or a failing internal component, can crash the boot.
- **Corrupted system files**: Damage to kernel files or the registry hives from a bad shutdown or disk error.
- **Overclocked or misconfigured firmware**: Aggressive BIOS settings (XMP, CPU overclock) that are unstable crash the system as drivers load.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Boot into Safe Mode

Safe Mode loads only essential drivers — if it works, a third-party driver is the cause.

1. From the recovery screen: **Troubleshoot** > **Advanced options** > **Startup Settings** > **Restart**.
2. Press **4** for Safe Mode (or **5** for Safe Mode with Networking if you need downloads).
3. If Safe Mode boots fine, the problem is a non-essential driver or startup program — continue to Fix 2.
4. If Safe Mode also crashes, skip to Fix 4 — the problem is in core Windows, the boot files, or hardware.

### Fix 2: Roll back the suspect driver or remove startup items

In Safe Mode, unwind the most likely changes.

1. Open **Device Manager** (**Win + X**), and check **Display adapters**, **Network adapters**, and **Storage controllers** for devices with warning icons.
2. Right-click any recently updated device > **Properties** > **Driver** tab > **Roll Back Driver**.
3. Open **Task Manager** > **Startup apps** and disable everything non-essential — a crashing startup program can mimic a driver crash.
4. Also check **Settings** > **Apps** > **Installed apps** sorted by date — uninstall anything installed right before the crashes began.
5. Restart normally and test. If it boots, re-enable startup items a few at a time to find the culprit.

### Fix 3: Uninstall the latest Windows update

When the timeline points at Patch Tuesday, reverse it.

1. From WinRE: **Troubleshoot** > **Advanced options** > **Uninstall Updates**.
2. Remove the latest **quality update** first, restart, and test.
3. If crashes persist, remove the latest **feature update** the same way.
4. In Safe Mode or normal Windows afterward, go to **Settings** > **Windows Update** and **Pause updates** for a week so the bad update doesn't reinstall immediately.
5. Check the [Microsoft support page for Windows](https://support.microsoft.com/en-us/windows) for known issues with that update — Microsoft usually acknowledges widespread boot crashes quickly.

### Fix 4: Run System Restore

Roll the system state back to when it worked.

1. From WinRE: **Troubleshoot** > **Advanced options** > **System Restore**.
2. Choose a restore point dated before the startup crashes began.
3. Let it complete — it restores system files, drivers, and registry without touching personal files.
4. If no restore points exist, enable System Protection afterward (**Control Panel** > **System** > **System Protection**) so you have this option next time.
5. Test a normal boot. If restore fails or no points exist, continue.

### Fix 5: Repair the boot files

Fix corruption in the boot chain itself.

1. From WinRE, open **Command Prompt** (**Troubleshoot** > **Advanced options** > **Command Prompt**).
2. Run:

   ```cmd
   bootrec /fixmbr
   bootrec /fixboot
   bootrec /rebuildbcd
   ```

3. If `/fixboot` gives "Access is denied" on a UEFI system, use the `diskpart` + `bcdboot` method detailed in our [SrtTrail.txt guide](/articles/how-to-fix-srttrail-txt-blue-screen-error/).
4. Type `exit`, remove any installation media, and restart.

### Fix 6: Check the drive and disconnect peripherals

Rule out hardware before deeper software surgery.

1. In the WinRE command prompt, run `chkdsk C: /f /r` (use the correct Windows drive letter — verify with `diskpart` > `list vol` if unsure).
2. Disconnect all USB devices, docks, and external monitors — a failing peripheral or its driver can crash the boot. Test with only the power adapter connected.
3. If the laptop has removable RAM, reseat it; if two sticks, test with one at a time.
4. Enter BIOS and load optimized defaults (**F9** on most systems) to rule out unstable overclock or XMP settings.
5. If chkdsk finds many bad sectors, back up the drive via another PC and replace it — a dying drive will keep producing startup crashes.

### Fix 7: Repair system files offline or reset Windows

The last software steps before suspecting the motherboard.

1. In WinRE command prompt:

   ```cmd
   sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows
   ```

   followed by `DISM /Image:C:\ /Cleanup-Image /RestoreHealth` if you have installation media.

2. If that fails, use **Reset this PC** from **Troubleshoot** — choose **Keep my files** first.
3. After any successful boot, install drivers from the manufacturer's support page (Dell, HP, Lenovo) rather than letting old ones restore.
4. If even a reset crashes during setup, that's a hardware verdict — typically storage, RAM, or board — and it's repair-shop time.

## Closing

Startup blue screens feel like a dead machine, but they're usually a boot-time driver or a recent update — both reversible from the recovery environment. The order matters: Safe Mode to confirm it's software, rollback to undo the change, repair to fix the boot chain, hardware checks last. And once you're back up, create a restore point and a recovery USB *before* you need them again — future you will be grateful.
