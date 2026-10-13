---
title: "Laptop Slow When Plugged In on Windows 10? Fix the Power Trap"
slug: how-to-fix-laptop-slow-when-plugged-in-on-windows-10
date: 2026-10-07
categories: ["performance"]
tags: ["laptop slow when plugged in", "windows 10 slow charging", "power throttling", "ac adapter issue"]
description: "Laptop runs fine on battery but slows to a crawl when plugged in on Windows 10? Uncover the power-management trap causing it and fix it for good."
thumbnail: "/images/thumbs/how-to-fix-laptop-slow-when-plugged-in-on-windows-10.webp"
faqs:
  - q: "Why is my laptop slower when plugged in than on battery?"
    a: "It sounds backwards, but it happens when the charger cannot deliver enough power, the power plan switches to an aggressive saving mode on AC, or thermal throttling kicks in because charging generates extra heat. Windows 10 applies separate settings for battery and plugged-in states, so a misconfigured AC profile can throttle the CPU exactly when you expect maximum performance. The charger itself is the culprit more often than people expect."
  - q: "Can a faulty charger really make my laptop slow?"
    a: "Absolutely — this is one of the most underdiagnosed causes. If the charger is underpowered, damaged, or not recognized by the laptop (a broken center ID pin on Dell/Lenovo barrel chargers is classic), the laptop limits CPU speed to stay within the available power budget. Symptoms include the battery not charging, or charging very slowly, alongside the slowness. Always test with the original manufacturer charger before assuming a software problem."
  - q: "What is power throttling in Windows 10?"
    a: "Power throttling is Windows 10's feature that limits background apps' CPU access to save energy, shown as a Throttling column in Task Manager's Details tab. It is supposed to target background work, but misconfigured power plans can throttle foreground apps too. On the plugged-in side, the relevant setting is the processor power management policy — if maximum processor state is capped low on AC, your CPU can never stretch its legs when you need it most."
  - q: "Should I use High Performance power plan all the time?"
    a: "The High Performance plan keeps the CPU at higher minimum speeds, which eliminates throttling-related slowness but increases heat, fan noise, and electricity use. For most users, the Balanced plan with correct AC settings performs identically in real workloads because the CPU boosts on demand. Use High Performance as a diagnostic tool: if it fixes the plugged-in slowness, your Balanced plan's AC settings were the problem — fix those settings rather than running hot permanently."
---

It defies logic: you plug in the charger expecting full speed, and the laptop gets slower. Apps lag, videos stutter, and everything felt snappier on battery. If your Windows 10 laptop slows down the moment AC power connects, you have stumbled into a power-management trap — and it is almost always fixable once you find which layer is throttling you.

Windows 10 keeps completely separate performance settings for battery and plugged-in states, and any of them can be misconfigured: capped processor states, aggressive power saving on AC, a charger the laptop does not trust, or extra heat from charging pushing thermals over the edge. For the reverse scenario, see [laptop slow when plugged in after a Windows 11 update](/articles/how-to-fix-laptop-slow-when-plugged-in-after-windows-11-update/); for general speedups, [speed up a slow Windows 11 laptop](/articles/laptop-running-slow-windows-11-how-to-speed-up/) covers the broader toolkit.

## Why this happens

- **Underpowered or unrecognized charger**: A weak, damaged, or third-party charger makes the laptop cap CPU speed to fit the available power — the single most common hardware cause.

- **Capped processor state on AC**: The power plan's Maximum processor state for the plugged-in profile can be set below 100%, hard-limiting CPU speed on charger power.

- **Aggressive PCI Express / USB power saving on AC**: Link-state power management and selective suspend settings meant for battery can be wrongly applied to the AC profile.

- **Extra heat from charging**: Charging the battery adds heat inside the chassis; combined with CPU load it can push thermals into throttling territory.

- **Manufacturer power utilities**: Dell Power Manager, Lenovo Vantage, or HP utilities can enforce quiet/cool profiles on AC that override Windows settings.

- **Intel SpeedStep / AMD Cool'n'Quiet misbehavior**: Firmware-level frequency scaling can get stuck at low multipliers when AC state changes confuse it.

- **Dirty or loose charging port**: An intermittent connection makes the laptop rapidly switch between AC and battery profiles, and each switch can momentarily throttle performance.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Test with the correct charger

Rule out the power supply first — it is the cause in a surprising share of cases.

1. Check the charger's wattage on its label and compare with your laptop's requirement (often printed near the charging port or in the manual).
2. Use only the original manufacturer charger for testing — phone chargers and low-wattage USB-C bricks will throttle most performance laptops.
3. Inspect the charger tip and laptop port for damage, bent pins, or debris; on Dell/Lenovo barrel chargers the thin center ID pin is critical.
4. Boot into the BIOS/UEFI (usually F2 or Del at startup) and look for the AC adapter status — many business laptops report the detected wattage there.
5. If the BIOS shows Unknown or a lower wattage than the brick's rating, replace the charger; no software fix overcomes a power supply the laptop does not trust.

### Fix 2: Verify CPU speed while plugged in

Confirm the throttling is real and measure it before changing settings.

1. Unplug the charger, open **Task Manager > Performance > CPU**, and note the speed during a heavy task.
2. Plug the charger in and repeat the same task — if speed drops significantly on AC, throttling is confirmed.
3. Run a quick benchmark (Cinebench or Geekbench) on battery and on AC to get hard numbers; a large AC deficit proves the point.
4. Check temperatures with HWMonitor or HWiNFO during the AC test — if temps are high, heat (Fix 6) is your issue, not power policy.
5. Keep Task Manager open during the remaining fixes so you can watch CPU speed respond in real time.

### Fix 3: Fix the plugged-in processor power settings

Windows 10's per-profile processor settings are the classic software culprit.

1. Open **Control Panel > Power Options**, click **Change plan settings** on your active plan, then **Change advanced power settings**.
2. Expand **Processor power management > Maximum processor state** — set **Plugged in** to **100%** (if it is capped at 50-80%, you found it).
3. Set **Minimum processor state > Plugged in** to **5-10%** (not 100% — that just wastes power and heat at idle).
4. Expand **System cooling policy > Plugged in** and set it to **Active** so fans spin up before the CPU throttles.
5. Click OK, unplug and re-plug the charger, and retest CPU speed under load.

### Fix 4: Audit the rest of the AC power profile

Other power-saving settings can also be wrongly aggressive on AC.

1. In the same **Advanced power settings** dialog, expand **PCI Express > Link State Power Management > Plugged in** and set it to **Off** or **Moderate** (not Maximum power savings).
2. Expand **USB settings > USB selective suspend > Plugged in** and set it to **Disabled** — this also fixes stuttering USB devices on AC.
3. Expand **Wireless Adapter Settings > Power Saving Mode > Plugged in** and set it to **Maximum Performance** if Wi-Fi feels slow on AC.
4. If the plan is a mess, click **Restore plan defaults** and reapply only the changes above.
5. For a clean comparison, switch to the **High performance** plan temporarily — if slowness vanishes, your custom plan's AC settings were at fault.

### Fix 5: Check manufacturer power utilities

OEM tools can silently override everything you just set in Windows.

1. Open your maker's utility — Dell Power Manager, Lenovo Vantage, HP OMEN Hub, or MyASUS — and check the thermal/power profile active on AC.
2. Switch it to **Performance** or **Best performance** mode and retest; Quiet/Cool modes cap CPU deliberately.
3. Look for battery charge thresholds or Battery Saver features that engage on AC and limit performance — disable them for the test.
4. Check for a **Fn + power** hotkey or BIOS setting (often under Power or Performance) enforcing a quiet profile.
5. If the utility itself is buggy, update it from the maker's support site — [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/) — before changing anything else.

### Fix 6: Rule out heat from charging

Charging adds 10-20W of heat inside the chassis; on dusty laptops that is enough to trigger throttling.

1. Monitor CPU temperature on AC with HWMonitor during normal use — sustained temps above 90-95°C mean thermal throttling.
2. Test with the battery at 100% (charging complete, minimal charge heat) versus at 20% (fast charging, maximum heat); a big performance gap points at heat.
3. Clean the vents with compressed air and make sure the laptop sits on a hard flat surface, ideally elevated at the back.
4. In the BIOS, check whether fan curves differ between AC and battery — some firmware runs fans quieter on AC by default, which is exactly backwards.
5. If the laptop is several years old and runs hot regardless, dried thermal paste may need professional replacement.

### Fix 7: Reset power plans and update firmware

When settings look right but behavior is wrong, reset the whole power subsystem.

1. Open **Terminal (Admin)** and run **powercfg -restoredefaultschemes** to rebuild all power plans from defaults, then reapply the AC tweaks from Fix 3.
2. Update the BIOS/UEFI from your manufacturer's support site — firmware updates regularly fix AC/battery state detection bugs.
3. Update chipset drivers too; the chipset driver mediates power-state transitions between the OS and firmware.
4. Check **Device Manager > Batteries > Microsoft ACPI-Compliant Control Method Battery** — uninstall it, then restart to let Windows redetect the battery subsystem.
5. If slowness persists only on AC after all this, with a known-good charger, the charging circuitry itself may be failing — a repair-shop diagnosis is the next step. Microsoft documents power troubleshooting tools like powercfg in its official Windows support documentation.

## Closing

A laptop that slows down when plugged in is being throttled by something that only engages on AC power: usually a weak or unrecognized charger, a capped processor state in the plugged-in profile, or an OEM utility enforcing a quiet mode. Test the charger, fix the AC power settings, and the paradox disappears — plugged in should mean full speed, and now it will.
