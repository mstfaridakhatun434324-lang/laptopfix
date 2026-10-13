---
title: "How to Turn Off Windows Tips and Suggestions on Windows 11"
slug: "how-to-turn-off-windows-tips-and-suggestions"
date: "2026-09-04"
categories: ["performance"]
tags: ["windows tips", "notifications", "windows 11", "privacy"]
description: "Annoyed by Windows tips, suggestions, and sync-provider notifications? Turn them all off in Settings with these quick steps."
thumbnail: "/images/thumbs/how-to-turn-off-windows-tips-and-suggestions.webp"
faqs:
  - q: "Where are tips and suggestions controlled in Windows 11?"
    a: "Most of them live under Settings, then System, then Notifications. Scroll to the bottom of the Notifications page to find toggles for suggested content in Settings, tips about Windows features, and the Windows welcome experience. Each toggle is independent, so you can silence the promotional suggestions while keeping useful alerts like low-battery warnings and security notifications fully enabled."
  - q: "Will turning off suggestions improve performance?"
    a: "Only marginally on modern hardware, but the real benefit is fewer interruptions and less background activity. The tips system periodically checks for new suggestion content, which uses small amounts of network and CPU. On low-end laptops with 4 GB of RAM, disabling suggestions alongside [visual effects](/articles/how-to-disable-visual-effects-on-windows-11/) and startup apps produces a noticeably snappier feel."
  - q: "What is the difference between tips and suggested content?"
    a: "Tips are the small pop-ups that explain Windows features, such as how to use Snap layouts. Suggested content refers to promotional cards inside the Settings app itself that recommend Microsoft services like OneDrive or Microsoft 365. The welcome experience is the full-screen tour shown after major updates. All three are controlled by separate toggles on the same Notifications settings page."
  - q: "Can I disable tips with Group Policy or the registry?"
    a: "Yes. On Windows 11 Pro, open gpedit.msc and navigate to Computer Configuration, Administrative Templates, Windows Components, Cloud Content, then enable Do not show Windows tips. On Home editions, the same effect comes from creating the DWORD DisableSoftLanding and setting it to 1 under the CloudContent registry key. The Settings toggles are simpler and sufficient for most home users."
---

Windows 11 loves to teach. Pop-up tips explain features you never asked about, the Settings app shows suggested cards for Microsoft services, the lock screen rotates fun facts, and after every major update you get the full welcome-experience tour. Individually these are harmless; together they are a steady drip of interruptions, and each one involves background tasks checking for fresh suggestion content.

On a performance level the impact is small, but it is not zero. The tips and suggestion engine runs scheduled checks, downloads content, and renders notifications, all of which consume CPU cycles, memory, and network on laptops that may already be stretched thin. More importantly for many users, these suggestions are promotional: they nudge you toward OneDrive, Microsoft 365, and Edge whether you want them or not.

Turning them off takes about two minutes and is completely safe. This guide covers every toggle: notification-level tips, suggested content in Settings, the post-update welcome experience, lock screen suggestions, and Start menu recommendations. Nothing here affects security alerts, app notifications, or Windows Update.

## Why this happens

- **Tips about Windows features enabled:** A dedicated toggle pushes how-to pop-ups about features like Snap layouts and widgets at unpredictable moments.
- **Suggested content in Settings:** Promotional cards inside the Settings app recommend Microsoft services and count as suggestions, not ads, so they slip past ad blockers.
- **Windows welcome experience:** After each feature update, Windows shows a full-screen tour that also re-enables some suggestion surfaces.
- **Lock screen fun facts and tips:** The Windows spotlight lock screen mixes pretty pictures with tips and occasional promotional links.
- **Start menu recommended section:** The Recommended area surfaces recently added apps and suggestions that many users mistake for ads.
- **Sync provider notifications:** File Explorer shows nudges to back up with OneDrive, driven by the sync-provider notification setting.
- **Tailored experiences diagnostic data:** With optional diagnostic data on, Microsoft personalizes tips and suggestions, which keeps the suggestion engine busier.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Turn off tips in Notifications settings

The main tips toggle lives at the bottom of the Notifications page. Switching it off stops the how-to pop-ups without touching your app notifications.

1. Press Win+I to open Settings, then select System.
2. Click Notifications in the right pane.
3. Scroll to the very bottom of the page.
4. Expand Additional settings if it is collapsed.
5. Uncheck Offer suggestions on how I can set up my device and Get tips and suggestions when I use Windows.

### Fix 2: Disable suggested content in the Settings app

Even with pop-up tips off, the Settings app itself can show suggestion cards. There is a separate toggle for those.

1. In Settings, stay on the System page and click Notifications.
2. Scroll to Additional settings at the bottom.
3. Uncheck Show the Windows welcome experience after updates.
4. Uncheck Suggest ways I can finish setting up my device.
5. Uncheck Get tips and suggestions when I use Windows if it is still on.

### Fix 3: Silence lock screen tips and fun facts

The spotlight lock screen is the prettiest suggestion surface in Windows. Switching to a plain picture background removes the tips and links.

1. Open Settings and go to Personalization.
2. Select Lock screen in the left pane.
3. Change the background dropdown from Windows spotlight to Picture.
4. Uncheck Get fun facts, tips, tricks, and more on your lock screen.
5. Pick any built-in picture or browse to one of your own.

### Fix 4: Turn off Start menu recommendations

The Recommended section of the Start menu shows recently added apps and occasional suggestions. You can shrink or hide most of it.

1. Open Settings and go to Personalization, then Start.
2. Turn off Show recently added apps.
3. Turn off Show recently opened items in Start, Jump Lists, and File Explorer.
4. Turn off Show recommendations for tips, shortcuts, new apps, and more.
5. Open the Start menu to confirm the Recommended section is now minimal.

### Fix 5: Disable OneDrive sync-provider nudges in File Explorer

Those backup-your-files banners inside File Explorer come from sync provider notifications. Microsoft documents File Explorer options in its [Windows support hub](https://support.microsoft.com/en-us/windows).

1. Open File Explorer and click the three-dot menu, then Options.
2. Switch to the View tab in Folder Options.
3. Scroll down and uncheck Show sync provider notifications.
4. Click Apply, then OK.
5. Restart File Explorer from Task Manager to see the change immediately.

### Fix 6: Turn off tailored experiences

Tailored experiences let Microsoft use your diagnostic data to personalize tips. Disabling it quiets the suggestion engine and slightly improves privacy.

1. Open Settings and go to Privacy and security.
2. Select Diagnostics and feedback.
3. Expand Tailored experiences.
4. Toggle Let Microsoft use your diagnostic data for tailored tips off.
5. While here, consider setting Diagnostic data to Required only.

### Fix 7: Block tips with the registry (Windows 11 Home)

Windows 11 Home lacks the Group Policy editor, but the same policies exist as registry values. Setting them silences tips, suggested content, and the welcome experience machine-wide. Export the key first as a backup so you can undo the change.

1. Press Win+R, type regedit, and press Enter.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent.
3. Create the CloudContent key if it does not exist.
4. Create a DWORD named DisableSoftLanding and set it to 1.
5. Create a DWORD named DisableWindowsConsumerFeatures and set it to 1.
6. Restart the laptop for the policies to take effect.

### Fix 8: Block tips with the registry (Windows 11 Home)

Windows 11 Home lacks the Group Policy editor, but the same policies exist as registry values. Setting them silences tips, suggested content, and the welcome experience machine-wide. Export the key first as a backup so you can undo the change.

1. Press Win+R, type regedit, and press Enter.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\CloudContent.
3. Create the CloudContent key if it does not exist.
4. Create a DWORD named DisableSoftLanding and set it to 1.
5. Create a DWORD named DisableWindowsConsumerFeatures and set it to 1.
6. Restart the laptop for the policies to take effect.

## Closing

With these toggles off, Windows 11 becomes noticeably quieter: no how-to pop-ups, no suggestion cards in Settings, no spotlight tips on the lock screen, and no OneDrive banners in File Explorer. None of this affects anything important, and every toggle can be reversed in seconds if you miss the guidance. If your laptop still feels sluggish after silencing suggestions, the next biggest wins are usually [disabling unnecessary visual effects](/articles/how-to-disable-visual-effects-on-windows-11/) and trimming startup programs. Microsoft documents these notification options in its [Windows support hub](https://support.microsoft.com/en-us/windows) if you ever want to reverse them. Microsoft documents these notification options in its [Windows support hub](https://support.microsoft.com/en-us/windows) if you ever want to reverse them. If suggestions are only part of what slows your boot, [trimming startup programs](/articles/how-to-disable-startup-apps-on-windows-11/) usually helps more.
