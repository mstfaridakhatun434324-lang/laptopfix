---
title: "Windows Update Error 0x80080005: A Complete Step-by-Step Repair Guide"
slug: how-to-fix-windows-update-error-0x80080005-step-by-step
date: 2026-09-22
categories: ["windows-update"]
tags: ["windows update", "error 0x80080005", "windows 11", "services", "step by step"]
description: "Error 0x80080005 means the update engine could not start. Follow these 7 ordered steps to repair services, permissions, and components."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80080005-step-by-step.webp"
faqs:
  - q: "What is a COM server execution failure?"
    a: "COM is the Windows mechanism programs use to launch system components like the update engine. A server execution failure means the launch request was issued but the component crashed or was blocked during startup. For updates, it almost always traces to broken registrations or permissions, both fixable."
  - q: "The service starts but updates still fail. Now what?"
    a: "Then the engine launches but hits a downstream problem — corrupted cache, damaged store, or connection issues. The engine starting successfully actually narrows the field considerably: move to cache-reset and servicing repairs, since activation itself is now proven working. Proving activation works is genuine progress — it cuts the suspect list in half immediately."
  - q: "Should the service be Automatic or Manual?"
    a: "Automatic (Delayed Start) is the Windows 11 default and the recommended setting. Manual also works since the system starts it on demand, but Disabled guarantees this error. If you find it set to Disabled and did not change it, some installed software did — investigate what."
  - q: "Will an in-place upgrade definitely fix this?"
    a: "It resolves the overwhelming majority of persistent 0x80080005 cases because it reinstalls every update component from pristine sources. The rare exceptions involve hardware problems like a failing drive corrupting newly written files — which is why the diagnostics step comes before the upgrade."
---

Error 0x80080005 is Windows telling you the update engine failed to launch. Technically it is a COM server execution failure: something asked the Windows Update service to start, and the start operation itself blew up. You will see it the moment you check for updates, because nothing downstream can run without the engine.

This is a local activation problem, not a network or download problem — which is actually good news, because every cause lives on your machine and every fix is under your control. The suspects, in order of likelihood: the service is disabled or stuck, the engine's DLL registrations are broken, registry permissions drifted, or security software is blocking activation.

Work through the steps in order. Each one repairs a deeper layer of the activation chain, and the checkpoints tell you exactly when the engine is breathing again.

## Why this happens

- **Service set to Disabled:** The most mundane cause — the service cannot start because it is configured not to.
- **Broken COM registrations:** The DLLs implementing the update engine must be registered; broken registration means failed activation.
- **Permission problems:** Incorrect ACLs on service registry keys block the service control manager.
- **Security software hooks:** Kernel-level security products can interfere with service launches.
- **Corrupt dependencies:** The engine depends on RPC, DCOM, and other services; if they are damaged, activation fails.
- **Stuck service state:** A service wedged in Start Pending never completes activation.
- **Profile corruption:** Damaged user profiles can break the security context activation requires.
- **Disk errors:** File-system damage to engine binaries or registry hives prevents loading.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the engine is the problem

Verify the service itself fails to start, rather than assuming. Precision here directs the whole repair.

1. Open services.msc and find Windows Update.
2. Check its status and startup type — note if it is Disabled or stuck.
3. Try starting it manually and note the exact error.
4. If it fails with an error, proceed; the activation chain needs repair.

### Fix 2: Set correct startup types and start dependencies

The engine depends on other services. Ensuring the whole dependency chain is healthy removes the simple causes. If the troubleshooter itself misbehaves, see [How to fix windows 11 stuck on restarting screen reddit](/articles/how-to-fix-windows-11-stuck-on-restarting-screen-reddit/) for a dedicated walkthrough.

1. Set Windows Update to Automatic and try to start it.
2. Set Background Intelligent Transfer Service to Automatic (Delayed Start) and start it.
3. Confirm Remote Procedure Call (RPC) is running — the engine depends on it.
4. Retry Check for updates.

### Fix 3: Re-register the engine components

Rebuilds the COM activation entries for the update engine's DLLs — the definitive fix for registration damage.

1. Open Terminal (Admin).
2. Run these, confirming each success dialog: regsvr32 wuaueng.dll, then regsvr32 wucltux.dll.
3. Then: regsvr32 wuwebv.dll, then regsvr32 atl.dll.
4. Restart and test the update check.

### Fix 4: Clear corrupted state folders

Forces the engine to initialize from clean state on next start.

1. Stop the services: net stop wuauserv, net stop bits, net stop cryptsvc.
2. Rename SoftwareDistribution and catroot2 with .old suffixes.
3. Restart all three services.
4. Test Windows Update.

### Fix 5: Rule out security software blocks

Isolates third-party interference as a variable. [the Microsoft Update Catalog](https://www.catalog.update.microsoft.com) covers the engine's normal behavior for comparison.

1. Temporarily disable third-party antivirus and firewall.
2. Attempt to start the Windows Update service.
3. If it starts, configure exclusions in the security suite.
4. Re-enable protection and retest.

### Fix 6: Repair files with DISM and SFC

Fixes damaged engine binaries and dependencies at the file level.

1. Run: DISM /Online /Cleanup-Image /RestoreHealth in Terminal (Admin).
2. Follow with: sfc /scannow.
3. Restart.
4. Verify the service starts cleanly.

### Fix 7: In-place upgrade and verification

Replaces the entire update engine when targeted repairs fail, then proves the fix.

1. Back up data and run Windows 11 setup, keeping files and apps.
2. Complete the upgrade.
3. Open services.msc and confirm Windows Update starts.
4. Run Check for updates and confirm the queue processes.

### Fix 8: Make engine health a recurring check

Activation chains degrade silently until the day the engine will not start. A brief recurring inspection keeps every link — service configuration, registrations, permissions — verified good. Five minutes a quarter is the entire cost, and it converts 0x80080005 from a recurring nightmare into a solved problem you never think about again.

1. Quarterly, confirm in services.msc that Windows Update, BITS, and Cryptographic Services are set to Automatic.
2. Ban registry cleaners from the machine entirely — broken registrations are their signature damage.
3. Uninstall software through proper uninstallers to avoid orphaning shared component registrations.
4. Smoke-test Windows Update after every security software change.
5. Keep a system restore point from a known-good state; activation repairs are easier with a fallback.
6. At the first sign of start failures, re-register the engine DLLs the same day.

## Closing

With 0x80080005 resolved, the update engine should start reliably from here on. Protect it by leaving service registrations alone, keeping security software configured with proper exclusions, and addressing the first activation failure promptly. For related errors, see [How to fix we couldn't complete the updates undoing changes on hp laptop](/articles/how-to-fix-we-couldn-t-complete-the-updates-undoing-changes-on-hp-laptop/) and [How to fix superfetch high disk usage on hp laptop](/articles/how-to-fix-superfetch-high-disk-usage-on-hp-laptop/). Activation failures never arrive without warning signs — a service flipped to Manual here, a cleaner run there — so the quarterly audit is really an early-warning system. Keep it, keep registry cleaners off the machine entirely, and the engine will start on demand for years without another 0x80080005. If anything ever does block a service launch again, you now know the exact repair sequence, which makes the second occurrence a fifteen-minute task instead of a crisis. The update engine is one of the quietest critical services in Windows — you only ever notice it when it fails to start. The quarterly audit keeps it quiet, and quiet is exactly what you want from infrastructure. Boring, reliable, invisible: the three adjectives every system service should aspire to.
