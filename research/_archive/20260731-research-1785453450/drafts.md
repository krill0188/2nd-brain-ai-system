**Bash** `find . -path ./node_modules -prune -o -name "*.md" -print | xargs grep -l "claim_type" 2>/dev/null | head -20`
