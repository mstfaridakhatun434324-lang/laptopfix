---
title: "DRIVER_VERIFIER_IOMANAGER_VIOLATION: What the Fix Really Is"
slug: how-to-fix-driver-verifier-iomanager-violation-reddit
date: 2026-09-15
categories: ["windows-errors"]
tags: ["bsod", "driver-verifier", "iomanager"]
description: "DRIVER_VERIFIER_IOMANAGER_VIOLATION means a driver broke I/O rules under Verifier. Here's how to find it, fix it, and stop the crashes."
thumbnail: "/images/thumbs/how-to-fix-driver-verifier-iomanager-violation-reddit.webp"
faqs:
  - q: "What does DRIVER_VERIFIER_IOMANAGER_VIOLATION mean?"
    a: "It is a blue screen stop code (0x000000C9) raised when Driver Verifier catches a driver violating I/O Manager rules — mishandling IRPs, completing requests incorrectly, or breaking plug-and-play protocols. The driver is misbehaving at the I/O layer."
  - q: "Is this different from DRIVER_VERIFIER_DETECTED_VIOLATION?"
    a: "Yes, but they are cousins. DETECTED_VIOLATION (0xC4) covers general driver rule-breaking like memory misuse, while IOMANAGER_VIOLATION (0xC9) specifically covers I/O request handling. The fix process — identify the driver, update or remove it, disable Verifier — is the same."
  - q: "Why do forum posts say to just disable Driver Verifier?"
    a: "Because disabling Verifier with verifier /reset stops the crashes instantly, which looks like a fix. It is really just removing the referee. The bad driver remains and can cause silent data corruption. Always identify the driver first."
  - q: "Which drivers usually trigger this?"
    a: "Storage controller drivers, USB drivers, virtual disk tools, disk encryption filters, and virtualization software. Anything that processes I/O request packets (IRPs) is in the blast radius — which is why storage and USB drivers top the list."
---

`DRIVER_VERIFIER_IOMANAGER_VIOLATION` — stop code `0x000000C9` — is Driver Verifier catching a driver breaking the I/O Manager's rules. Every I/O operation in Windows travels as an I/O Request Packet (IRP) through a strict protocol, and when a driver mishandles one — completes it wrong, leaks it, or violates plug-and-play sequencing — Verifier crashes the system deliberately.

You will see a lot of forum advice that boils down to "just turn off Driver Verifier." That stops the crashes, but it is the equivalent of unplugging a smoke detector. The driver is still broken. Here is how to actually fix it: find the driver, deal with it, and *then* turn Verifier off.

## Why this happens

- **Driver Verifier is monitoring I/O with strict checks enabled.** The I/O Verification option specifically watches IRP handling, and this stop code only fires when it is active.
- **A storage or USB driver mishandles IRPs.** The most common trigger — storage controller, USB host, and NVMe drivers that complete requests incorrectly.
- **Disk encryption or virtual disk filters.** Third-party encryption, backup, and virtual-drive tools insert filter drivers into the I/O stack that frequently violate the rules.
- **Virtualization software drivers.** Hypervisors and emulators that virtualize storage or USB devices are classic offenders.
- **A recent driver or software update introduced the bug.** New versions of storage utilities and disk tools sometimes ship with I/O violations.
- **Corrupted driver binaries.** Damaged files on disk cause erratic I/O behavior that Verifier flags.

## How to fix it

Work through these in order, from least to most invasive. Identify the driver first — everything else follows from that.

### Fix 1: Read the minidump to name the violating driver

The dump is the entire point of running Verifier, so extract the answer from it.

1. Press `Win + R`, type `%SystemRoot%\Minidump`, and press **Enter**.
2. Open the newest `.dmp` in **WinDbg Preview** (free from the Microsoft Store).
3. Run `!analyze -v` and read `MODULE_NAME` and `IMAGE_NAME`.
4. Typical offenders: `stornvme.sys` or vendor NVMe drivers, `USBXHCI.SYS` (USB), `vhdmp.sys` (virtual disks), or a third-party filter like an encryption driver.
5. If the dump names a filter driver, the *software that installed it* is what you need to update or remove — note the vendor.
6. The dump-reading steps mirror our [DRIVER_VERIFIER_DETECTED_VIOLATION guide](/articles/how-to-fix-driver-verifier-detected-violation-youtube/) if you want a second walkthrough.

### Fix 2: Update the storage and chipset drivers

Storage drivers are the top category for this stop code, so update them from the right source.

1. Open **Device Manager** and expand **Storage controllers** and **IDE ATA/ATAPI controllers**.
2. Right-click each controller and choose **Update driver** > **Search automatically for drivers**.
3. Better: download the latest **chipset** and **storage/NVMe** drivers from your laptop maker's support page for your exact model.
4. For Intel platforms, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) finds the correct chipset and Rapid Storage drivers automatically.
5. Restart and test with disk-heavy activity — large file copies, for example — since I/O violations surface under I/O load.

### Fix 3: Remove or update disk utilities and encryption tools

Filter drivers from third-party disk software are disproportionately represented in `0xC9` dumps.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Look for disk encryption tools, virtual drive software, disk imagers, "SSD optimizers," and old backup programs.
3. Uninstall the one matching the dump's driver, or update it to the latest version if you need it.
4. Use the vendor's clean-removal tool when available — filter drivers often survive ordinary uninstalls.
5. Restart and confirm the crashes stop before reinstalling anything.

### Fix 4: Disable virtualization-related drivers temporarily

If the dump points at a hypervisor or emulator driver, test without it.

1. Uninstall or disable the virtualization software (VMware, VirtualBox, Android emulators) temporarily.
2. In **Windows Features** (`optionalfeatures`), you can also toggle **Hyper-V** and **Virtual Machine Platform** off for testing.
3. Restart and use the laptop normally for a few days.
4. If crashes stop, reinstall the virtualization software at its latest version — older releases have known I/O violations on Windows 11.
5. Re-enable Hyper-V features afterward if you need them.

### Fix 5: Roll back the driver if the violation is new

A driver update that introduced the violation should simply be undone.

1. In **Device Manager**, find the device, open **Properties** > **Driver** tab.
2. Click **Roll Back Driver**, choose a reason, and restart.
3. If rollback is greyed out, uninstall the device with driver removal checked and let Windows install its inbox driver.
4. Block the bad version from returning via **Windows Update** > **Advanced options** > **Optional updates** — leave it unchecked.

### Fix 6: Run SFC and DISM, then disable Verifier properly

Clean up system corruption, then retire Verifier now that it has served its purpose.

1. Open an elevated Command Prompt, run `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart, then run `verifier /query` to see what is still being monitored.
3. Run `verifier /reset` to disable all verification and restart again.
4. Confirm with `verifier /query` that nothing is under verification.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents Verifier's options if you ever need to re-enable it for future diagnostics.

### Fix 7: Test the drive hardware

If I/O violations persist across driver changes, the storage hardware itself may be faulting.

1. Run `chkdsk C: /f /r` from an elevated Command Prompt (type **Y** and restart).
2. Check SMART data with CrystalDiskInfo — look for reallocated sectors and overall health.
3. Run your laptop maker's built-in drive diagnostics from the boot menu.
4. A failing SSD under I/O load produces errors that look exactly like driver I/O violations — replace the drive if health is poor.

## Closing

`DRIVER_VERIFIER_IOMANAGER_VIOLATION` means a driver broke the I/O rules and Verifier caught it. The forums are half-right: you *do* end up disabling Verifier — but only after the dump tells you which driver to fix and you have fixed it. Storage drivers, disk utilities, and virtualization filters are the usual suspects. Handle them in that order and this stop code goes away for real, not just until the next bad I/O. Verifier's other memory-focused stop codes, like [SPECIAL_POOL_DETECTED_MEMORY_CORRUPTION](/articles/what-to-do-if-special-pool-detected-memory-corruption/), follow the same identify-fix-disable rhythm.
