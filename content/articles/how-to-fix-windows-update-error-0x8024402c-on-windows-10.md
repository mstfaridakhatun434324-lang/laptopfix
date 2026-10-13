---
title: "Fix Windows Update Error 0x8024402C on Windows 10: Connection Failed"
slug: how-to-fix-windows-update-error-0x8024402c-on-windows-10
date: 2026-09-10
categories: ["windows-update"]
tags: ["windows 10", "windows update", "error 0x8024402c", "proxy", "winhttp"]
description: "Error 0x8024402C on Windows 10 means the update service can't reach Microsoft's servers. Fix WinHTTP proxy, DNS, and VPN leftovers with these steps."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x8024402c-on-windows-10.webp"
faqs:
  - q: "What does 0x8024402C mean on Windows 10?"
    a: "It is a connection failure: the Windows Update service could not resolve or reach Microsoft's update servers. The cause is almost always local — a stale WinHTTP proxy, leftover VPN configuration, DNS problems, or a firewall blocking the service — rather than a Microsoft outage."
  - q: "Where is the WinHTTP proxy set on Windows 10?"
    a: "It is separate from Internet Explorer/Edge proxy settings and is managed via the netsh command: 'netsh winhttp show proxy' displays it and 'netsh winhttp reset proxy' clears it. Many users do not know it exists, which is why this error persists through browser-proxy fixes."
  - q: "Why did this error appear right after I uninstalled my VPN?"
    a: "VPN uninstallers frequently leave behind the WinHTTP proxy setting, virtual network adapters, or routing entries they created. Windows Update then tries to reach Microsoft through a proxy that no longer exists. Resetting the WinHTTP proxy and removing orphaned adapters fixes it."
  - q: "Could my antivirus firewall cause 0x8024402C?"
    a: "Yes. Third-party firewalls sometimes block the Windows Update service's outbound connections while permitting browsers. Temporarily disabling the third-party firewall (keeping Windows Firewall on) for one update check is a valid diagnostic test — just remember to re-enable it immediately afterward regardless of the result."
---

On Windows 10, error 0x8024402C means the update service cannot reach home: a name-resolution or connection failure between your laptop and Microsoft's update servers. Everything else may work perfectly — the browser, email, streaming — because those applications do not use the WinHTTP connection path that Windows Update relies on. That split is the key to the whole diagnosis: when the browser works but updates cannot connect, the problem is in the update service's private connection settings.

Windows 10 machines are particularly prone to this after VPN installs and uninstalls, which love to rewrite the WinHTTP proxy and leave it behind. The fix sequence below walks the connection layer in order, using Windows 10's tools and the netsh commands that expose the hidden proxy.

## Why this happens

- **Stale WinHTTP proxy:** A proxy configured for the system service that points nowhere — the number one cause.
- **VPN uninstall leftovers:** Proxy settings, virtual adapters, and routes surviving the VPN's removal.
- **DNS resolution failures:** System DNS unable to resolve update hostnames.
- **Third-party firewall blocks:** Security suites blocking the update service specifically.
- **Corrupted WinHTTP stack:** Damaged configuration from tools or failed uninstalls.
- **Wrong system clock:** TLS handshake failures from badly skewed date/time.
- **Network-level blocking:** Restrictive corporate or public networks blocking update endpoints.
- **Corrupted network stack:** Winsock/TCP-IP damage affecting service connections.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Sync the clock and test another network

Quick eliminations before the deeper proxy work.

1. Right-click the clock, choose **Adjust date/time**, enable **Set time automatically**, and click **Sync now**.
2. Try a mobile hotspot to rule out your main network blocking update endpoints.
3. Go to **Settings > Update & Security > Windows Update** and click **Check for updates**.

### Fix 2: Show and reset the WinHTTP proxy

The core fix for this error. Expose the hidden proxy and clear it if it is stale.

1. Open **Command Prompt (Admin)**.
2. Run `netsh winhttp show proxy` and read the output carefully.
3. If it lists a proxy server you do not use (often a VPN remnant), run `netsh winhttp reset proxy`.
4. If your environment genuinely needs a proxy, import the correct one: `netsh winhttp import proxy source=ie`.
5. Retry the update check.

### Fix 3: Check Internet Options proxy settings

Windows 10's legacy proxy dialog still feeds the system configuration.

1. Press **Win + R**, type `inetcpl.cpl`, and open the **Connections** tab.
2. Click **LAN settings** and uncheck **Use a proxy server for your LAN** unless you need it. Also uncheck suspicious automatic configuration scripts.
3. Click OK, then run `netsh winhttp import proxy source=ie` in an elevated prompt to sync WinHTTP with the corrected settings.
4. Retry Windows Update.

### Fix 4: Clean up VPN remnants

Remove every trace of VPNs you no longer use.

1. Uninstall old VPN clients via **Control Panel > Programs > Programs and Features**.
2. Open **Device Manager**, enable **View > Show hidden devices**, and uninstall greyed-out virtual network adapters from the VPN.
3. Run `netsh winhttp reset proxy` once more, restart, and retry.
4. The same VPN-cleanup logic helps [download failures](/articles/how-to-fix-windows-update-error-0x80240034-on-windows-10/) that share these network-layer causes.

### Fix 5: Flush DNS and use public resolvers

Fix name resolution directly.

1. In **Command Prompt (Admin)**, run `ipconfig /flushdns`.
2. Open the adapter's IPv4 properties (**Control Panel > Network and Sharing Center > Change adapter settings**, right-click your connection, **Properties**).
3. Set DNS to 8.8.8.8 and 8.8.4.4 (or 1.1.1.1 / 1.0.0.1) and retry the update.

### Fix 6: Reset Winsock and the IP stack

Repair corrupted network stack configuration.

1. In **Command Prompt (Admin)**, run `netsh winsock reset` and `netsh int ip reset`.
2. Restart the laptop when prompted.
3. Check for updates again.

### Fix 7: Test with the third-party firewall disabled

Isolate firewall interference as the last connection-layer suspect.

1. Temporarily disable your third-party firewall (leave Windows Firewall enabled).
2. Immediately run **Check for updates**.
3. Re-enable the firewall right after the test, regardless of outcome.
4. If the check succeeded with the firewall off, add an exception for the Windows Update service in the firewall's application rules rather than leaving it disabled — and review the [Microsoft Windows support page](https://support.microsoft.com/en-us/windows) for the endpoints that must stay reachable.

Windows 10's proxy architecture has an extra wrinkle worth knowing: the legacy Internet Options dialog (inetcpl.cpl) still controls the WinINet proxy that many system components consult, and the netsh winhttp import proxy source=ie command bridges the two worlds. When a VPN uninstaller or privacy tool scrambles these settings, the reliable repair is to fix the Internet Options side first — unchecking stale proxy servers and auto-config scripts — and then import the clean configuration into WinHTTP. Doing it in that order ensures both layers agree. Also be aware that some third-party firewalls on Windows 10 install their own Winsock layered service providers to inspect traffic; a botched firewall uninstall can leave a broken chain that blocks the update service while browsers keep working. If you uninstalled a firewall shortly before this error appeared, reinstalling and then cleanly uninstalling it (using the vendor's removal tool) often clears the damage. The [Windows 11 version of this guide](/articles/how-to-fix-windows-update-error-0x8024402c-on-windows-11/) covers the same concepts with Windows 11's Settings paths. When both proxy layers are clean and DNS resolves, 0x8024402C has nowhere left to hide. A final sanity check costs nothing: run the update check on a completely different network, such as a phone hotspot, to confirm the problem follows the machine and not the network.

## Closing

Windows 10's 0x8024402C is a connection-layer problem wearing an update error's clothes. The WinHTTP proxy is the prime suspect — expose it with `netsh winhttp show proxy`, reset it if stale, and clean up the VPN leftovers that usually put it there. With DNS fixed and firewalls verified, the update service reconnects and the error becomes a footnote in your update history.
