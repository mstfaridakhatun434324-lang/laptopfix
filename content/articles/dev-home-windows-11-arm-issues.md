---
title: "How to Fix Dev Home Problems on Windows 11 ARM"
slug: dev-home-windows-11-arm-issues
date: 2026-10-23
categories: ["ai-pc"]
tags: ["dev home", "windows 11", "arm64", "dev drive", "dashboard", "troubleshooting"]
description: "Fix Dev Home issues on Windows 11 ARM: blank dashboards, GitHub sign-in failures, broken Dev Drive setup, widget errors, and app launch problems, fixed."
thumbnail: "/images/thumbs/dev-home-windows-11-arm-issues.webp"
faqs:
  - q: "Why is my Dev Home dashboard blank on ARM Windows?"
    a: "Blank dashboards are usually a widget-host or extension problem: an outdated Widgets platform component, a disabled extension, or corrupted dashboard state. Updating Dev Home and the Widgets platform from the Microsoft Store, then re-adding widgets one at a time, resolves it in most cases."
  - q: "Why does Dev Home fail to create a Dev Drive?"
    a: "Dev Drive creation needs virtualization enabled in the firmware, the ReFS-capable storage stack, and enough unallocated or shrinkable disk space. On ARM laptops the most common blocker is virtualization disabled in UEFI, followed by trying to create the drive on an external or BitLocker-locked volume."
  - q: "Why can't Dev Home sign in to GitHub?"
    a: "The GitHub extension stores OAuth tokens in Windows Credential Manager, and stale or revoked tokens cause silent sign-in failures. Removing the stored GitHub credentials and signing in fresh through the extension almost always fixes it."
  - q: "Is Dev Home still supported on Windows 11?"
    a: "Microsoft has scaled back Dev Home's development, but the app remains installable and functional on Windows 11 including ARM64. If you depend on features that stop working, the individual pieces — Dev Drive, winget, Windows Terminal — all work standalone without Dev Home."
---

You installed Dev Home on your Snapdragon laptop for the developer dashboard, one-click environment setup, and Dev Drive — but the dashboard loads blank, GitHub sign-in loops, Dev Drive creation fails cryptically, or the app will not launch. The promise was streamlined setup; the reality is another troubleshooting session.

On Windows 11 on ARM, Dev Home's problems cluster around a few components: the Widgets platform it renders on, its GitHub/Azure extensions, the virtualization and storage stack Dev Drive needs, and the app's own cached state. These are integration points where an ARM machine's configuration differs from what the setup wizard assumed.

This guide gives you six fixes in dependency order: update the app and its platform, fix sign-in, repair the dashboard, get Dev Drive creation working, fix environment setup, and finish with a full reset when the app itself is corrupt.

## Why this happens

- **Outdated Dev Home or Widgets platform:** Dev Home renders its dashboard on the Windows Widgets platform. If either component is stale, widgets fail to load or the whole dashboard goes blank.
- **Stale GitHub OAuth tokens:** The GitHub extension caches tokens in Credential Manager. Revoked, expired, or half-migrated tokens produce sign-in loops with no useful error.
- **Virtualization disabled in firmware:** Dev Drive and some environment features need the hypervisor. Many ARM laptops ship with virtualization off in UEFI, and Dev Home's error message does not say so plainly.
- **Unsuitable target disk for Dev Drive:** Dev Drive needs ReFS on an internal volume with available space — external drives, SD cards, and fully-allocated disks all fail creation.
- **Corrupted app state or extension cache:** Interrupted updates leave Dev Home's local state inconsistent, with dashboard layouts referencing widgets that no longer exist.
- **Missing optional Windows features:** Components like the Virtual Machine Platform or specific .NET runtimes may be absent on a fresh ARM install, and Dev Home assumes they are present.
- **Extension version skew:** The GitHub or Azure extension updating independently of Dev Home can produce API mismatches that surface as blank widgets or failed operations — the same version-skew class of problem behind [MIPI camera driver errors on AI laptops](/articles/mipi-camera-driver-error-ai-laptop/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Update Dev Home, extensions, and the Widgets platform

Many Dev Home issues are simply stale components disagreeing with each other. Update everything in the chain before diagnosing deeper.

1. Open the **Microsoft Store**, go to **Library**, and install all pending updates — especially **Dev Home**, **Dev Home GitHub Extension**, and the **Widgets** platform components.
2. Restart the laptop after updates; the Widgets platform hosts out-of-process and a reboot ensures the new versions actually load.
3. In Dev Home, check **Settings > Extensions** — every extension should show as enabled and up to date, with no error badges.
4. If an extension shows an error, disable and re-enable it, then restart Dev Home from Task Manager (end the task; it relaunches cleanly).
5. Retest the failing feature before moving on — dashboard, sign-in, or setup — since updates alone resolve a large share of reports.

### Fix 2: Fix GitHub and Azure DevOps sign-in

When the extension shows you as signed out, loops on sign-in, or widgets say "authentication required" forever, the stored credential is almost always the problem — not your account.

1. Open **Credential Manager > Windows Credentials** and delete every entry mentioning **GitHub** or **Dev Home**.
2. In Dev Home, go to **Settings > Accounts** (or the extension's accounts page) and sign in fresh — complete the full browser OAuth flow rather than reusing a remembered session.
3. If the browser flow never completes, confirm your default browser reaches github.com and no VPN or proxy intercepts the callback.
4. After sign-in, verify in the extension settings that the account shows as connected with the right username before touching widgets.
5. Re-add one GitHub widget and confirm it populates — if it does, the token was the whole story. Token hygiene matters across the platform; similar credential staleness causes [work-account sign-in loops in the Copilot app](/articles/copilot-app-work-account-sign-in/) too.

### Fix 3: Repair a blank or broken dashboard

A dashboard that loads empty, shows perpetual spinners, or throws widget errors is usually corrupted layout state or a dead widget host — not a dead app.

1. In Dev Home, remove all widgets from the dashboard (or as many as it lets you), then restart Dev Home.
2. Re-add widgets **one at a time**, waiting for each to populate before adding the next — the widget that breaks the dashboard identifies itself.
3. If the dashboard will not even render the "add widget" UI, reset the app's state: **Settings > Apps > Installed apps > Dev Home > Advanced options > Repair**, then **Reset** if Repair does not help.
4. After a Reset, sign in again (Fix 2) before judging the dashboard — a signed-out dashboard legitimately shows less.
5. Do not restore a widget layout synced from an x64 machine wholesale; rebuild it natively instead.

### Fix 4: Get Dev Drive creation working

Dev Drive failures give the least helpful errors in the app. Satisfy the prerequisites manually and creation usually succeeds on the next attempt.

1. Enable virtualization: restart into UEFI/BIOS and turn on the virtualization option (often under Security or Advanced), then in Windows enable **Virtual Machine Platform** via **Turn Windows features on or off**.
2. Confirm the target disk: Dev Drive must live on an internal drive with unallocated space or shrinkable partitions — not a USB drive, SD card, or network volume.
3. Use **Disk Management** to shrink the Windows partition, leaving unallocated space for the Dev Drive (32 GB minimum; 50+ GB is comfortable).
4. Temporarily suspend BitLocker on the target disk during creation if it is enabled — re-enable it after the Dev Drive is created and formatted.
5. Retry creation in Dev Home; if it still fails, create the ReFS volume manually in Disk Management and then point Dev Home at it. Storage-stack quirks on new hardware are not unique to Dev Home — [DirectStorage detection problems on ARM laptops](/articles/directstorage-not-working-arm-laptop/) come from the same young-driver territory.

### Fix 5: Repair machine configuration and environment setup

Environment-setup flows that stall, fail halfway, or report false success usually hit missing prerequisites or a winget/DSC hiccup beneath Dev Home's UI.

1. Open an elevated **Windows Terminal** and run `winget --version` — Dev Home's setup engine leans on winget, and a broken winget breaks setup silently.
2. Run the failing configuration's steps manually where possible: install the listed apps via winget yourself to see the real error message Dev Home swallowed.
3. Check **Settings > Accounts** in Dev Home — some setup flows need the GitHub sign-in from Fix 2 before they can clone or configure anything.
4. Check `%LOCALAPPDATA%\DevHome\logs` after a failed run; the logs name the actual failing step.
5. For Desired State Configuration failures, ensure the **PowerShell 7 ARM64** host is healthy first — a broken shell host (see our [PowerShell 7 on ARM guide](/articles/powershell-7-arm-windows-issues/)) undermines everything built on it.

### Fix 6: Fully reset Dev Home when the app itself is corrupt

If the app will not launch, crashes on the dashboard, or every feature fails after the fixes above, stop repairing pieces and reset everything.

1. Back up anything valuable: export dashboard intent (screenshots of the layout), and note your Dev Drive letter — the drive itself survives an app reset.
2. Go to **Settings > Apps > Installed apps > Dev Home > Advanced options** and click **Reset** (use Repair first if you have not already).
3. If Reset is unavailable or the app will not uninstall cleanly, uninstall Dev Home and its extensions from the Store library, restart, and reinstall Dev Home fresh.
4. On first launch, sign in (Fix 2) before rebuilding the dashboard — widgets added while signed out can stick in a broken state.
5. Check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for any servicing updates for your Windows build — Dev Home's platform dependencies ship through Windows Update, and a pending update can be the missing piece. If you are doing a broader refresh, the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) has the latest installation media.

## Closing

Dev Home on ARM Windows breaks at its integration points — stale platform components, expired GitHub tokens, disabled virtualization, corrupted dashboard state — not in its core logic. Update the chain, refresh credentials, satisfy the Dev Drive prerequisites, and reset when state goes bad. If your troubles are camera-related rather than dashboard-related, the same driver-update discipline applies — see how a [camera-black driver update fixes Studio Effects](/articles/studio-effects-camera-black-driver-update/).
