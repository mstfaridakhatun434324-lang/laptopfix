---
title: "How to Fix Cortana High CPU Usage on Asus Laptop"
slug: how-to-fix-cortana-high-cpu-on-asus-laptop
date: 2026-10-13
categories: ["performance"]
tags: ["cortana", "high cpu", "asus laptop", "windows 11", "background apps"]
description: "Cortana spiking CPU on your Asus laptop? Shut down its background activity, disable it properly, or remove it — with Asus-specific tuning included."
thumbnail: "/images/thumbs/how-to-fix-cortana-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "Why does Cortana run at all on my Asus laptop when I never use it?"
    a: "Windows ships Cortana as a preinstalled app with background permissions enabled, and Asus's factory image doesn't change that. Its background tasks — sync checks, voice-activation readiness, tile updates — wake the CPU on schedules whether or not you've ever opened the app. Since Microsoft has retired Cortana as a consumer assistant, there's no functional reason to let it keep running in the background."
  - q: "Does disabling Cortana affect MyASUS or Armoury Crate?"
    a: "Not at all. MyASUS, Armoury Crate, and other Asus utilities are completely separate applications with no dependency on Cortana. Disabling or uninstalling Cortana changes nothing about Asus-specific features like fan profiles, battery health charging, or system diagnostics. The two ecosystems don't interact."
  - q: "What's the difference between disabling and uninstalling Cortana?"
    a: "Disabling (background permission set to Never, plus the Group Policy/registry block) leaves the app installed but inert — it can't run, wake, or update itself into activity. Uninstalling removes the package entirely. Disabling is reversible in seconds and survives most updates; uninstalling is cleaner but a major Windows update can occasionally reinstall it, requiring a repeat."
  - q: "Can Armoury Crate make Cortana's CPU usage worse?"
    a: "Indirectly, yes. Armoury Crate's background services and aggressive performance profiles raise baseline CPU activity, which makes Cortana's periodic background bursts more noticeable and can delay the CPU returning to idle. If you're troubleshooting idle CPU on an Asus laptop, calming both Cortana and Armoury Crate's background behavior together gives the clearest result."
---

Same symptom, different brand: Cortana is burning CPU on your Asus laptop despite never being used. The core fix is identical to any Windows 11 machine — Cortana is just an app now, and apps can be disabled — but Asus laptops have their own background ecosystem (Armoury Crate, MyASUS services) that interacts with idle CPU behavior. This guide handles Cortana itself first, then tunes the Asus side so background activity as a whole settles down.

You don't need Cortana for anything in Windows 11. Windows Search, voice typing, and the Start menu all work without it. So the approach is simple: measure the drain, cut Cortana's background lifelines one by one, and verify idle CPU returns to near zero.

## Why this happens

- **Default background permissions:** Cortana ships allowed to run background tasks on Asus's factory image.
- **Voice activation readiness:** The "Hey Cortana" listener keeps audio infrastructure warm.
- **Scheduled background wakes:** Sync and maintenance tasks fire periodically regardless of use.
- **Armoury Crate baseline activity:** Asus's own services raise idle CPU, amplifying Cortana's bursts.
- **MyASUS background checks:** Update and health checks waking alongside Cortana's tasks.
- **App updates restoring permissions:** Cortana updates can silently re-enable background activity.
- **Corrupted app state:** A damaged install can loop background tasks instead of finishing them.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Measure Cortana's actual CPU cost

Open Task Manager → Processes, sort by CPU, and watch for two full minutes — catch both the baseline and any periodic spikes, noting the process name (Cortana, or SearchUI.exe on older builds). Switch to the Startup apps tab and check for Cortana entries launching at boot. Also glance at overall idle CPU: if the system idles above 5–10% with Cortana as only part of it, Asus background services are contributing too (addressed in Fix 6). Write down the numbers — you'll compare against them after each fix to prove what worked.

1. Sort Task Manager by CPU and observe for two minutes.
2. Identify Cortana's baseline vs. spike pattern.
3. Check Startup apps for Cortana entries.
4. Note total idle CPU as your before-measurement.

### Fix 2: Cut background permissions and terminate the app

Go to **Settings → Apps → Installed apps → Cortana → Advanced options**: set background permission to Never, then click Terminate to kill the running instance and Repair to fix corrupted state. This is the single most effective step — scheduled background wakes are the primary CPU source, and Never blocks all of them. Monitor Task Manager for an hour of normal use: if Cortana stays absent and idle CPU dropped, you're done. If it reappears after a reboot, continue to the policy-level block in Fix 4.

1. Set Cortana's background permission to Never.
2. Terminate the running instance, then Repair.
3. Monitor for an hour of normal use.
4. Continue if Cortana reappears after reboot.

### Fix 3: Disable voice activation and speech services

In **Settings → Privacy & security → Voice activation**, disable voice activation for Cortana or turn it off system-wide — the warm audio pipeline serves no purpose if you never use voice commands. Under **Privacy & security → Speech**, disable online speech recognition unless you dictate text. These changes remove Cortana's audio-related background footprint entirely. Combined with Fix 2, Cortana now has no legitimate reason to wake the CPU — anything remaining is either a policy gap or a corrupted install, both handled next.

1. Turn off voice activation for Cortana.
2. Disable online speech recognition if unused.
3. Restart and check Task Manager for Cortana processes.
4. Proceed to the policy block if anything persists.

### Fix 4: Block Cortana with Group Policy or Registry

For a persistent, update-resistant block: on Pro editions use `gpedit.msc` → **Computer Configuration → Administrative Templates → Windows Components → Search** → set "Allow Cortana" to Disabled. On Home, create `HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search\AllowCortana` (DWORD) = 0. This stops Cortana from executing at all, so future app updates can't silently restore its background activity. Restart after applying. Microsoft documents Cortana configuration in the [Windows support hub](https://support.microsoft.com/en-us/windows). Reversal is trivial: set the policy back to Not Configured or delete the registry value.

1. Apply the Allow Cortana = Disabled policy or registry value.
2. Restart the laptop.
3. Verify Cortana is absent from Task Manager.
4. Note the reversal steps in case you ever need them.

### Fix 5: Uninstall Cortana completely

For the nuclear option, remove the package: right-click Cortana in Start → Uninstall, or run `Get-AppxPackage -allusers Microsoft.549981C3F5F10 | Remove-AppxPackage` in admin PowerShell. Verify it's gone from Installed apps and doesn't return after a reboot. Windows Search and Start-menu search are unaffected — they're separate systems. If a future feature update reinstalls Cortana, just repeat the command; it takes ten seconds. Pair this decision with the [Dell Cortana guide](/articles/how-to-fix-cortana-high-cpu-on-dell-laptop/) only if you're comparing brand-specific notes — the uninstall itself is identical.

1. Uninstall via Start menu or PowerShell.
2. Confirm removal in Installed apps.
3. Reboot and verify no Cortana processes.
4. Re-run the command if a future update restores it.

### Fix 6: Quiet Asus's own background layer

With Cortana handled, address the Asus side of idle CPU. Open Armoury Crate and switch from Turbo/Performance to the Silent or Balanced profile for everyday use — aggressive profiles keep clocks high, which makes every background burst cost more. In **Task Manager → Startup apps**, disable Asus utilities you don't actively use (keep MyASUS if you rely on it for updates). Open MyASUS → System Diagnostics and turn off overly frequent automated checks. Finally, update Asus system drivers via MyASUS — outdated ATK/Armoury components are a known source of background CPU churn. Re-measure idle CPU: the combination of a silenced Cortana and a calmed Asus layer should land you at 1–3% idle.

1. Switch Armoury Crate to Silent/Balanced for daily use.
2. Disable unused Asus startup utilities.
3. Reduce MyASUS automated check frequency.
4. Update Asus system drivers and re-measure idle CPU.

## Closing

Cortana on an Asus laptop is two problems stacked: the app's own background activity, and Asus's background layer making every burst worse. Revoke Cortana's background permission, block it via policy or uninstall it, then calm Armoury Crate and MyASUS. Idle CPU drops to where it should be, the fan stays quiet, and an assistant you never used stops taxing a laptop you use every day. The [general slow-laptop speed-up guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) covers the wider background cleanup.
