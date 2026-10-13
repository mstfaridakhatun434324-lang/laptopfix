---
title: "How to Fix Battery Saver Not Working on Windows 11 24H2"
slug: how-to-fix-battery-saver-not-working-on-laptop-in-windows-11-24h2
date: 2026-10-05
categories: ["battery"]
tags: ["battery saver", "power saving", "windows 11 24h2", "troubleshooting"]
description: "Battery saver won't turn on or does nothing on Windows 11 24H2? Fix it with these 7 targeted steps, from settings resets to power plan repair."
thumbnail: "/images/thumbs/how-to-fix-battery-saver-not-working-on-laptop-in-windows-11-24h2.webp"
faqs:
  - q: "Why won't battery saver turn on in Windows 11 24H2?"
    a: "Common causes include a corrupted power plan, the energy saver feature being blocked by a vendor power profile, a stuck setting from the 24H2 upgrade, or group policy restrictions on managed devices. The fastest fixes are toggling it manually in Settings, resetting the power plan, and running the Power troubleshooter."
  - q: "Is battery saver the same as energy saver in Windows 11?"
    a: "They're closely related. Microsoft rebranded Battery Saver as Energy Saver in newer Windows 11 builds, and Energy Saver now works on both battery and plugged-in power. If your laptop shows Energy Saver instead of Battery Saver, you're looking at the same feature with a broader scope."
  - q: "Does battery saver actually extend battery life?"
    a: "Yes, measurably. It reduces background activity, throttles the CPU, dims the screen slightly, and cuts sync tasks. Real-world gains are typically 10 to 30 percent more runtime, depending on what you were running."
  - q: "Why is battery saver greyed out when my laptop is plugged in?"
    a: "In older builds battery saver only activates on battery power. In 24H2, Energy Saver can run while plugged in, but the automatic low-battery trigger (like 20 percent) still only applies when unplugged. Toggle it manually in Settings > System > Power & battery to force it on."
---

You flip on Battery Saver expecting your laptop to sip power gently, but nothing happens. The toggle won't stay on, the taskbar icon doesn't change, or the feature activates yet your battery keeps draining at the same pace. On Windows 11 24H2 this is a surprisingly common complaint — the upgrade rearranged power settings, renamed the feature on some systems, and left behind corrupted power plans that silently block it.

The good news: Battery Saver (now called Energy Saver in newer 24H2 builds) is just a coordinated set of Windows settings. When it refuses to work, one of those underlying settings is stuck, corrupted, or overridden by a vendor utility. The seven fixes below walk you from quick toggles to deeper power-plan surgery.

## Why this happens

- **A corrupted power plan from the 24H2 upgrade.** The upgrade can migrate power schemes incorrectly, leaving Battery Saver's activation rules broken.
- **A vendor power profile is overriding Windows.** Lenovo Vantage, Dell Power Manager, Asus Armoury Crate, and HP tools can seize control of power settings and block Windows' saver.
- **Energy Saver is blocked by group policy.** On work or school laptops, administrators may disable the feature entirely via policy.
- **The Power troubleshooter settings are stuck.** Stale registry values from the old build can prevent the toggle from engaging.
- **The trigger threshold is misconfigured.** If the automatic turn-on level got set to "Never" or to an odd percentage during migration, it will never activate on its own.
- **Background apps and drivers ignore the saver.** A single misbehaving driver or a high-drain app can cancel out the saver's gains, making it look broken when it's actually working.

## How to fix it

Work through these in order — the early fixes resolve most cases.

### Fix 1: Toggle Energy Saver manually and check the name

Microsoft renamed Battery Saver to Energy Saver in recent builds, which confuses the search.

1. Open **Settings > System > Power & battery**.
2. Expand **Energy saver** (or **Battery saver** on older installs).
3. Turn the toggle **On** manually. Note whether it stays on or flips back off.
4. If the setting is missing entirely, your vendor utility may have replaced it — check Lenovo Vantage, Dell Power Manager, or Asus Armoury Crate for an equivalent low-power mode.
5. Also confirm your power mode under **Power mode** — if it's locked to **Best performance** by a vendor profile, the saver can't engage. Microsoft's [Windows support pages](https://support.microsoft.com/en-us/windows) document where the Energy Saver toggle lives if a build renames things again.

### Fix 2: Set the automatic activation threshold

If manual mode works but automatic activation never kicks in, the threshold is wrong.

1. Go to **Settings > System > Power & battery > Energy saver**.
2. Set **Turn energy saver on automatically at** to a sensible value like **20%** instead of Never or Always.
3. Unplug the charger and let the battery drop past the threshold, then watch the taskbar battery icon — it should show the saver state.
4. If your laptop also has vendor thresholds (Lenovo Conservation Mode, Asus Battery Health Charging), make sure they don't conflict. For charge caps that look like saver problems, see [how to limit your battery charge to 80 percent](/articles/how-to-limit-battery-charge-to-80/).

### Fix 3: Run the Power troubleshooter

Windows can detect and reset broken power settings automatically.

1. Open **Settings > System > Troubleshoot > Other troubleshooters**.
2. Click **Run** next to **Power**.
3. Apply every recommended fix, then restart the laptop.
4. After rebooting, open **Settings > System > Power & battery** and try the saver toggle again.

### Fix 4: Restore the default power plans

A corrupted power scheme can silently disable the saver. Restoring defaults rebuilds it.

1. Right-click **Start** and open **Terminal (Admin)** or **Windows PowerShell (Admin)**.
2. Run `powercfg -restoredefaultschemes` and press Enter.
3. Restart the laptop.
4. Open **Settings > System > Power & battery** and verify the saver toggle now engages.
5. Note: this resets any custom power plan tweaks you've made, so reapply them afterward.

### Fix 5: Check for vendor utility conflicts

Vendor power apps frequently hijack the same settings Windows' saver controls.

1. Open your manufacturer's utility — **Lenovo Vantage**, **Dell Power Manager**, **MyASUS**, **HP OMEN Gaming Hub**, or **Acer Care Center**.
2. Look for any active performance or battery profile (like "Extreme Performance" or "Rapid Charge") and switch it to **Balanced** or the equivalent.
3. In MyASUS, check **Battery Health Charging** and **Fan Profile** — aggressive modes override the Windows saver.
4. Try disabling the vendor utility's power features temporarily, then test the Windows saver again. If it works, the vendor profile was the blocker.

### Fix 6: Fix the registry values for Energy Saver

When the toggle flips back off immediately, stuck registry values are often the cause. Proceed carefully.

1. Press **Win + R**, type `regedit`, and press Enter. Click **Yes** on the UAC prompt.
2. Navigate to `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\EnergySaver`.
3. If the **EnergySaverEnabled** or **EnergySaverBatteryThreshold** values look wrong, you can delete the **EnergySaver** key entirely — Windows rebuilds it with defaults on next sign-in.
4. Sign out and back in, then test the saver toggle. Only edit these keys if you're comfortable with the registry; a wrong edit elsewhere can cause real damage.

### Fix 7: Create a fresh power plan as a workaround

If the built-in plans stay broken, a new plan sidesteps the corruption.

1. Open **Control Panel > Hardware and Sound > Power Options**.
2. Click **Create a power plan** on the left, choose **Power saver** as the base, and name it something like "Custom Saver".
3. Click **Change plan settings > Change advanced power settings**.
4. Expand **Battery** and configure the low/critical battery levels and actions the way you want (for example, low at 20%, critical at 7%, hibernate at critical).
5. Set this plan as active and test. This gives you the practical effect of a working saver even if the toggle stays broken. If your laptop also drains abnormally fast on battery, [check what's draining it](/articles/how-to-fix-battery-drains-overnight-when-laptop-is-off-on-windows-11/).

## Closing

Nine times out of ten, Battery Saver not working on 24H2 is a corrupted power plan or a vendor utility fighting Windows for control — not a hardware fault. Once the toggle engages reliably and the automatic threshold fires at your chosen percentage, the feature is fixed. If it's a managed work laptop and the setting stays greyed out, your IT administrator's policy is the real gatekeeper.
