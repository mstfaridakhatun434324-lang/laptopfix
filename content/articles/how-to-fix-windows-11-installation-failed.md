---
title: "How to Fix Windows 11 Installation Failed Errors"
slug: how-to-fix-windows-11-installation-failed
date: 2026-09-19
categories: ["windows-errors"]
tags: ["installation failed", "Windows 11", "setup error"]
description: "Windows 11 installation keeps failing? Diagnose setup errors, fix driver and disk blockers, and complete the install successfully."
thumbnail: "/images/thumbs/how-to-fix-windows-11-installation-failed.webp"
faqs:
  - q: "Why does my Windows 11 installation keep failing?"
    a: "The most common blockers are incompatible drivers (especially storage and graphics), insufficient disk space, corrupted installation media, BIOS settings like Secure Boot or TPM being off, and connected peripherals loading conflicting drivers. The setup logs in C:\\$Windows.~BT\\Sources\\Panther usually name the specific failure, which is far more useful than the generic error message."
  - q: "How much free space does Windows 11 installation need?"
    a: "Microsoft requires 64 GB of storage for Windows 11, but the installer works far more reliably with breathing room — aim for at least 20 to 30 GB free beyond your data on the target drive. The setup stages files, keeps a rollback copy, and needs temporary space during driver migration. Clean installs on cramped drives fail more often than people expect."
  - q: "Can I install Windows 11 without TPM 2.0 and Secure Boot?"
    a: "Officially, no — Windows 11 requires TPM 2.0 and Secure Boot, and the installer checks for them. There are registry workarounds that bypass the checks, but Microsoft does not support those installations and they may miss updates or have stability issues. The supported path is enabling TPM and Secure Boot in your BIOS, which most laptops from the last several years support."
  - q: "Should I disconnect USB devices during installation?"
    a: "Yes. External drives, printers, USB hubs, and dongles load extra drivers during setup, and any conflicting one can abort the installation. Disconnect everything except the installation USB, charger, keyboard, and mouse. This simple step resolves a meaningful share of mysterious setup failures."
---

"Windows 11 installation has failed" is the message nobody wants after watching a progress bar for an hour. Whether you are upgrading from Windows 10 or doing a clean install, the failure usually happens late — during the driver migration or finalization phase — and Windows rolls everything back, leaving you where you started with no clear explanation.

The causes are a familiar lineup: a driver that fights the new build, not enough disk space, bad installation media, BIOS settings the installer dislikes, or a peripheral injecting a conflicting driver. Work through the checklist below before your next attempt, and read the setup logs if it fails again — they almost always name the culprit.

## Why this happens

- **Incompatible storage or chipset drivers.** Old AHCI/RAID/NVMe drivers crash setup during driver migration.
- **Insufficient disk space.** The installer needs room for staging, temp files, and a rollback copy.
- **Corrupted installation media.** A bad USB write or incomplete ISO download fails integrity checks mid-install.
- **TPM or Secure Boot disabled.** The installer blocks or misbehaves when requirements are not met.
- **Connected peripherals.** External devices load drivers that conflict with setup.
- **Failing drive.** Bad sectors cause file-copy failures the installer cannot recover from.

## How to fix it

Work through these in order, testing a normal boot after each one.

### Fix 1: Meet the requirements — TPM, Secure Boot, and specs

1. Press `Win + R`, type `tpm.msc`, and confirm it reports **TPM 2.0** ready for use.
2. Restart into the BIOS (**F2**/**Del**) and enable **TPM**/**PTT** and **Secure Boot** if they are off.
3. While in the BIOS, set SATA mode to **AHCI** unless you specifically need RAID.
4. Verify 4 GB RAM and 64 GB storage minimums — and realistically, much more free space than the minimum.
5. Retry the installation.

### Fix 2: Free disk space and disconnect peripherals

1. Aim for 30 GB+ free on the target drive; run **Disk Cleanup** with system files and move personal data elsewhere.
2. Unplug all USB devices except the installation media, keyboard, and mouse.
3. Disconnect external monitors if possible — display driver conflicts during setup are real.
4. Retry the installation.

### Fix 3: Recreate the installation media cleanly

Bad media causes a large share of failures.

1. Download a fresh ISO from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create the USB with the official **Media Creation Tool** or Rufus — do not reuse a years-old USB stick without rewriting it.
3. Use a USB port directly on the laptop, not a hub.
4. Boot from the USB and retry.

### Fix 4: Update the BIOS and key drivers first

1. Update the BIOS from the manufacturer's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) with the charger connected.
2. In your current Windows, update chipset, storage, and graphics drivers from manufacturer sources before upgrading.
3. Uninstall third-party antivirus completely — its filter drivers are a known setup blocker.
4. Retry the installation.

### Fix 5: Read the setup logs after a failure

Stop guessing; the logs name the failure.

1. After a rollback, open `C:\$Windows.~BT\Sources\Panther\` (show hidden items in File Explorer's **View** menu).
2. Open **setuperr.log** and read the last entries — they typically name a driver or failing phase.
3. Common finds: storage driver names (update them), error 0xC1900101 codes (driver conflict — treat per our upgrade-error guidance), disk errors (check the drive).
4. Fix what the log names, then retry.

### Fix 6: Check the drive health

1. Open **Command Prompt (Admin)** and run `chkdsk C: /f /r`, letting it complete on restart.
2. Check SMART status with the drive maker's tool or `wmic diskdrive get status`.
3. If the drive is failing, replace it before installing — no setup survives bad sectors in system areas.

### Fix 7: Do a true clean install instead of an upgrade

When upgrades keep failing, wiping the slate works.

1. Back up everything to an external drive.
2. Boot from the installation USB, choose **Custom: Install Windows only**.
3. Delete the old partitions on the target drive and install to the unallocated space.
4. After installation, install drivers from the laptop manufacturer's site before connecting extra peripherals.

Brand-specific walkthroughs exist for the same failure: [installation failed on Dell](/articles/how-to-fix-windows-11-installation-failed-on-dell-laptop/), and the step-by-step [installation troubleshooting guide](/articles/how-to-fix-windows-11-installation-failed-step-by-step/). If setup completes but updates then fail, see [error 0x80070002](/articles/how-to-fix-windows-11-install-error-0x80070002-on-lenovo-laptop/).

### Fix 8: Strip the system to essentials and check for extra drives

Multiple drives and RAID configurations complicate setup's disk handling.

1. If the laptop has two drives, physically disconnect the secondary one during installation (on desktops; on laptops, disable it in the BIOS if possible).
2. In the BIOS, confirm the target drive is first in the boot order and that no stale boot entries point at removed drives.
3. If you previously used RAID mode, switching to AHCI requires the OS-side driver change first — otherwise setup cannot see the drive correctly.
4. With a single visible target drive and clean boot order, run setup again.
5. If setup still fails at the same phase, compare against the setuperr.log from the previous attempt — an identical failure point means the trigger was not the drive configuration, so return to the driver and media checks.

## Closing

Failed Windows 11 installations are almost never mysterious once you check the basics: requirements met, space free, peripherals unplugged, media freshly written, drivers current. The setup log is the difference between a third failed attempt and a successful one — read it before retrying. And when upgrades stubbornly refuse, a clean install with proper backups is not defeat; it is the fastest path to a healthy system. Most failed installs I have seen came down to one skipped basic, usually the media or a forgotten USB device, so run the checklist honestly before assuming something exotic. Patience here saves hours: one careful attempt beats three rushed ones.
