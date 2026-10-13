---
title: "Cortana Using High CPU on Windows 11? Shut It Down for Good"
slug: how-do-i-fix-cortana-high-cpu-windows-11
date: 2026-10-06
categories: ["performance"]
tags: ["cortana", "high cpu", "windows 11", "background apps", "disable cortana"]
description: "Cortana burning CPU in the background on Windows 11 even though you never use it? Disable it properly via Settings, Group Policy, or the registry."
thumbnail: "/images/thumbs/how-do-i-fix-cortana-high-cpu-windows-11.webp"
faqs:
  - q: "Why is Cortana running if I never opened it?"
    a: "On Windows 11, Cortana's remnants are tied into the search and shell experience rather than being a standalone app you launch. Background processes related to voice services and search integration can wake and consume CPU, especially after updates that re-enable components. Even users who never clicked the Cortana icon can see its processes active in Task Manager, doing indexing-adjacent work or checking for voice activation triggers."
  - q: "Is it safe to disable Cortana completely?"
    a: "Yes. Cortana is deprecated as a consumer assistant and disabling it does not affect Windows Search, the Start menu, or system stability. The supported methods are toggling it off in Settings, using Group Policy (Pro editions) to block it, or a documented registry value. Windows continues to update and function normally — you are simply preventing an unused service from consuming CPU and memory."
  - q: "Will disabling Cortana break Windows Search?"
    a: "No. Windows Search is powered by SearchHost.exe and the search indexer, which are separate from Cortana. Disabling Cortana via policy or registry leaves search fully functional — Start menu search, File Explorer search, and search highlighting all keep working. If search itself is slow or CPU-hungry, that is a separate issue covered in our search indexer troubleshooting guides."
  - q: "Cortana keeps coming back after Windows updates. How do I stop that?"
    a: "Feature updates can reset per-user Settings toggles, which is why the Settings switch alone is unreliable long-term. The Group Policy setting (Computer Configuration > Administrative Templates > Windows Components > Search > Allow Cortana > Disabled) or its registry equivalent survives updates because it is a machine-level policy. Re-apply and verify after each feature update if you used the registry method on Home edition."
---

Cortana is the houseguest who never left. Microsoft deprecated the consumer assistant years ago, yet its processes still wake up on Windows 11 systems, burn CPU in Task Manager, and generally act like they pay rent. If you've spotted Cortana-related processes chewing cycles on a laptop where nobody has said "Hey Cortana" since 2019, you're not imagining it — and the fix is to disable it at the policy level so it stays off.

The key insight: the toggle in Settings is a suggestion; Group Policy (or its registry equivalent on Home edition) is an instruction. Updates routinely reset the gentle toggle but respect the policy. This guide covers all three levels — the quick Settings switch, the durable policy/registry method, and cleanup of the leftover scheduled tasks and startup entries — plus what to do when a *different* process is the real CPU hog wearing Cortana's clothes. If your actual problem is search being slow rather than Cortana specifically, see [SearchHost.exe high CPU troubleshooting](/articles/searchhost-exe-high-cpu-troubleshooting/).

## Why this happens

- **Voice activation services waking**: Background listeners checking for wake words consume CPU in bursts.
- **Search integration hooks**: Cortana components tied into the shell doing indexing-adjacent work.
- **Updates re-enabling components**: Feature updates reset user-level toggles and reinstall app packages.
- **Scheduled tasks firing**: Cortana maintenance tasks running on schedules regardless of use.
- **Corrupt app package looping**: A damaged Cortana/Search app package retrying failed operations.
- **Settings toggle not sticking**: Per-user Settings changes overridden by defaults or sync.
- **Confused identity with SearchHost**: Users misattribute SearchHost.exe CPU to Cortana since both relate to "search."
- **Enterprise policies partially applied**: Domain-joined machines with conflicting Cortana/search policies causing retry loops.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm it's actually Cortana using the CPU

Make sure you're blaming the right process.

1. Open **Task Manager** > **Processes** tab and look for **Cortana** — note its CPU over a minute. Also check the **Details** tab for `SearchHost.exe`, `SearchIndexer.exe`, and ` Cortana`-related entries separately.
2. If **SearchHost.exe** is the hot one rather than Cortana, your problem is Windows Search, not the assistant — jump to [SearchHost.exe troubleshooting](/articles/searchhost-exe-high-cpu-troubleshooting/) instead, since disabling Cortana won't help.
3. Right-click the Cortana process > **Open file location** to verify it's the genuine system component and not malware wearing the name.
4. Check the **Startup apps** tab in Task Manager for Cortana entries set to Enabled.
5. Only proceed with Cortana-specific fixes if a genuine Cortana process is actually consuming the CPU; otherwise you're fixing the wrong thing.

### Fix 2: Disable Cortana in Settings (quick but soft)

The easy switch — do it, but don't stop here.

1. Open **Settings** > **Apps** > **Installed apps**, search for **Cortana**, click the **...** menu > **Advanced options**.
2. Under **Background apps permissions**, set it to **Never**, and under **Runs at log-in**, turn the toggle **Off**.
3. Go to **Settings** > **Privacy & security** > **Speech** and turn off **Online speech recognition** if you don't use voice features — this quiets related background activity.
4. Check **Settings** > **Bluetooth & devices** and any voice-activation settings; disable wake-word listening.
5. Restart and verify in Task Manager. This often works for weeks — until the next feature update resets it, which is why Fix 3 exists.

### Fix 3: Block Cortana with Group Policy or registry (durable)

The method that survives updates.

1. **Windows 11 Pro/Enterprise**: press **Win + R**, type `gpedit.msc`, and navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Search**.
2. Double-click **Allow Cortana**, set it to **Disabled**, click OK. This is a machine policy — updates respect it.
3. **Windows 11 Home** (no gpedit): open an elevated Command Prompt and run: `reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows\Windows Search" /v AllowCortana /t REG_DWORD /d 0 /f` — this writes the exact same policy value Group Policy would set.
4. Restart the laptop (a full restart, not Fast Startup shutdown) so the policy applies.
5. Verify: Cortana processes should no longer appear in Task Manager after boot, and the Settings toggles from Fix 2 should show as managed. Re-check after the next feature update; the policy value occasionally needs re-applying on Home edition.

### Fix 4: Clean up scheduled tasks and startup remnants

Kill the stragglers that the policy doesn't cover.

1. Open **Task Scheduler** (`taskschd.msc`) and browse **Task Scheduler Library** > **Microsoft** > **Windows** for Cortana or voice-activation-related tasks.
2. Right-click any Cortana maintenance tasks > **Disable** — don't delete them; disabling is reversible and survives updates better.
3. Open Task Manager > **Startup apps** and disable any remaining Cortana or voice-service entries.
4. Check **Settings** > **Apps** > **Installed apps** for the Cortana app package itself — on current Windows 11 builds you can **Uninstall** it; the policy in Fix 3 covers the OS-integrated components that can't be uninstalled.
5. Also review [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) generally — Cortana is rarely the only unused thing launching at boot.

### Fix 5: Repair the app package if it's looping

Sometimes high CPU means a corrupted component retrying forever.

1. In **Settings** > **Apps** > **Installed apps** > **Cortana** > **...** > **Advanced options**, click **Repair** first — this reinstalls the package's files without touching your data.
2. If Repair doesn't help, click **Reset** on the same page — this clears the app's local state, which fixes corrupted caches that cause CPU loops.
3. Run `sfc /scannow` from an elevated prompt to check for broader system file corruption affecting shell components.
4. Check **Settings** > **Windows Update** for pending updates — a half-applied update can leave Cortana components in a broken state that the completed update resolves.
5. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the Settings repair/reset flow if you need the official reference.

### Fix 6: Handle the enterprise / domain-joined case

For work laptops where policies fight each other.

1. If your laptop is domain-joined or managed (school/work), local Group Policy edits may be overridden by domain policy — check with your IT admin before fighting it.
2. Run `gpresult /h C:\gpreport.html` from a prompt and open the report to see which policies actually apply to Cortana/Search — conflicting Allow/Block settings cause exactly the "keeps coming back" behavior.
3. Don't edit the registry on a managed machine to work around domain policy; it will be reverted and may flag compliance tooling.
4. Ask IT whether Cortana is intentionally enabled (some orgs use it with Microsoft 365) — if so, the CPU usage may be legitimate sync work, and the fix is scheduling, not disabling.
5. For unmanaged personal machines, the Fix 3 policy is the final word — combined with Fixes 2 and 4, Cortana stays quiet permanently.

## Closing

Cortana high CPU is an annoyance with a clean solution: verify it's really Cortana (Fix 1), apply the quick Settings toggles (Fix 2), then lock it down with the machine-level policy (Fix 3) so updates can't resurrect it. Total time: about fifteen minutes. Your Task Manager — and your battery — will thank you, and Windows Search keeps working exactly as before.
