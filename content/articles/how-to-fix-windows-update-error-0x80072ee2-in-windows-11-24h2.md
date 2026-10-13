---
title: "How to Fix Windows Update Error 0x80072EE2 in Windows 11 24H2"
slug: how-to-fix-windows-update-error-0x80072ee2-in-windows-11-24h2
date: 2026-10-06
categories: ["windows-update"]
tags: ["windows update", "0x80072ee2", "error code", "windows 11", "timeout"]
description: "Error 0x80072EE2 means the connection to Microsoft's update servers timed out. Diagnose the slowdown and speed up the handshake with this guide."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80072ee2-in-windows-11-24h2.webp"
faqs:
  - q: "What does error 0x80072EE2 mean?"
    a: "WININET_E_TIMEOUT: the request to Microsoft's servers exceeded its time allowance and was abandoned. The symptom is distinctive — Windows spends a long time checking for updates, then gives up. Something between your PC and Microsoft is too slow: the network, a proxy lookup, or security software inspecting each connection."
  - q: "Should I just wait and retry later?"
    a: "Often, yes — timeouts are frequently temporary. Patch Tuesday congestion, a bad Wi-Fi moment, or a brief ISP hiccup all resolve on their own. Wait an hour or two and retry once. If the timeout is consistent across hours and networks, though, something local is slowing the handshake and needs fixing."
  - q: "How can a proxy cause a timeout when I don't use one?"
    a: "Windows may still perform automatic proxy detection (WPAD) on networks without a proxy, and that lookup can hang for ages — eating the whole timeout budget before the real request even starts. Disabling automatic detection removes the delay entirely on networks that need no proxy."
  - q: "Does my VPN slow down Windows Update?"
    a: "It can substantially. Tunneled routes are slower and less reliable than direct ones, and the added latency is a classic trigger for this code. Disconnect the VPN completely for the update attempt. If updates work without it, the VPN was the bottleneck."
---

The symptom stands out: Windows lingers on "checking for updates," the spinner revolves, and then — nothing. No error dialog with details, no partial progress; just an abandoned request after a long, fruitless wait. The connection to Microsoft's servers timed out. 0x80072EE2 is the formal name for that abandonment: WININET_E_TIMEOUT, the request that exceeded its allowance.

This hits laptops hardest on sluggish hotel Wi-Fi, crowded home networks, and anywhere firewalls or VPNs scrutinize traffic. But the slowdown is not always the network's fault. Where no proxy exists, the automatic detection lookup may hang endlessly, devouring the entire timeout budget. Security software that examines each connection also injects latency into every handshake.

Many timeouts are transient — Patch Tuesday crowds or a flaky Wi-Fi moment. A brief triage separates wait-it-out cases from repair cases, and the fixes below begin with that distinction. Five minutes of diagnosis now saves you from an hour of unnecessary repairs — or from waiting all day on a problem that will never fix itself.

## Why this happens

- **Sluggish or crowded network.** Update servers will not wait indefinitely; over a saturated link the request outlasts its window.
- **VPN injecting latency.** Tunnelled paths run slower and less reliably — deadly for timeout-sensitive requests.
- **Proxy auto-detection stalls.** Where no proxy is configured, the WPAD lookup can hang and swallow the whole time budget.
- **Firewall performing deep inspection.** Security tools examining every connection may push the handshake beyond its deadline.
- **BITS queue jammed.** A wedged background transfer can hog the download pipeline, starving the update check.
- **Slow ISP routing.** Certain providers reach the update CDN over paths that are simply sluggish.
- **Too many retries piled up.** Rapid repeated checks can queue conflicting requests that all time out.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Determine whether the network is just having a moment

There is no point waiting indefinitely on a saturated link — but do not rebuild Windows over a hiccup either. The triage below takes five minutes and tells you which situation you are in — and the answer determines whether Fix 1 alone suffices or the deeper repairs are needed.

1. Pause for an hour or two, then retry a single time — particularly on the month's second Tuesday, when Microsoft's servers are swamped.
2. If you are on Wi-Fi, move closer to the router or try a wired connection.
3. When timeouts persist across hours and networks alike, keep going — some local factor is slowing the handshake.

### Fix 2: Switch off proxy auto-detection

Where the network uses no proxy, the automatic detection lookup can stall for ages. Switching it off costs nothing and removes a whole category of delay. Corporate laptops that genuinely need a proxy should leave it alone — this fix is for home and personal machines where no proxy exists.

1. Launch Settings > Network & internet > Proxy.
2. Switch off the Automatically detect settings option.
3. Also verify that no manual proxy is set, unless the network truly requires one.
4. Retry the update check at once.

### Fix 3: Empty the wedged BITS transfer queue

Background Intelligent Transfer Service handles update downloads, and one jammed job in its queue can stall new requests until they time out. The queue survives reboots, so restarting the PC alone will not clear it — the reset command below is required.

1. Summon an administrator Command Prompt now.
2. Run `bitsadmin /reset /allusers` to cancel stuck transfers.
3. Run `net stop bits`, wait a moment, then `net start bits`.
4. Check for updates once again.

### Fix 4: Briefly sidestep traffic-scanning security tools

Security tools that scrutinize every connection slow each handshake measurably. A controlled test with inspection switched off identifies the culprit quickly.

1. Switch off the web-shield or firewall piece of third-party security tools for the test; keep the core antivirus active.
2. Retry the update check immediately.
3. On success, create an exclusion for Windows Update traffic instead of leaving the shield disabled.
4. Sever any VPN connection entirely — tunneled latency classically triggers this code.

### Fix 5: Let the troubleshooter take a turn

The troubleshooter detects connectivity misconfigurations and stuck queues, repairing them automatically.

1. Call up Settings > System > Troubleshoot > Other troubleshooters.
2. Release the Windows Update entry and chase its prompts.
3. Reboot the laptop and re-attempt the update check.

### Fix 6: Reset the update components fully

When the local pipeline itself is the bottleneck, a full reset clears every layer at once.

1. Cut the services: `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`.
2. Shelve the folders: `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
3. Restore the services: `net start wuauserv`, `net start bits`, `net start cryptsvc`.
4. Seek updates and confirm the timeout is fully gone.

### Fix 7: Grab the update yourself from the Catalog

A browser download does not share the update engine's timeout budget, so even a slow connection can fetch the package given enough time. The [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) carries every cumulative release.

1. Under Settings, open Windows Update > Update history and record the KB number.
2. Download the x64 Windows 11 package from the Catalog using your browser.
3. Run the `.msu` file, then reboot if asked.

## Closing

Timeouts reward the patient and the methodical: rule out the transient, remove the local slowdowns, and the handshake completes. Keep a mental note of what fixed it, too — timeout causes tend to recur on the same laptop, and the same repair will work next time. Once the check succeeds but downloads start collapsing, the [24H2 update-error reference](/articles/how-to-fix-windows-update-error-in-windows-11-24h2/) continues with the download-phase codes, while the [Update troubleshooter guide](/articles/best-way-to-fix-windows-update-with-troubleshooter/) handles the automated basics — including the documented steps for clearing jammed update downloads in [Microsoft's Windows support hub](https://support.microsoft.com/en-us/windows).
