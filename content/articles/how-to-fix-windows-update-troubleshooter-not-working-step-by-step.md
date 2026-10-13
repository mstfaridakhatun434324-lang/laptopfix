---
title: "Windows Update Troubleshooter Not Working? Step-by-Step Repair"
slug: how-to-fix-windows-update-troubleshooter-not-working-step-by-step
date: 2026-10-05
categories: ["windows-update"]
tags:
  - troubleshooter
  - windows update
  - get help
  - step-by-step
  - troubleshooting
description: "Step-by-step repair when the Windows Update troubleshooter will not run, crashes, or finds nothing: Get Help fixes, service resets, and manual repairs."
thumbnail: "/images/thumbs/how-to-fix-windows-update-troubleshooter-not-working-step-by-step.webp"
faqs:
  - q: "Where did the Windows Update troubleshooter go in Windows 11?"
    a: >
      It moved from the old Control Panel/msdt system into Settings > System > Troubleshoot > Other troubleshooters, powered by the Get Help app. The old msdt.exe commands and Control Panel troubleshooting links for Windows Update no longer function on current builds — always start from Settings.
  - q: "Why does the troubleshooter say no problems were found when updates clearly fail?"
    a: >
      The built-in troubleshooter only checks a fixed list of common issues: service states, cache size, and basic connectivity. It cannot diagnose corrupted system images, specific bad KBs, driver conflicts, or safeguard holds. A clean troubleshooter result just means the problem is outside its checklist — continue with manual error-code diagnosis.
  - q: "Can I download the Windows Update troubleshooter separately?"
    a: >
      No — there is no standalone installer; it is part of Windows. The downloadable Show or hide updates tool (wushowhide) is a different, narrower tool for hiding specific updates. To restore a broken built-in troubleshooter, repair the Get Help app and run DISM/SFC; an in-place upgrade repair restores everything as a last resort.
  - q: "Is it safe to reset the SoftwareDistribution folder by hand?"
    a: >
      Yes. Renaming SoftwareDistribution (rather than deleting it) forces Windows to build a fresh update cache, and the old folder remains as a backup you can restore. Installed updates are not affected — only the download cache and pending metadata are rebuilt. It is the same operation the troubleshooter performs in most successful repairs.
---

The troubleshooter is meant to be the first resort, so when it will not launch, crashes instantly, or runs and declares everything fine while updates keep failing, you are stuck with a broken tool and a broken update system. This guide fixes both — the troubleshooter first, then the update problem it was supposed to solve.

Context matters here: Microsoft retired the old msdt-based troubleshooters and rebuilt them inside the Get Help app. Many cannot-run cases are just people launching the old dead entry points, while the crash cases usually trace to corrupted diagnostic packages or stopped services underneath.

This is the complete, brand-neutral repair sequence, from launching the right thing to doing the troubleshooter's job by hand.

## Why this happens

- **Launching the retired msdt version:** old shortcuts, scripts, and Control Panel links point to a troubleshooter that no longer exists.
- **Broken Get Help app:** the modern troubleshooters live inside Get Help — a damaged Get Help breaks them all.
- **Corrupted diagnostic packages:** the troubleshooter's own files can be damaged by failed updates.
- **Required services stopped:** the tool needs the update services in a startable state to diagnose them.
- **Permission issues:** non-admin accounts or broken elevation can kill the launch.
- **System file corruption:** damaged system files crash the diagnostic framework itself.
- **The real problem is outside the tool's scope:** the troubleshooter checks common issues only; deeper corruption needs manual repair.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Launch the troubleshooter the correct modern way

Half of all not working reports end here — the tool was fine, the launch method was obsolete. The old msdt commands and Control Panel troubleshooting pages still exist as ghosts on some systems: they open, they appear to do something, and then nothing happens. The Settings path is the only launch method Microsoft still maintains, so make it your habit and delete any ancient troubleshooter shortcuts from your desktop.

1. Open Settings > System > Troubleshoot > Other troubleshooters.
2. Click Run next to Windows Update.
3. If it opens the Get Help app, follow its guided prompts to completion.
4. If nothing happens when you click Run, continue to Fix 2.

### Fix 2: Repair the Get Help app

The troubleshooter framework lives or dies with Get Help. Repairing the host app restores every troubleshooter it contains.

1. Go to Settings > Apps > Installed apps, find Get Help.
2. Open Advanced options and click Repair, then test the troubleshooter.
3. If it still fails, click Reset in the same place and reboot.
4. Test the Windows Update troubleshooter once more.

### Fix 3: Restart the update services manually

Give the troubleshooter something healthy to diagnose by waking the services yourself. The troubleshooter's first checks assume the Windows Update service, BITS, and the cryptographic service can at least be started — when all three are dead or stuck in a stopping state, the diagnostic cannot even collect its baseline and bails out. Starting them by hand restores the baseline it needs.

1. Open an elevated Command Prompt.
2. Run: net start wuauserv, net start bits, net start cryptsvc (ignore already-running messages).
3. If a service refuses to start, note which one — that is a clue, not a dead end.
4. Run the troubleshooter again with the services awake.

### Fix 4: Re-register the diagnostic infrastructure

Corrupted troubleshooter packages can be re-registered with built-in commands, restoring the tool without reinstalling Windows. On builds where the PowerShell troubleshooting cmdlets are unavailable — Microsoft has been thinning them out — do not fight it: Fix 5's manual cache reset accomplishes the same practical repair the troubleshooter would have performed.

1. Open PowerShell as administrator.
2. Run: Get-TroubleshootingPack -Path C:\Windows\diagnostics\system\WindowsUpdate | Invoke-TroubleshootingPack (if available on your build).
3. If that cmdlet is unavailable, skip to Fix 5 — the manual path covers the same ground.
4. Test the troubleshooter from Settings afterward.

### Fix 5: Do the troubleshooter's job manually: reset update components

When the tool cannot run, perform its core repair yourself. This cache reset is what the troubleshooter does in most successful runs anyway.

1. Open Command Prompt as administrator.
2. Run: net stop wuauserv, net stop bits, net stop cryptsvc.
3. Run: ren C:\Windows\SoftwareDistribution SoftwareDistribution.old and ren C:\Windows\System32\catroot2 catroot2.old.
4. Run: net start wuauserv, net start bits, net start cryptsvc, then Check for updates.

### Fix 6: Repair the system image underneath

A troubleshooter that crashes on launch usually signals damaged system files. Repair the foundation and the tool often revives.

1. In an elevated prompt run: DISM /Online /Cleanup-Image /RestoreHealth.
2. Follow with: sfc /scannow, then reboot.
3. Launch the troubleshooter again — and run Windows Update to check the original issue.
4. Document any remaining error codes from Update history for targeted fixes.

### Fix 7: Use alternative diagnostics and manual error-code fixes

If the troubleshooter is unrecoverable, route around it: manufacturer tools and error-code-specific guides replace it functionally.

1. Use your laptop maker's tool (Dell SupportAssist, HP Support Assistant, Lenovo Vantage, MyASUS) for driver-side issues.
2. Look up the specific update error code on the [Windows support hub](https://support.microsoft.com/en-us/windows).
3. For download errors, our [0x80070002 fix](/articles/how-to-fix-error-0x80070002-in-windows-11-24h2/) covers the most common one step by step.
4. An in-place upgrade repair (reinstalling Windows while keeping files and apps) restores all built-in troubleshooters as a final option.

## Closing

A dead troubleshooter is usually a dead launch path or a sick Get Help app — both repairable in minutes, and both worth fixing because the same framework powers the network, audio, and power troubleshooters you will reach for later. And when the tool cannot be revived, its core repairs are all doable by hand: the cache reset, the service restarts, and the image repair above. You were never truly dependent on the button. On HP hardware specifically, pair this with our [HP troubleshooter fix](/articles/how-to-fix-windows-update-troubleshooter-not-working-on-hp-laptop/).
