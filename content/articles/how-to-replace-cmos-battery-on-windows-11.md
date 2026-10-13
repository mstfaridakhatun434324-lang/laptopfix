---
title: "How to Replace the CMOS Battery in a Windows 11 Laptop"
slug: how-to-replace-cmos-battery-on-windows-11
date: 2026-09-05
categories: ["battery"]
tags: ["cmos battery", "cr2032", "bios"]
description: "Your clock keeps resetting and BIOS settings won't stick? Here's how to replace the dead CMOS battery in your Windows 11 laptop, step by step."
thumbnail: "/images/thumbs/how-to-replace-cmos-battery-on-windows-11.webp"
faqs:
  - q: "What are the signs of a dead CMOS battery?"
    a: "The clock resets to a wrong date after every shutdown, BIOS or UEFI settings revert to defaults, you see a 'CMOS checksum error' or 'Press F1 to continue' message at boot, and BitLocker may ask for a recovery key because hardware measurements changed."
  - q: "What type of CMOS battery do laptops use?"
    a: "Most use a CR2032 coin cell, but many modern thin laptops use a wired CR2032 pack with a 2-pin connector instead of a bare cell. Check your laptop's service manual before buying, because the wrong type will not fit."
  - q: "Will replacing the CMOS battery erase my files?"
    a: "No. The CMOS battery only keeps the real-time clock and BIOS settings alive. Your files, Windows 11, and programs live on the SSD and are completely unaffected. You will just need to re-enter the date, time, and any custom BIOS settings."
  - q: "How long does a CMOS battery replacement take?"
    a: "For most laptops, fifteen to thirty minutes, including removing the bottom panel. Laptops where the cell sits under the motherboard take longer. If your manual shows the motherboard must come out, consider having a repair shop do it."
---
Your laptop keeps waking up thinking it's 2015, the boot order resets itself, and Windows asks for the time every morning like it has amnesia. That is not a Windows 11 problem — it's a tiny coin-cell battery on the motherboard giving up after years of quiet service.

That little battery is called the CMOS battery, and replacing it is one of the simplest hardware repairs you can do yourself. No Windows reinstall, no data loss, and in most laptops it takes about twenty minutes with a basic screwdriver. Here's how to diagnose it, open the machine safely, and swap the cell.

## Why this happens

- **The CMOS battery keeps the clock and BIOS settings alive.** It is a small CR2032 cell (sometimes a wired pack) that powers the real-time clock and stores UEFI/BIOS settings when the laptop is unplugged.
- **Coin cells last roughly three to five years.** After that the voltage sags, the clock drifts, and eventually settings reset on every full shutdown.
- **Laptops left unplugged for weeks die faster.** When the main battery is at zero and no adapter is connected, the CMOS cell carries the whole load and drains quickly.
- **Heat accelerates the decline.** A laptop that runs hot for years ages its CMOS cell faster, just like it ages the main battery. If your machine already runs warm, [check what heat does while charging](/articles/how-to-fix-laptop-overheating-while-charging-in-windows-11-24h2/) too.
- **Some laptops don't use a bare coin cell.** Thin ultrabooks often use a wired CMOS pack with a 2-pin connector, and a few have the cell soldered — in which case this becomes a repair-shop job.
- **A dead cell can trigger BitLocker recovery.** When BIOS settings revert, measured boot values change, and BitLocker may demand the recovery key. Save yours before you start: search **BitLocker** in the Start menu and back up the key to your Microsoft account.

## How to fix it

Work through these in order. The first two confirm the diagnosis and get the right part; the rest are the physical swap.

### Fix 1: Confirm the symptoms are CMOS-related

Before opening anything, make sure the problem is the CMOS battery and not the main battery or Windows.

1. Shut the laptop down fully (not sleep, not hibernate), unplug the charger, and wait five minutes.
2. Power on and check whether the Windows clock is wrong and whether BIOS settings (like boot order) have reset. If yes both times, the CMOS cell is almost certainly dead.
3. Rule out the main battery as the cause: generate a quick health check with `powercfg /batteryreport` — the full steps are in our [battery report guide](/articles/how-to-generate-battery-report-windows-11-powercfg/). A healthy main battery plus resetting clocks means the coin cell is the culprit.

### Fix 2: Get the correct replacement cell

Buying the wrong cell is the most common mistake in this repair.

1. Look up your exact model's service or maintenance manual — Dell, HP, and Lenovo all publish free PDFs showing the CMOS battery type and location. [Dell's support site](https://www.dell.com/support) and [HP's support site](https://support.hp.com/us-en) are good starting points.
2. Note whether you need a bare **CR2032** or a **wired CMOS pack** (CR2032 in a plastic sleeve with a 2-pin cable). They are not interchangeable.
3. Buy a fresh cell from a reputable seller. Coin cells sit on shelves for years; a cheap stale cell can arrive half-dead. Check the printed expiry date on the packaging.

### Fix 3: Prepare a safe workspace

Laptop internals are fragile, and static discharge can kill a motherboard.

1. Shut down Windows completely: **Start > Power > Shut down**. Do not just close the lid.
2. Unplug the charger and remove every peripheral — USB drives, dongles, SD cards.
3. If your laptop has a removable main battery, take it out now. If it is internal, you will disconnect it in the next step.
4. Work on a clean, non-carpeted table. Touch a grounded metal object (like a radiator or the screw on a wall outlet plate) before touching anything inside.

### Fix 4: Open the bottom panel

This is where most people get nervous, but it is just screws and clips.

1. Flip the laptop over and photograph the screw layout so every screw goes back in the right hole — they are often different lengths.
2. Remove all bottom-panel screws with a small Phillips screwdriver and keep them in a tray or on tape in their original pattern.
3. Gently pry the panel starting at a corner with a plastic spudger or old credit card. Never use a metal knife; it scratches and can short components.
4. Lift the panel off slowly. Some panels have ribbon cables to the speakers — tilt, don't yank.

### Fix 5: Disconnect the main battery first

This is a safety step you should not skip, even though the laptop is off.

1. Locate the main battery's connector on the motherboard — usually a wide multi-pin plug near the battery itself.
2. Slide or lift the connector straight out. On many models there is a small locking tab; release it first.
3. Press and hold the power button for ten seconds to drain residual charge from the board.

### Fix 6: Locate and remove the old CMOS cell

Now for the actual five-second part of the repair.

1. Find the coin cell: a silver disc about the size of a shirt button, often near the center of the motherboard, sometimes tucked under a piece of tape or a cable.
2. If it sits in a metal holder, push the small metal tab aside and the cell pops up. Note which side faces up — the **+ side** is almost always up.
3. If it is a wired pack, follow its cable to the tiny 2-pin connector on the motherboard and pull the connector straight out by the plug, not the wires. Peel the old pack off its adhesive pad.
4. Take a photo of the old cell in place before removing it, so you have a reference.

### Fix 7: Install the new cell and reassemble

Reverse the process carefully.

1. Place the new cell with the **+ side up** (or plug in the new wired pack's 2-pin connector until it clicks).
2. Reconnect the main battery connector firmly — a half-seated connector causes "battery not detected" errors later.
3. Replace the bottom panel, pressing the clips in around the edges, then reinstall the screws in their original holes using your photo.
4. Plug in the charger before the first power-on; this lets the fresh cell and main battery stabilize together.

### Fix 8: Set the date and time in BIOS, then verify

The new cell starts with no memory, so you must teach it the time once.

1. Power on and immediately press the BIOS key for your brand (**F2** for Dell/Acer, **Esc** then **F10** for HP, **F1** or **Enter** then **F1** for Lenovo, **Del** or **F2** for ASUS).
2. In the BIOS/UEFI setup, set the correct date and time, and re-apply any custom settings you had (boot order, virtualization, secure boot state).
3. Save and exit (usually **F10**), let Windows boot, and confirm the Windows clock is correct.
4. Verify the fix sticks: shut down fully, unplug for ten minutes, boot again. If the clock is still right, the new cell is doing its job. Microsoft documents BIOS-adjacent startup behavior on the [Windows support site](https://support.microsoft.com/en-us/windows) if anything looks off.

## Closing

A dead CMOS battery feels like a mysterious software curse, but it's just a three-dollar coin cell that ran out of energy. Swap it, set the clock once in BIOS, and your laptop will remember the time, the date, and its settings again — no reinstall, no lost files, and one less strange boot message to start your day.
