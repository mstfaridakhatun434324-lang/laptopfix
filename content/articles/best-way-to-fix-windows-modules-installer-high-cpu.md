---
title: "Windows Modules Installer Eating Your CPU? The Best Way to Fix It"
slug: best-way-to-fix-windows-modules-installer-high-cpu
date: 2026-10-11
categories: ["performance"]
tags: ["windows modules installer", "tiworker.exe", "high cpu", "windows update", "trustedinstaller"]
description: "TiWorker.exe (Windows Modules Installer Worker) pinning your CPU at 100%? Here's the best way to fix it — let updates finish, then repair the update system."
thumbnail: "/images/thumbs/best-way-to-fix-windows-modules-installer-high-cpu.webp"
faqs:
  - q: "What is Windows Modules Installer Worker (TiWorker.exe)?"
    a: "TiWorker.exe is the worker process behind Windows Update, optional feature installation, and system component servicing. When Windows installs updates, adds .NET frameworks, or enables features like Hyper-V, TiWorker.exe does the heavy lifting — extracting, verifying, and registering files. High CPU from it is normal during active servicing, typically lasting 30 minutes to a few hours. It becomes a problem only when it never stops."
  - q: "Can I disable Windows Modules Installer Worker?"
    a: "You shouldn't disable it permanently. TiWorker.exe is how Windows installs security updates — killing the service (Windows Modules Installer / TrustedInstaller) breaks updating entirely and leaves your system unpatched. The right fix is letting it finish its current job, then repairing the Windows Update components if it gets stuck in a loop. Disabling the service is a temporary diagnostic step at most."
  - q: "How long should TiWorker.exe run at high CPU?"
    a: "After a Patch Tuesday update or feature update, expect 30 minutes to 2 hours of elevated CPU, longer on older hard drives or very old laptops. If TiWorker.exe has been at high CPU for more than 4–6 hours with no progress in Windows Update, or if it restarts at high CPU on every single boot, the update components are stuck and need repair using the steps below."
  - q: "Will ending TiWorker.exe in Task Manager break my computer?"
    a: "Ending the task once won't break anything — Windows will restart it, and an interrupted update simply resumes later. But repeatedly killing it mid-install can corrupt the component store over time. If you must end it to use your laptop urgently, do it once, then run the Windows Update troubleshooter and DISM/SFC repairs afterward to make sure the interrupted work completed cleanly."
---

Few things are more frustrating than a laptop that's unusable for no visible reason — fans screaming, everything laggy — only to find `TiWorker.exe`, the Windows Modules Installer Worker, consuming 80–100% of your CPU in Task Manager. Your first instinct might be to kill it. Resist that instinct for a moment, because in most cases TiWorker.exe is doing legitimate, necessary work: installing Windows updates in the background.

The key insight: TiWorker.exe high CPU is a *symptom*, not a disease. The disease is one of three things — an update that's still legitimately installing, an update that's stuck and retrying forever, or a corrupt component store that makes every servicing operation grind. The best fix is a sequence: confirm what it's doing, give it a fair chance to finish, then repair the update machinery if it's stuck.

If your whole system feels slow beyond just this process, our guide to [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) covers the bigger picture, and [Windows 11 slow after an update](/articles/windows-11-slow-after-update-how-to-fix/) addresses the post-update sluggishness that often accompanies TiWorker.exe activity.

## Why this happens

- **Windows Update actively installing**: The normal case — TiWorker.exe works hard while updates download, extract, and install.
- **A stuck update retrying in a loop**: A failed update that keeps retrying on every boot produces endless high CPU.
- **Corrupt component store (WinSxS)**: Damaged servicing files make every operation slow and failure-prone.
- **Pending feature update**: Major Windows version upgrades run TiWorker.exe for hours in the background.
- **Optional features installing**: .NET Framework versions, language packs, or Hyper-V being enabled all use this process.
- **Low disk space during servicing**: Updates need working room — a nearly full drive makes servicing crawl.
- **Conflicting third-party "optimizer" software**: Aggressive cleaners that delete WinSxS or SoftwareDistribution contents mid-update cause corruption loops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check what TiWorker.exe is actually doing

First, determine whether it's working or stuck.

1. Open **Settings** > **Windows Update** — if it shows "Downloading," "Installing," or a percentage progressing, TiWorker.exe is doing its job. Let it finish.
2. Note the timestamp: when did the high CPU start? If it began right after Patch Tuesday (second Tuesday of the month) or after you clicked "check for updates," it's almost certainly legitimate.
3. Open Task Manager > **Details** tab, find **TiWorker.exe**, and check its CPU trend over 10 minutes — steadily working with disk activity is fine; flatlined at 25% with zero disk activity for an hour suggests stuck.
4. Check **Settings** > **Windows Update** > **Update history** for failed updates — a failed entry that keeps reappearing is your stuck-update suspect.
5. Decision rule: if updates are progressing, give it up to 2 hours (plugged in, don't sleep the laptop). If nothing progresses for over an hour, move to Fix 2.

### Fix 2: Give it a clean window to finish

Sometimes TiWorker.exe just needs uninterrupted time.

1. Plug in your laptop — Windows throttles background servicing on battery, which stretches a 40-minute job into a 4-hour one.
2. Go to **Settings** > **System** > **Power & battery** and set the screen to stay on, then leave the laptop alone for 60–90 minutes. Constant use competes with servicing for CPU.
3. Make sure you have at least 10–15 GB free on C: — servicing needs scratch space. If you're low, our [low disk space on C: drive guide](/articles/how-to-fix-low-disk-space-on-c-drive-on-windows-11/) will help you reclaim room quickly.
4. Don't restart repeatedly during this window — each reboot can force TiWorker.exe to restart its current phase from scratch.
5. After the waiting period, check Windows Update again — if it now shows "You're up to date," you're done.

### Fix 3: Run the Windows Update troubleshooter

The built-in troubleshooter fixes common stuck-update states automatically.

1. Go to **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Find **Windows Update** and click **Run**. Let it complete — it resets update services, clears stuck download states, and repairs common misconfigurations.
3. Restart your laptop when it finishes, then check **Settings** > **Windows Update** and click **Check for updates**.
4. Watch TiWorker.exe for 15 minutes after the restart — the troubleshooter often unblocks the queue, causing one final burst of legitimate activity followed by calm.
5. If the troubleshooter reports it couldn't fix everything, note what it found — then proceed to Fix 4 for the manual repair.

### Fix 4: Repair the component store with DISM and SFC

This is the heavy-duty fix for corrupt servicing components — and the one that permanently solves most recurring TiWorker.exe loops.

1. Open **Terminal (Admin)** — right-click Start > **Terminal (Admin)**.
2. Run: `DISM /Online /Cleanup-Image /RestoreHealth` — this downloads clean copies of corrupt system files from Windows Update. It takes 10–20 minutes; let it finish.
3. Then run: `sfc /scannow` — this scans protected system files and repairs them from the now-healthy component store.
4. Restart, then check Task Manager — on many systems, TiWorker.exe settles within minutes of the restart because the corruption that kept it retrying is gone.
5. If DISM fails with an error about the source, run it with explicit source: `DISM /Online /Cleanup-Image /RestoreHealth /Source:WIM:C:\Sources\Install.wim:1 /LimitAccess` (adjust the path to your Windows installation media).

### Fix 5: Reset the Windows Update components manually

When the update cache itself is corrupt, clear it out.

1. Open **Terminal (Admin)** and stop the update services:
   `net stop wuauserv` → `net stop cryptSvc` → `net stop bits` → `net stop msiserver`
2. Rename the corrupt cache folders:
   `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`
3. Restart the services in reverse:
   `net start wuauserv` → `net start cryptSvc` → `net start bits` → `net start msiserver`
4. Go to **Settings** > **Windows Update** > **Check for updates** — Windows rebuilds a fresh, clean download cache and re-attempts pending updates from scratch.
5. Monitor TiWorker.exe — a fresh cache usually means one clean install pass instead of endless retries. Delete the `.old` folders after a week of stable updating.

### Fix 6: Set active hours and metered connections to control timing

You can't stop updates forever, but you can stop them ambushing you.

1. Go to **Settings** > **Windows Update** > **Advanced options** > **Active hours** — set the hours you actually use the laptop so restarts and heavy servicing avoid them.
2. On a metered connection (mobile hotspot), toggle **Settings** > **Network & internet** > your connection > **Metered connection** to On — Windows won't download most updates over metered connections.
3. In **Advanced options**, you can **pause updates** for up to 5 weeks — useful when you need a stable machine for a project, but don't leave it paused indefinitely; security updates matter.
4. Consider switching to manual update checks: pause, then unpause and check manually when convenient — you control when TiWorker.exe gets busy.
5. Never use third-party tools that claim to "permanently disable Windows Update" — they break servicing in ways that cause exactly the loops you're trying to fix.

### Fix 7: Check for the deeper problems

If TiWorker.exe is still stuck after all of the above, look wider.

1. Check your drive health — a failing SSD/HDD makes servicing crawl and fail. Run `wmic diskdrive get status` in Terminal; anything other than "OK" means replace the drive.
2. Run a memory check: press **Win + R**, type `mdsched.exe`, restart and test — corrupt RAM causes file-verification failures that keep servicing retrying.
3. Look for the specific failing update: **Settings** > **Windows Update** > **Update history**, note the KB number, and search it on the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) — some updates have known issues with manual workarounds.
4. Uninstall third-party "PC optimizer" or aggressive antivirus temporarily — these can interfere with the TrustedInstaller service.
5. As a final measure, an in-place repair install (download the Windows 11 ISO from [Microsoft's software download page](https://www.microsoft.com/en-us/software-download/windows11), run setup, choose "keep files and apps") rebuilds the entire servicing stack while preserving everything.

## Closing

Windows Modules Installer Worker high CPU is Windows doing maintenance — the fix is making sure that maintenance can actually complete. Let legitimate updates finish, repair the component store when they're stuck, and reset the update cache when corruption sets in.
