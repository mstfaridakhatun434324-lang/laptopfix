---
title: "Windows Search Not Working? Repair It (Even After a Blue Screen)"
slug: windows-search-not-working-blue-screen-error-fix
date: 2026-10-02
categories: ["windows-errors"]
tags: ["windows search", "blue screen", "windows 11"]
description: "Windows Search broken or crashing — sometimes alongside blue screens? Rebuild the index, repair system files, and restore search step by step."
thumbnail: "/images/thumbs/windows-search-not-working-blue-screen-error-fix.webp"
faqs:
  - q: "Why did Windows Search stop working after a blue screen?"
    a: "Blue screens can corrupt the search index database or damage the SearchHost process files. The index is a large database file that's vulnerable to sudden shutdowns — rebuilding it usually restores search completely."
  - q: "Will rebuilding the search index delete my files?"
    a: "No. The index is just a catalog for fast searching; rebuilding it doesn't touch your actual files. It takes a while to re-index (sometimes hours), during which search results may be incomplete."
  - q: "Search shows a blank box when I type. What's wrong?"
    a: "That's usually the SearchHost.exe process hanging or the index being corrupt. Restarting the Windows Search service and rebuilding the index fixes it in most cases. Corrupt system files are the next suspect."
  - q: "Can I just disable Windows Search instead?"
    a: "You can, but you'll lose Start menu search and fast file search. It's better to fix it — the repairs below take less time than living without search. Only disable it as a temporary diagnostic step."
---
Windows Search dies in annoying ways: you type in the Start menu and nothing happens, the search box is blank, or results never appear. Sometimes it breaks right after a blue screen corrupts the index — the search database is a large file that's especially vulnerable to sudden shutdowns, and one bad crash can leave it unreadable. Other times it just quietly stops working after an update reshuffles system components.

Either way, the repair path is the same — restart the search components, rebuild the index, and repair any underlying system damage. Work through these in order. If your machine is also blue-screening regularly, fix the crashes first with our [blue screen guide](/articles/how-to-fix-blue-screen-of-death-windows-11/) — a corrupting crash will just break search again.

## Why this happens

- **Corrupted search index.** The index database gets damaged, especially by sudden shutdowns.
- **SearchHost.exe hanging.** The search UI process crashes or deadlocks.
- **Windows Search service stopped.** The background service fails to start.
- **Corrupted system files.** Damage to search-related Windows components.
- **Broken Cortana/Search app package.** The UWP search app registration breaks.
- **Third-party software conflicts.** Some utilities interfere with search indexing.
- **Disk errors.** Bad sectors in the index location corrupt the database repeatedly.

## How to fix it

Work through these in order — test search after each.

### Fix 1: Restart the Windows Search service

The quickest fix for a hung search backend.

1. Press **Win + R**, type `services.msc`, and press **Enter**.
2. Find **Windows Search** in the list.
3. If it's running, right-click and choose **Restart**. If it's stopped, right-click and choose **Start**.
4. Double-click it and set **Startup type** to **Automatic (Delayed Start)**.
5. Press **Win + S** and test typing a query.
6. If search works now, you're done. If the service keeps stopping on its own, continue — something deeper is wrong.

### Fix 2: End and restart SearchHost

The search UI process sometimes needs a kick.

1. Press **Ctrl + Shift + Esc** to open Task Manager.
2. Go to the **Details** tab and find **SearchHost.exe**.
3. Right-click it and choose **End task**. (It restarts automatically.)
4. If you don't see it, check under **Processes** for **Search**.
5. Try **Win + S** again after 30 seconds.
6. If the search box was blank and now shows suggestions, the hung process was the problem.

### Fix 3: Run the Search and Indexing troubleshooter

Windows has a dedicated troubleshooter for this.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Search and Indexing**.
3. Check the boxes matching your symptoms (search doesn't start, shows no results, etc.).
4. Apply any fixes it suggests.
5. Restart the laptop when it finishes.
6. Test with several different queries — files, apps, and settings — to confirm full function.

### Fix 4: Rebuild the search index

The definitive fix for index corruption.

1. Open Control Panel and go to **Indexing Options** (switch to small icons view if needed).
2. Click **Advanced**.
3. Under Troubleshooting, click **Rebuild**. Confirm the prompt.
4. Rebuilding takes a long time — potentially several hours on large drives. You can keep using the laptop; search results will be incomplete until it finishes. To speed things up, avoid moving large numbers of files around while the rebuild runs, since every change adds to the indexing queue.
5. Monitor progress in the Indexing Options window — wait for "Indexing complete." You can also click **Modify** in Indexing Options afterward to confirm your key folders (Users, Start Menu) are included in indexed locations.
6. Test search thoroughly afterward. If the index corrupts again quickly, run `chkdsk C: /f` — recurring corruption suggests disk problems.

### Fix 5: Re-register the Search app package

For when the search app itself is broken.

1. Open an elevated PowerShell: right-click **Start > Terminal (Admin)**.
2. Re-register the search/Cortana package:
   `Get-AppxPackage -AllUsers Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for completion, ignoring red text.
4. Restart the laptop.
5. Press **Win + S** and verify the search UI opens and returns results.
6. If the package won't re-register, run `sfc /scannow` first — the package files themselves may be corrupt.

### Fix 6: Repair system files

Underlying corruption breaks search repeatedly.

1. Open an elevated terminal.
2. Run:
   `DISM /Online /Cleanup-Image /RestoreHealth`
3. Then:
   `sfc /scannow`
4. Restart.
5. After repairing, rebuild the index once more (Fix 4) to ensure it's built from healthy components.
6. Microsoft's repair documentation on [support.microsoft.com](https://support.microsoft.com/en-us/windows) covers advanced DISM scenarios.

### Fix 7: Create a new user profile

If search works for other users, your profile's search data is corrupt.

1. Open **Settings > Accounts > Other users** and add a new local account (make it administrator).
2. Sign into the new account and test **Win + S**.
3. If search works there, the old profile's search database is unrecoverable — migrate your files.
4. Copy Documents, Desktop, Downloads, and other data from `C:\Users\<oldname>`.
5. Reinstall your apps on the new profile as needed.
6. If search is broken on a fresh profile too, the problem is system-wide — consider an in-place upgrade from [Microsoft's download page](https://www.microsoft.com/en-us/software-download/windows11). For systems that also crash to blue screens with memory errors, our [MEMORY_MANAGEMENT guide](/articles/how-to-fix-memory-management-bsod-on-asus-laptop/) covers the hardware angle.

## Closing

Windows Search failures are almost always the index or the SearchHost process — Fix 1 and Fix 4 resolve the large majority. When blue screens preceded the breakage, always repair the crash cause first, or you'll be rebuilding the index again next week. Once search is healthy, leave the Windows Search service on Automatic and let indexing finish after big file changes; a complete index is what makes search feel instant. And if you ever see the troubleshooter report problems it can't fix, take that as an early warning to check your drive health — search is often the canary in the coal mine for failing storage.
