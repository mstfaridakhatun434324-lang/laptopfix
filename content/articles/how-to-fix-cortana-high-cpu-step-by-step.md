---
title: "How to Fix Cortana High CPU Usage, Step by Step"
slug: how-to-fix-cortana-high-cpu-step-by-step
date: 2026-09-21
categories: ["performance"]
tags: ["cortana", "high cpu", "searchui.exe", "windows 11", "step by step"]
description: "A careful step-by-step walkthrough for fixing Cortana (SearchHost/SearchUI) high CPU usage — from the quick process restart to index rebuilds and policy tweaks."
thumbnail: "/images/thumbs/how-to-fix-cortana-high-cpu-step-by-step.webp"
faqs:
  - q: "Which process is Cortana in Windows 11?"
    a: "In current Windows 11 builds, Cortana's functionality lives in SearchHost.exe (the taskbar search experience), while older builds and Windows 10 use SearchUI.exe. Both may appear labeled as Search or Cortana in Task Manager. They're legitimate Windows components behind the search box — not separate apps you installed."
  - q: "How long should each fix take?"
    a: "The process restart takes under a minute, toggling search settings takes a few minutes, and re-registering the app package takes about five minutes plus a restart. The search index rebuild is the long one — anywhere from 15 minutes to several hours depending on your files — but it runs in the background while you work."
  - q: "Will I lose the taskbar search box?"
    a: "No. None of these steps remove the search box itself. Disabling Cortana's cloud features only removes web results and highlights from your search results — the box stays exactly where it is, and local file, app, and settings search keep working just as before."
  - q: "What if CPU is still high after all steps?"
    a: "Then the problem likely isn't Cortana at all — verify in Task Manager that SearchHost.exe is truly the top consumer and not a similarly-named process. If it is, a Windows repair install (in-place upgrade keeping files) usually resolves deep corruption. Also check for malware masquerading under a similar name."
---

This is the methodical, no-shortcuts walkthrough for fixing Cortana-related high CPU usage on Windows 11. If you've seen SearchHost.exe or SearchUI.exe sitting at 25-50 percent CPU in Task Manager while your laptop does nothing, this guide takes you from the simplest fix to the most thorough, with a checkpoint after each step so you know whether to continue or stop.

The approach is deliberately sequential. Each step targets a deeper layer of the problem: first the stuck process itself, then the settings that trigger it, then the index it chokes on, then the app package, and finally the policy-level controls. After every step, you'll restart the relevant component and check Task Manager for 2-3 minutes. If CPU stays low, stop — there's no need to do the remaining steps.

A note on naming: depending on your Windows 11 build, the process may appear as SearchHost.exe, SearchUI.exe, or simply "Search" in Task Manager. The fixes apply to all of them — they're the same search experience under different build names.

## Why this happens

- **Stuck search process**: The search host can get wedged in a loop after waking from sleep or after a Windows update, burning CPU on nothing.
- **Corrupted search index**: Damaged index data causes endless retry loops as the process tries to read what it can't parse.
- **Cloud search sync problems**: Bing integration and Microsoft account search history syncing can loop when account states change.
- **Search highlights fetching**: The rotating search highlights content in the search box fetches remote content that can hang the process.
- **Damaged app package**: The Windows CBS package containing the search experience can corrupt, causing crash-restart loops.
- **Conflicting privacy settings**: Partially-applied privacy changes leave the process attempting operations that settings block.
- **Third-party software conflicts**: Some utilities that hook into search or the taskbar interfere with the search host.
- **Post-update component mismatch**: Feature updates occasionally leave search components at mixed versions until a repair runs.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the search process (checkpoint: 3 minutes)

The quickest fix. A stuck process often just needs a fresh start.

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. On the **Processes** tab, find **Search** (or SearchHost.exe / SearchUI.exe — click Details tab if needed).
3. Right-click it and choose **End task**. Windows restarts it automatically within seconds.
4. **Checkpoint**: Watch the CPU column for 3 minutes. If it stays under 5%, you're done. If it climbs back up, continue to Fix 2.

### Fix 2: Disable cloud content search and highlights (checkpoint: restart + 3 minutes)

These network-dependent features are the most common loop triggers.

1. Open **Settings > Privacy & security > Search permissions**.
2. Under **Cloud content search**, turn off **Microsoft account** and **Work or School account**.
3. Scroll down to **More settings** and turn off **Show search highlights**.
4. Restart your laptop.
5. **Checkpoint**: After booting, wait 3 minutes and check Task Manager. Stable and low? Stop here.

Local file and app search is unaffected — you only lose web results in the Start menu. For the HP-specific variant of this problem, see our guide on [fixing Cortana high CPU on HP laptops](/articles/how-to-fix-cortana-high-cpu-on-hp-laptop/).

### Fix 3: Rebuild the search index (checkpoint: after rebuild completes)

If the index is corrupted, the process will keep choking on it regardless of settings.

1. Open **Control Panel > Indexing Options**.
2. Click **Advanced**, then **Rebuild** under Troubleshooting. Confirm.
3. Let it run — check progress in the Indexing Options window. It runs in the background; avoid heavy disk work meanwhile.
4. When it shows "Indexing complete," restart your laptop.
5. **Checkpoint**: Monitor Task Manager for 5 minutes. If the search process stays quiet, the corrupted index was your problem.

To reduce future index strain, click **Modify** and uncheck locations you never search.

### Fix 4: Re-register the search app package (checkpoint: restart + 3 minutes)

Repairs a damaged installation of the search experience itself.

1. Press **Win + X** and select **Terminal (Admin)**.
2. Run: `Get-AppXPackage -Name MicrosoftWindows.Client.CBS | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for the command to finish (it may show red text for already-registered items — that's normal).
4. Restart your laptop.
5. **Checkpoint**: Check Task Manager after 3 minutes of idle time.

### Fix 5: Disable Cortana features via policy (checkpoint: restart + 5 minutes)

For users who don't need assistant features, policy-level disabling stops the related background activity.

1. Press **Win + R**, type `gpedit.msc`, press Enter (Pro editions).
2. Go to **Computer Configuration > Administrative Templates > Windows Components > Search**.
3. Set **Allow Cortana** to **Disabled** and **Allow Cloud Search** to **Disabled**.
4. On Home editions, use Registry Editor: create DWORD `AllowCortana` = `0` under `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search` (back up first).
5. Restart.
6. **Checkpoint**: Monitor for 5 minutes. The search box still works for local files and apps.

### Fix 6: Check for conflicting software (checkpoint: after each uninstall)

Some third-party tools interfere with the search host.

1. Think about what changed around when the problem started — new utilities, taskbar customizers, "debloating" tools.
2. Temporarily uninstall the most recent additions one at a time, restarting and checking Task Manager after each.
3. Pay special attention to anything that modifies the taskbar, Start menu, or Windows search behavior.
4. **Checkpoint**: If CPU normalizes after removing something, you've found your conflict — look for an updated version before reinstalling.

### Fix 7: Repair Windows system files (final checkpoint)

The deep repair for corruption that survives everything above.

1. Open an **elevated Command Prompt**.
2. Run `sfc /scannow`. Restart when it completes.
3. If the problem persists, run `DISM /Online /Cleanup-Image /RestoreHealth`. Restart.
4. **Checkpoint**: Give the system 10 minutes of idle time and verify the search process stays under 5% CPU.
5. If it's still high at this point, an in-place Windows repair install (keeping files and apps) is the next step — documented on Microsoft's [Windows support page](https://support.microsoft.com/en-us/windows).

If your CPU trouble is broader than the search process, our [technician's high-CPU checklist](/articles/how-to-fix-high-cpu-usage-on-acer-laptop/) covers the other usual suspects.

## Closing

Cortana high CPU yields to methodical work: restart the stuck process, strip the cloud features that trigger loops, rebuild the corrupted index, repair the package, and only then reach for policy and system repairs. Checkpoints after each step keep you from doing unnecessary work — and most people stop at step two or three.
