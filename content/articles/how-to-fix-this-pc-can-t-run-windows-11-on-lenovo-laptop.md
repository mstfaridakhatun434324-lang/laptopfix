---
title: "\"This PC Can't Run Windows 11\" on Your Lenovo? Here's the Fix"
slug: how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop
date: 2026-09-03
categories: ["windows-errors"]
tags: ["windows 11", "compatibility", "tpm", "lenovo"]
description: "PC Health Check says your Lenovo can't run Windows 11? It's usually just TPM or Secure Boot settings. Here's how to pass the check."
thumbnail: "/images/thumbs/how-to-fix-this-pc-can-t-run-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "Why does my Lenovo fail the Windows 11 compatibility check?"
    a: "In most cases it's not the hardware — it's BIOS settings. TPM 2.0 is often labeled 'Security Chip' and ships disabled on older Lenovo BIOS versions, and Secure Boot may be off too. Enabling both in the BIOS makes the large majority of supported ThinkPads, Ideapads, and Legions pass the check."
  - q: "What are the actual Windows 11 hardware requirements?"
    a: "A 1GHz+ 64-bit dual-core CPU from the supported list, 4GB RAM, 64GB storage, UEFI with Secure Boot, TPM 2.0, and DirectX 12 graphics. The PC Health Check app tests each one and tells you exactly which failed — start there before changing anything."
  - q: "My CPU isn't on Microsoft's supported list. Can I still install Windows 11?"
    a: "The installer will block you, and bypassing the check is possible via registry edits during setup — but Microsoft warns such installs may not receive updates. For a daily-use laptop, staying on Windows 10 (supported with updates into late 2025) or upgrading the machine is the safer path."
  - q: "Where is the TPM setting in Lenovo BIOS?"
    a: "Enter BIOS with F1 (ThinkPad) or F2 (Ideapad/Legion) during startup, then go to the Security tab. Look for Security Chip or TPM 2.0 and set it to Enabled/Active. On newer ThinkPads it's under Security > Security Chip Selection — choose TPM 2.0 rather than TPM 1.2."
---

"This PC Can't Run Windows 11" on Your Lenovo? Here's the Fix

You ran Microsoft's PC Health Check, full of hope, and it cheerfully announced your perfectly good Lenovo "can't run Windows 11." Before you start shopping for a new laptop: on Lenovos, this message is wrong more often than it's right. The hardware is usually fine — it's the BIOS settings (TPM hiding under the name "Security Chip," Secure Boot switched off) that trip the check.

This guide walks through the real requirements, shows you exactly where Lenovo hides the relevant BIOS settings on ThinkPads, Ideapads, and Legions, and tells you honestly what to do if your machine genuinely doesn't qualify. If setup itself is failing rather than the check, see our guide to [Windows 11 installation failures](/articles/how-to-fix-windows-11-installation-failed-on-dell-laptop/).

## Why this happens

- **TPM is disabled or set to 1.2.** Lenovo BIOSes call it "Security Chip," and many shipped with it off or on the older 1.2 mode.
- **Secure Boot is off.** Required by Windows 11, but disabled on machines that shipped with Legacy boot or were tweaked for Linux.
- **The BIOS is in Legacy/CSM mode.** Windows 11 requires UEFI; Compatibility Support Mode must be off.
- **The CPU genuinely isn't supported.** Microsoft's CPU list cuts off older generations (pre-8th-gen Intel, pre-Ryzen 2000 AMD) even if they're fast enough.
- **The BIOS is outdated.** Old firmware can misreport TPM status to the checker.
- **PC Health Check itself was buggy.** Early versions gave false failures; make sure you're running the latest version from Microsoft.

## How to fix it

Work through these in order — most Lenovos pass after Fix 1 and 2.

### Fix 1: Run PC Health Check and note what failed

Don't guess; let the tool tell you exactly which requirement failed.

1. Download the latest **PC Health Check** app from Microsoft's Windows 11 page and run it.
2. Click **Check now** and read the results carefully — it lists each requirement with a pass/fail.
3. Screenshot or note the failures. TPM, Secure Boot, and processor are the big three.
4. If everything passes but the installer still complains, your installation media is probably old — recreate it from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).

### Fix 2: Enable the Security Chip (TPM 2.0) in Lenovo BIOS

This single setting fixes the majority of Lenovo failures.

1. Shut down fully, power on, and press **F1** (ThinkPad) or **F2** (Ideapad/Legion) repeatedly to enter BIOS setup.
2. Go to the **Security** tab. Find **Security Chip** (older BIOS) or **Security Chip Selection** (newer ThinkPads).
3. Set it to **Enabled**, or select **TPM 2.0** if there's a 1.2/2.0 choice. Also enable **Security Chip** sub-options like **Intel PTT** if present (PTT is Intel's firmware TPM — it counts).
4. On AMD Lenovos, look for **AMD fTPM Switch** under Security or Advanced and enable it.
5. Save and exit (**F10**), then re-run PC Health Check.

### Fix 3: Enable Secure Boot and UEFI mode

The second most common blocker.

1. Re-enter BIOS (**F1**/**F2**) and go to the **Security** tab (ThinkPad) or **Boot** tab.
2. Set **Secure Boot** to **Enabled**. If it's greyed out, first set **UEFI/Legacy Boot** to **UEFI Only** and disable **CSM Support**.
3. On ThinkPads: **Security > Secure Boot > Secure Boot = Enabled**, with **UEFI/Legacy Boot** under the **Startup** tab set to **UEFI Only**.
4. Save, exit, and re-run the check. Note: switching from Legacy to UEFI on an existing Windows 10 install requires converting the disk to GPT first (Microsoft's `mbr2gpt` tool) or Windows won't boot.

### Fix 4: Update the Lenovo BIOS

Old firmware misreports capabilities to the checker.

1. Find your serial number (bottom sticker, or in Lenovo Vantage under **Device**).
2. Go to [Lenovo Support](https://support.lenovo.com/us/en/), enter the serial, and check for BIOS updates under **Drivers & Software**.
3. Install via **Lenovo Vantage** (easiest — it handles the flash) or download the BIOS Update Utility — always on AC power.
4. After flashing, re-check that TPM and Secure Boot are still enabled (updates can reset them), then re-run PC Health Check.

### Fix 5: Verify CPU and RAM requirements honestly

Sometimes the answer is genuinely no — here's how to confirm.

1. Check your CPU against Microsoft's supported processor lists (search "Windows 11 supported Intel/AMD processors" on [Windows support](https://support.microsoft.com/en-us/windows)).
2. Verify 4GB+ RAM: **Settings > System > About** shows installed RAM.
3. If the CPU is the only failure and it's a generation or two too old, the machine can still run Windows 11 via documented bypasses — but expect possible update issues, and weigh that against a machine that meets the spec.
4. If multiple core requirements fail on very old hardware, the pragmatic move is a clean Windows 10 install or a hardware upgrade, not a fight with the installer.

### Fix 6: Use Lenovo Vantage to prep the system

Lenovo's own tool smooths the path.

1. Install **Lenovo Vantage** from the Microsoft Store if it's not present.
2. Run **System Update** inside Vantage to pull firmware and driver updates — outdated firmware is a sneaky check-failure cause.
3. Use Vantage's **Hardware Scan** to confirm no underlying hardware faults are confusing the issue.
4. Related boot-mode confusion (UEFI vs Legacy) also causes [installation failures](/articles/how-to-fix-windows-11-installation-failed-on-dell-laptop/) — the same BIOS screens are involved.

### Fix 7: Do a clean compatibility retest

Finish with a clean, definitive test.

1. Update PC Health Check to the latest version (Microsoft fixed early false-failure bugs).
2. Re-run the check after all BIOS changes — it should now pass on any supported Lenovo from the last several years.
3. If it passes, proceed with the Windows 11 install via Windows Update or the Installation Assistant.
4. If one requirement still fails despite correct settings, reset the BIOS to defaults (**F9** in BIOS, then re-enable TPM/Secure Boot) — a corrupted BIOS setting can report wrong values to the checker.

## Closing

"This PC can't run Windows 11" on a Lenovo is usually the BIOS telling a white lie — the Security Chip is off, Secure Boot is off, or the firmware is old. Flip the right switches in the Security tab, update the BIOS, and the check that failed yesterday passes today. And if your CPU genuinely misses the list, at least you'll know it's the silicon, not a setting. For a full checklist of every compatibility-check failure and its fix beyond Lenovo-specific settings, see our [general "This PC can't run Windows 11" troubleshooting guide](/articles/this-pc-can-t-run-windows-11-troubleshooting/).
