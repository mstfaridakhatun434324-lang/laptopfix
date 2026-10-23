---
title: "How to Fix Foundry Local Model Downloads Stuck on Windows 11"
slug: foundry-local-model-download-stuck
date: 2026-10-23
categories: ["ai-pc"]
tags: ["foundry local", "model download", "microsoft foundry", "windows 11", "npu", "local ai"]
description: "Fix Foundry Local model downloads stuck on Windows 11: clear partial caches, resolve network and permission issues, and get local AI models downloading again."
thumbnail: "/images/thumbs/foundry-local-model-download-stuck.webp"
faqs:
  - q: "Why is my Foundry Local model download stuck at a percentage?"
    a: "The usual causes are a corrupted partial download in the model cache, an interrupted network connection, or antivirus quarantining model files mid-download. Clear the partial cache for that model and retry on a stable connection before anything else."
  - q: "How much disk space do Foundry Local models need?"
    a: "Several gigabytes per model, plus headroom for the temporary download files — a nearly full drive is one of the most common reasons downloads stall. Free up at least twice the model's size on the cache drive before retrying."
  - q: "Can a VPN or proxy break model downloads?"
    a: "Yes. VPNs, corporate proxies, and aggressive firewalls can interrupt the large file transfers that model downloads require, leaving them permanently stalled. Temporarily disable the VPN or proxy to test whether the download completes."
  - q: "Do I need to reinstall Foundry Local if downloads keep failing?"
    a: "Usually not. Clear the model cache, update the app and Windows, and check permissions first — those resolve the vast majority of stuck downloads. Reinstall only if the cache and network are both proven healthy and downloads still stall."
---

Microsoft Foundry Local brings open models onto your Copilot+ PC's NPU — download a model once, run it privately forever. Except the download never finishes: the progress bar freezes at 37 percent, or crawls to 99 and sits there, or fails and restarts from zero every time. The model catalog looks fine, your browser downloads other files normally, and yet Foundry Local cannot complete a single model.

Model downloads are large, resumable file transfers into a managed cache, and several ordinary things break them: a corrupted partial download that the resume logic chokes on, a drive too full for the temp files, a VPN or proxy interrupting the transfer, or antivirus quarantining model files as they land. The app rarely names the actual cause, so the symptom — a stuck progress bar — has to be diagnosed from the outside in.

This guide gives you six fixes in order: clearing the partial cache, checking disk space, ruling out network interference, and fixing permissions — the sequence that resolves nearly every stuck download. On company-managed PCs there is one more suspect: device policy blocking the transfer, similar to [Recall group policy not applying via Intune](/articles/recall-group-policy-intune-not-applying/) — policy can quietly forbid what the app is trying to do.

## Why this happens

- **Corrupted partial download:** an interrupted transfer leaves a bad chunk in the model cache, and the resume logic stalls on it instead of starting over.
- **Insufficient disk space:** models need several gigabytes plus temp-file headroom; a nearly full drive stalls the download partway through.
- **VPN, proxy, or firewall interference:** intermediaries interrupt large transfers, and corporate networks may block the model endpoints entirely.
- **Antivirus quarantining model files:** security software flags large binary model files as they land, silently removing pieces of the download.
- **Stale app or Windows AI components:** an outdated Foundry Local build or OS runtime mishandles the catalog or the download protocol.
- **Permission problems on the cache folder:** the app cannot write to its own cache directory after a user-profile or ownership change.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Clear the partial download from the model cache

A corrupted partial download is the most common cause of a permanently stuck progress bar — the resume logic keeps tripping over the same bad chunk instead of starting over. Foundry Local stores models in a cache folder on disk; deleting the incomplete files for the stuck model forces a genuinely fresh download. This is safe: it only removes the broken partial files, never your working models or the app itself. Quit the app fully first, including any background process in Task Manager.

1. Fully quit Foundry Local, ending any lingering background process in Task Manager.
2. Open the model cache folder (named in the app’s settings or documentation).
3. Delete only the stuck model’s folder or partial files; leave working models alone.
4. Relaunch the app and restart the download from zero.
5. Watch whether it now passes the percentage where it previously stalled.

### Fix 2: Free up disk space on the cache drive

Model downloads need the model’s full size plus temporary working space, and Windows gets conservative about large writes as a drive fills. A download that stalls at the same high percentage every time is the classic signature of a full disk. Check the free space on whichever drive holds the cache, and clear comfortably more than the model needs — twice the model’s size is a safe rule of thumb before retrying. If the cache sits on a small system drive, check whether the app’s settings allow moving it.

1. Check free space on the cache drive in File Explorer.
2. Run Disk Cleanup (including system files) to reclaim space quickly.
3. Move large personal files off the cache drive if space is still tight.
4. Restart the download and confirm it passes the previous stall point.
5. Keep at least twice the model’s size free as a standing rule.

### Fix 3: Rule out VPN, proxy, and firewall interference

Large model transfers are fragile through intermediaries: VPNs reroute them, corporate proxies inspect or block them, and overzealous firewalls drop the long-lived connections mid-transfer. If the download stalls at random percentages rather than the same one, the network path is the prime suspect. Temporarily simplify the path — no VPN, no proxy — and retry; that single test answers the question definitively. If the download completes with the VPN off, the VPN is the cause — try a different server or split-tunneling.

1. Disconnect any VPN and retry the download on the direct connection.
2. In **Settings > Network & internet > Proxy**, temporarily disable proxy configuration.
3. On a corporate or school network, test from a home network or phone hotspot.
4. Allow Foundry Local through Windows Firewall (or add it to allowed apps).
5. If it completes with the VPN off, switch servers or enable split-tunneling.

### Fix 4: Stop antivirus from quarantining model files

Security software loves large, unfamiliar binary files, and model weights fit that description perfectly. The maddening version of this failure is a download that reaches 100 percent and then the model “disappears” — the antivirus removed pieces as they landed. Check your protection history for quarantined files from the cache folder; if you find them, the fix is an exclusion for the cache directory, not a different download technique. Apply the same exclusion in third-party antivirus — it quarantines independently of Windows Security.

1. Open Windows Security > **Protection history**; look for quarantined cache files.
2. Restore any model files that were wrongly quarantined.
3. Add the model cache folder as an exclusion (Virus & threat protection > Exclusions).
4. Add the same exclusion in third-party antivirus if you run one.
5. Clear the partial cache once more (Fix 1) and redownload with the exclusion in place.

### Fix 5: Update Foundry Local, Windows, and the NPU driver

A stale app or OS runtime can mishandle the model catalog protocol or the download handshake itself — the download stalls not because of your network but because the client speaks an outdated dialect. Update Foundry Local to the latest release, install all Windows Updates, and make sure the NPU and chipset drivers are current — on Intel use the [Intel Driver & Support Assistant](https://www.intel.com/content/www/us/en/support/detect.html), on AMD the [AMD driver page](https://www.amd.com/en/support/download/drivers.html) — since the runtime that Foundry Local targets ships with the platform stack. This is the same driver hygiene that fixes [MIPI camera driver errors on AI laptops](/articles/mipi-camera-driver-error-ai-laptop/) — one platform package, many dependents.

1. Update Foundry Local to the latest release and restart it.
2. Run Windows Update, install everything offered, then restart.
3. Update chipset and NPU drivers from your maker’s support site (or the Intel/AMD detectors above).
4. Reopen the model catalog and confirm it loads fresh — stale catalogs can offer broken URLs.
5. Retry the download; watch the first 10 percent closely.

### Fix 6: Fix cache-folder permissions and reset the app

If the cache is clear, the disk has space, the network is clean, and everything is updated — yet downloads still stall — the app likely cannot write reliably to its own cache folder. Profile migrations, ownership changes, or a previous admin-mode run can leave the cache directory owned by the wrong identity. Reset the permissions, and as a last resort reset the app itself; if even that fails, the OS install may be damaged, in which case a [clean install of Windows 11 with proper AI-laptop drivers](/articles/clean-install-windows-11-ai-laptop-drivers/) is the final escalation.

1. Right-click the cache folder > Properties > Security; confirm your account has Full control.
2. If ownership is wrong, take ownership as your user and reapply to subfolders.
3. Never run Foundry Local as administrator daily — admin runs create files your user cannot overwrite.
4. As a last app-level step, uninstall, delete data and cache folders, and reinstall fresh.
5. Retry one model download before restoring anything else.

## Closing

A stuck Foundry Local download is almost never a broken model or a dead server — it is a corrupted partial file, a full disk, a VPN in the way, or antivirus eating the pieces. Clear the cache first, verify space and network second, and work the list in order. The progress bar will move.
