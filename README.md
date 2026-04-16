# tpqoa-3.13

This repository is a maintenance fork of [`yhilpisch/tpqoa`](https://github.com/yhilpisch/tpqoa).
It remains public as a narrow compatibility fork for newer Python runtimes, not as a primary public project.

## Status

- Maintenance fork
- Public for reference
- Not under active feature development

## Purpose Of This Fork

- Preserve a working copy of the upstream package while testing Python compatibility updates
- Keep local changes small and easy to diff against upstream
- Make the repository intent explicit so it does not read like a standalone flagship project

## When To Use It

Use this repository only if you need the specific compatibility behavior in this fork.

For the canonical package documentation, examples, and broader project context, use the upstream repository:
<https://github.com/yhilpisch/tpqoa>

## Installation

```bash
git clone git@github.com:itsklimov/tpqoa-3.13.git
cd tpqoa-3.13
python setup.py install
```

## Risk Note

This package interfaces with trading infrastructure. Validate behavior in a non-production environment before relying on it, and prefer the upstream project for authoritative documentation.
