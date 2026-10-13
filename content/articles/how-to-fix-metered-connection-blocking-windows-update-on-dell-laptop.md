---
title: "How to Fix a Metered Connection Blocking Windows Update on a Dell Laptop"
slug: how-to-fix-metered-connection-blocking-windows-update-on-dell-laptop
date: 2026-09-18
categories: ["windows-update"]
tags: ["metered connection", "windows update", "dell", "wifi", "windows 11"]
description: "Windows Update won't download on your Dell laptop? A metered connection setting may be blocking it. Here's how to check and fix it."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-on-dell-laptop.webp"
faqs:
  - q: "What does a metered connection do to Windows Update?"
    a: "Marking a connection as metered tells Windows to treat it like a limited mobile data plan: automatic update downloads pause, some app updates stop, and OneDrive syncing may reduce. Critical security updates can still come through, but feature and driver updates wait. It is a data-saving feature, not an error — but it blocks updates when enabled accidentally."
  - q: "How do I know if my connection is set as metered?"
    a: "Go to Settings, then Network and internet, then Wi-Fi, and click your connected network. If the Metered connection toggle is on, that is your blocker. Windows Update will show a message that updates are paused or that it is waiting on a metered connection. Ethernet connections can be metered too — check the Ethernet page the same way."
  - q: "Will turning off metered connection use a lot of data?"
    a: "It can. A monthly cumulative update is typically a few hundred megabytes, and feature updates run several gigabytes. If you are genuinely on a limited data plan, keep the metered flag on and install updates manually over unmetered Wi-Fi when convenient. Only disable it permanently on connections with generous or unlimited data."
  - q: "Can I download updates over a metered connection anyway?"
    a: "Yes. In Settings, then Windows Update, then Advanced options, enable Download updates over metered connections. This keeps the metered flag — and its other data-saving behaviors — while allowing updates through. It is the best compromise when you need updates but want to keep background data usage restrained."
---

You click "Check for updates" on your Dell laptop and nothing downloads. Or Windows Update shows updates available but sits at 0 percent indefinitely, sometimes with a note about a metered connection. Everything else about the internet works fine. The culprit is often a single toggle: your Wi-Fi or Ethernet connection is marked as metered, and Windows is obediently refusing to download updates over it.

Metered connection is a data-saving feature designed for mobile hotspots and capped plans. When it is on, Windows pauses automatic update downloads to protect your data allowance. The problem is that the toggle gets enabled accidentally — Windows sometimes auto-enables it on connections it identifies as mobile, and it stays on long after you are back on home Wi-Fi. Dell laptops with mobile broadband or frequent hotspot use are especially prone to this.

The fix is quick once you know where to look, but there are a few subtleties: per-network settings, the difference between pausing the flag and allowing updates through it, and Dell-specific update tools that bypass it. Work through the fixes in order.

## Why this happens

- **The Wi-Fi network is marked as metered.** Windows pauses update downloads on metered connections by design.
- **Windows auto-enabled it on a hotspot.** Connections Windows identifies as mobile get the metered flag automatically, and it persists.
- **The Ethernet connection is metered too.** Less common, but the same toggle exists for wired connections.
- **A VPN or virtual adapter inherited the flag.** Some VPN setups mark their virtual adapter as metered.
- **Updates are paused in addition to the metered flag.** Both conditions can be active at once, and both must be cleared.
- **Delivery Optimization is restricted on metered connections.** Peer-to-peer update sharing shuts down, which can stall already-started downloads.
- **Dell's own tools behave differently.** SupportAssist may still download drivers while Windows Update is blocked, creating confusion about what is actually updating.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check whether the connection is metered

Confirm the diagnosis before changing anything.

1. Open **Settings > Network & internet > Wi-Fi** and click your connected network's name.
2. Look at the **Metered connection** toggle. If it is on, you have found your blocker.
3. For wired connections, check **Settings > Network & internet > Ethernet** and click the connection — the same toggle exists there.
4. Note which networks are metered. The setting is per-network, so your home Wi-Fi and your phone hotspot have independent flags.

### Fix 2: Turn off the metered flag on trusted networks

If you are on unlimited home or office Wi-Fi, the flag should not be there.

1. On the network's properties page, turn **Metered connection** off.
2. Return to **Settings > Windows Update** and click **Check for updates**. Downloads should begin immediately.
3. Repeat for any other trusted networks where the flag was wrongly enabled.
4. Leave the flag on for genuine mobile hotspots and capped connections — that is what it is for.

### Fix 3: Allow updates over metered connections instead

If you want to keep the data-saving behavior but still get updates, use the compromise setting.

1. Go to **Settings > Windows Update > Advanced options**.
2. Enable **Download updates over metered connections**.
3. Click **Check for updates**. Updates now download even with the metered flag on.
4. Monitor your data usage for a month to make sure the compromise fits your plan — feature updates are several gigabytes.

### Fix 4: Check for paused updates

Metered connections and paused updates are independent blockers that produce the same symptom.

1. Open **Settings > Windows Update** and look for a **Paused** notice with a resume date.
2. If updates are paused, click **Resume updates**.
3. Also check **Advanced options** for any active pause period and clear it.
4. With both the metered flag handled and the pause cleared, retry the update check.

### Fix 5: Reset the network stack if the flag will not stay off

Occasionally the metered setting re-enables itself due to a corrupted network profile.

1. In **Settings > Network & internet > Wi-Fi**, forget the network, then reconnect fresh and set the metered toggle correctly.
2. If it still misbehaves, open an elevated Command Prompt and run `netsh winsock reset` followed by `netsh int ip reset`, then restart.
3. Reconnect to the network and verify the metered setting holds.
4. As a last resort for the network profile, use **Settings > Network & internet > Advanced network settings > Network reset**.

### Fix 6: Use Dell SupportAssist for drivers in the meantime

While sorting out Windows Update, Dell's own tool can keep drivers current.

1. Open **SupportAssist** and run a driver scan. It downloads independently of the Windows Update metered restriction.
2. Install any offered drivers, especially network drivers — an outdated Wi-Fi driver can itself cause connection misidentification.
3. Get the latest network driver from [Dell support](https://www.dell.com/support) using your Service Tag if SupportAssist misses it.
4. Once Windows Update is unblocked, let both systems run — they cover different update types.

### Fix 7: Clear the stalled update queue

Downloads that started before the metered flag was set can be stuck in a half-paused state.

1. In an elevated Command Prompt, stop the services: `net stop wuauserv`, `net stop cryptSvc`, `net stop bits`, `net stop msiserver`.
2. Rename the cache folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restart the services with the matching `net start` commands.
4. Check for updates. With the metered issue resolved and a clean cache, the queue rebuilds and downloads normally. For general update pipeline help, [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows) documents the metered behavior in detail.

## Closing

A metered connection blocking Windows Update is one of the most satisfying problems to fix, because the cause is a single toggle and the solution takes thirty seconds once you find it. The lesson worth keeping is that the setting is per-network and sticky — check it whenever updates mysteriously stall after switching networks. If your updates are stuck at 0 percent for a different reason, the [update stuck downloading guide](/articles/how-to-fix-windows-update-stuck-downloading-after-windows-11-update/) covers the other causes, and the [0x80070002 error walkthrough](/articles/how-to-fix-windows-update-error-0x80070002-after-windows-11-update/) handles the missing-files failure that sometimes follows a long stall.
