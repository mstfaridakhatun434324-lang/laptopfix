---
title: "What to Do If Shutdown Takes Too Long on Windows 11"
slug: "what-to-do-if-shutdown-takes-long-windows-11"
date: "2026-09-17"
categories: ["performance"]
tags: ["slow shutdown", "windows 11", "shutdown time", "troubleshooting"]
description: "Windows 11 taking minutes to shut down? Find the hanging app, service, or driver delaying shutdown and speed it up."
thumbnail: "/images/thumbs/what-to-do-if-shutdown-takes-long-windows-11.webp"
faqs:
  - q: "How long should Windows 11 take to shut down?"
    a: "On a healthy SSD laptop, shutdown should complete in 10 to 20 seconds from clicking Shut down to power off. Up to 30 seconds is acceptable if several apps were open. Consistently taking over a minute indicates something is hanging: an app refusing to close, a service timing out, or a driver stalling the power transition."
  - q: "Is holding the power button to force shutdown harmful?"
    a: "Occasionally, no; modern file systems are resilient and Windows replays its journal on the next boot. Habitually, yes: forced power-offs interrupt disk writes and can corrupt open files, damage the update state, and over time contribute to file system errors. Fix the underlying hang instead of making forced shutdowns routine."
  - q: "Does Fast Startup make shutdown slower or faster?"
    a: "Fast Startup actually skips the full shutdown sequence by hibernating the kernel session, which usually makes the process faster. But it can also mask the hangs that a true shutdown would reveal, and on some firmware it causes its own delays. Toggling it is a useful diagnostic step when shutdown times are abnormal."
  - q: "Can a Windows update cause slow shutdowns?"
    a: "Yes, temporarily. After cumulative updates, the first shutdown often takes several minutes while Windows finalizes the installation with its configuring updates screen. That is normal and expected. The problem is when slow shutdowns persist across many days with no update in progress, which points to a hanging app or service instead."
---

You click Shut down, the screen says shutting down, and then nothing happens for two minutes. Or the laptop appears off but the power light stays on, fans whispering, for far too long. Slow shutdown is Windows waiting on something that will not let go: an application with unsaved state, a service that will not stop, or a driver stalling the power transition.

The diagnostic approach mirrors a detective story. Windows actually logs shutdown performance, and the Event Viewer records exactly which application or driver held things up and for how long. Most users never look at these logs and instead guess, but the answer is usually sitting in Event ID 203 or 200-series entries waiting to be read.

This guide shows you how to read those logs, identify the hanging component, and apply the targeted fix, plus the settings tweaks that shorten the timeouts Windows waits before giving up on stubborn processes.

## Why this happens

- **An app refusing to close:** Programs with unsaved documents or hung windows block the shutdown sequence until Windows force-closes them.
- **A service timing out:** Background services get 20 seconds by default to stop; a stuck service consumes the full timeout every shutdown.
- **Driver stalling power transition:** Storage or network drivers that mishandle the shutdown IRP delay the final power-off.
- **Pending Windows Update finalization:** Updates that need a shutdown to complete legitimately extend the process, sometimes by many minutes.
- **Fast Startup hibernating a messy session:** Hibernating the kernel session can stall if drivers are in a bad state.
- **Page file clearing enabled:** The ClearPageFileAtShutdown policy writes zeros across the page file, adding minutes on large RAM systems.
- **Hybrid sleep and hibernation file writes:** Writing gigabytes of RAM to hiberfil.sys takes time on slower drives.
- **Corrupted user profile shutdown scripts:** Logoff scripts or profile unload hangs delay the phase before the actual shutdown.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Read the shutdown logs in Event Viewer

Windows logs shutdown performance data. This tells you exactly what hung instead of guessing.

1. Press Win+R, type eventvwr.msc, and press Enter.
2. Navigate to Applications and Services Logs, Microsoft, Windows, Diagnostics-Performance, Operational.
3. Filter for Event IDs 200 through 299, which cover shutdown performance.
4. Look for entries naming a specific application or driver and the delay in milliseconds.
5. Note the culprit; every fix below targets a category these logs reveal.

### Fix 2: Close the hanging application properly

If the log names an app, the fix is usually updating, reconfiguring, or replacing that app rather than a Windows setting.

1. Identify the app from the Event Viewer entry.
2. Check for updates to that application first.
3. Disable any of its features that run at shutdown, like cloud sync on exit.
4. If it is nonessential, uninstall it and find an alternative.
5. Test shutdown three times to confirm the delay is gone.

### Fix 3: Shorten the hung-application timeout

Windows waits 5 seconds for hung apps by default before killing them. On a healthy system you can safely reduce this.

1. Press Win+R, type regedit, and press Enter.
2. Navigate to HKEY_CURRENT_USER\Control Panel\Desktop.
3. Find or create the string value HungAppTimeout and set it to 2000 milliseconds.
4. Find or create WaitToKillAppTimeout and set it to 2000 as well.
5. Restart and time your next shutdowns.

### Fix 4: Shorten the service timeout

Services get 20 seconds each by default. Reducing this speeds shutdowns where a service dawdles but eventually stops.

1. In regedit, navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control.
2. Find or create the string value WaitToKillServiceTimeout.
3. Set it to 5000 milliseconds instead of the default 20000.
4. Do not set it below 2000; services need some time to flush data safely.
5. Restart and verify shutdown time improved without new errors.

### Fix 5: Toggle Fast Startup as a diagnostic

Fast Startup changes the shutdown path significantly. Testing both states isolates firmware versus software hangs.

1. Open Control Panel, Power Options, Choose what the power buttons do.
2. Click Change settings that are currently unavailable.
3. Note the current state of Turn on fast startup, then toggle it.
4. Test three shutdowns in the new state and time them.
5. Keep whichever state shuts down faster and more reliably.

### Fix 6: Check for page file clearing policy

Clearing the page file at shutdown is a security policy that adds minutes on systems with 16 GB or more RAM. Most home users do not need it.

1. Press Win+R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration, Windows Settings, Security Settings, Local Policies, Security Options.
3. Find Shutdown: Clear virtual memory pagefile and set it to Disabled.
4. On Home editions, check the registry value ClearPageFileAtShutdown under Memory Management and set it to 0.
5. Restart and time shutdown again.

### Fix 7: Audit tasks that run at shutdown

Scheduled tasks with logoff or shutdown triggers can delay the process. Reviewing them takes a few minutes.

1. Press Win+R, type taskschd.msc, and press Enter.
2. Browse the Task Scheduler Library for tasks with triggers at log off or shutdown.
3. Disable nonessential ones, especially from software you uninstalled long ago.
4. Pay attention to updater tasks that phone home during shutdown.
5. Test three shutdowns and compare times.

### Fix 8: Audit tasks that run at shutdown

Scheduled tasks with logoff or shutdown triggers can delay the process. Reviewing them takes a few minutes.

1. Press Win+R, type taskschd.msc, and press Enter.
2. Browse the Task Scheduler Library for tasks with triggers at log off or shutdown.
3. Disable nonessential ones, especially from software you uninstalled long ago.
4. Pay attention to updater tasks that phone home during shutdown.
5. Test three shutdowns and compare times.

## Closing

Slow shutdowns are Windows being polite to a fault, waiting on apps and services that will not finish. The Event Viewer tells you who the rude guest is, and the timeout tweaks put a firm limit on everyone's patience. In most cases the fix is updating or removing one hanging application. If shutdowns are slow and startups are too, the broader [slow-after-update checklist](/articles/how-to-fix-windows-11-slow-after-24h2-update/) is worth working through next. If slow shutdowns come with slow startups too, our [slow shutdown checklist](/articles/best-way-to-fix-windows-11-slow-shutdown/) covers the boot side, and Microsoft documents shutdown behavior in its [Windows support hub](https://support.microsoft.com/en-us/windows). If slow shutdowns come with slow startups too, our [slow shutdown checklist](/articles/best-way-to-fix-windows-11-slow-shutdown/) covers the boot side, and Microsoft documents shutdown behavior in its [Windows support hub](https://support.microsoft.com/en-us/windows).
