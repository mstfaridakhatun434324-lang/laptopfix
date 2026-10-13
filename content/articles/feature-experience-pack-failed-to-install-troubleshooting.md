---
title: "Feature Experience Pack Failed to Install? Troubleshoot It Here"
slug: feature-experience-pack-failed-to-install-troubleshooting
date: 2026-09-12
categories: ["windows-update"]
tags: ["feature experience pack", "install failed", "windows 11", "troubleshooting", "update"]
description: "Windows Feature Experience Pack failing to install? Understand what it is, why it fails, and how to get it installed cleanly."
thumbnail: "/images/thumbs/feature-experience-pack-failed-to-install-troubleshooting.webp"
faqs:
  - q: "What is the Windows Feature Experience Pack?"
    a: "It's a Microsoft package that delivers updates to Windows shell features — Start menu, taskbar, Settings pages, and built-in UX components — independently of full OS builds. Think of it as feature updates for the Windows 'face' without a whole version upgrade. It installs through Windows Update like any other package."
  - q: "Is it safe to ignore a failed Feature Experience Pack?"
    a: "Mostly yes — it's not a security update, so skipping it doesn't leave you vulnerable. But repeated failures can signal underlying servicing problems that will eventually block security updates too, so it's worth fixing the mechanism even if you don't care about the pack itself."
  - q: "Why does it fail when cumulative updates install fine?"
    a: "The Experience Pack uses a different servicing path (it's an AppX/provisioned-package style update rather than a classic cumulative). It trips over corrupted AppX registrations, broken Microsoft Store infrastructure, and user-profile issues that cumulative updates never touch, which is why standard update fixes often miss it."
  - q: "Can I install it manually?"
    a: "There's no standalone .msu for the Experience Pack like there is for KBs — it comes through Windows Update or the Store servicing pipeline. The fixes below repair that pipeline rather than sidestepping it, which is the only reliable path, since the pack cannot exist outside that pipeline."
---

The Windows Feature Experience Pack is one of those updates most people never notice — until it starts failing. Then it sits in Windows Update as a persistent red mark, retrying and failing, sometimes blocking the "you're up to date" status even though everything important installed fine. It's not a security update, so the stakes are low, but a perpetually failing package is both annoying and a warning sign about your servicing health.

The Experience Pack fails for different reasons than cumulative updates: it rides the AppX/Store servicing pipeline, so its enemies are corrupted app registrations, broken Store caches, and profile issues. This guide troubleshoots that specific pipeline. For classic cumulative-update failures, our [step-by-step cumulative guide](/articles/how-to-fix-cumulative-update-fails-to-install-step-by-step/) is the right page.

A useful way to think about the Experience Pack: it's closer to a Microsoft Store app update than to a Windows patch. That mental model explains everything about its failures — why Store troubleshooter fixes it, why debloat scripts break it (they remove the "apps" it updates), and why a new user profile can succeed where yours fails. Whenever you're stuck on which fix to try, ask "what would I do if a Store app wouldn't update?" and you'll usually land on the right answer.

## Why this happens

- **Corrupt AppX registrations**: The pack's package registration damaged, blocking install.
- **Broken Microsoft Store cache**: Store servicing infrastructure the pack depends on is wedged.
- **Corrupt user profile**: Profile-specific package state preventing per-user provisioning.
- **Pending Store updates deadlock**: Other stuck Store updates blocking the queue.
- **Servicing stack inconsistency**: Mismatch between the pack version and the servicing stack.
- **Third-party "debloat" damage**: Scripts that removed AppX packages the pack expects to update.
- **Insufficient space for staging**: AppX staging needs temp room like any installer.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the Store and Update troubleshooters

Cover both pipelines the pack touches.

1. **Settings > System > Troubleshoot > Other troubleshooters** → run **Windows Update**, then **Microsoft Store Apps**.
2. Apply all recommended fixes; restart.
3. Check Windows Update — the pack often installs on the next pass after troublemaker repairs.

### Fix 2: Reset the Microsoft Store cache

The pack's delivery truck.

1. Press **Win + R**, type `wsreset.exe`, press Enter — a Store window opens and closes when done.
2. Open the **Microsoft Store** → **Library** → **Get updates**; install any pending Store updates first.
3. Return to Windows Update and retry the Experience Pack.

### Fix 3: Re-register the pack's AppX package

Repair the damaged registration directly.

1. Elevated PowerShell: `Get-AppxPackage -AllUsers *WindowsFeatureExperiencePack* | Format-List Name, PackageFullName, Status`. If the command returns nothing at all, the package was removed entirely (likely by a debloat script) — skip to Fix 7, since re-registration needs something to re-register.
2. If Status shows anything odd, re-register: `Get-AppxPackage -AllUsers *WindowsFeatureExperiencePack* | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`. Run this exactly as written; the `-DisableDevelopmentMode` flag is what makes it a repair rather than a sideload.
3. Restart and retry the update. If PowerShell throws red errors about missing manifests, the package files themselves are gone — again, that's a Fix 7 situation, not a Fix 3 one.

### Fix 4: Clear the update cache

For when the downloaded pack copy is corrupt.

1. Elevated Terminal: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Rename `C:\Windows\SoftwareDistribution` → `SoftwareDistribution.old`.
3. Restart services; check for updates for a fresh pack download.

### Fix 5: Test in a new user profile

Isolate profile-level corruption.

1. **Settings > Accounts > Other users** → add a new local administrator account.
2. Sign into it, run Windows Update — if the pack installs there, your main profile's package state is corrupt.
3. Migrate to the new profile (or repair the old one's AppX state) rather than fighting the broken one.

### Fix 6: Repair system files

Deep servicing damage affects the pack pipeline too.

1. Elevated Terminal: `DISM /Online /Cleanup-Image /RestoreHealth`, then `sfc /scannow`. Budget 20–40 minutes for the pair; DISM's restore phase is slow because it's rebuilding damaged payloads from Windows Update, which is itself part of what you're repairing.
2. Restart; retry. If DISM fails to find a repair source — a real possibility when the servicing pipeline is the thing that's broken — mount a Windows 11 ISO and point DISM at it with the `/Source` parameter instead of relying on the online source.
3. Microsoft's servicing-repair guidance is at the [Windows update support hub](https://support.microsoft.com/en-us/windows). After the repair, run the Store troubleshooter once more (Fix 1) before retrying the pack — the two pipelines interact, and fixing one sometimes unblocks the other.

### Fix 7: In-place upgrade to rebuild servicing

The definitive pipeline rebuild.

1. Download the Windows 11 ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Mount → `setup.exe` → **Keep personal files and apps**.
3. The upgrade reinstalls the AppX and servicing infrastructure the pack needs.

## Closing

Feature Experience Pack failures are low-stakes but informative — they point at the AppX/Store servicing pipeline, a corner of Windows most troubleshooting ignores. Fix the pipeline (Store cache, registrations, profile health) and the pack installs quietly, as it was always meant to. And if it ever fails again without blocking anything else, you'll know exactly which three fixes to try first.

There's a broader takeaway worth pocketing: modern Windows has several independent servicing pipelines — classic Windows Update, the Store/AppX pipeline, and driver delivery — and they fail independently. A healthy cumulative-update history doesn't prove the Store pipeline is healthy, just as a working Store doesn't prove drivers are fine. When something fails, identify *which* pipeline it rides before troubleshooting; applying Windows Update fixes to a Store-pipeline problem is the most common reason these repairs "don't work." Diagnose the pipeline, fix the pipeline — and the Feature Experience Pack goes back to being the invisible, boring update it was designed to be. For the closely related case where the pack fails specifically after a Windows 11 update, see our [post-update Experience Pack guide](/articles/how-to-fix-feature-experience-pack-failed-to-install-after-windows-11-update/).
