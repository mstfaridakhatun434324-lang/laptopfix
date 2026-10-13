---
title: "Acer Battery Says 'Plugged In, Not Charging'? Here's the Fix"
slug: how-do-i-fix-acer-laptop-battery-not-charging
date: 2026-09-20
categories: ["battery"]
tags: ["acer battery", "plugged in not charging", "acer aspire", "troubleshooting"]
description: "Acer shows 'plugged in, not charging'? Decode what that message really means and fix it with adapter checks, EC resets, and driver repairs."
thumbnail: "/images/thumbs/how-do-i-fix-acer-laptop-battery-not-charging.webp"
faqs:
  - q: "What does 'plugged in, not charging' mean on an Acer?"
    a: "It means Windows sees AC power but the battery isn't accepting charge. On Acers the usual causes are: an 80% charge limit active in Acer Care Center, an underpowered or failing adapter, a stuck battery driver, or an embedded controller that needs the pinhole reset."
  - q: "Is 'plugged in, not charging' bad for my Acer?"
    a: "Not by itself — if a charge limit is active, it's protective behavior. But if no limit is set and the message persists across chargers, the battery may be worn out or the charging circuit may have a fault, both worth investigating rather than ignoring."
  - q: "Why does my Acer only say this at certain percentages?"
    a: "Because that's the signature of a charge limit: the message appears exactly when the battery reaches the cap (usually 80%). If the message appears at random percentages or at 0-5%, it's more likely a driver, adapter, or battery health issue."
  - q: "Can I still use my Acer while it says not charging?"
    a: "Yes — the laptop runs on AC power normally. But don't ignore it long-term: if the battery is deeply discharged and not charging, a power cut means instant shutdown and possible data loss. Fix the charging so the battery is a real backup."
---
"Plugged in, not charging" is Windows telling you, in its least helpful phrasing, that power is reaching the laptop but the battery isn't taking any of it. On an Acer, this message has a short list of usual suspects — and the percentage where it appears is your biggest clue. Stuck at 80%? That's a setting. Stuck at 5%? That's a problem.

This guide decodes the message by symptom, then fixes each cause. If you already worked through the general Acer charging guide, think of this as the focused companion for this exact message.

## Why this happens

- **The 80% charge limit is on:** Acer Care Center's battery limit stops charging at 80%. Windows reports this as "plugged in, not charging" — confusing wording for intentional behavior.
- **The adapter can't deliver enough power:** A weak, failing, or wrong-wattage adapter may power the laptop but not have enough headroom to charge the battery simultaneously.
- **The battery driver is stuck:** After sleep, hibernation, or updates, the ACPI battery driver can freeze and report "not charging" even while the battery charges fine underneath — or vice versa.
- **The embedded controller needs a reset:** The EC manages the physical charging. When it glitches, it can stop requesting charge from the adapter entirely.
- **The battery is at end of life:** A severely worn battery's protection circuit can refuse charge. The message then appears at low percentages and never clears.
- **The DC jack or cable is intermittent:** A loose connection can deliver enough power to run the laptop but drop out during the charge handshake, leaving the battery uncharged.
- **BIOS or firmware confusion:** After updates, the firmware's charge logic can get out of sync with Windows' expectations, freezing the status message.

## How to fix it

Work through these in order — the percentage clue tells you where to focus.

### Fix 1: Read the percentage — it tells you the cause

Before changing anything, look at where the battery is stuck. This single observation narrows the field enormously.

1. **Stuck at exactly 80%:** Almost certainly the Acer Care Center charge limit. Skip to Fix 2.
2. **Stuck at 50–60%:** Possible limit setting or a battery health mode. Check Fix 2 as well.
3. **Stuck at a low percentage (0–15%) and never moves:** Adapter, driver, EC, or worn battery. Work through Fixes 3–6.
4. **Percentage slowly climbs but message persists:** The driver display is stale while charging actually works — Fix 4 (driver reinstall) usually clears it.
5. **Percentage jumps around:** Gauge or driver issue — Fix 4, then consider calibration.

Write down the stuck percentage. You'll use it to verify each fix worked. For the broader Acer charging walkthrough, see [troubleshoot an Acer laptop battery that won't charge](/articles/troubleshoot-acer-laptop-battery-not-charging/).

### Fix 2: Check Acer Care Center's charge limit

The 80% limit is the number-one cause of this exact message on Acers.

1. **Open Acer Care Center** (Windows key, type `Acer Care Center`).
2. **Find the battery section** under Checkup or Tune-Up — look for **Battery charge limit** or similar.
3. **If it's on:** That's your message. The laptop is protecting the battery, not malfunctioning. Leave it on for desk use; turn it off when you need a full charge.
4. **If it's off but the battery sticks at 80% anyway:** Toggle it on and back off, then do a full shutdown (**Shift + Shut down**). A stuck limiter state can persist until a true shutdown clears it.

If the limit was the cause, the message clears within a minute of disabling it. See [fix a battery charge limiter that isn't working](/articles/how-to-fix-battery-limiter-not-working-reddit/) for stubborn limiter cases.

### Fix 3: Test the adapter properly

A marginal adapter is the classic cause of "not charging" at low percentages.

1. **Check the wattage on the brick** against your model's needs: Swift/Aspire 45–65W, Nitro/Predator 135W+.
2. **Inspect the cable** along its full length for kinks, fraying, or soft spots. Flex it gently while watching the charge LED — flickering means internal wire damage.
3. **Try a different wall outlet** directly (no power strip).
4. **Borrow a known-good adapter** of equal or higher wattage with the right tip. If the message clears, replace your adapter.
5. **Check the charge LED behavior:** Solid charging LED + "not charging" message = driver/display issue. No LED or flickering LED = power delivery issue.

Never keep using a damaged adapter — a failing brick can take the charging circuit with it. Microsoft's hardware guidance at [support.microsoft.com](https://support.microsoft.com/en-us/windows) reinforces the same point about power accessories.

### Fix 4: Reinstall the battery drivers

The "not charging" text comes from Windows' battery driver. When the driver lies, the message lies.

1. **Open Device Manager** (**Windows + X > Device Manager**).
2. **Expand Batteries.** Right-click **Microsoft ACPI-Compliant Control Method Battery** → **Uninstall device**. Confirm. Repeat for any second entry.
3. **Shut down fully** (**Shift + Shut down**), unplug the charger for 30 seconds, plug back in, and power on.
4. **Watch the taskbar icon** for a minute after reaching the desktop. The message should now reflect reality.

If the message said "not charging" but the percentage was actually climbing, this fix clears the stale display. If it correctly reported no charging, continue.

### Fix 5: Reset the embedded controller via the pinhole

When the EC stops managing charge, no driver reinstall will help — it needs a hardware reset.

1. **Shut down fully** (**Shift + Shut down**) and unplug everything, including USB devices.
2. **Flip the laptop** and find the battery pinhole on the bottom cover (small hole, battery icon, usually central).
3. **Press a straightened paperclip in** and hold for **5 seconds**.
4. **Reconnect the charger**, confirm the charge LED lights, then power on.

This resets the chip that physically controls charging. It's the fix for "not charging" that survives driver reinstalls — especially after power outages or long storage. (Removable-battery models: pull the battery for 60 seconds instead.)

### Fix 6: Generate a battery report and face the wear question

If the message persists through all of the above, get the capacity numbers.

1. **Open Terminal (Admin)** and run `powercfg /batteryreport`.
2. **Compare Full Charge Capacity to Design Capacity.** Under 60% is heavily worn.
3. **Match wear to the symptom:** A worn battery stuck "not charging" at 5–10% with a good adapter is a battery that can't accept charge anymore.
4. **Check for swelling:** Power off and set the laptop on a flat surface. Wobble or a lifting trackpad means a swelling pack — handle carefully and replace promptly.

A worn battery explains the message completely: the protection circuit refuses charge to a pack that can't safely take it. See [check your battery's wear level on Windows 11](/articles/how-to-check-battery-wear-level-on-windows-11/) for the full interpretation guide.

### Fix 7: Update the BIOS if Acer documents a charging fix

Last resort before professional diagnosis.

1. **Find your exact model** (`msinfo32` → System Model) and check Acer's support page for BIOS updates.
2. **Read the release notes.** Only flash if they mention battery, charging, or power fixes.
3. **Flash with the charger connected**, following Acer's instructions exactly, without touching the laptop.

If the notes say nothing about charging, skip it — and take the laptop to a repair shop. At this point you've ruled out settings, adapter, drivers, EC, and battery wear, which points to the charging circuit on the motherboard.

## Closing

"Plugged in, not charging" on an Acer is a message with a translation: at 80%, it means your charge limit is doing its job; at low percentages, it means the adapter, driver, EC, or battery needs attention. Read the stuck percentage first, check Acer Care Center's limit second, and work down the list. Most owners find the answer in the first three fixes — and the battery report at the end tells you honestly when the real answer is a new battery.
