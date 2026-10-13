---
title: "Windows 11 23H2 Not Showing in Windows Update? What to Do"
slug: what-to-do-if-windows-11-23h2-not-showing-in-update
date: 2026-09-27
categories: ["windows-update"]
tags: ["windows 11 23h2", "feature update missing", "windows update", "upgrade"]
description: "The Windows 11 23H2 feature update is not appearing in Windows Update? Learn why Microsoft withholds it and how to get the offer safely."
thumbnail: "/images/thumbs/what-to-do-if-windows-11-23h2-not-showing-in-update.webp"
faqs:
  - q: "Why is the Windows 11 23H2 update not showing up?"
    a: "Microsoft rolls out feature updates in waves and withholds the offer from machines with known compatibility issues — a safeguard hold. Your laptop may have a driver or hardware combination flagged in Microsoft's telemetry. Other causes include metered connections, paused updates, enterprise policies, or simply not yet being in the rollout wave. A missing offer is usually protection, not a bug."
  - q: "Is it safe to force the 23H2 update if Windows Update does not offer it?"
    a: "Usually yes, but check why it is withheld first. If the cause is a safeguard hold for your hardware, forcing the install can trigger the exact crash Microsoft was protecting you from. Update your drivers and BIOS first, then use the Installation Assistant. If the hold was telemetry-based and your drivers are current, the forced install typically succeeds cleanly."
  - q: "How long does it take for a feature update to appear?"
    a: "Rollout waves span several months, so a machine can legitimately wait weeks or months for the automatic offer. Microsoft prioritizes newer hardware and clean telemetry. If it has been more than three months and your system meets all requirements, something is actively blocking the offer — check pause settings, policies, and safeguard holds rather than waiting longer."
  - q: "Can a metered connection hide the feature update?"
    a: "Yes. Windows does not download feature updates over metered connections, so the offer may not appear at all until you unmark the connection. Go to Settings, then Network and internet, then Wi-Fi, select your network, and turn off the metered connection toggle. Check for updates again afterward — the offer often appears within minutes."
---

When everyone else is discussing the new Windows 11 23H2 features and your Windows Update page shows nothing, the instinct is to assume something is broken. Usually it is not. Microsoft deliberately withholds feature updates from machines with known issues — a system called safeguard holds — and rolls the update out in waves over months. A missing offer is often your laptop being protected, not neglected.

That said, sometimes the offer is missing for fixable reasons: a paused update setting you forgot, a metered connection flag, a policy from a previous workplace, or drivers old enough to trip the compatibility check. The technician move is to find out which reason applies to your machine, fix what is fixable, and only then decide whether to wait or to install manually.

This guide walks through that diagnosis and gives you the safe paths to 23H2 — whether that means unblocking the automatic offer or installing it deliberately.

## Why this happens

- **Safeguard hold on your hardware:** Microsoft's telemetry flagged a driver or hardware combination like yours as problematic, so the offer is withheld until the issue is resolved.
- **Rollout wave timing:** Feature updates reach machines over months; newer hardware and clean telemetry get priority.
- **Updates paused:** A pause set months ago — sometimes by a "tweak" tool — silently blocks all feature offers.
- **Metered connection:** Windows will not even display large feature updates on connections marked as metered.
- **Old drivers or BIOS:** The compatibility check fails quietly on outdated storage, graphics, or firmware, suppressing the offer.
- **Group policy blocks:** A registry or policy setting from school, work, or a utility can pin the machine to an older feature version.
- **Insufficient disk space:** The offer is suppressed when free space is too low for the upgrade to stage. The [24H2 rollout issues guide](/articles/how-to-fix-windows-11-24h2-rollout-issues-step-by-step/) describes the same mechanics for the newer release.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the obvious blockers first

1. Open **Settings → Windows Update** and confirm updates are not **paused** — resume them if they are.
2. Go to **Settings → Network & internet → Wi-Fi**, click your network, and turn **off** Metered connection.
3. Check **Settings → System → About** to confirm you are actually on an older build (22H2 or earlier).
4. Verify you have at least **20 GB free** on C:.
5. Click **Check for updates** and wait — the offer sometimes appears within minutes of clearing these flags.

### Fix 2: Run the compatibility check

1. Download the **PC Health Check** app from Microsoft and run it.
2. Confirm it reports your laptop meets Windows 11 requirements — CPU, TPM 2.0, Secure Boot, RAM.
3. If it flags anything, resolve that item first; a failed requirement suppresses the offer entirely.
4. Note the specific requirement that fails — TPM issues are usually a BIOS setting, not hardware.
5. Re-run the check after fixing; a clean pass means the machine is eligible and the hold is elsewhere.

### Fix 3: Update drivers and BIOS to clear safeguard holds

1. Visit your manufacturer's support site and update **chipset, storage, graphics, and network** drivers.
2. Update the **BIOS** to the latest version for your exact model.
3. Restart and run **Windows Update** to pull any pending monthly updates first.
4. Wait 24–48 hours — Microsoft re-evaluates safeguard holds as telemetry updates, and the offer often appears on its own.
5. This is the highest-success fix: most holds exist because of a driver Microsoft already knows is bad, and updating it lifts the hold. If optional updates are also misbehaving, see [optional updates not installing](/articles/how-to-fix-optional-updates-not-installing-in-windows-11-24h2/).

### Fix 4: Check for policy blocks

1. Press **Win + R**, type `gpedit.msc` (Pro editions) and check **Computer Configuration → Administrative Templates → Windows Components → Windows Update** for configured policies.
2. On Home editions, check the registry at `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate` for a `TargetReleaseVersion` entry pinning you to an old version.
3. Remove or update any target-version pin that references 22H2 or older.
4. Also check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings` for stale pause data.
5. Restart and check for updates after clearing policy blocks.

### Fix 5: Use the Installation Assistant deliberately

1. If the machine is eligible and updated but the offer still has not appeared after a week, decide to install manually.
2. Download the **Windows 11 Installation Assistant** from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
3. Run it and let its own compatibility check run — it will flag anything the silent check found.
4. Proceed with the upgrade, keeping the laptop plugged in.
5. This is the supported manual path and produces the identical 23H2 build the automatic offer would deliver.

### Fix 6: Use the Media Creation Tool as an alternative

1. If the Assistant also refuses, download the **Media Creation Tool** from the same official page.
2. Choose **Upgrade this PC now** for an in-place upgrade to the latest build.
3. Alternatively, create installation media and run `setup.exe` from within Windows.
4. The in-place upgrade keeps files, apps, and settings while moving you to 23H2.
5. Afterward, confirm the build in `winver` and check that Windows Update offers monthly patches normally.

### Fix 7: Wait strategically when a hold is genuine

1. If Microsoft's documentation lists a known issue for your hardware, respect the hold — it exists to prevent crashes.
2. Keep monthly cumulative updates installing; they sometimes include the driver fix that lifts the hold.
3. Recheck the offer every few weeks rather than forcing it.
4. Monitor your manufacturer's support page for the driver or BIOS update that resolves the known issue.
5. Forcing past a genuine safeguard hold is how 24H2 blue screens happen — patience here is a technical decision, documented further on the [Microsoft support site](https://support.microsoft.com/en-us/windows).

## Closing

A missing 23H2 offer is information, not just an absence. Check the simple blockers, update drivers and BIOS to lift safeguard holds, clear any policy pins, and then either wait for the wave or install deliberately with the Assistant. Either path lands you on the same build — the difference is whether you arrive with your drivers ready or your fingers crossed.
