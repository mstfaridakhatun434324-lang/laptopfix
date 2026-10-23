---
title: "Cloud Download Recovery Stuck on ARM Laptops: How to Fix It"
slug: cloud-download-recovery-arm-laptop
date: 2026-10-23
categories: ["ai-pc"]
tags: ["cloud download", "windows recovery", "arm laptop", "reset stuck", "winre", "troubleshooting"]
description: "Fix cloud download recovery stuck on ARM laptops: stabilize the download, repair WinRE, free disk space, and complete the reset step by step."
thumbnail: "/images/thumbs/cloud-download-recovery-arm-laptop.webp"
faqs:
  - q: "How long should cloud download recovery take?"
    a: "The download itself is 4-5GB, so on a fast connection it takes 15-30 minutes, plus installation time. If the progress percentage hasn't moved for over an hour on a good connection, it's genuinely stuck, not just slow."
  - q: "Can I use cloud download recovery without Wi-Fi?"
    a: "You need internet — that's the whole point of cloud download. WinRE includes basic Wi-Fi and Ethernet drivers, but if your ARM laptop's Wi-Fi driver isn't in WinRE, use a USB Ethernet adapter or a USB-C dock with Ethernet."
  - q: "Will cloud download work on a metered connection?"
    a: "Technically yes, but a 4-5GB download will burn through a metered allowance fast. Connect to an unmetered network if possible, and disable any metered-connection download blocks in Settings first."
  - q: "What if the download fails at the same percentage every time?"
    a: "A consistent failure point suggests corrupted local staging, a proxy or firewall blocking Microsoft's servers, or disk errors. Clear the staging area with a network reset, check the firewall, and run chkdsk before retrying."
---

Cloud download is supposed to be the reliable reset path on ARM laptops — a fresh Windows image straight from Microsoft, no local recovery files needed. But sometimes the download stalls at 12%, fails outright, or the recovery environment cannot even reach the internet. The "reliable" path has its own failure modes.

On ARM64 machines the stakes are slightly higher: WinRE's built-in driver set is smaller than on x64, so Wi-Fi in the recovery environment fails more often, and the ARM64 image must be fetched specifically. Every fix below addresses one of these ARM-specific wrinkles.

Work through the six fixes in order: connectivity first, then the recovery environment, then the disk and fallback paths.

## Why this happens

- **No network in WinRE:** The recovery environment loads only basic drivers. If your ARM laptop's Wi-Fi chip lacks a WinRE driver, the cloud download cannot start — the most common ARM-specific failure.
- **Unstable or slow connection:** A flaky Wi-Fi signal turns a 20-minute download into a multi-hour stall. The progress bar barely moves, and eventually the process times out.
- **Insufficient disk space:** Cloud download stages the 4-5GB image on your disk before installing. With less than ~10GB free, the download cannot complete.
- **Corrupted WinRE or staging area:** A damaged recovery environment or leftover partial download from a previous attempt blocks the new download.
- **Firewall, proxy, or DNS interference:** Corporate proxies, aggressive firewalls, or broken DNS in WinRE can block access to Microsoft's download servers while normal browsing (in full Windows) works fine.
- **Metered connection blocks:** If the connection is marked metered, Windows may refuse or throttle the large download.
- **Server-side or account issues:** Rare, but Microsoft's download endpoints can have outages, and some enterprise-managed devices restrict cloud download by policy — a management restriction in the same family as [game install failures on managed ARM devices](/articles/game-pass-arm-laptop-install-failed/).

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Get reliable wired internet into WinRE

Wi-Fi in the recovery environment is the weak link on ARM laptops. A wired connection eliminates the entire class of WinRE Wi-Fi driver problems.

1. Connect a USB Ethernet adapter or a USB-C dock with Ethernet directly to the laptop before starting the reset — WinRE includes generic USB Ethernet drivers that work on ARM.
2. If you must use Wi-Fi, connect to a 2.4GHz network rather than 5GHz in the recovery environment — the basic WinRE Wi-Fi drivers handle 2.4GHz more reliably.
3. Move the laptop close to the router to rule out weak signal as the stall cause.
4. Start the reset via **Settings > System > Recovery > Reset PC > Cloud download** from within Windows (where your full Wi-Fi driver works) rather than from the boot-time recovery menu when possible — the download begins in full Windows, which has proper networking.
5. If the download starts in Windows but stalls, do not cancel immediately — give it a full hour on a known-good connection before declaring it stuck.

### Fix 2: Free disk space and clear stale download state

A previous failed attempt can leave gigabytes of partial download staging that block the retry. Clearing space and stale state gives the new attempt a clean runway.

1. In full Windows, free at least 15GB on C:: empty the Recycle Bin, run **Disk Cleanup** (including system files), and move personal files to external storage.
2. Run **Settings > System > Storage > Temporary files** and remove everything safe — especially "Delivery Optimization Files" and temporary Windows installation files.
3. Open **Settings > Network & internet > Advanced network settings > Network reset** and reset — this clears corrupted network state that can stall downloads.
4. Restart, then retry the cloud download reset from **Settings > System > Recovery**.
5. If it stalls at the exact same percentage as before, the staging area may still hold the corrupt partial file — the WinRE repair in Fix 3 addresses that.

### Fix 3: Repair the Windows Recovery Environment

A damaged WinRE produces download failures that look like network problems. Verifying and rebuilding it is quick.

1. Open **Terminal as administrator** and run `reagentc /info` — confirm "Windows RE status: Enabled".
2. If disabled, run `reagentc /enable`; if enabling fails, run `reagentc /disable` followed by `DISM /Online /Cleanup-Image /RestoreHealth`, then `reagentc /enable` again.
3. Confirm with `reagentc /info` that WinRE is enabled with a valid location.
4. Retry the cloud download. A healthy WinRE with a clean image resolves the "download fails immediately" pattern.
5. For the broader reset-failure context — when the reset itself (not just the download) is the problem — see [fixing failed Reset This PC on ARM](/articles/reset-this-pc-arm-laptop-failed/).

### Fix 4: Bypass proxy, firewall, and DNS issues

If the download fails while general internet works, something is filtering Microsoft's endpoints. Corporate and school networks are the usual suspects.

1. If you are on a corporate, school, or VPN network, switch to a plain home network or phone hotspot for the download — proxies and firewalls on managed networks commonly block the download endpoints.
2. Disconnect any VPN before starting the reset — VPN drivers do not load in WinRE anyway, and a half-configured VPN can break the handoff.
3. In full Windows, temporarily disable third-party firewalls and security suites during the download phase.
4. Try changing DNS to a public resolver (in **Settings > Network & internet > your connection > DNS settings**, set manual DNS to 8.8.8.8 / 1.1.1.1) before starting the reset.
5. Retry the download. If it works on the hotspot but not the office network, the network — not the laptop — was the blocker all along.

### Fix 5: Check the metered connection setting

Windows treats metered connections as precious and may refuse a 4GB download on them. This setting hides in the Wi-Fi properties and is easy to overlook.

1. In **Settings > Network & internet > Wi-Fi**, click your connected network and check **Metered connection** — set it to **Off** for the download.
2. Also check **Settings > Windows Update > Advanced options > Delivery Optimization** — ensure downloads are allowed and not restricted.
3. If you are on a genuinely metered connection (mobile hotspot with a cap), be aware the download is 4-5GB — connect to unmetered Wi-Fi if at all possible.
4. Restart the reset flow after changing the setting; the metered flag is read at the start of the download process.
5. After the reset completes, you can re-enable the metered flag if you need it.

### Fix 6: Fall back to ARM64 installation media

When cloud download will not cooperate despite good networking, external media achieves the same fresh-install result without depending on WinRE's networking at all.

1. On another computer, download the Windows 11 ARM64 ISO from [Microsoft's Windows 11 download page](https://www.microsoft.com/en-us/software-download/windows11).
2. Create a bootable USB with Rufus using the ARM64 ISO.
3. Boot the laptop from the USB and choose **Install now** for a clean install, or **Repair your computer > Troubleshoot** for recovery options.
4. During setup, delete the old Windows partitions only if you have backups — a clean install is destructive by design.
5. After installation, run Windows Update fully to pull ARM64 drivers, then reinstall apps. Developers rebuilding their toolchain afterward should grab the [ARM64 Git setup](/articles/git-arm64-windows-setup/) early — it is one of the first tools you will miss. And if you are curious what the fresh system's AI hardware can actually do, [NPU performance specs](/articles/npu-tops-explained-real-world/) make a good post-install read.

## Closing

Cloud download recovery on ARM laptops fails at the network layer more than anywhere else: WinRE's limited Wi-Fi drivers, metered flags, proxies, and stale staging. Get wired Ethernet into the recovery environment, free ample disk space, repair WinRE, and keep ARM64 USB media as the fallback — the fresh install is always reachable one way or another.
