---
title: "Best Way to Fix Windows Search Not Working"
slug: best-way-to-fix-windows-search-not-working
date: 2026-09-17
categories: ["windows-errors"]
tags: ["windows search", "windows 11", "troubleshooting"]
description: "Windows Search showing blank results or refusing to open? Restart the search services, rebuild the index, and get it working again with these proven steps."
thumbnail: "/images/thumbs/best-way-to-fix-windows-search-not-working.webp"
faqs:
  - q: "Why did Windows Search suddenly stop working?"
    a: "The usual triggers are a Windows update that broke the search component, a corrupted search index, the Windows Search service crashing, or a damaged user profile. Third-party tools that disable web search or telemetry can also break it. Because search depends on several moving parts — the index, the service, and the SearchHost app — any one of them failing produces the same blank or frozen search box."
  - q: "Will rebuilding the search index delete my files?"
    a: "No, rebuilding only deletes and recreates the index database, not your actual files. Your documents, emails, and settings stay exactly where they are. The rebuild can take anywhere from 30 minutes to a few hours depending on how many files you have, and search results will be incomplete until it finishes, so start it when you can leave the laptop running."
  - q: "What if search works in a new user account but not mine?"
    a: "That confirms your user profile is corrupted, which is actually good news — Windows itself is fine. You can migrate to the new account by copying your files from the old profile folder, or try repairing the profile by re-registering the search package. Most people find moving to a fresh profile faster and more reliable than chasing the corruption."
  - q: "Does disabling web search results break Windows Search?"
    a: "It shouldn't, but registry tweaks and third-party privacy tools that disable Bing integration sometimes break the whole search box instead of just hiding web results. If search broke right after you ran a debloating or privacy tool, undo its changes or restore the related registry keys. The fixes below, especially re-registering the search app, usually repair the damage."
---

You press the Windows key, type the name of a program you use every day, and get... nothing. Or the search box opens and instantly freezes. Windows Search breaking is one of those small failures that makes the whole laptop feel broken.

The best approach is to work from the lightest fix to the heaviest: restart the search processes, then the service, then rebuild the index, and only then touch the deeper repairs. Most people are fixed by step three.

## Why this happens

- **The search index is corrupted.** The database Windows uses to find files quickly gets damaged, so queries return blank results.
- **Windows Search service crashed.** If the background service stops, the search box has nothing to talk to.
- **A Windows update broke the search app.** Feature updates sometimes ship with a broken SearchHost or shell component.
- **Corrupted user profile.** Profile-specific search settings and caches can break while everything else works fine.
- **Third-party interference.** Debloating scripts, privacy tools, and some antivirus products disable parts of the search pipeline.
- **System file corruption.** Damaged Windows components that search depends on cause silent failures with no error message.

## How to fix it

Work through these in order, from Fix 1 onward, and stop as soon as search works again.

### Fix 1: Restart the search processes

The quickest fix — the search app sometimes just needs a fresh start.

1. Press **Ctrl + Shift + Esc** to open **Task Manager**.
2. On the **Processes** tab, find **SearchHost.exe** (it may be listed under Background processes).
3. Right-click it and choose **End task** — Windows restarts it automatically.
4. Also restart **Windows Explorer**: find it in the list, right-click, and choose **Restart**.
5. Press **Win + S** and test the search box immediately.

### Fix 2: Run the Search and Indexing troubleshooter

Windows has a built-in troubleshooter that catches the common misconfigurations automatically.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Find **Search and Indexing** and click **Run**.
3. Check the boxes that describe your problem (for example, "Files don't appear in search results").
4. Let it apply any fixes it finds and follow its recommendations.
5. Test search again — if the troubleshooter found nothing, move on to Fix 3.

### Fix 3: Restart the Windows Search service

If the service itself is stuck, restarting it clears the jam.

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Scroll to **Windows Search** in the list.
3. Right-click it and choose **Restart**. If it's stopped, choose **Start** instead.
4. Double-click it and set **Startup type** to **Automatic (Delayed Start)** so it reliably starts with Windows.
5. Wait a minute, then test the search box.

### Fix 4: Rebuild the search index

When the index database is corrupt, rebuilding it from scratch is the definitive fix. It takes a while but works.

1. Open **Control Panel** and search for **Indexing Options**, then open it.
2. Click **Advanced** at the bottom of the window.
3. Under Troubleshooting, click **Rebuild** and confirm the warning.
4. Leave the laptop plugged in and running — a full rebuild can take one to several hours.
5. Check back in Indexing Options: when it says "Indexing complete," test your searches.

### Fix 5: Re-register the Windows Search app

If the search box won't even open, the app package itself may be damaged. This PowerShell command re-registers it.

1. Press **Win + X** and choose **Terminal (Admin)**.
2. Paste this command and press Enter:
   `Get-AppXPackage -Name Microsoft.Windows.Search | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}`
3. Wait for it to finish — ignore any red warnings about packages already being registered.
4. Restart your laptop.
5. Test **Win + S**. If the box opens and searches work, you're done.

### Fix 6: Install pending Windows updates

Microsoft regularly ships fixes for broken search components through normal updates.

1. Open **Settings > Windows Update** and click **Check for updates**.
2. Install everything offered, including optional driver updates.
3. Restart even if it doesn't ask you to — search components often only reload at boot.
4. If search broke right after an update instead, go to **Update history > Uninstall updates** and remove the most recent one as a test.
5. Our [update troubleshooting guide](/articles/how-to-fix-windows-search-not-working-on-windows-11/) covers trickier update-related search failures.

### Fix 7: Test with a new user profile

This tells you definitively whether the problem is your profile or Windows itself.

1. Open **Settings > Accounts > Other users** and click **Add account**.
2. Create a local account (choose **I don't have this person's sign-in information > Add a user without a Microsoft account**).
3. Sign out and sign in to the new account.
4. Test Windows Search there.
5. If it works, your old profile is corrupt — copy your files over and switch to the new account rather than fighting the old one.

### Fix 8: Make sure your folders are included in the index

Sometimes search "breaks" simply because the locations you search stopped being indexed.

1. Open **Indexing Options** from the Control Panel again.
2. Click **Modify** and expand the folder tree.
3. Make sure **Users** (or at least your user folder) is checked — if it got unchecked, that's your whole problem.
4. Click **Advanced > File Types** and confirm common types like docx, pdf, and txt are set to **Index Properties and File Contents** if you want content search.
5. Click **OK**, let indexing catch up, and test again.

## Closing

Windows Search is fragile because so many pieces have to cooperate, but that also means there's always a fix — you just have to find which piece broke. Start light with a process restart and escalate only as needed, giving the index time to rebuild before judging the result. If search is fine but your Start menu is misbehaving too, a [clean boot](/articles/how-to-perform-clean-boot-windows-11-on-laptop/) can reveal conflicting software. Microsoft's [official search troubleshooting article](https://support.microsoft.com/en-us/windows) has a few extra steps if you need them.
