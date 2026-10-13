---
title: "Disable Superfetch (SysMain) the Right Way on Windows"
slug: best-way-to-disable-superfetch-sysmain
date: 2026-09-30
categories: ["performance"]
tags: ["disable superfetch", "disable sysmain", "windows services", "disk fix"]
description: "The correct way to disable Superfetch/SysMain on Windows 10 and 11: Services, registry, verification, and what to do if it returns."
thumbnail: "/images/thumbs/best-way-to-disable-superfetch-sysmain.webp"
faqs:
  - q: "What's the correct way to disable Superfetch on Windows 11?"
    a: "On Windows 11 the service is named SysMain. Open services.msc, double-click SysMain, click Stop, set Startup type to Disabled, and restart. For permanence, also set the EnableSuperfetch registry value to 0 under HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters. Verify afterward in Task Manager that Service Host: SysMain no longer consumes disk."
  - q: "Should I use Disabled or Manual startup type?"
    a: "Use Disabled. Manual means Windows can still start the service when something requests it, which allows the disk storms to return unexpectedly. Disabled prevents all automatic starts. The only reason to prefer Manual is if you want to experiment with the service occasionally — for a permanent fix, Disabled is correct."
  - q: "Will disabling Superfetch affect Windows Update?"
    a: "No. Superfetch/SysMain is purely a preloading optimization service with no role in Windows Update, security, or system stability. Updates download, install, and function identically with it disabled. The services are completely independent — disabling one has zero effect on the other."
  - q: "How do I know the disable actually worked?"
    a: "Restart your laptop, open Task Manager > Processes sorted by Disk, and confirm Service Host: SysMain no longer appears. Then watch Performance > Disk for 10 minutes after boot — Active time should no longer pin at 100%. As a final check, run 'sc query SysMain' in an elevated prompt; it should report STOPPED with the service set to DISABLED."
---

There are a dozen ways to disable Superfetch/SysMain floating around the internet, and half of them are wrong — setting it to Manual instead of Disabled, editing the wrong registry key, or using sketchy "optimizer" tools that change twenty things at once. Done wrong, the service comes back after the next update and you're troubleshooting the same 100% disk problem again. Done right, it's a two-minute job that stays done.

This is the right way: the correct service setting, the registry lock that survives updates, proper verification, and the re-check routine. For the diagnostic background, see [troubleshooting Superfetch](/articles/troubleshoot-superfetch-high-disk-usage/) and [SysMain high disk](/articles/sysmain-high-disk-usage-troubleshooting/).

## Why this happens

- **Service set to Manual instead of Disabled**: Windows restarts it on demand — the most common "it came back" cause.
- **Feature updates reset services**: Major Windows updates restore SysMain to its default Automatic state.
- **Wrong registry key edited**: Guides pointing at obsolete keys leave the real setting untouched.
- **"Optimizer" tools reverting changes**: Tune-up utilities often re-enable services they consider "should be on."
- **Confusion between Superfetch and SysMain**: Disabling one name on a system that uses the other leaves the real service running.
- **Prefetch folder left intact**: Stale cache data can cause issues if the service ever restarts.
- **Never verified after reboot**: The disable is only real if it survives a restart — many skip this check.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify the correct service name

Know what you're disabling.

1. Press **Win+R**, type `services.msc`, press Enter.
2. Look for **SysMain** — that's the name on Windows 10 (1809+) and all of Windows 11. Its description mentions Superfetch.
3. On older Windows 10 builds you may see **Superfetch** directly — same service, old name.
4. Note the current **Status** (Running?) and **Startup Type** (Automatic?) — this is your "before" state.
5. There's only one of these — if you see both names, you're on a transitional build; disable SysMain.

### Fix 2: Disable via Services — the correct settings

The core procedure, done right.

1. Double-click **SysMain** in the Services console.
2. Click **Stop** and wait for the service to halt — the Status column should clear.
3. Set **Startup type** to **Disabled** — not Manual, not Automatic (Delayed Start). Disabled.
4. Click **Apply**, then **OK**.
5. Do not close the console yet — you'll verify in Fix 4 after a restart.

### Fix 3: Lock it in the registry

The step that makes it survive updates.

1. Press **Win+R**, type `regedit`, and navigate to:
   `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters`
2. Find or create **EnableSuperfetch** (DWORD 32-bit) and set its value to `0`.
3. Find or create **EnablePrefetcher** (DWORD 32-bit) and set it to `0` as well.
4. Back up first: right-click the PrefetchParameters key > **Export**, save the .reg file somewhere safe.
5. These values are what the Services console manipulates — setting them directly ensures the intent is recorded at the lowest level.

### Fix 4: Verify after a full restart

Prove it worked — this step is non-optional.

1. **Restart** the laptop (full restart, not shutdown-with-fast-startup — or hold Shift while clicking Shut down).
2. After boot, open an elevated Command Prompt and run `sc query SysMain` — expect STATE: STOPPED.
3. Open Task Manager > **Processes**, sort by **Disk** — confirm no **Service Host: SysMain** entry during the post-boot period.
4. Watch **Performance** > **Disk** for 10 minutes — Active time should spike briefly, not camp at 100%.
5. If the service is running again, something reverted it — check for optimizer tools or group policies (Fix 6).

### Fix 5: Clean up the leftovers

Remove what the disabled service leaves behind.

1. Open `C:\Windows\Prefetch` (Win+R, accept the admin prompt) and delete its contents — stale patterns serve no purpose now.
2. Run Disk Cleanup (`cleanmgr.exe`) > **Clean up system files** for the temp-file categories.
3. Check **Task Scheduler** > **Microsoft** > **Windows** > **Application Experience** — the prefetch-related tasks are harmless when the service is disabled, but you can disable them for tidiness.
4. Empty the Recycle Bin and restart once more for a clean final state.
5. Re-run the Fix 4 verification — belt and suspenders.

### Fix 6: Handle Group Policy and optimizer interference

When something keeps turning it back on.

1. Check for tune-up utilities (CCleaner, "optimizers," manufacturer tools) with "service optimization" features — disable those features or the tools.
2. On Pro editions, check `gpedit.msc` > **Computer Configuration** > **Windows Settings** > **Scripts** — logon scripts can start services.
3. In enterprise or school laptops, Group Policy may enforce the service — check with your IT admin rather than fighting policy.
4. After each Windows **feature update**, re-verify with Fix 4's steps — updates are the most common legitimate resetter.
5. Keep a note of this article's Fix 2–3 steps somewhere — reapplying them after a feature update takes 60 seconds. Microsoft documents service management on [Windows support](https://support.microsoft.com/en-us/windows).

### Fix 7: Decide whether to ever re-enable

The honest assessment of the tradeoff.

1. On **SSDs**: leave it disabled permanently — there's no meaningful benefit to re-enabling, ever.
2. On **HDDs**: try two weeks disabled and note app launch times for your most-used programs — if you genuinely feel a slowdown, re-enable and set the registry to app-preloading-only.
3. To re-enable: Services > SysMain > **Automatic**, Start the service, registry values back to `3`.
4. If disk usage returns to 100% after re-enabling, the answer is clear — the tradeoff isn't worth it on your hardware.
5. For the bigger picture of disk performance, our [100% disk guide](/articles/how-to-fix-windows-11-high-disk-usage-on-startup/) and [slow laptop guide](/articles/laptop-running-slow-windows-11-how-to-speed-up/) cover the other levers.

## Closing

Disabling Superfetch/SysMain the right way is a small procedure with outsized importance: Disabled (not Manual), registry locked, verified after restart, and re-checked after feature updates. It's two minutes of precision that ends the 100%-disk problem instead of postponing it. Do it once, do it right, verify it stuck.
