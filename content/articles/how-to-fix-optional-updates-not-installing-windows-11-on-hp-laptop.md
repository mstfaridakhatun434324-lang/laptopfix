---
title: "How to Fix Optional Updates Not Installing on Windows 11 on an HP Laptop"
slug: "how-to-fix-optional-updates-not-installing-windows-11-on-hp-laptop"
date: 2026-09-13
categories: ["windows-update"]
tags: ["optional updates", "hp laptop", "windows 11", "drivers"]
description: "Optional updates not installing on Windows 11 on your HP laptop? Six HP-specific fixes for Support Assistant conflicts and stale driver offers."
thumbnail: "/images/thumbs/how-to-fix-optional-updates-not-installing-windows-11-on-hp-laptop.webp"
faqs:
  - q: "Should I use HP Support Assistant or Windows Update for drivers?"
    a: "HP Support Assistant delivers drivers validated for your exact HP model and serial number, typically newer than the generic WHQL packages in Windows Update’s optional list. Install HP’s drivers and hide Microsoft’s conflicting optional offers. Running both on overlapping schedules causes the file locks behind most failures — designate HP Support Assistant as your single driver manager."
  - q: "Can I download HP drivers manually?"
    a: "Yes. Go to HP’s support site, enter your product number or serial, and download drivers directly. This bypasses every conflict vector: no scheduling races, no version ambiguity, no stale catalog offers. Install major drivers with restarts between them, then hide the corresponding optional Windows Update offers so the failure loop ends."
  - q: "Does HP Wolf Security block driver updates?"
    a: "It can. HP Wolf Security and Sure Sense hook file operations deeply, and driver installs are exactly the kind of operation they scrutinize. If optional driver updates fail consistently on an HP while everything else works, temporarily disable the HP security stack’s real-time protection during the install as a diagnostic step — then re-enable it immediately after."
  - q: "What does 0x80070103 mean on my HP laptop?"
    a: "It means Windows Update offered a driver older than the one HP already installed — an attempted downgrade. This is normal on HP laptops where Support Assistant moves faster than Microsoft’s catalog. Do not force the install; hide that specific optional offer with the wushowhide tool. Your HP driver stays, which is the correct outcome."
---

On HP laptops, the Optional updates list in Windows 11 is where HP’s driver ecosystem and Microsoft’s catalog visibly disagree. HP Support Assistant installs model-specific drivers — often newer than anything Microsoft offers — and then the optional list keeps presenting older versions that fail on install because your system refuses the downgrade.

The general mechanics of optional updates are covered in the [optional-updates overview](/articles/how-to-fix-optional-updates-not-installing-after-windows-11-update/). This guide is the HP-specific companion: Support Assistant conflicts, HP’s security stack, and the version comparisons that resolve the loop.

## Why this happens

- **HP Support Assistant holding newer drivers:** HP’s tooling installs drivers newer than Microsoft’s catalog versions; the older WU offers then fail as downgrades.
- **HP-customized hardware IDs:** HP board revisions on audio, network, and fingerprint hardware do not match generic WU packages cleanly.
- **Concurrent HP and Microsoft driver installs:** Support Assistant scheduled updates colliding with Windows Update cause file locks failing both.
- **Interrupted HP driver installs:** A killed Support Assistant update leaves partial driver staging that Windows Update trips over.
- **BIOS updates re-enumerating devices:** HP BIOS updates can change device enumeration, desyncing WU hardware matching until metadata refreshes.
- **Stale catalog metadata:** Local metadata offering driver versions HP already superseded guarantees conflict failures.
- **HP Wolf Security or Sure Sense interference:** HP’s security stack can intercept driver installs, failing the optional package at the file-operation step.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Let HP Support Assistant set the driver baseline

HP validates these packages against your exact product number, including custom board revisions. Making HP’s tooling the driver authority eliminates the version mismatches behind optional-update failures.

1. Open HP Support Assistant and run its updates check.
2. Install all driver and firmware updates it offers.
3. Restart the laptop.
4. Revisit Settings > Windows Update > Advanced options > Optional updates — stale failures should be gone.

### Fix 2: Compare versions before installing any optional

An optional offer is availability, not a recommendation. On HP laptops the installed HP driver is routinely newer than Microsoft’s optional package — recognizing the downgrade saves you from “fixing” something that is not broken.

1. In Device Manager, note the installed driver version for the failing device.
2. Compare with the optional offer’s version in Windows Update.
3. If yours is newer, hide the optional (Fix 6) instead of installing it.
4. Only install optionals that are genuinely newer or fill missing drivers.

### Fix 3: Separate the lanes and pause interception

Concurrent installers plus a vigilant security stack is the HP failure trifecta. Separating the lanes — and pausing interception during installs — removes all three at once.

1. Set HP Support Assistant updates to manual or a quiet schedule.
2. Let Windows Update handle OS patches; HP handles drivers.
3. Temporarily disable HP Wolf Security real-time protection during driver installs.
4. Re-enable security immediately after.

### Fix 4: Clean-reinstall the HP driver from scratch

Interrupted HP installs can poison driver staging beyond incremental repair. Clean removal plus a fresh HP-sourced install restores a state both updaters can work with.

1. Uninstall the problem device in Device Manager, ticking “Delete the driver software”.
2. Restart for the baseline driver.
3. Install the exact-model driver from [HP Support](https://support.hp.com/us-en).
4. Restart and confirm the optional failure does not return.

### Fix 5: Refresh the update cache

Stale catalog metadata keeps offering drivers HP superseded months ago. A cache refresh forces a new catalog query and clears the phantom entries.

1. Elevated Command Prompt: net stop wuauserv, net stop bits.
2. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
3. Restart the services.
4. Recheck Optional updates — phantom HP-conflicting offers usually vanish.

### Fix 6: Hide the stale optional offers

When HP’s driver is right and Microsoft’s optional is outdated, hiding is the supported permanent fix. OS security updates continue normally; only the stale optional offer is silenced.

1. Download wushowhide.diagcab from [Microsoft Support](https://support.microsoft.com/en-us/windows).
2. Run it, choose Hide updates, tick the failing HP-conflicting optionals.
3. Verify they leave the Optional updates list.
4. For the general optional-update mechanics, see the [optional updates guide](/articles/how-to-fix-optional-updates-not-installing-after-windows-11-update/).

### Fix 7: Audit HP software you do not need that ships its own drivers

HP laptops often ship with more than just Support Assistant managing drivers: trial utilities, printer software bundles, and accessory managers sometimes install their own driver packages or filter drivers, and these show up in the Optional updates list as conflicting offers. An audit of installed HP software — keeping Support Assistant and removing redundant driver managers — simplifies the driver picture dramatically. Fewer driver owners means fewer conflicts, and the optional list shrinks to packages that actually make sense. This is also the moment to check for the third-party “driver updater” trials that HP preloads on some consumer models; they are a notorious source of exactly the optional-update failures this guide addresses. Remove them through Settings > Apps, restart, and re-check the Optional updates list — you may find the failures vanish along with the redundant software.

1. Open Settings > Apps > Installed apps and search for “HP”.
2. Keep HP Support Assistant; evaluate everything else for actual use.
3. Uninstall redundant HP driver/utility managers and any third-party driver updater trials.
4. Also remove old printer software bundles that install filter drivers you no longer need.
5. Restart the laptop.
6. Revisit Optional updates — the list should be shorter and the remaining offers more likely to install cleanly.

## Closing

On HP hardware, optional driver updates fail for the most boring reason: HP already installed something better. Let HP Support Assistant own your drivers, hide Microsoft’s stale offers, and keep Wolf Security from intercepting the installs. The optional list goes quiet — because there is nothing left worth installing from it. Seeing the same failure on the 24H2 build rather than HP driver offers? The [optional updates failing on 24H2](/articles/how-to-fix-optional-updates-not-installing-in-windows-11-24h2/) guide covers that side of the problem.
