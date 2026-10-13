---
title: "Optional Updates Won't Install? Video-Style Fix Walkthrough"
slug: how-to-fix-optional-updates-not-installing-youtube
date: 2026-09-11
categories: ["windows-update"]
tags: ["optional updates", "driver updates", "windows update", "windows 11", "not installing"]
description: "Optional updates selected but never installing? Follow this visual, step-by-step walkthrough to get driver and feature optionals working again."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-youtube.webp"
faqs:
  - q: "What are optional updates in Windows 11?"
    a: "Optional updates are driver updates, firmware, and non-security extras that Microsoft offers but does not install automatically. They appear under Settings, Windows Update, Advanced options, Optional updates. Unlike security updates, they are never urgent — but they often fix hardware quirks, which is why people seek them out."
  - q: "Do I actually need to install optional updates?"
    a: "Usually not. If your hardware works correctly, skipping optional driver updates is perfectly fine and sometimes safer, since newer drivers occasionally introduce regressions. Install them when you are troubleshooting a specific device problem or when a manufacturer recommends a particular version."
  - q: "Why do optional updates fail more often than regular ones?"
    a: "Optional updates are overwhelmingly driver packages, and driver installation is finicky: the wrong driver version for your hardware revision, conflicts with manufacturer utilities, or a device in a bad state can all cause failures. Regular cumulative updates touch core OS files with far fewer hardware variables."
  - q: "Can a failed optional update harm my laptop?"
    a: "Rarely. A failed driver update typically rolls back to the previous driver automatically, leaving the device working as before. In the worst case you may need to reinstall the driver manually from the manufacturer's site. Your files and OS are not at risk from optional update failures."
---

Optional updates are the "would you like fries with that" of Windows Update: driver refreshes and extras that Microsoft offers but never forces. When you tick those boxes and click Download and install, only to watch them fail or vanish, it is annoying — especially when you were chasing a specific driver fix.

This walkthrough follows the visual style of a good video tutorial: look here, click this, check that. The fixes move from the optional-updates page itself outward to the driver layer underneath, because that is where these failures actually live.


A useful first test: try installing just one small optional update rather than the one you actually want. If even the small one fails, the problem is systemic and the deeper fixes apply. If the small one succeeds, the issue is specific to the problematic driver — skip straight to the manufacturer-driver fix.
## Why this happens

- **Wrong driver for the hardware revision:** The offered driver does not match your specific device variant.
- **Manufacturer utility conflicts:** Dell Update, MyASUS, or Vantage fighting Windows over the same driver.
- **Device in a bad state:** The target device is disabled or erroring, so its driver cannot install.
- **Corrupted driver store:** The local driver repository has damaged entries.
- **Pending restart:** A previous installation left a reboot pending that blocks new driver installs.
- **Stale optional update listing:** The offered update was superseded but the UI did not refresh.
- **Insufficient permissions:** Driver installation needs elevation the session lacks.
- **Driver ranking conflicts:** Windows preferring its driver over the manufacturer's already-installed one.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Refresh the optional updates list

1. Go to **Settings > Windows Update > Advanced options > Optional updates**.
2. Click **Check for updates** on the main Windows Update page, then reopen the optional list.
3. Uncheck everything, close Settings, reopen, and re-check only the update you need.
4. Stale listings are common — a refresh often replaces the failing entry with a working newer version. Our Lenovo-specific guide covers [optional updates failing on Lenovo machines](/articles/how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop/).
5. After refreshing, wait a few minutes — the list repopulates asynchronously.
6. If the failing entry disappears entirely, it was superseded and the problem solved itself.

### Fix 2: Install one update at a time

1. In the optional updates list, select only **one** driver update.
2. Click **Download and install** and let it complete fully.
3. Restart if prompted before touching the next one.
4. Batch-installing multiple drivers is the top cause of cascading optional update failures; serial installation isolates problems.
5. Restart between each driver install, not just at the end — stacked pending installs cause failures.
6. Keep a note of which driver installed cleanly in case a later one breaks something.

### Fix 3: Check the target device's state

1. Open **Device Manager** and find the device the driver targets (display adapter, Wi-Fi, audio).
2. Look for warning icons or disabled states — right-click and **Enable device** if needed.
3. If the device shows an error code, resolve that first; no driver will install onto a broken device state.
4. Retry the optional update after the device is healthy.
5. Expand hidden devices in Device Manager to catch greyed-out problem entries.
6. If the device is missing entirely, scan for hardware changes before retrying.

### Fix 4: Get the driver from the manufacturer instead

1. Identify the exact driver version Windows is offering and your hardware model.
2. Download the equivalent driver from the manufacturer's support site — [Dell](https://www.dell.com/support), HP, Lenovo, or [Intel's detection tool](https://www.intel.com/content/www/us/en/support/detect.html) for Intel components.
3. Install it manually and restart.
4. Manufacturer drivers are validated against your exact model; after installing, the optional entry usually disappears as satisfied. For persistent driver failures, see our guide on [driver updates failing in Windows Update](/articles/how-to-fix-driver-updates-failing-in-windows-update-in-windows-11-24h2/).
5. Compare version numbers: install the manufacturer's driver only if it differs meaningfully.
6. After manual installation, hide the Windows optional entry if it still offers the older version.

### Fix 5: Clear pending operations and the cache

1. Restart the laptop to clear any pending-install state blocking new drivers.
2. In an elevated Command Prompt, run `net stop wuauserv` and `net stop bits`.
3. Empty `C:\Windows\SoftwareDistribution\Download`, then restart both services.
4. Reopen the optional updates list and try again with a clean slate.
5. Restart after clearing the pending state — pending operations only clear on boot.
6. Check Update history for entries marked 'pending restart' and resolve those first.

### Fix 6: Clean the driver store

1. Open an elevated Command Prompt and run `pnputil /enum-drivers` to list third-party drivers.
2. Identify obviously stale or duplicate entries for the problem device.
3. Remove the offending package with `pnputil /delete-driver oemXX.inf /uninstall` (replace oemXX with the real number).
4. Retry the optional update. A corrupted driver store entry blocks every install attempt against that device.
5. Export the driver list with pnputil before deleting anything, as a rollback reference.
6. Delete only drivers for the problem device — broad deletions cause more harm.

### Fix 7: Reset Windows Update components

1. Stop `wuauserv`, `bits`, and `cryptsvc` in an elevated Command Prompt.
2. Rename `C:\Windows\SoftwareDistribution` and `C:\Windows\System32\catroot2` with `.old` suffixes.
3. Restart the services and check for updates.
4. This is the deep reset for when every optional update fails. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document the full procedure.
5. After the reset, install optional updates one at a time as in Fix 2.
6. If all optionals still fail, the Windows installation itself may need a repair install.

## Closing

Optional updates fail at the driver layer, so fix them there: refresh the list, install serially, check the device, and prefer the manufacturer's driver when Windows' offering misbehaves. Remember that optional means optional — if everything works, you lose nothing by skipping them. Save your troubleshooting energy for the updates that actually protect you. Treat optional updates as a toolbox, not a to-do list: reach for a specific driver when you need it, ignore the rest. Your laptop does not grade you on optional update completion.
