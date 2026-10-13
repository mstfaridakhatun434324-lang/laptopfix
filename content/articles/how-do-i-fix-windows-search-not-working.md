---
title: "Windows Search Not Working? Here's How to Fix It"
slug: how-do-i-fix-windows-search-not-working
date: 2026-09-23
categories: ["windows-errors"]
tags: ["windows search", "search fix", "indexing", "windows 11", "start menu"]
description: "Windows Search broken on your laptop? Here's how to fix it step by step — restarting search, rebuilding the index, and repairing system files."
thumbnail: "/images/thumbs/how-do-i-fix-windows-search-not-working.webp"
faqs:
  - q: "How do I fix Windows Search when typing does nothing?"
    a: "Start with the fastest fixes: restart the SearchHost.exe process in Task Manager, then run the built-in Search and Indexing troubleshooter under Settings > System > Troubleshoot. If typing still does nothing, verify the Windows Search service is running in services.msc, then rebuild the search index from Control Panel > Indexing Options > Advanced. These four steps resolve the large majority of cases."
  - q: "Why is my Windows Search blank when I open it?"
    a: "A blank search window almost always means the SearchHost.exe process has crashed or the search app package is damaged. End SearchHost.exe in Task Manager's Details tab and reopen search — Windows relaunches it automatically. If the blank window persists, re-register the search app package with PowerShell or repair the system files with DISM and SFC, as described in the steps below."
  - q: "How long does rebuilding the search index take?"
    a: "Anywhere from thirty minutes to several hours, depending on how many files are on your drive and whether it's an SSD or HDD. SSDs rebuild dramatically faster. You can keep using your laptop during the rebuild, but search results will be incomplete until it finishes. Check progress in Control Panel > Indexing Options, which shows the number of items indexed."
  - q: "Will these fixes delete any of my files?"
    a: "No. Every fix in this guide — restarting processes, running troubleshooters, rebuilding the index, re-registering app packages, repairing system files — leaves your personal files completely untouched. The index rebuild only recreates the search catalog, not the files it catalogs. Your documents, photos, and installed apps are safe throughout."
---

When Windows Search breaks, it breaks your whole workflow. You press the Windows key, type the name of an app or file you need, and get... nothing. A blank panel. A spinner that never resolves. It's the kind of failure that makes a fast laptop feel broken, because the feature you use fifty times a day is suddenly gone.

The good news: Windows Search is very fixable. It's a set of well-understood components — a UI process, an indexing service, a database, and some system files — and each has a standard repair. You don't need to reinstall Windows, and you won't lose any files. This guide gives you the repairs in the order a technician would try them: quick process restarts first, then the built-in troubleshooter, then the index rebuild, then the deeper system repairs. If you'd rather diagnose the root cause first instead of working through fixes, our [diagnostic walkthrough](/articles/troubleshoot-windows-search-not-working/) takes the troubleshooter's approach to the same problem.

## Why this happens

- **SearchHost.exe crashed**: The search UI runs as its own process. When it hangs or crashes, the search box goes blank or won't open while the rest of Windows works fine.
- **Windows Search service stopped**: The indexing service can be stopped by updates, crashes, or third-party "optimizer" tools — without it, no new results get indexed.
- **Corrupted search index**: Sudden shutdowns and disk errors damage the index database, producing missing or stale results.
- **Broken app package after an update**: Windows updates occasionally damage the system app packages that power the search experience.
- **Damaged system files**: Corruption in shared Windows components breaks search along with other features.
- **Third-party interference**: Start menu replacements, aggressive antivirus, and privacy tools hook into or disable search components.
- **Corrupt user profile**: Sometimes search works for a new user account but not yours, pointing at profile-level damage.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Restart the SearchHost process

The thirty-second fix that resolves a surprising number of cases.

1. Press **Ctrl + Shift + Esc** to open Task Manager and switch to the **Details** tab.
2. Find **SearchHost.exe**, right-click it, and choose **End task**.
3. Press **Windows + S** — Windows automatically relaunches the process and the search window should now work.
4. If search breaks again after every reboot, something is crashing it at startup — keep going; don't just repeat this forever.

### Fix 2: Run the Search and Indexing troubleshooter

Let Windows diagnose itself before you do manual surgery.

1. Open **Settings** > **System** > **Troubleshoot** > **Other troubleshooters**.
2. Click **Run** next to **Search and Indexing**.
3. Select the symptoms that match yours and let the troubleshooter apply its fixes.
4. Test search immediately after. Microsoft's [support pages](https://support.microsoft.com/en-us/windows) document further manual steps if the troubleshooter reports it couldn't fix everything.

### Fix 3: Make sure the Windows Search service is running

No service, no indexing, no results.

1. Press **Windows + R**, type `services.msc`, and press Enter.
2. Scroll to **Windows Search**. Confirm **Status** is **Running** and **Startup type** is **Automatic (Delayed Start)**.
3. If not, double-click the service, set the startup type, click **Start**, then **OK**.
4. Ask yourself what stopped it — if you use a system "debloater" or privacy tool, it likely did this. Configure an exception or the fix won't survive a reboot.

### Fix 4: Rebuild the search index

The standard cure for missing, incomplete, or stale results.

1. Open **Control Panel**, switch to icon view, and open **Indexing Options**.
2. Click **Advanced**, then click **Rebuild** under Troubleshooting, and confirm.
3. Leave the laptop on — the rebuild takes 30 minutes to several hours. You can work normally; results improve as it progresses.
4. When finished, verify your user folders are still in the indexed locations list — updates sometimes silently remove them.

### Fix 5: Re-register the search components

For cases where the search window won't open at all, refresh the app packages.

1. Right-click **Start** and open **Windows Terminal (Admin)**.
2. Run: `Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Ignore red errors about packages that are already registered — those are harmless.
4. Restart the laptop and test. If a new local user account (**Settings** > **Accounts** > **Other users** > **Add account**) has working search, your profile is corrupt — migrate to the new account rather than fighting the old one.

### Fix 6: Repair Windows system files

Update damage to shared components needs DISM and SFC.

1. In **Windows Terminal (Admin)**, run `DISM /Online /Cleanup-Image /RestoreHealth` and wait for completion.
2. Then run `sfc /scannow` and restart when it finishes.
3. Test search after rebooting. If the damage came from a specific update, grab the revised version from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) rather than letting the broken one reinstall.
4. These repairs also fix other quietly broken features — Start menu tiles, Settings search, and Widgets often recover alongside.

### Fix 7: Check for interfering third-party software

Sometimes the "fix" is removing the thing that broke it.

1. Uninstall or temporarily disable Start menu replacements (Start11, Open-Shell) and test search.
2. Check your antivirus — temporarily disable its real-time protection and test. If search works, add an exclusion for `SearchHost.exe` and the index location (`C:\ProgramData\Microsoft\Search`).
3. Review recently installed "optimizer," "privacy," or "debloater" tools in **Settings** > **Apps** > **Installed apps** sorted by date. Undo their changes or uninstall them.
4. After removing the culprit, rebuild the index once more (Fix 4) to undo any damage it caused.

## Closing

Windows Search looks like magic and breaks like plumbing — but the repairs are straightforward once you know the components. Restart the process, run the troubleshooter, check the service, rebuild the index: that sequence alone fixes the vast majority of cases in under an hour, most of it unattended rebuild time. The deeper lesson is to be wary of tools that promise to "optimize" or "debloat" Windows — disabling the Search service is one of their favorite tricks, and the five minutes of snappiness they buy isn't worth breaking the feature you use fifty times a day. If the search box is only one of several misbehaving system apps, our [Microsoft Store repair guide](/articles/how-to-fix-windows-store-not-opening-in-windows-11-24h2/) covers the shared AppX repair techniques that fix them together.
