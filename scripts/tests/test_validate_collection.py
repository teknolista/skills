"""Exercise the collection gate against disposable Git inventories."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


VALIDATOR = Path(__file__).resolve().parents[1] / "validate_collection.py"


class CollectionValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.write("LICENSE", "fixture license\n")
        self.write("penta-pro/LICENSE", "fixture license\n")
        self.write("penta-pro/SKILL.md", "---\nname: penta-pro\ndescription: Test specification workflow\nlicense: MIT\nmetadata:\n  version: '1.0.0'\n---\n# Workflow\n")
        self.write("penta-pro/assets/process.md", "| Template version | 1.0.0 |\n")
        self.write("README.md", "# PentaPRO\n| [PentaPRO](#pentapro) | 1.0.0 |\nyour-project/.agents/skills/penta-pro/SKILL.md\n")

    def write(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    def check(self, expected=None):
        result = subprocess.run([sys.executable, str(VALIDATOR)], cwd=self.root,
                                text=True, capture_output=True)
        if expected is None:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn(expected, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_valid_collection_with_optional_host_metadata(self):
        self.write("penta-pro/agents/openai.yaml", 'interface:\n  display_name: "PentaPRO"\n  short_description: "Create useful project specifications"\n  default_prompt: "Use $penta-pro to specify this project."\n')
        self.check()

    def test_fenced_heading_cannot_supply_an_anchor(self):
        self.write("guide.md", "[Missing](#fake)\n```markdown\n# Fake\n```\n")
        self.check("missing anchor")

    def test_fenced_heading_does_not_shift_duplicate_anchor(self):
        self.write("guide.md", "~~~markdown\n# Real\n~~~\n# Real\n[Real](#real)\n[Missing](#real-1)\n")
        self.check("missing anchor")

    def test_real_duplicate_headings_and_code_examples(self):
        self.write("guide.md", "# Real\n# Real\n[Second](#real-1)\n```\n[Example](absent.md)\n```\n")
        self.check()

    def test_ignored_target_is_not_distributable(self):
        self.write(".gitignore", "private.md\n")
        self.write("private.md", "# Local only\n")
        self.write("guide.md", "[Invalid](private.md)\n")
        self.check("missing or outside collection")

    def test_package_link_cannot_escape_installed_directory(self):
        self.write("penta-pro/references/guide.md", "[Unavailable after standalone installation](../../README.md)\n")
        self.check("link is not portable in a standalone package")

    def test_package_cannot_link_to_an_absolute_checkout_path(self):
        asset = self.root / "penta-pro/assets/process.md"
        self.write("penta-pro/references/guide.md", f"[Unavailable after relocation]({asset})\n")
        self.check("link is not portable in a standalone package")

    def test_package_can_link_to_its_own_parent_resource(self):
        self.write("penta-pro/references/guide.md", "[Packaged template](../assets/process.md)\n")
        self.check()

    def test_metadata_cannot_contain_non_string_values(self):
        entry = self.root / "penta-pro/SKILL.md"
        entry.write_text(entry.read_text().replace("  version: '1.0.0'", "  version: '1.0.0'\n  tags: [spec]"))
        self.check("metadata keys and values must be strings")

    def test_catalog_version_must_match(self):
        target = self.root / "README.md"
        target.write_text(target.read_text().replace("1.0.0", "1.0.1"))
        self.check("README version mismatch")

    def test_duplicate_host_key_is_rejected(self):
        self.write("penta-pro/agents/openai.yaml", "interface: {}\ninterface: {}\n")
        self.check("duplicate mapping key")

    def test_host_prompt_must_invoke_its_owner(self):
        self.write("penta-pro/agents/openai.yaml", 'interface:\n  default_prompt: "Use $other-skill for this task."\n')
        self.check("default_prompt")

    def test_host_policy_requires_a_boolean(self):
        self.write("penta-pro/agents/openai.yaml", 'policy:\n  allow_implicit_invocation: "false"\n')
        self.check("allow_implicit_invocation")

    def test_host_icon_must_be_shipped_inside_package(self):
        self.write("penta-pro/agents/openai.yaml", 'interface:\n  icon_small: "../LICENSE"\n')
        self.check("icon_small")

    def test_valid_host_icon_and_explicit_policy(self):
        self.write("penta-pro/assets/icon.svg", '<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.write("penta-pro/agents/openai.yaml", 'interface:\n  icon_small: "./assets/icon.svg"\n  brand_color: "#123aBc"\npolicy:\n  allow_implicit_invocation: false\n')
        self.check()

    def test_host_mapping_shape_is_reported_without_crashing(self):
        self.write("penta-pro/agents/openai.yaml", 'interface: [unexpected]\n')
        self.check("interface must be a mapping")


if __name__ == "__main__":
    unittest.main()
