---
title: "Fix Windows Update Error 0x80072ee2 on Windows 10 (Solved Step by Step)"
slug: how-to-fix-windows-update-error-0x80072ee2-on-windows-10
date: 2026-09-12
categories: ["windows-update"]
tags: ["windows update", "0x80072ee2", "troubleshooting", "windows 11", "windows 10"]
description: "Error 0x80072ee2 on Windows 10 means Windows Update timed out contacting Microsoft's servers. These step-by-step fixes repair the connection so updates install cleanly."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80072ee2-on-windows-10.webp"
faqs:
  - q: "What does error 0x80072ee2 actually mean?"
    a: "Error 0x80072ee2 translates to ERROR_INTERNET_TIMEOUT. It means the Windows Update client on your Windows 10 laptop started a connection to Microsoft's update servers but received no response before the timeout expired. The failure is in the network path — proxy, firewall, DNS, or connectivity — rather than in the update files themselves, which is why network-focused fixes resolve it."
  - q: "Can a VPN cause Windows Update error 0x80072ee2?"
    a: "Yes. VPN clients reroute traffic through their own tunnels and sometimes leave stale proxy or DNS settings behind even after disconnecting. These leftovers redirect update requests into dead ends, producing the timeout. Disconnect the VPN, reset the WinHTTP proxy with `netsh winhttp reset proxy`, flush DNS, and retry the update to confirm the VPN was responsible."
  - q: "Why does 0x80072ee2 appear only on some networks?"
    a: "Because the cause travels with the network, not the laptop. A corporate proxy, a hotel captive portal, or an ISP with aggressive filtering can block the specific endpoints Windows Update needs while normal browsing works fine. If the error follows you between home, office, and mobile hotspot, the pattern tells you which network's policy is interfering."
  - q: "Will resetting SoftwareDistribution delete my installed updates?"
    a: "No. Renaming the SoftwareDistribution folder only clears the download cache and the update history log. Updates already installed on your Windows 10 system stay installed, and Windows rebuilds the folder automatically on the next check. It is one of the safest resets in Windows troubleshooting."
---
On Windows 10, error 0x80072ee2 means Windows Update tried to contact Microsoft's servers and the connection timed out. Your update components are almost certainly fine — the request simply never completed, which points at the network path: proxy settings, firewall rules, DNS, or a connection that Windows has marked as metered.

This is a common sight on office laptops behind corporate proxies, on machines running aggressive third-party firewalls, and after VPN software changes the routing. The good news is that because no update files were touched, you can reset the whole download pipeline without risking your installed updates.

The [Windows 11 guide](/articles/how-to-fix-windows-update-error-0x80072ee2-on-windows-11/) walks through the same error on Windows 11, while the [companion guide for 0x80246007](/articles/how-to-fix-windows-update-error-0x80246007-on-windows-10/) helps when the download starts but stalls partway. The fixes below are ordered from quickest to most thorough.

## Why this happens

- **The request timed out at the network layer:** 0x80072ee2 is ERROR_INTERNET_TIMEOUT: your laptop's request to the update server got no reply in time, so Windows Update gave up and reported the timeout.
- **A proxy server is misconfigured or unreachable:** If a proxy is set — by your employer, a VPN client, or leftover software — and it no longer responds, every update request dies waiting for the proxy instead of reaching Microsoft directly.
- **Firewall or antivirus is silently blocking traffic:** Third-party security suites sometimes block the Background Intelligent Transfer Service or the Windows Update service itself, which looks exactly like a server timeout from the update engine's point of view.
- **DNS cannot resolve the update servers:** If your DNS server is slow, hijacked by ISP redirection, or failing, the update client cannot even find Microsoft's servers to begin the download, producing the same timeout code.
- **The connection is flagged as metered:** Windows pauses most update downloads on metered connections. When the engine tries anyway — for a critical patch — the stalled download can surface as 0x80072ee2.
- **VPN or network filtering interferes mid-download:** VPN tunnels, hotel or campus captive portals, and content filters can break the long-lived connections that large update downloads need, causing timeouts partway through.
- **The local download queue is corrupted:** A previously interrupted download can leave the Background Intelligent Transfer Service with a stuck job that blocks every new attempt, so each retry times out against the jammed queue.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the basics: clock, connectivity, and metered status

Open Settings > Update & Security > Windows Update and confirm the page loads cleanly, then check Settings > Update & Security > Troubleshoot > Additional troubleshooters is reachable. Fix the clock first — it is the cheapest win on this list.

1. Right-click the clock in the taskbar, choose Adjust date/time, and enable Set time automatically, then Set time zone automatically.
2. Open a browser and load any website to confirm general internet access works outside Windows Update.
3. Go to Settings > Network & internet (or Network & Internet on Windows 10), select your Wi-Fi network, and make sure Metered connection is off.
4. Disconnect any VPN temporarily and retry the update to see whether the tunnel was the culprit.
5. Restart the laptop once — this clears transient socket states — then check for updates again.

### Fix 2: Bypass or reset the proxy configuration

After the reset, Windows Update connects directly to Microsoft's servers. Corporate users should check with IT before changing proxy settings permanently.

1. Open Settings > Network & internet > Proxy and turn off Automatically detect settings and Use a proxy server if they are enabled without your knowledge.
2. Open Command Prompt as administrator.
3. Run `netsh winhttp reset proxy` to clear the system-level proxy that services like Windows Update use.
4. Run `netsh winhttp show proxy` to confirm it now reports Direct access (no proxy server).
5. Restart the Windows Update service from Services, then check for updates again.

### Fix 3: Let Windows Update through the firewall and antivirus

Never leave protection off longer than the test — disable, retry the update, then re-enable immediately. If the update succeeds with the suite disabled, add exclusions for the update services instead of leaving the machine exposed.

1. Open Windows Security > Firewall & network protection and confirm the firewall is on for your active network profile.
2. In your third-party antivirus, temporarily disable real-time protection and any web shield or firewall component.
3. Open Settings > Update & Security > Windows Update and click Check for updates while protection is paused.
4. If it works, re-enable protection and add exclusions for `svchost.exe` BITS traffic or the Windows Update service per your vendor's docs.
5. As a cross-check, Microsoft's [Windows support hub](https://support.microsoft.com/en-us/windows) documents the required service endpoints if your firewall uses allow-lists.

### Fix 4: Flush DNS and reset the network stack

This is a standard technician step for any timeout-class update error and takes under two minutes. Your saved Wi-Fi passwords are preserved; only the low-level stack state is rebuilt.

1. Open Command Prompt as administrator.
2. Run `ipconfig /flushdns` followed by `ipconfig /registerdns`.
3. Run `netsh winsock reset` and then `netsh int ip reset`.
4. Restart the laptop so the stack rebuilds cleanly.
5. After reboot, open Settings > Update & Security > Windows Update and retry the update check.

### Fix 5: Reset the Windows Update components and BITS queue

Renaming rather than deleting keeps a backup in place, and Windows recreates both folders automatically. Your installed updates and personal files are untouched — only the download cache is refreshed.

1. Open Command Prompt as administrator.
2. Run `net stop wuauserv`, `net stop bits`, `net stop cryptsvc`, and `net stop msiserver`.
3. Run `ren C:\Windows\SoftwareDistribution SoftwareDistribution.old` and `ren C:\Windows\System32\catroot2 catroot2.old`.
4. Run `net start wuauserv`, `net start bits`, `net start cryptsvc`, and `net start msiserver`.
5. Check for updates again in Settings > Update & Security > Windows Update.

### Fix 6: Run the Windows Update troubleshooter

On either OS the troubleshooter lives one level inside the Troubleshoot settings page, and it takes about five minutes to complete its checks.

1. Open Settings > Update & Security > Troubleshoot > Additional troubleshooters.
2. Select Windows Update and click Run.
3. Apply every fix it recommends, even ones that look unrelated.
4. Restart when it finishes, then check for updates.
5. For persistent cases, Microsoft's Windows support hub has guided walkthroughs for this exact error code.

### Fix 7: Download the update manually from the Microsoft Update Catalog

This is also the fastest way to confirm the problem is delivery-related rather than system-related: if the manual package installs cleanly, your Windows installation is healthy and only the automatic download path needs repair.

1. In Settings > Update & Security > Windows Update, note the KB number of the update that keeps failing.
2. Visit the Microsoft Update Catalog site and search for that KB number.
3. Download the package matching your system architecture (x64 for most modern laptops).
4. Double-click the downloaded .msu file and follow the installer prompts.
5. Restart when prompted, then run a normal update check to confirm the queue is clear.

## Closing

On Windows 10, 0x80072ee2 is rarely a sign of system damage — it is the update engine telling you the road to Microsoft's servers is blocked. Proxy resets, firewall checks, and a clean download queue resolve the large majority of cases. Keep the manual Catalog download in your back pocket for stubborn networks, and your updates will stay current without drama.
