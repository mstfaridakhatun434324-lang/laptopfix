---
title: "How to Fix Miracast Not Working on Your Snapdragon Laptop"
slug: miracast-not-working-snapdragon-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["miracast", "wireless display", "snapdragon", "arm laptop", "windows 11", "troubleshooting"]
description: "Fix Miracast wireless display on your Snapdragon laptop with step-by-step Wi-Fi driver checks, Connect app repair, firewall rules, and receiver troubleshooting."
thumbnail: "/images/thumbs/miracast-not-working-snapdragon-laptop.webp"
faqs:
  - q: "Why does my Snapdragon laptop say Miracast is not supported?"
    a: "The 'not supported' message usually comes from the Wi-Fi driver, not the hardware — Snapdragon laptops support Miracast via Wi-Fi Direct, but a generic or outdated ARM Wi-Fi driver may not expose it. Installing the OEM Wi-Fi driver is the fix in most cases."
  - q: "Does Miracast work on 5GHz networks?"
    a: "Miracast uses Wi-Fi Direct, which negotiates its own connection independent of your router — but both devices must have Wi-Fi turned on, and some receivers only negotiate on 2.4GHz. Keep Wi-Fi enabled on the laptop even though no router is involved."
  - q: "Can a VPN or firewall block Miracast?"
    a: "Yes. Miracast discovery uses local network broadcast traffic that VPNs tunnel away and firewalls can block. Disconnect the VPN and allow the Wireless Display / Connect app through Windows Firewall when troubleshooting."
  - q: "Is Miracast different from the Connect app?"
    a: "They're two sides of the same feature: Miracast is the wireless display protocol for projecting FROM your laptop to a TV or dongle, while the Connect app (Wireless Display feature) lets other devices project TO your laptop. Both depend on the same Wi-Fi Direct driver support."
---

You hit **Win + K**, pick your TV, and… "Couldn't connect," or worse, the cast panel says your device doesn't support Miracast at all. On Snapdragon-powered Copilot+ laptops, Miracast failures are frustratingly common — and the culprit is rarely the TV. It's the Wi-Fi driver stack on the ARM side, which handles the Wi-Fi Direct connection Miracast depends on.

Miracast doesn't use your router. It builds a direct Wi-Fi Direct link between the laptop and the receiver, then streams the display over it. That means the entire feature lives or dies on whether the ARM Wi-Fi driver exposes Wi-Fi Direct properly — the same class of driver-exposure problem that breaks hardware features across the platform, from [NPU DirectML failures](/articles/stable-diffusion-npu-directml-error/) to missing installer components.

This guide gives you six fixes in technician order: quick checks first, then Wi-Fi driver repair, then the Windows feature and firewall layer, then receiver-side troubleshooting. Work through them in sequence and retry the cast after each step.

## Why this happens

- **ARM Wi-Fi driver missing Wi-Fi Direct support:** The single most common cause — a generic or outdated Wi-Fi driver on the Snapdragon laptop doesn't expose the Wi-Fi Direct / Miracast capability Windows checks for.
- **"Wireless Display" optional feature not installed:** Projecting *to* the laptop requires the Wireless Display feature (the Connect app); on some installs it's missing and needs adding manually.
- **Firewall blocking discovery traffic:** Miracast discovery uses local broadcast traffic that Windows Firewall — or a third-party security suite — can silently block.
- **VPN tunneling discovery away:** An active VPN routes local network traffic through the tunnel, which breaks the device discovery Miracast depends on.
- **Receiver incompatibility or outdated firmware:** The TV, dongle, or streaming stick may need a firmware update, a settings toggle (screen mirroring input), or simply a reboot to accept connections.
- **Driver or feature broken by an update:** Like [ARM64 installer components that break after updates](/articles/visual-studio-arm64-installer-issues/), Miracast's driver chain can regress when Windows Update swaps in a mismatched Wi-Fi driver.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Run the quick pre-checks

Half of Miracast failures are environmental, not technical. Two minutes of checks here saves a driver reinstall — and confirms Wi-Fi Direct is even possible on your hardware.

1. Press **Win + K** and read the exact message: "Your device doesn't support Miracast" means a driver problem (skip to Fix 2); "Couldn't connect" means discovery or receiver trouble (keep going here).
2. Make sure **Wi-Fi is turned ON** on the laptop — Miracast needs the radio active even though no router is involved. Airplane mode must be off.
3. Disconnect any active **VPN** completely (not just paused) — VPNs break local discovery.
4. Put the TV/receiver on its **screen mirroring / Miracast input** explicitly; many TVs only listen for connections on that input.
5. Move within a few meters for the test and retry the cast — weak signal causes exactly the flaky "couldn't connect" behavior people blame on drivers.

### Fix 2: Reinstall the OEM Wi-Fi driver

If Windows says Miracast isn't supported, the Wi-Fi driver is lying to it. Snapdragon laptops need the maker's validated ARM Wi-Fi driver — the generic one Windows Update sometimes installs may lack Wi-Fi Direct entirely.

1. Open **Device Manager > Network adapters**, right-click your Wi-Fi adapter, choose **Properties > Driver**, and note the driver date and provider.
2. Open an elevated Terminal and run `Get-NetAdapter | Select Name, InterfaceDescription` followed by `netsh wlan show drivers` — look for the **"Wireless Display Supported"** line; it must say **Yes**.
3. If it says No (or the adapter looks generic), download the latest Wi-Fi driver for Windows 11 on ARM for your exact model from [Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), or [Lenovo](https://support.lenovo.com/us/en/).
4. Install as administrator, restart, and rerun `netsh wlan show drivers` — confirm "Wireless Display Supported: Yes" before testing the cast.
5. If a future Windows Update swaps the driver again and Miracast breaks, check [Microsoft's Windows support pages](https://support.microsoft.com/en-us/windows) for blocking that specific driver update.

### Fix 3: Add the Wireless Display feature and repair the Connect path

Projecting *to* your Snapdragon laptop — using it as the receiver — needs the Wireless Display optional feature. It's also worth repairing even if you only cast outward, since the two share components.

1. Open **Settings > System > Optional features > View features**, search for **Wireless Display**, check it, and install.
2. After installation, search the Start menu for **Wireless Display** (the Connect app) and open it once — it must be running to receive connections.
3. In the app's settings, set **"Some Windows and Android devices can project to this PC when you say it's OK"** to **Available everywhere** (or "on secure networks") for testing.
4. Try projecting from a phone to the laptop to verify the receive path works — this isolates whether the problem is outbound-only.
5. If the feature fails to install, run Windows Update first — the same update-channel issues that break [DirectML fallback paths](/articles/onnxruntime-directml-fallback-cpu/) can stall optional-feature downloads too.

### Fix 4: Open the firewall and check network profile

Miracast discovery traffic looks suspicious to firewalls — it's unsolicited local broadcast. Windows Firewall usually allows the Connect app automatically, but third-party suites and hardened profiles don't.

1. Open **Windows Security > Firewall & network protection > Allow an app through firewall** and confirm **Wireless Display** / **Connect** is allowed on Private (and Public, for testing).
2. Check your network profile in **Settings > Network & internet > Wi-Fi > your network** — set it to **Private**; Public profiles apply stricter firewall rules that can block discovery.
3. If you run a third-party antivirus/firewall, temporarily disable its firewall component (keep antivirus on) and retry the cast — re-enable afterward and add an exception if this was the cause.
4. In an elevated Terminal, run `netsh advfirewall reset` only if you suspect corrupted rules — this restores defaults, so note any custom rules first.
5. Retry **Win + K** after each change; firewall blocks produce instant "couldn't connect" failures, so you'll know immediately when it's fixed.

### Fix 5: Update and reset the receiver side

When the laptop checks out — driver good, firewall open — but the TV or dongle still won't connect, the receiver is the problem. Receivers fail just as often as laptops, and they're easier to fix.

1. Reboot the TV, streaming stick, or Miracast dongle fully (unplug for 30 seconds, not just standby) — receiver firmware gets into bad states regularly.
2. Check the receiver's settings for a **screen mirroring / Miracast / wireless display** toggle and make sure it's enabled; install any pending firmware update for the TV or dongle.
3. Remove the laptop from the receiver's paired/remembered devices list and re-pair from scratch — stale pairings cause cryptic failures.
4. If the TV supports it, try a different mirroring protocol path (some TVs expose both Miracast and a proprietary cast) to confirm the TV's wireless hardware works at all.
5. Test with a phone casting to the same receiver — if the phone also fails, you've proven the receiver is at fault and can stop troubleshooting the laptop.

### Fix 6: Reset the network stack on the laptop

When everything looks right but connections still fail or drop mid-stream, corrupted network state — stale Wi-Fi Direct virtual adapters, bad Winsock catalogs — is the last suspect.

1. In Device Manager, expand **Network adapters**, show hidden devices (**View > Show hidden devices**), and uninstall any greyed-out **Microsoft Wi-Fi Direct Virtual Adapter** entries.
2. In an elevated Terminal, run `netsh winsock reset` and `netsh int ip reset`, then restart the laptop.
3. After reboot, go to **Settings > Network & internet > Advanced network settings > Network reset** and run it — this reinstalls all network adapters and resets every network component to defaults.
4. Reconnect to your Wi-Fi network, reinstall the OEM Wi-Fi driver from Fix 2 if the reset replaced it, and verify `netsh wlan show drivers` still reports Wireless Display: Yes.
5. Retry the cast as the final test — a clean network stack plus a validated driver resolves the remaining stubborn cases.

## Closing

Miracast on a Snapdragon laptop lives or dies on the Wi-Fi driver exposing Wi-Fi Direct — check `netsh wlan show drivers` first, install the OEM ARM Wi-Fi driver second, and only then chase firewalls, VPNs, and receiver firmware. The TV is guilty far less often than the driver stack makes it look.
