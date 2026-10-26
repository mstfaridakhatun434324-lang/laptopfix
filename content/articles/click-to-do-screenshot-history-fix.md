---
title: "Click to Do Screenshot History Not Working? How to Fix It on Windows 11"
slug: click-to-do-screenshot-history-fix
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, windows-11, screenshot-history, copilot-plus-pc, troubleshooting, privacy]
description: "Click to Do screenshot history not working on Windows 11? Learn why past screenshots vanish and restore history today with these proven Copilot+ PC fixes."
thumbnail: "/images/thumbs/click-to-do-screenshot-history-fix.webp"
faqs:
  - q: "Is Click to Do screenshot history the same as Recall?"
    a: >
      No, though they are related. Click to Do can act on a screenshot you capture now, while Recall keeps a searchable history of past activity. History features in Click to Do depend on related snapshot settings being enabled.
  - q: "Does screenshot history store images on my laptop?"
    a: >
      History and snapshot data are processed on your device on Copilot+ PCs. Still, you should review privacy settings and only enable history if you are comfortable with on-device storage of past screenshots.
  - q: "Why is history empty after I enabled it?"
    a: >
      History only records screenshots taken after you enable it. It cannot recover screenshots from before the setting was turned on, so an empty list right after setup is normal.
  - q: "Can I clear Click to Do screenshot history?"
    a: >
      Yes. Use the relevant history or snapshot settings to delete stored items, or turn history off entirely. Clearing history does not delete screenshots you saved manually to a folder.
---
You took a screenshot yesterday, acted on it with Click to Do, and now you cannot find it again. Or the history list opens but stays empty, shows only today's captures, or refuses to load older items at all. The feature works for new screenshots, yet its memory seems broken, and that gap is frustrating when you need to revisit something quickly.

Screenshot history depends on several quiet pieces working together: the capture tool, snapshot or history settings, storage permissions, and the AI components that index past captures. If any piece is paused, restricted, or damaged, new screenshots still work while history silently stops recording. That is why the symptom looks partial rather than total.

This guide separates those pieces and fixes them in order, starting with settings and ending with repairs. If charging or display features are also acting up, they may share the same underlying cause, so see the [USB-C charging fix](/articles/ai-laptop-usb-c-charging-fix/) and the [adaptive brightness fix](/articles/adaptive-brightness-not-working-ai/) for related checks. To compare with snapshot exports, read [how to export Recall snapshots](/articles/how-to-export-recall-snapshots/) once history is working again.

## Why this happens

- **History setting turned off:** Screenshot history only records after you enable it, so a disabled setting leaves the list empty even when captures work.
- **Privacy or snapshot setting paused:** Windows can pause snapshot collection after an update, a policy change, or a privacy prompt you dismissed.
- **Storage or cleanup removed items:** Disk cleanup, storage sense, or a full drive can delete older history entries automatically.
- **Wrong account or profile:** History is tied to your user profile, so a different account or a new profile shows an empty list.
- **Corrupt history database:** A crashed capture or failed update can damage the index, making old entries unreadable while new ones still save.
- **App permissions blocked:** If the capture tool lacks permission to store or access screenshots, history never gets written in the first place.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm history is enabled and check what should be there
Start by confirming the setting rather than assuming it. Open the Click to Do and related history settings, verify that history or snapshot collection is actually on, and check the retention period if one is shown. Then test with a fresh screenshot: capture something now, act on it, and see whether it appears in history. If the new item appears but old ones do not, the problem is retention or deletion, not recording.
1. Open Settings and search for Click to Do, then open its settings page.
2. Confirm that screenshot history or snapshot collection is turned on.
3. Check for any retention, filtering, or excluded-app options and note them.
4. Take a new screenshot and open it with Click to Do immediately.
5. Check history again to see whether the new capture was recorded.

### Fix 2: Review privacy settings and excluded apps
Windows lets you exclude apps and websites from history, and an exclusion you set months ago can hide exactly the screenshots you now need. Privacy prompts after updates can also pause collection without a clear warning. Reviewing these lists takes two minutes and often explains why history works for some apps but not others, which is a pattern a repair tool cannot fix.
1. Go to Settings, Privacy and security, and review snapshot and history options.
2. Look for excluded apps or websites and remove any you still want recorded.
3. Confirm that history collection is not paused for your current account.
4. If you use a work or school device, ask IT whether history is restricted.
5. Restart, take a test screenshot, and check whether history records it.

### Fix 3: Free storage and stop automatic cleanup deleting history
A nearly full drive is a common silent cause, because Windows prioritises system space over history and cleanup tools happily delete older entries. Storage Sense can be especially aggressive if it is set to remove temporary or unused files frequently. Freeing space and adjusting cleanup settings protects future history, though it cannot bring back entries that were already deleted.
1. Open Settings, System, Storage, and check how much free space remains.
2. Free at least several gigabytes by removing large unused files or apps.
3. Review Storage Sense settings and turn off aggressive automatic cleanup.
4. Check whether disk cleanup recently ran and removed history data.
5. Restart and capture a test screenshot to confirm recording resumes.

### Fix 4: Test in the correct profile and account
History belongs to one user profile, so signing in with a different account, a temporary profile, or a new local account will show an empty list even when the original history is intact. This step is a quick control test: if history appears under your usual account, the data was never lost, and the fix is simply using the right sign-in. If it is empty everywhere, move on to repairs.
1. Confirm you are signed in with the account that took the screenshots.
2. Check for a temporary profile warning after sign-in, which loses history.
3. Sign out and back in with your usual Microsoft account if needed.
4. Open history again and look for entries from before the problem began.
5. If a new profile was created by mistake, migrate back to the original profile.

### Fix 5: Repair the capture and history components
When settings, privacy, storage, and profile all check out, the history index itself may be damaged. System repairs fix the underlying capture components without deleting your saved screenshots, and they resolve the cases where new captures record but old ones refuse to load. Run these tools in order and restart between stages if Windows prompts you to do so.
1. Open Terminal as administrator from the Start menu right-click options.
2. Run sfc /scannow and wait for the scan to finish completely.
3. Then run DISM /Online /Cleanup-Image /RestoreHealth for the store.
4. Restart your laptop and test history with a fresh screenshot.
5. If old entries still fail to load, clear history once and rebuild it fresh.

### Fix 6: Reset history and rebuild it cleanly
As a last resort, clearing a corrupt history database and starting fresh is better than a permanently broken list. You will lose old entries, so export or save anything important first using the export guidance linked above. After the reset, history records cleanly again, and you can confirm the fix within minutes rather than wondering whether old data will ever return.
1. Save any screenshots you still need to a folder before clearing history.
2. Turn screenshot history off in Settings, then restart your laptop.
3. Turn history back on and confirm the setting stays enabled after restart.
4. Take several test screenshots across different apps over a few minutes.
5. Check history after each capture to confirm entries appear in order.
6. For current update guidance, see the official [Windows support pages](https://support.microsoft.com/en-us/windows) and the [Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11) if an update is offered.

## Closing

Screenshot history fails quietly because it depends on settings, privacy, storage, and an index that all have to agree. Working through them in order tells you whether history was never recorded, was deleted, or is simply hidden in another profile. Once recording resumes, protect it by keeping storage free and checking privacy settings after each major Windows update.
