---
title: "Airplane Mode Stuck On? Get Your Laptop's Radios Back"
slug: how-to-fix-airplane-mode-stuck-on-youtube
date: 2026-09-14
categories: ["drivers"]
tags: ["airplane mode", "wifi radio", "wireless", "troubleshooting", "network"]
description: "Airplane mode won't turn off and WiFi/Bluetooth are dead? Fix the stuck radio switch with driver, service, and BIOS steps in order."
thumbnail: "/images/thumbs/how-to-fix-airplane-mode-stuck-on-youtube.webp"
faqs:
  - q: "Why is airplane mode stuck on with the toggle grayed out?"
    a: "A grayed-out toggle means Windows can't communicate with the radio hardware — usually a crashed WiFi/Bluetooth driver, a disabled radio management service, or a physical switch stuck in the off position. The OS isn't refusing; it literally can't reach the radios to switch them."
  - q: "Can a physical switch cause airplane mode to stick?"
    a: "Yes, and it's the first thing to check. Many laptops have a physical WiFi switch or an Fn-key radio toggle. If the hardware switch is off, Windows shows airplane mode as stuck on and no software toggle will override it — the hardware state wins."
  - q: "Does airplane mode stuck on mean my WiFi card is dead?"
    a: "Rarely. A dead card usually vanishes from Device Manager rather than showing airplane mode. Stuck airplane mode with the adapter still visible points to driver state, the Radio Management Service, or a switch — all fixable in software in most cases."
  - q: "Why did airplane mode get stuck after a Windows update?"
    a: "Updates can replace the WiFi driver with an incompatible version, reset the Radio Management Service to disabled, or corrupt the radio state that Windows stored. The driver rollback in Fix 3 specifically targets this update-induced variant. If the problem started with a feature update, a System Restore to the pre-update point is also worth trying before deeper driver surgery."
---

Airplane mode is supposed to be a toggle. When it gets stuck on — grayed out, unresponsive, or snapping back on the instant you turn it off — your WiFi and Bluetooth go with it, and the laptop becomes an island. The frustrating part is that the toggle *looks* like a simple switch while the actual fault hides in the radio driver, a Windows service, or a physical switch you forgot existed.

The diagnostic split is simple: if a physical switch or Fn key controls it, that's hardware state and software can't override it. If it's purely software, the Radio Management Service and the WiFi driver are the two suspects. Check in that order.

## Why this happens

- **A physical radio switch is off.** Side switches and Fn-key toggles set hardware state that Windows cannot override — the toggle grays out.
- **The WiFi driver crashed or is incompatible.** When Windows can't talk to the radio, it parks the UI in airplane mode. Compare [AX201 driver faults](/articles/how-to-fix-intel-wifi-6-ax201-not-working-in-windows-11-24h2/).
- **Radio Management Service is stopped or disabled.** This Windows service brokers radio state; without it, airplane mode can't change.
- **Corrupted radio state after sleep/hibernate.** Resume bugs can leave the radio stack believing airplane mode is on with no way to clear it through the UI.
- **Windows Update driver replacement.** A new-but-wrong WiFi driver can break radio control while leaving basic driver loading intact.
- **BIOS-level wireless disable.** Some BIOS setups have a wireless toggle; if off, Windows sees no radios to manage.
- **Third-party "airplane mode" utilities.** Manufacturer utilities (especially on business laptops) can fight Windows' own radio management.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Check every physical radio control

Hardware state beats software every time.

1. Inspect the laptop's sides and front edge for a physical **WiFi/wireless switch**. Flip it on.
2. Press **Fn + the radio key** (tower icon, often F2/F3/F12). Press it deliberately and watch for an on-screen radio indicator.
3. Check for a dedicated **airplane mode key** — some laptops have one that toggles with a single press and no Fn.
4. If your laptop has a manufacturer utility (Lenovo Vantage, Dell Optimizer, HP Support Assistant), check its radio/wireless settings — these can override Windows.
5. After flipping any hardware control, wait 10 seconds and check whether the Windows airplane mode toggle becomes responsive.

### Fix 2: Restart the Radio Management Service

The service that actually flips the radios.

1. Press **Win + R**, type `services.msc`, and find **Radio Management Service**.
2. If it's not **Running**, right-click > **Start**. Set **Startup type** to **Manual** (its normal setting) — if it's Disabled, that's your problem.
3. Also verify **WLAN AutoConfig** and **Bluetooth Support Service** are running.
4. Try the airplane mode toggle again (Action Center or Settings > Network & internet).
5. If the service won't start or immediately stops, note any error — then continue to the driver fixes, because a broken radio driver can prevent the service from functioning.

### Fix 3: Roll back or reinstall the WiFi driver

For update-induced stuck airplane mode.

1. Open **Device Manager** > **Network adapters**. Right-click your WiFi adapter > **Properties** > **Driver** tab.
2. If **Roll Back Driver** is available, use it — this is the fastest fix when an update caused the problem. Restart and test.
3. If not available: **Uninstall device** (check "Attempt to remove the driver"), restart, then install the driver from your laptop maker's support page — for Lenovo, [Lenovo support](https://support.lenovo.com/us/en/).
4. Do the same for the **Bluetooth** adapter if Bluetooth is also stuck — combo cards share the radio state.
5. After reinstalling, recheck the Radio Management Service (Fix 2) — driver reinstalls can leave it in a bad state.

### Fix 4: Clear the stuck state via Settings and registry-adjacent resets

When the toggle moves but snaps back.

1. Go to **Settings** > **Network & internet** > **Airplane mode**. Toggle it off here rather than in Action Center — the Settings page writes state more reliably.
2. Restart into **Safe Mode** (Settings > System > Recovery > Advanced startup). In Safe Mode, toggle airplane mode off, then restart normally — Safe Mode bypasses third-party interference.
3. Run the **Network Adapter troubleshooter**: Settings > System > Troubleshoot > Other troubleshooters.
4. As a stronger reset: **Settings** > **Network & internet** > **Advanced network settings** > **Network reset**, then restart and reconfigure.

### Fix 5: Check BIOS and power-drain the radio

For radios invisible or unresponsive at the hardware level.

1. Reboot into **BIOS/UEFI** and verify **Wireless**, **WLAN**, and **Bluetooth** are all **Enabled**.
2. Shut down fully, unplug everything, and hold the power button **30 seconds** to drain residual power — this resets radio firmware wedged in airplane state.
3. Boot up and immediately check Device Manager: the WiFi and Bluetooth adapters should be present without warnings.
4. If the adapters are missing from Device Manager even after this, check **View** > **Show hidden devices** — then suspect hardware (Fix 7).

### Fix 6: Remove conflicting software

Third-party radio managers fight Windows.

1. Uninstall manufacturer "connection manager" or "wireless utility" software you don't use — keep only one radio manager (Windows' own).
2. Temporarily uninstall **VPN clients** — their filter drivers can interfere with radio state changes.
3. Check **Task Manager** > **Startup** for wireless utilities launching at boot and disable the non-essential ones.
4. Retest the toggle after each removal so you know which one was fighting.

### Fix 7: Verify the hardware

The final verdict.

1. Boot a **Linux live USB** and check whether WiFi/Bluetooth radios work there. Working in Linux = Windows problem (revisit Fixes 2–4). Dead in Linux = hardware or BIOS.
2. If the card is a removable M.2 module, reseat it and its antenna wires per the service manual.
3. A radio that works in Linux but never in Windows across clean installs points to a deep Windows/radio-firmware incompatibility — check for BIOS updates from the manufacturer.
4. Stopgap: a USB WiFi adapter restores connectivity regardless of the internal radio's state.

The [stuck-airplane-mode variant guide](/articles/how-to-fix-airplane-mode-stuck-on-after-windows-11-update/) covers additional scenarios for newer Windows builds.

## Closing

Stuck airplane mode is a state problem, not a toggle problem: something — a physical switch, a stopped service, a replaced driver, a wedged firmware state — is holding the radios off, and the UI is just reporting it. Check hardware controls first, restart the Radio Management Service, rebuild the WiFi driver, clear the stuck state, and power-drain the firmware. One of those releases the radios, and the toggle starts behaving like a toggle again.
