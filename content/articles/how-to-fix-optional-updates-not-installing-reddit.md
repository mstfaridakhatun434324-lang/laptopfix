---
title: "Optional Updates Not Installing? Fix It on Windows 11"
slug: "how-to-fix-optional-updates-not-installing-reddit"
date: "2026-09-26"
categories: ["windows-update"]
tags: ["windows update", "optional updates", "drivers", "not installing"]
description: "Optional updates won't install on your Windows 11 laptop? Learn why driver and optional updates fail and how to get them installed properly."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-reddit.webp"
faqs:
  - q: "What are optional updates in Windows 11?"
    a: "Optional updates are driver updates, firmware packages, and non-security quality updates that Microsoft offers but does not install automatically. They appear under Settings, Windows Update, Advanced options, Optional updates. They are called optional because Windows considers them non-critical, but they often contain important driver fixes, so installing relevant ones is good maintenance."
  - q: "Should I install all optional updates?"
    a: "Install optional updates selectively. Driver updates for hardware you actually use, such as Wi-Fi, Bluetooth, and graphics, are usually worth installing. Skip updates for hardware you do not have or features you do not use. If your laptop runs perfectly, there is no obligation to install any of them, but do not ignore a driver update that addresses a problem you are experiencing."
  - q: "Why do optional driver updates fail more often than regular updates?"
    a: "Optional driver updates fail more often because drivers interact directly with hardware, and mismatches between the offered driver and your specific hardware revision cause installation errors. Manufacturer utilities like Dell Update or Lenovo Vantage may also hold locks on the same drivers. Getting drivers from the manufacturer's own tool first usually succeeds where the optional update fails."
  - q: "Can a failed optional update harm my laptop?"
    a: "Rarely. A failed optional update typically rolls back cleanly and leaves your existing driver in place, so the only cost is time. In uncommon cases a partially installed driver can cause device issues, which Device Manager's Roll Back Driver option fixes. The fixes in this guide minimize even these rare outcomes by ensuring clean installation conditions."
---
Optional updates sit in a quiet corner of Windows Update, offering driver refreshes and firmware packages that never install on their own. When you finally open that list and try to install them, only to watch them fail, it is annoying in a particular way: these were supposed to be the easy, low-stakes updates. The failures usually have mundane causes, and the fixes are straightforward once you know where optional updates differ from regular ones.

The key difference is that optional updates are mostly drivers, and drivers touch hardware directly. A driver package built for a slightly different hardware revision, a manufacturer utility holding the same driver files open, or a device that is currently in use can all abort the install. Windows is also less aggressive about retrying optional updates, so a transient failure can sit there indefinitely until you intervene.

This guide walks you through seven fixes for optional updates that will not install, from the simple retry through manufacturer driver tools to manual installation. If the main cumulative updates are failing too, start with our [cumulative update failure guide](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) since the underlying machinery is shared.

## Why this happens

- **Hardware revision mismatch:** The offered driver targets a different revision of the component than you have.
- **Manufacturer utility locks:** Dell Update, Vantage, or HP tools may hold the same driver files.
- **Device in use:** Drivers for active devices sometimes cannot update while the device is busy.
- **Corrupted optional update cache:** Damaged metadata or payloads in the download cache.
- **Outdated firmware dependency:** Some driver updates require a minimum BIOS version first.
- **Stalled update service:** Wedged Windows Update components affect optional updates too.
- **Already-newer driver installed:** A manually installed newer driver can block the older optional one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Retry selectively and note which ones fail

Not all optional updates matter equally. Identify the failures worth fixing.

1. Open Settings, Windows Update, Advanced options, Optional updates.
2. Expand Driver updates and note exactly which ones fail.
3. Try installing them one at a time instead of all at once.
4. Record the error message or code for the ones that fail.
5. Skip updates for hardware you do not use; focus on the relevant ones.

### Fix 2: Get the driver from the manufacturer instead

Manufacturer tools deliver drivers tested for your exact model, often newer than the optional update.

1. Open your manufacturer's utility: Dell Update, Lenovo Vantage, or HP Support Assistant.
2. Check for driver updates and install what it offers.
3. Alternatively, visit the vendor support site with your model number.
4. Install the manufacturer's driver for the failing device.
5. Return to Optional updates; the entry often disappears once a current driver is installed.

Dell owners can use https://www.dell.com/support and Lenovo owners https://support.lenovo.com/us/en/.

### Fix 3: Update the device manually through Device Manager

Target the specific failing device directly for precise control.

1. Open Device Manager and find the device matching the failed update.
2. Right-click it and choose Update driver, then Search automatically.
3. If that fails, choose Browse my computer and Let me pick, selecting a compatible driver.
4. Restart after the driver installs.
5. Verify the device works and the optional update no longer fails.

### Fix 4: Run the Windows Update troubleshooter

Clear service-level issues affecting the optional update pipeline.

1. Go to Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart the laptop.
4. Retry the optional updates one at a time.

### Fix 5: Reset the update cache

Remove corrupted optional update payloads and metadata with a clean reset.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
4. Run `ren C:\Windows\System32\catroot2 catroot2.old`.
5. Restart the services and reboot.
6. Revisit Optional updates and retry the failing entries.

### Fix 6: Check for firmware prerequisites

Some driver updates need a minimum BIOS version. Check yours.

1. Run `msinfo32` and note your BIOS version and date.
2. Compare it against the latest on your manufacturer's support site.
3. Flash the BIOS update on AC power if yours is outdated.
4. Restart and retry the optional driver update.
5. Driver installs that failed for months often succeed after the firmware catches up.

### Fix 7: Install the driver manually from the vendor

When all automated paths fail, download the driver package directly.

1. Identify the exact device and hardware ID in Device Manager, Details tab.
2. Search the vendor support site for that device's driver package.
3. Download and run the installer as administrator.
4. Restart and confirm the device functions correctly.
5. The optional update entry should clear on the next check.

For related driver servicing problems, see our guide on [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/).

### Fix 8: Install the vendor driver in compatibility mode

Some older driver packages fail on Windows 11 because their installers check the OS version too strictly. Running the manufacturer's driver installer in compatibility mode for an earlier Windows version bypasses these artificial blocks while installing the exact same driver files. This trick rescues optional driver updates whose vendor packages predate Windows 11 but remain the correct drivers for your hardware.

1. Download the driver package from your laptop manufacturer's support site.
2. Right-click the installer executable and choose Properties.
3. Open the Compatibility tab and check Run this program in compatibility mode.
4. Select Windows 8 or Windows 10 from the dropdown menu.
5. Check Run this program as an administrator, then apply and launch the installer.
6. Restart after installation and confirm the device works in Device Manager.

## Closing

Optional updates fail for driver-specific reasons: revision mismatches, manufacturer utility conflicts, or missing firmware prerequisites. The most reliable fix is usually getting the driver from your laptop maker's own tool rather than fighting the optional update entry. Install the optional updates that matter for your hardware, skip the rest without guilt, and your laptop stays current where it counts.
