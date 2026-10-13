---
title: "How to Fix Battery Saver Greyed Out in Windows"
slug: how-to-fix-battery-saver-greyed-out-youtube
date: 2026-09-11
categories: ["battery"]
tags: ["battery saver", "greyed out", "windows settings"]
description: "Battery saver toggle greyed out and unclickable? Fix it with power plan, policy, driver, and registry checks."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-greyed-out-youtube.webp"
faqs:
  - q: "Why is battery saver greyed out in Windows 11?"
    a: "The usual reasons: the laptop is currently plugged in (battery saver only engages on battery), a group policy or MDM setting disabled it, the power plan is corrupted, or a driver issue hides the toggle. On some systems the toggle is intentionally unavailable while charging — unplug and check again first."
  - q: "Can I turn on battery saver while plugged in?"
    a: "By design, Windows only auto-engages battery saver on battery power, and the manual toggle is often disabled while charging. The workaround is the 'turn on automatically' threshold plus, on some builds, enabling it via Settings before plugging in. It's a design choice, not a bug."
  - q: "Does battery saver actually extend battery life?"
    a: "Yes, measurably — typically 10-20% more runtime. It dims the screen, throttles background activity, reduces visual effects, and limits push notifications. It's most effective combined with lowering screen brightness manually, which remains the biggest single lever."
  - q: "Is battery saver the same as a power plan?"
    a: "No. Power plans (balanced, best performance, best power efficiency) set the baseline behavior; battery saver is an additional low-power mode that kicks in on top, either automatically at a threshold or manually. They stack — best power efficiency plus battery saver is the maximum-runtime combination."
---

You open Settings, find Battery saver, and the toggle is greyed out — mocking you exactly when you need it. Before diving into fixes, check the obvious: if the laptop is plugged into the charger right now, that's probably the whole story. Windows deliberately disables the battery saver toggle while on AC power on many builds. Unplug, wait a few seconds, and look again — if the toggle wakes up, there was never a problem.

If it's still greyed out on battery power, then something is genuinely blocking it: a policy, a corrupted power plan, a driver issue, or a registry setting. This guide works through those in order. For the related "battery saver doesn't do anything" complaint, see [what to do if battery saver is not working](/articles/what-to-do-if-battery-saver-not-working-on-laptop/).

## Why this happens

- **Plugged in:** By design, the toggle is unavailable on AC power on many Windows builds — the most common "cause."
- **Group policy / MDM:** Work or school machines often have battery saver disabled by administrator policy.
- **Corrupted power plan:** A damaged power scheme can hide or disable the battery saver UI.
- **Driver issues:** Display or chipset driver problems can break the power UI that hosts the toggle.
- **Registry misconfiguration:** A flipped policy registry value disables the feature silently.
- **Windows edition quirks:** Some battery saver behaviors differ between Home and Pro, and between Windows 10 and 11 builds.

## How to fix it

Work through these in order — start with the two-minute checks.

### Fix 1: Unplug and retest (the 10-second fix)

Eliminate the by-design explanation.

1. Unplug the charger completely and wait 10-15 seconds for Windows to register battery power.
2. Open **Settings > System > Power & battery > Battery saver** and check the toggle.
3. If it's now active, that was the entire issue — Windows gates the toggle on AC power.
4. While unplugged, you can also turn it on manually and it will stay on until you plug back in.
5. If it's still greyed out on battery, continue — something is really blocking it.

### Fix 2: Check the automatic threshold setting

Sometimes the toggle is fine but the automation is misconfigured.

1. In **Battery saver** settings, check **Turn battery saver on automatically at** — set it to **20%** or higher.
2. If the dropdown itself is greyed out, that's the same blocking issue — continue to the policy checks.
3. Test by setting the threshold above your current battery level (temporarily) and watching whether saver engages on its own.
4. Note: automatic engagement only happens on battery power, never while charging.
5. If automation works but the manual toggle doesn't, the block is UI-specific — the plan reset in Fix 4 often clears it.

### Fix 3: Check for group policy or MDM control

Work machines play by admin rules.

1. Press **Win + R**, type `gpedit.msc` (Pro/Enterprise only), and navigate to **Computer Configuration > Administrative Templates > System > Power Management**.
2. Look for policies controlling battery saver / energy saver and set any configured ones to **Not Configured** (if you're the admin).
3. On Home edition (no gpedit), check the registry: `HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Power\PowerSettings` — unexpected values here indicate policy control.
4. Check **Settings > Accounts > Access work or school** — an enrolled device may receive power policies from the organization.
5. If it's a work/school machine and policy-controlled, ask your IT admin — bypassing management policy isn't advisable.

### Fix 4: Reset the power plans to defaults

Fix a corrupted power scheme.

1. Open an elevated Command Prompt or Terminal and run `powercfg /restoredefaultschemes` — this rebuilds all power plans from defaults.
2. Reboot and recheck the battery saver toggle on battery power.
3. This also fixes the related issue where the **Power mode** slider misbehaves — they share the same underlying scheme data.
4. After the reset, reapply your preferred settings (sleep timers, etc.) since defaults overwrite customizations.
5. If you had a custom OEM power plan, check the manufacturer's app to restore its recommended plan afterward.

### Fix 5: Update display and chipset drivers

Repair the UI and power stack underneath the toggle.

1. Open **Device Manager > Display adapters**, right-click your GPU, and **Update driver**.
2. Update chipset drivers under **System devices**, or download the latest from your OEM's support site.
3. Run **Windows Update** and install all pending updates, including optional driver updates.
4. Reboot and test the toggle on battery again.
5. Driver-level power UI bugs are a known cause of greyed-out saver controls, especially after major Windows updates.

### Fix 6: Check the registry values directly

For when policy isn't the cause but the registry is wrong.

1. Press **Win + R**, type `regedit`, and navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\CloudStore` — corruption here can break Settings UI elements (back up the key first via File > Export).
2. More relevantly, check `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PolicyManager\current\device\Power` for saver-related policy values set to disabled.
3. Don't delete keys blindly — export before changing, and only modify values you understand.
4. A safer alternative: create a new local user account and check the toggle there — if it works in the new account, your user profile's settings store is corrupted, and migrating to the new account fixes it.
5. If registry editing feels risky, the in-place Windows repair in Fix 7 achieves similar results safely.

### Fix 7: Repair Windows as the last resort

When the block survives everything else.

1. Go to **Settings > System > Recovery** and use **Fix problems using Windows Update** (Windows 11) — this reinstalls Windows while keeping files and apps.
2. Alternatively, run `sfc /scannow` followed by `DISM /Online /Cleanup-Image /RestoreHealth` in an elevated prompt to repair system file corruption.
3. After repair, verify the toggle on battery power before reinstalling anything else.
4. If it works, reinstall apps one batch at a time — a third-party "optimizer" or "tweaker" may have been the original culprit.
5. Microsoft's official battery-saver documentation is at [Microsoft Support](https://support.microsoft.com/en-us/windows). Once the toggle works, pair it with hunting down [which apps are draining your battery](/articles/how-can-i-find-which-app-is-draining-battery/) — saver mode plus fewer background hogs is the real runtime win.

## Closing

Nine times out of ten, a greyed-out battery saver toggle is either the plugged-in design behavior or a policy/plan glitch — both fixed in minutes. Work the list in order, and by the time you reach the Windows repair step, you'll either have a working toggle or a confirmed system-level issue worth the repair install. Either way, you'll have your battery saver back for the next long day away from an outlet.
