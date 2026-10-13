---
title: "Fix Windows Modules Installer High CPU on an HP Laptop"
slug: how-to-fix-windows-modules-installer-high-cpu-on-hp-laptop
date: 2026-10-13
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "high cpu", "hp laptop", "windows update"]
description: "Stop TiWorker.exe from pinning your HP laptop's CPU: fix stuck Windows Update servicing, repair components, and calm the Modules Installer."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-on-hp-laptop.webp"
faqs:
  - q: "What is Windows Modules Installer (TiWorker.exe)?"
    a: "TiWorker.exe — Windows Modules Installer Worker — is the background process that installs Windows updates, enables and disables Windows features, and maintains system components. High CPU from it is normal during and shortly after updates. It becomes a problem when it runs hot for days with no update in progress, which signals stuck servicing rather than legitimate work."
  - q: "Is it safe to end TiWorker.exe in Task Manager?"
    a: "Ending it is safe in the sense that it won't damage Windows — the process restarts as needed — but it's pointless as a fix, because stuck servicing just resumes the loop. Worse, killing it mid-install can corrupt an update in progress. The correct approach is letting legitimate work finish, then repairing the servicing stack so the loop stops on its own."
  - q: "How long should TiWorker.exe legitimately run hot?"
    a: "During a feature update install, several hours is normal. After a monthly cumulative update, 30 minutes to a couple of hours of elevated activity is typical while it finalizes. Beyond 24 hours with no update activity in Settings → Windows Update, it's no longer legitimate — treat it as stuck servicing and start the repair steps."
  - q: "Will this problem come back after the next Windows update?"
    a: "It can, since each update exercises the same servicing machinery. But a healthy servicing stack handles updates cleanly — recurrence usually means the underlying corruption was never fully repaired, or a specific update keeps failing. Keeping drivers current, maintaining free disk space, and not interrupting updates mid-install are the best prevention."
---

**TiWorker.exe** — the Windows Modules Installer Worker — is supposed to be a temporary guest on your CPU. It shows up, installs updates, maintains Windows features, and leaves. On your HP laptop, though, it's become a permanent resident: 20–40% CPU, day after day, fans droning, battery draining. Nothing is visibly updating. That's not TiWorker doing its job — that's TiWorker stuck.

Stuck Windows servicing is one of the more common persistent-CPU causes on HP laptops, partly because HP's own driver delivery through Windows Update adds servicing workload. The fix sequence below distinguishes legitimate update work from a wedged servicing stack, then repairs the stack properly.

## Why this happens

- **A stuck or failed update:** An update that can't complete keeps the servicing stack retrying indefinitely — the number-one cause.
- **Corrupted servicing stack:** Damaged component store (WinSxS) makes every servicing operation thrash instead of completing.
- **Corrupted SoftwareDistribution cache:** The update download cache in a bad state forces repeated re-downloads and reprocessing.
- **Pending operations never finalizing:** Reboot-pending update operations that never clear keep TiWorker active across restarts.
- **HP driver updates via Windows Update:** HP hardware drivers delivered through Windows Update add servicing passes; a failing HP driver update loops the whole stack.
- **Low disk space:** Servicing needs working room; a nearly-full drive makes operations crawl and retry.
- **Conflicting third-party software:** Aggressive "optimizer" or antivirus tools interfering with the component store.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether an update is actually in progress

Open **Settings → Windows Update** first. If updates are downloading, installing, or pending restart, TiWorker's CPU is legitimate — let it finish, plugged in, without interrupting. Check **Update history** for failed entries; a failed update with error codes is your smoking gun and points directly at Fix 4.

1. **Settings → Windows Update**: note any active or pending items.
2. Check **Update history** for failed updates and error codes.
3. If work is genuinely in progress, allow hours, plugged in — don't interrupt.
4. Failed entries or nothing in progress with high CPU → continue.

### Fix 2: Give legitimate work a deadline

If updates are active, set a mental deadline: monthly updates should settle within a few hours; feature updates within a day. Note TiWorker's CPU trend — decreasing over hours means progress. Flat and unchanging for 24+ hours means stuck, not working. This distinction prevents you from "fixing" something that was about to finish on its own.

1. Note TiWorker.exe CPU now; recheck in 2–3 hours.
2. Decreasing = working; let it finish.
3. Flat after 24 hours = stuck; continue to Fix 3.
4. Never force-shutdown during an active feature update install.

### Fix 3: Run the Windows Update troubleshooter

**Settings → System → Troubleshoot → Other troubleshooters → Windows Update → Run**. It resets update service states, checks for common misconfigurations, and clears simple blockages. It's the gentlest repair and resolves a fair share of stuck-servicing cases without command-line work.

1. **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run **Windows Update**; apply all recommended fixes.
3. Restart the laptop.
4. Check TiWorker CPU after 30 minutes.

### Fix 4: Repair the servicing stack with SFC and DISM

The heavy repair for a corrupted component store. Elevated Command Prompt, in order: `sfc /scannow`, then `DISM /Online /Cleanup-Image /RestoreHealth`. DISM specifically repairs the component store that TiWorker works against — when the store is damaged, servicing thrashes, and this is what fixes it. Allow both to complete fully; they take 15–45 minutes.

1. Elevated Command Prompt: `sfc /scannow` → wait.
2. Then `DISM /Online /Cleanup-Image /RestoreHealth` → wait.
3. Restart the laptop.
4. Observe TiWorker for an hour. The [post-update servicing variant](/articles/how-to-fix-windows-modules-installer-high-cpu-after-windows-11-update/) covers this same repair in the update-triggered scenario.

### Fix 5: Reset the Windows Update cache

A corrupted SoftwareDistribution cache keeps the servicing loop fed with bad data. Stop the update services, rename the cache folders (Windows rebuilds them clean), and restart the services. This is safe — you're discarding downloaded update files, not installed updates.

1. Elevated Command Prompt, run:
   `net stop wuauserv` then `net stop bits`
2. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
3. Run `ren C:\Windows\System32\catroot2 catroot2.old`
4. Run `net start wuauserv` then `net start bits`; restart; check for updates.

### Fix 6: Free disk space and update HP drivers

Servicing needs breathing room: ensure 15–20% free on C: via **Disk Cleanup → Clean up system files**. Then update HP's drivers properly — get chipset and storage drivers from [HP Support](https://support.hp.com/us-en) for your exact model rather than letting Windows Update guess. A failing HP driver update delivered through Windows Update is a known servicing-loop trigger; installing it directly from HP breaks the cycle. The 24H2-specific servicing angle is covered in the [24H2 modules installer guide](/articles/how-to-fix-windows-modules-installer-high-cpu-in-windows-11-24h2/).

1. Disk Cleanup → Clean up system files → remove update leftovers.
2. Confirm 15–20% free on C:.
3. Install HP chipset/storage drivers from HP Support directly.
4. Check Windows Update again; install what succeeds cleanly.

### Fix 7: Manual update via the Catalog (last resort before escalation)

If a specific KB keeps failing and looping TiWorker, bypass the broken path: find the KB number in Update history, download it manually from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), and install it directly. If even that fails, the servicing stack needs deeper repair — an in-place upgrade repair install (keeps files and apps) rebuilds it. Document the failing KB; it's the key detail for any support case.

1. Note the failing KB number from Update history.
2. Download it from the Microsoft Update Catalog; install manually.
3. If it installs cleanly, TiWorker should settle within hours.
4. If all fails → in-place upgrade repair install.

## Closing

TiWorker.exe burning CPU for days isn't Windows updating — it's Windows *failing* to update, over and over. Check for real update activity, give it a fair deadline, run the troubleshooter, repair the component store with DISM, reset the update cache, and feed it disk space and proper HP drivers. Stuck servicing surrenders to methodical repair — and your CPU, fans, and battery all come back when it does.
