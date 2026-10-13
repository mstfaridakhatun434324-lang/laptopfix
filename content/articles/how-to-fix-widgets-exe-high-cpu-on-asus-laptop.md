---
title: "Widgets.exe High CPU on ASUS Laptop? Fix It Fast"
slug: how-to-fix-widgets-exe-high-cpu-on-asus-laptop
date: 2026-10-11
categories: ["performance"]
tags: ["widgets.exe", "high cpu", "asus laptop", "windows 11"]
description: "Widgets.exe burning CPU on your ASUS laptop? Fix the feed loops, Armoury Crate conflicts, and settings behind Widgets high CPU."
thumbnail: "/images/thumbs/how-to-fix-widgets-exe-high-cpu-on-asus-laptop.webp"
faqs:
  - q: "Why is Widgets.exe using CPU on my ASUS laptop when I never open widgets?"
    a: "Widgets.exe runs in the background regardless of whether you open the board — it refreshes weather, news, and feed content on a schedule. On ASUS laptops, the issue is often compounded: Armoury Crate and MyASUS utilities add their own background activity, and Windows updates frequently re-enable Widgets after you turned it off. The process is Chromium-based, so a stuck feed is like a frozen browser tab burning CPU forever."
  - q: "Does Armoury Crate conflict with Windows Widgets?"
    a: "Not directly, but they compound each other's load: Armoury Crate runs its own monitoring, overlays, and update checks while Widgets.exe churns feeds in the background. On ASUS gaming laptops the combined background CPU can be noticeable. The fix isn't choosing one — it's quieting both: disable Widgets background activity and set Armoury Crate to a balanced profile instead of letting it poll aggressively."
  - q: "Can I uninstall Widgets.exe completely on ASUS laptops?"
    a: "You can uninstall the Windows Web Experience Pack (which provides Widgets.exe) via Settings > Apps > Installed apps, and ASUS-specific software won't miss it. Alternatively, disable it via Group Policy (Allow widgets > Disabled) or the registry. None of ASUS's utilities — Armoury Crate, MyASUS, or Aura — depend on Windows Widgets, so removal is safe."
  - q: "Will disabling Widgets affect MyASUS or Armoury Crate?"
    a: "No. MyASUS, Armoury Crate, and other ASUS utilities are independent desktop applications that don't use the Windows Widgets platform. Disabling or uninstalling Widgets only removes the taskbar weather/news panel. Your ASUS fan controls, performance profiles, and system diagnostics keep working exactly as before."
---

ASUS laptops run a busy background ecosystem — Armoury Crate, MyASUS, Aura lighting services — and Windows' own `Widgets.exe` adds to the pile. When Widgets.exe starts burning 10–30% CPU on an ASUS machine, it's usually a stuck content feed, but the ASUS software stack can amplify the symptoms and make diagnosis confusing: you see high total CPU and don't know which vendor to blame.

This guide separates the two and quiets both. Start with Widgets itself — that's the named culprit — and measure before and after each change so you know what's actually helping. None of ASUS's utilities depend on the Windows Widgets platform, so you can be aggressive with Widgets without breaking anything ASUS.

For the general Widgets board guide, see [Widgets board high CPU](/articles/what-to-do-if-widgets-board-high-cpu-windows-11/); for ASUS fan noise that often accompanies this, [fixing a non-working fan](/articles/best-way-to-fix-laptop-fan-not-working/).

## Why this happens

- **Stuck Widgets feed loop**: A news/weather feed failing and retrying keeps the Chromium renderer busy.
- **Windows Update re-enabling Widgets**: Updates turn the taskbar Widgets toggle back on.
- **Armoury Crate background polling**: Aggressive hardware monitoring adding its own CPU load alongside Widgets.
- **MyASUS update checks**: Background update and diagnostics activity compounding the load.
- **Buggy Web Experience Pack version**: A bad Store update to the Widgets platform itself.
- **Third-party widgets**: Added widgets with broken refresh logic.
- **Chromium renderer overhead**: Each widget is effectively a background browser tab.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Confirm Widgets.exe vs. ASUS processes

Separate the culprits before changing anything.

1. Open **Task Manager** > **Details** tab, sort by CPU — identify exactly how much `Widgets.exe` uses vs. ASUS processes (`ArmouryCrate`, `AsusCertService`, `Aura`).
2. If Widgets.exe dominates, proceed with the Widgets fixes below; if ASUS processes dominate, skip to Fix 6.
3. Right-click `Widgets.exe` > **Open file location** to confirm it's the genuine Microsoft binary.
4. Disconnect from the network for 2 minutes as a test — a CPU drop implicates a feed refresh loop.
5. Note baseline numbers so you can measure improvement after each fix.

### Fix 2: Disable the Widgets taskbar entry

The fastest relief for the named problem.

1. Right-click the taskbar > **Taskbar settings** > toggle **Widgets** to **Off**.
2. Check Task Manager after a reboot — Widgets.exe should be gone or idle on most systems.
3. If it persists, press **Win + W** to open the board once, remove all third-party widgets (**...** > **Remove widget**), and sign out of the Widgets account.
4. Leave the toggle off for a day and compare CPU against your baseline.
5. This alone resolves the majority of Widgets.exe cases.
6. If Widgets.exe creeps back after a Windows update, that's the known re-enable behavior — Fix 5's policy block makes the off-state permanent.

### Fix 3: Block Widgets background activity

Stop it from running when the board is closed.

1. Open **Settings** > **Apps** > **Installed apps** > **Windows Web Experience Pack** > **...** > **Advanced options**.
2. Set **Background apps permissions** to **Never**.
3. In **Task Manager** > **Startup apps**, disable anything Widgets-related.
4. Reboot and verify in Task Manager's Details tab that Widgets.exe stays dead at idle.
5. If it still respawns, proceed to the policy-level disable in Fix 5.

### Fix 4: Update or reinstall the Web Experience Pack

Fix a buggy Widgets platform.

1. Open **Microsoft Store** > **Library** > **Get updates** — install any **Windows Web Experience Pack** update.
2. If none is offered, uninstall the pack via **Settings** > **Apps** > **Installed apps** > **Uninstall**.
3. Reboot and test — Windows runs fine without it; reinstall from the Store only if you want the feature back.
4. After reinstall, monitor CPU for a day — platform-version bugs vanish with a fresh copy.
5. Keep the Store's auto-updates on for this component, or check manually monthly.

### Fix 5: Disable Widgets via policy or registry

Make the off-state permanent and update-proof.

1. Pro/Enterprise: `gpedit.msc` > **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Widgets** > **Allow widgets** > **Disabled**.
2. Home: `regedit` > `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Dsh` > DWORD **AllowNewsAndInterests** = `0`.
3. Reboot — the Widgets toggle vanishes from Taskbar settings entirely.
4. Verify Widgets.exe never appears in Task Manager, even after Windows updates.
5. Reverse by deleting the value or setting the policy to **Not Configured**; policy docs at [Microsoft support](https://support.microsoft.com/en-us/windows).

### Fix 6: Quiet Armoury Crate and MyASUS background load

Address the ASUS-side amplifier.

1. Open **Armoury Crate** and switch from Turbo/Performance to **Balanced** or **Silent** profile for everyday use.
2. In Armoury Crate settings, disable **automatic updates** and reduce hardware-monitoring poll frequency if options exist.
3. Open **MyASUS** > settings and turn off background diagnostics and automatic driver checks you don't need.
4. In **Task Manager** > **Startup apps**, disable ASUS utilities you rarely open manually (keep essential hotkey services).
5. Re-measure total idle CPU — the combined reduction from Widgets + ASUS tuning is often dramatic.

### Fix 7: Clean up the overall background load

Finish with a general background audit.

1. Open **Settings** > **System** > **Notifications** and disable Windows tips and suggestions.
2. Set lock screen to **Picture** instead of **Windows spotlight** (**Settings** > **Personalization** > **Lock screen**).
3. Work through [disabling startup programs](/articles/how-to-disable-startup-programs-windows-11/) for the full pass.
4. Install pending **Windows Update** packages — platform fixes for background CPU ship regularly.
5. If slowness persists beyond background CPU, see [speeding up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/).

## Closing

On ASUS laptops, Widgets.exe high CPU is usually a stuck feed — but the ASUS software stack makes the total background load worse than the sum of its parts. Kill the Widgets board, block its background activity, calm Armoury Crate down to a balanced profile, and the idle CPU (and the fan) settles. Nothing ASUS-specific depends on Widgets, so disabling it is pure win — and with the policy block in place, Windows updates can't silently resurrect the problem.
