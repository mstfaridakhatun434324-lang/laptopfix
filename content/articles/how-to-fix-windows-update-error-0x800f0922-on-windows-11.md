---
title: "Fix Windows Update Error 0x800F0922 on Windows 11: Causes and Fixes"
slug: how-to-fix-windows-update-error-0x800f0922-on-windows-11
date: 2026-09-03
categories: ["windows-update"]
tags: ["windows 11", "windows update", "error 0x800f0922", "secure boot", "efi partition"]
description: "Error 0x800F0922 on Windows 11 is often tied to Secure Boot or a full EFI partition. Diagnose the real trigger and apply the right fix."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0922-on-windows-11.webp"
faqs:
  - q: "What does error 0x800F0922 mean?"
    a: "It indicates a failure in the CBS (Component-Based Servicing) layer, often when the update cannot verify boot files or write to the EFI system partition. Common triggers include Secure Boot policy conflicts, a full EFI partition, corrupted servicing data, or VPN interference during download."
  - q: "Is 0x800F0922 caused by Secure Boot being enabled?"
    a: "Not by Secure Boot itself, but by conflicts around it — for example, boot files signed in a way the firmware rejects, or third-party bootloaders (like Linux dual-boot setups) that Secure Boot policies flag during the update's boot-file verification phase."
  - q: "Can a VPN cause 0x800F0922?"
    a: "Yes, surprisingly often. Some VPN configurations interfere with the download or verification of update payloads in ways that surface as this CBS error rather than a network error. Disconnecting the VPN completely and retrying the update is a quick, worthwhile test that takes under two minutes."
  - q: "How much free space does the EFI partition need?"
    a: "The EFI system partition is typically 100 MB, and updates need a portion of it free to stage boot files. If it is nearly full — common on systems with multiple bootloaders from dual-boot setups — the update fails. Freeing space by removing obsolete bootloader entries, or recreating the partition larger, resolves it."
---

Error 0x800F0922 is one of the more interesting Windows Update failures because it sits at the intersection of servicing, boot security, and networking. The code surfaces from the Component-Based Servicing layer when an update cannot complete its boot-file or payload-verification steps. On Windows 11, the usual suspects are Secure Boot conflicts, a cramped EFI system partition, corrupted servicing data, or — unexpectedly often — an active VPN connection mangling the download.

Because the triggers are diverse, diagnosis matters more here than with simpler errors. The sequence below starts with the quick environmental checks (VPN, Secure Boot state, EFI space) before moving to servicing repairs. Note when the error appears: during download points at the network; during the install phase points at boot files and servicing.

## Why this happens

- **Secure Boot policy conflicts:** Boot files that fail Secure Boot verification — common with dual-boot setups or modified bootloaders — abort the update's boot phase.
- **Full EFI system partition:** The 100 MB EFI partition fills up with multiple bootloaders or stale files, leaving no room to stage updated boot files.
- **Corrupted servicing (CBS) data:** Damaged component store or manifests cause the CBS layer to fail with this code.
- **VPN interference:** VPN tunnels can corrupt or block update payload transfers, producing verification failures that surface as 0x800F0922.
- **Third-party boot managers:** Tools like rEFInd or GRUB alongside Windows can conflict with the update's boot-file operations.
- **Corrupted boot configuration data:** Damaged BCD entries fail the update's boot validation checks.
- **Antivirus blocking boot-file writes:** Security software preventing writes to the EFI partition stalls the update.
- **Failing SSD sectors in boot areas:** Storage damage under the EFI partition or boot files produces persistent failures.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disconnect the VPN and retry

The quickest test on the list. VPN interference is a documented trigger for this exact error.

1. Disconnect any VPN client completely (not just pause — fully disconnect or exit the app).
2. If you use a VPN at the router level, temporarily bypass it.
3. Go to **Settings > Windows Update** and click **Retry** or **Check for updates**.
4. If the update now succeeds, the VPN was the cause — update with it disconnected in future, or whitelist Microsoft update endpoints in the VPN.

### Fix 2: Check Secure Boot status and boot configuration

Determine whether boot security is part of the problem before changing anything.

1. Press **Win + R**, type `msinfo32`, and check **Secure Boot State** — note whether it is On, Off, or Unsupported.
2. If you dual-boot Linux, be aware the update may be tripping over the alternate bootloader — this is a known 0x800F0922 trigger.
3. Do not disable Secure Boot permanently as a "fix" — instead, ensure your bootloaders are current and properly signed. Temporarily toggling it off for one update attempt is a diagnostic step, not a solution.
4. If the machine has third-party boot managers, update them to their latest versions.

### Fix 3: Free space on the EFI system partition

A full EFI partition is a classic cause. Check and clean it carefully.

1. Open **Disk Management** and identify the **EFI System Partition** (usually 100 MB, FAT32).
2. In **Terminal (Admin)**, run `mountvol S: /s` to mount it as S:.
3. Open S: in File Explorer and look for duplicate or stale bootloader folders (e.g., old Linux entries you no longer use, or duplicate Microsoft folders).
4. Remove only entries you are certain are obsolete — never delete the active Microsoft boot folder. Then run `mountvol S: /d` to unmount.
5. Retry the update.

### Fix 4: Reset the update cache

Clear corrupted payloads and manifests that fail CBS verification.

1. In **Terminal (Admin)**, run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Restart and check for updates with the VPN still disconnected.

### Fix 5: Repair the component store with DISM and SFC

CBS-layer errors respond to servicing repairs.

1. In **Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then run `sfc /scannow`.
3. Restart and retry. This same servicing repair clears [0x80070490 element-not-found errors](/articles/how-to-fix-windows-update-error-0x80070490-on-windows-11/), which share the CBS layer with this error.

### Fix 6: Rebuild the boot configuration data

If boot validation is the failing step, rebuild the BCD.

1. Boot into WinRE (**Settings > System > Recovery > Advanced startup > Restart now**, then **Troubleshoot > Advanced options > Command Prompt**).
2. Run `bootrec /fixmbr`, then `bootrec /rebuildbcd`.
3. If prompted about installations found, answer **Y** to add them.
4. Exit, boot normally, and retry the update.

### Fix 7: Install the update manually

Bypass the whole pipeline: note the KB number, download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), and run the `.msu` directly with the VPN disconnected. If the manual install also fails at the boot phase, the issue is definitively in the boot environment (EFI space, Secure Boot, BCD) rather than the download — focus your remaining effort there, consulting the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) for boot-related guidance.

Dual-boot users should pay special attention to the Secure Boot and EFI steps, because this error's boot-file dimension hits them hardest. When Windows Update stages new boot files, it validates the boot environment — and a GRUB or rEFInd setup with outdated signatures can fail that validation even though Windows itself boots fine day to day. Keeping your Linux bootloader updated is not just good hygiene; it is update compatibility maintenance. If your machine is Windows-only and you still see this error, the VPN test remains the most likely winner. The [Windows 10 version of this guide](/articles/how-to-fix-windows-update-error-0x800f0922-on-windows-10/) covers the same ground with Windows 10's menus for mixed-OS households.

## Closing

Error 0x800F0922 rewards a diagnostic mindset: check the VPN first, then Secure Boot and EFI space, then servicing health. Most cases resolve in the first three fixes — a disconnected VPN, a cleaned EFI partition, or an updated bootloader. The servicing repairs stand behind them for the cases where CBS data itself is damaged. Identify which layer is failing and the fix is usually straightforward.
