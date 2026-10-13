---
title: "How to Fix Windows 11 Update Error 0x800f0922 on a Dell Laptop"
slug: how-to-fix-windows-11-update-error-0x800f0922-on-dell-laptop
date: 2026-10-10
categories: ["windows-update"]
tags: ["0x800f0922 fix", "dell windows update error", "net framework 3.5 update error", "windows 11 update failed"]
description: "Error 0x800f0922 on your Dell laptop means the .NET Framework 3.5 installer step failed. Repair the feature state, clear pending updates, and install the KB manually."
thumbnail: "/images/thumbs/how-to-fix-windows-11-update-error-0x800f0922-on-dell-laptop.webp"
faqs:
  - q: "What does error 0x800f0922 actually mean?"
    a: "It is the servicing stack reporting that one of the update's sub-installers collapsed. Nine times out of ten that sub-installer is the .NET Framework 3.5 feature step — which is why effective repairs focus on the .NET 3.5 feature state rather than generic update troubleshooting."
  - q: "Do I need .NET Framework 3.5 at all?"
    a: "Most likely not, unless some older desktop program you use depends on it. When the feature sits half-enabled and nothing needs it, turning it fully off in optionalfeatures.exe usually clears 0x800f0922 on the spot. Repair the feature only for an application you genuinely run."
  - q: "Why does the update fail at the same point every time?"
    a: "The failure is deterministic: the installer arrives at the .NET 3.5 configuration step, meets the broken feature state, and fails the identical way each attempt. Retrying without touching the feature state cannot ever succeed — the broken piece has to be repaired or removed first."
  - q: "Is it safe to disable Secure Boot to test?"
    a: "As a brief test, yes, provided you switch it back on right after. Secure Boot blocks boot-level malware, so leaving it disabled is not an option. The test is only worth doing on Dell firmware where the .NET installer shim is known to conflict with Secure Boot validation."
---

Code 0x800f0922 is the servicing stack reporting a collapsed sub-installer inside the update. On Dell laptops that sub-installer is nearly always the .NET Framework 3.5 feature step — the code decodes to a CBS installer failure, and experience says the failing piece is the .NET 3.5 payload that cumulative updates attempt to configure. Dell machines with .NET 3.5 stranded half-enabled (a frequent souvenir of in-place upgrades) hit this more than most. [the Windows 10 write-up](/articles/how-to-fix-error-0x800f0922-on-windows-10/)

Do not keep pressing Retry. Each attempt replays the same failing installer against the same broken payload, so the outcome cannot change. The repairs below either restore the .NET feature state so the installer can succeed, or bypass the broken piece with a manual install. Follow them in sequence; most Dell owners never get past the third repair.

## Why this happens

- **.NET 3.5 stuck between on and off.** The feature is neither fully enabled nor fully disabled, or its payload is damaged, so its installer step dies on every attempt. Launch optionalfeatures.exe — a half-filled checkbox exposes the condition instantly.
- **Payload sources deleted by cleanup.** Disk Cleanup's "Windows Update Cleanup" sometimes removes the side-by-side sources .NET 3.5 requires, leaving the installer with nothing to build from.
- **Secure Boot blocking the installer shim.** Some Dell firmware builds reject the .NET installer shim while Secure Boot is active. Switch it off briefly to test, then back on immediately.
- **App Readiness disabled by a debloater.** Feature configuration during updates depends on this service, and debloat utilities target it eagerly. services.msc reveals its current state.
- **Damage inside the CBS store.** The component-based servicing store cannot complete the transaction the .NET installer needs. `DISM /Online /Cleanup-Image /ScanHealth` gauges the extent.
- **SupportAssist scrambling feature states.** Dell's utility occasionally leaves Windows features inconsistent after driver work — review its history around the date updates began failing.
- **A wedged pending.xml.** One frozen pending file from an earlier update kills every fresh attempt at the same installer step. Delete C:\Windows\WinSxS\pending.xml only after a clean reboot fails to dislodge it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the .NET Framework 3.5 feature state

Start with the five-second diagnosis behind most 0x800f0922 cases: is .NET 3.5 actually in a clean state? The DISM feature query reports enabled, disabled, or stranded in a broken partial state — run it before and after your change.

1. Launch optionalfeatures.exe via Win + R, then open the ".NET Framework 3.5 (includes .NET 2.0 and 3.0)" node.
2. A filled-but-not-checked box means half-enabled: uncheck it completely, click OK, and restart. Unchecked-and-unneeded means leave it off and retry the update. Checked-and-healthy means look elsewhere.
3. Confirm the outcome with DISM /Online /Get-FeatureInfo /FeatureName:NetFx3 — the state should read cleanly enabled or cleanly disabled.
4. Retry the update; a large share of 0x800f0922 cases end right here.

### Fix 2: Rebuild .NET 3.5 from a fresh source

A corrupted or missing SxS payload leaves DISM with nothing to build from — unless you supply a fresh source. Check C:\Windows\Logs\CBS\CBS.log to identify the failure; it names the payload file that was absent when the .NET step collapsed.

1. In an elevated Command Prompt, run DISM /Online /Enable-Feature /FeatureName:NetFx3 /All.
2. If DISM complains about the source, mount a Windows 11 ISO and rerun as DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /Source:X:\sources\sxs /LimitAccess, swapping X for the mounted drive letter.
3. Restart once it succeeds, then retry Windows Update — the 0x800f0922 step should now clear.
4. Re-run the exact update that failed and check that no 0x800f0922 entry returns to update history.

### Fix 3: Drain the pending update queue

A single frozen pending.xml from an earlier update poisons every retry identically. This code is deterministic — unchanged retries fail unchanged — so verify each change lands.

1. Halt the update services from an elevated prompt: net stop wuauserv, then net stop bits.
2. Back up the pending file at C:\Windows\WinSxS\pending.xml and delete it when present.
3. Restart the services: net start wuauserv, then net start bits.
4. Check for updates again, then open C:\Windows\Logs\CBS\CBS.log and confirm the .NET step passed without new errors.

### Fix 4: Restore the App Readiness service

Feature configuration during updates leans on App Readiness, a favorite target of debloat tools. [the broader Windows 11 update-failure walkthrough](/articles/how-to-fix-windows-update-error-0x800f0922-in-windows-11-24h2/) When .NET 3.5 exists only because some legacy application once demanded it, decide whether that application still matters before repairing the feature.

1. Open services.msc from Win + R.
2. Set "App Readiness" — and "AppX Deployment Service (AppXSVC)" — to Manual startup.
3. If a tuner keeps disabling it, remove or reconfigure the tuner.
4. Restart, retry the update, and note the failure point: dying at a different percentage counts as progress.

### Fix 5: Rule Secure Boot in or out

Certain Dell firmware lets Secure Boot interfere with the .NET installer shim. Treat this purely as a diagnostic, never a permanent change. Note also that SupportAssist driver sessions occasionally flip Windows features as a side effect — recheck the feature state after any SupportAssist run.

1. Reboot into BIOS/UEFI setup (F2 on most Dell laptops) and find Secure Boot under Security or Boot.
2. Disable it temporarily, save, and boot Windows.
3. Retry the update; on success, re-enable Secure Boot immediately. On failure, re-enable it anyway and continue.
4. Restart once more and run a second update check for follow-on updates the first pass may have unblocked.

### Fix 6: Wipe the update cache

A damaged download can still collapse at the .NET step with the feature state perfect. The .NET 3.5 SxS payload is roughly 300 MB; when Disk Cleanup deletes it, DISM needs an external source — which is why Fix 2's ISO method exists.

1. From an elevated Command Prompt, stop the services: net stop wuauserv, net stop bits, net stop cryptsvc.
2. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
3. Start the services again — net start wuauserv, net start bits, net start cryptsvc — and check for updates to fetch a fresh payload.
4. Afterward, confirm applications depending on .NET 3.5 still launch.

### Fix 7: Heal the store with SFC and DISM

CBS store corruption destroys the transaction the .NET installer requires. Remember what 0x800f0922 means specifically — a CBS installer failed — which separates it from download errors (0x800700xx) and servicing corruption (0x80073712).

1. In an elevated Command Prompt, run sfc /scannow followed by DISM /Online /Cleanup-Image /RestoreHealth.
2. Reboot the laptop and attempt the update again.
3. If DISM cannot repair the store, abandon the automatic path for the manual install.
4. Unmount any ISO when done, keeping it around for future use.

## Closing

The cryptic code is a precise diagnosis in disguise: the .NET Framework 3.5 sub-installer is the failing piece, and every repair above aims at that exact step. Straighten the feature state, drain the pending queue, and keep the manual Catalog install ready as the bypass around the broken path. For adjacent stubborn codes, [the 24H2 edition of this error](/articles/how-to-fix-error-0x800f0922-in-windows-11-24h2/) takes the same methodical approach. Microsoft's own repair documentation is on [Microsoft's update support site](https://support.microsoft.com/en-us/windows).
