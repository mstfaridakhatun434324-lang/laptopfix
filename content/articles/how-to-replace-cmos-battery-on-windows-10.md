---
title: "How to Replace the CMOS Battery in a Windows 10 Laptop"
slug: how-to-replace-cmos-battery-on-windows-10
date: 2026-10-08
categories: ["battery"]
tags: ["cmos battery", "bios reset", "date time error", "hardware"]
description: "Clock resetting every boot? That's the CMOS battery. Learn the symptoms, what to buy, and how to replace it safely."
thumbnail: "/images/thumbs/how-to-replace-cmos-battery-on-windows-10.webp"
faqs:
  - q: "What are the symptoms of a dead CMOS battery?"
    a: "The classic signs: the system clock resets to a wrong date/time every time you power off, BIOS settings won't stick, and you may see 'CMOS checksum error' or 'press F1 to continue' on boot. If the clock is wrong only after full shutdowns (not restarts), the CMOS battery is the prime suspect."
  - q: "What type of CMOS battery do laptops use?"
    a: "Most use a CR2032 coin cell, but in laptops it's often a CR2032 in a small plastic holder with a two-wire lead and connector, rather than the bare coin cell found in desktops. Check your model's service manual for the exact part — some ultrabooks use smaller cells or soldered batteries."
  - q: "Can I replace a laptop CMOS battery myself?"
    a: "On many models, yes — it's usually accessible after removing the bottom cover, sometimes under the main battery or near the RAM. But on thin ultrabooks it may be buried under other components or soldered, in which case a repair shop is the safer choice."
  - q: "Will replacing the CMOS battery delete my files?"
    a: "No. The CMOS battery only powers the real-time clock and BIOS settings memory. Your files, Windows installation, and programs live on the SSD/HDD and are completely unaffected. You'll just need to re-enter the correct date/time and any custom BIOS settings afterward."
---
Every time you shut down completely, your laptop forgets what time it is. BIOS settings revert. Maybe you get a cryptic "CMOS checksum error" on boot. These are the calling cards of a dead CMOS battery — the tiny coin cell that keeps your motherboard's clock and settings alive when all other power is gone.

The good news: the battery itself costs a few dollars. The work is in getting to it, which ranges from trivial to tricky depending on your laptop. Here's how to handle it.

## Why this happens

- **The coin cell is simply exhausted.** CMOS batteries last 3–7 years; after that, voltage drops too low to maintain the real-time clock and CMOS memory.
- **The laptop sat unused for a long time.** Without any power source for months, even a healthy CMOS battery drains faster.
- **Heat accelerates the drain.** Laptops that run hot shorten the coin cell's life, just like they shorten the main battery's.
- **The connector worked loose.** On laptops with wired CMOS batteries, the tiny two-pin connector can creep loose over years of thermal cycling and movement.
- **A failing cell holder.** Corrosion or a weakened spring contact in the holder can mimic a dead battery even when the cell is fine.
- **Confusion with the main battery.** Some users chase the CMOS battery when the real problem is Windows time-sync settings — verify the symptoms first.

## How to fix it

Work through these in order — confirm the diagnosis before opening the laptop.

### Fix 1: Confirm it's actually the CMOS battery

Don't open the laptop for a software problem.

1. Shut the laptop **fully down** (not sleep, not hibernate), unplug it, wait **10 minutes**, then power on — if the clock is wrong, it's the CMOS battery.
2. If the clock is only wrong after the battery fully dies but stays correct on normal shutdowns, that's still consistent with a weak CMOS cell.
3. Rule out Windows: go to **Settings > Time & language > Date & time**, enable **Set time automatically**, and confirm Windows can sync when online — if it syncs fine but forgets after power-off, the hardware cell is dead.

### Fix 2: Identify the correct replacement part

Laptop CMOS batteries aren't one-size-fits-all.

1. Find your exact model number and check the **service manual** on the maker's support site ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)) for the CMOS battery part number.
2. Most use a **CR2032** in a wired holder with a 2-pin connector — buy the version with the correct wire length and connector for your model.
3. Avoid ultra-cheap no-name cells; a reputable brand (Panasonic, Energizer, Duracell) lasts years longer.

### Fix 3: Prepare for safe disassembly

A little prep prevents expensive mistakes.

1. **Back up important data** — not because this procedure risks it, but because any disassembly carries small risks.
2. Gather a **small Phillips screwdriver**, a **plastic pry tool**, and a tray or magnetic mat for screws.
3. Work on a **clean, static-safe surface**; touch a grounded metal object before handling internals, or wear an anti-static wrist strap.
4. Photograph each disassembly step so reassembly is straightforward.

### Fix 4: Access and replace the battery

The core procedure — adapt to your model's layout.

1. Power off, unplug, and remove the **main battery** if it's removable.
2. Remove the **bottom cover screws** (note which screws go where — lengths often differ) and gently pry the cover off.
3. Locate the **CMOS battery** — a coin cell in a holder, often with red/black wires leading to a small white connector on the motherboard.
4. Gently disconnect the **2-pin connector** (pull the plug, never the wires) or release the cell from its holder.
5. Install the **new battery**, reconnect firmly, and reassemble in reverse order of your photos.

### Fix 5: When it's buried or soldered

Know when to hand it to a professional.

1. If the service manual shows the CMOS battery under the **motherboard** or **soldered** to the board, stop — this needs a technician with the right tools.
2. Some ultrabooks require near-complete disassembly (keyboard, display, motherboard removal) — weigh the labor cost against the annoyance of the symptoms.
3. A local repair shop typically charges modest labor for this since the part is cheap — get a quote before attempting a risky teardown.

### Fix 6: Reconfigure after replacement

The new battery means a blank slate for BIOS settings.

1. Power on and enter **BIOS/UEFI** (**F2**/**Del**) — set the correct **date and time**.
2. Reapply any custom BIOS settings you had (**boot order**, **virtualization**, **secure boot** preferences).
3. Boot into Windows, go to **Settings > Time & language > Date & time**, and confirm **Set time automatically** is on.
4. Shut down fully, wait 10 minutes, and power on to verify the clock survived — confirming the fix.

### Fix 7: Maintain the new cell

Make it last as long as possible.

1. Don't leave the laptop **completely unpowered for months** — occasional use keeps the charging circuit topping up the CMOS cell on models that support it.
2. Keep the laptop reasonably **cool**; heat shortens coin-cell life.
3. If symptoms return within a year, suspect the **holder contacts** or a **parasitic drain** on the board rather than another dead cell.

## Closing

A dead CMOS battery is one of the most benign hardware failures a laptop can have — a few dollars, half an hour, and your clock behaves again. The key steps are confirming the diagnosis before opening anything and buying the exact wired replacement your model needs rather than a generic coin cell. Take photos during disassembly, keep track of screws, and don't force anything. And if your model buries the cell under the motherboard, there's no shame in letting a shop handle it — the part is cheap either way. For related power diagnostics, our [powercfg battery guide](/articles/best-way-to-use-powercfg-to-check-battery/) covers the main battery's health checks, and if the main battery itself is aging, our [wear-level guide](/articles/how-to-check-battery-wear-level-on-laptop/) shows you how to measure it — worth doing while you have the tools out, since a laptop old enough to need a CMOS cell is old enough to have a tired main battery too.
