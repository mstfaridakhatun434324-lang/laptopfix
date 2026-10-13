---
title: "How Do I Fix My Laptop Battery Not Charging When Plugged In?"
slug: how-do-i-fix-laptop-battery-not-charging-when-plugged-in
date: 2026-09-23
categories: ["battery"]
tags: ["not charging", "plugged in", "battery fix", "beginner guide"]
description: "New to troubleshooting? This plain-English guide walks you through fixing a laptop battery that won't charge when plugged in — no jargon, just steps."
thumbnail: "/images/thumbs/how-do-i-fix-laptop-battery-not-charging-when-plugged-in.webp"
faqs:
  - q: "My laptop says plugged in but the battery percentage never goes up. Where do I start?"
    a: "Start with the charger: make sure it's the original (or same wattage), plugged firmly into a working wall outlet, with no damage to the cable. Then check for battery-saving features that limit charging (like Lenovo Conservation Mode or an 80% cap in your manufacturer's app). Those two checks solve most cases."
  - q: "Is it safe to keep using my laptop if the battery won't charge?"
    a: "Yes, as long as it runs fine on the charger — you're essentially using it as a desktop. But back up your important files, because if the power blips or the charger comes loose, the laptop will shut off instantly with no battery to cover the gap. And don't ignore a swelling battery — that's a safety issue."
  - q: "How do I know if I need a new battery or just a new charger?"
    a: "Test with a borrowed charger of the same wattage: if charging works, your charger was bad. Check the battery's health with a battery report (powercfg /batteryreport): high wear means the battery is the problem. And if the laptop runs fine on AC with a removable battery taken out, the battery is the culprit."
  - q: "Will reinstalling Windows fix my charging problem?"
    a: "Almost never, and it's a lot of disruption for nothing. Charging is controlled by firmware and drivers, not Windows itself. The driver reinstall and EC reset steps in this guide address the same layer a Windows reinstall would touch, without wiping your files."
---

Let's keep this simple. Your laptop is plugged in, but the battery isn't charging — the percentage sits still, or Windows says "plugged in, not charging." Most charging problems are simple, and you can check the simple things yourself in about twenty minutes.

We'll start with the easy, obvious stuff (because that's what it usually is) and work toward the less obvious. No jargon where we can avoid it, and every technical step is spelled out.

## Why this happens (in plain English)

- **The charger isn't up to the job:** Wrong charger, damaged cable, or a dead wall outlet. The laptop sees "something plugged in" but gets no useful power.
- **A battery-saving feature is limiting charging:** Your laptop's manufacturer app may be capping the charge at 60% or 80% to make the battery last longer. It looks broken, but it's a setting.
- **Windows got confused:** The part of Windows that talks to the battery can get stuck, especially after the battery fully drained or the laptop crashed.
- **The battery is worn out:** Batteries age. An old battery may simply not accept charge anymore.
- **The charging port is loose or dirty:** If the plug wobbles, power comes and goes.
- **Something deeper failed:** Rarely, the charging electronics inside the laptop break. That's a repair-shop job, and we'll help you recognize it.

## How to fix it

Do these in order. Stop when charging works.

### Fix 1: Check the charger and outlet (5 minutes)

This sounds too simple, but it's the cause more often than anything else.

1. Look at your charger brick. Is it the one that came with the laptop? If you're using a different charger, it might not be powerful enough.
2. Follow the cable from wall to laptop. Look for fraying, kinks, or a plug that feels loose in the laptop.
3. Unplug from the wall and plug into a **different outlet** — one you know works (test it with a lamp or phone charger). Skip power strips for this test.
4. Push the laptop plug in firmly. You should feel it seat solidly, not wobble.
5. Wait 5 minutes and check: hover over the battery icon near the clock. Does the percentage move up at all? Any upward movement means power is flowing.

### Fix 2: Look for a battery-saving limit

Manufacturers add features that stop charging early to protect the battery. They sometimes turn on by themselves after updates.

1. Think: does your battery stop at a round number like 60% or 80%? That's the telltale sign of a limiter, not a broken battery.
2. Open your manufacturer's app and look for battery settings:
   - **Lenovo:** Lenovo Vantage → Conservation Mode → turn it **off**.
   - **ASUS:** MyASUS → Battery Health Charging → **Full capacity mode**.
   - **Dell:** Dell Power Manager → Battery Settings → **Standard**.
   - **HP:** this one's in the BIOS (restart, tap F10) → Battery Health Manager.
3. Don't have the app? Search the Microsoft Store for it (e.g., "Lenovo Vantage") and install it — it's free.
4. After changing the setting, **shut the laptop down completely** (Start → Power → Shut down), wait 10 seconds, turn it back on, and check charging.

### Fix 3: Restart the battery connection in Windows

Windows talks to your battery through a driver. Sometimes that conversation breaks, and reintroducing them fixes it.

1. Right-click the **Start** button and choose **Device Manager**.
2. Find **Batteries** in the list and click the little arrow to expand it.
3. Right-click **Microsoft ACPI-Compliant Control Method Battery** and choose **Uninstall device**. Confirm. (Don't worry — Windows puts it back automatically.)
4. Now shut down the laptop completely: **Start → Power → Shut down**.
5. Unplug the charger. Count to 30. Plug it back in.
6. Turn the laptop on. Windows will quietly reinstall the driver. Give it 10-15 minutes and check whether the battery percentage is climbing.

### Fix 4: Reset the laptop's power hardware

Laptops have a tiny built-in controller that manages charging, separate from Windows. It can get stuck — especially after the battery drained completely.

1. Shut down the laptop and unplug the charger.
2. Look on the bottom of the laptop for a **tiny pinhole** (many Lenovo, HP, and Acer models have one, sometimes with a battery icon next to it).
3. If you find it: straighten a paperclip, gently push it in, and hold for about 15 seconds.
4. No pinhole? Do this instead: with everything unplugged, press and hold the **power button for 30 seconds**.
5. Plug the charger back in, wait 10 seconds, then turn on the laptop.
6. Check charging for 15 minutes. This reset clears the "stuck" state that causes a surprising number of charging failures.

### Fix 5: Check how healthy the battery actually is

If the easy fixes didn't work, let's see what shape the battery is in. This takes two minutes.

1. Right-click **Start** and choose **Terminal (Admin)** (or Windows PowerShell (Admin)).
2. Type exactly this and press Enter: `powercfg /batteryreport`
3. It will tell you where it saved a file. Open **File Explorer**, go to your user folder (usually `C:\Users\YourName`), and double-click **battery-report.html**.
4. Near the top you'll see **Design Capacity** and **Full Charge Capacity**. Divide the second by the first.
5. If the result is above 0.75 (battery holds 75%+ of original): the battery is okay — keep troubleshooting below.
6. If it's below 0.6 (under 60%): the battery is worn out and likely needs replacing. Skip to Fix 7.
7. Our plain-English explainer on [checking battery health numbers](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/) can help if the report looks confusing.

### Fix 6: Rule out the port and test systematically

Let's make sure power is actually getting in.

1. With the charger plugged in, **gently** wiggle the plug. Watch the charging light: if it flickers, the port is loose — that's a hardware repair (don't force it; a wobbly port gets worse with forcing).
2. Look into the charging port with a flashlight. Blow out any lint or dust with a quick puff of air (don't use anything metal or wet).
3. If your battery is removable (older laptops have a latch on the bottom): take it out, plug in, and turn on. If the laptop works fine without the battery, the charger and laptop are okay — the battery is the problem.
4. Try charging while the laptop is **completely off**. If it charges while off but not while on, your charger is too weak for the job — you need the correct-wattage replacement.

### Fix 7: Replace the battery (if the numbers say so)

If the health check showed a worn-out battery, here's how to do this right.

1. Find your exact battery model: it's printed on the battery itself, or look up your laptop's serial number on the manufacturer's support website.
2. Buy a **genuine** battery from the manufacturer or an authorized seller. The cheap ones from random online sellers often don't work properly and can be unsafe. This is the one place not to bargain-hunt.
3. Check your warranty first — many laptops cover the battery for a year. You might get it free.
4. Replacing it is usually simple: for removable batteries, it's a latch. For internal ones, it's typically 8-12 screws on the bottom panel and one plug — very doable if you're careful, or any local repair shop will do it cheaply.
5. **Important safety note:** if the battery looks puffed up or the laptop's bottom doesn't sit flat, stop using it and get professional help right away. Swollen batteries can be dangerous — don't puncture or bend them.
6. After installing the new battery, charge it to 100% without interruption, then use it normally. Check our brand-specific guides if you have a [Dell](/articles/how-to-fix-dell-laptop-battery-not-charging-step-by-step/) or [Acer](/articles/how-to-fix-acer-laptop-battery-not-charging-step-by-step/) for model-specific tips.

## Closing

Charging problems feel alarming, but the fix is usually unglamorous: the right charger, a forgotten battery-saver setting, or a quick driver reset. Work the list top to bottom, and you'll either fix it or know exactly what's wrong.

*Related reading: [systematic troubleshooting walkthrough](/articles/troubleshoot-laptop-battery-not-charging-when-plugged-in/), [battery health numbers explained](/articles/best-way-to-check-battery-design-vs-full-charge-capacity/)*
