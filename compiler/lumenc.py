#!/usr/bin/env python3
import sys
import re

def compile_lumen_to_pacm(source: str) -> str:
  lines = [line.strip() for line in source.split('\n') if line.strip() and not line.strip().startswith('//')]
  pacm = []
  pacm.append("; Generated PACM from LUMEN")
  pacm.append("ORG WL_1620")
  pacm.append("MAIN:")

  i = 0 
  while i < len(lines):
    line = lines[i]

    if line.startswith("morph "):
      name = line.split()[1].split('(')[0]
      pacm.append(f"{name.upper()}:")
      i += 1
      continue

    if line.startswith("let "):
      var = line.split(" = ")[0].replace("let ", "").strip()
      expr = line.split(" = ")[1].replace(";", "").srtip()
      pacm.append(f"  ; let {var} = {expr}")
      i += 1
      continue

    if "threshold" in line or "if " in line:
      pacm.append("  C VTHRESH R_val R_out")
      i += 1
      continue

    if line.startswith("loop "):
      pacm.append("LOOP:")
      i += 1
      continue

    if "write" in line:
      pacm.append("  SW R_data \"output\" #1")
      i += 1
      continue

    pacm.append(f"  ; {line}")
    i += 1

  return "\n".join(pacm)

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python lumenc.py <input.lm> <output.pacm>")
    sys.exit(1)

  with open(sys.argv[1], "r") as f:
    source = f.read()

  pacm = compile_lumen_to_pacm(source)

  with open(sys.argv[2], "W") as f:
    f.write(pacm)

  print(f"Compiled {sys.argv[1]} -> {sys.argv[2]}")
