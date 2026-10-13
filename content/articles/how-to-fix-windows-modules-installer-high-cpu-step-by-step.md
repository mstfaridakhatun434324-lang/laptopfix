---
title: "Windows Modules Installer Worker High CPU: Step-by-Step Fix"
slug: how-to-fix-windows-modules-installer-high-cpu-step-by-step
date: 2026-09-10
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "high cpu", "windows update", "trustedinstaller"]
description: "TiWorker.exe (Windows Modules Installer Worker) eating your CPU? Step-by-step guide to diagnose it, let updates finish, and fix stuck updates."
thumbnail: "/images/thumbs/how-to-fix-windows-modules-installer-high-cpu-step-by-step.webp"
faqs:
  - q: "What is Windows Modules Installer Worker?"
    a: "Windows Modules Installer Worker (TiWorker.exe) is the background process that installs Windows updates, optional features, and system components. When Windows Update is downloading or installing — especially large feature updates — TiWorker legitimately uses high CPU and disk while it decompresses packages, resolves dependencies, and writes system files. It's a core Windows component, not malware, and killing it mid-install can corrupt an update in progress."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "For a monthly cumulative update, expect 15–60 minutes of elevated activity. For a feature update like 24H2, one to three hours is normal, particularly on slower CPUs or hard drives. If TiWorker has been pinning CPU for many hours across multiple days with no update progress in Settings > Windows Update, the update is likely stuck — that's when you intervene with the troubleshooter, the SoftwareDistribution reset, or a manual install."
  - q: "Can I disable Windows Modules Installer Worker?"
    a: "You shouldn't. TiWorker is launched on demand by the TrustedInstaller service, and disabling Windows Update components breaks security patching — leaving you exposed. The correct approach is letting legitimate update work finish, then fixing whatever is stuck if it doesn't. If update-related CPU usage bothers you, set active hours and schedule updates for overnight instead of crippling the update mechanism."
  - q: "Why does TiWorker.exe run even when Windows Update says I'm up to date?"
    a: "Windows Update saying 'you're up to date' only covers the last check — TiWorker also handles optional features, .NET updates, driver installations, Microsoft Store app servicing, and post-install cleanup. Check Settings > Windows Update > Advanced options > Optional updates and the update history for recently installed items still finalizing. Background component store (WinSxS) cleanup via Task Scheduler also triggers TiWorker outside of visible updates."
---

**Windows Modules Installer Worker** (TiWorker.exe) camping at 30–80% CPU in Task Manager sends a lot of people down a malware rabbit hole. It's not malware — it's Windows Update doing its job. TiWorker is the engine that installs updates, optional features, and system components: decompressing packages, resolving dependencies, writing files. That work is legitimately CPU-intensive, and on a big feature update it can run hot for hours.

The key skill here is telling "working" from "stuck." A TiWorker that's making progress will finish and go quiet on its own — interrupting it is how you get corrupted updates. A TiWorker that's been spinning for days with the update progress bar frozen is stuck, and there are clean, safe ways to unstick it. This guide shows you how to tell the difference and what to do in each case. For broader update-related slowness, see [Runtime Broker high CPU after updates](/articles/how-to-fix-runtime-broker-high-cpu-after-windows-11-update/); for general speedups, [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Why this happens

- **Feature update installing**: 24H2-class updates keep TiWorker busy for 1–3 hours — normal.
- **Cumulative update finalizing**: Monthly updates trigger 15–60 minutes of component installation.
- **Stuck or looping update**: A corrupted download makes TiWorker retry the same work endlessly.
- **Corrupted SoftwareDistribution cache**: Damaged update files cause repeated failed install attempts.
- **Component store (WinSxS) cleanup**: Post-update cleanup tasks invoke TiWorker outside visible updates.
- **Optional features installing**: Language packs, .NET versions, and features-on-demand install via TiWorker silently.
- **Driver updates via Windows Update**: Driver packages install through the same pipeline, extending TiWorker's run time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether an update is actually in progress

The most important diagnostic — don't interrupt real work.

1. Open **Settings** > **Windows Update** — look for "Downloading," "Installing," or a pending restart. Any of these means TiWorker is legitimately working.
2. Check the percentage: if it's moving (even slowly), let it cook. Go make coffee.
3. Open **Settings** > **Windows Update** > **Update history** — a recently installed update may still be finalizing components in the background.
4. Check **Advanced options** > **Optional updates** — pending driver or feature installs also drive TiWorker.
5. Rule of thumb: if Windows Update shows activity within the last few hours, TiWorker gets a pass. Only proceed to fixes if it's been stuck for many hours or days.

### Fix 2: Let it finish under good conditions

If it's working, help it finish faster instead of fighting it.

1. Plug in the laptop — Windows throttles update installation on battery, stretching a 30-minute job into hours.
2. Close heavy applications to free CPU and disk for the installer.
3. Stay connected to stable internet — interrupted downloads restart and extend the process.
4. Don't reboot mid-install unless Windows explicitly asks — a forced reboot during component installation is the #1 cause of stuck updates.
5. Set **Active hours** (**Settings** > **Windows Update** > **Advanced options**) so future updates install overnight instead of during your workday.

### Fix 3: Run the Windows Update troubleshooter

For updates that seem stalled.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Windows Update** and follow the prompts — it resets update services and fixes common corruption automatically.
3. Restart after it completes, then check **Settings** > **Windows Update** for movement.
4. This resolves a surprising number of "TiWorker stuck at 50% for two days" cases.
5. Microsoft's guided help for update problems is at [Microsoft Support](https://support.microsoft.com/en-us/windows).

### Fix 4: Reset the SoftwareDistribution cache

The classic fix for corrupted update downloads that keep TiWorker looping.

1. Open Terminal as administrator.
2. Run these commands in order, pressing Enter after each:
   `net stop wuauserv`
   `net stop cryptSvc`
   `net stop bits`
   `net stop msiserver`
3. Rename the cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old`
   `ren C:\Windows\System32\catroot2 catroot2.old`
4. Restart the services:
   `net start wuauserv`
   `net start cryptSvc`
   `net start bits`
   `net start msiserver`
5. Go to **Settings** > **Windows Update** > **Check for updates** — Windows rebuilds the cache and re-downloads cleanly. TiWorker should now make steady progress.

### Fix 5: Repair the component store with DISM and SFC

When TiWorker struggles with damaged system components.

1. In an elevated Terminal, run: `DISM /Online /Cleanup-Image /RestoreHealth` — this repairs the component store TiWorker works from. It takes 10–20 minutes.
2. Then run: `sfc /scannow` to fix protected system files.
3. Restart, then check Windows Update again.
4. If DISM itself fails, the component store is badly damaged — consider the in-place upgrade in Fix 7.
5. These two commands fix a wide class of "update installs to 90% then rolls back" loops that keep TiWorker churning.

### Fix 6: Install the stuck update manually

Bypass the broken automatic pipeline.

1. In **Settings** > **Windows Update** > **Update history**, note the KB number of the failing update (e.g., KB5037771).
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/), search the KB number, and download the version matching your system (x64 for most laptops).
3. Run the downloaded `.msu` file — the standalone installer often succeeds where Windows Update loops.
4. Restart when prompted and verify in Update history that it shows as installed.
5. Manual installs don't fix the underlying Windows Update problem, but they get the security patch applied — then run the troubleshooter (Fix 3) to heal the pipeline.

### Fix 7: In-place upgrade repair (last resort)

Refresh Windows while keeping everything.

1. Download the Windows 11 Installation Assistant or ISO from the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Run setup from within Windows and choose **Keep personal files and apps**.
3. This reinstalls all system components — including the entire update pipeline — while preserving your files and programs. It takes 30–90 minutes.
4. Afterward, TiWorker behavior should be completely normal.
5. This is the definitive fix for update systems damaged beyond what DISM can repair.

## Closing

Windows Modules Installer Worker high CPU is Windows Update working — until it isn't. Check for real progress first, give legitimate installs the plugged-in time they need, and only reach for the cache reset and repair tools when TiWorker is clearly stuck. Nine times out of ten, patience or a SoftwareDistribution reset ends the story.
