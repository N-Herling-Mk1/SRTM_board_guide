#!/usr/bin/env python3
"""
OPC UA Server Browser - CSV Output
Connects to an OPC UA server and dumps all available nodes to a CSV file.

Usage:
    python browse_opcua_to_csv.py [output_file]
    
Default output: opcua_nodes.csv
"""

from opcua import Client
from datetime import datetime
import sys
import csv

ENDPOINT = "opc.tcp://192.168.0.117:4841"
OUTPUT_FILE = sys.argv[1] if len(sys.argv) > 1 else "opcua_nodes.csv"

def browse(node, parent_path="", max_depth=5, rows=None, depth=0):
    """Recursively browse OPC UA nodes and collect as CSV rows."""
    if rows is None:
        rows = []
    if depth > max_depth:
        return rows
    try:
        for child in node.get_children():
            name = child.get_browse_name()
            nodeid = child.nodeid
            
            # Build full path
            current_path = f"{parent_path}.{name.Name}" if parent_path else name.Name
            
            # Extract namespace and identifier from nodeid
            ns = nodeid.NamespaceIndex if hasattr(nodeid, 'NamespaceIndex') else ""
            identifier = str(nodeid.Identifier) if hasattr(nodeid, 'Identifier') else str(nodeid)
            
            rows.append({
                'depth': depth,
                'name': name.Name,
                'full_path': current_path,
                'namespace': ns,
                'identifier': identifier,
                'nodeid_str': str(nodeid)
            })
            
            browse(child, current_path, max_depth, rows, depth + 1)
    except Exception as e:
        rows.append({
            'depth': depth,
            'name': f"[ERROR]",
            'full_path': parent_path,
            'namespace': "",
            'identifier': "",
            'nodeid_str': str(e)
        })
    return rows

def main():
    print(f"Connecting to {ENDPOINT}...")
    
    client = Client(ENDPOINT)
    client.connect()
    print("Connected!\n")
    
    root = client.get_root_node()
    objects = root.get_child(["0:Objects"])
    
    # Browse and collect nodes
    print("Browsing nodes...")
    rows = browse(objects)
    
    # Write CSV
    with open(OUTPUT_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['depth', 'name', 'full_path', 'namespace', 'identifier', 'nodeid_str'])
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"CSV written to: {OUTPUT_FILE}")
    print(f"Total nodes: {len(rows)}")
    
    # Summary
    srtm_nodes = [r for r in rows if 'SRTM' in r['full_path'] and r['depth'] == 1]
    print(f"\nSRTM top-level nodes: {len(srtm_nodes)}")
    
    # Print categories
    categories = {}
    for r in rows:
        if r['full_path'].startswith('SRTM.'):
            parts = r['name'].split('_')
            if len(parts) > 1:
                cat = parts[0]
                categories[cat] = categories.get(cat, 0) + 1
    
    if categories:
        print("\nSRTM Node Categories:")
        for cat, count in sorted(categories.items()):
            print(f"  {cat}: {count} nodes")
    
    client.disconnect()
    print("\nDisconnected.")

if __name__ == "__main__":
    main()
