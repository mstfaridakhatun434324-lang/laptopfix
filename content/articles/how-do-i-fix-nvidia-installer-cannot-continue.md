---
title: "How Do I Fix the NVIDIA 'Installer Cannot Continue' Error?"
slug: how-do-i-fix-nvidia-installer-cannot-continue
date: 2026-10-04
categories: ["drivers"]
tags: ["nvidia installer error", "fix nvidia install failed", "nvidia driver won't install", "geforce experience install error", "nvidia clean install"]
description: "Stuck on 'NVIDIA Installer cannot continue'? Here's the direct answer: the checks to run, the order to run them in, and the fixes that get the driver installed."
thumbnail: "/images/thumbs/how-do-i-fix-nvidia-installer-cannot-continue.webp"
faqs:
  - q: "I keep getting 'NVIDIA installer cannot continue.' What's the first thing to try?"
    a: "Pause Windows Update, then run the installer again as administrator. Background Windows driver installs colliding with your manual install cause a large share of these failures, and pausing updates removes the conflict instantly. If it still fails, download a fresh copy of the driver from NVIDIA's site — corrupted downloads are the second most common cause — and choose the DCH driver type during selection."
  - q: "How do I know whether I need the DCH or standard NVIDIA driver?"
    a: "Almost everyone needs DCH now — it's the driver type Windows 10 and 11 expect, with the control panel delivered via the Microsoft Store. You only need the standard driver if you're running an older OS configuration or specific enterprise tooling. If a previous install used one type and you're installing the other, the installer fails; a clean removal with Display Driver Uninstaller in Safe Mode lets you switch types cleanly."
  - q: "The installer fails even in Safe Mode. What now?"
    a: "First, confirm you downloaded the driver for your exact GPU model — installing a desktop RTX driver package on a laptop with a mobile variant, or vice versa, fails the hardware check. Second, check for pending Windows updates requiring a restart, since the OS blocks driver installs until they complete. Third, run Display Driver Uninstaller to clear remnants, then install immediately before Windows Update intervenes."
  - q: "Can I just let Windows Update install the NVIDIA driver instead?"
    a: "You can, and it works for basic display output, but Windows Update drivers lag months behind NVIDIA's releases and lack GeForce Experience, game-ready optimizations, and the full control panel. They're fine as a temporary fallback to get a working display. For gaming, creative work, or CUDA, install the proper NVIDIA package — just pause Windows Update first so the two don't fight."
---

Short answer first: pause Windows Update, download a fresh DCH driver from NVIDIA, run it as administrator, and choose Custom > Clean Installation. That sequence fixes the majority of "installer cannot continue" failures. If it doesn't, the problem is one level deeper — driver-type mismatch, locked remnants, or a hardware check failure — and the steps below walk you through identifying and fixing each one.

This guide is the practical companion to driver troubleshooting: less theory, more "do this, then this." You'll need your exact GPU model (check Device Manager > Display adapters if you're unsure).

Here is the honest order of operations, ranked by how often each step resolves it: first, stop the thing fighting the installer (pause Windows Update); second, make sure the package itself is good (fresh DCH download, run as admin); third, clear whatever the previous install left behind (DDU in Safe Mode). That sequence resolves the overwhelming majority of cases, and each step takes only a few minutes. The remaining steps below are for the stubborn remainder — wrong package, pending OS updates, antivirus interference — plus how to read the installer log when you need the actual error instead of another guess. Work them in order and do not skip the log step if you reach it; it is the difference between fixing and flailing. And once you have a working install, write down the exact driver version and package name somewhere — the next time this error appears, that note tells you in seconds whether you are dealing with a regression or a new problem. Most "installer cannot continue" errors are solved once and never return — the ones that recur almost always trace back to Windows Update being unpaused too early.

## Why this happens

- **Windows Update is installing a driver at the same time**, and the two installers collide.
- **DCH vs. standard driver type mismatch** with whatever was installed before.
- **Corrupted installer download** — partial or damaged package.
- **Leftover files and registry entries** from a previous install blocking the new one.
- **Wrong driver package** for your GPU variant (desktop vs. laptop/mobile).
- **Pending Windows updates** requiring a restart before driver installs are allowed.
- **Not running as administrator**, so the installer can't write system files.
- **Antivirus quarantining** installer components mid-install.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Pause Windows Update, then retry as administrator

The quickest win — do this before anything drastic.

1. Go to **Settings > Windows Update** and **Pause updates** for one week.
2. Right-click the NVIDIA installer and choose **Run as administrator**.
3. Choose **Custom (Advanced)** and tick **Perform a clean installation**.
4. If it succeeds, you've just fixed a Windows Update collision — the most common cause.

### Fix 2: Get a fresh, correct driver package

Don't trust the installer file you've been retrying.

1. Delete the old installer file.
2. Go to [NVIDIA's driver download page](https://www.nvidia.com/Download/index.aspx).
3. Enter your exact GPU — pay attention to laptop (mobile/Max-Q) vs. desktop variants, which are separate entries.
4. Select **DCH** as the Windows driver type and download fresh.

### Fix 3: Clear remnants with Display Driver Uninstaller

When the installer keeps failing on the same machine, old remnants are usually the blocker.

1. Download DDU from its official source (Wagnardsoft).
2. Boot into **Safe Mode**.
3. In DDU, select **GPU > NVIDIA** and click **Clean and restart**.
4. After reboot, install the fresh DCH driver from Fix 2 immediately — before unpausing Windows Update.
5. DDU removes the services, registry keys, and locked files the standard uninstaller leaves behind.

### Fix 4: Install pending Windows updates first

Sometimes the OS itself is the gatekeeper.

1. Unpause updates temporarily and install everything pending in **Settings > Windows Update**.
2. Restart fully when prompted — some updates need two restart cycles.
3. Pause updates again, then run the NVIDIA installer.
4. The installer is blocked when Windows has a pending restart flag; clearing it removes the block.

### Fix 5: Temporarily disable antivirus during install

Five minutes of testing that rules out interference.

1. Open **Windows Security > Virus & threat protection** and turn off real-time protection temporarily.
2. Run the installer as administrator with the clean-install option.
3. Turn protection back on immediately after.
4. If this was the fix, add the NVIDIA installer to your antivirus exclusions for future updates.

### Fix 6: Check the installer log for the specific failure

When all else fails, get the actual error.

1. After a failure, check `C:\Program Files\NVIDIA Corporation\Installer2\` for the latest log.
2. Search for "failed" or "error" — the surrounding lines name the component.
3. Hardware ID mismatches mean wrong package; "file in use" means remnants (back to Fix 3); DCH/standard messages mean type mismatch.
4. For a structured walkthrough of log-based diagnosis, see our [NVIDIA installer troubleshooting guide](/articles/troubleshoot-nvidia-installer-cannot-continue/).

### Fix 7: Use Windows Update as a temporary fallback

Get a working display now, fix it properly later.

1. Uninstall the broken partial install via **Settings > Apps**.
2. Unpause Windows Update and check for updates — let it install its NVIDIA driver.
3. You'll get basic display output without GeForce Experience or game-ready features.
4. Return to the manual install later when you have time for the DDU process.

## Closing

The direct answer to "how do I fix it" is: eliminate the collision (pause Windows Update), eliminate the package (fresh DCH download), eliminate the remnants (DDU in Safe Mode), in that order. Most people never need to get past step two. Once the driver is in, verify the installed version matches what you downloaded — our [driver version check guide](/articles/how-to-check-driver-version-in-device-manager/) shows how — and consider making future updates [proper clean installs](/articles/how-can-i-update-nvidia-drivers-clean-install/) so this error stays in your past. If the installer fails again on the next driver release, you now have a repeatable playbook: pause updates, fresh download, clean install — and the log file to tell you exactly which step matters.
