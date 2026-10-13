---
title: "Stop OneDrive Launching at Startup in Windows 11 24H2"
slug: how-to-disable-onedrive-startup-in-windows-11-24h2
date: 2026-09-24
categories: ["performance"]
tags: ["onedrive startup", "disable onedrive", "windows 11 24h2", "startup programs"]
description: "OneDrive slowing your Windows 11 24H2 boot? Learn how to stop OneDrive from starting with Windows — via Settings, Task Manager, or full unlink — without losing your files."
thumbnail: "/images/thumbs/how-to-disable-onedrive-startup-in-windows-11-24h2.webp"
faqs:
  - q: "Will disabling OneDrive startup delete my files?"
    a: "No. Stopping OneDrive from launching at startup only prevents the sync client from running — your files stay exactly where they are, both locally and in the cloud. Files already synced remain in your local OneDrive folder and accessible in File Explorer. Nothing is deleted from your PC or from OneDrive online by disabling startup."
  - q: "What's the difference between disabling startup and unlinking OneDrive?"
    a: "Disabling startup keeps OneDrive installed and your account linked; you can launch it manually anytime and syncing resumes. Unlinking signs the PC out of OneDrive entirely — sync stops completely until you sign in again. Disabling startup is the lighter touch and the right choice if you use OneDrive occasionally."
  - q: "Why does OneDrive keep re-enabling itself at startup?"
    a: "Usually because of a Windows update resetting startup preferences, or because the OneDrive setting Start OneDrive automatically when I sign in to Windows got re-checked. In managed or work PCs, an IT policy may also force it on. After major Windows updates, it's worth rechecking the OneDrive setting — updates are the most common cause of it coming back."
  - q: "Does OneDrive at startup actually slow down my laptop?"
    a: "Yes, measurably on many systems. At login, OneDrive scans your synced folders for changes, which means disk I/O and CPU during the exact window when everything else is also loading. On laptops with large synced libraries or slower drives, this can add 30 seconds or more to a usable desktop. Disabling it is one of the highest-impact startup trims you can make."
---

OneDrive is useful — until it's the reason your laptop takes forever to become usable after login. On Windows 11 24H2, OneDrive starts with Windows by default, and the moment you sign in it begins scanning synced folders, checking for changes, and occasionally downloading files. That's disk and CPU activity stacked on top of everything else loading at startup.

The fix takes about a minute, and you have options depending on how much OneDrive you want gone: stop it launching at boot but keep it available, unlink the PC from your account, or remove it entirely. None of these delete your files. If startup speed is the broader goal, pair this with [disabling other startup programs](/articles/how-to-disable-startup-programs-windows-11/); if OneDrive is also eating CPU while it runs, [OneDrive high CPU after the Windows 11 update](/articles/how-to-fix-onedrive-high-cpu-usage-after-windows-11-update/) tackles that side.

Start with the simplest method — the in-app toggle — and only go deeper if OneDrive keeps coming back.

## Why this happens

- **Default auto-start setting**: OneDrive's installer enables Start OneDrive automatically when I sign in to Windows, so it launches on every boot unless you change it.
- **Large synced libraries**: The more files OneDrive tracks, the longer its startup scan takes — tens of thousands of files means serious disk I/O at login.
- **Files On-Demand re-checks**: With Files On-Demand, OneDrive verifies placeholder states at startup, adding overhead even when nothing needs downloading.
- **Update resets**: Windows feature updates and OneDrive client updates can silently re-enable the auto-start toggle you turned off.
- **Work or school policy**: On managed devices, IT policies can force OneDrive to start and even prevent you from disabling it.
- **Multiple accounts syncing**: Personal plus work/school accounts double the startup workload — two sync engines scanning at once.
- **Slow drive amplifying the cost**: On HDDs or nearly-full SSDs, OneDrive's startup scan competes with everything else for disk access, multiplying the delay.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off auto-start in OneDrive settings

The official toggle — quick, clean, and the right first move for most people.

1. Click the OneDrive cloud icon in the system tray (click Show hidden icons if needed).
2. Click the gear icon and choose Settings.
3. Under the Settings tab, uncheck Start OneDrive automatically when I sign in to Windows.
4. Click OK, then restart to confirm OneDrive no longer launches at login.

### Fix 2: Disable it in Task Manager's Startup apps

A second switch that catches OneDrive even if its own setting misbehaves.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Go to the Startup apps tab and find Microsoft OneDrive.
3. Right-click it and choose Disable.
4. The Status column should now read Disabled — this persists independently of OneDrive's own toggle.

### Fix 3: Unlink the PC from OneDrive

If you barely use OneDrive, unlinking stops all syncing without uninstalling anything. Your files stay put.

1. Open OneDrive settings via the tray icon, gear icon, Settings.
2. Go to the Account tab and click Unlink this PC.
3. Confirm. OneDrive signs out and stops syncing; the local OneDrive folder remains with your files.
4. You can sign back in anytime by launching OneDrive from the Start menu.

### Fix 4: Uninstall OneDrive entirely

For users who never touch OneDrive, removing the client frees the most resources. Fully reversible via the Microsoft Store.

1. Open Settings, Apps, Installed apps.
2. Find Microsoft OneDrive, click the three dots, and choose Uninstall.
3. Confirm the uninstall. Your synced files remain in the local OneDrive folder.
4. To reinstall later, get it from the Microsoft Store or [Microsoft's Windows support site](https://support.microsoft.com/en-us/windows).

### Fix 5: Use Group Policy to block it (Pro editions)

On Windows 11 Pro, a policy prevents OneDrive from running at all — useful if updates keep re-enabling it.

1. Press Win + R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration, Administrative Templates, Windows Components, OneDrive.
3. Open Prevent the usage of OneDrive for file storage and set it to Enabled.
4. Restart. OneDrive will no longer launch, and the policy survives updates.

### Fix 6: Stop it re-enabling after updates

Windows updates are the main reason OneDrive startup comes back. A quick post-update routine keeps it off.

1. After each feature update, reopen OneDrive settings and verify the auto-start toggle is still off.
2. Check Task Manager's Startup apps tab for a re-enabled OneDrive entry.
3. If you're on Pro, the Group Policy above is the durable fix — policies persist where toggles don't.
4. Consider pausing sync during the first hour after a big update to avoid sync storms.

### Fix 7: Trim what OneDrive syncs to speed up manual launches

Even with auto-start off, a leaner sync set means faster launches when you do open OneDrive.

1. Open OneDrive settings, Account tab, and click Choose folders.
2. Uncheck folders you rarely need on this laptop — they stay in the cloud, accessible via browser.
3. Keep Files On-Demand enabled so remaining files don't consume local disk.
4. Fewer tracked files means every future OneDrive launch is quicker and lighter.

### Fix 8: Block OneDrive via Registry (Home edition)

If you're on Windows 11 Home and OneDrive keeps resurrecting after updates, the registry equivalent of the Group Policy gives you a durable block. This is the heavy hammer — use it only if the gentler toggles above failed.

1. Press Win + R, type regedit, and press Enter. Back up first with File, Export.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\OneDrive.
3. Create the OneDrive key if it doesn't exist, then add a DWORD (32-bit) value named DisableFileSyncNGSC and set it to 1.
4. Restart your laptop. OneDrive will no longer launch, and the setting survives feature updates.
5. To reverse it later, delete the value or set it to 0 and restart.

## Closing

OneDrive at startup is a convenience you probably didn't choose — and on Windows 11 24H2 it's one of the easiest boot-time wins available. The in-app toggle plus the Task Manager disable covers nearly everyone; unlinking or the Group Policy handles the stubborn cases. Your files are safe either way, and OneDrive is one manual launch away whenever you actually want it.
