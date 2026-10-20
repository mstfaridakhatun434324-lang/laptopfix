---
title: "Copilot Daily Briefing Not Showing? How to Get It Back"
slug: copilot-daily-briefing-not-showing
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot", "daily briefing", "morning briefing", "troubleshooting", "ai pc", "windows 11"]
description: "Copilot daily briefing missing from your morning routine? Learn why the personalized briefing disappears and restore it with these step-by-step fixes."
thumbnail: "/images/thumbs/copilot-daily-briefing-not-showing.webp"
faqs:
  - q: "What is the Copilot daily briefing?"
    a: "The daily briefing is a personalized morning summary from Copilot: your calendar, weather, top news, and reminders in one place. It appears in the Copilot app, the Widgets board, or as a notification depending on your settings and region."
  - q: "Why did my daily briefing stop appearing?"
    a: "The usual causes: the briefing toggle got reset by an update, you signed out of the account the briefing is tied to, notification permissions changed, or the underlying calendar/weather data sources disconnected. Work through the toggles before assuming the feature is gone."
  - q: "Does the daily briefing need my calendar connected?"
    a: "For the calendar portion, yes. Without a connected Outlook or Google calendar, the briefing shows weather and news but no schedule. If your briefing looks empty rather than missing, a disconnected calendar is the likely cause."
  - q: "Is the daily briefing available in all regions?"
    a: "No — it is a staged rollout, and some regions get a reduced version (news and weather only). If the full briefing never appeared for you, availability rather than breakage may explain it."
---

The daily briefing is supposed to greet you with your day at a glance — meetings, weather, headlines. When it stops showing up, mornings get a little worse and the cause is rarely obvious: a reset toggle, a signed-out account, or a disconnected data source. This guide restores it step by step.

First, define "missing." Briefing shows but is empty? That is a data-source problem (calendar disconnected). Briefing nowhere to be found? That is a toggle, account, or rollout problem. The fixes below handle both. If the whole Widgets board is broken rather than just the briefing, fix the board first with our [Copilot widgets guide](/articles/copilot-widgets-not-working/).

Check your usual briefing location after each fix.

## Why this happens

- **Briefing toggle reset:** Updates sometimes flip the briefing setting off.
- **Signed out of the Copilot/Microsoft account:** The briefing is tied to your account identity.
- **Notification permissions revoked:** The briefing-as-notification path needs notification permission.
- **Calendar disconnected:** The schedule section vanishes when the calendar link breaks.
- **Region rollout limits:** Your region may not have the full briefing.
- **Corrupted Copilot app data:** Stale app state suppresses the briefing card.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Find and enable the briefing toggle

Updates reset this toggle more often than any other Copilot setting. Check it first.

1. Open the Copilot app and go to Settings.
2. Look for the daily briefing / morning briefing option and turn it on.
3. Set your preferred delivery time and location if the options appear.
4. Check the next morning — or look for the briefing card in the app immediately.

### Fix 2: Sign into the right Microsoft account

The briefing belongs to an account. A signed-out or switched account means no briefing.

1. In the Copilot app, verify the signed-in account is your personal one — the briefing is generated for the signed-in identity, so a different account means a different (or empty) briefing.
2. Sign out and back in to refresh the token.
3. Confirm the same account on the Widgets board if your briefing lives there.
4. Wait a few minutes for the briefing card to populate.

### Fix 3: Reconnect your calendar

An empty-looking briefing is usually a disconnected calendar, not a missing briefing.

1. Open the briefing settings and check connected accounts.
2. Reconnect Outlook (or your calendar provider) and grant calendar permission.
3. Verify upcoming events appear in the briefing card.
4. If the calendar will not connect, check its own sign-in separately — expired tokens are common.

### Fix 4: Allow briefing notifications

If your briefing arrives as a notification, revoked notification permission kills it silently.

1. Open Settings > System > Notifications.
2. Ensure notifications are on globally and for the Copilot app specifically.
3. Check Focus / Do Not Disturb schedules — a morning DND window eats the briefing. Also confirm Copilot may show notifications on the lock screen if that is where you look for it.
4. Test by triggering a manual briefing view in the app.

### Fix 5: Reset the Copilot app

Stale app state can suppress the briefing card even when every toggle is correct.

1. Go to Settings > Apps > Installed apps > Microsoft Copilot > Advanced options.
2. Click Repair and check for the briefing.
3. If repair fails, click Reset (have your sign-in credentials ready).
4. Sign back in, re-enable the briefing toggle, and reconnect the calendar.

### Fix 6: Check region and update everything

The remaining causes are availability and outdated components.

1. Confirm your region supports the full daily briefing (staged rollout).
2. Update the Copilot app from the Microsoft Store and install Windows updates.
3. Restart and check for the briefing the next morning.
4. If the Widgets board itself is broken, repair it with our [Copilot widgets guide](/articles/copilot-widgets-not-working/) — and if AI features broadly misbehave after an update, see [NPU disappeared after Windows update](/articles/npu-disappeared-after-windows-update/). Microsoft documents Copilot features on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

The daily briefing disappears for mundane reasons: a reset toggle, a signed-out account, a disconnected calendar, or a muted notification channel. Re-enable the toggle, refresh the sign-in, reconnect the calendar, allow the notification, and reset the app if needed. Tomorrow morning, your day should be waiting for you again — summarized before coffee. Microsoft's own image tools share AI components — see [Copilot Designer Image Creator errors](/articles/copilot-designer-image-creator-error/) — and Recall issues overlap on Lenovo machines ([Lenovo Yoga Slim 7x Recall issues](/articles/lenovo-yoga-slim-7x-recall-issues/)).
