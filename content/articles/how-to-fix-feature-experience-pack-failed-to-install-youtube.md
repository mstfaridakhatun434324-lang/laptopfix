---
title: "How to Fix ‘Feature Experience Pack Failed to Install’"
slug: how-to-fix-feature-experience-pack-failed-to-install-youtube
date: 2026-09-17
categories: ["windows-update"]
tags: ["feature experience pack failed", "microsoftwindows.client.cbs", "windows 11 update error", "appx update failed"]
description: "'Feature Experience Pack failed to install' in update history? Fix the AppX deployment stack, reset the Store cache, and clear the stuck package update."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-youtube.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It is a Microsoft package (MicrosoftWindows.Client.CBS) that updates built-in Windows experiences — taskbar, quick settings, parts of Settings — independently of full OS updates. It lets Microsoft ship shell improvements faster. Its updates are small and non-security, but they should still install cleanly."
  - q: "Is it dangerous to ignore a failed Feature Experience Pack?"
    a: "Not dangerous, but not ideal. You miss minor shell improvements, and the stuck entry can clutter update history or hold up the queue. The underlying cause (often AppX corruption) can also affect Store apps. Fifteen minutes of fixes is worth it."
  - q: "Why do debloat tools break the Experience Pack?"
    a: "Because they remove its AppX package to 'declutter' Windows. Once the inbox package is gone, its updates fail permanently — there is nothing to update. Restoring defaults in the tool or doing an in-place upgrade are the only real fixes."
  - q: "Will resetting the Microsoft Store delete my apps?"
    a: "No. wsreset.exe only clears the Store's cache — your installed apps, purchases, and settings are untouched. It is one of the safest troubleshooting commands in Windows, and it resolves a surprising number of pack and Store-app issues. Run it any time the Store itself behaves oddly, too."
---

The 'Feature Experience Pack failed to install' error looks alarming but is one of the more benign Windows Update failures. The Windows Feature Experience Pack (the MicrosoftWindows.Client.CBS package) delivers updates to built-in experiences — the taskbar, Settings pages, and shell components — separately from the main OS. When its update fails, your laptop keeps working normally; you are just missing the latest tweaks to those built-in features. [the Feature Experience Pack failing in 24H2](/articles/how-to-fix-feature-experience-pack-failed-to-install-in-windows-11-24h2/)

The failure itself usually comes down to the servicing stack mishandling this particular package type, or the Microsoft Store infrastructure it depends on being in a bad state. Because the pack is small and self-contained, the fixes are quick — most people clear it in under twenty minutes with the steps below.

## Why this happens

- **Corrupted AppX deployment state.** The pack installs via the AppX stack; corruption there fails it. Get-AppxPackage -AllUsers *MicrosoftWindows.Client.CBS* shows its state.
- **Microsoft Store cache corruption.** The pack's delivery depends on Store infrastructure. wsreset.exe is safe; it only clears the cache, not apps.
- **App Readiness service disabled.** Needed to stage the pack's components. Both services should be Manual in services.msc.
- **Servicing stack mishandling.** The CBS engine failing on this specific package type. SSU updates are listed separately on the Catalog.
- **Corrupted update cache.** Damaged payload in SoftwareDistribution. The payload lives in SoftwareDistribution like any update.
- **Pending restart blocking.** A previous update's pending state blocking the pack. A reboot clears most pending states; check WinSxS\pending.xml.
- **Third-party debloat removal.** Debloat tools removing the pack's components, breaking its update. Restore the tool's defaults or accept the in-place upgrade path.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart and retry once

Clear any transient pending state before doing real repairs. The Windows Feature Experience Pack (MicrosoftWindows.Client.CBS) updates shell experiences — taskbar, quick settings, Settings pages — independently of the OS build.

1. Restart the laptop normally.
2. Open Settings > Windows Update and click Retry.
3. If the pack installs, you are done — it was a transient lock.
4. If it fails again with the same error, continue.
5. One clean retry rules out the trivial cases.
6. Retry the Feature Experience Pack update in Settings > Windows Update and confirm it installs.

### Fix 2: Reset the Microsoft Store cache

The pack depends on Store infrastructure; a corrupt cache breaks it. Its updates install through the AppX deployment stack rather than pure CBS servicing, which is why standard update resets only half-work here.

1. Press Win + R, type wsreset.exe, and press Enter.
2. Wait for the Store to open automatically (this confirms the reset).
3. Close the Store and retry the update.
4. If wsreset hangs, continue to the AppX re-registration.
5. This is safe and touches nothing else.
6. Check update history to confirm the pack entry now shows as successful.

### Fix 3: Enable the AppX deployment services

The pack needs these services running to stage its components. [a cumulative update that fails to install](/articles/how-to-fix-cumulative-update-fails-to-install-in-windows-11-24h2/) The pack depends on the Microsoft Store infrastructure, so a corrupt Store cache (fixed by wsreset.exe) breaks its updates too.

1. Press Win + R, type services.msc, and press Enter.
2. Set 'AppX Deployment Service (AppXSVC)' to Manual and start it.
3. Set 'App Readiness' to Manual and start it.
4. Set 'Client License Service (ClipSVC)' to Manual as well.
5. Retry the Feature Experience Pack update.
6. Open the Microsoft Store and confirm it loads correctly, proving the shared infrastructure is healthy.

### Fix 4: Re-register the pack's AppX package

Repair the installed pack package directly with PowerShell. App Readiness and AppX Deployment Service must be running for the pack to stage; debloat tools love to disable both.

1. Open PowerShell as administrator.
2. Run: Get-AppxPackage -AllUsers *MicrosoftWindows.Client.CBS* to confirm it is present.
3. If present but broken, re-register it: Get-AppxPackage -AllUsers *MicrosoftWindows.Client.CBS* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}.
4. Restart and retry the update.
5. If the package is missing entirely, debloat tools likely removed it — see below.
6. Verify App Readiness and AppXSVC are still running after a reboot.

### Fix 5: Undo debloat tool damage

Some debloat scripts remove the Experience Pack, breaking its updates permanently. Debloat scripts that remove the pack's AppX package break its updates permanently — there is nothing left to update.

1. If you ran a debloat tool, re-run it and restore defaults.
2. Alternatively, reinstall the pack via PowerShell: Add-AppxPackage -Register with the system package path.
3. As a cleaner path, do an in-place upgrade repair (last fix) which restores all inbox packages.
4. Avoid debloat tools that remove inbox AppX packages.
5. Removing system packages always breaks their updates eventually.
6. Run a Store app update to confirm the AppX stack works beyond the pack.

### Fix 6: Reset the Windows Update cache

Clear the standard update pipeline in case the payload is corrupt. A failed pack is harmless day-to-day but its stuck queue entry can hold up other updates behind it.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Rename C:\Windows\SoftwareDistribution to SoftwareDistribution.old.
4. Restart the services and retry.
5. This handles the cases where the pack's payload itself was damaged.
6. If you re-registered the package, confirm it with Get-AppxPackage *MicrosoftWindows.Client.CBS*.

### Fix 7: Run SFC and DISM

Repair the shell components the pack patches. Re-registering the package with Add-AppxPackage repairs the local install without touching user data.

1. Open Command Prompt as administrator and run: sfc /scannow.
2. Then: DISM /Online /Cleanup-Image /RestoreHealth.
3. Restart and retry the pack update.
4. Component store damage is a common root cause for repeated pack failures.
5. Clean results here point back to the AppX side.
6. Check that pending cumulative updates now proceed, proving the queue is unblocked.

## Closing

The Feature Experience Pack is small, self-contained, and quick to fix once you target its actual dependencies — the AppX stack and the Store cache rather than generic update machinery. Clear those, and the monthly pack updates install quietly in the background again. For bigger update failures, [the pack failing on other brands](/articles/how-to-fix-feature-experience-pack-failed-to-install-on-dell-laptop/) handles those. For Microsoft's own documentation on these repairs, see [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows).
