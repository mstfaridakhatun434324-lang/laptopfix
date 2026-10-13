---
title: "Bluetooth Disappeared From Device Manager in Windows 11 24H2? Here's the Fix"
slug: "how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2"
date: "2026-09-27"
categories: ["drivers"]
tags: ["bluetooth disappeared", "windows 11 24h2", "device manager", "bluetooth driver", "24h2 issues"]
description: "Windows 11 24H2 removed Bluetooth from Device Manager? This guide covers the 24H2-specific causes — driver model changes, LE Audio conflicts, and known issues — with targeted fixes."
thumbnail: "/images/thumbs/how-to-fix-bluetooth-disappeared-from-device-manager-in-windows-11-24h2.webp"
faqs:
  - q: "Is Bluetooth disappearing a known issue in Windows 11 24H2?"
    a: "Yes. The 24H2 feature update reworked parts of the Bluetooth stack, including broader Bluetooth LE Audio support, and several Bluetooth regressions were documented after its release. Symptoms range from the adapter vanishing in Device Manager to pairing failures with previously working devices, particularly with older Intel and Realtek radios."
  - q: "Should I roll back from Windows 11 24H2 to fix Bluetooth?"
    a: "Only as a last resort. Most 24H2 Bluetooth cases are fixed by installing a 24H2-certified driver from your laptop manufacturer, which is far less disruptive than rolling back the entire OS. You have only ten days after upgrading to roll back easily anyway, so driver-level fixes are the practical path for most users."
  - q: "Why does 24H2 break Bluetooth that worked on 23H2?"
    a: "Major feature updates reinstall the driver stack and can replace a working vendor driver with an inbox driver that lacks support for your specific radio firmware. 24H2 also changed Bluetooth power management defaults and enabled LE Audio paths that conflict with some older drivers, so the adapter fails to enumerate."
  - q: "Will a clean install of Windows 11 24H2 fix Bluetooth?"
    a: "A clean install can help if the upgrade left the driver store corrupted, but it is not guaranteed — if the root cause is that no 24H2-compatible driver exists yet for your Bluetooth chip, a clean install hits the same wall. Check your manufacturer's support page for a 24H2-specific Bluetooth driver before considering a reinstall."
---

Windows 11 24H2 brought welcome features — and, for many laptop owners, a nasty surprise: Bluetooth gone from Device Manager, no Settings toggle, wireless peripherals useless. This guide covers the 24H2-specific causes and their fixes.

24H2 reworked parts of the Bluetooth stack, expanded LE Audio support, and changed driver power-management defaults. On older Intel, Realtek, or MediaTek radios the old driver cannot talk to the new stack, so Windows hides the adapter instead of showing an error. The hardware is fine; the driver-OS contract broke.

Because this is version-specific, the fixes emphasize 24H2-certified drivers, known-issue mitigations, and 24H2's new settings. Work through them in order.

## Why this happens

- **Driver-to-stack mismatch**: 24H2's reworked Bluetooth stack requires drivers built against its new interfaces; older vendor drivers fail initialization and the adapter never enumerates.
- **Inbox driver replacement**: during the feature upgrade, Windows substitutes its generic inbox Bluetooth driver, which lacks firmware support for some older radio chips.
- **Bluetooth LE Audio conflicts**: 24H2 enables LE Audio paths by default, and on radios whose firmware predates the feature, this can crash the driver at startup.
- **Changed power-management defaults**: 24H2 applies stricter USB power policies that can keep internally-connected Bluetooth radios asleep through boot.
- **Corrupted driver migration**: the upgrade process migrates drivers between OS versions, and Bluetooth — with its layered service/driver architecture — is especially vulnerable to a botched migration.
- **Firmware/BIOS expectations**: some 24H2 Bluetooth components expect newer embedded-controller firmware than the laptop ships with, breaking enumeration on older BIOS versions.
- **Known 24H2 regressions**: Microsoft documented several Bluetooth issues in 24H2's early months, some fixed by later cumulative updates and some requiring vendor driver updates.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install all pending 24H2 cumulative updates

Before driver surgery, make sure you are on the latest 24H2 build. Microsoft fixed several documented Bluetooth regressions in post-release cumulative updates — your machine may simply be behind.

1. Open **Settings > Windows Update** and click **Check for updates** — install everything offered, including optional driver updates listed there.
2. Note the build number (**Settings > System > About**) before and after updating.
3. Restart with a full shutdown (hold **Shift** while clicking **Shut down**) rather than a quick restart.
4. Check Device Manager for the Bluetooth category after booting into the new build.
5. If Bluetooth returns, pause and test pairing for a day before changing drivers — a moving target of simultaneous fixes makes diagnosis impossible.

### Fix 2: Install the 24H2-certified driver from your manufacturer

This is the core fix for 24H2 Bluetooth losses. Laptop vendors released updated Bluetooth drivers specifically validated against 24H2, and these resolve the stack-mismatch problem that generic drivers cannot.

1. Identify your exact laptop model (check the sticker on the bottom or run `msinfo32`).
2. Visit your manufacturer's support site and download the newest 24H2-validated Bluetooth driver for your exact model.
3. Check the driver's release notes or date: you want one released after 24H2's rollout, explicitly mentioning 24H2 or recent Windows 11 support.
4. In Device Manager (**View > Show hidden devices**), uninstall any grayed-out Bluetooth adapter, ticking driver removal.
5. Install the downloaded driver, do a full shutdown, cold-boot, and verify the Bluetooth category is back — [Intel's driver assistant](https://www.intel.com/content/www/us/en/support/detect.html) can also detect the correct wireless driver for Intel-based radios.

### Fix 3: Disable Bluetooth LE Audio if the driver crashes at startup

On older radios, 24H2's LE Audio enablement can crash the Bluetooth driver during initialization — which looks exactly like a missing adapter. Disabling the LE Audio path lets the classic Bluetooth stack start cleanly.

1. In Device Manager, if the Bluetooth adapter appears briefly then vanishes, or shows a warning icon, open its **Properties**.
2. Look under the **Advanced** tab for LE Audio or "Bluetooth LE" related properties and disable them if present.
3. Alternatively, in **Settings > Bluetooth & devices > Devices**, check for audio-device-specific LE options and switch affected devices to classic pairing.
4. For Intel adapters, the PROSet/Wireless driver package settings may expose an LE Audio toggle — install the full manufacturer package, not the bare driver.
5. Restart and observe whether the adapter now stays enumerated; if it does, keep LE Audio off until a driver update explicitly adds support for your radio.

### Fix 4: Reset the Bluetooth stack with a power cycle and service restart

24H2's stricter power defaults can leave the radio in a state where neither the driver nor the services can reach it. A deliberate power cycle plus service reset breaks the deadlock.

1. Shut down fully (Shift + Shut down), unplug the charger, and hold the power button for 30 seconds.
2. Boot up, open `services.msc`, and set **Bluetooth Support Service** to **Automatic**, then start it.
3. In an elevated Command Prompt, run `sfc /scannow` to repair any stack files damaged during the upgrade.
4. Open **Settings > Bluetooth & devices** and confirm the toggle has returned.
5. If the toggle appears but pairing fails, remove all previously paired devices first — 24H2 sometimes invalidates old pairing keys (see [our general Bluetooth troubleshooting guide](/articles/bluetooth-not-working-on-windows-11-laptop-fix/) for that separate issue).

### Fix 5: Update the BIOS/UEFI firmware

Several 24H2 Bluetooth failures trace to the embedded controller: the new OS expects firmware behaviors the old BIOS does not provide, so the radio never appears on the internal bus.

1. Check your current BIOS version (`msinfo32` > BIOS Version/Date).
2. On the manufacturer's support page for your exact model, compare against the latest BIOS and read its changelog for Bluetooth, wireless, or embedded-controller fixes.
3. Update the BIOS following the manufacturer's instructions precisely — charger connected, no interruptions.
4. After the update, enter the BIOS once and choose "Load optimized defaults" to clear any stale device configuration.
5. Boot into Windows and check Device Manager; BIOS-level enumeration fixes often make the adapter reappear instantly.

### Fix 6: Block driver downgrades after the fix

A painful 24H2 pattern: you install the working manufacturer driver, and days later Windows Update replaces it with the broken inbox driver again. Lock the working driver in place.

1. Open **System > About > Advanced system settings > Hardware > Device Installation Settings** and select **No**.
2. In Group Policy (`gpedit.msc`), enable "Do not include drivers with Windows Updates" under **Computer Configuration > Administrative Templates > Windows Components > Windows Update**.
3. Verify in Device Manager (**Driver tab**) that your driver version and date match the manufacturer's package, not a Microsoft-dated one.
4. Create a system restore point now, while Bluetooth works, as a quick rollback target.
5. Re-check after the next Patch Tuesday — if Windows respected the policy, the driver version will be unchanged, unlike the pre-fix behavior described in [our post-update Bluetooth guide](/articles/how-to-fix-bluetooth-disappeared-from-device-manager-after-windows-11-update/).

### Fix 7: Consider the 10-day rollback window (last resort)

If no 24H2-certified driver exists and every fix fails, rolling back to 23H2 restores the old stack — but only within ten days of upgrading, and at the cost of 24H2's improvements.

1. Go to **Settings > System > Recovery** and check whether **Go back** is available.
2. If available, choose it, select "my apps or devices don't work on this build," and complete the rollback.
3. Immediately verify Bluetooth in Device Manager on the older build.
4. If the window has expired, a clean install of 23H2 from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) is the alternative — back up everything first.
5. Report the issue via Feedback Hub with your radio's hardware ID so Microsoft and the vendor have data for a proper 24H2 driver; also check [Microsoft's support hub](https://support.microsoft.com/en-us/windows) for newly published known-issue mitigations.

## Closing

Bluetooth losses tied to 24H2 are a version-mismatch problem: the OS moved forward and the driver did not. That dictates the fix order — cumulative updates first, then the manufacturer's 24H2-certified driver, then the LE Audio, power, and BIOS layers. Resist rolling back the OS until the driver avenue is exhausted; the vendor's updated package usually brings the adapter straight back.
