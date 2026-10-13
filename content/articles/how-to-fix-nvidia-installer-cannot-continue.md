---
title: "How to Fix ‘NVIDIA Installer Cannot Continue’ on a Windows Laptop"
slug: "how-to-fix-nvidia-installer-cannot-continue"
date: "2026-09-11"
categories: ["drivers"]
tags: ["nvidia driver", "installer error", "geforce", "graphics driver"]
description: "Stuck on the ‘NVIDIA Installer cannot continue’ error? Here are the proven fixes — from clean installs to compatibility tweaks — that get GeForce drivers installing on Windows laptops."
thumbnail: "/images/thumbs/how-to-fix-nvidia-installer-cannot-continue.webp"
faqs:
  - q: "Why does the NVIDIA installer say it cannot continue on my laptop?"
    a: "The most common reasons are installing a desktop GPU driver on a laptop GPU, leftover files from a previous driver conflicting with the new one, or a Windows build older than the driver requires. Downloading the correct notebook driver package and choosing the clean-install option fixes it in most cases."
  - q: "Should I use DDU to fix NVIDIA installer errors?"
    a: "Display Driver Uninstaller is the most thorough option when the standard clean install fails. Run it from Safe Mode to remove every trace of the old driver, then install the fresh package immediately. It is safe when used correctly and is the standard technician approach for stubborn installer failures."
  - q: "Can antivirus software block NVIDIA driver installation?"
    a: "Yes. Third-party antivirus real-time protection can quarantine installer components or block driver service registration, causing the installer to abort. Temporarily disable real-time protection during the installation and re-enable it right after. Windows Defender rarely causes this problem, and adding the installer to exclusions is an alternative."
  - q: "Do I need to update Windows before installing NVIDIA drivers?"
    a: "Often, yes. Current NVIDIA drivers require a minimum Windows 10 or 11 build, and the installer checks your OS version explicitly. If your laptop has been offline or updates have been paused, install all pending Windows updates first, then retry the driver installation."
---

Few errors are as stubborn as 'NVIDIA Installer cannot continue.' It appears at the end of a GeForce driver installation, offers no useful detail, and leaves you with no driver or a half-installed one. On laptops it is especially common because mobile GPUs face stricter hardware checks — the installer verifies your exact GPU, BIOS, and Windows build.

The error has a short list of well-understood causes: usually a leftover driver conflicting with the new one, a desktop GPU driver installed on a laptop GPU, or a Windows build older than the driver requires.

Confirm you are installing the correct package: notebook drivers for mobile GPUs from [NVIDIA's official driver page](https://www.nvidia.com/Download/index.aspx) — the desktop package fails the hardware check on laptops every time. Our [clean-install guide](/articles/how-to-update-nvidia-drivers-clean-install-in-windows-11-24h2/) covers the full process.

## Why this happens

- ****Wrong driver package for your GPU**:** Desktop GeForce drivers fail the hardware check on laptop GPUs and vice versa — even installing a standard driver on a DCH-only system triggers the error.
- ****Leftover files from a previous installation**:** Partially uninstalled drivers leave registry entries and system files that make the new installer believe an incompatible version is still active.
- ****Windows build too old for the driver**:** Recent NVIDIA drivers require a minimum Windows 10 or Windows 11 build. An outdated, long-unpatched system fails the installer's OS check.
- ****Antivirus or security software blocking the install**:** Real-time protection can quarantine installer components or block the driver service registration mid-install.
- ****Corrupted installer download**:** Large driver packages sometimes download with bit errors, especially over unstable Wi-Fi. The installer detects the damage and aborts.
- ****Disabled NVIDIA services or conflicting GPU software**:** If NVIDIA Display Container or related services are disabled, or another GPU utility is fighting for control, the installer cannot complete registration.
- ****BIOS or firmware incompatibility**:** On some laptops, an outdated system BIOS misreports the GPU's device ID, so the installer concludes your hardware is not supported.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Download the Correct Laptop Driver Package

On NVIDIA's driver download page, select your exact product: GeForce, the correct series (e.g. GeForce RTX 40 Series Notebooks), your GPU, and Windows 11 64-bit. Most modern laptops need the DCH driver type, not the standard one.

Also verify your Windows build meets the driver's minimum requirement, listed in the release notes. A laptop still on an early Windows 11 build may need a Windows update before a current GeForce driver will install.

1. 1. Open NVIDIA's official driver download page.
2. 2. Select GeForce, your series with 'Notebooks' in the name, and your GPU.
3. 3. Choose the DCH driver type for Windows 11 64-bit.
4. 4. Compare your Windows build against the driver's minimum requirement.
5. 5. Download the full package — do not use a third-party mirror.

### Fix 2: Perform a Clean Installation

The NVIDIA installer itself offers a clean-install option that removes the old driver before installing the new one. Run the installer, choose Custom (Advanced) instead of Express, tick 'Perform a clean installation,' and continue. This wipes the previous driver's files, registry entries, and profiles, eliminating the conflicts that cause the 'cannot continue' error.

If the installer will not even reach the custom-install screen, remove the existing driver first through Device Manager or Apps settings, restart, and then run the installer again.

1. 1. Run the NVIDIA installer and select Custom (Advanced).
2. 2. Tick the box for Perform a clean installation.
3. 3. Complete the installation and restart when prompted.
4. 4. If the installer aborts early, uninstall the old driver first via Settings, Apps.
5. 5. Run the installer again after the reboot.

### Fix 3: Use Display Driver Uninstaller in Safe Mode

When the standard clean install is not enough, Display Driver Uninstaller (DDU) removes every trace of the GPU driver from Safe Mode, where Windows cannot lock the files. This is the option technicians reach for when the installer repeatedly refuses to continue.

Boot into Safe Mode, run DDU, select GPU and NVIDIA, and choose 'Clean and restart.' After the reboot, install the freshly downloaded driver package before Windows Update has a chance to install its own version.

1. 1. Download DDU and the correct NVIDIA driver package first.
2. 2. Boot Windows into Safe Mode.
3. 3. Run DDU, select GPU then NVIDIA, and choose Clean and restart.
4. 4. After reboot, run the NVIDIA installer immediately.
5. 5. Choose Custom install with the clean-install checkbox ticked.

### Fix 4: Temporarily Disable Antivirus and Disconnect Extras

Third-party antivirus suites are a documented cause of aborted NVIDIA installations. Temporarily disable real-time protection, run the installer, and re-enable protection as soon as the install completes.

Also unplug external monitors and docks during the installation. Multi-display setups with active DisplayLink or USB-C dock drivers occasionally interfere with the installer's display detection step.

1. 1. Temporarily disable your third-party antivirus real-time protection.
2. 2. Unplug external monitors, docks, and USB display adapters.
3. 3. Run the NVIDIA installer as administrator (right-click, Run as administrator).
4. 4. Complete the installation and restart.
5. 5. Re-enable antivirus protection immediately afterward.

### Fix 5: Update Windows to a Supported Build

Open Settings, Windows Update, and install all pending updates. Current NVIDIA drivers require a recent Windows 11 build, and the installer checks your OS version explicitly — a long-unpatched laptop fails this check.

If Windows Update itself is stuck, run the Windows Update troubleshooter first. In rare cases you may need to install the latest servicing stack update manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) before the feature updates will flow.

1. 1. Open Settings and go to Windows Update.
2. 2. Click Check for updates and install everything offered.
3. 3. Restart and check for updates again until fully current.
4. 4. Retry the NVIDIA installer.
5. 5. If updates fail, run the Windows Update troubleshooter first.

### Fix 6: Re-enable NVIDIA Services

In services.msc, find the NVIDIA services — particularly NVIDIA Display Container LS and NVIDIA LocalSystem Container. If any are disabled, set them to Automatic and start them; the installer depends on them to register the new driver.

While you are there, check that the Windows Installer service is running. Some 'cannot continue' failures are actually Windows Installer problems wearing an NVIDIA mask.

1. 1. Press Windows key + R, type services.msc, and press Enter.
2. 2. Find the NVIDIA Display Container and LocalSystem Container services.
3. 3. Set any disabled ones to Automatic and start them.
4. 4. Confirm the Windows Installer service is running.
5. 5. Run the NVIDIA installer again.

### Fix 7: Update the System BIOS

As a last resort, check your laptop maker's support site for a BIOS update. On certain models, an old BIOS misreports the mobile GPU's hardware ID, so the installer concludes your GPU is unsupported — a BIOS update corrects the identification.

This is uncommon but worth checking when every driver-level fix has failed. Follow the maker's BIOS update instructions exactly with the charger connected. If drivers install but then crash, see our [display driver recovery guide](/articles/how-to-fix-display-driver-stopped-responding-after-windows-11-update/).

1. 1. Visit your laptop maker's support site and find your model.
2. 2. Compare your current BIOS version against the latest release.
3. 3. Download and run the BIOS update with the charger connected.
4. 4. Do not interrupt the update for any reason.
5. 5. Retry the NVIDIA driver installation after the BIOS flash.

## Closing

The 'NVIDIA Installer cannot continue' error looks cryptic, but it is almost always one of three things: the wrong package, leftover driver debris, or an outdated Windows build. Start with the correct laptop driver and a clean install, escalate to DDU in Safe Mode if needed, and save the BIOS update for last.
