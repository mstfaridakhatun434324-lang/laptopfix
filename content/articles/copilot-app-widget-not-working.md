---
title: "How to Fix the Copilot App Widget Not Working on Windows 11"
slug: copilot-app-widget-not-working
date: 2026-10-26
categories: ["ai-pc"]
tags:
  - copilot
  - widgets
  - windows-11
  - troubleshooting
  - widgets-board
description: "Copilot widget not working on Windows 11? Fix blank, frozen, or missing widgets with these proven steps for the Widgets board, app, sign-in, and board settings."
thumbnail: "/images/thumbs/copilot-app-widget-not-working.webp"
faqs:
  - q: "Where should the Copilot widget appear on Windows 11?"
    a: >
      The Copilot widget normally appears on the Widgets board, opened with Windows key + W or by
      clicking the Widgets icon on the taskbar. If the widget is pinned, it shows a compact Copilot
      card with a prompt box; if it is missing, the board itself or the widget service may be at
      fault.
  - q: "Why is my Copilot widget blank or stuck on loading?"
    a: >
      A blank widget usually means the Widgets service cannot reach Copilot's content — because of a
      sign-in problem, a stalled Web Experience Pack, or a network block. The widget shell loads
      fine, but the content feed behind it never arrives.
  - q: "Can I remove and re-add the Copilot widget?"
    a: >
      Yes. Open the Widgets board, find the Copilot widget's menu, and remove it, then re-add it
      from the widget gallery. This forces a fresh content fetch and often clears a stuck widget
      without touching the main Copilot app.
  - q: "Does the Copilot widget need the full Copilot app installed?"
    a: >
      Yes, the widget is a companion view powered by the Copilot app and its sign-in. If the app is
      missing, outdated, or signed out, the widget has nothing to display and may vanish from the
      board entirely.
---

Widgets are supposed to give you Copilot at a glance: open the Widgets board, and there is a compact card ready for a quick question, a summary, or a shortcut into the full app. When the Copilot widget stops working, that glanceable helper disappears or turns useless. The widget may be missing from the board entirely, stuck on a loading spinner, blank white, or frozen on yesterday's content. The full Copilot app often works perfectly in the meantime, which points the finger squarely at the widget layer rather than Copilot itself.

The widget layer has its own moving parts. The Widgets board is powered by the Windows Web Experience Pack, the widget fetches its content through your Microsoft account sign-in, and it renders inside a web-based shell that is separate from the main app. If the Experience Pack stalls, the board cannot render any widget properly. If sign-in lapses, the widget cannot fetch personalized content. If the Copilot app is outdated, the widget may have nothing to connect to. Each failure looks slightly different, but all of them live in this middle layer.

The fixes below start with the board itself, then the widget, then the app and sign-in behind it. A similar layered approach solves other companion-feature failures; for example, [scanner driver problems on ARM Windows](/articles/scanner-driver-arm-windows-issues/) often come down to a middle layer — the driver service — rather than the app or the hardware. Widget issues can also cluster with other app quirks on AI-branded machines, as seen in [Acer Swift X 14 AI reports](/articles/acer-swift-x-14-ai-problems/), where one misbehaving service affects several features at once. And if your Copilot theme is also misbehaving, note that the [Copilot app stuck in dark mode](/articles/copilot-app-dark-mode-stuck/) shares the same rendering plumbing as the widget.

## Why this happens

- **Widgets board service stalled:** The Windows Web Experience Pack renders the board. If its process hangs, every widget — including Copilot's — freezes or goes blank.
- **Widget removed or unpinned accidentally:** A stray click on the widget's menu can remove it from the board, making it look like the feature broke when it was simply dismissed.
- **Sign-in expired or account mismatch:** The widget fetches content for the signed-in account. If sign-in lapsed or the board uses a different account, the feed never loads.
- **Outdated Copilot app or Experience Pack:** The widget depends on a matching app version. An outdated Copilot app or a pending Experience Pack update can break the connection.
- **Network block on widget content:** The widget loads its content from the web. A firewall, VPN, or proxy rule that blocks the feed leaves a blank card.
- **Corrupted widget cache:** Stale cached widget data can trap the card in a loading state that survives reboots until the cache is cleared.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Reopen the Widgets board and refresh it

The simplest explanation is a one-time board glitch, and a clean reopen is the fastest way to rule it out before you change any settings.

1. Close the Widgets board completely with the Esc key or by clicking elsewhere.
2. Press Windows key + W to reopen the board.
3. Wait 30 seconds for the widgets to refresh their content.
4. Scroll the board to check whether the Copilot widget appears further down.
5. If the board itself is blank, restart the laptop and try again.

### Fix 2: Remove and re-add the Copilot widget

Re-adding the widget forces a brand-new content fetch and a fresh rendering, which clears most stuck or blank states without touching the main app.

1. Open the Widgets board with Windows key + W.
2. Find the Copilot widget and click its three-dot menu.
3. Choose Remove widget or Unpin, then close the board.
4. Reopen the board and click the plus icon to open the widget gallery.
5. Find Copilot in the gallery and add it back, then wait for content to load.

### Fix 3: Restart the Widgets service and Experience Pack

When the whole board misbehaves, the service behind it needs a restart. This refreshes the rendering engine that all widgets share.

1. Press Ctrl + Shift + Esc to open Task Manager.
2. Look for Widgets or Windows Web Experience Pack processes.
3. Right-click each one and choose End task.
4. Reopen the Widgets board, which relaunches the service automatically.
5. Wait a full minute for all widgets, including Copilot, to reload.

### Fix 4: Check sign-in and account consistency

A widget signed into the wrong account, or no account at all, cannot fetch its content. Aligning the board's account with Copilot's account restores the feed.

1. Open the Widgets board and check which account is shown at the top.
2. Open the Copilot app and confirm the same account is signed in there.
3. If they differ, sign out of the board's account and sign in with the matching one.
4. If sign-in expired, sign out of Copilot and sign back in.
5. Reopen the board and check whether the widget content appears.

### Fix 5: Update Copilot and the Web Experience Pack

Version mismatches between the app and the board break the widget's connection silently. Updating both sides together removes that mismatch as a cause.

1. Open the Microsoft Store, then Library, and update the Copilot app.
2. Also update the Windows Web Experience Pack if it appears in the library.
3. Then open Settings, then Windows Update, and install pending system updates.
4. Restart the laptop after all updates finish installing.
5. Open the Widgets board and confirm the Copilot widget loads fresh content.

### Fix 6: Repair Copilot and clear the widget cache

When the widget stays blank after updates, corrupted local data is the remaining suspect. Repairing the app and clearing the widget cache gives both layers a clean start.

1. Open Settings, then Apps, then Installed apps, and find Copilot.
2. Click the three dots, choose Advanced options, and click Repair.
3. If Repair fails, use Reset on the same page and sign in again.
4. Check [Copilot in Windows support](https://support.microsoft.com/en-us/windows) for any current widget service issues.
5. Reopen the Widgets board and re-add the Copilot widget if needed.

## Closing

A broken Copilot widget is a middle-layer problem: the app is usually fine, and the board is usually fine, but the connection between them has stalled. Reopening the board, re-adding the widget, restarting the service, and aligning sign-in covers nearly every case, with an app repair as the final step. Once the card loads again, Copilot returns to its proper place — a glance away, whenever you need a quick answer.
