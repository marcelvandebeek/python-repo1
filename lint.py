# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name
# pylint: disable=trailing-newlines
# pylint: disable=trailing-whitespace
# pylint: disable=missing-final-newline

import sys
from pylint import lint
THESHOLD = 9
run = lint.Run(["hello.py"], exit=False)
score = run.linter.stats.global_note
if score < THESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)
sys.exit(0)
