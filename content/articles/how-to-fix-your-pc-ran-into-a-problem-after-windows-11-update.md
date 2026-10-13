---
title: "\"Your PC Ran Into a Problem\" After a Windows 11 Update — How to Fix It"
slug: how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update
date: 2026-09-28
categories: ["windows-errors"]
tags: ["your pc ran into a problem", "blue screen", "windows 11 update"]
description: "Fix the \"Your PC ran into a problem\" blue screen after a Windows 11 update: read the stop code, roll back the update, and stabilize your laptop."
thumbnail: "/images/thumbs/how-to-fix-your-pc-ran-into-a-problem-after-windows-11-update.webp"
faqs:
  - q: "What does \"Your PC ran into a problem\" actually mean?"
    a: "It is the friendly face of a blue screen — Windows hit a critical error it could not recover from and stopped to protect your data. The small stop code at the bottom (like MEMORY_MANAGEMENT) is the real diagnosis; the headline text is the same for every crash."
  - q: "Will I lose my files because of this error?"
    a: "The crash itself does not delete files. Your documents are safe on the disk. Only use Reset options that promise to keep files, and avoid clean installs until you have a backup — the fixes in this guide do not touch your data."
  - q: "It happens every time I start Windows. What do I do?"
    a: "Boot into the recovery environment (interrupt boot three times), then use System Restore to roll back to before the update, or uninstall the latest update from Troubleshoot → Advanced options. Both options keep your files."
  - q: "How do I find the stop code if the screen disappears too fast?"
    a: "Disable automatic restart (sysdm.cpl → Advanced → Startup and Recovery → uncheck Automatically restart) so the screen stays up. After rebooting, Event Viewer → Windows Logs → System → BugCheck entries always have the code too."
---

"Your PC ran into a problem and needs to restart" is Windows 11's polite way of showing you a blue screen. The sad-face screen is generic — the useful part is the small stop code printed near the bottom. When this starts happening right after a Windows 11 update, the update disturbed something: a driver, a system file, or a setting.

The fix is a process, not a single button: capture the stop code, undo the update's damage, and stabilize the drivers. Here is the whole thing in order.

## Why this happens

- **A driver the update replaced:** Windows Update bundles driver updates that can be buggy or mismatched to your hardware.
- **Corrupted system files:** An interrupted update leaves half-written system files that crash on load.
- **Incompatible software:** Old antivirus, VPN, or disk utilities with kernel drivers break against the new Windows build.
- **Insufficient disk space during install:** Updates that squeeze onto a nearly-full drive can install incompletely and unstably.
- **BIOS/firmware mismatch:** New Windows builds sometimes need newer firmware; old BIOS versions cause crashes under the new kernel.
- **Pre-existing disk or RAM faults:** The update's heavy disk and memory activity can push marginal hardware over the edge.

- **Debugging tools left behind:** If the machine was ever debugged (by you or a shop), leftover Driver Verifier settings can crash on new drivers — `verifier /query` reveals this in seconds.
## How to fix it

Work through these in order — capture the code first, then undo and repair.

### Fix 1: Capture the stop code

1. If the screen vanishes too fast, disable [automatic restart](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/): **Win + R → `sysdm.cpl` → Advanced → Startup and Recovery → Settings** → uncheck **Automatically restart**.
2. On the next crash, photograph the screen and write down the **stop code** and any **.sys filename**.
3. After rebooting, open **Event Viewer → Windows Logs → System** and find **BugCheck** events for the hex code and details.
4. The stop code tells you which of our specific guides to follow next — common ones include [MEMORY_MANAGEMENT](/articles/how-to-fix-stop-code-memory-management-after-windows-11-update/) and [page fault errors](/articles/how-to-fix-page-fault-in-nonpaged-area-after-windows-11-update/).

### Fix 2: Boot into Safe Mode to stabilize

1. From the login screen, hold **Shift** and click **Restart**. (If you cannot reach it, interrupt boot three times to force WinRE.)
2. Go to **Troubleshoot → Advanced options → Startup Settings → Restart**, press **4** for Safe Mode.
3. If the laptop is stable in Safe Mode, the problem is a third-party driver or startup program — not Windows itself.
4. Use Safe Mode as your base for the driver work in the next steps.

### Fix 3: Uninstall the problematic update

1. In normal or Safe Mode, open **Settings → Windows Update → Update history → Uninstall updates**.
2. Remove the most recent update (check the install date against when crashes began).
3. Restart normally and test for a day.
4. If stability returns, pause updates for 2–3 weeks (**Settings → Windows Update → Pause updates**) so the same update is not immediately reinstalled. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the pause and uninstall options.

### Fix 4: Roll back or update drivers

1. Open **Device Manager** and check **Display adapters**, **Network adapters**, and **Storage controllers** for warning icons.
2. For anything updated recently, use **Properties → Driver → Roll Back Driver**.
3. Then install fresh drivers from your laptop maker's support page — Dell, HP, Lenovo, ASUS, or Acer — rather than trusting Windows Update's versions.
4. Update the GPU from NVIDIA, AMD, or [Intel](https://www.intel.com/content/www/us/en/support/detect.html) directly, using clean-install options where offered.

### Fix 5: Run SFC, DISM, and chkdsk

1. Open **Terminal (Admin)** and run `sfc /scannow`.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow` again.
3. Run `chkdsk C: /f` (schedule at restart with **Y** if prompted).
4. These three repair corrupted system files and disk errors — the two most common non-driver causes of post-update crashes.

### Fix 6: Use System Restore to go back in time

1. Press **Win + R**, type `rstrui`, and press Enter.
2. Choose a restore point dated **before** the update that started the crashes.
3. Let it complete — your files are untouched; only system files, drivers, and registry settings roll back.
4. If no restore point exists, enable System Protection afterwards (**sysdm.cpl → System Protection → Configure → Turn on system protection**) so you have one next time.

### Fix 7: Repair-install Windows as the final software fix

1. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount it, run `setup.exe`, and choose **Keep personal files and apps**.
3. The repair install (30–60 minutes) replaces all Windows system files while preserving everything else.
4. If crashes continue after a repair install with updated drivers, suspect hardware — run `mdsched.exe` (memory test) and check drive health next.

### Fix 8: Enable System Protection so the next bad update is trivial

The best fix for the next bad update is a time machine. System Protection gives you one — set it up now while the system is healthy.

1. Press **Win + R**, type `sysdm.cpl`, and open the **System Protection** tab.
2. Select your system drive, click **Configure**, choose **Turn on system protection**, and set max usage to 5–10%.
3. Click **Create** and name the restore point something like "healthy baseline".
4. After every major Windows update that goes well, create another manual restore point — it takes thirty seconds.
5. Next time an update misbehaves, `rstrui` and a five-minute rollback replace an entire troubleshooting session.

## Closing

"Your PC ran into a problem" is a symptom, not a diagnosis — the stop code underneath is what actually matters, so capture it first and everything else follows. Roll back the offending update, refresh your drivers from the manufacturer's site, repair system files with SFC and DISM, and enable System Protection so the next bad update is a five-minute rollback instead of another deep dive. That sequence resolves the overwhelming majority of post-update crash loops without touching a single one of your files.
