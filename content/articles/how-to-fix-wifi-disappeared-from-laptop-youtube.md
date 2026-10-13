---
title: "Wi-Fi Disappeared From Your Laptop? Get It Back"
slug: how-to-fix-wifi-disappeared-from-laptop-youtube
date: 2026-09-04
categories: ["drivers"]
tags: ["wifi disappeared", "wifi missing", "wireless fix", "windows 11", "network"]
description: "Wi-Fi option completely gone from your laptop? Recover the vanished Wi-Fi with driver, service, and hardware checks that actually work."
thumbnail: "/images/thumbs/how-to-fix-wifi-disappeared-from-laptop-youtube.webp"
faqs:
  - q: "Why did the Wi-Fi option disappear from my laptop entirely?"
    a: "The Wi-Fi section vanishes from Settings when Windows can't communicate with the wireless adapter — a corrupted driver, a disabled device, a stopped WLAN service, or a failed wireless card. The distinction that matters: if the adapter is still in Device Manager, it's software and fixable. If it's gone from Device Manager too, work through driver recovery and BIOS checks before suspecting hardware."
  - q: "How do I get the Wi-Fi icon back on my taskbar?"
    a: "The taskbar icon returns automatically once the underlying problem is fixed — it's a symptom, not the problem. But first check it's not just hidden: open Quick Settings (Win+A) and look for the Wi-Fi tile, and check Settings > Personalization > Taskbar > System tray icons. If Wi-Fi is genuinely gone from Settings > Network & internet, the adapter itself needs recovery."
  - q: "Can airplane mode make Wi-Fi disappear?"
    a: "A stuck airplane mode can hide Wi-Fi options and make the adapter seem gone. Check Settings > Network & internet for an airplane mode toggle stuck on. If the toggle won't move, the radio management service or wireless driver is the real problem — fixing that restores both airplane mode control and Wi-Fi."
  - q: "What if Wi-Fi disappeared after a Windows update?"
    a: "This is the most common trigger. Feature updates replace wireless drivers with incompatible versions or corrupt the driver's registration. The fix is reinstalling the wireless driver from your laptop manufacturer's site — downloaded on another device if necessary. Rolling back the driver in Device Manager also works if the option is available."
---

One minute you're browsing, the next the Wi-Fi section is simply gone — not disconnected, gone. No Wi-Fi in Settings, no Wi-Fi tile in Quick Settings, and the taskbar shows a globe icon or an ethernet-only menu. Video tutorials on this problem get millions of views because it's both common and terrifying: your laptop has forgotten how to do wireless.

The recovery is methodical. Wi-Fi disappears for a short list of reasons — the WLAN service stopped, the adapter got disabled, the driver corrupted (very often right after a Windows update), or the hardware failed. Each has a distinct fingerprint, and this guide reads them in order from quickest to deepest. Your phone is your backup internet for downloading drivers; keep it charged. And don't be misled by the taskbar icon: a globe icon means Windows sees no network path at all, which is consistent with every cause on this list, so it tells you nothing about which one you're facing.

## Why this happens

- **WLAN AutoConfig service stopped:** This Windows service manages all wireless connections; if it's disabled or crashed, the entire Wi-Fi UI disappears.
- **Driver corrupted by Windows update:** Feature updates are the number one trigger — they replace or damage the wireless driver, and Wi-Fi vanishes on the next boot.
- **Adapter disabled:** The Wi-Fi adapter can be disabled in Device Manager, by a function key, or by power management — disabled means invisible in Settings.
- **Airplane mode stuck on:** A jammed airplane mode state hides Wi-Fi controls and blocks the radio; the toggle and the Wi-Fi section fail together.
- **Network adapter missing from Device Manager:** When the driver registration corrupts badly enough, the adapter itself disappears — the deeper variant covered in the [missing adapter guide](/articles/how-to-fix-network-adapter-missing-in-windows-11-24h2/).
- **BIOS wireless disabled:** A firmware-level disable hides the card from Windows completely — no driver or service fix can reach it.
- **Corrupted network profiles/stack:** Damaged wireless profiles or Winsock corruption can cascade into the Wi-Fi UI failing to load.
- **Failed wireless card:** Hardware death is real but it's the last suspect, not the first — confirm with diagnostics before concluding it.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check Quick Settings and airplane mode

1. Press **Win+A** to open Quick Settings. Look for the Wi-Fi tile — is it missing, or just off?
2. Go to **Settings > Network & internet** and check whether a Wi-Fi section exists at all, and whether airplane mode is stuck on.
3. Try your laptop's wireless function key (often Fn+F2/F3/F12 with an antenna icon) — a hardware-level radio toggle can hide Wi-Fi from Windows.
4. If airplane mode is stuck on, the [airplane mode recovery](/articles/how-to-fix-airplane-mode-stuck-on-in-windows-11-24h2/) fixes that root cause directly.

### Fix 2: Restart the WLAN AutoConfig service

1. Press **Win+R**, type `services.msc`, and press Enter.
2. Find **WLAN AutoConfig**, right-click, and choose **Restart** (or **Start** if it's stopped).
3. Double-click it and set **Startup type** to **Automatic**.
4. Check Settings again — if the Wi-Fi section reappears, a stalled service was the whole story.

### Fix 3: Re-enable the adapter in Device Manager

1. Open Device Manager (**Win+X > Device Manager**) and expand **Network adapters**.
2. If your Wi-Fi adapter shows a down arrow, right-click and choose **Enable device**.
3. If it's not listed, click **View > Show hidden devices**, then **Action > Scan for hardware changes**.
4. Right-click the adapter > **Properties > Power Management** and uncheck **Allow the computer to turn off this device to save power**.

### Fix 4: Reinstall the wireless driver

1. In Device Manager, right-click the Wi-Fi adapter, choose **Uninstall device**, and tick **Attempt to remove the driver for this device**.
2. Restart — Windows will attempt a fresh install.
3. If Wi-Fi is still gone, download the wireless driver from your laptop manufacturer's support site using your phone, transfer it via USB, and install it manually.
4. For Intel cards, the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html) (run from another PC if needed) identifies the exact driver package.

### Fix 5: Reset the network stack and profiles

1. Open Terminal as administrator (**Win+X > Terminal (Admin)**).
2. Run `netsh winsock reset`, `netsh int ip reset`, and `netsh wlan delete profile name=*` (this clears all saved Wi-Fi networks — you'll re-enter passwords).
3. Restart and check for the Wi-Fi section. This clears corruption in the wireless configuration store that can suppress the entire Wi-Fi UI.

### Fix 6: Check the BIOS wireless setting

1. Restart and enter the BIOS (F2/Del/F10 depending on brand).
2. Find the wireless/WLAN device setting and confirm it's **Enabled**.
3. Run the built-in hardware diagnostics' wireless test if available — a pass means hardware is fine and Windows-side fixes are the answer.
4. Save and exit. If the BIOS shows no wireless device at all, the card may have failed or worked loose.

### Fix 7: Rule out hardware failure

1. If the adapter is invisible in Device Manager even after rescans, absent in BIOS, and failing diagnostics, the wireless card is the prime suspect.
2. A USB Wi-Fi adapter (inexpensive, plug-and-play) restores Wi-Fi in minutes as a workaround or permanent fix.
3. Internal card replacement is a standard M.2 swap on most laptops — match the form factor and antenna connectors. Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) offers additional guided recovery for persistent cases.

## Closing

Vanished Wi-Fi is a recovery problem, not a mystery: the WLAN service, the adapter's enabled state, the driver, and the BIOS setting account for nearly every case. Work them in order and the Wi-Fi section comes back — usually at the driver step, since Windows updates cause most of these disappearances. Only when the card is invisible to the BIOS itself is it time to talk about replacement hardware.
