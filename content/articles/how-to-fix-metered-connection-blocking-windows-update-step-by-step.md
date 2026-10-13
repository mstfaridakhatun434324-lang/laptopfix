---
title: "Metered Connection Blocking Windows Update? Step-by-Step Fix (All PCs)"
slug: how-to-fix-metered-connection-blocking-windows-update-step-by-step
date: 2026-09-22
categories: ["windows-update"]
tags:
  - metered connection
  - windows update
  - windows 11
  - windows 10
  - step-by-step
description: "Step-by-step guide to unblock Windows Update on a metered connection: Settings toggles, registry edits, group policy, and manual install workarounds."
thumbnail: "/images/thumbs/how-to-fix-metered-connection-blocking-windows-update-step-by-step.webp"
faqs:
  - q: "What is a metered connection in Windows?"
    a: >
      A metered connection is a network Windows treats as having a limited data allowance — mobile hotspots, tethered phones, and 4G modems are typical examples. On metered networks Windows pauses automatic update downloads, restricts Store app updates, and limits background data to avoid unexpected charges. You can mark any network metered manually, and Windows marks obvious mobile connections automatically.
  - q: "Will Windows ever update on a metered connection by itself?"
    a: >
      Rarely. Critical security updates can occasionally slip through, but in practice monthly quality updates, driver updates, and feature updates all wait until you are on an unmetered network or explicitly permit downloads. If you rely on a hotspot full-time, enabling Download updates over metered connections is the practical answer.
  - q: "Is editing the registry to allow metered updates safe?"
    a: >
      Yes, the specific DWORD described in this guide only controls whether Windows Update may download over metered connections — it does not disable metering for other apps or change billing behavior. Still, back up the registry key first (right-click > Export), and do not apply random registry tweaks from forums without understanding them.
  - q: "Why does the metered toggle keep turning itself back on?"
    a: >
      The usual culprits are a corrupted network profile, a data limit that re-implies metering, or management policy on a work machine reapplying the setting. Forget and rejoin the network, remove data limits, and check for MDM or group policy enforcement. On personal machines, the registry value in Fix 4 makes your preference survive.
---

Windows Update and metered connections are natural enemies. Mark a network as metered and Windows politely stops downloading updates to protect your data — which is exactly what you want on a phone hotspot, and exactly what you do not want when the flag is wrong or when a critical patch cannot wait.

This guide is the complete step-by-step reference for every way to resolve the conflict, from the simple Settings toggle most people need, through the registry edit for Windows Home users who want updates allowed permanently, to the Group Policy route for Pro users, and finally the manual-install escape hatch.

Unlike brand-specific guides, this one covers the underlying machinery, so it works on any Windows 10 or Windows 11 laptop regardless of manufacturer.

## Why this happens

- **The metered toggle is on for the active network:** the most common cause — the flag is set on Wi-Fi or Ethernet and Windows is simply obeying it.
- **Windows auto-detects hotspot hardware as metered:** connections through phone tethering or 4G/5G USB modems are flagged metered automatically, correctly but inconveniently.
- **A data limit implies metered behavior:** setting a data cap in Windows makes the connection behave as metered for updates even if the toggle looks off.
- **Roaming or cost-aware network detection:** Windows can mark networks metered based on cost signals from the connection hardware.
- **Policy or registry forcing metered handling:** IT-managed machines or old tweaks can force metered behavior that the Settings toggle cannot override.
- **Delivery Optimization throttled on metered links:** peer-to-peer update sharing is restricted on metered connections, slowing or stalling large downloads.
- **Corrupted network profile caching the flag:** a damaged profile can report metered status that survives normal toggling.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Toggle metered connection off in Settings

Start here — this resolves the issue for the overwhelming majority of users in under a minute.

1. Open Settings > Network & internet and click Wi-Fi or Ethernet, whichever you use.
2. Click the connected network's name to open its properties.
3. Set Metered connection to Off.
4. Go to Windows Update, click Check for updates, and confirm downloads begin.

### Fix 2: Permit updates over metered connections

When the network truly is metered but you need updates anyway, this targeted permission is better than unflagging the whole network, because other apps still treat it as metered. It is the ideal compromise on hotel Wi-Fi, airport networks, or a phone tether where every megabyte counts but a critical security patch cannot wait until you are back on an unlimited connection.

1. Go to Settings > Windows Update > Advanced options.
2. Turn on Download updates over metered connections.
3. Optionally enable it only long enough to pull the pending updates, then turn it off.
4. Note that large feature updates may still wait — this setting mainly unblocks quality and security updates.

### Fix 3: Remove data limits and reset the network profile

Stale data limits and corrupted profiles are the two ghosts that survive the basic toggle. Exorcise both.

1. Go to Settings > Network & internet > Advanced network settings > Data usage and remove any limit.
2. Go to Wi-Fi > Manage known networks, forget the network, and rejoin it fresh.
3. Confirm the metered toggle is Off on the new profile.
4. Check for updates again.

### Fix 4: Allow updates via Registry (Windows Home)

Home edition has no Group Policy editor, but the same setting lives in the registry. This makes the permission permanent across reboots and network changes.

1. Press Win + R, type regedit, and approve the elevation prompt.
2. Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsUpdate\UX\Settings.
3. Right-click, choose New > DWORD (32-bit) Value, and name it AllowAutoWindowsUpdateDownloadOverMeteredNetwork.
4. Set its value to 1, close the editor, and reboot — then check for updates.

### Fix 5: Allow updates via Group Policy (Windows Pro)

Pro and Enterprise users get the clean supported path: a policy that explicitly permits update downloads on metered networks.

1. Press Win + R, type gpedit.msc, and press Enter.
2. Navigate to Computer Configuration > Administrative Templates > Windows Components > Windows Update > Manage updates offered from Windows Update.
3. Open Allow updates to be downloaded automatically over metered connections, set it to Enabled, and click OK.
4. Run gpupdate /force in an elevated Command Prompt, then check for updates.

### Fix 6: Install the update manually from the Microsoft Update Catalog

When policy, data caps, or a work machine make the flag immovable, sidestep the whole mechanism: download the update package directly and install it by hand.

1. Find the KB number in Settings > Windows Update > Update history.
2. Go to the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) and search for that KB.
3. Download the package matching your architecture (usually x64) and double-click the .msu.
4. Reboot and verify it in update history.

### Fix 7: Reset the network stack as a last resort

If the metered flag behaves erratically — on for some networks, stuck on others — the network stack itself may need resetting. This clears all profiles, so have your Wi-Fi passwords handy.

1. Open Command Prompt as administrator.
2. Run: netsh winsock reset and then netsh int ip reset.
3. Reboot, reconnect to your Wi-Fi, and verify the metered toggle is Off.
4. Check for updates to confirm normal behavior is restored.

## Closing

Metered-connection blocks are Windows protecting your data plan a little too enthusiastically. The Settings toggle fixes most cases; the registry and policy routes make the permission stick; and the manual catalog install bypasses the machinery entirely when nothing else is allowed. Once updates flow again, consider setting active hours so large downloads happen when the network is idle, and re-enable the metered flag on genuinely limited connections to keep background data under control. If your HP laptop specifically mislabels networks, see our [HP metered connection guide](/articles/how-to-fix-metered-connection-blocking-windows-update-on-hp-laptop/), and when updates stall for other reasons, the [error 0x80070002 fix](/articles/how-to-fix-error-0x80070002-in-windows-11-24h2/) covers the next most common download failure.
