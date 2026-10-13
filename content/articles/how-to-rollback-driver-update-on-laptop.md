---
title: "How to Roll Back a Driver Update on a Windows Laptop"
slug: "how-to-rollback-driver-update-on-laptop"
date: "2026-09-17"
categories: ["drivers"]
tags: ["driver rollback", "device manager", "windows 11", "driver update", "troubleshooting"]
description: "A driver update broke something on your laptop? Learn how to roll back to the previous driver version in Device Manager and stop the bad update returning."
thumbnail: "/images/thumbs/how-to-rollback-driver-update-on-laptop.webp"
faqs:
  - q: "How do I roll back a driver in Windows 11?"
    a: "Open Device Manager, find the device, open its Properties, go to the Driver tab, and click Roll Back Driver. Windows will restore the previously installed version. This works for graphics, audio, network, and most other drivers, but only if a previous version exists on the system. Restart the laptop after the rollback completes."
  - q: "Why is the Roll Back Driver button greyed out?"
    a: "The button is greyed out when Windows has no previous driver version stored. This happens on fresh Windows installs, when the driver was installed with the delete-previous option, or when a cleanup tool removed old driver packages. In that case, download the older driver manually from the manufacturer's support page and install it over the current one."
  - q: "Will Windows reinstall the bad driver after I roll back?"
    a: "It often will, because Windows Update treats drivers as updates to deliver. To prevent this, pause updates temporarily, use the Show or Hide Updates troubleshooter to block the specific driver, or disable automatic driver updates in the advanced system settings. Our guide on [disabling automatic driver updates](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) walks through the options."
  - q: "Is rolling back a driver safe?"
    a: "Yes, rolling back simply restores the driver version that was working before. It does not affect your files or applications. The only risk is losing a fix or feature from the newer driver, which is a worthwhile trade when the new version causes crashes, black screens, or dead hardware."
---

Everything worked until the update. Then the Wi-Fi started dropping, the screen flickered, or the audio crackled, and the timing lined up exactly with a driver update. This is one of the most common failure patterns on Windows laptops: a new driver that is technically newer but practically worse for your specific hardware.

Windows keeps the previous driver version around precisely for this situation, and rolling back is a built-in, one-minute operation. The trick is knowing where the button lives and what to do when Windows tries to reinstall the bad version overnight. Driver crashes like [display driver failures](/articles/how-to-fix-display-driver-stopped-responding-on-windows-11/) are frequent candidates for rollback.

This guide covers the standard rollback, what to do when the button is greyed out, and how to keep the bad driver from coming back.

## Why this happens

- **The new driver has a bug for your hardware:** Drivers are tested broadly but can still break specific laptop models or hardware revisions.
- **Windows installed a generic driver over the OEM one:** Windows Update sometimes replaces a tuned manufacturer driver with a generic version missing laptop-specific fixes.
- **The update was interrupted:** A partial driver install leaves mismatched files that behave worse than either the old or new version alone.
- **Conflicting leftover files:** New drivers do not always clean up the old version's registry entries and configuration files.
- **Firmware mismatch:** A driver may require a BIOS or firmware version your laptop does not have yet.
- **The wrong driver was offered:** On rare occasions, Windows Update offers a driver intended for different but similar hardware.
- **Beta or optional drivers installed automatically:** Optional driver updates can include less-tested versions that cause regressions.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Roll back the driver in Device Manager

This is the built-in, supported path. Windows stored the previous driver when the update installed, and this button restores it in under a minute.

1. Open Device Manager (right-click Start and select it).
2. Find the problem device, right-click it, and choose Properties.
3. Go to the Driver tab and click Roll Back Driver.
4. Select the reason that best matches, such as previous version worked better, and confirm.
5. Restart the laptop and verify the problem is gone.

### Fix 2: Manually install the older driver version

When the rollback button is greyed out, you can achieve the same result by installing the older driver yourself. Laptop makers archive previous driver versions on their support pages.

1. Note the device name and your exact laptop model from Device Manager.
2. Visit the manufacturer's support page and find the driver download section.
3. Download the previous driver version, not the latest one.
4. Run the installer; most will cleanly replace the newer version.
5. Restart and confirm the device works. Keep the installer file in case you need it again.

### Fix 3: Use System Restore to undo the update

If the bad driver came with a Windows update or you cannot identify which driver changed, System Restore can roll the whole system back to before the update. Your personal files are not affected.

1. Search for Create a restore point and open System Protection.
2. Click System Restore and choose a restore point dated before the problem started.
3. Review the affected programs list so you know what else will change.
4. Start the restore and let the laptop restart on its own.
5. Verify the hardware works, then create a fresh restore point.

### Fix 4: Block the bad driver with the Show or Hide Updates tool

Rolling back is pointless if Windows Update reinstalls the same broken driver the next night. Microsoft's Show or Hide Updates troubleshooter lets you block a specific driver update.

1. Download the Show or Hide Updates troubleshooter (wushowhide) from Microsoft's support site.
2. Run it and choose Hide updates.
3. Select the problematic driver from the list and confirm.
4. Run the tool again later and unhide the driver once a fixed version is released.
5. Check periodically whether the manufacturer has published a corrected driver.

### Fix 5: Disable automatic driver updates

For a broader shield, you can tell Windows to stop delivering drivers through Windows Update entirely. You then update drivers manually from the manufacturer's site on your own schedule.

1. Open System Properties, go to the Hardware tab, and click Device Installation Settings.
2. Choose No for automatic driver downloads, or use the Group Policy or registry method on Pro editions.
3. Confirm the change and restart if prompted.
4. From now on, get drivers from the laptop maker's support page or the Microsoft Update Catalog at https://www.catalog.update.microsoft.com/.
5. Re-enable automatic updates later if you prefer convenience over control.

### Fix 6: Perform a clean install of the working driver

Sometimes a rollback leaves fragments of the bad driver behind. A clean install removes every trace before putting the good version back, which fixes stubborn cases where rollback alone did not help.

1. Download the known-good driver version from the manufacturer first.
2. Open Device Manager, right-click the device, and choose Uninstall device.
3. Tick Delete the driver software for this device if the option appears.
4. Restart the laptop, then install the downloaded older driver.
5. Restart once more and confirm stable operation over a full day of use.

### Fix 7: Report the bad driver and watch for a fixed release

The loop is only closed when a corrected driver arrives. Reporting the issue and monitoring for the fix turns a temporary workaround into a permanent solution.

1. Use the Feedback Hub to report the driver problem to Microsoft with details.
2. Check the laptop manufacturer's support page monthly for a new driver version.
3. Subscribe to the manufacturer's driver notification service if one exists.
4. When a new version appears, unhide it in the troubleshooter and install it.
5. Keep the old installer archived until the new version proves stable.

## Closing

Driver rollback is one of the most underused tools in Windows: a built-in undo button for exactly the situation where an update makes things worse. Roll back first, then block the bad version so it cannot return overnight. Once a fixed driver is published, [update on your own terms](/articles/how-to-update-drivers-on-windows-11-laptop/) instead of letting Windows surprise you again.
