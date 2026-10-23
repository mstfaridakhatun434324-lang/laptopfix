---
title: "AMD Adrenalin Ryzen AI Driver Issues: How to Fix Them"
slug: amd-adrenalin-ryzen-ai-driver-issues
date: 2026-10-23
categories: ["ai-pc"]
tags: ["amd adrenalin", "ryzen ai", "xdna npu", "driver issues", "radeon driver", "troubleshooting"]
description: "Fix AMD Adrenalin Ryzen AI driver issues: clean-install the chipset and graphics drivers, repair the NPU driver, and resolve crashes step by step."
thumbnail: "/images/thumbs/amd-adrenalin-ryzen-ai-driver-issues.webp"
faqs:
  - q: "Why does AMD Adrenalin fail to install on my Ryzen AI laptop?"
    a: "The usual causes are a conflicting OEM-customized driver already installed, Windows Update having installed a partial driver, or the installer detecting an unsupported configuration. A clean uninstall with AMD Cleanup Utility followed by the OEM or AMD driver usually succeeds."
  - q: "Should I use AMD's driver or my laptop maker's driver?"
    a: "For Ryzen AI laptops, start with your laptop maker's driver — it's validated for your specific NPU firmware and power configuration. AMD's generic Adrenalin package works on many models but can break OEM-specific NPU features."
  - q: "Why did my NPU disappear after updating Adrenalin?"
    a: "The graphics driver package and the NPU (XDNA) driver are separate components. Some Adrenalin updates change the graphics driver without updating the NPU driver, leaving a version mismatch. Reinstalling the chipset/NPU driver package restores the NPU."
  - q: "Does Adrenalin work on Ryzen AI laptops at all?"
    a: "Yes, but with caveats — some OEMs customize the graphics driver enough that the stock Adrenalin installer refuses or misbehaves. When that happens, the OEM's driver package is the supported path."
---

AMD's Adrenalin software is the control center for Radeon graphics — and on Ryzen AI laptops it sits next to the XDNA NPU driver in a sometimes-uneasy coexistence. Update one without the other, mix OEM and AMD-generic packages, or let Windows Update meddle, and you get the classic symptoms: Adrenalin won't open, the NPU vanishes, games stutter, or the installer fails outright.

Ryzen AI platforms (Strix Point, Strix Halo, and newer) pair the Radeon iGPU with the XDNA NPU under one chipset driver umbrella, but the components version independently. The fixes below respect that architecture: clean the slate, install matched components, and keep Windows Update from rearranging them.

## Why this happens

- **OEM vs. AMD-generic driver conflict:** Laptop makers customize AMD drivers for their thermal and power designs. Installing AMD's generic Adrenalin over (or under) the OEM package creates mismatched components that fail in odd ways.
- **Windows Update partial installs:** Windows Update may install the graphics driver but not the NPU driver (or vice versa), leaving a version-skewed pair where Adrenalin can't initialize properly.
- **NPU driver and graphics driver version skew:** The XDNA NPU driver ships in the chipset package while graphics come from Adrenalin. Updating one without the other breaks the handshake between them.
- **Corrupted Adrenalin installation:** Failed or interrupted Adrenalin updates leave half-registered components — the app opens to errors or won't launch at all.
- **Old driver remnants in the driver store:** Previous driver versions staged in the Windows driver store can be reinstalled automatically, undoing your clean install within days.
- **Firmware/driver pairing requirements:** The NPU firmware expects a compatible driver version. Too-new or too-old drivers produce "device cannot start" on the NPU specifically.
- **Overlapping auto-update tools:** AMD's auto-detect tool, Windows Update, and the OEM's updater can fight over the same components — the same multi-source chaos behind [Windows Update driver ranking problems](/articles/windows-update-driver-ranking-npu/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify exactly which component is broken

"Adrenalin issues" is a bucket, not a diagnosis. Pin down whether it's the app, the graphics driver, or the NPU driver before changing anything.

1. Try opening AMD Software: Adrenalin — note the exact error (won't launch, "driver not compatible," missing tabs).
2. Open **Device Manager** and check **Display adapters** (Radeon graphics) and the NPU entry (under **System devices** or **Neural processors** — "AMD IPU Device") for yellow warnings.
3. Open **Task Manager > Performance** — is the NPU listed? A missing NPU with healthy graphics means the chipset/NPU package is the problem, not Adrenalin.
4. Note driver versions: **Device Manager > Properties > Driver** for both graphics and NPU, and compare dates — a big skew between them confirms version mismatch.
5. Check **Settings > Windows Update > Update history** for recent AMD driver installs — if one coincides with the breakage, you have your culprit and Fix 4 (blocking) will matter later.

### Fix 2: Clean uninstall with AMD Cleanup Utility

A standard uninstall leaves remnants that poison the reinstall. AMD's own Cleanup Utility wipes the slate properly — run it from Safe Mode for best results.

1. Download **AMD Cleanup Utility** from [AMD's driver support page](https://www.amd.com/en/support/download/drivers.html).
2. Boot into Safe Mode (**Settings > System > Recovery > Advanced startup**, or the triple-interrupt method) so no AMD components are loaded during removal.
3. Run AMD Cleanup Utility and let it remove all AMD graphics, chipset, and Adrenalin components — the screen may flicker or drop to low resolution, which is normal.
4. Restart back into normal Windows. Device Manager will show basic display adapters — that is expected at this stage.
5. Do not let Windows Update install drivers yet — disconnect from the internet temporarily if Windows Update is aggressive, and move to Fix 3 immediately.

### Fix 3: Install the OEM chipset and graphics drivers as a matched set

With the slate clean, install your laptop maker's validated packages — chipset (with NPU driver) first, then graphics — so the components version together.

1. Download both the **chipset driver** (includes the XDNA NPU driver) and the **graphics driver** for your exact model from [Lenovo](https://support.lenovo.com/us/en/), [HP](https://support.hp.com/us-en), or [Dell](https://www.dell.com/support/).
2. Install the chipset package first as administrator, and restart when prompted — this registers the NPU driver.
3. Then install the graphics/Adrenalin package from the OEM, and restart again.
4. Verify: Device Manager shows healthy Radeon graphics and AMD IPU/NPU devices, Task Manager > Performance lists the NPU, and AMD Software: Adrenalin opens without errors.
5. Test an NPU workload (Windows Studio Effects is the quickest check) and a graphics workload to confirm both paths work.

### Fix 4: Block Windows Update from breaking the matched set

A clean matched install survives until Windows Update "improves" one component. Prevent that with Microsoft's official blocking tools.

1. Use the **"Show or hide updates" troubleshooter** (wushowhide) to hide any AMD driver updates Windows offers — Microsoft documents this on [Windows support](https://support.microsoft.com/en-us/windows).
2. Consider the stronger policy: **Group Policy > Do not include drivers with Windows Updates** (or the equivalent registry value on Home) to exclude all driver updates.
3. Run **Windows Update > Check for updates** and confirm no AMD driver updates are offered.
4. Update AMD drivers manually going forward — check the OEM page quarterly, or AMD's page if your model is known to work well with generic Adrenalin.
5. After every Windows feature update, re-verify the driver versions — feature updates are the most common block-resetter.

### Fix 5: Repair a broken Adrenalin app without touching drivers

Sometimes the drivers are fine and only the Adrenalin application itself is corrupted — a much lighter repair.

1. Open **Settings > Apps > Installed apps**, find **AMD Software**, click the three dots, and try **Repair** if the option exists.
2. If repair is unavailable or fails, uninstall AMD Software (the app only — not the drivers) and reinstall it from the package you downloaded in Fix 3.
3. Check that **AMD Crash Defender** and related services are running in **Services** (`services.msc`) — set them to Automatic if they are disabled.
4. Delete Adrenalin's cached profiles: remove the contents of `%localappdata%\AMD\CN` (back up first if you have custom game profiles) and relaunch the app.
5. If the app works but shows wrong or missing NPU information, the issue is the driver pairing from Fix 3, not the app — reinstall the matched set.

### Fix 6: Handle persistent NPU disappearance and firmware pairing

When the NPU specifically refuses to appear despite correct drivers, the firmware/driver pairing is the remaining suspect.

1. In Device Manager, open the NPU device's **Properties > Events** tab — look for "device not started" messages naming the missing or mismatched component.
2. Check your maker's support page for an **NPU firmware** or **platform firmware** update separate from drivers, and install it with the charger connected.
3. After any firmware update, reinstall the chipset/NPU driver package from Fix 3 — firmware updates can change the hardware IDs drivers match against.
4. As a last resort, reset the BIOS to defaults (firmware NPU settings can get into bad states), then re-enable any NPU-related options the BIOS exposes.
5. If the NPU remains missing with correct firmware and drivers, contact your maker's support — and keep perspective: unrelated app problems like [video editors crashing](/articles/capcut-arm-windows-laptop-issues/) or [policy application failures](/articles/recall-group-policy-intune-not-applying/) are separate tracks, not NPU symptoms. Also note that moving large data like [Recall snapshots to another drive](/articles/move-recall-snapshots-another-drive/) is storage management, unrelated to driver health.

## Closing

AMD Adrenalin and Ryzen AI driver issues are almost always version-skew or source-conflict problems: OEM vs. generic, graphics vs. NPU, or Windows Update vs. your clean install. Wipe with AMD Cleanup Utility, install the OEM's matched chipset+graphics set, block Windows Update driver meddling, and the NPU and Adrenalin coexist peacefully.
