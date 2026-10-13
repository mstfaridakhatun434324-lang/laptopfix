---
title: "How to Fix Windows Update Error 0x80070490 on a Laptop"
slug: "how-to-fix-windows-update-error-0x80070490-on-laptop"
date: "2026-10-13"
categories: ["windows-update"]
tags: ["0x80070490", "element-not-found", "windows-update", "component-store"]
description: "Error 0x80070490 ('element not found') signals corruption in the update database or component store. Repair it with these targeted steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80070490-on-laptop.webp"
faqs:
  - q: "What does 'element not found' mean during Windows Update?"
    a: "It means the update engine looked up a component, package, or database record it expected to exist and found nothing. The usual underlying cause is corruption in the component store — the database Windows uses to track every system file — or in the update data store. The engine's internal references no longer match what is actually on disk."
  - q: "Is 0x80070490 caused by a failing hard drive?"
    a: "It can be, though software corruption is more common. If file system damage or bad sectors have eaten parts of the component store, the update engine hits 'element not found' when it reaches the damaged areas. Running a disk check is a sensible part of the repair sequence, especially if the error survives the standard DISM and SFC repairs."
  - q: "Will DISM fix error 0x80070490?"
    a: "DISM with the RestoreHealth option is the primary tool for this error because it repairs exactly the component store corruption that causes it. In many cases DISM alone resolves the error. When it does not, the deeper repairs in this guide — manual component reset, disk checks, and in-place upgrade repair — address the remaining causes."
  - q: "Can I ignore 0x80070490 if everything else works?"
    a: "You should not ignore it for long. The error means the servicing infrastructure is damaged, and while daily use may seem fine, the damage tends to spread: future updates fail, SFC reports unfixable corruption, and eventually feature updates refuse to install. Repairing it promptly with DISM is far easier than recovering from the compounded problems later."
---

Error 0x80070490, "element not found," is the update engine discovering that its internal map does not match reality. Somewhere in the component store or the update database, a record points to something that is not there — and the whole update operation stops. It sounds dire, but it is one of the better-understood update errors, and the repair tools for it are excellent.

The key insight is that this error lives one level deeper than a simple cache problem. Clearing the download cache helps sometimes, but the real fix is usually repairing the component store itself with DISM. The steps below escalate from the quick wins to the deep repairs in the right order.

‘Element not found’ sounds like the update engine lost something, and in a sense it did: the component store — Windows’ master database of every system file — contains references to components that are no longer where the database says they are. The engine looks up what it needs, finds a dangling reference, and stops. This error lives one level deeper than a cache problem, which is why cache clears alone often disappoint here. The real repair targets the component store itself, and the tool for that job is DISM’s RestoreHealth, purpose-built to reconcile the store with reality.

## Why this happens

- **Corrupt component store:** Damage to the WinSxS component database breaks the references updates depend on.
- **Damaged update data store:** Corruption in the SoftwareDistribution database orphans the records the engine looks up.
- **Interrupted servicing operations:** Power loss during a previous update leaves half-written component records.
- **Failed driver installations:** A crashed driver install can leave component references pointing nowhere.
- **Disk errors and bad sectors:** Physical or file system damage in the component store area produces this exact error.
- **Third-party "cleaner" damage:** Aggressive cleaners that touch WinSxS or the update cache cause reference breakage.
- **Incomplete feature update rollback:** A rollback that did not fully restore the component state leaves dangling references.
- **Manifest mismatches:** Component manifests that disagree with the actual files confuse the servicing engine.

## How to fix it

Work through these in order — diagnose first, then act.

DISM RestoreHealth downloads clean replacement files from Windows Update, so it needs a working internet connection and can take 15 to 30 minutes. Do not interrupt it — a half-repaired component store is worse than a damaged one. Start it when you can leave the machine alone, and let it finish completely.

### Fix 1: Run DISM RestoreHealth

This is the primary repair for this error — it fixes the component store directly.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth`.
3. Wait for it to complete; it downloads clean copies from Windows Update and can take 15 to 30 minutes.
4. Restart the laptop and retry Windows Update.

### Fix 2: Follow with System File Checker

SFC repairs the protected files that reference the component store.

1. In the same admin Command Prompt, run `sfc /scannow` after DISM finishes.
2. Let it complete to 100 percent and review its summary.
3. If it reports it fixed corruption, restart and test updates.
4. If it reports unfixable corruption, continue to the deeper fixes below.

### Fix 3: Reset the Windows Update components

Rebuild the update data store that holds the broken references.

1. Stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart all four services with `net start`.
4. Reboot and check for updates.

### Fix 4: Check the disk for damage

Rule out the physical layer before deeper software repairs.

1. Run `chkdsk C: /f /r` in an admin Command Prompt.
2. Schedule the scan and restart — the /r pass takes a while on large drives.
3. Review the summary for bad sectors or repaired file system issues.
4. After booting, rerun DISM RestoreHealth to fix anything the disk damage had corrupted.

### Fix 5: Run the Windows Update troubleshooter

The automated tool catches the straightforward faults contributing to this error.

1. Open Settings, System, Troubleshoot, Other troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart and test.
4. For persistent troubleshooter problems, see [fixing the Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working/).

### Fix 6: Analyze the CBS log for specifics

When general repairs fail, the log names the broken component.

1. Open `C:\Windows\Logs\CBS\CBS.log` in a text editor after a failed DISM or SFC run.
2. Search for "Failed" or "error" entries near the end of the log.
3. Note any specific package or manifest names mentioned.
4. Use that information to target the repair — or to explain the situation if you seek further help.

### Fix 7: Perform an in-place upgrade repair

Reinstall Windows over itself to rebuild the entire servicing infrastructure.

1. Download the Windows 11 ISO from Microsoft's software download page.
2. Mount the ISO and run setup.exe.
3. Choose to keep personal files and apps.
4. The in-place upgrade rebuilds the component store while preserving everything.
5. After completion, run Windows Update to confirm the error is gone.

### Fix 8: Install the specific update manually

If one particular KB keeps hitting 0x80070490, deliver it directly.

1. Note the failing KB number from update history.
2. Download the .msu from the Microsoft Update Catalog.
3. Run the standalone installer and restart when prompted.
4. The manual path sometimes succeeds where the damaged servicing lookup fails.
5. Our [manual installation guide](/articles/how-to-manually-install-windows-update-on-windows-11/) covers the Catalog steps in full.

After repairing, it is worth asking how the store got damaged, because the same cause will damage it again. The usual stories are forced shutdowns during updates, ‘cleaner’ apps that touch the WinSxS folder, and failing storage. If you recognize your own habits in that list, change the habit: let updates finish, keep cleaners away from system folders, and check drive health at the first sign of trouble. A component store that stays healthy makes every future update boring — which is the highest compliment an update pipeline can earn. For the deeper store-corruption repairs, our [0x80073712 guide](/articles/how-to-fix-windows-update-error-0x80073712-on-laptop/) continues where this one leaves off.

## Closing

Error 0x80070490 is the servicing infrastructure asking for repair, and DISM RestoreHealth is purpose-built to answer. Work from the component store outward — DISM, SFC, disk check, in-place upgrade — and the "element not found" becomes an element repaired.
