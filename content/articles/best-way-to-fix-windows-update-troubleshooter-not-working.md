---
title: "Fix the Windows Update Troubleshooter Not Working"
slug: best-way-to-fix-windows-update-troubleshooter-not-working
date: 2026-09-30
categories: ["windows-update"]
tags: ["troubleshooter", "windows update", "diagnostics", "windows 11"]
description: "The Windows Update troubleshooter won't run or can't fix anything? Here are 7 ways to repair the troubleshooter itself — and workarounds when it won't cooperate."
thumbnail: "/images/thumbs/best-way-to-fix-windows-update-troubleshooter-not-working.webp"
faqs:
  - q: "Why won't the Windows Update troubleshooter run at all?"
    a: "Usually because the diagnostic infrastructure it depends on is broken: the Diagnostic Policy Service is disabled, the troubleshooter's own system files are corrupted, or a group policy blocks troubleshooting. Less commonly, the Settings app page that hosts it is damaged. The fixes below repair the infrastructure layer by layer, starting with the services the troubleshooter needs."
  - q: "The troubleshooter runs but says it couldn't identify the problem. Now what?"
    a: "That message means the automated checks found nothing in their limited checklist — not that nothing is wrong. The troubleshooter only tests a fixed set of conditions, and many real update failures fall outside it. Treat its verdict as inconclusive and move to manual diagnosis: the cache reset, DISM repair, and manual install methods in our other guides cover everything the troubleshooter cannot."
  - q: "Is there a command-line version of the update troubleshooter?"
    a: "Yes. The classic Control Panel troubleshooters can still be launched directly: press Win + R, type msdt.exe -id WindowsUpdateDiagnostic, and press Enter. This bypasses the Settings app entirely, which helps when the Settings troubleshooters page itself is broken. It runs the same diagnostic engine with the same capabilities — just through a different door."
  - q: "Can I fix Windows Update without the troubleshooter?"
    a: "Absolutely — experienced technicians usually skip it. Every repair the troubleshooter performs (restarting services, clearing the cache, re-registering components) can be done manually with more control, and the manual methods in our guides go further than the automated checks. The troubleshooter is a convenience, not a requirement; nothing about Windows Update repair depends on it."
---

It is a special frustration: the tool Microsoft gives you to fix Windows Update is itself broken. You click Run on the Windows Update troubleshooter and nothing happens — or it spins forever, or it finishes instantly claiming it could not identify any problem while updates very obviously still fail. When the repair tool needs repairing, you need a different approach.

The troubleshooter is not magic; it is a scripted checklist that depends on its own infrastructure — diagnostic services, system files, and the Settings app page that hosts it. When any of that infrastructure breaks, the troubleshooter fails in confusing ways. The good news is twofold: the infrastructure is repairable, and even if you never fix the troubleshooter, every repair it performs can be done manually — usually better. This guide does both: fixes the troubleshooter, then shows you the manual path that makes it optional.

## Why this happens

- **Disabled diagnostic services.** The Diagnostic Policy Service or Diagnostic Service Host is stopped or disabled, so no troubleshooter can run.
- **Corrupted troubleshooter files.** Damage to the diagnostic package store breaks the troubleshooter's own scripts.
- **Broken Settings app page.** The Troubleshoot page in Settings fails to launch the underlying diagnostic.
- **Group policy restrictions.** Policies disabling scripting or diagnostics block the troubleshooter silently.
- **Corrupted system files.** General system damage that breaks both updates and the tools that repair them.
- **Third-party software interference.** Security software blocking the diagnostic's system access.
- **User profile corruption.** A damaged profile can break Settings-app-hosted troubleshooters while the system is otherwise fine.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check the diagnostic services

The troubleshooter cannot run without its service infrastructure. Verify the foundation first.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Find **Diagnostic Policy Service** — set its startup type to **Automatic** and start it if it is stopped.
3. Do the same for **Diagnostic Service Host** and **Diagnostic System Host**.
4. Retry the troubleshooter at **Settings > System > Troubleshoot > Other troubleshooters**. If it now runs, the services were the whole problem.

### Fix 2: Launch the troubleshooter via the classic path

If the Settings page is what is broken, bypass it with the direct diagnostic launcher.

1. Press **Win + R**, type `msdt.exe -id WindowsUpdateDiagnostic`, and press Enter.
2. The classic Windows Update troubleshooter window opens — click **Next** and let it run.
3. Apply any fixes it offers. This is the same diagnostic engine as the Settings version, just hosted differently.
4. If msdt.exe also fails to launch, the diagnostic store itself is damaged — continue to Fix 3.

### Fix 3: Repair system files with DISM and SFC

Corrupted system files break both the troubleshooter and the updates it would repair. Fix the foundation.

1. Open Command Prompt as administrator.
2. Run `DISM /Online /Cleanup-Image /RestoreHealth` (15–30 minutes).
3. Run `sfc /scannow` to 100% completion.
4. Restart and retry the troubleshooter. If DISM reports source errors, see our guide to [running DISM RestoreHealth](/articles/how-to-run-dism-restore-health-on-windows-11/) for the ISO-based repair.

### Fix 4: Check group policy and registry blocks

Policies can silently disable troubleshooting. Check both the policy editor and the registry.

1. On Pro editions, open `gpedit.msc` and navigate to **Computer Configuration > Administrative Templates > System > Troubleshooting and Diagnostics** — ensure nothing is set to Disabled that should not be.
2. Also check **User Configuration > Administrative Templates > System** for script-execution restrictions.
3. In the registry (`regedit`), verify `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\ScriptedDiagnostics` does not contain disabling values — back up the key before changing anything.
4. On work-managed laptops, these policies may be set by your organization — your IT administrator controls them, not you.

### Fix 5: Test in a new user profile

A corrupted user profile can break Settings-hosted troubleshooters while everything else works.

1. Go to **Settings > Accounts > Other users** and add a new local administrator account.
2. Sign out and sign in as the new user.
3. Try running the Windows Update troubleshooter there.
4. If it works in the new profile, your main profile is damaged — migrate your files to the new account rather than fighting the old one. (Profile repair is rarely worth the effort compared to migration.)

### Fix 6: Do the troubleshooter's job manually

Stop depending on the tool. Its entire checklist, done by hand, with more thoroughness:

1. Reset the update cache manually: stop wuauserv/bits/cryptsvc, rename SoftwareDistribution and catroot2, restart the services — the full commands are in our [0x80070002 guide](/articles/how-to-fix-windows-update-error-0x80070002-on-dell-laptop/).
2. Re-register update components: `regsvr32 wuapi.dll`, `wuaueng.dll`, `wups.dll`, `wuwebv.dll` in an elevated prompt.
3. Clear the BITS queue: `bitsadmin /reset /allusers`.
4. Check for updates. This manual sequence covers everything the troubleshooter checks — plus the cache rebuild it cannot do.

### Fix 7: Reset the diagnostic store and consider an in-place upgrade

For the truly stubborn cases where the diagnostic infrastructure itself is wrecked:

1. In an administrator Command Prompt, run `sfc /scannow` once more after the Fix 3 repairs, then run the **System File Checker**-adjacent command `DISM /Online /Cleanup-Image /StartComponentCleanup` to tidy the store.
2. If troubleshooters across the board (not just Windows Update) fail, the diagnostic store needs the in-place upgrade in step 3.
3. Download the Windows 11 ISO from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11), mount it, run `setup.exe`, and choose **Keep personal files and apps** — this rebuilds both the update and diagnostic subsystems.
4. Afterward, verify the troubleshooter runs — and keep the manual techniques from Fix 6 in your back pocket, since they work whether the troubleshooter cooperates or not.

## Closing

A broken Windows Update troubleshooter is an infrastructure problem — diagnostic services, system files, or policies — and it is fixable, but it is also optional: every repair the troubleshooter performs can be done manually, and the manual versions go further. Fix the services, repair the system files, and learn the manual cache reset so you never depend on the tool again. For the full manual repair sequence applied to a specific error, our [0x80070002 guide](/articles/how-to-fix-windows-update-error-0x80070002-on-dell-laptop/) walks through it end to end; and if your actual symptom is updates hanging rather than erroring, see updates [stuck downloading on Windows 11](/articles/how-to-fix-windows-update-stuck-downloading-on-windows-11/).
