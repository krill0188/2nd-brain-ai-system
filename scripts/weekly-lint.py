#!/usr/bin/env python3
"""Wiki lint script - checks canonical pages for violations."""
import os
import re
from collections import defaultdict

WIKI_PATH = "/Users/amaster/2nd"

# Canonical directories
canonical_dirs = ["entities", "concepts", "comparisons", "queries"]

# Required frontmatter fields per SCHEMA.md
required_fields = ["title", "created", "updated", "type", "tags", "sources", "confidence", "contested", "contradictions"]

# Valid types per SCHEMA.md
valid_types = {"entity", "concept", "comparison", "query"}

# Results
issues = {
    "orphan_pages": [],
    "broken_wikilinks": [],
    "missing_frontmatter": [],
    "updated_date_error": [],
    "type_mismatch": [],
    "index_missing": [],
    "index_extra": []
}

# Collect all canonical pages
all_canonical_files = {}
all_canonical_slugs = set()

for dir_name in canonical_dirs:
    dir_path = os.path.join(WIKI_PATH, dir_name)
    if not os.path.isdir(dir_path):
        continue
    for filename in os.listdir(dir_path):
        if filename.endswith(".md"):
            slug = filename[:-3]
            rel_path = f"{dir_name}/{filename}"
            full_path = os.path.join(dir_path, filename)
            all_canonical_files[rel_path] = full_path
            all_canonical_slugs.add(slug)

print(f"Total canonical pages found: {len(all_canonical_files)}")

# Parse index.md to get expected pages
index_slugs = set()
with open(os.path.join(WIKI_PATH, "index.md"), "r", encoding="utf-8") as f:
    index_content = f.read()

index_wikilinks = re.findall(r'\[\[([^\]]+)\]\]', index_content)
for link in index_wikilinks:
    slug = link.split('#')[0].strip()
    index_slugs.add(slug)

print(f"Total pages referenced in index.md: {len(index_slugs)}")

# Process each canonical file
wikilinks_inbound = defaultdict(list)

for rel_path, full_path in all_canonical_files.items():
    slug = os.path.basename(full_path)[:-3]
    dir_name = os.path.dirname(rel_path)
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    frontmatter = {}
    if frontmatter_match:
        fm_text = frontmatter_match.group(1)
        for line in fm_text.split('\n'):
            if ':' in line and not line.strip().startswith('#'):
                key, val = line.split(':', 1)
                frontmatter[key.strip()] = val.strip()
    
    # Check missing frontmatter fields
    missing_fields = [f for f in required_fields if f not in frontmatter]
    if missing_fields:
        issues["missing_frontmatter"].append((rel_path, missing_fields))
    
    # Check type matches directory
    if "type" in frontmatter:
        page_type = frontmatter["type"]
        type_to_dir = {
            "entity": "entities",
            "concept": "concepts", 
            "comparison": "comparisons",
            "query": "queries"
        }
        if page_type in type_to_dir and type_to_dir[page_type] != dir_name:
            issues["type_mismatch"].append((rel_path, page_type, dir_name))
        if page_type not in valid_types:
            issues["type_mismatch"].append((rel_path, page_type, "invalid_type"))
    
    # Check updated date format
    if "updated" in frontmatter:
        updated_val = frontmatter["updated"]
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', updated_val):
            issues["updated_date_error"].append((rel_path, updated_val))
    
    # Extract wikilinks from content and track inbound
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    for link in wikilinks:
        target_slug = link.split('#')[0].strip()
        if target_slug != slug:
            wikilinks_inbound[target_slug].append(rel_path)

# Check for orphan pages
for rel_path in all_canonical_files:
    slug = os.path.basename(rel_path)[:-3]
    inbound_count = len(wikilinks_inbound.get(slug, []))
    if inbound_count == 0:
        issues["orphan_pages"].append(rel_path)

# Check for broken wikilinks
broken_wikilinks_list = []
for rel_path, full_path in all_canonical_files.items():
    slug = os.path.basename(full_path)[:-3]
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    wikilinks = re.findall(r'\[\[([^\]]+)\]\]', content)
    for link in wikilinks:
        target_slug = link.split('#')[0].strip()
        if target_slug not in all_canonical_slugs and target_slug != slug:
            broken_wikilinks_list.append((rel_path, target_slug))

issues["broken_wikilinks"] = broken_wikilinks_list

# Check index completeness
for slug in all_canonical_slugs:
    if slug not in index_slugs:
        for rp in all_canonical_files:
            if os.path.basename(rp)[:-3] == slug:
                issues["index_missing"].append(rp)
                break

for slug in index_slugs:
    if slug not in all_canonical_slugs:
        issues["index_extra"].append(slug)

# Print report
print("\n" + "="*60)
print("WIKI LINT REPORT")
print("="*60)

total_issues = 0

if issues["orphan_pages"]:
    print("\n## Orphan Pages (no inbound links from other canonical pages)")
    for page in sorted(issues["orphan_pages"]):
        print(f"  - {page}")
    total_issues += len(issues["orphan_pages"])

if issues["broken_wikilinks"]:
    print("\n## Broken Wikilinks")
    broken_by_source = defaultdict(list)
    for src, tgt in issues["broken_wikilinks"]:
        broken_by_source[src].append(tgt)
    for src in sorted(broken_by_source):
        print(f"  - {src} -> {', '.join(sorted(set(broken_by_source[src])))}")
    total_issues += len(issues["broken_wikilinks"])

if issues["missing_frontmatter"]:
    print("\n## Missing Frontmatter Fields")
    for page, fields in sorted(issues["missing_frontmatter"]):
        print(f"  - {page}: missing {', '.join(fields)}")
    total_issues += len(issues["missing_frontmatter"])

if issues["updated_date_error"]:
    print("\n## Updated Date Format Errors")
    for page, date_val in sorted(issues["updated_date_error"]):
        print(f"  - {page}: '{date_val}' (expected YYYY-MM-DD)")
    total_issues += len(issues["updated_date_error"])

if issues["type_mismatch"]:
    print("\n## Type/Directory Mismatches")
    for page, ptype, directory in sorted(issues["type_mismatch"]):
        print(f"  - {page}: type='{ptype}' in directory '{directory}'")
    total_issues += len(issues["type_mismatch"])

if issues["index_missing"]:
    print("\n## Pages Missing from index.md")
    for page in sorted(issues["index_missing"]):
        print(f"  - {page}")
    total_issues += len(issues["index_missing"])

if issues["index_extra"]:
    print("\n## Index Entries for Non-existent Pages")
    for slug in sorted(issues["index_extra"]):
        print(f"  - [[{slug}]]")
    total_issues += len(issues["index_extra"])

if total_issues == 0:
    print(f"\nlint passed {len(all_canonical_files)} pages checked")
else:
    print(f"\n\nTotal issues found: {total_issues}")
