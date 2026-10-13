---
title: "Windows 11 Green Screen of Death: Step-by-Step Troubleshooting"
slug: how-to-fix-windows-11-green-screen-of-death
date: 2026-09-03
categories: ["windows-errors"]
tags: ["green-screen-of-death", "windows-insider", "windows-11"]
description: "Seeing a green screen instead of blue on Windows 11? You are running an Insider preview build. Here is what the GSOD means and how to fix it."
thumbnail: "/images/thumbs/how-to-fix-windows-11-green-screen-of-death.webp"
faqs:
  - q: "What is the Green Screen of Death?"
    a: "It is exactly the same as the Blue Screen of Death, but green — Microsoft uses the green color on Windows Insider preview builds so engineers can instantly tell a crash came from a preview build rather than a stable release. The stop codes and troubleshooting are identical to BSODs."
  - q: "Does a green screen mean my problem is worse?"
    a: "No. The color only tells you which Windows channel you are on. But it does mean you are running pre-release software, which is buggier by design — some GSODs are Microsoft's bugs, not yours, and get fixed in the next Insider flight."
  - q: "Should I leave the Insider program if I keep getting green screens?"
    a: "If the machine is your daily driver and stability matters, yes — drop back to stable Windows. Insider builds exist to find bugs, and regular GSODs are the price of admission. Stay only if you can tolerate breakage and want to help test."
  - q: "How do I report a green screen to Microsoft?"
    a: "Use the Feedback Hub (**Win + F**) and file it under the appropriate category with the stop code. If the crash generated a dump, mention it. Microsoft triages Insider crashes aggressively — your report genuinely helps get the bug fixed in a later flight."
---
If your crash screen is green instead of blue, nothing exotic has happened — you are running a Windows Insider preview build, and Microsoft colors those crashes green to distinguish them from stable-release blue screens. Same stop codes, same causes, same fixes. If your crash screen is green instead of blue, nothing exotic has happened — you are running a Windows Insider preview build, and Microsoft colors those crashes green to distinguish them from stable-release blue screens. Same stop codes, same causes, same fixes.

The one real difference: some green screens are bugs in the preview build itself, which no amount of driver updating on your part will fix. This guide covers both sides — fixing your stuff, and handling Microsoft's stuff. The one real difference: some green screens are bugs in the preview build itself, which no amount of driver updating on your part will fix. This guide covers both sides — fixing your stuff, and handling Microsoft's stuff.

## Why this happens

- **You are on an Insider preview build.** Pre-release code has pre-release bugs; some GSODs are simply Microsoft's fault.
- **The same driver causes as blue screens.** Buggy graphics, storage, and filter drivers crash Insider builds too.
- **Incompatible software.** Some antivirus and system utilities do not support preview kernel changes and crash.
- **A bad Insider flight.** Occasionally a specific preview build has a known-crashing bug affecting many users.
- **Failing hardware.** RAM and drive failures cause green screens exactly like blue ones — the color changes nothing here.
- **Overclocking.** Unstable tuning crashes preview builds just as readily as stable ones.

## How to fix it

Work through these in order, from the quickest and most likely fixes to the deeper ones. Stop as soon as the crashes stop.

### Fix 1: Note the stop code and check for known flight issues

On Insider builds, your first check is whether Microsoft already knows about it. On Insider builds, your first check is whether Microsoft already knows about it — a surprising number of GSODs are known flight bugs with fixes already in the pipeline.

1. Write down the full stop code from the green screen (disable auto-restart first if needed — see our [auto-restart guide](/articles/how-to-disable-automatic-restart-after-bsod-in-windows-11-24h2/)).
2. Search the Feedback Hub and the Windows Insider blog for the stop code plus your build number (`winver` shows it).
3. If it is a known issue with a fix in the next flight, the correct action is to wait — or roll back, below.

### Fix 2: Update your drivers

Preview builds change kernel interfaces; drivers must keep up. Preview builds change kernel interfaces; drivers must keep up — and GPU vendors usually ship Insider-compatible drivers within days of a new flight.

1. Update graphics drivers from the GPU maker: [NVIDIA](https://www.nvidia.com/Download/index.aspx), [AMD](https://www.amd.com/en/support/download/drivers.html), or the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html).
2. Update chipset and storage drivers from your laptop maker's support site.
3. Uninstall any system utility that has not released an Insider-compatible version — old filter drivers are GSOD factories on preview builds.

### Fix 3: Run the standard corruption repairs

The usual suspects still apply on green builds. The usual suspects still apply on green builds — SFC, DISM, chkdsk, and the memory diagnostic work exactly the same regardless of screen color.

1. In an elevated **Terminal**, run `sfc /scannow`.
2. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Run `chkdsk C: /f` and reboot for the disk scan.
4. Test the RAM with `mdsched.exe` — hardware does not care what color the crash screen is.

### Fix 4: Roll back to the previous Insider build

If the GSODs started with the latest flight, retreat one step. If the GSODs started with the latest flight, retreat one step — the 10-day rollback window is short, so do not sit on a crashing build hoping it fixes itself.

1. Go to **Settings > System > Recovery > Go back** (available for 10 days after a new build installs).
2. If that option is gone, download the previous build's ISO from the Windows Insider ISO page and do an in-place downgrade keeping files.
3. Pause Insider updates for a week or two to avoid reinstalling the bad flight immediately.

### Fix 5: Leave the Insider program for stable Windows

The permanent fix for preview-build instability is to stop running preview builds. The permanent fix for preview-build instability is to stop running preview builds — stable Windows exists precisely for machines that need to work.

1. Go to **Settings > Windows Update > Windows Insider Program > Stop getting preview builds**.
2. Choose to unenroll — on Dev channel this may require a clean install of stable Windows, so back up first.
3. Download stable Windows 11 from Microsoft's official Windows 11 download page and install it.
4. Your green screens become blue screens — or better, disappear entirely, since stable builds lack the preview bugs. For general crash troubleshooting on stable, our [BSOD guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) applies.

### Fix 6: File feedback before you leave

If a genuine Microsoft bug caused your crashes, report it so it gets fixed. If a genuine Microsoft bug caused your crashes, report it so it gets fixed — Insider crashes with good feedback get triaged fast.

1. Press **Win + F** to open Feedback Hub.
2. File under **Install and Update > Windows Insider Program** or the relevant hardware category.
3. Include the stop code, build number, and steps to reproduce. Attach the minidump from `C:\Windows\Minidump` if the form allows.

### Fix 7: Switch Insider channels instead of leaving entirely

If you like early features but Dev-channel chaos is too much, the Beta channel is the middle ground — still preview, far calmer.

1. Go to **Settings > Windows Update > Windows Insider Program** and change to the **Beta Channel**.
2. Beta builds are tied to upcoming releases and go through more validation than Dev builds.
3. You may need to wait for the next Beta flight rather than downgrading immediately — check the Insider blog for timing.
4. Many chronic GSOD sufferers find Beta gives them the early-access feel without the weekly breakage.

## Closing

A green screen of death is a blue screen wearing an Insider badge. Troubleshoot it like any crash — drivers, files, hardware — but keep one eye on the possibility that the preview build itself is the bug. And if stability matters more than early features, the stable channel is always waiting. Green screens are the cost of running preview software — budget for them, report them, and keep stable Windows on any machine you actually depend on.
