---
title: "Cortana High CPU on Windows 10? How to Fix It"
slug: "how-to-fix-cortana-high-cpu-on-windows-10"
date: "2026-09-14"
categories: ["performance"]
tags: ["cortana", "high cpu", "windows 10", "searchui.exe", "background apps"]
description: "Cortana is spiking CPU on Windows 10 even though you never use the assistant. Learn to disable it properly via Settings, Group Policy, or the registry."
thumbnail: "/images/thumbs/how-to-fix-cortana-high-cpu-on-windows-10.webp"
faqs:
  - q: "Why does Cortana use CPU on Windows 10 when I never open it?"
    a: "On Windows 10, Cortana is deeply integrated with taskbar search — the SearchUI.exe process handles both. It indexes content, fetches suggestions, processes voice-activation listening, and syncs with your Microsoft account in the background. High CPU usually means the search index is looping, suggestion fetching is stuck, or the 'Hey Cortana' listener is active."
  - q: "Will disabling Cortana break Windows 10 search?"
    a: "Disabling Cortana via policy or registry disables the assistant features but leaves local file and app search working. The search box still finds your programs and documents. What stops working are Cortana-specific features: voice assistant, web-answer cards, and personalized suggestions — none of which most users miss."
  - q: "What is the difference between disabling and uninstalling Cortana on Windows 10?"
    a: "Disabling via Group Policy or registry turns off Cortana's functionality while leaving its files in place — easily reversible. Uninstalling via PowerShell removes the app package entirely, which is more thorough but harder to reverse since the package must be re-provisioned. For most users, policy-based disabling achieves the goal with less risk."
  - q: "Does 'Hey Cortana' voice activation waste CPU?"
    a: "Yes, measurably. Always-on voice listening keeps audio processing active continuously, which consumes CPU and battery. If you never use voice commands, turning off 'Hey Cortana' in Cortana's settings is a quick win that reduces background activity with zero downside."
---

Windows 10 shipped with Cortana woven into the operating system — not as an optional app but as part of search itself. The SearchUI.exe process powers both the taskbar search box and the Cortana assistant, which means "Cortana CPU usage" and "search CPU usage" are often the same thing wearing two names. When it spikes to 15–30% CPU while you are doing nothing, the assistant you never asked for is taxing the hardware you paid for.

Unlike Windows 11, where Cortana was retired, Windows 10 retains the full Cortana stack — voice activation, suggestions, cloud integration — and all of it can generate background load. The fixes range from simple toggles to policy-level disablement. Because Cortana and search share a process on Windows 10, the guide also covers taming the search side, since that is frequently the actual source of the CPU burn.

Work through these in order, checking Task Manager after each change.

## Why this happens

- **SearchUI.exe doing double duty:** One process serves both search and Cortana, so assistant background work hides inside search CPU.
- **"Hey Cortana" always listening:** Voice activation keeps audio processing running continuously.
- **Suggestion and web-result fetching:** Continuous fetching of suggestions, news, and web cards burns CPU in the background.
- **Corrupted search index:** A damaged index traps the shared process in re-indexing loops.
- **Microsoft account sync churn:** Syncing Cortana preferences, history, and notebooks across devices adds load.
- **Cortana background permissions:** The app's background execution allowance lets it work while closed.
- **Outdated Windows 10 builds:** Older builds contain SearchUI inefficiencies addressed by later cumulative updates.
- **Timeline and activity history:** The Timeline feature feeds Cortana's backend with continuous activity logging.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm the process and pattern

1. Open Task Manager, sort by CPU, and find **SearchUI.exe** (listed as Search or Cortana).
2. Right-click, Open file location — confirm `C:\Windows\SystemApps\Microsoft.Windows.Cortana_cw5n1h2txyewy`.
3. Observe for five minutes: constant load suggests index or sync loops; spikes on search-box hover suggest suggestion fetching.
4. Test: open Cortana's settings and toggle off "Hey Cortana," then watch CPU for 15 minutes.

The file-location check rules out malware mimicking the name. The pattern tells you where to focus: constant usage means Fixes 4–5 (index, sync), while interactive spikes mean Fixes 2–3 (suggestions, voice). Note your baseline CPU before changing anything so improvements are measurable.

### Fix 2: Turn off "Hey Cortana" and voice activation

1. Click the Cortana/search box, open Settings (gear icon), and turn off **"Hey Cortana"** / voice activation.
2. In Settings, Privacy, Speech, turn off online speech recognition if you do not use dictation.
3. Under Settings, Privacy, Microphone, review which apps have access and trim aggressively.
4. Monitor CPU for 30 minutes — always-on listening was a constant drain for many users.

Voice activation is the most clear-cut waste in the Cortana stack: continuous audio processing for a feature most people never invoke. Disabling it has no effect on typing searches, and the CPU savings are immediate and permanent. This is the first toggle every Windows 10 Cortana troubleshooter should flip.

### Fix 3: Disable Cortana's suggestions and cloud content

1. In the search box settings, turn off Cortana suggestions, web results, and "search highlights"-style content.
2. Go to Settings, Search, Permissions & History, and disable cloud content search.
3. Turn off search history if you do not use it.
4. End the SearchUI task in Task Manager so it restarts fresh, then observe.

The web-connected half of Cortana — suggestions, cards, news, web answers — is the dominant CPU driver, just as with its Windows 11 successor. Cutting it leaves local search intact: your apps, files, and settings still appear instantly. Most users find the search box becomes faster as well as quieter, since it no longer waits on network fetches.

### Fix 4: Rebuild the search index

1. Go to Settings, Search, Searching Windows, Advanced Search Indexer Settings.
2. Click Advanced, then **Rebuild** under Troubleshooting.
3. Allow several hours for completion on large drives — schedule overnight.
4. After completion, monitor SearchUI CPU for a full day.

Because Cortana and search share SearchUI.exe, a corrupted index punishes both. Rebuilding is the definitive fix for the "constant CPU, no trigger" pattern that survives all the toggles. Our [SearchApp.exe high CPU guide](/articles/how-to-fix-searchapp-exe-high-cpu-youtube/) covers the search-UI side of this same process family. If you have already tamed Cortana via our [Windows 11 Cortana guide](/articles/how-to-fix-cortana-high-cpu-on-windows-11/), note the Windows 10 process differs — the fixes rhyme but the process names do not.

### Fix 5: Disable Cortana via Group Policy (Pro)

1. Press `Win + R`, type `gpedit.msc`, navigate to Computer Configuration, Administrative Templates, Windows Components, Search.
2. Set **Allow Cortana** to Disabled.
3. Run `gpupdate /force` and restart.
4. Verify the Cortana settings pages show as managed and SearchUI CPU drops.

Group Policy disablement is the IT-standard method: it turns off the assistant at the policy level while keeping local search functional. It survives updates better than Settings toggles and is instantly reversible. On Pro editions this is the recommended permanent fix — cleaner than killing processes and more durable than toggles.

### Fix 6: Disable Cortana via registry (Home)

1. Open regedit and navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\Windows Search` (create the key if missing).
2. Create DWORD `AllowCortana` set to `0`.
3. Restart the laptop.
4. Confirm Cortana features are off while taskbar search still finds local apps and files.

This is the same policy as Fix 5, written directly for Home editions without gpedit. It is safe, documented, and reversible — delete the value to restore defaults. Microsoft documents policy-backed registry settings in [Windows support](https://support.microsoft.com/en-us/windows). If registry editing makes you nervous, Fix 7's PowerShell approach is an alternative path to the same outcome.

### Fix 7: Remove the Cortana package via PowerShell (thorough)

1. Open PowerShell as administrator.
2. Run `Get-AppxPackage -AllUsers *Microsoft.549981C3F5F10* | Remove-AppxPackage -AllUsers`.
3. Restart and verify no Cortana app remains and search still works for local items.
4. If anything search-related breaks, re-provision via `Get-AppxPackage -AllUsers` restore or an in-place Windows repair.

Package removal is the most thorough option — the assistant is gone, not just disabled. The trade-off is reversibility: reinstalling requires re-provisioning the package. For a Windows 10 machine in its final years of service, where Cortana offers nothing you use, removal is a reasonable permanent cleanup. If Windows Update itself is misbehaving on your machine, the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com/) can supply updates manually.

## Closing

Cortana CPU usage on Windows 10 is really SearchUI.exe doing the assistant's background work — voice listening, suggestions, syncing — on top of search. Turn off voice activation and web content first, rebuild the index if the load is constant, then disable via policy or registry for permanence. Local search survives all of it, and the CPU and battery you reclaim are yours to keep.
