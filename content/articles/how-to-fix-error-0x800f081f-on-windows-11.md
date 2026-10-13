---
title: "How to Fix Error 0x800f081f on Windows 11"
slug: how-to-fix-error-0x800f081f-on-windows-11
date: 2026-10-07
categories: ["windows-errors"]
tags: ["error-0x800f081f", "windows-11", "dism"]
description: "Error 0x800f081f saying source files not found? Repair the component store and point DISM at a valid source."
thumbnail: "/images/thumbs/how-to-fix-error-0x800f081f-on-windows-11.webp"
faqs:
  - q: "What does error 0x800f081f mean?"
    a: "It means CBS_E_SOURCE_MISSING — Windows needed source files to complete a repair or feature install and couldn't find them. It appears when DISM can't reach Windows Update for repair files, or when installing .NET Framework 3.5 without the right source available."
  - q: "Why does DISM fail with 0x800f081f?"
    a: "Because the component store is too damaged for online repair, or a policy blocks DISM from downloading from Windows Update. Pointing DISM at a local Windows 11 ISO as the source bypasses both problems."
  - q: "Do I need the exact same Windows build ISO?"
    a: "Ideally yes — the ISO should match your installed build as closely as possible. A newer ISO usually works; a much older one may not contain the files DISM needs. When in doubt, download the latest ISO from Microsoft."
  - q: "Can I fix 0x800f081f without an ISO?"
    a: "Sometimes. If the cause is a group policy blocking online repair, changing the policy lets DISM download from Windows Update normally. But the ISO method is more reliable and works offline, so it's the recommended approach."
---
# How to Fix Error 0x800f081f on Windows 11

**Error 0x800f081f** translates to "the source files could not be found." You'll meet it in two places: when **DISM** fails to repair your system, or when installing **.NET Framework 3.5** (which older apps and games still need) fails through Windows Features. In both cases, Windows needs files it can't locate — and the fix is showing it where they are.

The reliable solution is a Windows 11 ISO used as a local repair source. It works offline, bypasses broken policies, and fixes both the DISM and .NET scenarios. If you're hitting a different servicing error, our [error 0x80070057 fix](/articles/error-code-0x80070057-fix/) covers the parameter-incorrect variant.

## Why this happens

- **Component store too damaged for online repair:** DISM can't fix corruption using only the broken local store.
- **Policy blocking Windows Update as a repair source:** Group Policy or registry settings prevent DISM from downloading files.
- **Missing .NET 3.5 payload:** The feature's files aren't in the local component store and online download fails.
- **Corrupted Windows Update components:** The download path DISM relies on is itself broken.
- **Wrong or missing install media:** Pointing DISM at an ISO of the wrong edition or build.
- **Metered connection blocking downloads:** Windows refusing to fetch repair files over a metered network.

## How to fix it

Work through these in order. The ISO-source method (Fix 2) is the definitive fix.

### Fix 1: Check the policy blocking online repair

Sometimes DISM is simply forbidden from using Windows Update — and flipping that fixes everything without an ISO.

1. Press **Win + R**, type `gpedit.msc` (Pro editions), and go to **Computer Configuration > Administrative Templates > System**.
2. Open **Specify settings for optional component installation and component repair**.
3. Set it to **Enabled**, tick **Download repair content and optional features directly from Windows Update**, and click **OK**.
4. On Home editions, set the registry instead: in an admin Terminal, run
   `reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Servicing" /v RepairContentServerSource /t REG_DWORD /d 2 /f`
5. Retry DISM. If it still fails with 0x800f081f, continue to Fix 2.

### Fix 2: Download the Windows 11 ISO

You need a local source of pristine Windows files.

1. Download the latest Windows 11 ISO from the [official Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Double-click the ISO to mount it and note the drive letter (for example `E:`).
3. Verify the ISO mounted correctly by browsing to `E:\Sources` — you should see `install.wim` or `install.esd`.
4. Keep the ISO mounted for the next steps; don't unmount it until repairs complete.

### Fix 3: Repair with DISM using the ISO as source

This is the core fix — DISM with an explicit, known-good source.

1. Open **Terminal (Admin)**.
2. First check the image index you need:
   `dism /Get-WimInfo /WimFile:E:\Sources\install.wim`
   (use `install.esd` and `/Get-EsdInfo` if that's what you have). Note the index number matching your edition (usually 1 or 6 for Pro).
3. Run the repair:
   `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:E:\Sources\Install.wim:1 /LimitAccess`
   Replace `1` with your index and `E:` with your mounted drive letter.
4. For ESD files use `/Source:ESD:E:\Sources\Install.esd:1` instead.
5. Let it complete — it takes 10–30 minutes. Then run `sfc /scannow` to verify.

### Fix 4: Install .NET Framework 3.5 from the ISO

If your 0x800f081f appeared when enabling .NET 3.5 in Windows Features, use the ISO as its source too.

1. With the ISO still mounted, open an admin Terminal.
2. Run:
   `DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /Source:E:\Sources\sxs /LimitAccess`
3. Wait for the "operation completed successfully" message.
4. Retry the app or game that needed .NET 3.5.
5. Alternatively, download the offline .NET Framework installer from Microsoft — but the DISM method is more reliable when the component store is involved.

### Fix 5: Repair the Windows Update components

If DISM's online path was broken by corrupted update components, fix those too.

1. In an admin Terminal:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
2. Turn off any metered connection flag (**Settings > Network & internet > Wi-Fi > your network**) so repair downloads aren't blocked.
3. Retry the online DISM repair — with healthy components it may now succeed without the ISO.

### Fix 6: Do an in-place upgrade as the final repair

When the component store is damaged beyond what DISM can fix even with a source, reinstall Windows over itself.

1. With the ISO mounted, run `E:\setup.exe`.
2. Choose **Keep personal files and apps**.
3. Let the upgrade complete — it rebuilds the entire component store from the ISO's pristine files.
4. Afterward, `sfc /scannow` and DISM should both run cleanly.
5. Microsoft documents in-place upgrades and repair installs on the [Windows support hub](https://support.microsoft.com/en-us/windows).

### Fix 7: Prevent recurrence

A healthy component store doesn't break on its own — find what damaged it.

1. Run `chkdsk C: /f` to rule out disk errors as the original cause.
2. Uninstall "system cleaner" tools that aggressively delete WinSxS or servicing files — they're a top cause of component-store damage.
3. Keep at least 15–20 GB free on C: so servicing operations never run out of room mid-write.
4. Let Windows Update install servicing stack updates promptly; they're the updates that keep the repair machinery itself healthy. For related blue-screen issues on the same machine, see our [blue screen fix guide](/articles/how-to-fix-blue-screen-of-death-windows-11/).

## Closing

Error 0x800f081f is Windows admitting it can't find the files it needs to fix itself — so you hand it the files on a Windows 11 ISO and point DISM at them. The ISO-source repair resolves both the DISM failure and the .NET 3.5 install failure in one stroke. Once the component store is healthy again, keep it that way: no aggressive cleaners, enough free disk space, and servicing updates installed on time.
