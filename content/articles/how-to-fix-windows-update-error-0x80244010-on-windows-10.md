---
title: "Fix Error 0x80244010 on Windows 10: Reconnect to the Update Server"
slug: how-to-fix-windows-update-error-0x80244010-on-windows-10
date: 2026-09-01
categories: ["windows-update"]
tags: ["windows update", "0x80244010", "windows 10", "wsus", "update server"]
description: "Windows 10 error 0x80244010 means too many failed trips to the update server. Clear the stale redirects and get your update scans working again."
thumbnail: "/images/thumbs/how-to-fix-windows-update-error-0x80244010-on-windows-10.webp"
faqs:
  - q: "Why does Windows 10 show error 0x80244010?"
    a: "The update client exceeded its allowed number of server round trips in one session. The usual cause is misdirection: stale WSUS registry keys pointing at a dead server, a proxy looping requests, or corrupt local metadata making the client ask for things the server keeps rejecting."
  - q: "I never worked anywhere with a WSUS server. Why would I have those keys?"
    a: "Some third-party tweaking and debloating tools write WSUS-style keys to block or redirect updates, and pre-owned laptops may carry them from a previous owner. It is worth checking the registry even on a machine that was always yours."
  - q: "How many server trips are allowed before this error?"
    a: "Microsoft does not publish the exact budget, and it varies by client version — but the number does not matter for fixing it. What matters is stopping the redirect loop, because a healthy scan uses only a handful of trips. Focus on the redirect loop itself; the budget resets with every fresh scan."
  - q: "Is this the same as the Windows 11 version of the error?"
    a: "The code and causes are the same; only the navigation differs. Our [Windows 11 0x80244010 guide](/articles/how-to-fix-windows-update-error-0x80244010-on-windows-11/) mirrors this repair with Windows 11 menu paths if you support both systems."
---

When Windows 10 reports error 0x80244010, it is telling you about a conversation that went nowhere: the update client kept going back and forth with the server — redirected, retried, redirected again — until it hit the session's round-trip limit and gave up. The updates themselves are not the problem. The path to them is.

That path gets bent by a small set of usual suspects. Registry leftovers from old management, proxies that rewrite requests, VPNs with broken split tunneling, and hosts-file entries from long-forgotten tweaking tools all produce the same symptom: a client that cannot get a straight answer. The repair below straightens the path first and rebuilds the client second, which matches how often each layer is actually at fault.

Give each fix a few quiet minutes before retesting. Rapid-fire retries burn the trip budget and can make a working fix look broken.

## Why this happens

- **Leftover WSUS pointers**: Registry values directing the client to an internal server that is gone.
- **Debloater tool remnants**: Third-party tools that wrote update-blocking or redirecting registry keys.
- **Proxy interference**: Corporate or misconfigured proxies mangling the update protocol's redirects.
- **VPN routing issues**: Update traffic forced down tunnels that redirect it repeatedly.
- **Corrupt metadata cache**: Local update catalog damage causing invalid repeated requests.
- **Hosts file redirects**: Stale entries hijacking Microsoft update hostnames.
- **Outdated servicing stack**: Old client mishandling the server's current redirect behavior.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clean out stale WSUS and policy keys

Start where the fault usually lives. These registry keys override where Windows Update looks, and when they point at nothing, every scan becomes a redirect loop ending in 0x80244010.

1. Open regedit as administrator and back up via File > Export.
2. Go to HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate and delete the key if it holds WUServer or WUStatusServer values on an unmanaged PC.
3. Check HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate for orphaned AccountDomainSid or PingID entries and remove them.
4. Reboot and test Check for updates in Settings > Update & Security > Windows Update.

### Fix 2: Straighten the network path

Proxies and VPNs are the next most common benders of the update path. Testing without them isolates the network layer cleanly.

1. Disconnect the VPN completely and clear any manual proxy in Settings > Network & Internet > Proxy.
2. Turn off Automatically detect settings temporarily during testing.
3. Flush the resolver with ipconfig /flushdns in an elevated Command Prompt.
4. Wait a few minutes, then run Check for updates.

### Fix 3: Audit the hosts file

The hosts file overrides DNS for the whole machine, and stale entries aimed at Microsoft domains break update requests in exactly this looping fashion. It takes a minute to audit.

1. Open C:\Windows\System32\drivers\etc\hosts in an administrator Notepad.
2. Delete or comment out any lines referencing microsoft, windowsupdate, or msftconnecttest that you did not intentionally add.
3. Save, then run ipconfig /flushdns and ipconfig /registerdns.
4. Retry the update scan.

### Fix 4: Run the troubleshooter

With redirection suspects cleared, the built-in troubleshooter checks the client's internal health — services, pending operations, and metadata integrity.

1. Go to Settings > Update & Security > Troubleshoot > Additional troubleshooters.
2. Run the Windows Update troubleshooter and apply its fixes.
3. Restart the laptop with Start > Power > Restart.
4. Check for updates again.

### Fix 5: Reset components and rebuild metadata

Damaged local metadata makes the client request update sets that the server keeps refusing, which looks like a redirect loop from the client's side. A full cache reset ends that cycle.

1. In an elevated Command Prompt, stop wuauserv, cryptSvc, bits, and msiserver.
2. Rename SoftwareDistribution to SoftwareDistribution.old and catroot2 to catroot2.old.
3. Restart all four services and reboot.
4. Allow the first post-reset scan its full time — it rebuilds everything from scratch.

### Fix 6: Refresh the servicing stack from the catalog

Protocol handling improves with each servicing stack release. If the client's redirect logic is simply outdated, a manual stack update from the [Microsoft Update Catalog](https://www.catalog.update.microsoft.com) fixes the behavior directly.

1. Find your Windows 10 version in Settings > System > About.
2. Search the Update Catalog for the newest servicing stack update for that version.
3. Install the x64 package and reboot.
4. Run Check for updates to confirm the loop is gone.

### Fix 7: Try a different network as a diagnostic

When every local fix fails, the bent path may be upstream — ISP-level filtering or a captive portal interfering with update traffic. A different network answers that question in minutes.

1. Connect the laptop to a phone hotspot or a different Wi-Fi network.
2. Run Check for updates there and note whether 0x80244010 still appears.
3. If updates work on the alternate network, the home router or ISP is interfering — check router-level filtering and DNS settings.
4. If it fails everywhere, an in-place repair install is the final local remedy; Microsoft's [support hub](https://support.microsoft.com/en-us/windows) documents the process.

### Fix 8: Flush stuck BITS transfer jobs

The Background Intelligent Transfer Service queues every update download as a job, and crashed jobs can linger in the queue indefinitely. A corrupted or wedged job makes the client re-request the same data in a loop, burning through the server trip budget until 0x80244010 appears. Clearing the queue gives the client a clean transfer slate, and it is entirely safe — Windows recreates the jobs it still needs on the next scan.

1. Open an elevated Command Prompt.
2. Run bitsadmin /reset /allusers to cancel every queued transfer job on the machine.
3. Then run net stop bits followed by net start bits to restart the service on the clean queue.
4. Delete the contents of C:\Windows\SoftwareDistribution\Download to remove partial files tied to the dead jobs.
5. Reboot and run Check for updates — the client rebuilds only the jobs it needs.
## Closing

On Windows 10, 0x80244010 almost always traces back to something redirecting the client — old keys, old tools, or an interfering middlebox — rather than to the updates themselves. Clean the pointers, verify on a clean network path, and the trip budget stops being a problem. And if the laptop ever joins a workplace network again, remember to remove any WSUS keys before it leaves, or this exact error will be waiting at home. Related: our [Windows 11 0x80244010 guide](/articles/how-to-fix-windows-update-error-0x80244010-on-windows-11/) mirrors these steps, and the [undoing changes stuck guide](/articles/best-way-to-fix-undoing-changes-made-to-your-computer-stuck/) covers the related rollback failure.
