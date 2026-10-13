---
title: "Windows Search Not Working in Windows 11 24H2? Get It Back"
slug: how-to-fix-windows-search-not-working-in-windows-11-24h2
date: 2026-10-13
categories: ["windows-errors"]
tags: ["windows 11", "windows search", "start menu", "troubleshooting"]
description: "Can't type in Windows Search or getting no results on 24H2? Here's how to restart Search, rebuild the index, and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-windows-search-not-working-in-windows-11-24h2.webp"
faqs:
  - q: "Why is Windows Search not working after the 24H2 update?"
    a: "The 24H2 update changed Search components and can leave the SearchHost process or the search index in a broken state. Corrupted index data, a stuck SearchHost.exe, or damaged system files are the usual causes. The fixes below — restarting the process, rebuilding the index, and running the troubleshooter — resolve the large majority of cases."
  - q: "I can't type in the search box at all. What do I do?"
    a: "That usually means SearchHost.exe has hung. Open Task Manager, find Windows Search or SearchHost.exe under Processes, and End task — it restarts automatically. If typing still fails, restart the Windows Search service in services.msc, or reboot the laptop."
  - q: "Will rebuilding the search index delete my files?"
    a: "No. Rebuilding the index only deletes and recreates the search database — the catalog Windows uses to find things quickly. Your actual files, apps, and settings are completely untouched. The rebuild runs in the background and can take a few hours on large drives."
  - q: "Search shows a blank white box. Is that the same problem?"
    a: "Yes, it's a variant of the same failure — the Search UI process (SearchHost.exe) isn't rendering. The same fixes apply: end the SearchHost task, check for Windows updates that patch Search, and if needed reset the Search app package with PowerShell."
---

Windows Search Not Working in Windows 11 24H2? Get It Back

You press the Windows key, start typing, and... nothing. Or the search box opens but shows no results, or a blank white rectangle where your apps should be. Since the 24H2 update, broken Windows Search has become one of those quietly infuriating problems — everything else works, but the fastest way to launch anything is gone.

The good news: Windows Search is just a handful of processes and a database, and every one of them can be restarted, repaired, or rebuilt. This guide goes from the 30-second fixes to the full index rebuild, in the order you'd want to try them. If your Start menu itself is misbehaving too, our guide to [Start menu problems](/articles/how-to-fix-start-menu-not-working-on-windows-11-on-lenovo-laptop/) pairs well with this one.

## Why this happens

- **SearchHost.exe hung or crashed.** The process that renders the search UI can wedge itself, leaving the box unresponsive or blank.
- **The search index is corrupted.** 24H2's update process can damage the index database, so queries return nothing.
- **The Windows Search service stopped.** If the underlying WSearch service isn't running, indexing and results both die.
- **A 24H2 bug in Search components.** Microsoft has shipped Search-breaking bugs in feature updates before; cumulative updates often contain the fix.
- **Corrupted system files.** Damage to the app packages behind Search (it's a modern app under the hood) breaks it silently.
- **Third-party "debloating" tools.** Scripts that strip Windows components sometimes remove or disable Search dependencies.

## How to fix it

Work through these in order, testing the search box after each step.

### Fix 1: Restart the Search process

The quickest fix for a hung search box.

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. On the **Processes** tab, find **Search** or **SearchHost.exe** (use the search box at the top of Task Manager if needed).
3. Right-click it and choose **End task**. It restarts automatically within seconds.
4. Press the **Win** key and try typing. If search works now, you're done.

### Fix 2: Restart the Windows Search service

If the process restart didn't help, cycle the underlying service.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Search** in the list, right-click it, and choose **Restart**.
3. Double-click it and confirm **Startup type** is set to **Automatic (Delayed Start)** — if it's Disabled, that alone explains everything.
4. Click **OK** and test the search box again.

### Fix 3: Run the Search and Indexing troubleshooter

Windows has a dedicated troubleshooter that fixes common index problems automatically.

1. Go to **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Search and Indexing** and click **Run**.
3. Check the boxes matching your symptoms (can't start a search, no results, etc.) and let it work.
4. Apply any fixes it suggests and retest. It often repairs permissions and service states you'd never find manually.

### Fix 4: Rebuild the search index

Corrupted index data needs a fresh start — this is the heavy hitter.

1. Open **Control Panel** (press **Win + R**, type `control`, Enter), set **View by** to **Small icons**, and open **Indexing Options**.
2. Click **Advanced**, then under **Troubleshooting** click **Rebuild**.
3. Confirm and let it run — indexing restarts from scratch in the background. It can take several hours on a full drive; the laptop stays usable meanwhile.
4. You can watch progress back in **Indexing Options**. Once it shows thousands of items indexed, test search again.

### Fix 5: Reset the Search app package with PowerShell

Search is a modern app package, and re-registering it fixes deep corruption.

1. Open **Windows PowerShell as administrator** (**Win + X > Terminal (Admin)**).
2. Run this command to re-register the Search package:
   `Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to complete (errors in red about already-registered packages are harmless), then reboot.
4. Test search after the reboot.
5. If PowerShell reports the package can't be found at all, your Search app may have been removed by a debloating script — in that case, reinstall it from the Microsoft Store by searching for "Windows Search" or run `wsreset.exe` to clear the Store cache first, since a broken Store cache can block the reinstall.

### Fix 6: Check for Windows updates and repair system files

A 24H2 cumulative update may contain the actual bug fix.

1. Go to **Settings > Windows Update** and install everything pending, then reboot.
2. Open an elevated **Terminal** and run `sfc /scannow`.
3. Follow with `DISM /Online /Cleanup-Image /RestoreHealth`.
4. Reboot once more and test. If Search broke immediately after 24H2 installed and nothing helps, consider whether a recent update should be uninstalled via **Update history > Uninstall updates** — Microsoft documents Search issues on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Create a new user profile to isolate the problem

If Search works in a new account, your profile's Search data is the problem.

1. Go to **Settings > Accounts > Other users > Add account** and create a local account.
2. Sign into it and test search. If it works there, the issue is profile-specific.
3. Back in your main account, you can reset Search data by deleting the index location: stop the **Windows Search** service, then delete everything under `C:\ProgramData\Microsoft\Search\Data\Applications\Windows` and restart the service.
4. Alternatively, migrate to the new profile — copy your files from `C:\Users\OldName` and keep going. Profile-level fixes like this also resolve several [Windows 11 login issues](/articles/how-to-fix-windows-11-login-screen-loop-on-lenovo-laptop/).

## Closing

Windows Search feels like magic until it breaks, and then you realize how often you lean on it — launching apps, finding documents, doing quick math. The fix is almost always in this list: a hung process, a dead service, or a corrupted index. Work through them patiently rather than jumping to drastic measures like a full reinstall. And once search is working again, leave the index alone and let Windows maintain it quietly in the background; the less you poke at it, the happier it stays.
