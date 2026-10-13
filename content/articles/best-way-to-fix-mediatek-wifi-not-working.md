---
title: "The Best Way to Fix MediaTek WiFi on a Laptop"
slug: best-way-to-fix-mediatek-wifi-not-working
date: 2026-10-04
categories: ["drivers"]
tags: ["mediatek wifi", "wireless driver", "wifi not working", "windows 11", "driver fix"]
description: "MediaTek WiFi dropping or dead on your laptop? The best repair sequence for MT7921/MT7922 cards — driver cleanup, OEM install, and stability settings."
thumbnail: "/images/thumbs/best-way-to-fix-mediatek-wifi-not-working.webp"
faqs:
  - q: "Why is MediaTek WiFi so problematic on Windows laptops?"
    a: "MediaTek wireless cards like the MT7921 and MT7922 are common in budget and mid-range laptops, and their Windows drivers have a history of aggressive power management bugs and update conflicts. Windows Update frequently replaces the stable OEM driver with a newer but buggier generic MediaTek package."
  - q: "Should I replace my MediaTek card with an Intel one?"
    a: "It is an option on laptops with socketed M.2 WiFi cards, and many users report better stability with Intel AX210 cards. But try the driver fixes first — most MediaTek issues are software, and a card swap requires opening the chassis and checking BIOS whitelists on some brands."
  - q: "Why does MediaTek WiFi disconnect randomly?"
    a: "Random disconnects usually come from the driver's power-saving features putting the card to sleep too aggressively, or from roaming sensitivity set too high. Disabling adapter power management and setting roaming aggressiveness to a moderate value typically stabilizes the connection. If disconnects persist, try the laptop maker's driver one version older, since the newest OEM release occasionally reintroduces the same regression."
  - q: "Which driver version is best for MediaTek WiFi?"
    a: "The driver from your laptop manufacturer's support site for your exact model, not the newest generic MediaTek release. OEM versions are validated against your card's firmware revision. Newer generic drivers sometimes fix issues but often introduce the power-management regressions that cause disconnects."
---

MediaTek wireless cards — the MT7921 (Wi-Fi 6) and MT7922 (Wi-Fi 6E) most commonly — ship in a huge number of otherwise excellent laptops, and they generate a disproportionate share of WiFi complaints. The pattern is familiar: random disconnects, the adapter vanishing after sleep, slow speeds on 5 GHz, or total failure after a Windows update. The hardware itself is capable; the Windows driver ecosystem around it is where things fall apart.

The best repair approach for MediaTek WiFi is specific to these cards: get the OEM driver installed cleanly, tame the power management, and stop Windows Update from undoing it all.

MediaTek's reputation for flaky WiFi is mostly a driver-maturity story rather than a hardware story. The MT7921 and MT7922 are competent radios — they wouldn't ship in millions of laptops otherwise — but MediaTek's Windows driver team has historically been slower than Intel's at fixing power-management edge cases, and Windows Update's habit of pushing the newest generic driver means users constantly receive versions that reintroduce regressions the OEM had already fixed. This creates the characteristic MediaTek experience: WiFi that works fine for months, breaks overnight after an update, and works again once the OEM driver is restored. Understanding that cycle is liberating, because it means the fix is always the same trio — OEM driver, tamed power settings, blocked bad updates — no matter which symptom appears this time.

## Why this happens

- **Buggy generic driver from Windows Update:** Newer MediaTek drivers pushed by Windows Update often introduce power-management regressions.
- **Overaggressive power saving:** The driver's sleep states disconnect the card during idle moments and fail to wake it cleanly.
- **Roaming aggressiveness misconfigured:** The card jumps between access points or bands unnecessarily, causing drops.
- **Firmware-driver mismatch:** The card's firmware expects a driver generation that Windows replaced.
- **5 GHz/6 GHz band issues:** Driver bugs in band steering cause the card to cling to a weak 5 GHz signal or fail on 6 GHz entirely.
- **Fast Startup preserving a crashed state:** The hibernated driver state survives reboots, making the failure look permanent.
- **Antenna or card seating:** Less common, but a loose M.2 card or pinched antenna wire produces identical symptoms.
- **Router incompatibility:** Certain MediaTek driver versions conflict with specific router features like 802.11ax target wake time.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Identify your exact card and driver

1. Open **Device Manager → Network adapters** and note the exact name (e.g., MediaTek Wi-Fi 6 MT7921 Wireless LAN Card).
2. Open **Properties → Driver** and record the version and date.
3. Check the **Events** tab to see when the current driver was installed — matching it to the start of your problems confirms the suspect.
4. Knowing the exact card matters because MT7921 and MT7922 fixes differ slightly in driver versions.

### Fix 2: Disable adapter power management

1. In the adapter's **Properties → Power Management**, uncheck **Allow the computer to turn off this device to save power**.
2. Open the **Advanced** tab and find **Power Saving Mode** — set it to **Maximum Performance**.
3. Look for **Selective Suspend** or similar entries and disable them.
4. This single fix resolves the majority of random-disconnect complaints on MediaTek cards, because the disconnects are usually the card sleeping when it shouldn't.

### Fix 3: Tune roaming and band settings

1. In the adapter's **Advanced** tab, set **Roaming Aggressiveness** to **3. Medium** (not highest).
2. Set **Preferred Band** to **Prefer 5 GHz** if your router supports it, or **No Preference** if 5 GHz is unstable.
3. Disable **802.11a/b/g Wireless Mode** legacy options you don't need, keeping **802.11ax** enabled for Wi-Fi 6.
4. Restart and test for a full day — roaming changes need real-world movement between rooms to evaluate properly.

### Fix 4: Clean-reinstall the OEM driver

1. In **Device Manager**, right-click the MediaTek adapter and choose **Uninstall device**, checking **Attempt to remove the driver**.
2. Download the **wireless driver** for your exact laptop model from the manufacturer's support site.
3. Install it, restart, and verify the driver version in **Properties → Driver**.
4. The OEM package is validated against your card's firmware — generic MediaTek drivers from Windows Update are the usual source of regressions. For the Intel equivalent of this repair, see our [Intel WiFi 6 guide](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).

### Fix 5: Block driver replacement by Windows Update

1. Use the **Show or hide updates** troubleshooter to hide MediaTek driver updates.
2. In **Settings → Windows Update → Advanced options → Optional updates**, uncheck any MediaTek wireless driver before installing updates.
3. This prevention step is essential for MediaTek cards — the bad driver will return with the next update cycle otherwise.
4. Re-verify after major Windows feature updates, which can reset hidden-update lists.

### Fix 6: Cold-boot past Fast Startup

1. Disable **Fast Startup** in **Control Panel → Power Options → Choose what the power buttons do**.
2. Shut down fully, wait fifteen seconds, and power on.
3. If WiFi works after a cold boot but fails after restarts or sleep, the hibernated driver state was corrupt.
4. MediaTek cards are particularly sensitive to stale power states — many users leave Fast Startup off permanently for this reason.

### Fix 7: Test with a Linux live USB

1. Boot a **Linux live USB** and test WiFi for 30 minutes, including sleep/wake cycles.
2. If WiFi is stable in Linux, the card and antennas are healthy — the problem is purely the Windows driver.
3. If Linux shows the same disconnects, suspect the card seating, antennas, or the card itself.
4. This test cleanly separates the endless "is it hardware or software" debate. For the vanished-adapter variant, see [WiFi disappeared troubleshooting](/articles/how-to-fix-wifi-disappeared-from-laptop-in-windows-11-24h2/).

### Fix 8: Consider a card swap (last resort)

1. Check your service manual — if the WiFi card is a socketed **M.2 2230** card, replacement is straightforward.
2. The **Intel AX210** is the popular upgrade: stable drivers, Wi-Fi 6E support, and wide compatibility.
3. Check for BIOS whitelists on HP and Lenovo business models, which may reject non-approved cards.
4. Also verify antenna connectors (MHF4) carefully — they're tiny and fragile. Microsoft's [Windows support site](https://support.microsoft.com/en-us/windows) documents wireless known issues if you want to confirm a driver regression before spending money.

## Closing

MediaTek WiFi problems are driver-management problems: tame the power settings, install the OEM driver cleanly, and keep Windows Update from replacing it. That trio stabilizes the overwhelming majority of MT7921/MT7922 complaints. The card-swap option exists, but most people never need it once the driver situation is under control. File this trio away for the future: every MediaTek WiFi problem you'll ever meet is some variation of driver, power management, or update regression — and now you know the answer to all three.
