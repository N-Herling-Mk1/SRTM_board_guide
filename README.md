# SRTM Board Monitoring GUI

WinCC OA setup and configuration guide for monitoring the SRTM (Slow Rate Timing Module) board via OPC UA.

## Overview

This repository contains documentation and scripts for creating a real-time monitoring GUI for the SRTM board using Siemens WinCC OA. The SRTM board exposes sensor data (temperatures, voltages, currents) via an OPC UA server.

| Component | Details |
|-----------|---------|
| SRTM Board | IP: 192.168.0.117 |
| OPC UA Server | `opc.tcp://192.168.0.117:4841` |
| WinCC OA Server | eepp-bigmem3.physics.arizona.edu |
| WinCC OA Version | 3.19 |

## Repository Structure

```
SRTM_board_guide/
├── docs/
│   ├── SRTM_WinCC_OA_GUI_Guide.pdf    # Complete guide (rendered)
│   ├── SRTM_WinCC_OA_GUI_Guide.tex    # LaTeX source
│   └── images/                         # Screenshots for documentation
├── scripts/
│   ├── browse_opcua.py                 # Browse OPC UA nodes → CSV
│   └── read_fpga_temp.py               # Test script for FPGA temperature
└── README.md
```

## Documentation

The full guide covers:

1. **OPC UA Node Discovery Tools** — Python scripts to browse available nodes
2. **Creating a New WinCC OA Project** — Project wizard and copy method
3. **OPC UA Driver Configuration** — Connecting to the SRTM board
4. **Datapoint Configuration** — Mapping OPC UA nodes to WinCC OA
5. **GUI Panel Creation** — LCD display and trend charts
6. **Key File Locations** — Reference paths
7. **Quick Reference Commands** — Common operations

## Quick Start

### 1. Browse OPC UA Nodes

```bash
/usr/bin/python3 scripts/browse_opcua.py
```

Output: `opcua_nodes.csv`

### 2. Test OPC UA Connection

```bash
/usr/bin/python3 scripts/read_fpga_temp.py
```

### 3. Start WinCC OA Project Administrator

```bash
startPA
```

## Building the Documentation

To compile the LaTeX source:

```bash
cd docs
pdflatex SRTM_WinCC_OA_GUI_Guide.tex
```

## Authors

- **Nathan Herling** — M.S. Candidate, Data Science, University of Arizona (nth@arizona.edu)
- **Claude** (Anthropic) — Documentation assistance

## License

See LICENSE file.
