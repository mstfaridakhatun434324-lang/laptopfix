---
title: "KERNEL_SECURITY_CHECK_FAILURE on HP Laptops: Fix Guide"
slug: how-to-fix-kernel-security-check-failure-on-hp-laptop
date: 2026-09-28
categories: ["windows-errors"]
tags: ["bsod", "kernel-security-check-failure", "hp-laptop"]
description: "KERNEL_SECURITY_CHECK_FAILURE on your HP laptop is usually a driver or corrupt file issue. Here's the exact fix order that works."
thumbnail: "/images/thumbs/how-to-fix-kernel-security-check-failure-on-hp-laptop.webp"
faqs:
  - q: "What does KERNEL_SECURITY_CHECK_FAILURE mean?"
    a: "It is a blue screen stop code (0x00000139) triggered when the Windows kernel detects corruption in a data structure it depends on. On HP laptops the usual triggers are a faulty driver, corrupted system files, or failing RAM."
  - q: "Why does it happen on HP laptops specifically?"
    a: "It is not HP-specific, but HP's broad hardware lineup means driver mismatches are common — Windows Update installing a generic driver over an HP-validated one is a classic trigger for this stop code."
  - q: "Can HP's built-in diagnostics help?"
    a: "Yes. Pressing F2 during boot opens HP's UEFI diagnostics, which test memory, drive, and system board quickly. A clean bill of health there points you at drivers and software instead of hardware."
  - q: "Will I lose my files fixing this?"
    a: "No. The standard fixes — SFC, DISM, driver updates, memory tests — do not touch personal files. Only a full reset with the remove-everything option deletes data, and that is the last resort."
---

`KERNEL_SECURITY_CHECK_FAILURE` — stop code `0x00000139` — means the Windows kernel caught one of its critical data structures in a corrupted state and crashed before the corruption could do real damage. It sounds severe, and the name is intimidating, but the causes are familiar: a bad driver, damaged system files, or flaky memory.

On HP laptops there is a recurring theme worth knowing about. HP ships model-specific drivers, and Windows Update has a habit of replacing them with generic versions that do not quite fit — and that mismatch is a textbook trigger for this exact stop code. It is also why the crashes sometimes start on a Tuesday morning with no warning: Patch Tuesday delivered a driver overnight. Here is how to fix it, in order.

## Why this happens

- **A driver passes corrupted data to the kernel.** The most common trigger — network, graphics, or storage drivers feeding the kernel bad structures.
- **Windows Update replaced an HP driver with a generic one.** Extremely common on HP laptops and a top cause of this specific stop code.
- **Corrupted system files.** A bad update or hard shutdown damages core files the kernel validates.
- **Faulty RAM.** Bad memory corrupts kernel data structures in transit.
- **Outdated HP BIOS.** Old firmware misreports hardware tables to Windows 11.
- **Conflicting security software.** Kernel-level antivirus filters clash with updated system files.
- **Failing storage drive.** Bad sectors corrupt driver and system files silently.

## How to fix it

Work through these in order, from least to most invasive. Most HP owners fix this without ever reinstalling Windows — the driver and file-repair steps resolve the large majority of cases, so start there with full confidence.

### Fix 1: Run HP's UEFI hardware diagnostics

Start with hardware — HP makes this easy and it runs outside Windows.

1. Shut down completely, then power on while tapping **F2** repeatedly.
2. Select **Component Tests** and run the **Memory** test first, then the **Hard Drive** test.
3. If either fails, you have a hardware answer — contact HP support with the failure code for warranty service.
4. If both pass, continue below — the problem is software. HP's [support site](https://support.hp.com/us-en) takes your serial number for drivers and warranty checks.

### Fix 2: Repair system files with SFC and DISM

Corrupted system files are the quickest software win.

1. Open an elevated Command Prompt (**Start** > type `cmd` > right-click **Command Prompt** > **Run as administrator**).
2. Run `sfc /scannow` and let it finish completely.
3. Then run `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Restart and use the laptop for a day. A large share of `0x139` crashes end here.
5. Microsoft documents both tools on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 3: Install HP-validated drivers for your exact model

Replace any generic Windows Update drivers with HP's tested versions.

1. Find your exact model and product number on the sticker under the laptop.
2. Go to [HP Support](https://support.hp.com/us-en), enter your model, and open **Software and Drivers**.
3. Download the latest **chipset**, **graphics**, **network**, and **storage** drivers.
4. Install the chipset driver first, then the rest, restarting between major installs.
5. If the crashes began after a specific driver update, install the previous version from HP's site instead of the newest.

### Fix 4: Stop Windows Update from swapping the drivers back

The fix in Fix 3 only sticks if Windows stops "helpfully" replacing your drivers.

1. After installing the good HP drivers, open **Settings** > **Windows Update** > **Advanced options**.
2. Review **Optional updates** carefully — uncheck driver updates for devices you just fixed.
3. For a stronger block, use Microsoft's **Show or hide updates** troubleshooter to hide the specific driver update.
4. Going forward, update these devices only from HP's site.
5. This same generic-driver problem causes the [DRIVER_IRQL_NOT_LESS_OR_EQUAL](/articles/how-to-fix-driver-irql-not-less-or-equal-on-hp-laptop/) stop code on HP machines, so the habit protects you twice.

### Fix 5: Test the RAM

When crashes feel random and frequent, memory is a prime suspect.

1. Press `Win + R`, type `mdsched.exe`, and press **Enter**.
2. Choose **Restart now and check for problems** and let the full pass run.
3. Check results in **Event Viewer** > **Windows Logs** > **System** for `MemoryDiagnostics-Results`.
4. If errors appear, reseat the RAM sticks and retest; replace any stick that still errors.
5. Test one stick at a time on models with two slots to isolate the faulty one.

### Fix 6: Remove conflicting low-level software

Kernel hooks from third-party tools trip the security check even with good drivers.

1. Open **Settings** > **Apps** > **Installed apps**.
2. Uninstall third-party antivirus, disk utilities, VPN clients, and system optimizers added recently.
3. Check **HP Wolf Security** settings if installed — its kernel components have clashed with Windows updates before.
4. Restart and test for a few days with only Windows Security active.
5. Reinstall needed software one at a time from the latest versions.

### Fix 7: Update the BIOS and reset as a last resort

Firmware first, then the nuclear option.

1. Check your BIOS version with `msinfo32` and download the latest for your exact model from HP support.
2. Flash it with the charger plugged in; do not interrupt the process.
3. Load BIOS defaults afterward unless you need specific settings.
4. If crashes persist, go to **Settings** > **System** > **Recovery** > **Reset PC** > **Keep my files**.
5. After the reset, install HP drivers before Windows Update touches anything — then apply the Fix 4 block immediately.

## Closing

`KERNEL_SECURITY_CHECK_FAILURE` on an HP laptop usually means a driver fed the kernel bad data — and on HP machines, that driver is often a generic Windows Update replacement for an HP-validated original. Repair the system files, install the right HP drivers, stop Windows from swapping them back, and test the RAM if the crashes feel random. That sequence resolves this stop code for the vast majority of HP owners without a reinstall. The general Windows 11 version of this fix is covered in our [KERNEL_SECURITY_CHECK_FAILURE guide](/articles/how-to-fix-kernel-security-check-failure-on-windows-11/).
