---
title: "Update Orchestrator Eating CPU on Your HP Laptop? Fix It Now"
slug: how-to-fix-update-orchestrator-high-cpu-on-hp-laptop
date: 2026-09-12
categories: ["windows-update"]
tags: ["update orchestrator", "high cpu", "hp laptop", "usoclient", "performance"]
description: "UsoClient or Update Orchestrator pinning your HP laptop's CPU? Here's why it happens and the ordered fixes that calm it down for good."
thumbnail: "/images/thumbs/how-to-fix-update-orchestrator-high-cpu-on-hp-laptop.webp"
faqs:
  - q: "What is the Update Orchestrator and why does it use so much CPU?"
    a: "The Update Orchestrator Service (UsoSvc) schedules and coordinates Windows Update operations — scanning, downloading, and installing. High CPU usually means it's stuck in a scan loop: repeatedly checking for updates, failing, and retrying. On HP laptops, HP's own update utilities can trigger extra scan cycles that compound the problem."
  - q: "Is it safe to disable the Update Orchestrator Service?"
    a: "No — don't disable it. UsoSvc is a protected system service, and disabling it breaks Windows Update entirely, leaving you unpatched. The correct fix is resolving whatever is making it loop (corrupt cache, stuck scan state), not killing the service. Fixes below target the cause."
  - q: "Why does this happen more on HP laptops?"
    a: "HP ships Support Assistant, HP Image Assistant hooks, and scheduled tasks that interact with the Windows Update stack. When HP's tools and Windows Update disagree about driver states — or when HP tasks trigger update scans on wake — the orchestrator can get stuck re-scanning. It's a coordination problem, not defective hardware."
  - q: "How can I tell if it's the orchestrator or something else using CPU?"
    a: "Open Task Manager → Details tab, sort by CPU, and look for UsoClient.exe, usocoreworker.exe, or Service Host entries consuming CPU. Cross-check in Task Manager → Services that UsoSvc is running. If those processes spike specifically after boot or wake and settle within 30 minutes, it's normal scan behavior, not a loop."
---

Your HP laptop's fans are screaming, Task Manager shows the Update Orchestrator Service chewing 30–60% CPU, and it's been going for an hour. You haven't asked it to update anything — it's just... busy. This is the UsoSvc scan loop: the orchestrator trying to do its job, hitting something broken, retrying, and never finishing. It's maddening because the process doing the damage is a legitimate Windows component.

On HP machines the loop has favorite triggers: HP Support Assistant's scheduled tasks kicking off redundant update scans, a corrupted update datastore that makes every scan fail the same way, or a stuck 'reboot required' state that the orchestrator keeps trying to resolve. The fixes below go from immediate relief (calm it down now) to permanent resolution (stop the loop from returning). For the pure step-by-step version without the HP specifics, see [fixing Update Orchestrator high CPU step by step](/articles/how-to-fix-update-orchestrator-high-cpu-step-by-step/).

First, confirm the diagnosis: Task Manager → Details → sort by CPU → look for UsoClient.exe or Service Host: Update Orchestrator entries. If they're the top consumers for over 30 minutes, you're in the right guide.

## Why this happens

- **Corrupted update datastore**: A damaged DataStore.edb makes every scan fail identically, so the orchestrator retries forever. The datastore is a single ESE database — one torn page can poison every subsequent scan identically.
- **HP scheduled tasks triggering scans**: HP Support Assistant tasks can fire update scans on schedules that collide with Windows' own. These tasks often fire at logon and wake, which is why the CPU spike follows you around the day.
- **Stuck reboot-required state**: A pending reboot flag the orchestrator can't clear keeps it in a perpetual 'finishing up' loop. The flag persists across reboots by design, so restarting alone never clears a genuinely stuck one.
- **Conflicting HP driver update sources**: HP and Windows Update disagreeing on driver versions causes repeated re-evaluation. Each source corrects the other on alternate scans, producing the endless re-evaluation loop.
- **Corrupt BITS queue**: Failed background transfers keep the orchestrator's download phase spinning. Dead BITS jobs retry with backoff, creating the characteristic sawtooth CPU pattern.
- **Windows Update service wedged**: A half-started wuauserv leaves the orchestrator waiting on a dependency that never responds properly. A half-started service answers health checks just well enough to avoid being restarted automatically.
- **Outdated HP Support Assistant**: Old HP tool versions have known bugs that spam the update stack with scan requests. HP fixed several scan-spam bugs in newer releases, so updating the updater is genuinely the fix.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get immediate relief: restart the orchestrator and its dependencies

This won't fix the root cause, but it stops the CPU burn right now so you can work. Think of this as first aid: it stops the bleeding so you can perform surgery.

1. Open Task Manager → Details → right-click **UsoClient.exe** → End task (it restarts on demand).
2. Win + R → `services.msc` → restart **Update Orchestrator Service** if the option is available.
3. Also restart **Windows Update** and **Background Intelligent Transfer Service**.
4. CPU should drop within minutes. If it climbs again within the hour, continue — the loop's cause is still active.
5. Note the time — if CPU returns within the hour, you have a re-triggering loop, not a one-off spike.

### Fix 2: Tame HP Support Assistant's scheduling

HP's tools are the most common HP-specific trigger. Calm them down. HP's defaults assume a desktop that never sleeps; laptops need gentler schedules.

1. Open HP Support Assistant → settings → change automatic update checks from daily to weekly (or manual).
2. Open Task Scheduler (Win + R → `taskschd.msc`) → Task Scheduler Library → **HP** folder → disable redundant update-check tasks (keep hardware diagnostics).
3. Update HP Support Assistant itself to the latest version from [HP Support](https://support.hp.com/us-en) — old versions have scan-spam bugs.
4. Restart and monitor CPU for an hour.
5. After changing schedules, reboot and confirm in Task Scheduler that the next-run times look sane.

### Fix 3: Clear the corrupted update datastore

A damaged DataStore.edb is the classic infinite-scan cause. Deleting it forces a clean rebuild. Deleting DataStore.edb is safe precisely because it is a cache — Windows treats its absence as never-scanned and rebuilds.

1. Admin Command Prompt: `net stop wuauserv` and `net stop bits`.
2. Navigate to `C:\Windows\SoftwareDistribution\DataStore` and delete **DataStore.edb** (or rename the whole DataStore folder to DataStore.old).
3. `net start wuauserv` and `net start bits`.
4. Run Settings → Windows Update → **Check for updates** once — the first scan rebuilds the database and may take 10–15 minutes, then CPU should settle.
5. Do not delete the whole SoftwareDistribution folder here — the targeted DataStore rebuild is faster and sufficient.

### Fix 4: Resolve the stuck reboot-required flag

An un-clearable reboot flag keeps the orchestrator in cleanup mode forever. Phantom reboot flags are the loop's most frustrating cause because everything looks finished.

1. Check Settings → Windows Update for any 'Restart required' message — if present, just restart (don't postpone).
2. If no message but the loop persists, open Registry Editor and check `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update\RebootRequired` — pending entries here confirm the stuck state.
3. Complete any pending update install, then restart twice (the second restart clears staged flags).
4. Verify the RebootRequired key is empty afterward.
5. If the registry key keeps repopulating, an update is genuinely mid-flight — let it complete instead of fighting it.

### Fix 5: Reset Windows Update components fully

When the datastore rebuild alone doesn't break the loop, reset the whole stack. The full reset is the datastore rebuild's bigger sibling — use it when the targeted fix does not hold.

1. Admin Command Prompt: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`; `ren C:\Windows\System32\catroot2 catroot2.old`.
3. `net start wuauserv`, `net start cryptSvc`, `net start bits`, `net start msiserver`.
4. Check for updates once and let the scan complete. Details: [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).
5. Time the post-reset scan: if it completes in under twenty minutes and CPU settles, you are done.

### Fix 6: Run DISM/SFC to repair the servicing layer

Deep store corruption can make scans fail at the same point every time. Servicing-layer damage is the deep cause that makes scans fail at the same checkpoint every cycle.

1. Admin Command Prompt: `DISM /Online /Cleanup-Image /RestoreHealth`.
2. Then `sfc /scannow`; restart.
3. Monitor Task Manager for 30 minutes after boot — orchestrator CPU should spike briefly during the post-repair scan, then settle.
4. Persistent looping after this points to a third-party trigger — continue to Fix 7.
5. Run the repair on AC power — DISM downloads replacement files and hates interruptions.

### Fix 7: Check for conflicting third-party updaters

Other vendor tools (Intel DSA, NVIDIA, motherboard utilities) can also poke the update stack. Every vendor updater you do not need is a potential scan-trigger you do not need.

1. Task Scheduler → look for non-Microsoft, non-HP update tasks firing frequently; disable the aggressive ones.
2. Update Intel drivers via the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) so driver states stop flip-flopping.
3. In Task Manager → Startup, disable vendor updater entries you don't need.
4. Give the system a full day — the orchestrator's scan cadence normalizes once triggers stop colliding.
5. Revisit Task Scheduler quarterly — updaters love re-enabling their tasks during their own updates.

## Closing

Update Orchestrator high CPU on an HP is a loop, not a workload — and loops have causes. Restart for relief, tame HP's scheduled tasks, rebuild the datastore, clear the reboot flag, and reset the components. Somewhere in that sequence the scan completes, the CPU drops, and your fans finally go quiet. Related guides: [fixing Update Orchestrator high CPU step by step](/articles/how-to-fix-update-orchestrator-high-cpu-step-by-step/) and [reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).
