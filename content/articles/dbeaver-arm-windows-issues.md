---
title: "How to Fix DBeaver Issues on ARM Windows Laptops"
slug: dbeaver-arm-windows-issues
date: 2026-10-24
categories: ["ai-pc"]
tags: ["dbeaver", "arm64", "database", "java", "windows 11", "troubleshooting"]
description: "DBeaver crashing or failing to connect on your ARM Windows laptop? Follow these step-by-step fixes for the ARM64 build, Java runtime, drivers, and heap tuning."
thumbnail: "/images/thumbs/dbeaver-arm-windows-issues.webp"
faqs:
  - q: "Is there a native ARM64 build of DBeaver for Windows?"
    a: >
      DBeaver publishes Windows ARM64 (aarch64) builds. Download the installer labeled for ARM64/aarch64 from DBeaver's official download page — the x64 build runs under emulation and is notably slower and less stable.
  - q: "Why does DBeaver fail to start with a Java error?"
    a: >
      DBeaver bundles its own Java runtime, but a broken install or a JAVA_HOME pointing at an x64 JDK can break startup. Reinstalling the ARM64 DBeaver package (which includes the matching bundled JRE) fixes most startup failures.
  - q: "My database connections fail in DBeaver on Snapdragon. Why?"
    a: >
      Connection failures are usually driver or network issues, not ARM issues. Download the database driver fresh inside DBeaver, check that your VPN or firewall allows the database port, and verify the credentials work in another client.
  - q: "DBeaver is very slow on my ARM laptop. How do I speed it up?"
    a: >
      First confirm you are running the ARM64 build (Task Manager > Details > Architecture column). Then raise the heap size in dbeaver.ini (-Xmx), close unused result tabs, and disable automatic metadata reading for large databases.
---

You launch DBeaver on your Snapdragon laptop and it crashes immediately, throws a Java error, or opens but refuses to connect to databases that work from every other client. Database work is deadline work — a broken client is not a minor annoyance.

DBeaver is a Java/Eclipse-based app, so on ARM Windows it has two architecture layers to get right: the app build itself (ARM64 vs emulated x64) and the Java runtime underneath it. Get either wrong and you get crashes, hangs, or mysterious failures. Database drivers add a third layer — JDBC drivers are pure Java and usually fine, but anything with native libraries needs ARM64 natives. The same Java-architecture discipline applies to [installing a JDK on ARM Windows](/articles/java-jdk-arm-windows-install/), and the same "wrong build" story affects [new Outlook on ARM laptops](/articles/new-outlook-arm-laptop-issues/). The pattern extends beyond dev tools — [AI Windows Search breaking](/articles/ai-windows-search-not-working/) and [NPU driver error 39](/articles/npu-driver-error-code-39-fix/) both start with the same architecture check.

This guide gives you six fixes in order: install the ARM64 build, fix Java runtime issues, repair database connections, fix driver problems, tune performance, and do a clean reinstall. Mostly GUI work, no terminal required.

## Why this happens

- **x64 build under emulation:** The default DBeaver download is x64. Under emulation the Eclipse platform is sluggish and crash-prone, and large result sets can hang the app.
- **Wrong-architecture Java runtime:** DBeaver bundles a JRE, but a system JAVA_HOME pointing at an x64 JDK — or a corrupted bundled JRE — breaks startup with Java errors.
- **Stale or missing database drivers:** DBeaver downloads JDBC drivers on first connect. A failed or partial driver download produces connection errors that look like server problems.
- **Native libraries in drivers:** A few database drivers bundle native code. x64-only natives fail on ARM64 even though the JDBC layer is pure Java.
- **VPN/firewall blocking database ports:** Database ports (5432, 3306, 1433) are commonly blocked by VPN clients and firewalls — the connection fails before authentication is even attempted.
- **Insufficient heap allocation:** The default JVM heap is modest. Large queries and big schemas exhaust it, producing freezes and out-of-memory crashes.
- **Corrupted workspace metadata:** DBeaver's workspace (connections, drivers, UI state) can corrupt after a crash, causing startup loops that survive reinstalls of the app binaries.

## How to fix it

Work through these in order — diagnose first, then act.

### Fix 1: Install the native ARM64 build

The emulated x64 build is the root cause of most DBeaver instability on Snapdragon laptops.

1. Uninstall the current DBeaver from **Settings > Apps > Installed apps**.
2. Go to DBeaver's official download page and choose the **Windows ARM64 (aarch64)** installer.
3. Install it and launch — note whether startup is faster and whether the previous crash is gone.
4. In Task Manager's **Details** tab, confirm the DBeaver process **Architecture** reads **ARM64**.
5. Let the first launch complete fully — DBeaver initializes its workspace on first run, which takes longer than subsequent launches.

### Fix 2: Fix the Java runtime

DBeaver needs a working, matching-architecture JRE. Repair the Java layer when startup throws Java errors.

1. Check your system **JAVA_HOME** environment variable — if it points to an x64 JDK, either remove it or point it at an ARM64 JDK.
2. The ARM64 DBeaver installer bundles a matching JRE; a reinstall (Fix 1) normally repairs a corrupted bundled runtime.
3. If you prefer a system Java, install an **ARM64** JDK (Temurin or Microsoft Build of OpenJDK both publish ARM64 Windows builds) and set JAVA_HOME to it.
4. In `dbeaver.ini` (in the install folder), check the `-vm` line — it should point at the bundled JRE or your ARM64 JDK's `bin\javaw.exe`.
5. Relaunch DBeaver and confirm the Java error is gone before touching any database connections.

### Fix 3: Repair database connections

The app runs but connections fail — work through the connection stack methodically.

1. Test the basics first: can you reach the database host at all? Try `Test Connection` in DBeaver and read the full error, not just the headline.
2. Fully quit your VPN client and retest — VPNs blocking database ports is the most common sudden-connection-failure cause.
3. Check Windows Firewall for a DBeaver/Java rule blocking outbound connections, and add an allow rule if needed.
4. Verify the connection details (host, port, database name, credentials) by connecting with another client or `psql`/`mysql` from the terminal.
5. For SSH tunnels, confirm the tunnel itself connects — test the SSH hop separately before blaming the database driver.

### Fix 4: Fix database driver issues

"Driver not found," class-loading errors, or connections that fail only for one database type point at the JDBC driver.

1. In DBeaver, open **Database > Driver Manager**, select your database's driver, and check its libraries tab for download errors.
2. Delete the cached driver files and click **Download** again to force a fresh driver fetch.
3. If the driver bundles native libraries, check the driver's documentation for ARM64/aarch64 support — pure-Java drivers are always safe.
4. For corporate databases, confirm you are using the driver version your DBA team supports — mismatched driver versions cause cryptic protocol errors.
5. After refreshing the driver, use **Test Connection** before opening any editors — a green test isolates driver issues from query issues.

### Fix 5: Tune performance for large databases

DBeaver works but crawls on big schemas or large result sets — tune the JVM and the app's behavior.

1. Confirm you are on the ARM64 build first (Fix 1, step 4) — no tuning fixes emulation slowness.
2. Edit `dbeaver.ini` and raise the heap: change `-Xmx` to `-Xmx2048m` (or 4096m on 16 GB+ laptops), then restart DBeaver.
3. In **Preferences > Database > Result Sets**, lower the fetch size and enable **Read query metadata** only when needed.
4. Disable automatic completion and background metadata reading for very large databases under **Preferences > Database > Editors**.
5. Close result tabs and editors you are not using — each holds memory, and Eclipse does not release it aggressively.

### Fix 6: Clean reinstall with a fresh workspace

Startup loops or corruption that survives the above need a workspace wipe — the app binaries are fine, the metadata is not.

1. Uninstall DBeaver, then rename `%APPDATA%\DBeaverData` to a backup name (this preserves your connections for later recovery).
2. Reinstall the **ARM64** build fresh and launch — it creates a clean workspace.
3. Recreate one connection manually and confirm it works before restoring anything.
4. Re-import connections selectively: use **File > Import** from the backed-up workspace rather than copying the whole folder back.
5. If the fresh workspace works but the old one does not, keep the fresh one — migrate connections over rather than reviving corrupted metadata.

## Closing

DBeaver on Snapdragon laptops is a capable native app once the two architecture layers line up: the ARM64 DBeaver build on top of a working ARM64 Java runtime. Connection failures after that are ordinary database networking — VPNs, firewalls, drivers, credentials — diagnosed the same way on any platform. Keep the heap sized for your workload and your drivers fresh, and the app stays out of your way. For JDK questions on these machines, our [Java JDK on ARM Windows guide](/articles/java-jdk-arm-windows-install/) covers the runtime side in depth.
