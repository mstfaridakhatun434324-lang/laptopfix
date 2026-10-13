---
title: "How to Fix the Feature Experience Pack Failed to Install on Windows 10"
slug: "how-to-fix-feature-experience-pack-failed-to-install-on-windows-10"
date: 2026-10-12
categories: ["windows-update"]
tags: ["feature experience pack", "windows update", "windows 10", "failed to install"]
description: "Feature Experience Pack failed to install on Windows 10? Six fixes covering prerequisites, cache resets, and service repairs for this stubborn small package."
thumbnail: "/images/thumbs/how-to-fix-feature-experience-pack-failed-to-install-on-windows-10.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "The Windows Feature Experience Pack is a small Microsoft package that updates select Windows shell and feature components independently of full OS upgrades. On Windows 10 it arrives through Windows Update. Its contents are minor — UI and experience refinements — which is why a failed install is more useful as a diagnostic signal of update-pipeline trouble than as a loss worth mourning."
  - q: "Do I actually need the Feature Experience Pack?"
    a: "For most users, no. The pack delivers minor shell and experience refinements, not security fixes. Security comes through the cumulative updates, which are unaffected by the pack’s failure. That said, treat a failed pack as an early warning: the same cache corruption or service problem will likely break the next cumulative update, so fix the pipeline now rather than ignoring it."
  - q: "Can a missing cumulative update block the pack?"
    a: "Yes, indirectly. The pack’s installer checks that the system is at a minimum cumulative update level before applying. If your Windows 10 is months behind on cumulative updates, install the latest cumulative update first — via Windows Update or manually from the Microsoft Update Catalog — then retry the Feature Experience Pack. The prerequisite chain is a common hidden cause of pack failures."
  - q: "Where do I see the failed pack entry?"
    a: "On Windows 10, open Settings, then Update and Security, then Windows Update, and click View update history. Failed Feature Experience Pack entries appear with their error codes. If nothing is listed there, check Settings, then Apps, for the pack entry, or simply run Check for updates — Windows will re-offer the pack automatically once the underlying pipeline is repaired."
---

The Windows Feature Experience Pack is a small bundle — tens of megabytes, not gigabytes — which makes its repeated failure on Windows 10 feel disproportionate. It downloads, attempts to install, fails, and Windows Update offers it again tomorrow like nothing happened. The pack itself contains minor shell refinements, so the frustration is less about missing features and more about the nagging sense that updates are broken.

That instinct is correct: a pack that cannot install usually means the update pipeline underneath it has a problem that will soon affect bigger updates too. The Windows 11 variant of this failure is covered separately in the [Windows 11 Feature Experience Pack guide](/articles/how-to-fix-feature-experience-pack-failed-to-install-on-windows-11/).

## Why this happens

- **Feature Experience Pack delivered via a stuck queue:** On Windows 10 the pack arrives through Windows Update’s feature pipeline; a jammed queue blocks it like any other payload.
- **Corrupted update cache:** Damaged SoftwareDistribution metadata makes the small pack fail its integrity check even though the download is tiny.
- **Missing prerequisite cumulative update:** The pack sometimes requires a minimum cumulative update level; without it, the installer refuses the package.
- **Disabled Windows Update services:** Debloat scripts that disable wuauserv or BITS break the pack’s delivery while leaving the rest of Windows superficially fine.
- **Metered connection deferral:** As a non-critical payload, the pack is deferred on metered connections indefinitely.
- **Corrupted system files in shell components:** The pack updates shell-adjacent components; damaged base files cause the install to fail at application time.
- **Insufficient permissions on package staging:** ACL damage on the staging folders produces access-denied failures for the pack’s installer.

## How to fix it
Work through these in order — diagnose first, then act.

### Fix 1: Bring the cumulative update base current first

The pack is built against a recent servicing baseline. If your Windows 10 has skipped several cumulative updates, the pack installer fails its prerequisite check. Bringing the base current first resolves this silently and also patches security gaps.

1. Open Settings > Update & Security > Windows Update and install any pending cumulative updates first.
2. Restart when prompted — do not skip the reboot.
3. After rebooting, click Check for updates again and look for the Feature Experience Pack.
4. Install it on the now-current base.

### Fix 2: Reset the update cache

For a package this small, cache corruption is the most disproportionate cause of failure: a few damaged metadata bytes block a 50 MB payload. The standard component reset clears it in minutes.

1. Run Command Prompt as administrator.
2. Stop the services: net stop wuauserv, net stop bits, net stop cryptSvc.
3. Rename: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old.
4. Restart the services with net start and check for updates — the pack should reappear with fresh metadata.

### Fix 3: Repair system files with DISM and SFC

Because the pack touches shell components, damaged system files beneath it cause application-time failures. DISM repairs the component store and SFC repairs the files drawn from it — the standard one-two for any package that fails while applying.

1. Open an elevated Command Prompt.
2. Run: DISM /Online /Cleanup-Image /RestoreHealth and wait for completion.
3. Follow with: sfc /scannow.
4. Restart and retry the pack install.

### Fix 4: Re-enable disabled update services

Debloat and privacy scripts love disabling the update services, which breaks the pack’s delivery channel while Windows otherwise seems fine. The pack cannot arrive if its transport is switched off — restore the services and it flows again.

1. Press Win + R, type services.msc, and verify Windows Update and Background Intelligent Transfer Service are not Disabled.
2. Set both to Manual (Trigger Start) if a debloat tool changed them.
3. Start both services.
4. Check for updates again.

### Fix 5: Rule out metered-connection deferral

Non-critical payloads are the first casualties of metering. If the pack is the only thing failing while cumulative updates succeed, a metered flag is the likely discriminator — cumulative updates may be allowed through while the pack waits indefinitely.

1. Check Settings > Network & Internet > Wi-Fi (or Ethernet) > your network for a metered flag and switch it off.
2. Alternatively, allow the download: Update & Security > Windows Update > Advanced options, enable downloads over metered connections.
3. Retry the pack install.
4. For the full metered walkthrough see the [metered connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-on-windows-10/).

### Fix 6: Install the pack manually from the Update Catalog

The Catalog hosts the pack as a standalone package, bypassing the Windows Update client entirely. A successful manual install both delivers the pack and proves the system itself is healthy — pointing the finger squarely at the client pipeline if automatic delivery keeps failing.

1. Note the KB number from the failed entry in Update history.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/).
3. Download and install the package manually.
4. Verify success in Update history, then confirm automatic updates still work next cycle.

### Fix 7: Run the built-in troubleshooters as a final automated pass

After the manual repairs above, the built-in Windows Update troubleshooter deserves one more run — partly as verification, partly because on a now-healthy system it can clear residual state the manual steps missed. On Windows 10 it lives at Settings > Update & Security > Troubleshoot > Additional troubleshooters. If the troubleshooter itself misbehaves, that is a separate (and fixable) problem from the pack failure.

1. Open Settings > Update & Security > Troubleshoot > Additional troubleshooters.
2. Run the Windows Update troubleshooter and apply any fixes it suggests.
3. Restart the laptop after it completes.
4. Check for updates — the Feature Experience Pack should now download and install.
5. If the pack still fails, install it manually from the Update Catalog as the definitive workaround.

## Closing

A failed Feature Experience Pack on Windows 10 is a delivery problem, not a missing feature worth chasing for its own sake — the pack’s changes are minor. Still, its failure often signals update-pipeline trouble that will hit the next cumulative update too, so run the repairs: update the cumulative base, reset the cache, and let the pack come through cleanly.
