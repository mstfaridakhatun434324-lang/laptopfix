---
title: "Fix Windows Update Error 0x800F020B on Windows 10: Resolve the Package Conflict"
slug: how-to-fix-windows-update-error-0x800f020b-on-windows-10
date: 2026-09-13
categories: ["windows-update"]
tags: ["windows update", "0x800f020b", "windows 10", "driver mismatch", "device driver"]
description: "Windows 10 error 0x800F020B means a driver package does not fit your device. Hide the bad offer and install the correct manufacturer driver."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x800f020b-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 show 0x800F020B for a driver update?"
    a: "The package's applicability check failed: as far as the installer can tell, the driver does not match the device. Causes include shared hardware IDs across revisions, OEM-customized components, ghost device entries, or a currently installed driver in a state the package cannot upgrade."
  - q: "Is it safe to ignore 0x800F020B?"
    a: "Mostly — other updates install fine. But the failed package retries every scan, and the underlying device may genuinely need its driver updated from the right source. Hide the bad package and handle the driver manually rather than ignoring it forever."
  - q: "How do I stop Windows 10 from offering the wrong driver?"
    a: "Hide it with the wushowhide troubleshooter, then optionally disable automatic driver updates in Device Installation Settings so the OEM site becomes your driver source. That ends the mismatch cycle permanently. Revisit the hidden list yearly; hardware changes can make old blocks obsolete."
  - q: "Where do I get the right driver instead?"
    a: "From your laptop manufacturer's support page for your exact model — they validate drivers against your hardware. For Intel parts, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) is the reliable second source. Our [Windows 11 version of this fix](/articles/how-to-fix-windows-update-error-0x800f020b-on-windows-11/) mirrors these steps for Windows 11."
---

On Windows 10, error 0x800F020B is the installer declining a driver it does not trust itself to install: the package does not match the device. It is a protective refusal, not a system failure, and it almost always concerns one specific driver package that Windows Update keeps offering and that keeps failing applicability checks. Everything else on the update list is unaffected.

The repair has two halves. First, administrative: identify the offending package and hide it so the retry loop stops. Second, substantive: get the device its correct driver from the manufacturer, because the device probably does need attention — just not from the mismatched package. Device Manager and the OEM driver page are your main tools here, not the update client's internals.

Do not force the package. A driver that fails applicability checks is wrong for the hardware, and forcing it trades a benign error for a broken device.

## Why this happens

- **Shared hardware IDs**: Detection matching a driver to the wrong revision.
- **OEM customization**: Factory-tweaked devices rejecting stock drivers.
- **Driver state confusion**: Current install reporting versions the package cannot handle.
- **Phantom devices**: Removed hardware still attracting driver offers.
- **Dock/printer complexity**: Multi-function externals with fragile driver matching.
- **Metadata damage**: Corrupt local data misdescribing devices.
- **Stale driver store**: Old driver packages interfering with applicability checks.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Name the failing package

Precision first. The update history tells you exactly which driver package fails with 0x800F020B — capture its name, version, and target device before doing anything else.

1. Go to Settings > Update & Security > Windows Update > View update history.
2. Locate the entry failed with 0x800F020B and record the full driver name and version.
3. Identify the device it targets (printer, display, network, chipset, dock).
4. Open Device Manager and find that device to confirm it exists and is working.

### Fix 2: Hide the bad package with wushowhide

End the retry loop. Microsoft's official hide-updates tool removes the mismatched package from future scans without affecting anything else.

1. Download the Show or hide updates troubleshooter from Microsoft.
2. Run wushowhide.diagcab, click Next, then Hide updates.
3. Select the failing 0x800F020B driver package and finish the wizard.
4. Run Check for updates to confirm it is gone from the offered list.

### Fix 3: Install the manufacturer's driver

Replace the guess with certainty. The OEM validates drivers against your exact model and revision, which is precisely the matching Windows Update got wrong.

1. Identify your exact model from the service tag or Settings > System > About.
2. On the manufacturer's support site (Dell, HP, Lenovo, or your brand), download the driver for the specific device.
3. Install it and reboot if asked.
4. Verify in Device Manager that the device reports the new driver version and works normally.

### Fix 4: Remove phantom and duplicate devices

Ghost entries for removed hardware are a classic source of phantom driver offers. Showing hidden devices and clearing the phantoms removes the false targets.

1. In Device Manager, enable View > Show hidden devices.
2. Uninstall any grayed-out instances of the affected device type.
3. Also remove duplicate entries if the device appears twice.
4. Choose Action > Scan for hardware changes and verify a single healthy entry remains.

### Fix 5: Do a clean driver reinstall

If the currently installed driver is in a confused state, its reported metadata can fail every future applicability check. A clean reinstall resets the device's driver state completely.

1. Right-click the device in Device Manager and choose Uninstall device, ticking Delete the driver software for this device.
2. Reboot and let Windows install its baseline driver.
3. Install the manufacturer's latest driver on top of the clean baseline.
4. Check for updates — the device should no longer attract mismatched offers.

### Fix 6: Reset update components for a clean slate

Repeated failures can leave the update client's metadata describing the device incorrectly. A component reset rebuilds that metadata from the now-correct driver state.

1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
2. Rename SoftwareDistribution and catroot2 with .old suffixes.
3. Restart the four services and reboot.
4. Confirm the update scan is clean with the bad package still hidden.

### Fix 7: Take control of driver sourcing

For OEM-heavy laptops where Windows Update chronically misjudges drivers, the durable fix is policy: let Windows handle system updates and let the manufacturer handle drivers.

1. Open Control Panel > System > Advanced system settings > Hardware > Device Installation Settings.
2. Select No (your device might not work as expected) to stop automatic driver downloads — the wording is scarier than the effect when you manage drivers yourself.
3. Bookmark your OEM's driver page and check it quarterly.
4. Dell's [support site](https://www.dell.com/support) and equivalents offer automatic detection tools that keep this painless.

### Fix 8: Use the OEM utility and update firmware

Resolve the mismatch at its source. The manufacturer's utility installs drivers validated for your exact model, while a BIOS update corrects the hardware's self-reported identity so future driver matching evaluates correctly.

1. Install your maker's driver tool — Dell SupportAssist, HP Support Assistant, or Lenovo Vantage — and install every recommended driver.
2. Check your BIOS version in System Information (msinfo32) against the latest on the manufacturer's support page.
3. Follow the maker's BIOS update instructions exactly, with the charger connected and nothing else running.
4. After updating, verify the device in Device Manager and confirm Windows Update no longer offers the mismatched package.

## Closing

Windows 10's 0x800F020B is a matching problem, not a system problem: the wrong driver was offered, the installer correctly refused, and your job is to supply the right one. Hide the bad package, install the OEM driver, and take charge of driver sourcing if mismatches recur. Done this way, the error disappears and the device ends up better served than Windows Update alone would have managed. Related: the [Windows 11 0x800F020B guide](/articles/how-to-fix-windows-update-error-0x800f020b-on-windows-11/) and our [driver update failure guide](/articles/best-way-to-fix-driver-updates-keep-failing-windows-update/) for recurring driver mismatches.
