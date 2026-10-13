---
title: "Fix SearchHost.exe High CPU: Step-by-Step"
slug: how-to-fix-searchhost-exe-high-cpu-step-by-step
date: 2026-09-07
categories: ["performance"]
tags: ["searchhost.exe", "high cpu", "windows search", "step by step"]
description: "A complete step-by-step fix for SearchHost.exe high CPU: verify it's genuine, rebuild the index, trim the scope, and stop the spikes."
thumbnail: "/images/thumbs/how-to-fix-searchhost-exe-high-cpu-step-by-step.webp"
faqs:
  - q: "How do I know if SearchHost.exe is a virus or the real Windows file?"
    a: "Right-click it in Task Manager and choose Open file location. The genuine SearchHost.exe lives only in C:\\Windows\\SystemApps\\MicrosoftWindows.Client.CBS_cw5n1h2txyewy. If it opens anywhere else — especially a Temp folder or your user profile — treat it as malware, disconnect from the network, and run a full Windows Security scan immediately."
  - q: "Why does SearchHost.exe spike every time I open the Start menu?"
    a: "Opening Start triggers the search host to render results, and if the underlying index is corrupted or the search database is mid-rebuild, each query forces expensive re-scans. A healthy index answers instantly with near-zero CPU. Persistent spikes on every Start press point to index corruption, which the rebuild steps in this guide resolve."
  - q: "Can I disable SearchHost.exe without breaking Windows?"
    a: "Not cleanly. It is a protected system component tied to Start menu search, and force-disabling it breaks search and can cause Start menu glitches. The supported path is taming it: rebuild the index, narrow indexed locations, and fix the file churn feeding it. That delivers the same CPU savings without breaking anything."
  - q: "Does SearchHost.exe high CPU drain the laptop battery faster?"
    a: "Yes, noticeably. Sustained CPU usage keeps the processor out of its low-power states, spins up the fan, and can cut battery life by 20–40% during the spike. On battery power, Windows already throttles background indexing, so persistent SearchHost drain on battery usually means something is genuinely stuck rather than just busy."
---

SearchHost.exe is the process behind the Windows search box — the one that turns your typing in Start into instant results. When it works, you never notice it. When it breaks, it camps on your CPU at 30, 50, even 80 percent, the fan howls, and every keystroke in the search box feels like wading through mud.

This is a step-by-step guide in the most literal sense: each fix builds on the last, each has a clear pass/fail test, and you stop the moment the problem is gone. No registry hacks, no sketchy downloads, no disabling things Windows needs.

Before you start, it helps to understand the two halves of Windows search, because they fail differently. SearchHost.exe is the visible half — the process that renders the search box and results. SearchIndexer.exe is the invisible half — the crawler that builds the catalog the host reads from. High CPU in the host usually means a broken catalog or a bad query pipeline; high CPU in the indexer means the crawl itself is stuck. This guide targets the host. If Task Manager shows the indexer as the hot process instead, start with the host fixes anyway — a corrupt index punishes both halves, and the rebuild steps here help either way.

## Why this happens

- **Corrupted search database:** A damaged index forces SearchHost to re-scan files on every query instead of reading the catalog.
- **Over-broad indexing scope:** Indexing entire drives and cloud folders gives the host far more data to chew through per search.
- **Stuck database transactions:** A crashed indexing session leaves the search database retrying the same operation in a loop.
- **Cloud sync churn:** OneDrive and similar tools constantly changing files invalidate cached results, forcing fresh work every time.
- **Bing and web search integration:** Online search suggestions add network waits and parsing overhead to every query.
- **Third-party shell and search extensions:** Poorly written extensions hook into the search pipeline and stall it.
- **Post-update index rebuilds:** After Windows updates, the index rebuilds in the background, which looks exactly like a malfunction for a day or so.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Verify the process is genuine

1. Open Task Manager (**Ctrl + Shift + Esc**), find **SearchHost.exe** under Processes, and check its CPU.
2. Right-click it → **Open file location**. Confirm the path is `C:\Windows\SystemApps\MicrosoftWindows.Client.CBS_cw5n1h2txyewy`.
3. If the location is anywhere else, stop here: run a full **Windows Security** scan and consider the free Microsoft Safety Scanner from the [Microsoft support site](https://support.microsoft.com/en-us/windows).
4. If genuine, right-click → **End task** for immediate relief, then continue — Windows restarts it automatically.

### Fix 2: Restart the search pipeline

1. Press **Win + R**, type `services.msc`, and press Enter.
2. Right-click **Windows Search** → **Restart**. This clears stuck transactions in the search database.
3. In Task Manager, end **SearchHost.exe** once more so it relaunches against the fresh service state.
4. Use the Start menu search normally for ten minutes. If CPU stays low, a stuck transaction was the whole problem.

### Fix 3: Turn off web and cloud search integration

1. Go to **Settings → Privacy & security → Searching Windows**.
2. Under **Cloud content search**, turn off both **Microsoft account** and **Work or School account** toggles.
3. Scroll to **More settings** and disable **Show search highlights** — the highlights feed adds background fetching.
4. Test Start menu searches. Removing the online component eliminates an entire class of network-wait CPU spikes, especially on slow connections.

### Fix 4: Rebuild the search index

1. Open **Control Panel → Indexing Options → Advanced → Rebuild**, and confirm.
2. Keep the laptop plugged in — a rebuild is heavy by design and takes 30 minutes to several hours.
3. Wait for **Indexing complete**, then use search normally for a full day before judging.
4. If the rebuild stalls at the same item count for hours, a corrupt file is hanging the crawler — note it and continue to Fix 5. Our broader [search indexer guide](/articles/best-way-to-fix-windows-search-indexer-high-cpu/) covers the crawler side in more depth.

### Fix 5: Narrow indexed locations

1. In **Indexing Options**, click **Modify** and uncheck everything you never search: full drive letters, Downloads, cloud-synced folders, and program directories.
2. Keep the essentials: your user document folders and the Start Menu.
3. Click **OK**, then rebuild the index again (Fix 4) so old entries are purged from the database.
4. A smaller index is less work per query forever — this is the permanent fix for scope-driven spikes.

### Fix 6: Run the Search and Indexing troubleshooter

1. Go to **Settings → System → Troubleshoot → Other troubleshooters**.
2. Run **Search and Indexing**. When asked what problems you notice, check **Search or indexing is slow** and any other matching symptom.
3. Apply whatever fixes it recommends, then restart the laptop.
4. The troubleshooter resets permissions and re-registers search components — the kind of quiet corruption that manual steps miss.

### Fix 7: Reset the search app package

1. Open an elevated PowerShell and re-register the search host package with this command: `Get-AppxPackage -Name "MicrosoftWindows.Client.CBS" | ForEach-Object { Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml" }`.
2. Restart the laptop after the re-registration completes.
3. If SearchHost still spikes after all of this, check for disk-level causes — a struggling drive makes every search operation expensive. Our [100% disk guide](/articles/how-to-fix-disk-active-time-100-percent-youtube/) walks through that diagnosis.
4. As a final check, create a new local user account and test search there — instant search on a fresh profile proves your main profile's search database is damaged beyond repair, and migrating profiles is the clean fix.

## Closing

SearchHost.exe spikes are a pipeline problem: verify the binary, restart the service, cut the web integration, rebuild and narrow the index, and re-register the package. Worked in order, these steps resolve the issue without breaking search — and the search box goes back to answering before you finish typing.

To keep it that way, revisit your indexed locations once or twice a year. Folders accumulate — new sync clients, downloaded datasets, project directories — and each one quietly adds to the host's workload. A two-minute scope review in Indexing Options is the cheapest preventive maintenance in Windows, and it is the difference between a search box that stays instant and one that slowly degrades back into a CPU hog.
