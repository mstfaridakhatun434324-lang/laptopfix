---
title: "How to Fix Windows Update Error 0x800F081F"
slug: fix-windows-update-error-0x800f081f
date: 2026-10-01
categories: ["windows-update"]
tags: ["windows update", "0x800f081f", "error code", "windows 11"]
description: "Error 0x800F081F blocking your Windows updates? It means missing source files. Here are 6 fixes — DISM source repair, .NET reinstall, and in-place upgrade."
thumbnail: "/images/thumbs/fix-windows-update-error-0x800f081f.webp"
faqs:
  - q: "What does error 0x800F081F actually mean?"
    a: "It is CBS_E_SOURCE_MISSING: Windows needs a file payload to finish installing an update or feature, but cannot find a valid copy anywhere — not in the component store, not on Windows Update. The fix is to repair the component store or point Windows at a known-good source, such as a Windows installation ISO."
  - q: "Can I fix 0x800F081F without a Windows ISO?"
    a: "Sometimes. The built-in troubleshooter and a plain DISM RestoreHealth (without a source path) fix mild component-store damage because they pull clean files from Windows Update. You need an ISO or installation media only when that fails — a sign the store is too damaged or the payload is blocked from downloading."
  - q: "Why does this error appear when enabling .NET Framework 3.5?"
    a: "The .NET Framework 3.5 payload is not included in a default Windows 11 install, so Windows must fetch it from Windows Update or from installation media when you turn the feature on. If that download is blocked — by a metered connection, a proxy, or a damaged component store — the enablement fails with 0x800F081F."
  - q: "Will an in-place upgrade delete my files and apps?"
    a: "No, as long as you choose Keep personal files and apps during setup. An in-place upgrade reinstalls Windows over itself and preserves your data, programs, and most settings. It is still wise to back up important files first, because a power loss or crash during the upgrade could cause data loss."
---

Error 0x800F081F is one of the more cryptic failures Windows Update can throw. It usually appears when installing a cumulative update or when enabling .NET Framework 3.5, and the accompanying message — "the source files could not be found" — sends most people straight to a search engine without much hope of a clear answer.

Technically, the code is CBS_E_SOURCE_MISSING: Windows needs a file payload to complete the installation but cannot find a valid copy anywhere it looks — not in the local component store, not from Windows Update. Laptops run into it often because aggressive cleanup tools strip the local payload, metered connections block the download, or the component store is already damaged from a previously interrupted update. The good news: because the cause is literally "missing files," pointing Windows at a known-good source usually fixes it.

## Why this happens

- **A damaged component store.** Corrupted or incomplete files in the WinSxS store mean Windows has nothing valid to build the update from, so it reports the source as missing.
- **The .NET Framework 3.5 payload was never downloaded.** The payload isn't part of a default Windows 11 install; if Windows Update can't reach it (metered connection, proxy, WSUS restriction), enabling the feature fails with this exact code.
- **DISM ran without a valid /Source.** Repair attempts that can't reach Windows Update fall back to the same broken local store and fail again with 0x800F081F.
- **Over-aggressive disk cleanup.** Third-party cleaners and even Disk Cleanup's deep options can delete the cached payloads Windows needs for feature enablement.
- **Corrupted Windows Update components.** A broken SoftwareDistribution folder or stopped services can interrupt the download of the required payload midway, leaving the install half-fed.

## How to fix it

Work through these in order. Fix 1 tells you exactly which scenario you're in, so you don't waste time on the wrong repair.

### Fix 1: Pin down where the error comes from

The right repair depends on whether the failure was a cumulative update or a .NET Framework 3.5 enablement.

1. Open **Settings > Windows Update > Update history** and click the failed update to see its name and KB number.
2. Check whether the failure relates to **.NET Framework 3.5**: open **Control Panel > Programs > Turn Windows features on or off** and see if ".NET Framework 3.5 (includes .NET 2.0 and 3.0)" is unchecked or half-enabled.
3. If .NET 3.5 is the culprit, skip to Fix 4. For cumulative updates, continue with Fix 2.

### Fix 2: Run the Windows Update troubleshooter

Quick and harmless — worth trying before anything deeper.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow the prompts.
3. Restart, then retry the update at **Settings > Windows Update**. If 0x800F081F persists, the component store needs direct repair.

### Fix 3: Repair the component store with DISM and a source

This is the fix that resolves most 0x800F081F cases: you give DISM clean files from a Windows ISO instead of the broken local store.

1. Download the Windows 11 ISO from Microsoft's website, then double-click it to mount it. Note the drive letter it gets (for example, `E:`).
2. Open Command Prompt as administrator (search `cmd`, right-click, **Run as administrator**).
3. Run `DISM /Online /Cleanup-Image /RestoreHealth /Source:wim:E:\sources\install.wim:1 /LimitAccess` — replace `E:` with your mounted drive letter. The `:1` is the image index; if it fails, run `DISM /Get-WimInfo /WimFile:E:\sources\install.wim` first and use the index matching your edition.
4. When DISM completes, run `sfc /scannow`, restart, and retry the update.

### Fix 4: Enable .NET Framework 3.5 properly

If the error came from turning on .NET 3.5, install it from the same mounted ISO instead of letting Windows fetch it online.

1. With the ISO still mounted (from Fix 3), open **Control Panel > Programs > Turn Windows features on or off**.
2. Check **.NET Framework 3.5 (includes .NET 2.0 and 3.0)** and click OK.
3. If it fails again, run this in an administrator Command Prompt instead: `DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /Source:wim:E:\sources\install.wim:1 /LimitAccess` (again replacing `E:` with your drive letter).
4. Restart and confirm the feature shows as enabled in the Windows Features dialog.

### Fix 5: Reset the Windows Update components

If the payload download itself is corrupted, clearing the update cache forces a clean fetch.

1. In an administrator Command Prompt, stop the services: `net stop wuauserv`, `net stop bits`, and `net stop cryptsvc`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services: `net start wuauserv`, `net start bits`, and `net start cryptsvc`.
4. Go to **Settings > Windows Update** and check for updates again.

### Fix 6: Perform an in-place upgrade (repair install)

If nothing above clears the error, the component store is too damaged for targeted repair. An in-place upgrade reinstalls Windows over itself while keeping your files and apps.

1. Download the Windows 11 ISO from [Microsoft's official software download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, open it in File Explorer, and run `setup.exe`.
2. Accept the license terms, and on the "Choose what to keep" screen select **Keep personal files and apps**.
3. Let setup complete — it takes 30 to 90 minutes, and the PC will restart several times. Do not interrupt it.
4. After signing in, go to **Settings > Windows Update** and install the update that was failing.

Once updates are flowing again, keep an eye on the aftermath: if an update downloads but hangs on the final screen instead of erroring, see our guide on [Windows Update stuck at 100%](/articles/windows-update-stuck-at-100-percent-fix/). And if the update succeeds but your wireless adapter stops working — a common post-update headache — see how to fix [Wi-Fi not working after a Windows 11 update](/articles/wifi-not-working-after-windows-11-update-fix/).
