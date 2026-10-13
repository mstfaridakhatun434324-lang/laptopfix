---
title: "Fix Windows Update Error 0x800F0922 on Windows 10: Causes and Fixes"
slug: how-to-fix-windows-update-error-0x800f0922-on-windows-10
date: 2026-09-04
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x800f0922", "cbs error", "troubleshooting"]
description: "Error 0x800F0922 on Windows 10 points to servicing or boot-file problems. Work through VPN, EFI, and CBS repairs with these Windows 10 steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f0922-on-windows-10.webp"
faqs:
  - q: "What does 0x800F0922 mean on Windows 10?"
    a: "It is a Component-Based Servicing failure, typically occurring when the update cannot verify or stage boot-related files. On Windows 10 the most common triggers are VPN interference during download, a full EFI system partition, Secure Boot conflicts (especially on dual-boot machines), and corrupted servicing data."
  - q: "Why do forums always mention VPN for this error?"
    a: "Because it is a genuinely common trigger. Certain VPN configurations interfere with the way Windows Update downloads and verifies payloads, and the resulting verification failure surfaces as 0x800F0922. Disconnecting the VPN before retrying is the fastest diagnostic test available, which is why experienced troubleshooters suggest it first."
  - q: "Is it safe to clean the EFI partition myself?"
    a: "Yes, if you are careful: only remove bootloader entries you are certain are obsolete (like a Linux install you deleted long ago), and never touch the active Microsoft boot folder. When in doubt, just check how full it is and leave cleanup to the steps in this guide."
  - q: "Does 0x800F0922 mean I need to reinstall Windows?"
    a: "No. This error is fixable in place in the large majority of cases. The VPN test, EFI cleanup, cache reset, and DISM repair resolve it without touching your files or applications. Only if the EFI partition itself is damaged beyond cleanup would deeper boot repairs be needed, and even those preserve your data."
---

Windows 10's version of error 0x800F0922 comes from the same Component-Based Servicing layer as on Windows 11: the update failed during payload verification or boot-file staging. Windows 10 users hit this most often on cumulative updates and on machines with VPN clients, dual-boot setups, or EFI partitions crowded by years of bootloader history. The error code looks intimidating, but the fix list is practical and ordered from quickest test to deepest repair.

Pay attention to timing: if the error appears while the update is still downloading, suspect the VPN or network. If it appears during installation or the reboot phase, suspect the EFI partition, Secure Boot, or servicing data. That single observation cuts the diagnostic work in half.

## Why this happens

- **VPN tunnel interference:** VPNs altering or blocking update payload traffic cause verification failures that surface as this CBS error.
- **Full EFI system partition:** Years of bootloader accumulation on the small EFI partition leaves no room for updated boot files.
- **Secure Boot conflicts:** Unsigned or outdated bootloaders (common on dual-boot systems) fail the update's boot verification.
- **Corrupted CBS/servicing data:** Damaged component store or manifests in the servicing layer.
- **Third-party boot managers:** GRUB, rEFInd, or vendor boot tools conflicting with Windows' boot-file updates.
- **Damaged BCD:** Corrupted boot configuration data failing validation during the update.
- **Antivirus blocking EFI writes:** Security software preventing the update from staging boot files.
- **Corrupted download cache:** Damaged payloads in SoftwareDistribution failing hash verification.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disconnect the VPN and retry the update

The fastest diagnostic test for this error. Do it before anything else.

1. Fully exit your VPN client (disconnecting is not always enough — exit the application).
2. Go to **Settings > Update & Security > Windows Update** and click **Retry**.
3. If the update proceeds, the VPN was interfering. In future, update with the VPN exited, or configure split tunneling to exclude Microsoft update traffic.

### Fix 2: Inspect Secure Boot and the boot setup

Understand your boot environment before attempting repairs.

1. Press **Win + R**, type `msinfo32`, and note the **Secure Boot State**.
2. If you dual-boot, check whether the alternate OS's bootloader is current — outdated GRUB versions are a known trigger.
3. Open **Disk Management** and note the EFI partition's size and how full it appears.
4. Do not permanently disable Secure Boot; it is a security feature, and the real fix is compatible bootloaders, not disabled verification.

### Fix 3: Clean the EFI system partition

Free space for the update's boot-file staging.

1. In **Command Prompt (Admin)**, run `mountvol S: /s` to mount the EFI partition.
2. Browse S: in File Explorer. Look for clearly obsolete entries — for example, a `ubuntu` folder from a Linux install you removed years ago, or duplicated vendor folders.
3. Delete only entries you can positively identify as obsolete. Leave the `Microsoft` folder and anything you are unsure about completely alone.
4. Run `mountvol S: /d` to unmount, restart, and retry the update.

### Fix 4: Reset the Windows Update cache

Eliminate corrupted payloads that fail CBS verification.

1. Open **Command Prompt (Admin)**.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`.
5. Restart, keep the VPN off, and check for updates.

### Fix 5: Repair servicing with DISM and SFC

Fix the CBS layer itself.

1. In **Command Prompt (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Follow with `sfc /scannow`.
3. Restart and retry. These repairs also address [0x80070490 errors](/articles/how-to-fix-windows-update-error-0x80070490-on-windows-10/), which live in the same servicing layer.

### Fix 6: Rebuild the BCD

If the failure is in boot validation, rebuild the boot configuration.

1. Hold **Shift** while clicking **Restart** in the Start menu, then go to **Troubleshoot > Advanced options > Command Prompt**.
2. Run `bootrec /fixmbr` and `bootrec /rebuildbcd`, answering **Y** to add found installations.
3. Exit and boot normally, then retry the update.

### Fix 7: Manual install from the Update Catalog

Bypass the pipeline: find the KB number in update history, download it from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com), and install the `.msu` with the VPN disconnected. If it still fails at the boot phase, the remaining suspects are EFI space and boot validation — revisit Fixes 2, 3, and 6. The [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) has further boot-troubleshooting references.

The VPN angle on this error deserves emphasis because it is so counterintuitive. You would expect a VPN to either work or fail loudly — but certain VPN configurations transparently proxy or re-sign traffic in ways that corrupt the specific payload verification Windows Update performs, producing a CBS error instead of a network error. The maddening part is that everything else works: browsing, streaming, even other downloads. Only the update's integrity check fails. That is why disconnecting and retrying is the first fix rather than the fifth — it eliminates the single most common cause in under two minutes. Similarly, the EFI partition deserves respect disproportionate to its size: 100 MB seemed generous when the partition layout was designed, but years of accumulated bootloaders from dual-boot experiments, vendor utilities, and recovery tools can fill it silently. A quick look with mountvol every year or two prevents the surprise. For Windows 11 machines hitting the same code, our [Windows 11 0x800F0922 guide](/articles/how-to-fix-windows-update-error-0x800f0922-on-windows-11/) mirrors these steps. Both checks together — VPN off, EFI inspected — resolve the large majority of 0x800F0922 cases on Windows 10 without ever touching DISM.

## Closing

On Windows 10, 0x800F0922 is usually the VPN, the EFI partition, or servicing data — in that order of likelihood. The VPN test takes two minutes and resolves a remarkable share of cases; EFI cleanup and DISM handle the rest. Keep the VPN exited during updates and the EFI partition free of fossilized bootloaders, and this error has little reason to return.
