---
title: "Click to Do Open With App Not Working? Fix It on Your Copilot+ PC"
slug: click-to-do-open-with-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags: [click-to-do, open-with-app, copilot-plus-pc, windows-11, troubleshooting, default-apps]
description: "Click to Do open with app not working on your Copilot+ PC? Fix the broken app launch, default apps, and settings with this complete step-by-step guide."
thumbnail: "/images/thumbs/click-to-do-open-with-not-working.webp"
faqs:
  - q: "Why does Open With show no apps in Click to Do?"
    a: >
      Click to Do only lists apps that Windows knows can handle the selected content type. If no app is registered for that type, or the default-app associations are broken, the list comes up empty even though the apps themselves are installed and working.
  - q: "Can a missing default browser break Open With?"
    a: >
      Yes. Many Click to Do actions hand a link or a search to the default browser, so a missing or broken default browser can make the whole hand-off fail. Setting a working default browser often restores several Click to Do actions at once.
  - q: "Does Open With work for both text and images?"
    a: >
      It depends on the content. Text selections offer apps that handle text or links, while images offer apps that handle pictures. An app that appears for one type will not necessarily appear for the other, which is normal behaviour rather than a fault.
  - q: "Will reinstalling the target app fix Open With?"
    a: >
      It can, if the app's own registration is broken. Reinstalling re-registers the app with Windows, which restores its entry in the Open With list. Try default-app and Click to Do repairs first, since they are faster and safer.
---

You select an email address, a link, or a file reference, open Click to Do, choose Open With — and nothing launches, or the app list is empty, or the wrong app opens every time. The selection itself is fine, the menu appears, but the final hand-off to another program collapses.

It does not depend on the language model; it depends on Windows knowing which apps handle which content, on those apps being registered correctly, and on the default-app associations that route the hand-off. A broken association, a missing default browser, or a corrupted app registration can all break it while Summarize and Rewrite keep working perfectly.

This guide follows the hand-off itself: from the selection type, through the default apps, to the target app's registration. If a wider backup or sign-in problem is complicating matters, check [backup software not working on ARM](/articles/backup-software-arm-not-working/) and [Windows Hello fingerprint setup failed](/articles/windows-hello-fingerprint-setup-failed/) for those separate faults.

## Why this happens

- **No app is registered for the content type:** Click to Do lists only apps Windows knows can handle the selection. If none is registered the list is empty by design.
- **Default-app associations are broken:** A corrupted association sends the hand-off nowhere, or to the wrong app, even when the right app is installed and healthy.
- **Default browser is missing or broken:** Many Open With actions route through the browser. A missing or damaged default browser breaks the hand-off for links and searches.
- **Target app registration is damaged:** An app that was partially updated or moved can lose its Windows registration. It still launches from its own icon, but Click to Do can no longer see it.
- **Selection type does not match the app:** An app that handles images will not appear for a text selection, and vice versa. The mismatch looks like a missing app when it is really a content-type rule.
- **Click to Do feature state is stale:** A half-registered feature can show a stale or empty app list. The menu opens, but the hand-off data behind it is out of date.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test Open With with a simple link in Edge

Start with the easiest possible hand-off, because a test with a complicated selection hides the real fault. A plain web link in Edge is the best-understood content type in Windows, and the browser is the most reliably registered target.

1. Open Edge and select a plain web address in the address bar or on a page.
2. Press Win + Q or Win + Click on the selection to open Click to Do.
3. Choose the Open With action and look at the app list carefully.
4. Try opening the link in the browser from the list and note the result.

### Fix 2: Repair the default-app associations

Default-app associations are the routing table for every Open With hand-off, and they are surprisingly easy to damage: an uninstalled app, a botched update, or a changed default can leave a content type pointing at nothing. Resetting the association for the affected type, or setting a known-good default, restores the route without touching any app's data.

1. Open Settings, then Apps, then Default apps.
2. Find the file or link type you were trying to open, such as a web link.
3. Confirm a sensible, installed app is set as the default for that type.
4. If the entry looks wrong or empty, set it explicitly to your preferred app.
5. Retest Open With from Click to Do with the same kind of selection.

### Fix 3: Set and verify a working default browser

The browser is the fallback target for a large share of Click to Do actions, so a missing or broken default browser has an outsized effect. Even if you never open links from Click to Do, a damaged browser default can make the hand-off code fail before it reaches your intended app.

1. Open Settings, then Apps, then Default apps, and select your browser.
2. Set it as the default for web links and common web file types.
3. Launch the browser directly to confirm it opens without errors.
4. Return to Click to Do and test Open With on a plain web link.
5. If the browser hand-off works, test your original selection type again.

### Fix 4: Toggle Click to Do to refresh its app list

Click to Do caches the list of apps it can hand off to, and a stale cache shows apps you removed months ago while hiding apps you installed yesterday. Toggling the feature forces that list to rebuild from the current app registrations, which is exactly what a stale-list failure needs.

1. Open Settings, then Privacy and security, and select Click to Do.
2. Switch the main toggle off, wait about ten seconds, then switch it back on.
3. Open the app you want to hand off to once, so Windows refreshes its registration.
4. Select your test content again and open Click to Do to check the app list.
5. Confirm the target app now appears, and try the hand-off from the fresh list.

### Fix 5: Repair or reinstall the target app

When the default associations are correct and the Click to Do list is fresh, but one particular app still never appears or never launches, that app's own registration is the fault. The app may launch fine from its icon while still being invisible to Windows hand-offs, because launching and registering are separate mechanisms. Repairing re-registers the app without deleting its data.

1. Confirm the target app launches normally from its own icon or Start menu entry.
2. Open Settings, then Apps, then Installed apps, and find the target app.
3. Choose Repair from its advanced options and wait for the process to finish.
4. Test Open With from Click to Do again with matching content.
5. If repair fails, uninstall and reinstall the app, then retest the hand-off.
6. Check the [Microsoft Windows support hub](https://support.microsoft.com/en-us/windows) if the app still does not register after reinstalling.

### Fix 6: Update Windows and check for a wider registration fault

A system-wide registration fault shows up as several hand-offs failing at once, not just one app, and it usually follows a failed update or a disk problem. Windows updates can repair the hand-off components themselves, and a clean update pass plus a restart is the right final step before concluding that a deeper repair is needed.

1. Open Settings, then Windows Update, and install every pending update.
2. Restart the laptop after the updates, even if Windows does not insist on it.
3. Retest Open With with a plain link in Edge to confirm the basic hand-off.
4. Retest your original selection and target app to see whether both now work.
5. If several apps still fail together, note the pattern, since a system repair may be next.
6. For a related registration-style fault, see [eSIM not working on Snapdragon laptops](/articles/esim-not-working-snapdragon-laptop/), where a working component hides in the same way.

## Closing

Open With is a routing problem more often than an AI problem, so the fix usually lives in default apps or app registration rather than in the model or the NPU. Once a plain link hands off cleanly in Edge, you have a working reference point, and any remaining failure belongs to one specific app or content type.
