"""
PrismIO Obsidian Vault → Master Section MD Exporter
Consolidates vault content into machine-readable master files for ChatGPT project.
Output: knowledge_base/obsidian/
"""

import os
import re
import sys
import shutil
from pathlib import Path

# Paths
VAULT_DIR = Path(r"C:\Users\Sigma\Battle Eternal PrismIO")
OUTPUT_DIR = Path(r"C:\Users\Sigma\Battle Eternal PrismIO\knowledge_base\obsidian")

# Directories to skip entirely
SKIP_DIRS = {'.obsidian', '.smart-env', 'copilot', 'media', 'Chats',
             'scripts', 'knowledge_base'}


def clean_obsidian_content(text: str) -> str:
    """Strip Obsidian-specific syntax from markdown content."""
    # Remove YAML frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.DOTALL)

    # Convert [[wiki links]] to plain text
    # [[Page Name|Display Text]] → Display Text
    text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', text)
    # [[Page Name]] → Page Name
    text = re.sub(r'\[\[([^\]]+)\]\]', r'\1', text)

    # Convert Obsidian callouts to standard markdown blockquotes
    # > [!type] Title  →  > **Type: Title**
    text = re.sub(
        r'^(>\s*)\[!(\w+)\]\s*(.*?)$',
        lambda m: f'{m.group(1)}**{m.group(2).title()}{": " + m.group(3) if m.group(3) else ""}**',
        text,
        flags=re.MULTILINE
    )

    # Remove Obsidian comments %%...%%
    text = re.sub(r'%%.*?%%', '', text, flags=re.DOTALL)

    # Remove Obsidian embed syntax ![[filename]]
    text = re.sub(r'!\[\[([^\]]+)\]\]', r'(See: \1)', text)

    # Clean up excessive blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text.strip()


def read_and_clean(filepath: Path) -> str:
    """Read a markdown file and clean Obsidian syntax."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    return clean_obsidian_content(content)


def build_master_section(title: str, description: str,
                         file_groups: list[tuple[str, list[Path]]]) -> str:
    """
    Build a consolidated master MD file from multiple source files.
    file_groups: list of (group_label, [file_paths])
    """
    parts = [f"# {title}\n\n{description}\n"]

    for group_label, files in file_groups:
        if group_label:
            parts.append(f"\n---\n\n## {group_label}\n")

        for filepath in sorted(files):
            content = read_and_clean(filepath)
            if not content.strip():
                continue

            # Use filename (without extension) as section header
            file_label = filepath.stem
            # If content already starts with a heading, use it; otherwise add one
            if content.startswith('# '):
                # Bump the top-level heading down to ###
                content = re.sub(r'^# ', '### ', content, count=1)
                parts.append(f"\n{content}\n")
            else:
                parts.append(f"\n### {file_label}\n\n{content}\n")

    result = '\n'.join(parts)
    # Final cleanup
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip() + '\n'


def collect_files(subdir: str, pattern: str = '*.md') -> list[Path]:
    """Collect MD files from a vault subdirectory."""
    target = VAULT_DIR / subdir
    if not target.exists():
        return []
    return sorted(target.glob(pattern))


def collect_recursive(subdir: str, pattern: str = '*.md') -> list[Path]:
    """Collect MD files recursively from a vault subdirectory."""
    target = VAULT_DIR / subdir
    if not target.exists():
        return []
    return sorted(target.rglob(pattern))


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results = []

    # ─── 1. CHARACTER_ICP_MASTER.md ───
    char_ref_files = collect_files(
        'battle-eternal-character-architect/references'
    )
    # Exclude SKILL.md if it ended up here
    char_ref_files = [f for f in char_ref_files if f.name.lower() != 'skill.md']

    content = build_master_section(
        "Battle Eternal — Character ICP Master Reference",
        "Consolidated character ICP (Ideal Character Profile) blueprints, "
        "roster, module templates, and QA schema for all Battle Eternal characters.",
        [("Character Profiles & References", char_ref_files)]
    )
    out = OUTPUT_DIR / "CHARACTER_ICP_MASTER.md"
    out.write_text(content, encoding='utf-8')
    results.append(("CHARACTER_ICP_MASTER.md", len(content)))
    print(f"  ✓ CHARACTER_ICP_MASTER.md ({len(content):,} chars, {len(char_ref_files)} source files)")

    # ─── 2. CHARACTER_ARCHITECT_SKILL.md (standalone) ───
    skill_path = VAULT_DIR / 'battle-eternal-character-architect' / 'SKILL.md'
    if skill_path.exists():
        content = read_and_clean(skill_path)
        out = OUTPUT_DIR / "CHARACTER_ARCHITECT_SKILL.md"
        out.write_text(content, encoding='utf-8')
        results.append(("CHARACTER_ARCHITECT_SKILL.md", len(content)))
        print(f"  ✓ CHARACTER_ARCHITECT_SKILL.md ({len(content):,} chars)")

    # ─── 3. COSMOLOGY_AND_STRUCTURE_MASTER.md ───
    cosmology_files = collect_files('Cosmology of Battle Eternal')
    root_extras = []
    for name in ['The Furies — Tier-Level Synopsis.md',
                  'ALEXANDER_DEMARCO_RIVALRY CONTRACT.md']:
        p = VAULT_DIR / name
        if p.exists():
            root_extras.append(p)

    content = build_master_section(
        "Battle Eternal — Cosmology, Structure & Mythology",
        "Core cosmological framework, prophecy structures, narrative architecture, "
        "mythological archetypes, power hierarchies, and key relationship contracts.",
        [
            ("Cosmology & Narrative Structure", cosmology_files),
            ("Key Contracts & Synopses", root_extras),
        ]
    )
    out = OUTPUT_DIR / "COSMOLOGY_AND_STRUCTURE_MASTER.md"
    out.write_text(content, encoding='utf-8')
    results.append(("COSMOLOGY_AND_STRUCTURE_MASTER.md", len(content)))
    src_count = len(cosmology_files) + len(root_extras)
    print(f"  ✓ COSMOLOGY_AND_STRUCTURE_MASTER.md ({len(content):,} chars, {src_count} source files)")

    # ─── 4. SIN_EATER_ARC_MASTER.md ───
    sin_eater_files = collect_recursive('Season 1 Arcs')

    content = build_master_section(
        "Battle Eternal — Sin-Eater Arc (Season 1)",
        "Complete Sin-Eater / Scapegoat Protocol arc documentation including "
        "corporate hierarchy, narrative storylines, structure, and mythic context.",
        [("Sin-Eater Arc Documents", sin_eater_files)]
    )
    out = OUTPUT_DIR / "SIN_EATER_ARC_MASTER.md"
    out.write_text(content, encoding='utf-8')
    results.append(("SIN_EATER_ARC_MASTER.md", len(content)))
    print(f"  ✓ SIN_EATER_ARC_MASTER.md ({len(content):,} chars, {len(sin_eater_files)} source files)")

    # ─── 5. TEST_SCENES_MASTER.md ───
    scene_files = collect_files('Test Scenes')

    content = build_master_section(
        "Battle Eternal — Test Scene Scripts",
        "Visual novel scene scripts for production testing and reference. "
        "These are working drafts of key narrative moments.",
        [("Scene Scripts", scene_files)]
    )
    out = OUTPUT_DIR / "TEST_SCENES_MASTER.md"
    out.write_text(content, encoding='utf-8')
    results.append(("TEST_SCENES_MASTER.md", len(content)))
    print(f"  ✓ TEST_SCENES_MASTER.md ({len(content):,} chars, {len(scene_files)} source files)")

    # ─── 6. README.md (standalone copy) ───
    readme_path = VAULT_DIR / 'README.md'
    if readme_path.exists():
        content = read_and_clean(readme_path)
        out = OUTPUT_DIR / "README.md"
        out.write_text(content, encoding='utf-8')
        results.append(("README.md", len(content)))
        print(f"  ✓ README.md ({len(content):,} chars)")

    # ─── Summary ───
    total_chars = sum(c for _, c in results)
    print(f"\n{'='*60}")
    print(f"Generated: {len(results)} master section files")
    print(f"Total output: {total_chars:,} chars ({total_chars/1024:.1f} KB)")
    print(f"Output dir: {OUTPUT_DIR}")


if __name__ == '__main__':
    main()
