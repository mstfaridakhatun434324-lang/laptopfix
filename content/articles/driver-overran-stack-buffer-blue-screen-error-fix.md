---
title: "How to Fix the DRIVER_OVERRAN_STACK_BUFFER Blue Screen on Windows"
slug: driver-overran-stack-buffer-blue-screen-error-fix
date: 2026-10-02
categories: ["windows-errors"]
tags: ["blue screen", "driver error", "bsod fix"]
description: "Seeing DRIVER_OVERRAN_STACK_BUFFER on a blue screen? This guide explains what it means and walks you through proven fixes to stop the crashes."
thumbnail: "/images/thumbs/driver-overran-stack-buffer-blue-screen-error-fix.webp"
faqs:
  - q: "What does DRIVER_OVERRAN_STACK_BUFFER actually mean?"
    a: "It means a driver wrote data beyond the end of its memory buffer — a classic buffer-overflow bug. Windows detects the overflow and deliberately crashes with a blue screen to stop the rogue driver from corrupting anything else. The stop code is 0x000000F7."
  - q: "Can a virus cause DRIVER_OVERRAN_STACK_BUFFER?"
    a: "Rarely. This stop code is almost always a buggy or mismatched driver, failing RAM, or a conflicting third-party utility. Still, if the crashes started after downloading something shady, run a full scan with Windows Security before anything else — malware can install malicious drivers."
  - q: "Should I use a driver updater tool to fix it?"
    a: "No. Third-party driver updaters are a common cause of this exact crash because they install wrong or mismatched drivers. Always get drivers from Windows Update or directly from the hardware manufacturer's own support site."
  - q: "How do I know which driver caused the crash?"
    a: "Check the blue screen itself for a .sys file name, then confirm it in Event Viewer under Windows Logs > System by finding the BugCheck entry. You can also analyze the memory dump with WinDbg — our [dump file analysis guide](/articles/best-way-to-read-dump-files-with-windbg/) walks through that process."
---

Nothing kills your flow like a blue screen in the middle of work, and DRIVER_OVERRAN_STACK_BUFFER is one of the scarier-looking ones. The good news: despite the intimidating name, this stop code almost always traces back to a misbehaving driver — and drivers can be fixed.

The name tells you exactly what happened. A driver wrote more data than the memory 'buffer' it was given — it overran the stack — and Windows shut everything down to protect itself. If you want a deeper dive into this specific error, see our [companion guide](/articles/best-way-to-fix-driver-overran-stack-buffer/). Let's walk through the fixes that actually work, starting with the easiest.

## Why this happens

- A buggy or outdated device driver — most often the network adapter, graphics card, or audio driver — writing past its allocated memory.

- A recent driver update that introduced a regression; the crashes started right after Windows Update or a manual driver install.

- Overclocking utilities or aggressive 'game booster' software pushing hardware past stable limits.

- Corrupted system files that a driver depends on, so even a good driver crashes when it loads.

- Failing RAM that corrupts data as the driver uses it, making a software problem look like a driver problem.

- Two drivers fighting over the same device, common after upgrading hardware without removing the old driver first.

## How to fix it

Work through these in order, starting with Fix 1. Most of these crashes are resolved by one of the first three fixes, so don't skip ahead.

### Fix 1: Note the driver name on the blue screen

The blue screen often names the exact file that caused the crash, like nvlddmkm.sys or Netwtw10.sys. That name tells you which driver to target, saving you from updating everything blindly.

1. Next time the blue screen appears, look for a line under the stop code that ends in **.sys** — photograph it with your phone if it vanishes too fast.

2. After rebooting, open **Event Viewer**, go to **Windows Logs > System**, and look for **BugCheck** entries around the crash time for the same file name.

3. Search that file name on [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) to identify which device it belongs to.

4. Write the driver name down; you'll use it in the fixes below.

### Fix 2: Roll back the suspect driver

If the crashes began after a driver or Windows update, rolling back to the previous version is the fastest fix. Windows keeps the old driver around for exactly this situation.

1. Press **Win + X** and open **Device Manager**.

2. Expand the category for the suspect device (for example **Display adapters** or **Network adapters**).

3. Right-click the device, choose **Properties**, and open the **Driver** tab.

4. Click **Roll Back Driver**, pick a reason, and confirm. Restart your laptop.

5. If the button is greyed out, no previous driver is stored — move on to the next fix.

### Fix 3: Install a fresh driver from the manufacturer

Windows Update drivers are generic by design. The driver from your laptop or component maker is newer, better tested, and far less likely to overrun a buffer.

1. In **Device Manager**, right-click the suspect device and choose **Uninstall device**, ticking **Attempt to remove the driver for this device** if offered.

2. Restart the laptop so Windows loads a basic fallback driver.

3. Download the latest driver from the manufacturer's site — for Intel hardware use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).

4. Install it, restart again, and use the laptop normally for a day to confirm the crashes are gone.

### Fix 4: Run a memory diagnostic

Bad RAM can corrupt driver data and trigger this exact stop code. Since RAM problems mimic driver problems, it's worth ruling out before you go deeper.

1. Press **Win + R**, type `mdsched.exe`, and press **Enter**.

2. Choose **Restart now and check for problems**.

3. Let the Windows Memory Diagnostic finish — don't interrupt it.

4. After the reboot, check the results in **Event Viewer > Windows Logs > System** by filtering for **MemoryDiagnostics-Results**.

5. If errors are found, the RAM stick itself needs replacing; no driver fix will help.

### Fix 5: Scan and repair system files

Corrupted Windows files can destabilize drivers. The built-in SFC and DISM tools repair them without touching your personal files.

1. Open **Terminal (Admin)** or **Command Prompt (Admin)** from the **Win + X** menu.

2. Run `sfc /scannow` and wait for it to complete.

3. Then run `DISM /Online /Cleanup-Image /RestoreHealth` and wait — this can take 15-30 minutes.

4. Restart the laptop and see whether the blue screens stop.

### Fix 6: Do a clean boot to find conflicting software

Third-party utilities — especially antivirus, VPN clients, and RGB or fan-control apps — install their own drivers. A clean boot tells you whether one of them is the culprit.

1. Press **Win + R**, type `msconfig`, and open the **Services** tab.

2. Tick **Hide all Microsoft services**, then click **Disable all**.

3. Open **Task Manager > Startup apps** and disable everything non-essential.

4. Restart. If the crashes stop, re-enable items in small groups until the crashes return — the last group contains the offender.

5. For the full procedure, follow our [clean boot walkthrough](/articles/best-way-to-perform-clean-boot-windows-11/).

### Fix 7: Update the BIOS and chipset drivers

Old firmware can mishandle how drivers talk to hardware. Laptop makers release BIOS and chipset updates specifically to fix these low-level incompatibilities.

1. Find your exact model on the manufacturer's support site.

2. Download the latest **BIOS** and **chipset** updates for your model only — never a BIOS for a different model.

3. Install the chipset driver first, restart, then apply the BIOS update with the laptop plugged in.

4. Do not interrupt a BIOS update. When it finishes, load the laptop normally and monitor for crashes.

### Fix 8: Catch the driver with Driver Verifier

When the dump doesn't name a driver, Driver Verifier can force the guilty one to crash identifiably. Used narrowly — on a few suspects rather than everything — it's a safe, decisive diagnostic.

1. Press **Win + R**, type `verifier`, and press **Enter**.

2. Choose **Create standard settings**, then **Select driver names from a list**.

3. Tick only your prime suspects — the network, graphics, and audio drivers — not every driver on the system.

4. Restart and use the laptop normally until it blue-screens; Verifier will name the violator.

5. Boot into Safe Mode, run `verifier /reset` from an admin prompt, and restart.

6. Replace the named driver with the manufacturer's version as described in Fix 3.

## Closing

DRIVER_OVERRAN_STACK_BUFFER looks dramatic, but nine times out of ten it's one bad driver and the fix is a rollback or a clean reinstall of that driver. Work the list in order, and if you reach the memory test with errors, treat it as a hardware problem rather than a software one — replacing the faulty RAM stick ends the crashes for good. If a different stop code shows up next, our [KMODE_EXCEPTION_NOT_HANDLED guide](/articles/best-way-to-fix-kmode-exception-not-handled/) covers the next most common driver crash. One last habit worth building: after any driver update, give the laptop a day of normal use before calling it stable. Buffer-overrun bugs often need specific conditions to trigger, and catching them early — while you still remember what changed — makes the rollback trivial.
