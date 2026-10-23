---
title: "How to Speed Up a Slow JetBrains IDE on ARM Windows"
slug: jetbrains-ide-arm-windows-slow
date: 2026-10-23
categories: ["ai-pc"]
tags: ["jetbrains", "intellij", "arm64", "windows on arm", "jdk", "performance"]
description: "Fix a sluggish JetBrains IDE on ARM Windows: install the native ARM64 build, switch to an ARM64 JDK, tune the heap, trim indexing, and stop power throttling."
thumbnail: "/images/thumbs/jetbrains-ide-arm-windows-slow.webp"
faqs:
  - q: "Why is IntelliJ IDEA so slow on my ARM laptop?"
    a: "The most common cause is running the x64 build of the IDE under emulation instead of the native ARM64 build. An emulated IDE plus an emulated JDK stacks two translation layers, which makes indexing, builds, and even typing feel sluggish. Installing the ARM64 build with a matching ARM64 JDK usually fixes most of the lag."
  - q: "Is there a native ARM64 version of JetBrains IDEs?"
    a: "Yes. JetBrains ships ARM64 builds of IntelliJ IDEA, PyCharm, WebStorm, and the other IDEs for Windows on ARM. During download, choose the ARM64 option rather than the default x64 installer. You can confirm which build is running in Help > About — it should say aarch64, not amd64."
  - q: "Does the JDK really affect IDE speed on ARM?"
    a: "A lot. The IDE runs on the JDK, so an x64 JDK on an ARM machine forces the entire IDE through emulation. Pointing the IDE at a native ARM64 JDK — for example Azul Zulu for ARM64 — removes that layer and noticeably speeds up startup, indexing, and code completion."
  - q: "Will more RAM fix a slow JetBrains IDE?"
    a: "Only if memory is the actual bottleneck. On ARM laptops the usual culprits are emulation, an undersized heap, and heavy indexing — not total RAM. Fix the architecture mismatch and heap settings first; they deliver bigger gains than hardware you cannot change."
---

IntelliJ IDEA or PyCharm on your Snapdragon Copilot+ laptop feels like wading through mud: indexing crawls, completion lags a keystroke behind, and builds take twice as long as on your old Intel machine. The laptop itself is fast — browsers fly, Office is instant — so the IDE feels like the one broken app.

On Windows 11 on ARM, that sluggishness almost always comes from invisible emulation layers. If the IDE or its JDK is an x64 build running through Prism emulation, every operation pays a translation tax — and with default heap settings on top, even a fast Copilot+ laptop feels slow.

This guide gives you six fixes in technician order: confirm native ARM64 builds, point the IDE at a native ARM64 JDK, tune memory and indexing, strip unneeded plugins and background work, and stop Windows throttling the CPU underneath.

## Why this happens

- **Running the x64 IDE under emulation:** The default JetBrains download is often the x64 build, which runs through Prism emulation — adding overhead to everything the IDE does.
- **Emulated JDK underneath the IDE:** A native IDE launched with an x64 JDK still forces the whole runtime through translation — a second emulation layer.
- **Heap too small for real projects:** The default `-Xmx` is conservative; large projects trigger constant garbage collection, which surfaces as UI freezes and stuttering completion.
- **Indexing everything, including build output:** By default the IDE indexes `node_modules`, `target`, `build`, and virtual-environment folders, burning CPU and memory on files you never navigate.
- **Plugin and background-task bloat:** Unused bundled plugins, database tools, and background inspections consume threads at startup and during editing.
- **Windows power throttling:** Copilot+ laptops aggressively park efficiency cores and cap clocks on battery or in power-saver mode, and a CPU-bound IDE feels it immediately — the same throttling that causes [general reliability hiccups on AI PCs](/articles/reliability-monitor-ai-pc-crashes/).
- **Stale caches after updates:** Major IDE or JDK updates can leave incompatible caches behind, leaving the IDE fighting its own stale index.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build of the IDE

Half of all "slow JetBrains on ARM" reports end here. JetBrains publishes ARM64 builds for Windows, but the download page does not always select ARM64 for you — verify before assuming.

1. In your IDE, open **Help > About** and look at the architecture line: you want **aarch64**. If it says **amd64**, you are running the emulated build.
2. Download the installer again from the JetBrains site, this time explicitly choosing the **ARM64** build for Windows (not the default .exe if it offers a choice).
3. Uninstall the x64 IDE first via **Settings > Apps > Installed apps** so the two builds do not share settings in confusing ways — export settings with **File > Manage IDE Settings > Export Settings** if you have heavy customization.
4. Install the ARM64 build and import your settings on first launch.
5. Reopen your largest project and let indexing finish; compare startup and completion responsiveness against the old build before moving on.

### Fix 2: Point the IDE at a native ARM64 JDK

The IDE runs on a Java runtime, and an x64 runtime reintroduces emulation under even a native IDE. This is the biggest remaining speedup after Fix 1, and it is free.

1. Install an ARM64 JDK for Windows — Azul Zulu publishes one, and the Microsoft Build of OpenJDK also ships ARM64 binaries. Install it outside the IDE's folders so updates do not wipe it.
2. In the IDE, open **Help > Find Action** (Ctrl+Shift+A), type **"Choose Boot Java Runtime for the IDE"**, and pick the ARM64 runtime you installed.
3. For your *project* SDK, go to **File > Project Structure > Project** and set the SDK to the ARM64 JDK as well, so builds and tests also run natively.
4. Restart the IDE and confirm in **Help > About** that both the IDE and the runtime report **aarch64**.
5. Re-run a full build of your project and note the time — native compilation on Snapdragon is dramatically faster than the emulated path, much like native-vs-emulated differences seen across other ARM tooling such as [Miracast streaming on Snapdragon laptops](/articles/miracast-not-working-snapdragon-laptop/).

### Fix 3: Raise the heap and exclude folders from indexing

With architecture fixed, memory tuning is next: defaults suit small projects, while a real codebase needs headroom and the indexer needs boundaries.

1. Open **Help > Edit Custom VM Options** and raise `-Xmx` — for 16 GB machines, `-Xmx4096m` is a sane start; for 32 GB, `-Xmx8192m`. Leave at least half your RAM for Windows itself.
2. In the Project view, right-click `node_modules`, `target`, `build`, `.venv`, and generated-code folders and choose **Mark Directory as > Excluded**.
3. In **Settings > Build, Execution, Deployment > Compiler**, confirm **"Build project automatically"** is off if you do not need it — it re-triggers work on every save.
4. Delete stale shared indexes in **File > Invalidate Caches** (check all boxes) and restart, letting one clean full index complete without interruption.
5. Time a full project reopen after the clean index; if the UI still hitches, raise `-Xmx` one step and retest rather than guessing.

### Fix 4: Disable unused plugins and background inspections

Every enabled plugin adds startup cost and background threads, and most developers use a fraction of what ships enabled.

1. Open **Settings > Plugins > Installed** and disable anything you do not actively use — database tools, extra version-control integrations, cloud toolkits, and bundled frameworks for languages you never touch.
2. Restart the IDE so disabled plugins fully unload; a surprising amount of their cost is paid at startup.
3. In **Settings > Editor > Inspections**, turn off inspection profiles for languages and frameworks absent from your project.
4. Check the background-tasks indicator (bottom-right status bar) during normal editing — if something like "Updating indexes" or a linter runs constantly, that is your next exclusion or disable target.
5. Keep a short list of what you disabled; if a feature you need goes missing, re-enable just that plugin instead of turning everything back on.

### Fix 5: Stop Windows from throttling the CPU under the IDE

An IDE is one of the most CPU-hungry desktop apps there is, and Copilot+ power management does not know you are mid-build. This step takes a minute and matters most on battery.

1. Plug in the charger — on battery, several Snapdragon laptops cap sustained clocks no matter what the power slider says.
2. Open **Settings > System > Power & battery** and set **Power mode** to **Best performance** while doing heavy IDE work.
3. Make sure **Battery saver** is off, including its automatic turn-on threshold.
4. In the IDE, avoid running full builds, test suites, and Docker-style workloads simultaneously on battery; stagger them or stay plugged in.
5. If slowness appears only when unplugged and vanishes on AC power, you have found your answer — it was throttling, not the IDE, and no amount of JDK tuning will beat physics. Similar power-policy surprises affect unrelated features too, like [Click to Do image actions stalling on battery](/articles/click-to-do-not-working-images/).

### Fix 6: Update the IDE, JBR, and drivers together

JetBrains steadily improves ARM64 support, and Windows on ARM keeps maturing underneath. Running a year-old IDE on a new OS build invites exactly this kind of mismatch.

1. In the IDE, use **Help > Check for Updates** and install the latest stable release; major versions often carry ARM-specific performance work.
2. After updating, revisit **"Choose Boot Java Runtime"** — updates sometimes reset it to a bundled runtime, so re-select your ARM64 JDK if needed.
3. Update your laptop's chipset and system drivers from the maker ([Dell](https://www.dell.com/support), [HP](https://support.hp.com/us-en), [Lenovo](https://support.lenovo.com/us/en/)), since scheduler and power-plan behavior on Snapdragon comes through those drivers.
4. Install the latest Windows 11 on ARM servicing updates from Windows Update — Prism emulation itself gets faster with OS updates.
5. After each update round, do one clean **Invalidate Caches** restart so the new build is not dragging the old build's index behind it.

## Closing

A slow JetBrains IDE on ARM Windows is almost never the laptop's fault — it is an x64 build or x64 JDK running through emulation, a heap and indexer tuned for smaller projects, or Windows quietly throttling the CPU. Go native on both layers, give the heap room, fence the indexer in, and work on Best performance: the IDE will feel like the fast machine you bought.
