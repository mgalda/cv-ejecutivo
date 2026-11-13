"""Verifica la conservación literal y genera la matriz a partir del adjunto."""

import argparse
import hashlib
import re
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
SECTIONS = (
    (1, 12, "references/00-entrada.md", "Activación, fuente y objetivo"),
    (13, 128, "references/01-ajuste.md", "Ajuste, ATS, continuidad y revisión"),
    (129, 240, "references/02-preparacion.md", "STAR, investigación, simulación, diferenciación y salario"),
    (241, 256, "references/03-cierre.md", "CV final y formato"),
    (512, 535, "references/00-entrada.md", "Reglas generales, redacción y siguiente entrada"),
)
TEMPLATE = "assets/harvard-ats.tex"


def normalized(line):
    return line.strip().removeprefix("\\") if line.lstrip().startswith("\\##") else line.strip()


def verify(source):
    original = source.read_text(encoding="utf-8-sig").splitlines()
    targets = {
        path: (SKILL / path).read_text(encoding="utf-8").splitlines()
        for _, _, path, _ in SECTIONS
    }
    cursors = dict.fromkeys(targets, 0)
    rows = []
    covered = set()
    for start, end, path, stage in SECTIONS:
        for number in range(start, end + 1):
            covered.add(number)
            raw = original[number - 1]
            if not raw.strip():
                continue
            for index in range(cursors[path], len(targets[path])):
                if normalized(raw) == normalized(targets[path][index]):
                    break
            else:
                raise ValueError(f"Línea original {number} ausente o fuera de orden en {path}")
            cursors[path] = index + 1
            rows.append((number, path, index + 1, stage, raw.strip()))

    if original[256].strip() != "Utiliza la siguiente plantilla:":
        raise ValueError("Cambió la instrucción que precede a la plantilla")
    closing = targets["references/03-cierre.md"]
    template_link = next(
        index for index, line in enumerate(closing, 1)
        if line.startswith("Utiliza la siguiente plantilla") and f"../{TEMPLATE}" in line
    )
    rows.append((257, "references/03-cierre.md", template_link, "Plantilla vinculada", original[256]))
    if original[259:508] != (SKILL / TEMPLATE).read_text(encoding="utf-8").splitlines():
        raise ValueError("La plantilla cambió respecto del adjunto")
    rows.append(("260–508", TEMPLATE, "1–249", "Plantilla íntegra", "Coincidencia línea por línea"))
    covered.update(range(257, 509))
    unmatched = [i for i, line in enumerate(original, 1) if line.strip() and i not in covered]
    if unmatched:
        raise ValueError(f"Líneas no inventariadas: {unmatched}")
    for link in re.findall(r"\]\(([^)]+)\)", (SKILL / "SKILL.md").read_text(encoding="utf-8")):
        if not (SKILL / link).is_file():
            raise ValueError(f"Enlace de ejecución inválido: {link}")
    return rows


def markdown(rows, source):
    header = [
        "# Inventario y matriz de trazabilidad",
        "",
        "Cada párrafo no vacío del adjunto se localiza en su módulo. La plantilla se compara completa. "
        "Las referencias apuntan a líneas del adjunto original. Las filas de título organizan el inventario. "
        "Los verbos condicionales y requisitos documentales conservan su alcance original.",
        "",
        f"SHA-256 del adjunto: `{hashlib.sha256(source.read_bytes()).hexdigest()}`",
        "",
        "| Línea original | Implementación | Etapa | Instrucción o contenido preservado |",
        "|---|---|---|---|",
    ]
    for number, path, line, stage, content in rows:
        content = normalized(content).replace("|", "\\|")
        header.append(f"| {number} | [`{path}:{line}`](../{path}) | {stage} | {content} |")
    return "\n".join(header) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("adjunto", type=Path)
    parser.add_argument("--regenerar", action="store_true")
    args = parser.parse_args()
    rows = verify(args.adjunto)
    expected = markdown(rows, args.adjunto)
    matrix = Path(__file__).with_name("trazabilidad.md")
    if args.regenerar:
        matrix.write_text(expected, encoding="utf-8")
    elif matrix.read_text(encoding="utf-8") != expected:
        raise SystemExit("Matriz desactualizada. Revisa los cambios y regenera.")
    print(f"{len(rows)} filas trazadas y 249 líneas de plantilla verificadas")


if __name__ == "__main__":
    main()
