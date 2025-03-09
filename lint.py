# pylint: diable=missing-module-docstring
import sys
from pylint import lint
THESHOLD = 9
run = lint.Run(["hello.py"], exit=False)
score = run.linter.stats.global_note
if score < THESHOLD:
  print("Linter failed: Score < threshold value")
  sys.exit(1)
sys.exit(0)
