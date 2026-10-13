---
title: "How to Disable OneDrive Startup on Windows 10"
slug: how-to-disable-onedrive-startup-on-windows-10
date: 2026-09-10
categories: ["performance"]
tags: ["onedrive", "startup", "windows 10", "disable autostart", "boot"]
description: "Stop OneDrive from launching at every Windows 10 boot. Learn all the methods — settings, Task Manager, and registry — and when to just uninstall it."
thumbnail: "/images/thumbs/how-to-disable-onedrive-startup-on-windows-10.webp"
faqs:
  - q: "Will disabling OneDrive startup delete my files?"
    a: "No — disabling startup only stops OneDrive from launching at boot. All your local files stay exactly where they are, and your cloud files remain in OneDrive online. The app still works perfectly when you open it manually. Disabling startup, unlinking the PC, and uninstalling all preserve your files; only deleting files yourself (or emptying the OneDrive recycle bin) removes data."
  - q: "Why does OneDrive keep coming back after I disable it?"
    a: "OneDrive has redundant autostart paths: the in-app 'Start OneDrive automatically' setting, a Task Manager startup entry, and registry Run keys. Disabling only one lets the others restore it — and Windows 10 feature updates sometimes re-enable OneDrive startup as part of the upgrade. You need to disable all paths, and re-check after major updates."
  - q: "What's the difference between disabling startup and unlinking OneDrive?"
    a: "Disabling startup keeps OneDrive signed in and configured but stops it launching at boot — open it manually and syncing resumes instantly. Unlinking signs the PC out of the account entirely, requiring re-sign-in and folder re-selection before syncing works again. Disable startup for temporary relief; unlink when reconfiguring; uninstall when you're done with OneDrive."
  - q: "Can I remove OneDrive from Windows 10 completely?"
    a: "Yes — OneDrive is uninstallable on Windows 10 via Settings > Apps > Apps & features > Microsoft OneDrive > Uninstall. Your local OneDrive folder and files remain on disk; only the sync app is removed. If you change your mind, reinstall it from Microsoft's website. Some managed PCs block uninstallation via policy — in that case, disabling all startup paths is the practical equivalent."
---

OneDrive on Windows 10 has a habit: it starts with every boot, syncs in the background, and holds onto memory — whether you use it or not. For many people it's pure overhead: they never opened it deliberately, yet there it is in Task Manager at every login. Stopping it is easy; keeping it stopped requires knowing all its autostart paths.

This guide covers every method in order of simplicity, plus how to make the disable survive updates. If you're on Windows 11 instead, the steps are nearly identical — and for OneDrive's CPU issues generally, see [fixing OneDrive sync high CPU](/articles/how-to-fix-onedrive-sync-high-cpu-step-by-step/).

## Why this happens

- **In-app auto-start setting**: OneDrive's own "start automatically" preference, on by default.
- **Task Manager startup entry**: A separate autostart registration Windows manages.
- **Registry Run keys**: The persistence layer behind the other two.
- **Windows 10 feature updates**: Upgrades re-enable OneDrive startup as part of "getting you set up."
- **First-run setup prompts**: Windows nags you to configure OneDrive, which enables startup as a side effect.
- **Office integration**: Installing Microsoft 365 can re-register OneDrive startup.
- **Policy on managed PCs**: Organizations may enforce OneDrive via Group Policy.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off "Start OneDrive automatically"

The in-app setting — always first.

1. Click the **OneDrive cloud icon** in the notification area (click **Show hidden icons** ^ if needed).
2. Click the gear icon > **Settings** > on the **Settings** tab, uncheck **Start OneDrive automatically when I sign in to Windows**.
3. Click **OK**, then right-click the cloud icon > **Quit OneDrive** to stop the current session.
4. Verify in Task Manager (**Ctrl+Shift+Esc** > **Processes**) that no OneDrive.exe remains.
5. Reboot and check whether OneDrive returns — if it does, a deeper mechanism is active (continue below). This setting alone works on about half of systems.

### Fix 2: Disable the Task Manager startup entry

The layer the in-app setting sometimes misses.

1. Open **Task Manager** > **Startup** tab (on Windows 10 it's a top-level tab).
2. Find **Microsoft OneDrive**, check its **Status** — if **Enabled**, right-click > **Disable**.
3. Note the **Startup impact** — OneDrive is usually Medium or High, confirming real boot savings.
4. Reboot and verify — the combination of Fix 1 + Fix 2 holds on most consumer systems.
5. If OneDrive still appears, the registry layer (Fix 3) or an update (Fix 5) is restoring it.

### Fix 3: Remove the registry Run entry

The persistence that survives the other disables.

1. Press **Win+R**, type `regedit`, navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`.
2. Find the **OneDrive** value (data points to `OneDrive.exe /background`) — right-click > **Delete**.
3. Also check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` for a machine-wide entry (rare, but possible).
4. Check the **StartupApproved** key at `HKCU\...\Explorer\StartupApproved\Run` — delete any stale OneDrive entry so Windows doesn't "remember" it as approved.
5. Reboot and verify across two or three boots — registry-level removal is what finally breaks the resurrection cycle. Our [startup programs guide](/articles/how-to-disable-startup-programs-windows-11/) explains the general technique (same on Windows 10).

### Fix 4: Stop the nagging setup prompts

Windows 10 loves re-introducing OneDrive.

1. When Windows shows **"Set up OneDrive"** prompts after updates, don't click through them blindly — completing setup re-enables startup.
2. Dismiss the prompt with **"Not now"** or close it — declining doesn't delete anything.
3. In **Settings** > **System** > **Notifications & actions**, you can disable **"Show me the Windows welcome experience"** and **"Suggest ways I can finish setting up my device"** to reduce the nagging.
4. If OneDrive appears in File Explorer's navigation pane and bothers you, that's cosmetic — the registry tweak to hide it is separate from startup and optional.
5. After every Windows 10 feature update, re-check Fixes 1–3 — updates are the #1 resurrection vector, documented in Microsoft's [Windows support](https://support.microsoft.com/en-us/windows) update notes.

### Fix 5: Handle the Office 365 re-registration

A sneaky resurrection source.

1. If you install or update **Microsoft 365 / Office**, check OneDrive startup afterward — Office setup sometimes re-registers it.
2. The mechanism is usually the in-app setting (Fix 1) being reset — re-apply it and verify.
3. In Office apps, check **File** > **Options** > **Save** — the **"Save to Computer by default"** option reduces OneDrive entanglement even if you keep the app.
4. You don't need to unlink OneDrive to stop the Office prompts — just keep startup disabled and dismiss setup offers.
5. If your organization deploys Office with OneDrive integration enforced, talk to IT — policy beats local settings every time.

### Fix 6: Uninstall OneDrive (the permanent option)

When you're sure you don't want it.

1. Go to **Settings** > **Apps** > **Apps & features**, find **Microsoft OneDrive**, click **Uninstall**.
2. Your files stay: the local OneDrive folder remains on disk with everything in it; cloud files stay in the cloud.
3. Verify the cloud icon is gone from the notification area and no OneDrive.exe runs at boot.
4. If you ever need it back, download the installer from Microsoft's official OneDrive page — reinstalling takes two minutes.
5. Note: on some Windows 10 builds, major updates may reinstall OneDrive — if it reappears after an update, uninstall again; it takes 30 seconds. For broader boot-speed work, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) — the principles apply to Windows 10 too.

### Fix 7: Verify the full boot improvement

Confirm the payoff and lock it in.

1. Time boot-to-usable-desktop before and after — OneDrive typically costs 10–30 seconds on HDD systems, less on SSDs, plus its ongoing background RAM.
2. Check **Task Manager** > **Startup** — with OneDrive gone, the next-heaviest entries become your new targets.
3. Monitor for a week: if OneDrive reappears, note what preceded it (update? Office install?) — that identifies your personal resurrection trigger.
4. Keep a checklist of Fixes 1–3 — re-applying after updates takes two minutes once you know the drill.
5. Consider whether other cloud clients (Dropbox, Google Drive) deserve the same treatment — the same layered-disable technique works for all of them.

## Closing

Disabling OneDrive startup on Windows 10 is a three-layer job: the in-app setting, the Task Manager entry, and the registry key — applied in that order, verified across reboots, and re-checked after updates. Do all three and OneDrive stays off until you summon it; skip one and it'll be back by Monday. And if you never use it at all, uninstalling is the cleanest two minutes you'll spend this week.
