---
title: "'Undoing Changes Made to Your Computer' Stuck on a Lenovo Laptop? How to Break the Loop"
slug: how-to-fix-undoing-changes-made-to-your-computer-stuck-on-lenovo-laptop
date: 2026-09-29
categories: ["windows-update"]
tags: ["undoing changes", "lenovo laptop", "update rollback", "stuck update", "windows 11"]
description: "Your Lenovo laptop is stuck on 'Undoing changes made to your computer'? Here's how long to wait, how to break the loop safely, and Lenovo-specific recovery options."
thumbnail: "/images/thumbs/how-to-fix-undoing-changes-made-to-your-computer-stuck-on-lenovo-laptop.webp"
faqs:
  - q: "How long should 'Undoing changes' take on a Lenovo laptop?"
    a: "On a healthy Lenovo with an SSD, the rollback usually finishes in 15 to 45 minutes. Give it at least two full hours before intervening, especially on models with hard drives or large updates. If the spinner hasn't changed after three hours with no disk activity, it's genuinely stuck and safe to act."
  - q: "Will I lose my files if I force-restart during 'Undoing changes'?"
    a: "Your personal files are almost always safe. The rollback only reverses system files and registry changes from the failed update — it doesn't touch your documents, photos, or desktop. Forcing a restart mid-rollback carries a small risk of leaving Windows unbootable, but your data on the drive remains intact."
  - q: "Why does this keep happening on my Lenovo after every update?"
    a: "Recurring rollbacks usually mean something on your system consistently conflicts with updates: an outdated Lenovo BIOS, a third-party antivirus hooking the kernel, disk errors, or a nearly full drive. Fix the underlying cause with the steps below, or the next update will roll back exactly the same way."
  - q: "Can Lenovo Vantage help prevent failed updates?"
    a: "Yes. Lenovo Vantage keeps your BIOS, chipset, and Lenovo-specific drivers current, and outdated firmware is a leading cause of update rollbacks on Lenovo hardware. Open Vantage, run System Update, install everything it offers, then retry the Windows update — this resolves a surprising number of repeat failures."
---

There is a special dread that comes from watching your Lenovo laptop sit on "Undoing changes made to your computer" for the second hour. The update failed — that much is clear — and now Windows is supposedly putting everything back the way it was. But the spinner keeps spinning, the percentage (if there even is one) never moves, and you're left wondering whether it's actually doing something or just frozen in a way that looks busy.

First, the most important thing: in the majority of cases, this screen resolves itself if you give it enough time. A rollback involves Windows restoring thousands of system files from backups, and on slower drives that is genuinely slow work. But "give it time" has a limit, and Lenovo laptops have some specific recovery tools — the Novo button, Lenovo Vantage, and built-in diagnostics — that give you better options than just holding the power button and hoping. Here's how to tell stuck from slow, and what to do in each case.

## Why this happens

- **The update failed partway through**: A cumulative or feature update hit an error during installation, and Windows automatically reverses it to keep the system bootable.
- **Outdated Lenovo BIOS or firmware**: Lenovo's firmware updates fix hardware quirks that newer Windows builds trip over; old firmware is a top cause of failed updates on ThinkPads and Ideapads.
- **Third-party antivirus interference**: Kernel-level security software can block the update from replacing protected system files, forcing a rollback.
- **Disk errors or a nearly full drive**: Updates need working space and healthy sectors; bad blocks or less than 20 GB free cause failures mid-install.
- **Corrupt update download**: A damaged package in the SoftwareDistribution cache fails integrity checks during installation.
- **Incompatible drivers**: An old storage, chipset, or graphics driver conflicts with the new build's expectations.
- **Interrupted previous update**: A prior update that was force-restarted left the component store in a half-applied state.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Wait it out — but with a deadline

Patience is genuinely the first fix. Rollbacks on spinning hard drives can take over an hour, and interrupting a working rollback is worse than the failed update.

1. Note the current time and leave the laptop plugged into AC power.
2. Watch for signs of life: listen for drive activity, check if the fan spins up occasionally, look for the spinner animating smoothly.
3. Give it **two full hours** on an SSD, **three hours** on a hard drive.
4. If the spinner is frozen (not animating) and there's zero disk activity for 60+ minutes, move to Fix 2.
5. Never unplug a laptop mid-rollback unless you've confirmed it's truly stuck — a power loss here is the one thing that can turn a recoverable situation into an unbootable one.

### Fix 2: Force a restart and let it retry the rollback

If you've confirmed it's stuck, a single forced restart is safe to try. Windows is designed to resume or restart the rollback from a safe point.

1. Hold the **power button** for 10 seconds until the laptop shuts off completely.
2. Wait 30 seconds, then power it back on.
3. Watch the boot: it will often return to "Undoing changes" and this time complete within 20–40 minutes.
4. If it boots to the desktop, the rollback finished — go to **Settings > Windows Update > Update history** to see which update failed.
5. If it returns to the stuck screen again, power off and continue to Fix 3.

### Fix 3: Boot into Safe Mode and clear the update cache

Safe Mode loads a minimal driver set, which often lets a stuck system boot when normal mode can't. From there you can clear the corrupt download that caused the failure.

1. Power off, then power on and **interrupt the boot three times** (hold power during the Lenovo logo) to reach **Automatic Repair**.
2. Go to **Troubleshoot > Advanced options > Startup Settings > Restart**, then press **4** for Safe Mode.
3. Once in Safe Mode, open **Command Prompt as administrator**.
4. Run: `net stop wuauserv` then `net stop bits`.
5. Delete the contents of `C:\Windows\SoftwareDistribution\Download` (not the folder itself).
6. Restart normally with `net start wuauserv` first, or just reboot — the services restart on their own.

### Fix 4: Update everything through Lenovo Vantage before retrying

Lenovo's own update tool handles BIOS, firmware, and Lenovo drivers that Windows Update doesn't touch — and stale firmware is the classic repeat-offender behind rollback loops on Lenovo hardware. For a broader look at Lenovo-specific update failures, see our guide to [optional updates not installing on Lenovo laptops](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop/).

1. Open **Lenovo Vantage** (install it from the Microsoft Store if missing).
2. Go to **System Update** and click **Check for Updates**.
3. Install all BIOS, firmware, and driver updates it offers — BIOS updates require AC power and a restart.
4. After Vantage finishes, go to **Settings > Windows Update** and retry the failed Windows update.
5. If Windows Update still rolls back, note the exact KB number from Update history for targeted troubleshooting.

### Fix 5: Run Lenovo's built-in diagnostics to rule out hardware

A failing drive causes rollbacks that no software fix will cure. Lenovo's UEFI diagnostics run outside Windows, so they work even when Windows won't boot.

1. Power off the laptop completely.
2. Press the **Novo button** (small pinhole button beside the power button on most Ideapads) or press **F10** repeatedly during boot on ThinkPads.
3. Select **BIOS Setup**, then find **Diagnostics**, or choose **Lenovo Diagnostics** from the Novo menu.
4. Run the **storage** and **memory** quick tests.
5. If the drive fails, back up your data immediately (boot from USB if needed) and replace the drive — no update will ever install reliably on failing storage.
6. If hardware passes, continue to Fix 6.

### Fix 6: Uninstall the failed update and pause updates

If the same update keeps failing and rolling back, stop fighting it: remove its remnants, pause updates, and wait for Microsoft to fix the package.

1. Boot into Safe Mode (Fix 3, steps 1–2).
2. Go to **Settings > Windows Update > Update history > Uninstall updates**.
3. Remove the most recent **cumulative** or **feature** update if listed.
4. Back on the Windows Update page, choose **Pause updates** for 2–3 weeks.
5. Report the failure via **Feedback Hub** with the KB number — Microsoft prioritizes fixes by report volume.
6. Meanwhile, keep your system protected with the manual steps in our [general "undoing changes" guide](/articles/what-to-do-if-windows-update-says-undoing-changes-made-to-your-computer/).

### Fix 7: Use Lenovo's recovery options as a last resort

If Windows is unbootable after the forced restart, Lenovo's recovery environment can reset or restore the system without losing everything.

1. Power off, then boot with the **Novo button** and select **System Recovery**.
2. Choose **Troubleshoot > Reset this PC > Keep my files** — this reinstalls Windows while preserving personal data.
3. If Keep my files fails, the **Lenovo USB Recovery Creator** (on another PC) can build factory recovery media for your exact model from [Lenovo support](https://support.lenovo.com/us/en/).
4. After recovery, install Lenovo Vantage updates first, then Windows updates — in that order.

## Closing

The "Undoing changes" screen on a Lenovo is Windows protecting you from a bad update — the rollback itself is the safety net working. Give it its two hours, clear the corrupt cache if it's truly stuck, and use Lenovo Vantage to eliminate the firmware gaps that cause most repeat failures. Break the loop once with the steps above, fix the underlying cause, and the next update should sail through instead of rolling back.
