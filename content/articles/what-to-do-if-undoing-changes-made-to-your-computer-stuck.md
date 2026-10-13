---
title: "What to Do If 'Undoing Changes Made to Your Computer' Is Stuck"
slug: what-to-do-if-undoing-changes-made-to-your-computer-stuck
date: 2026-09-17
categories: ["windows-update"]
tags: ["undoing changes", "update stuck", "windows recovery", "windows 11"]
description: "'Undoing changes made to your computer' spinning for hours? Here's how long to wait, how to recover safely, and how to stop it happening again."
thumbnail: "/images/thumbs/what-to-do-if-undoing-changes-made-to-your-computer-stuck.webp"
faqs:
  - q: "How long does 'undoing changes' normally take?"
    a: "On a healthy machine with an SSD, anywhere from 15 to 60 minutes. Slower laptops with spinning hard drives or large updates can take up to two hours. If the screen has not changed, the disk light shows no activity, and more than three hours have passed, you are dealing with a genuine hang rather than a slow rollback."
  - q: "Is it safe to force restart during undoing changes?"
    a: "It carries some risk, but one controlled restart is the standard recovery step when the rollback is truly hung. Windows is designed to resume or restart the rollback on the next boot. The danger comes from repeated power cuts during the same rollback, which is what actually corrupts the boot files — so restart once, then be patient."
  - q: "Why does the rollback get stuck in the first place?"
    a: "Usually because the same problem that failed the update is blocking the rollback: corrupted system files, a failing hard drive, too little disk space, or a driver that crashes during the restore phase. The rollback replays the installation in reverse, so anything that broke the forward install can break the backward one too."
  - q: "Will I lose my files if the rollback hangs?"
    a: "Almost certainly not. The rollback restores system files and settings, not your documents, photos, or installed programs. Your personal files sit untouched in their folders throughout the process. Still, if the machine ends up needing a reset, having a current backup — as explained in our driver backup guide — is the one thing that removes all anxiety."
---

Few Windows moments are as nerve-wracking as watching "Undoing changes made to your computer" spin for an hour with nothing to show for it. The update failed, Windows promised to put everything back the way it was, and now the rollback itself seems to have given up. The instinct is to hold the power button — but the fear is that interrupting it will brick the laptop. Both feelings are valid. Here is the measured, technician-tested way through it.

First, the reassuring facts: the undoing-changes screen means Windows is actively restoring your previous system state from a backup it made before the update started. Your personal files are not being touched. And in most cases the screen is not actually stuck — it is just slow. Rollbacks on laptops with mechanical hard drives, nearly-full disks, or large feature updates routinely take 60 to 90 minutes while showing zero visible progress. The first rule is patience; the second rule, if patience runs out, is a single controlled restart rather than repeated power cuts.

## Why this happens

- **The rollback is genuinely slow.** Large updates on slow storage can take over an hour of apparent stillness while files are restored in the background.
- **Corrupted system files block the restore.** The same damage that failed the update can crash the rollback when it tries to restore those files.
- **A failing hard drive.** Bad sectors in the area holding the rollback backup make the restore crawl or hang indefinitely.
- **Too little disk space.** The rollback needs working room; a nearly full C: drive stalls both updates and their reversals.
- **A misbehaving driver.** Drivers load during the rollback's reboots — a crashing display or storage driver can freeze the process mid-restore.
- **Interrupted power.** A drained battery or unplugged charger during the original update can leave the rollback backup itself incomplete.
- **Stuck pending operations.** Leftover pending file renames from the failed install can deadlock the rollback engine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether it is actually stuck

Do not restart until you are sure the rollback has genuinely hung. Most "stuck" rollbacks are just slow.

1. Note the time. If less than 90 minutes have passed (120 for mechanical hard drives), keep waiting — really.
2. Check for disk activity: look at the storage LED, or listen closely for drive sounds. Any blinking or chatter means the rollback is working.
3. Try **Ctrl + Alt + Delete** once. If the screen responds or flickers, Windows is alive under the rollback UI.
4. Only if there is zero disk activity for a full hour and the screen ignores input should you conclude it is hung — then move to Fix 2.

### Fix 2: Perform one controlled restart

A single power-cycle gives Windows a chance to resume or restart the rollback cleanly. The key word is *single* — repeated restarts are what cause real damage.

1. Hold the power button for 10 seconds until the laptop fully shuts off. Disconnect the charger, wait 30 seconds, reconnect it, and power on.
2. Windows will usually return to the undoing-changes screen and either continue the rollback or detect the failed update and skip straight to the login screen.
3. If it boots to the desktop, the crisis is over. Go to **Settings > Windows Update > Update history** to confirm which update failed, then move to Fix 5 to prevent a repeat.
4. If it lands back on the spinning screen, wait another 90 minutes before doing anything else. One restart, then patience.

### Fix 3: Boot into Safe Mode to break the deadlock

If the rollback loops back to the same screen after restarting, Safe Mode loads a minimal driver set that often lets the restore finish.

1. Force the recovery environment: power off during the Windows logo three times in a row (hold power 10 seconds each time). On the fourth boot, Windows should show **Automatic Repair**.
2. Choose **Advanced options > Troubleshoot > Advanced options > Startup Settings**, then **Restart**, and press **4** for Safe Mode.
3. In Safe Mode, open **Settings > Windows Update** and check for the failed update — it may now install cleanly without the problematic driver loaded.
4. Alternatively, open **Control Panel > Programs > View installed updates**, find the failed update, and uninstall it explicitly. For a step-by-step on this screen, see our guide to fixing the [undoing changes loop](/articles/best-way-to-fix-windows-update-says-undoing-changes-made-to-your-computer/).

### Fix 4: Run Startup Repair and system file checks from recovery

When the rollback has damaged the boot files themselves, the recovery environment's own tools can repair them.

1. Get back to the recovery environment (**Advanced options**) using the three-interrupted-boots method from Fix 3.
2. Choose **Troubleshoot > Advanced options > Startup Repair** and let it run — it fixes boot configuration problems automatically.
3. If Startup Repair does not resolve it, go back to **Advanced options > Command Prompt** and run `sfc /scannow /offbootdir=C:\ /offwindir=C:\Windows` (replace C: if your Windows drive has a different letter in recovery).
4. Also run `chkdsk C: /f /r` to scan for bad sectors — a failing drive is a common root cause, and you want to know about it now rather than during the next update.

### Fix 5: Free up disk space and stabilize the system

Before retrying any update, remove the conditions that caused the failure — a cramped disk is the easiest to fix and the most commonly overlooked.

1. Open **Settings > System > Storage** and free the drive to at least 20 GB: run Disk Cleanup (with **Clean up system files**), empty the Recycle Bin, and move large media to external storage.
2. Uninstall programs you no longer use — old games and trial software are the usual space hogs.
3. Plug in the charger and set the laptop to never sleep during updates: **Settings > System > Power & battery**, set both sleep timers to **Never** temporarily.
4. Check your drive's health: in an administrator Command Prompt, run `wmic diskdrive get status` — anything other than "OK" means the drive itself needs attention before any update.

### Fix 6: Update drivers before retrying

Driver crashes during the rollback's reboots are a top cause of hangs. Bring the critical drivers current from the manufacturer.

1. Visit your laptop maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — and download the latest chipset, storage, and display drivers for your model.
2. Install them one at a time, restarting between each. Storage and chipset drivers matter most for update reliability.
3. Open Device Manager and confirm no yellow warning icons remain.
4. Our [driver update guide](/articles/best-way-to-update-drivers-on-windows-11/) covers the safe order and how to roll back a driver that makes things worse.

### Fix 7: Block the failing update temporarily

If one specific update keeps failing and rolling back, stop Windows from offering it while you sort out the underlying problem.

1. Identify the KB number in **Settings > Windows Update > Update history**.
2. Download Microsoft's "Show or hide updates" troubleshooter and use it to hide that specific update.
3. Keep your system protected in the meantime by installing other available updates normally.
4. Revisit the hidden update after you have fixed the root cause (space, drivers, or file corruption) — do not leave a security update hidden permanently.

## Closing

"Undoing changes made to your computer" is Windows doing you a favor — it is restoring your working system, not destroying it — and almost every hang resolves with patience, one restart, or a Safe Mode pass. Fix the root cause (space, drivers, disk health) before retrying the update so you do not relive the loop. If a future update fails differently — say, with an explicit error code instead of a rollback — look up that code directly; our [DISM RestoreHealth guide](/articles/how-to-run-dism-restore-health-on-windows-11/) covers the deep component-store repairs behind many error codes, and the same systematic approach applies everywhere.
