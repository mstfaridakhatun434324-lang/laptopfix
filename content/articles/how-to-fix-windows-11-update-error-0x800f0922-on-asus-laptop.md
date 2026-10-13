---
title: "How to Fix Windows 11 Update Error 0x800f0922 on an ASUS Laptop"
slug: how-to-fix-windows-11-update-error-0x800f0922-on-asus-laptop
date: 2026-09-18
categories: ["windows-update"]
tags: ["0x800f0922 fix", "asus windows update error", "net framework 3.5 update error", "windows 11 update failed"]
description: "Update error 0x800f0922 on your ASUS laptop? Repair the .NET Framework 3.5 feature state and use the manual install bypass to get updates working."
thumbnail: "/images/thumbs/how-to-fix-windows-11-update-error-0x800f0922-on-asus-laptop.webp"
faqs:
  - q: "Will a manual Catalog install really bypass the error?"
    a: "Often, yes. The standalone .msu installer configures features through a different path than the Windows Update engine, and many users report the manual install succeeding where automatic updates failed repeatedly with 0x800f0922. It's one of the highest-success fixes for this code."
  - q: "Should I just reinstall Windows to fix 0x800f0922?"
    a: "Only as a last resort. The .NET feature repair, the pending.xml cleanup, and the manual Catalog install resolve the large majority of cases without a reinstall. An in-place upgrade that keeps your files and apps is the sensible final step if everything else fails."
  - q: "What does error 0x800f0922 actually mean?"
    a: "It's a Component-Based Servicing error meaning one of the update's sub-installers failed. In practice the failing piece is almost always the .NET Framework 3.5 feature installer — which is why the most effective fixes target the .NET 3.5 feature state rather than generic update troubleshooting."
  - q: "Do I need .NET Framework 3.5 at all?"
    a: "Probably not, unless you run older desktop software that requires it. If the feature is half-enabled and you don't need it, fully disabling it in optionalfeatures.exe often clears 0x800f0922 immediately. Only repair it if an application you use depends on it."
---

0x800f0922 is one of the more specific Windows Update codes, which is genuinely good news — it shrinks the suspect list dramatically. Microsoft's own documentation ties it to failures in the .NET Framework 3.5 installer and, less often, to Secure Boot or app-readiness hiccups during the update. On ASUS laptops the .NET angle explains the large majority of cases I see. [a broader Windows 11 update failure](/articles/how-to-fix-windows-update-error-0x800f0922-in-windows-11-24h2/)

Don't burn time on generic fixes first. Clearing the update cache rarely helps here because the cache isn't the problem — the feature payload is. The sequence below goes straight at the .NET 3.5 state, then handles the Secure Boot and servicing-stack angles for the minority of cases where .NET is innocent.

## Why this happens

- **A stuck pending.xml from an earlier update.** A frozen pending file makes every new update attempt die at the same installer step. Delete C:\Windows\WinSxS\pending.xml only after a clean reboot fails to clear it.
- **Third-party .NET or developer tools.** SDKs and targeting packs can fight the inbox .NET 3.5 feature install. Visual Studio-era targeting packs are the usual suspects in this category.
- **A damaged update payload.** The downloaded cumulative update itself is broken and fails when it reaches the .NET step. Re-download from the Catalog instead of trusting a cached copy.
- **Odd EFI partition behavior.** Rare, but Secure Boot validation failures during feature configuration can produce this code. It's the rarest cause on the list — investigate it last.
- **A broken .NET Framework 3.5 feature state.** The feature is half-enabled or its payload is corrupt, so the installer step fails every time. Run optionalfeatures.exe — a half-filled checkbox is the classic tell.
- **A missing SxS payload.** The side-by-side source files for .NET 3.5 were cleaned up by Disk Cleanup, leaving the installer nothing to work with. Disk Cleanup's "Windows Update Cleanup" sometimes removes these payloads.
- **A Secure Boot policy conflict.** On some ASUS firmware versions, Secure Boot blocks the .NET installer shim during the update. Test by toggling Secure Boot temporarily; remember to re-enable it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Repair the servicing store

When the CBS store is damaged, the .NET installer step cannot complete its transaction. Read the code correctly: 0x800f0922 means a CBS sub-installer failed — download errors look like 0x800700xx, while outright store corruption shows up as 0x80073712.

1. Open an elevated Command Prompt, run `sfc /scannow` to completion, then `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Restart the laptop and retry the update.
3. If DISM reports damage it could not fix, move on to the manual install in Fix 2 instead of looping on a broken store.

### Fix 2: Install the KB manually from the Catalog

Bypass the failing installer path by applying the cumulative update yourself.

1. In Settings, then Windows Update, then Update history, copy the failing KB number.
2. Search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), download the x64 .msu, double-click to install, and restart when prompted.
3. Manual installs frequently succeed where the automatic engine dies at 0x800f0922. If you disabled .NET 3.5 as a workaround, note which of your apps need it before you forget.

### Fix 3: Remove conflicting .NET SDKs for the attempt

Developer targeting packs and SDKs occasionally fight the inbox .NET 3.5 feature.

1. In Settings, then Apps, then Installed apps, uninstall .NET SDKs and targeting packs you don't actively need — they can be reinstalled later.
2. Restart and retry the update; bring the SDKs back once it succeeds. Machines upgraded from Windows 10 sometimes carry a broken .NET feature state from the old install — the feature reset in Fix 5 clears those legacy states.

### Fix 4: Repair-install Windows in place

The last resort: reinstall Windows over itself, keeping files and apps, which rebuilds the feature and servicing state from scratch.

1. Back up important files, download the Windows 11 media creation tool from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11), run setup.exe, and choose "Keep personal files and apps".
2. Thirty to ninety minutes later the servicing stack is factory-fresh — the 0x800f0922 failure state does not survive that. Keep the KB number written down in case the error ever returns.

### Fix 5: Audit the .NET Framework 3.5 feature state

The five-second diagnosis for most 0x800f0922 cases: is .NET 3.5 genuinely clean or stuck halfway?

1. Open the Windows Features dialog — Win + R, then optionalfeatures.exe — and expand ".NET Framework 3.5 (includes .NET 2.0 and 3.0)".
2. A half-filled checkbox means a half-enabled feature: clear it fully, click OK, and restart. Unticked and unneeded? Leave it off and retry the update. Ticked and healthy? The fault lies elsewhere.
3. Confirm the final state with `DISM /Online /Get-FeatureInfo /FeatureName:NetFx3` — it should report fully enabled or fully disabled, never partial.

### Fix 6: Rebuild .NET 3.5 from a fresh source

When the SxS payload is corrupt or missing, DISM can restore the feature from Windows Update servers or local media.

1. In an elevated prompt, run `DISM /Online /Enable-Feature /FeatureName:NetFx3 /All`. If it fails with a source error, mount a Windows 11 ISO and run `DISM /Online /Enable-Feature /FeatureName:NetFx3 /All /Source:X:\sources\sxs /LimitAccess` (X = the mounted drive letter).
2. Restart, retry Windows Update, and confirm the 0x800f0922 entry is gone from update history. The CBS log at C:\Windows\Logs\CBS\CBS.log records exactly which payload file was missing when the .NET step failed.

### Fix 7: Clear the stuck pending state

A frozen pending.xml from an earlier update poisons every retry with the same failure — and this error is deterministic, so identical retries fail identically.

1. In an elevated prompt, stop the services (`net stop wuauserv`, `net stop bits`), delete C:\Windows\WinSxS\pending.xml if it exists (back it up first), then restart the services (`net start wuauserv`, `net start bits`).
2. Check for updates again, then inspect C:\Windows\Logs\CBS\CBS.log for fresh errors to confirm the .NET step passed this time.

## Closing

Error 0x800f0922 looks cryptic, but it's one of the most diagnosable update codes there is — the .NET Framework 3.5 step is failing, and you now know exactly where to hit it. Repair or remove the feature, flush the pending state, and use the manual Catalog install as your bypass. For other stubborn update codes, [the same error on Windows 10](/articles/how-to-fix-error-0x800f0922-on-windows-10/) walks through the same methodical approach.
