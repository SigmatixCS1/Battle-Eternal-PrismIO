
---

# Recommended Obsidian Vault Structure for Battle Eternal

Here’s a structure that works very well for **large IPs, games, and narrative universes**.

```
Battle Eternal Vault
│
├── 00 SYSTEM
│   ├── Episode Generation System
│   ├── Scene Template
│   ├── Character Template
│   ├── RenPy Integration
│   └── Production Pipelines
│
├── 01 STORY
│   ├── Episodes
│   │   ├── Episode 0
│   │   ├── Episode 1
│   │   └── Episode 2
│   │
│   ├── Arcs
│   │   └── Season 1 Arc
│   │
│   └── Narrative Structures
│
├── 02 WORLD
│   ├── Cosmology
│   ├── Atlas
│   ├── Saint Radian
│   ├── Dark Hold
│   └── Orders / Houses
│
├── 03 CHARACTERS
│   ├── Alexander
│   ├── Sigmatix
│   ├── Selene
│   ├── Spencer
│   ├── DeMarco
│   └── etc
│
├── 04 VISUAL NOVEL
│   ├── RenPy Scripts
│   ├── Scene Scripts
│   ├── Choice Trees
│   └── Dialogue Files
│
├── 05 ART + MEDIA
│   ├── Midjourney Prompts
│   ├── Concept Art
│   ├── Locations
│   └── Characters
```

---

# Where the Episode Generation System Goes

Place it here:

```
00 SYSTEM
└── Episode Generation System.md
```

This file becomes your **master blueprint** for creating new episodes.

---

# What the Episode Generation System Does

It standardizes **how every episode is built**.

Instead of reinventing the structure every time, you just follow the template.

Each episode will automatically include:

```
Episode Metadata
Scene Index
Scene Cards
RenPy Labels
Asset Checklist
Choice Flags
Mystery Escalation
Episode Hook
```

---

# Episode Generation System (Vault Note)

Create a new Obsidian note called:

```
Episode Generation System
```

Paste this into it:

---

# Battle Eternal — Episode Generation System

## Purpose

This system standardizes how **every episode of Battle Eternal is structured**.

It ensures consistent pacing, scalable production, and easy integration with the **Ren’Py visual novel pipeline**.

Episodes follow a **nine-scene narrative framework** first established in Episode 0.

---

# Episode Structure Template

Each episode follows this structure:

```
Scene 1 — Mythic / Cosmology Opening
Scene 2 — Anomaly Event
Scene 3 — Human Witness Perspective
Scene 4 — Psychic / Supernatural Insight
Scene 5 — Elite / Power Structure Scene
Scene 6 — Protagonist Character Scene
Scene 7 — Institutional Environment
Scene 8 — Hidden Layer / Secret Revelation
Scene 9 — Global or Philosophical Epilogue
```

---

# Scene Card Template

Each scene is generated using this card:

```
Scene ID:
Scene Title:

Location:
POV Character:

Narrative Purpose:
Emotional Tone:

Key Characters:
Reveals:

Player Choices:

Art Assets Needed:
Music Mood:
```

---

# Episode Metadata Template

Every episode begins with metadata:

```
Episode:
Title:
Season:
Arc:

Primary Theme:
Secondary Themes:

Major Characters Present:
Mysteries Introduced:
Mysteries Advanced:
Mysteries Resolved:
```

---

# RenPy Episode Skeleton

Each episode can automatically generate a script skeleton:

```
label episode_X_start:

    jump scene_1

label scene_1:
    jump scene_2

label scene_2:
    jump scene_3

label scene_3:
    jump scene_4

label scene_4:
    jump scene_5

label scene_5:
    jump scene_6

label scene_6:
    jump scene_7

label scene_7:
    jump scene_8

label scene_8:
    jump scene_9

label scene_9:
    return
```

---

# Episode Production Workflow

When creating a new episode:

1. Generate episode metadata
    
2. Generate scene index
    
3. Create scene cards
    
4. Write scene scripts
    
5. Generate Midjourney prompts
    
6. Export Ren’Py script
    
7. Link Obsidian notes
    

---

# Episode 0 Example

```
Scene 1 — The Spiral
Scene 2 — Sigmatix Airport Anomaly
Scene 3 — Spencer
Scene 4 — Selene Encounter
Scene 5 — Sovereign Rail Elite
Scene 6 — Alexander & Grant
Scene 7 — Saint Radian Arrival
Scene 8 — The Dark Hold
Scene 9 — Eucharist of Silicon
```

---

# Advantages of the System

This structure allows Battle Eternal to scale easily across:

- Visual novel production
    
- Graphic novel scripting
    
- Animation adaptation
    
- Lore documentation
    
- AI-assisted writing
    

---

# Next Step

Now that the system exists, the next file we should generate is:

**Episode Template.md**

This will allow you to create a **new episode in 60 seconds** inside Obsidian.

---
