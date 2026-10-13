---
title: "Windows Update Service Not Running? How to Fix It"
slug: "how-to-fix-windows-update-service-not-running-reddit"
date: "2026-10-05"
categories: ["windows-update"]
tags: ["windows-update", "wuauserv", "services", "windows-11"]
description: "The Windows Update service refuses to start or keeps stopping? Here's how to repair it, from service settings to component resets."
thumbnail: "/images/thumbs/how-to-fix-windows-update-service-not-running-reddit.webp"
faqs:
  - q: "How do I know the Windows Update service is the problem?"
    a: "The classic signs are error codes like 0x80070422, messages saying the service is not running, and the troubleshooter reporting it could not start the service. You can confirm directly by opening services.msc and checking whether the Windows Update service shows as Running. If it is stopped or set to Disabled, you have found your culprit."
  - q: "Why does the Windows Update service keep stopping by itself?"
    a: "Services stop on their own when they crash, which usually means corrupted service files, damaged dependencies like BITS or the cryptographic service, or interference from third-party software. Some aggressive 'debloat' scripts and optimizers also disable the service deliberately. Finding which of these applies determines whether you need a repair or just a settings change."
  - q: "Is it safe to set the Windows Update service to Automatic?"
    a: "Yes. Automatic or Manual are both normal startup types for this service; Windows starts it on demand when set to Manual. The problematic setting is Disabled, which prevents it from running at all. Setting it to Manual is the default on a healthy system and the safest choice if you are unsure."
  - q: "What if the service starts but updates still fail?"
    a: "Then the service was a symptom rather than the root cause. A running service with failing updates points to cache corruption, network issues, or component store damage instead. Work through the cache clear and component reset steps in this guide anyway, since they repair the infrastructure the service depends on, then troubleshoot the specific error code Windows Update reports."
---

Everything in Windows Update flows through a single service, wuauserv, and when it will not run, nothing else in the update pipeline can work either. The symptoms are distinctive: error 0x80070422, the troubleshooter complaining it could not start the service, or updates that fail instantly instead of after trying. The good news is that a dead update service is one of the more straightforward problems to fix, because the causes are a short list.

This is a frequent topic in community troubleshooting because so many different things can stop the service — from overzealous optimizer tools to genuine corruption. The steps below move from the simple settings check through to full component repair, so you stop at whatever level fixes it.

The Windows Update service, wuauserv, is the front door of the entire update pipeline: the scan, the download, and the install orchestration all go through it. When it will not run, the symptoms are unmistakable — instant failures, error 0x80070422, and a troubleshooter that reports it could not start the service. What surprises people is how often the service was turned off deliberately by software they installed themselves: debloat scripts, privacy tools, and optimizers all treat the update service as fair game. The repair is therefore two jobs, not one: switch the service back on, and find what switched it off.

## Why this happens

- **Startup type set to Disabled:** Debloat scripts, optimizers, and some tutorials disable the service outright.
- **Corrupted service files:** Damaged binaries or registry entries prevent the service from starting even when enabled.
- **Broken dependencies:** The update service relies on BITS, RPC, and the cryptographic service; if they are broken, it cannot start.
- **Third-party interference:** Security suites and system "tuners" sometimes block or kill the service.
- **Policy restrictions:** Group Policy can disable the service on managed or previously managed machines.
- **Corrupt SoftwareDistribution state:** A damaged data store can crash the service moments after it starts.
- **System file corruption:** Broader Windows corruption takes the service down with it.
- **Stuck in a stop-pending state:** A previous failed stop can leave the service wedged until the machine restarts.

## How to fix it

Work through these in order — diagnose first, then act.

As you work through these steps, pay attention to whether the service starts and then stops again on its own. A service that will not start points to configuration or corruption; a service that starts and dies points to crashing dependencies or active interference — and that distinction tells you which half of this guide matters most.

### Fix 1: Check and correct the service settings

Most cases end here — the service was simply disabled.

1. Press Win + R, type `services.msc`, and press Enter.
2. Find Windows Update in the list and double-click it.
3. Set Startup type to Manual, which is the healthy default.
4. Click Start, then Apply and OK, and confirm the status shows Running.
5. Try Windows Update again immediately to see if the pipeline works.

### Fix 2: Restart cleanly to clear a wedged state

A service stuck stopping will not respond to Start commands until the machine reboots.

1. Save your work and perform a full restart, not a shutdown with fast startup.
2. After booting, open services.msc and check the Windows Update service status.
3. If it shows Running now, the wedge is cleared — test Windows Update.
4. If it is still stopped, continue with the fixes below.

### Fix 3: Verify the dependency services

The update service cannot run if its dependencies are broken.

1. In services.msc, check Background Intelligent Transfer Service and set it to Manual, then start it.
2. Check Cryptographic Services the same way and make sure it is running.
3. Check Remote Procedure Call, which should already be running and set to Automatic.
4. Return to the Windows Update service and try starting it again.

### Fix 4: Remove third-party interference

Security and tuning tools are common service-killers.

1. Temporarily disable your third-party antivirus real-time protection.
2. Close or uninstall any "debloat," optimizer, or update-blocking utilities.
3. Try starting the Windows Update service again with the interference removed.
4. If it starts, re-enable your antivirus and look for a setting in the other tool that was disabling updates.

### Fix 5: Reset the service with the command line

When the GUI will not cooperate, direct commands sometimes succeed.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv` — it may report the service is not started, which is fine.
3. Run `sc config wuauserv start= demand` to set the startup type to Manual. Note the space after the equals sign.
4. Run `net start wuauserv` and confirm it reports the service started successfully.

### Fix 6: Repair system files

Corruption in the service's files or registry entries needs the standard repair tools.

1. In an admin Command Prompt, run `DISM /Online /Cleanup-Image /RestoreHealth`.
2. When DISM finishes, run `sfc /scannow`.
3. Restart the laptop after both complete.
4. Check the service status again and test Windows Update.
5. If the troubleshooter was also misbehaving, our guide on [fixing the Windows Update troubleshooter](/articles/how-to-fix-windows-update-troubleshooter-not-working/) pairs well with this step.

### Fix 7: Clear the SoftwareDistribution data store

A corrupted data store can crash the service seconds after it starts.

1. Open an admin Command Prompt and run `net stop wuauserv` and `net stop bits`.
2. Rename the store: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`.
3. Run `net start wuauserv` and `net start bits` to rebuild the store fresh.
4. Check that the service stays running this time, then retry updates.

### Fix 8: Check for policy blocks

A lingering policy can force the service to stay disabled no matter what you set.

1. Press Win + R and type `gpedit.msc`. Home edition users can skip this fix.
2. Go to Computer Configuration, Administrative Templates, Windows Components, Windows Update.
3. Look for policies that disable update functionality and set them to Not Configured.
4. Run `gpupdate /force` in an admin Command Prompt, restart, and verify the service starts.

A final preventive note: once the service is healthy, consider what you install next. The most common repeat offenders are ‘debloater’ scripts from forums and aggressive privacy tools that re-disable the service on a schedule. If updates break again weeks from now, check the service first — a repeat 0x80070422 almost always means the offending tool is still installed. For machines where the disabled service is the specific error code rather than a symptom, our dedicated [0x80070422 repair guide](/articles/how-to-fix-windows-update-error-0x80070422-on-laptop/) goes deeper into the policy and registry angles.

## Closing

A Windows Update service that will not run is usually disabled by a tool, blocked by a policy, or crashing on corruption — and each of those has a direct fix in the sequence above. Once the service starts and stays running, Windows Update typically resumes normal operation, though a cache clear afterward is cheap insurance against the next failure.
