---
title: "Driver Updates Failing in Windows Update? Fix Them Properly"
slug: how-to-fix-driver-updates-failing-in-windows-update
date: 2026-09-12
categories: ["windows-update"]
tags: ["driver updates", "windows update", "failing", "optional updates"]
description: "Fix driver updates failing in Windows Update: identify the bad driver, install it from the manufacturer, and stop the failure loop."
thumbnail: "/images/thumbs/how-to-fix-driver-updates-failing-in-windows-update.webp"
faqs:
  - q: "Should I get drivers from Windows Update or the manufacturer?"
    a: "For the initial fix, use the manufacturer's driver — it is validated for your exact model and usually newer. Windows Update's driver catalog is a fine maintenance source afterward, but when a Windows Update driver install is actively failing, the manufacturer's package bypasses the broken path entirely."
  - q: "Why does Windows Update keep offering a driver I already installed?"
    a: "Version detection mismatches: Windows Update sometimes fails to recognize a manually installed newer driver and keeps offering its older catalog version anyway. Installing the manufacturer's driver, then hiding the Windows Update offering with the show/hide troubleshooter, ends the loop permanently."
  - q: "Can a failing driver update damage my hardware?"
    a: "Extremely unlikely. Failed driver installs roll back to the previous driver; the failure is an inconvenience, not a hazard. The real risk is a half-installed driver on a critical device like storage or display, which is why you verify Device Manager shows a clean state after each attempt."
  - q: "Should I disable driver updates in Windows Update entirely?"
    a: "Only as a targeted measure for a specific repeatedly-failing driver, not as a blanket policy. Blanket disabling leaves genuinely useful driver updates — security fixes for Wi-Fi and Bluetooth, for example — uninstalled. Hide the problem driver; leave the pipeline open for the rest."
---

Driver updates failing inside Windows Update are a special frustration: the OS updates themselves install fine, but the optional driver offerings fail one after another, sometimes blocking the whole update queue behind them. The drivers are usually fine — it is the delivery and install path that is broken, or the catalog version is simply wrong for your hardware.

The fix has two halves. First, stop the bleeding: hide the failing offering so it stops retrying. Second, get the driver properly from the manufacturer, where it was actually validated for your laptop. This guide does both, in order.

## Why this happens

- **Catalog version mismatch:** Windows Update offers a driver older or incompatible with your specific hardware revision.
- **Manufacturer customization:** Laptop makers customize reference drivers; the generic catalog version conflicts with the custom stack.
- **Corrupted driver store:** Damage to the local driver repository fails every install attempt at the staging phase.
- **Pending reboot locks:** A previous driver install awaiting restart holds locks the new one needs.
- **Third-party driver utilities:** "Driver updater" tools install conflicting versions that Windows Update then tries to overwrite.
- **Insufficient permissions:** The update service lacking rights to the driver store after a botched manual install.
- **Failing device hardware:** A dying Wi-Fi card or GPU that no driver version can initialize — the installs fail because the hardware never responds correctly.
- **Stuck optional-updates queue:** One failing driver blocks the entire optional queue behind it. The same queue mechanics stall [automatic driver updates on 24H2](/articles/how-to-disable-automatic-driver-updates-in-windows-11-24h2/) for users who manage drivers manually.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which driver is failing

1. Open **Settings → Windows Update → Update history** and expand **Driver Updates** to see each failure and its code.
2. Note the device name and driver version for every failing entry — "Intel Wireless" failing is a different fix from "Realtek Audio" failing.
3. Open **Device Manager** and check the device's status; a yellow warning here confirms the device itself is unhappy.
4. Screenshot the failures; you will need the exact names for the manufacturer download in Fix 3.
5. Do not lump them together — fix the most critical (network, display, storage) first.

### Fix 2: Hide the failing offering to stop the loop

1. Download Microsoft's "Show or hide updates" troubleshooter from the [Windows support hub](https://support.microsoft.com/en-us/windows).
2. Run it, choose **Hide updates**, and select each failing driver offering.
3. Confirm Windows Update no longer lists them — the retry loop ends immediately.
4. This is triage, not surrender: it buys you a quiet system while you install the right drivers manually.
5. Never hide OS cumulative updates this way — only the failing driver offerings.

### Fix 3: Install the driver from the manufacturer

1. Go to your laptop maker's support site (Dell, HP, Lenovo) and enter your exact model or serial.
2. Download the driver for the failing device — match the device name from Fix 1.
3. For Intel Wi-Fi/Bluetooth/chipset, [Intel's Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) detects and installs the correct packages automatically.
4. Run the installer, reboot, and verify in Device Manager that the device reports the new version with no warnings.
5. Manufacturer drivers are validated against your exact hardware; the catalog's generic build is not.

### Fix 4: Clean-install a stubborn driver

1. In **Device Manager**, right-click the device and choose **Uninstall device**, checking **Attempt to remove the driver** if offered.
2. Reboot — Windows will either reinstall a basic driver or leave the device unclaimed.
3. Install the manufacturer's driver package fresh on the clean slate.
4. Verify the version in **Device Manager → Properties → Driver**.
5. Clean installation removes the corrupted remnants that in-place updates keep tripping over.

### Fix 5: Repair the driver store

1. Elevated Command Prompt: run `DISM /Online /Cleanup-Image /RestoreHealth` to repair the component store underlying driver staging.
2. Follow with `sfc /scannow`.
3. Reboot and retry the Windows Update driver offering (unhide it first via the show/hide tool).
4. A healthy store resolves the staging-phase failures that survive manufacturer installs.
5. If the offering now succeeds, you can leave it unhidden going forward.

### Fix 6: Clear pending operations and reboot properly

1. Check for a pending restart in **Settings → Windows Update** — install anything waiting and reboot.
2. Do a full **Restart**, not a shutdown (fast startup can preserve the locked state).
3. After reboot, verify Device Manager shows no warning icons before retrying updates.
4. Pending operations are invisible blockers; one proper restart clears them.
5. Retry the driver update once on the clean boot state.

### Fix 7: Remove third-party driver updater tools

1. Uninstall any "driver booster" or "driver updater" utilities via **Settings → Apps**.
2. These tools install unvalidated driver versions that conflict with both Windows Update and manufacturer packages.
3. After removal, clean-install the manufacturer's driver as in Fix 4.
4. Re-hide nothing yet — test whether Windows Update's offering now succeeds on its own.
5. One driver source of truth per device: pick the manufacturer and stick with it.

### Fix 8: When the hardware itself is the problem

1. If every driver version fails on the same device and Device Manager shows **Code 43** or similar, suspect the hardware.
2. Test with a Linux live USB: if the device fails there too, it is hardware, not drivers.
3. For Wi-Fi cards, a $20 USB Wi-Fi adapter is a valid permanent workaround on an older laptop.
4. For GPUs showing Code 43 across all drivers, professional repair or replacement is the honest answer.
5. Document the [crashing-driver pattern](/articles/how-to-fix-audio-driver-keeps-crashing-in-windows-11-24h2/) if audio is the affected device — the diagnostics overlap.

## Closing

Driver updates failing in Windows Update are a delivery problem, not a driver problem, in the vast majority of cases: a mismatched catalog version, a corrupted driver store, or a conflicting utility. Hide the failing offering to stop the loop, install the manufacturer's validated driver, clean-install the stubborn ones, and repair the driver store underneath. Then keep one source of truth per device — the manufacturer's packages — and let Windows Update handle the OS while the maker handles the hardware. That division of labor is how driver updates stop failing and start being invisible again.
