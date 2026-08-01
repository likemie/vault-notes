"""Task-local wrapper for the bundled renderer with a CJK font in its temp HOME."""

import importlib.util
import os
import shutil
import sys
from pathlib import Path


RENDERER = Path(
    "/Users/shaoyangwu/.codex/plugins/cache/openai-primary-runtime/"
    "documents/26.727.11326/skills/documents/render_docx.py"
)
CJK_FONT = Path("/Users/shaoyangwu/Library/Fonts/NotoSerifSC-Regular.ttf")

spec = importlib.util.spec_from_file_location("bundled_render_docx", RENDERER)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)

original_build_env = module._build_lo_env


def build_env_with_cjk_font(user_profile: str) -> dict:
    env = original_build_env(user_profile)
    fonts_dir = Path(user_profile) / ".fonts"
    fonts_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(CJK_FONT, fonts_dir / CJK_FONT.name)
    env["SAL_FONTPATH"] = str(fonts_dir)
    env["FONTCONFIG_PATH"] = str(fonts_dir)
    return env


module._build_lo_env = build_env_with_cjk_font
module.main()
