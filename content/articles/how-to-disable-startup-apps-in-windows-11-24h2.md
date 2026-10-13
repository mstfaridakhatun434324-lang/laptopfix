---
title: "Disable Startup Apps in Windows 11 24H2: The Full Guide"
slug: how-to-disable-startup-apps-in-windows-11-24h2
date: 2026-09-26
categories: ["performance"]
tags: ["startup apps", "disable startup", "windows 11 24h2", "boot speed", "task manager"]
description: "Too many apps launching at boot on Windows 11 24H2? Learn every method to disable startup apps — Task Manager, Settings, folders, and registry."
thumbnail: "/images/thumbs/how-to-disable-startup-apps-in-windows-11-24h2.webp"
faqs:
  - q: "Is it safe to disable all startup apps?"
    a: "Almost. Disabling a startup entry never uninstalls anything — the app still works when you launch it manually. The only entries worth keeping enabled are security software and hardware utilities (audio, touchpad). Everything else — updaters, chat clients, launchers, vendor tools — is safe to disable; the worst case is you launch the app yourself the first time you need it."
  - q: "Why does a disabled app keep starting anyway?"
    a: "Because it launches from a place you did not check. The four startup locations (Task Manager/Settings, Startup folders, registry Run keys, scheduled tasks) are independent — disabling in one does not affect the others. Scheduled tasks with 'At log on' triggers are the most common hidden culprit, followed by auto-start services. Work through all four methods in this guide to catch every path."
  - q: "What is Startup impact in Task Manager?"
    a: "Startup impact (Low/Medium/High/Not measured) estimates how much each app slows your boot, based on its CPU and disk usage during startup. It is a useful prioritization guide: disabling High-impact apps you do not need gives the biggest boot-time return. 'Not measured' just means Windows has not observed enough startups yet — it will categorize the app after a few more boots."
  - q: "Should I use a third-party startup manager?"
    a: "Usually unnecessary. Windows 11's built-in tools — Task Manager, Settings, Task Scheduler, and services.msc — cover every startup location a third-party tool would. Autoruns from Microsoft Sysinternals is the exception: it is the gold standard for seeing absolutely everything, including drivers and Explorer add-ons, and is worth using for the truly stubborn cases."
---

Every program that launches at boot steals a slice of your startup: CPU cycles, disk reads, and memory that should go to getting you to a usable desktop. Most laptops accumulate dozens of startup entries — updaters, chat clients, game launchers, vendor utilities — and each one was added silently by an installer that assumed you wanted it running forever. Each one felt reasonable to its installer; together they are a traffic jam.

Windows 11 24H2 gives you four different control points for startup apps, and they do not all show the same list: Task Manager's Startup apps tab, the Settings Startup page, the Startup folders, and the registry Run keys. An app disabled in one place can still launch from another, which is why 'I disabled it but it still starts' is such a common complaint. Four control points, four chances for an app to slip through.

This guide covers all four methods in order, plus how to measure the impact and handle the stubborn cases — scheduled tasks and services that behave like startup apps. For the broader boot-speed picture, see [slow boot on Dell](/articles/how-to-fix-windows-11-slow-boot-on-dell-laptop/). By the end, nothing will start without your knowledge.

## Why this happens

- **Installer-added startup entries**: most apps add themselves to startup during installation without asking clearly.
- **Update-resurrected entries**: Windows updates can re-enable entries you previously disabled.
- **Multiple startup locations**: an app disabled in Task Manager may still launch from a Run key or scheduled task.
- **Vendor utilities**: laptop makers preload utilities that all want to run at boot.
- **Chat and launcher apps**: Teams, Discord, Steam, and similar apps default to starting with Windows.
- **Background updaters**: Adobe, Google, and vendor updaters each take a startup slot.
- **Services misbehaving as startup**: some apps install services that launch their UI at boot regardless of startup settings.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Disable in Task Manager (primary method)

The Startup apps tab is the main switchboard — start here. When in doubt, disable it; you can re-enable in seconds.

1. Press Ctrl + Shift + Esc, then go to the Startup apps tab.
2. Check the Startup impact column and disable everything marked High that you do not need immediately.
3. Keep antivirus and essential drivers enabled; disable updaters, chat apps, and launchers.
4. Use the Startup impact column to prioritize — disable High impact entries first.

### Fix 2: Use the Settings Startup page

Settings shows the same entries with friendlier descriptions — useful for identifying unknowns. The Settings page is friendlier but shows less detail than Task Manager.

1. Open Settings > Apps > Startup.
2. Toggle off anything you do not recognize or do not need at boot.
3. Cross-check with Task Manager; the lists should match — investigate any discrepancy.

### Fix 3: Clean the Startup folders

The old Startup folders still work and bypass the other toggles. Shortcuts here are easy to miss because nothing lists them centrally. Some installers recreate these shortcuts on update, so recheck after major app updates.

1. Press Windows key + R, type shell:startup, and press Enter.
2. Delete shortcuts for apps you do not want launching.
3. Repeat with shell:common startup for the all-users folder (requires admin).

### Fix 4: Check the registry Run keys

Some apps hide only here. This is the deepest startup location. Export the key before deleting anything, for a one-click restore.

1. Open regedit and check HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run.
2. Also check the same path under HKEY_LOCAL_MACHINE.
3. Delete values for apps you have disabled elsewhere — but research unknown entries first.

### Fix 5: Hunt scheduled-task launchers

The stubborn 'still starts' cases are usually scheduled tasks, not startup entries. Tasks can also trigger on idle or schedule, mimicking startup behavior.

1. Open Task Scheduler and browse the Task Scheduler Library.
2. Look for tasks with 'At log on' triggers matching the resurrecting app.
3. Right-click and Disable the task; do not delete it, so you can re-enable if needed.
4. Pay special attention to tasks from updaters and chat apps, the most common resurrectors.

### Fix 6: Convert services to manual

Apps that install auto-start services relaunch themselves regardless of startup toggles. Manual services still start on demand; nothing breaks. Note the service's original setting before changing it, in case you need to revert.

1. Open services.msc and sort by Startup Type.
2. Find the app's service, set it to Manual instead of Automatic.
3. Test a reboot; the app should stay dormant until you launch it. More: [Microsoft's Windows help](https://support.microsoft.com/en-us/windows).

### Fix 7: Measure the improvement

Verify the cleanup actually shortened your boot. Put a quarterly reminder in your calendar; future you will be grateful.

1. Reboot and time from power button to responsive desktop.
2. Compare against your before measurement — expect 30–60% improvement on cluttered systems.
3. Revisit quarterly; installers will keep adding entries back.
4. Compare cold boot versus restart times; fast startup makes them behave differently.

### Fix 8: Audit everything with Autoruns

Microsoft's free Autoruns utility shows every single auto-start location in Windows — far beyond the four covered above, including Explorer add-ons, drivers, codecs, and scheduled tasks. When an app survives all four standard methods, Autoruns will show you the fifth location it was hiding in.

1. Download Autoruns from Microsoft Sysinternals and run it as administrator.
2. Wait for the scan to complete, then check the Logon tab.
3. Untick entries to disable them (unticking is reversible; deleting is not).
4. Use the Everything tab and its search to hunt a specific resurrecting app.

## Closing

Startup apps are death by a thousand cuts — each one small, together brutal. Work through all four control points, hunt the scheduled tasks behind the stubborn ones, and measure your boot before and after. A quarterly ten-minute cleanup keeps the list — and your boot time — under control permanently. Ten minutes, four times a year, and boot stays fast. For the companion overview, see [disable startup programs](/articles/how-to-disable-startup-programs-windows-11/).
