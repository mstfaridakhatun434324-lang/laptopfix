---
title: "How to Fix Windows Update Error 0x80070643 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80070643-in-windows-11-24h2
date: 2026-10-11
categories: ["windows-update"]
tags: ["windows update", "0x80070643", "error code", "windows 11", "defender"]
description: "Error 0x80070643 is a fatal install failure, common with .NET and Defender updates. Identify the failing update and apply the right fix."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070643-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80070643 mean?"
    a: "It is ERROR_INSTALL_FAILURE — a fatal error inside the update's own installer. The code alone does not say why; the identity of the failed update does. On Windows 11 24H2 the famous variants are the WinRE partition update failing for lack of recovery-partition space, corrupted .NET installs, and stuck Defender definition updates. Match the fix to the update."
  - q: "Is the WinRE partition failure dangerous?"
    a: "No, it is just annoying. The failing update cannot resize your recovery partition itself, so it aborts safely and your PC keeps working normally — including recovery tools. You can hide that specific update and wait for a superseding one, or resize the partition manually if you are comfortable with Disk Management."
  - q: "Will the .NET repair tool delete my apps?"
    a: "No. The Microsoft .NET Framework Repair Tool only repairs the .NET Framework system components — it re-registers libraries and fixes configuration data. Your applications and their data are untouched. A restart afterward lets everything pick up the repaired framework cleanly."
  - q: "Why does this error keep returning every Patch Tuesday?"
    a: "Because the underlying damage never got fixed — each month's update trips over the same broken .NET install, stuck Defender state, or cramped WinRE partition. Fix the root cause with the matching fix above rather than retrying the update, and the monthly failures stop."
---

Error 0x80070643 — "fatal error during installation" — is the chameleon of update errors: it appears with .NET Framework updates, Defender security intelligence updates, and Office updates alike. The code only tells you the installer died; the identity of the failed update, visible in update history, tells you why. On 24H2 the most infamous variant is the WinRE partition update that fails for lack of recovery-partition space.

Under the hood, 0x80070643 means a fatal error during installation — the update's installer itself failed. Technically it is ERROR_INSTALL_FAILURE: the MSI or update installer returned a fatal error during the install phase. On 24H2 it is notorious with .NET Framework updates, Microsoft Defender definition updates, and Office Click-to-Run updates — each with its own sub-cause.

The encouraging part: 0x80070643 is one of the better-understood update errors, and the fixes below are ordered from quickest to most thorough. Work through them in sequence — most readers never need the last two.

## Why this happens

- **The WinRE recovery partition is too small.** The well-known KB5034441-style failure: the update needs ~250 MB free in the recovery partition and aborts without it.
- **Corrupted .NET Framework installation.** .NET updates fail fatally when the existing framework install is damaged.
- **Defender definition update conflicts.** Stuck definition states or corrupted signature stores make the intelligence update fail.
- **Office Click-to-Run in a broken state.** Office updates ride the same installer engine and fail with this code when Click-to-Run is damaged.
- **A pending restart blocking the installer.** The installer refuses to run while another installation awaits a reboot.
- **Corrupted SoftwareDistribution state.** Damaged cache metadata makes the installer launch against broken files.
- **Third-party software blocking MSI operations.** Some security tools interfere with the Windows Installer service itself.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify which update is actually failing

Everything about 0x80070643 depends on the update's identity — the WinRE partition fix, the .NET repair, and the Defender fix are completely different. Check first, then jump to the matching fix.

1. Open **Settings > Windows Update > Update history** and find the 0x80070643 failure.
2. Note whether it is a **.NET Framework** update, a **Security Intelligence Update for Microsoft Defender**, an **Office** update, or a **recovery/WinRE** update.
3. For WinRE/recovery updates, go to Fix 2. For .NET, Fix 3. For Defender, Fix 4. For Office, Fix 5. Once you have the KB number in hand, you can also fetch it directly from the Catalog — the [manual install walkthrough for 24H2](/articles/how-to-manually-install-windows-update-in-windows-11-24h2/) shows the exact steps.
4. For anything else, continue with Fix 6.

### Fix 2: Fix the WinRE partition space problem

The notorious recovery-partition variant: the update needs free space in the hidden WinRE partition. Rather than risky partition surgery, the safe modern approach is Microsoft's own resolution path.

1. Confirm this is the WinRE variant: the failed update mentions recovery or WinRE in its title.
2. Check Microsoft's current guidance for the specific KB — for some of these updates Microsoft has issued revised packages or declared them superseded.
3. The safest general fix: ensure the recovery partition has free space by shrinking C: slightly in Disk Management and extending the recovery partition — back up first.
4. Alternative low-risk path: hide the specific failing update with the Show/Hide troubleshooter package and wait for the superseding update.

### Fix 3: Repair the .NET Framework installation

When a .NET update fails fatally, the existing framework install is usually damaged. Microsoft's .NET repair tool fixes the underlying install so the update can apply.

1. Download the **Microsoft .NET Framework Repair Tool** from Microsoft's website.
2. Run it, accept the license, and let it diagnose the installed .NET versions.
3. Apply its recommended fixes and restart when prompted.
4. Retry the .NET update in **Settings > Windows Update**.

### Fix 4: Fix a stuck Defender intelligence update

Defender definition updates fail with 0x80070643 when the signature store is stuck. Clearing it forces a clean re-download of definitions.

1. Open Windows Security > **Virus & threat protection > Protection updates** and click **Check for updates** there first.
2. If it fails, open an administrator Command Prompt and run `cd %ProgramFiles%\Windows Defender` then `MpCmdRun.exe -RemoveDefinitions -All`.
3. Then run `MpCmdRun.exe -SignatureUpdate` to pull fresh definitions directly.
4. Return to Windows Update and confirm the intelligence update clears.

### Fix 5: Repair Office Click-to-Run (Office update variant)

Office updates that fail with 0x80070643 usually mean the Click-to-Run engine is damaged. An online repair rebuilds it without touching your documents.

1. Open **Settings > Apps > Installed apps**, find **Microsoft 365** or **Office**, and click the three dots > **Modify**.
2. Choose **Online Repair** (not Quick Repair) and let it run — it re-downloads Office components.
3. Restart the PC when the repair finishes.
4. Check for updates again; the Office update should now install.

### Fix 6: Reset the Windows Update components

When 0x80070643 keeps returning no matter what you try, the update engine's own cache is usually the culprit. Stopping the services, renaming the SoftwareDistribution and catroot2 folders, and restarting forces Windows to rebuild its download state from scratch — no personal data is touched.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, and `net start cryptsvc`.
4. Go to **Settings > Windows Update**, check for updates, and see whether 0x80070643 is gone.

### Fix 7: Do an in-place upgrade as a last resort

When nothing else clears 0x80070643, the servicing stack itself is too damaged for targeted repair. An in-place upgrade reinstalls Windows 11 24H2 over your existing install while keeping files and apps. Grab the ISO from [Microsoft's official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) — never from a third-party mirror.

1. Download the Windows 11 ISO from Microsoft, double-click it to mount it, and run `setup.exe`.
2. Accept the license terms and choose **Keep personal files and apps** when asked what to keep.
3. Let setup run to completion — 30 to 90 minutes with several restarts. Do not force a shutdown mid-way.
4. After signing in, run **Settings > Windows Update** once more to confirm 0x80070643 no longer appears.

## Closing

0x80070643 rewards detective work: name the failing update, then apply its specific fix. The WinRE, .NET, Defender, and Office variants each have clean resolutions. For anything else failing the same way, the [component reset](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) and our [24H2 update error guide](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) cover the general cases. Microsoft documents installer failures in its [Windows support hub](https://support.microsoft.com/en-us/windows).
