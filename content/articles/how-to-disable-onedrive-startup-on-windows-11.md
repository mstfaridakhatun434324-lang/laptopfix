---
title: "How to Disable OneDrive Startup on Windows 11"
slug: "how-to-disable-onedrive-startup-on-windows-11"
date: 2026-09-15
categories: ["performance"]
tags: ["onedrive", "startup programs", "windows 11", "boot speed", "disable onedrive"]
description: "OneDrive slowing your Windows 11 boot? Here are four reliable ways to stop OneDrive from starting with Windows, from a simple toggle to Group Policy."
thumbnail: "/images/thumbs/how-to-disable-onedrive-startup-on-windows-11.webp"
faqs:
  - q: "Does disabling OneDrive startup delete my files?"
    a: "No. Disabling OneDrive at startup only stops the app from launching when Windows boots — it does not delete anything from your PC or from the cloud. Your files stay exactly where they are, and you can open OneDrive manually any time you want to sync. If you later unlink the PC or uninstall OneDrive, local copies in the OneDrive folder remain on disk unless you delete them yourself."
  - q: "Why does OneDrive start automatically on Windows 11?"
    a: "Microsoft bundles OneDrive with Windows 11 and registers it as a startup item during setup, because the company wants files backed up to the cloud by default. On many laptops the installer also enables folder backup for Desktop, Documents, and Pictures without asking clearly. That is why OneDrive appears in Task Manager's Startup apps list even if you never remember turning it on."
  - q: "Can I still use OneDrive if I disable it at startup?"
    a: "Yes, absolutely. Disabling the startup entry only prevents the automatic launch at boot. You can still open OneDrive from the Start menu whenever you need to sync files, and it will run normally until you close it or shut down. This on-demand approach is ideal if you sync occasionally but do not want OneDrive consuming RAM and CPU on every single boot."
  - q: "What is the difference between disabling startup and unlinking OneDrive?"
    a: "Disabling startup keeps your account signed in but stops the app launching at boot — sync resumes the moment you open it manually. Unlinking goes further: it signs the PC out of OneDrive entirely, so nothing syncs until you sign in again. Unlink if you want OneDrive completely dormant; just disable the startup entry if you still sync files a few times a week."
---
OneDrive launches with Windows 11 on most laptops whether you asked for it or not. The moment you sign in, it starts syncing, checking files, and holding several hundred megabytes of RAM — all before you have even opened your first app. On older laptops or machines with 8 GB of memory, that background activity can add ten to twenty seconds to an already slow boot.

Microsoft's reasoning is simple: automatic backup protects your files. But if you already back up elsewhere, rarely touch the cloud, or just want a leaner startup, there is no reason to let OneDrive run on every boot. Disabling its startup entry is safe, reversible, and takes about a minute.

There are four ways to do it, from a one-click toggle to enterprise-grade policy settings. Start with the simplest and only go deeper if OneDrive keeps resurrecting itself — which, on some Windows 11 builds, it stubbornly tries to do. For a broader cleanup, see our guide on [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) in Windows 11.

## Why this happens

- **OneDrive registers itself at startup during Windows setup:** the installer adds a startup entry by default, so it launches on every boot unless you intervene.

- **Folder backup silently enabled:** Desktop, Documents, and Pictures backup means OneDrive scans thousands of files at every sign-in.

- **Files On-Demand placeholders:** placeholder files trigger sync checks and thumbnail generation each time Explorer touches them.

- **Office upload center integration:** Office apps hand off files to OneDrive's sync engine even when you save locally.

- **Large or frequently changing folders:** developer folders, photo libraries, or game saves force constant re-scanning at startup.

- **Multiple signed-in accounts:** personal and work accounts each spawn sync activity, roughly doubling the startup cost.

- **Corrupted sync cache:** a damaged local sync database makes OneDrive re-scan everything from scratch on every boot instead of resuming.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable OneDrive in Task Manager's Startup apps

This is the fastest method and works on every Windows 11 edition. It stops the automatic launch but leaves your account signed in, so manual syncing still works whenever you open the app.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Click Startup apps in the left sidebar.
3. Find Microsoft OneDrive in the list and check its Startup impact column.
4. Right-click Microsoft OneDrive and choose Disable.
5. Restart your laptop and confirm OneDrive no longer appears in the system tray at boot.

### Fix 2: Turn off Start OneDrive automatically in its settings

OneDrive has its own internal autostart switch that can re-enable the Task Manager entry after updates. Turning it off inside the app's settings closes that loophole, and Microsoft documents these settings on its [Windows support pages](https://support.microsoft.com/en-us/windows).

1. Click the OneDrive cloud icon in the system tray (click the up arrow if it is hidden).
2. Click the gear icon and choose Settings.
3. On the Settings tab, uncheck Start OneDrive automatically when I sign in to Windows.
4. Click OK, then quit OneDrive completely from the tray icon menu.
5. Restart and verify both the Task Manager entry and this setting stay off.

### Fix 3: Unlink the PC if you barely use OneDrive

If you open OneDrive less than once a month, unlinking is cleaner than merely disabling startup. It signs the PC out entirely, so no background sync, no tray icon, and no RAM usage at all — while your cloud files stay untouched.

1. Open OneDrive Settings from the tray icon as in Fix 2.
2. Go to the Account tab and click Unlink this PC.
3. Confirm the unlink; the tray icon will disappear within seconds.
4. Your local OneDrive folder remains on disk — delete it manually only if you are sure you have copies elsewhere.
5. To use OneDrive again later, just launch it from Start and sign back in.

### Fix 4: Block it with Group Policy (Pro and Enterprise)

On Windows 11 Pro or Enterprise, Group Policy can prevent OneDrive from running at all, which also stops feature updates from silently re-enabling it. This is the method IT departments use, and it is the most permanent option for a personal Pro machine too.

1. Press Win + R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration > Administrative Templates > Windows Components > OneDrive.
3. Double-click Prevent the usage of OneDrive for file storage and set it to Enabled.
4. Click OK, then open Command Prompt and run gpupdate /force.
5. Restart — OneDrive will no longer launch, and its Settings pages become unavailable until you revert the policy.

### Fix 5: Remove the startup entry via the Registry (Home edition)

Windows 11 Home has no Group Policy editor, but the same result is possible through the registry. This is safe if you follow the path exactly and only delete the OneDrive value — nothing else.

1. Press Win + R, type regedit, and press Enter (approve the UAC prompt).
2. Navigate to HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run.
3. In the right pane, right-click the OneDrive value and choose Delete.
4. Also check HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run for a OneDrive entry and delete it there too.
5. Close the editor and restart to confirm OneDrive stays off.

### Fix 6: Stop the resurrection: check Task Scheduler and updates

Some users find OneDrive re-enables itself after a Windows update. That happens because update and maintenance tasks can restore the startup entry. A quick audit of scheduled tasks closes the last back door.

1. Open Task Scheduler from the Start menu.
2. In the left pane go to Task Scheduler Library and look for OneDrive-related tasks.
3. Right-click any OneDrive Standalone Update or maintenance task and choose Disable.
4. After each monthly Windows update, glance at Task Manager's Startup apps to confirm OneDrive is still disabled.
5. If you also want Teams gone from startup, the same Task Manager method in our [Teams autostart guide](/articles/how-to-fix-teams-autostart-slowing-laptop-in-windows-11-24h2/) applies.

## Closing

Disabling OneDrive at startup is one of the simplest boot-speed wins on Windows 11: one toggle, a minute of your time, and several hundred megabytes of RAM back on every boot. Keep it disabled if you sync rarely, or unlink entirely if you have moved on to another backup solution — either way, your files stay safe and the choice remains reversible.
