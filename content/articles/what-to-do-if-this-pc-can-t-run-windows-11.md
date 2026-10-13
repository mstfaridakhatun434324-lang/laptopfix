---
title: "This PC Can't Run Windows 11? Here's What to Do Next"
slug: what-to-do-if-this-pc-can-t-run-windows-11
date: 2026-09-21
categories: ["windows-errors"]
tags: ["windows 11", "compatibility", "tpm"]
description: "Failed the Windows 11 compatibility check? Enable TPM and Secure Boot, verify your CPU, and learn your real options if the PC truly can't upgrade."
thumbnail: "/images/thumbs/what-to-do-if-this-pc-can-t-run-windows-11.webp"
faqs:
  - q: "Why does my PC fail the Windows 11 check when it seems fast enough?"
    a: "Speed isn't the issue — Windows 11 has hard security requirements: TPM 2.0, Secure Boot capability, a supported 64-bit CPU, and 4 GB of RAM. Most failures are TPM 2.0 being disabled in the BIOS, which is a two-minute fix. Genuinely unsupported CPUs, mostly older than 8th-gen Intel or Ryzen 2000 series, are the other common cause."
  - q: "How do I check if my PC has TPM 2.0?"
    a: "Press Win + R, type tpm.msc, and press Enter. The TPM Management window shows whether a TPM is present and its specification version. If it says no compatible TPM was found, reboot into your BIOS and look for TPM, PTT (Intel), or fTPM (AMD) settings — enabling it there is all most PCs need."
  - q: "Is it safe to install Windows 11 on unsupported hardware?"
    a: "Microsoft documents a registry-based method to bypass the checks, but PCs installed that way may not receive updates, including security updates, and Microsoft warns they could experience problems. For a daily-use laptop, the safer paths are staying on a supported Windows 10 with good security habits or upgrading the hardware."
  - q: "What happens if I just stay on Windows 10?"
    a: "Windows 10 keeps working after its support end date, but it stops getting security patches, which gradually increases your risk online. If your hardware can't run Windows 11, you can still stay reasonably safe with an updated browser, Windows Security, and careful habits — but plan a hardware upgrade as your long-term answer."
---

Running the compatibility checker and seeing "This PC can't run Windows 11" is annoying, especially when your laptop feels perfectly fast. But here's the thing most people miss: the check usually fails on a setting, not on your hardware. TPM 2.0 sits disabled in the BIOS on countless PCs that fully support it.

Before you assume you need a new laptop, work through the checks below. A surprising number of "incompatible" PCs just need two BIOS toggles flipped.

## Why this happens

- **TPM 2.0 is disabled in the BIOS.** The chip is there on most PCs from 2016 onward, but the firmware setting is off by default on many boards.
- **Secure Boot is disabled or in Setup Mode.** Windows 11 requires Secure Boot capability, and some systems ship with it off.
- **CPU isn't on the supported list.** Microsoft cut off at 8th-gen Intel Core and AMD Ryzen 2000 series — older chips fail no matter what you toggle.
- **Outdated BIOS.** An old firmware version may not expose TPM 2.0 or Secure Boot options that a newer version adds.
- **Legacy BIOS/CSM boot mode.** Systems booting in old Legacy mode instead of UEFI can't enable Secure Boot.
- **Insufficient RAM or storage.** Less than 4 GB of RAM or a tiny system drive fails the check outright.

## How to fix it

Work through these in order, from Fix 1 onward, and stop once the checker gives you a green light.

### Fix 1: Find out exactly what failed

Don't guess — the checker tells you precisely which requirement failed.

1. Download the **PC Health Check** app from Microsoft's Windows 11 page.
2. Run it and click **Check now** in the Windows 11 section.
3. Click **See all results** to expand the full list of passed and failed requirements.
4. Write down every failed item — you'll address each one below.
5. If everything passes except one toggle, you're minutes away from upgrading.

### Fix 2: Enable TPM 2.0 in the BIOS

This single setting fixes the majority of failures.

1. Restart and enter the BIOS/UEFI (**F2**, **Del**, or **F12** during boot).
2. Look under **Security**, **Advanced**, or **Trusted Computing** for the TPM setting.
3. On Intel systems it may be called **PTT** (Platform Trust Technology); on AMD, **fTPM**.
4. Set it to **Enabled**, save, and exit.
5. Back in Windows, press **Win + R**, type `tpm.msc`, and confirm it now shows Specification Version 2.0.

### Fix 3: Enable Secure Boot

The second most common toggle, often disabled on systems that shipped with Windows 10.

1. Enter the BIOS/UEFI again.
2. Find **Secure Boot** under the **Security** or **Boot** tab.
3. If the OS Type or boot mode is set to **Legacy/CSM**, change it to **UEFI** first — Secure Boot requires UEFI mode.
4. Set **Secure Boot** to **Enabled**.
5. Save and exit, then re-run the PC Health Check to confirm it passes.

### Fix 4: Check your CPU against the supported list

If TPM and Secure Boot are fine but the CPU fails, verify it properly.

1. Press **Win + R**, type `msinfo32`, and note your exact **Processor** line.
2. Compare it against Microsoft's official supported CPU lists for Windows 11.
3. Note that 7th-gen Intel and first-gen Ryzen are excluded with very few exceptions, even though they're capable chips.
4. If your CPU is genuinely unsupported, skip to Fix 7 — no BIOS setting will change this.
5. If it IS on the list but the checker disagrees, update your BIOS (Fix 5) — old firmware sometimes misreports the CPU.

### Fix 5: Update the BIOS

Manufacturers added Windows 11 readiness — proper TPM exposure, Secure Boot fixes — in BIOS updates.

1. Check your current version with `msinfo32` under **BIOS Version/Date**.
2. Visit your laptop maker's support page and find BIOS updates for your exact model.
3. Read the release notes — look for mentions of TPM, Secure Boot, or Windows 11 support.
4. Flash the update with the laptop plugged in and all programs closed.
5. After the flash, re-enter the BIOS and verify TPM and Secure Boot are still enabled, then re-run the checker.

### Fix 6: Free up the basics — RAM, storage, and display

Sometimes the failure is refreshingly simple.

1. Confirm at least 4 GB of RAM in **Settings > System > About**.
2. Make sure the system drive has 64 GB or more total capacity.
3. Check your display is larger than 9 inches with 720p resolution (a non-issue for any real laptop).
4. If RAM is the only failure and your laptop has a free slot, a cheap stick upgrade solves it.
5. Re-run the checker after each change.

### Fix 7: Decide your path if the hardware truly can't do it

If the CPU is unsupported and no update will fix that, you have three honest options.

1. **Stay on Windows 10 carefully.** Keep your browser and antivirus updated, avoid sketchy downloads, and treat the machine as higher-risk over time.
2. **Upgrade the hardware.** On desktops, a motherboard/CPU swap may be cheaper than a new PC; on laptops, it usually means a new machine.
3. **Consider the documented bypass with eyes open.** Microsoft publishes a registry method to skip the checks, but warns such PCs may miss updates — only for tinkerers, never for your main work laptop.
4. Whatever you choose, back up your files first — big system changes always carry some risk.
5. If you do a fresh install of anything, our [reset guide](/articles/how-to-reset-windows-11-without-losing-files/) covers the process safely.

### Fix 8: Prepare properly once you pass the check

Passing the checker is step one — a smooth upgrade needs a little prep.

1. Back up your important files to an external drive or cloud storage.
2. Update your BIOS, chipset, and storage drivers to their latest versions first.
3. Uninstall any third-party antivirus temporarily — it causes a disproportionate share of upgrade failures.
4. Run the upgrade with the laptop plugged in and connected to stable internet.
5. After upgrading, create a [system restore point](/articles/how-to-use-system-restore-on-windows-11/) immediately so you have a way back.

## Closing

Most "This PC can't run Windows 11" verdicts are just TPM or Secure Boot waiting to be switched on — five minutes in the BIOS, not a new laptop. Only when the CPU itself is unsupported is the answer really no. Check precisely what failed, fix what's fixable, and make a deliberate choice about the rest. And if you do upgrade, grab Windows 11 from the [official download page](https://www.microsoft.com/en-us/software-download/windows11) to be sure you're getting the real thing.
