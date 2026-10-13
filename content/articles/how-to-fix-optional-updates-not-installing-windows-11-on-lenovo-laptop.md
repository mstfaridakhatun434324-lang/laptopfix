---
title: "Optional Updates Not Installing in Windows 11 on a Lenovo Laptop? Here's the Fix"
slug: how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop
date: 2026-10-06
categories: ["windows-update"]
tags: ["optional updates", "lenovo laptop", "windows 11", "driver updates", "lenovo vantage"]
description: "Optional updates won't install on your Lenovo laptop? Learn where they hide, why they fail, and when to use Lenovo Vantage instead of Windows Update."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-windows-11-on-lenovo-laptop.webp"
faqs:
  - q: "Where are optional updates in Windows 11?"
    a: "Open Settings > Windows Update > Advanced options > Optional updates. They're grouped into Driver updates and Other updates. Unlike regular updates, optional ones never install automatically — you must check the boxes and click Download & install yourself, which is why many users think they're broken when they're just waiting."
  - q: "Should I install all optional driver updates?"
    a: "No — be selective. Install optional drivers only for hardware that's actually misbehaving. If your Wi-Fi, Bluetooth, and graphics all work fine, those optional driver offers are unnecessary churn. The exception is chipset and firmware-adjacent drivers, which are worth keeping current."
  - q: "Why do optional updates fail but regular updates work?"
    a: "Optional updates are almost always drivers, which install through a stricter path involving hardware matching and signature checks. A driver offered for a slightly different hardware revision fails these checks while cumulative OS updates install fine. The failure is usually a mismatch, not system damage."
  - q: "Is Lenovo Vantage better than Windows Update for drivers?"
    a: "For Lenovo hardware, usually yes. Vantage delivers BIOS, firmware, and Lenovo-validated drivers tested against your exact model, while Windows Update offers generic versions. Use Vantage as your primary driver source and Windows Update optional drivers only as a supplement for non-Lenovo components."
---

Optional updates are Windows 11's most misunderstood feature. They sit quietly under Advanced options, never installing themselves, accumulating a list of driver and firmware offers that grows longer every month. Many Lenovo owners discover them, check every box, hit Download & install — and watch half of them fail. The natural conclusion is that something is broken. Usually, it isn't: optional updates fail for mundane reasons, and on Lenovo hardware there's often a better source for the same drivers anyway.

The key insight is that optional updates are almost entirely drivers, and drivers are the one update category where "latest from Windows Update" is frequently not the best answer for a Lenovo. Lenovo Vantage exists precisely because Lenovo validates drivers against specific models — BIOS versions, thermal profiles, and hardware revisions that Microsoft's generic packages don't account for. This guide covers fixing genuinely broken optional updates and, equally important, knowing when to get the driver from Vantage instead.

## Why this happens

- **Hardware revision mismatch**: The offered driver targets a slightly different revision of the component than your Lenovo has.
- **A newer driver is already installed (0x80070103)**: Vantage or Lenovo's factory image installed a newer version; Windows Update's older offer correctly fails.
- **You never actually triggered the install**: Optional updates don't auto-install — many "failures" are just updates that were never started.
- **Corrupt optional-update metadata**: The local catalog of what's available gets out of sync with what the server offers.
- **Pending restart blocks driver staging**: An earlier update's pending restart prevents optional drivers from installing.
- **Lenovo Vantage already handles it**: Vantage-installed drivers can conflict with Windows Update's attempts to manage the same device.
- **The driver needs a companion BIOS update**: Some Lenovo drivers require a minimum BIOS version and fail without it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the updates were actually attempted

Before troubleshooting failures, confirm there's a real failure. Optional updates are manual by design.

1. Go to **Settings > Windows Update > Advanced options > Optional updates**.
2. Expand **Driver updates** — each entry has a checkbox and a version number.
3. Check the boxes for the updates you want, then click **Download & install**.
4. Wait for the process to complete; don't navigate away mid-install.
5. If they install fine, there was never a problem — they were just waiting for you.
6. If specific ones fail, note which devices they target and continue.

### Fix 2: Decode the failure before fixing it

Optional driver failures carry the same error codes as regular driver failures, and the code determines the response.

1. Go to **Settings > Windows Update > Update history** and find the failed optional update.
2. **0x80070103** = you already have a newer driver. This is fine — leave it alone.
3. Other codes (0x800F020B, 0x80070002) indicate genuine install problems — continue below.
4. Open **Device Manager**, find the device, and check its current driver version and date on the **Driver** tab.
5. Compare with the version Windows Update offered — if yours is newer or equal, the "failure" is harmless.

### Fix 3: Get Lenovo drivers from Lenovo Vantage instead

For anything Lenovo-specific — chipset, power management, hotkeys, trackpad, BIOS-adjacent drivers — Vantage's versions beat Windows Update's generics.

1. Open **Lenovo Vantage** (install from the Microsoft Store if it's missing).
2. Go to **System Update** > **Check for Updates**.
3. Install everything Vantage offers, especially **BIOS** and **chipset** updates.
4. Restart when prompted — BIOS updates need AC power and take several minutes.
5. Return to Windows Update's optional updates: many previously failing offers will now show as installed or disappear.
6. For non-Lenovo components (NVIDIA graphics, Intel Wi-Fi), use the manufacturers' official driver pages directly.

### Fix 4: Clear the update cache to fix metadata sync issues

When the optional updates list shows stale offers or fails everything uniformly, the local catalog is corrupt.

1. Open **Command Prompt as administrator**.
2. Run `net stop wuauserv` and `net stop bits`.
3. Delete the contents of `C:\Windows\SoftwareDistribution\Download` and the `DataStore` subfolder.
4. Run `net start wuauserv` and `net start bits`.
5. Go to **Settings > Windows Update** and click **Check for updates** — this rebuilds the catalog.
6. Revisit **Optional updates**; the list should now reflect genuinely available drivers.

### Fix 5: Install the minimum BIOS version first

Some Lenovo driver packages declare a minimum BIOS version and fail silently without it. This is documented in Lenovo's driver release notes but never surfaced in Windows Update.

1. In **Lenovo Vantage**, check your current BIOS version under **System Update** or **Device** settings.
2. On [Lenovo support](https://support.lenovo.com/us/en/), look up your model and compare with the latest BIOS.
3. If you're behind, install the BIOS update from Vantage or the support site (AC power required, don't interrupt).
4. After the BIOS update, retry the failing optional drivers.
5. This particularly affects power management, thermal, and Thunderbolt drivers on ThinkPads and Legions.

### Fix 6: Resolve the pending-restart block

Driver installs queue behind pending restarts. If Windows is waiting on a restart from a previous update, optional drivers fail until it happens.

1. Check **Settings > Windows Update** for any "Restart required" notice.
2. Perform a full **Restart** (not shutdown — Fast Startup can preserve pending states).
3. Immediately after reboot, go to **Optional updates** and install the drivers before other updates queue.
4. If restarts hang, our [Restarting screen guide](/articles/how-to-fix-windows-update-stuck-on-restarting-screen-in-windows-11-24h2/) covers recovery.
5. Consider disabling Fast Startup (**Control Panel > Power Options > Choose what the power buttons do**) if pending states recur.

### Fix 7: Hide persistently failing offers and move on

A driver that fails after Vantage updates, cache clears, and BIOS updates is a bad package for your configuration. Stop offering it the chance to fail.

1. Confirm the device works fine with its current driver — if yes, the optional update is pure churn.
2. Download Microsoft's **"Show or hide updates"** troubleshooter and hide the specific failing driver.
3. Keep getting drivers from **Lenovo Vantage** on its schedule instead.
4. Revisit hidden updates quarterly — Microsoft sometimes fixes the packaging.
5. If optional updates fail alongside regular update problems, the issue is systemic — see our [update service guide](/articles/how-to-fix-windows-update-service-not-running-after-windows-11-update/) and Microsoft's [Windows Update documentation](https://support.microsoft.com/en-us/windows).

## Closing

Optional updates on a Lenovo are best treated as a supplement, not the main course. Let Lenovo Vantage handle Lenovo hardware — it's validated for your exact model — and use Windows Update's optional section selectively for everything else. A failing optional driver for a device that works fine isn't a problem to solve; it's an offer to decline.
