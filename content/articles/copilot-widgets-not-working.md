---
title: "Copilot Widgets Not Working on Windows 11? How to Fix Them"
slug: copilot-widgets-not-working
date: 2026-10-20
categories: ["ai-pc"]
tags: ["copilot", "widgets", "widgets board", "troubleshooting", "ai pc", "windows 11"]
description: "Copilot widgets blank or missing from the Windows 11 widgets board? Learn why the widgets fail to load their content and bring them back with these fixes."
thumbnail: "/images/thumbs/copilot-widgets-not-working.webp"
faqs:
  - q: "Where are Copilot widgets in Windows 11?"
    a: "Copilot-related widgets live on the Widgets board (Windows key + W): weather, news, calendar, and Copilot prompt shortcuts. If the board itself will not open, the problem is the Widgets feature, not any single widget."
  - q: "Why are my widgets blank or stuck loading?"
    a: "Blank widgets mean the board loaded but the web content behind the widgets failed — usually a sign-in problem with the widgets' Microsoft account, a network filter, or a corrupted Widgets cache. The board shell works; the data layer does not."
  - q: "Do widgets need me to be signed in?"
    a: "Personalized widgets (calendar, Copilot prompts tied to your account) need your Microsoft account signed into the Widgets board specifically — separate from your Windows sign-in. Generic widgets like weather can work signed out."
  - q: "Can I remove Copilot from the widgets board?"
    a: "You can remove individual widgets by clicking their three-dot menu and choosing remove, and you can disable the Widgets board entirely in Settings > Personalization > Taskbar. But if widgets are broken rather than unwanted, fix them with this guide instead."
---

The Widgets board should be a glanceable dashboard — weather, calendar, news, Copilot shortcuts. Instead yours shows blank cards, endless spinners, or the board will not open at all. Widget failures are data-layer problems: the board shell is fine, but sign-in, network, or cache issues starve the widgets of content. On Copilot+ PCs the board also hosts AI-powered widgets, so a broken board feels like a bigger loss.

The diagnostic split matters: board-won't-open is a Windows feature problem; board-opens-but-widgets-blank is a sign-in/data problem. This guide fixes both in order. If you are specifically missing the daily briefing content, see [daily briefing not showing](/articles/copilot-daily-briefing-not-showing/) — it builds on the same board.

Press Windows key + W to test the board after each fix, and give each change a few seconds — widget content loads asynchronously, and a hasty retest can look like a failure.

## Why this happens

- **Not signed into the Widgets board:** Personalized widgets need a separate board sign-in.
- **Widgets feature disabled:** The taskbar toggle for Widgets can be off.
- **Corrupted Widgets cache:** Stale cache data breaks widget rendering.
- **Network filtering:** Strict DNS or firewall rules block widget content endpoints.
- **Outdated Web Experience Pack:** Widgets run on this Store component; old versions have rendering bugs.
- **Conflicting region settings:** Widget content services vary by region and fail on mismatches.

## How to fix it

Work through these in order — diagnose first, then act.
### Fix 1: Turn the Widgets board on

If the board will not open at all, the feature itself may be disabled. This happens after some Windows updates that quietly reset taskbar preferences.

1. Open Settings > Personalization > Taskbar.
2. Make sure the Widgets toggle is on.
3. Press Windows key + W — the board should slide in.
4. If it opens now, the problem was just the toggle.

### Fix 2: Sign into the Widgets board

Personalized widgets need the board's own sign-in, separate from Windows sign-in.

1. Open the Widgets board (Windows key + W).
2. Click the profile icon in the board and sign in with your Microsoft account.
3. Wait for the widgets to refresh with your data.
4. Check whether calendar and Copilot widgets now populate.

### Fix 3: Clear the Widgets cache

Stale cache data is the top cause of blank or stuck-loading widgets. The board caches feed content aggressively, and one corrupted entry can poison every widget at once — which is why a cache clear fixes problems that look much deeper.

1. Close the Widgets board.
2. Open Task Manager and end any "Widgets" processes.
3. Alternatively, sign out and back into Windows to clear the board's session state.
4. Reopen the board and check whether widgets render.

### Fix 4: Update the Web Experience Pack

Widgets run on the Windows Web Experience Pack from the Microsoft Store. Old versions have rendering bugs.

1. Open the Microsoft Store > Library and check for updates.
2. Install any update for "Windows Web Experience Pack."
3. Restart the laptop.
4. Open the board and verify widgets load.

### Fix 5: Check network filtering

Widgets pull content from Microsoft endpoints. Strict DNS, VPNs, or firewalls starve them, and because the board shell loads locally, everything looks fine except the empty cards.

1. Disconnect your VPN temporarily and reopen the board.
2. If you use custom DNS or ad-blocking DNS, try your ISP's default temporarily.
3. Check firewall logs for blocked Microsoft content endpoints.
4. If widgets load off-VPN, adjust your VPN or filter's allowlist.

### Fix 6: Repair the Widgets feature

For stubborn cases, repair the underlying components.

1. Install all pending Windows updates and restart.
2. Run `sfc /scannow` in an elevated Command Prompt.
3. Confirm your region supports full widget content (Settings > Time & language > Language & region).
4. As a related check, our [daily briefing guide](/articles/copilot-daily-briefing-not-showing/) covers the briefing card specifically, and Microsoft documents Widgets on the [Windows support hub](https://support.microsoft.com/en-us/windows).

## Closing

Widgets fail at the data layer: board sign-in, cache, the Web Experience Pack, or network filtering. Turn the board on, sign into it, clear its cache, update its engine, and unblock its network path. The board should be a thirty-second glance at your day — these fixes get it back to that. MSI's AI laptops have their own quirks — see [MSI Prestige AI Evo problems](/articles/msi-prestige-ai-evo-problems/) — and confirm your AI hardware is healthy with [how to check NPU TOPS in Windows 11](/articles/how-to-check-npu-tops-windows-11/).
