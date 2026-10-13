---
title: "Metered Connection Blocking Windows Update? How to Fix It"
slug: how-to-fix-metered-connection-blocking-windows-update
date: 2026-09-09
categories: ["windows-update"]
tags: ["metered connection", "update blocked", "wifi", "windows 11", "data cap"]
description: "Windows Update stuck on 'pending download' because of a metered connection? Here's how to update on your terms without losing your data cap."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update.webp"
faqs:
  - q: "How do I know a metered connection is what's blocking my updates?"
    a: "Open Settings → Windows Update: if updates sit at 'Pending download' indefinitely with no error, and Settings → Network & internet shows your Wi-Fi marked as metered, that's the cause. The telltale sign is everything else working fine — browsing, streaming — while only Windows Update refuses to move."
  - q: "Will turning off metered connection use all my mobile data?"
    a: "Only if you leave it off. The safe pattern is: turn metered off, download and install the updates, turn it back on immediately. A monthly cumulative update is typically 300 MB–1 GB. Check your remaining allowance first, and do the update early in your billing cycle when you have headroom."
  - q: "Can I force just one important update through on a metered connection?"
    a: "Yes — download that specific KB manually from the Microsoft Update Catalog on any connection (even your phone's browser), transfer the .msu via USB, and install it offline. This bypasses the metered restriction entirely since Windows Update's download rules don't apply to manual installs."
  - q: "Does Windows Update ever ignore the metered flag on its own?"
    a: "Rarely, and only for critical security updates when you enable 'download over metered connections' in Advanced options. By default, feature updates, driver updates, and most cumulative updates wait for an unmetered network. Don't count on exceptions — manage it deliberately. Treat the metered flag as absolute and schedule your updates around it instead."
---

The metered connection flag is Windows trying to protect you — from itself. It sees your mobile hotspot or capped home plan and refuses to download gigabytes of updates over it. Reasonable in principle, infuriating in practice when you're staring at 'Pending download' for a week and just want the security patch installed. The update isn't broken; it's obeying orders.

The fix isn't to permanently disable the protection — that just trades one problem (stuck updates) for another (a blown data cap). The fix is controlled updating: deliberate windows where you allow downloads, then re-enable the guard. This guide shows the full set of controls, from the simple toggle to per-update manual installs. For the best-practice summary version, see [the best way through a metered connection block](/articles/best-way-to-fix-metered-connection-blocking-windows-update/).

First, get your numbers: remaining data allowance and billing reset date. Every decision below depends on them.

## Why this happens

- **Metered flag pauses automatic downloads**: Windows treats metered networks as expensive and holds back most update payloads by design. This is why a laptop used exclusively on a hotspot can go weeks with entries stuck at Pending download.
- **Per-network setting is easy to forget**: The flag is stored per Wi-Fi network — a hotspot you flagged months ago stays flagged forever. Audit your known networks twice a year; stale flags are the most common mystery block.
- **Hotspots default to metered**: Tethered connections are auto-flagged, so laptop-on-phone setups silently block updates. Even so-called unlimited phone plans get flagged, since Windows cannot see your plan's fine print.
- **Driver and feature updates fully blocked**: Only some critical updates are exempt; drivers and feature upgrades wait indefinitely. Over months this leaves hardware on outdated drivers and the OS a feature version behind.
- **Delivery Optimization restricted**: Peer-to-peer sharing is curtailed on metered connections, slowing anything that does download. The few allowed downloads then come only from Microsoft's servers, which can be slower on congested hotspots.
- **No clear UI explanation**: The update screen shows pending with no hint that the metered flag is the reason. With no error code to search, users often misdiagnose this as a broken update service and attempt unnecessary resets.
- **Background apps also throttled**: Store apps and OneDrive pause too, making the whole system feel frozen in time. If everything except updates seems stale, the metered flag is the first thing to check.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the metered flag is the culprit

Two minutes of verification before you change anything. Skipping this verification leads people to reset update components for a problem that was just a toggle.

1. Settings → Network & internet → Wi-Fi → click your connected network.
2. Check whether **Metered connection** is ON — if yes, you've found it.
3. Settings → Windows Update: confirm updates show 'Pending download' rather than an error code.
4. Check your data allowance and reset date before deciding how to proceed.
5. Note the exact network name — you will whitelist or un-flag it deliberately in Fix 5.

### Fix 2: Run a controlled update window

The core technique: open the gate, update, close the gate. This is the highest-leverage habit in the guide: ninety seconds of toggling saves gigabytes of surprise downloads.

1. Turn **Metered connection OFF** for your current network.
2. Settings → Windows Update → **Check for updates**; let everything download and install (stay nearby — don't let the laptop sleep mid-install).
3. Reboot when prompted and verify Update history shows success.
4. Turn **Metered connection back ON** immediately. Set a phone alarm labeled 'metered back on' — forgetting this step is how caps get blown.
5. After re-enabling the metered flag, revisit Windows Update to confirm the queue shows paused rather than pending download.

### Fix 3: Allow updates over metered connections (selective)

Windows has a middle-ground setting for when you want updates but still want the flag's other protections. This middle ground is ideal for capped-but-generous plans where you want security patches without babysitting toggles.

1. Settings → Windows Update → **Advanced options**.
2. Enable **Download updates over metered connections**.
3. Leave the network itself flagged as metered (other apps still throttle).
4. Revisit this toggle monthly — turn it on for Patch Tuesday week, off afterward.
5. Test the setting with a small definition update first, watching data usage under Settings, Network and internet, Data usage.

### Fix 4: Manually install critical updates via the Catalog

For when data is truly precious: skip Windows Update's bulk download and hand-pick only what matters. Manual installs are the precision instrument here: one KB, one download, zero ambiguity about what crossed the meter.

1. Identify the KB you need (Update history or the security bulletin).
2. On any unmetered connection, download the .msu from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com).
3. Transfer via USB and install offline — metered rules don't apply to manual installs.
4. This is ideal for a single urgent security update on a nearly-exhausted plan.
5. Keep a small USB stick as your update courier — download several needed KBs at once on an unmetered connection.

### Fix 5: Un-flag networks that shouldn't be metered

Old flags on home or office Wi-Fi are a common silent blocker. Stale flags are silent precisely because the network works fine for everything except updates.

1. Settings → Network & internet → Wi-Fi → **Manage known networks**.
2. Open each network you use regularly and verify **Metered connection** is OFF for unmetered ones.
3. Leave it ON only for genuine hotspots and capped connections.
4. Re-check Windows Update — queued downloads often start on their own once the flag clears.
5. After clearing flags, force a fresh check in Windows Update and watch previously stuck items start.

### Fix 6: Use Delivery Optimization settings to reduce data use

When you do open the gate, make the download as lean as possible. Bandwidth caps inside Delivery Optimization turn an all-or-nothing download into a polite background trickle.

1. Settings → Windows Update → Advanced options → **Delivery Optimization**.
2. Under **Advanced options**, set bandwidth limits for downloads (e.g., 50% of measured bandwidth).
3. Enable **Allow downloads from other PCs** on your local network only — PCs on your LAN share the payload instead of each re-downloading.
4. Monitor per-update sizes in Update history to calibrate future windows.
5. Set an absolute bandwidth cap in Mbps rather than a percentage — percentages misbehave on variable hotspot speeds.

### Fix 7: Schedule updates around your billing cycle

The strategic fix: align Patch Tuesday with your data reset. Aligning updates with your billing cycle converts update management from reactive firefighting into a two-minute monthly routine.

1. Note Microsoft's Patch Tuesday (second Tuesday monthly) and your plan's reset date.
2. If they misalign badly, use **Pause updates** (Settings → Windows Update) to defer up to 5 weeks until your cycle resets.
3. Run your controlled update window in the first days after reset, when allowance is fullest.
4. Document the rhythm somewhere you'll see it — a recurring phone reminder beats memory.
5. Put a recurring calendar event two days after your reset date titled update window so it becomes automatic.

## Closing

A metered connection blocking updates isn't a malfunction — it's a guardrail you steer around deliberately. Verify the flag, run controlled update windows, hand-pick critical KBs via the Catalog when data is tight, and audit your network flags twice a year. Your cap stays intact and your laptop stays patched. Related guides: [the best way through a metered connection block](/articles/best-way-to-fix-metered-connection-blocking-windows-update/) and [how to reset Windows Update components on Windows 11](/articles/how-to-reset-windows-update-components-on-windows-11/).
