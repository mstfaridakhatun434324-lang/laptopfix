---
title: "Windows 11 Installation Failed? 8 Fixes That Actually Work"
slug: how-do-i-fix-windows-11-installation-failed
date: 2026-09-21
categories: ["windows-errors"]
tags: ["windows 11", "installation failed", "setup error", "0x80070002", "upgrade"]
description: "Windows 11 installation keeps failing? Fix setup errors — from 0x80070002 to TPM blocks — with 8 proven steps that actually work."
thumbnail: "/images/thumbs/how-do-i-fix-windows-11-installation-failed.webp"
faqs:
  - q: "Why does my Windows 11 installation keep failing?"
    a: "The top reasons are unmet system requirements (TPM 2.0, Secure Boot), corrupted installation media, insufficient disk space, incompatible drivers, and third-party antivirus interfering with setup. The error code on the failure screen tells you which one — 0x80070002 is usually corrupted files, 0xC1900101 points at drivers."
  - q: "How much free space does Windows 11 setup need?"
    a: "Microsoft requires 64GB of storage, but setup works far more reliably with at least 20–30GB genuinely free on the system drive. If your drive is nearly full, setup fails in confusing ways — free up space first."
  - q: "Can I install Windows 11 without TPM 2.0?"
    a: "Officially no — TPM 2.0 and Secure Boot are hard requirements. Registry bypasses exist online but leave you with an unsupported system that may not receive updates. If your laptop is from 2017 or later, TPM 2.0 is usually present but disabled in BIOS — enable it instead of bypassing."
  - q: "Should I use Windows Update or a USB installer?"
    a: "If Windows Update's upgrade keeps failing, switch to the USB installer from Microsoft's download page — it bypasses many of the failure modes of the in-place upgrade path. For the specific 0x80070002 failure, see our [install error 0x80070002 guide](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/)."
---

A failed Windows 11 installation is frustrating because setup gives you a cryptic error code and rolls everything back, leaving you exactly where you started. But installation failures are highly diagnosable: the error code, the phase it fails in, and your hardware checklist narrow it to a handful of causes.

Work through these in the order given — they go from five-minute checks to the nuclear options.

## Why this happens

- **TPM 2.0 or Secure Boot disabled.** The most common blocker on capable hardware — the features exist but are off in BIOS.
- **Corrupted installation media or download.** A bad USB stick or interrupted download fails mid-setup.
- **Insufficient disk space.** Setup needs breathing room beyond the bare minimum.
- **Incompatible or outdated drivers.** Old storage, graphics, or BIOS versions block the upgrade (0xC1900101 family).
- **Third-party antivirus interfering.** Security suites hook setup operations and cause rollbacks.
- **Failing storage or RAM.** Hardware faults corrupt the installation as it's written.
- **Corrupted EFI system partition.** A damaged or nearly-full EFI partition causes setup to fail at the bootloader stage with misleading error codes.

## How to fix it

Work through these in order — start with Fix 1 and stop when installation succeeds.

### Fix 1: Verify requirements with the PC Health Check

Confirm the basics before anything else.

1. Download Microsoft's **PC Health Check** app and run it — it reports exactly which requirement fails.
2. The usual culprits: TPM 2.0, Secure Boot, CPU generation, 4GB RAM, 64GB storage.
3. If TPM shows as missing, it's almost always just disabled — proceed to Fix 2.
4. If the CPU is genuinely unsupported (pre-8th-gen Intel, pre-Ryzen 2000), the official path ends here.
5. Screenshot or note the results for reference.

### Fix 2: Enable TPM 2.0 and Secure Boot in BIOS

The fix for most "incompatible" reports on modern laptops.

1. Restart and enter BIOS/UEFI (**Del**, **F2**, or **F10**).
2. Find the security section and enable **TPM** (may be called **PTT** on Intel, **fTPM** on AMD) — set it to **2.0** / firmware TPM.
3. Enable **Secure Boot** (you may need to set the OS type to **Windows UEFI mode** first).
4. Ensure the boot mode is **UEFI**, not Legacy/CSM — Windows 11 requires UEFI.
5. Save, exit, and re-run PC Health Check to confirm everything passes.

### Fix 3: Free up disk space and check drive health

Give setup room to work.

1. Open **Settings > System > Storage** and run **Cleanup recommendations** — target at least 25–30GB free.
2. Empty the Recycle Bin, clear **Temporary files**, and move large personal files to external storage.
3. In **Terminal (Admin)**, run `chkdsk C: /f` to fix file-system errors that sabotage setup.
4. Check SMART health with your SSD manufacturer's tool — a failing drive corrupts installations.
5. If the drive is nearly full even after cleanup, consider a larger SSD; it's the most reliable long-term fix.

### Fix 4: Update BIOS and drivers before upgrading

Old firmware is a classic 0xC1900101 trigger.

1. Visit your manufacturer's support page and install the latest BIOS/UEFI for your model (charger plugged in, don't interrupt).
2. Update chipset, storage, and graphics drivers from the same page.
3. Disconnect unnecessary USB devices — printers, docks, and exotic peripherals have all blocked upgrades.
4. If you're upgrading from Windows 10, run Windows Update fully first so the base is current.
5. Retry the installation after the firmware and driver refresh.

### Fix 5: Remove third-party antivirus and clean-boot

Eliminate software interference.

1. Uninstall any third-party antivirus suite completely (use the vendor's removal tool if offered).
2. Uninstall "driver updater" and "PC optimizer" tools — these inject into setup.
3. Disconnect from VPNs and disable third-party firewalls.
4. Perform the upgrade with only Windows Defender active.
5. You can reinstall security software after Windows 11 is running stably. For post-upgrade crash issues, our [blue screen after Windows 11 update guide](/articles/how-to-fix-blue-screen-after-windows-11-update-on-lenovo-laptop/) helps.

### Fix 6: Create fresh installation media

Rule out corrupted setup files.

1. On a working PC, download the **Media Creation Tool** from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Use a USB stick of 8GB or larger — and use a different stick than before if the last attempt failed (sticks do go bad).
3. Let the tool verify and write the media; don't interrupt it.
4. Boot from the USB and choose **Upgrade** (keeps files) or do a clean install if you've backed up.
5. If setup still fails at the same percentage each time, note the exact point — failures at the same spot suggest hardware (Fix 8).

### Fix 7: Run setup with verbose logging

Get the real error instead of a generic code.

1. When setup fails, check `C:\$Windows.~BT\Sources\Panther\setuperr.log` — it logs the actual failure.
2. Common log findings: specific driver blocks (update that driver), disk errors (Fix 3/8), or specific update packages (uninstall them first).
3. Search the log for `0x` error codes and the word "failed" near the end.
4. Address whatever the log names, then retry.
5. This step turns guesswork into a targeted fix.

### Fix 8: Test hardware and clean-install

The final escalation.

1. Test RAM with `mdsched.exe` and the drive with `chkdsk /r` plus SMART data — replace failing parts.
2. Back up everything important to an external drive.
3. Boot from the fresh USB media, delete the old Windows partitions, and clean-install.
4. During setup, install storage drivers via **Load driver** if the drive isn't detected.
5. After installation, get drivers from the manufacturer before restoring files. Microsoft's [installation support](https://support.microsoft.com/en-us/windows) covers edge cases.

## Closing

Windows 11 installation failures are almost never mysterious — they're TPM toggles, tired USB sticks, full drives, or old BIOS versions. The error code and setup log tell you which; this list just makes you check them in the right order. Get the firmware and drivers current, use fresh media, and the install that failed three times usually sails through on the fourth. And once you're running, image the system to an external drive — a known-good backup turns the next failed experiment from a crisis into a twenty-minute restore. If setup fails with 0xC1900101 specifically, the [0xC1900101 install failure guide](/articles/how-to-fix-windows-update-error-0xc1900101-on-laptop/) works through the driver-related side of that error family.
